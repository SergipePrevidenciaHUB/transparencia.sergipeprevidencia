#!/usr/bin/env python3
"""Prepara os arquivos estáticos de dist para deploy no GitHub Pages.

Copia dist para _site e, caso o deploy esteja em um subcaminho
(ex: /transparencia.sergipeprevidencia), ajusta os links absolutos
para que CSS, imagens, scripts e navegação funcionem perfeitamente.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
SITE = ROOT / "_site"
TEST_PAGES_BASE_PATH = "/transparencia.sergipeprevidencia"


def check_synthetic_content(base_path: str, allow: bool = False) -> None:
    """Bloqueia o ensaio de despesas antes de alterar a pasta de publicação."""
    found = []
    for path in DIST.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".html", ".csv", ".json"}:
            content = path.read_text(encoding="utf-8-sig").lower()
            if any(marker in content for marker in (
                "data-despesas-sinteticas", "data-dado-sintetico",
                "dados sintéticos para teste do serigy",
            )):
                found.append(path.relative_to(DIST).as_posix())
    if not found:
        return
    normalized = "/" + base_path.strip().strip("/")
    if not allow or normalized != TEST_PAGES_BASE_PATH or (DIST / "CNAME").exists():
        raise ValueError(
            "Publicação oficial bloqueada: dados sintéticos de Despesas presentes. "
            "Execute tools/preparar_teste_despesas.py --desativar. "
            "O ensaio só pode ser preparado com --permitir-dados-sinteticos, "
            "na base /transparencia.sergipeprevidencia e sem CNAME. "
            "Arquivos: " + ", ".join(found)
        )

def adjust_html(content: str, base_path: str) -> str:
    """Ajusta href="/" e src="/" para prefixar com base_path, ignorando URLs protocol-relative //."""
    clean_base = "/" + base_path.strip("/")
    
    # Substitui href="/..." exceto href="//..."
    def replace_href(match: re.Match[str]) -> str:
        url = match.group(1)
        if url.startswith("//"):
            return match.group(0)
        return f'href="{clean_base}{url}"'

    def replace_src(match: re.Match[str]) -> str:
        url = match.group(1)
        if url.startswith("//"):
            return match.group(0)
        return f'src="{clean_base}{url}"'

    content = re.sub(r'href="(/[^"]*)"', replace_href, content)
    content = re.sub(r'src="(/[^"]*)"', replace_src, content)
    return content


def adjust_js(content: str, base_path: str) -> str:
    """Ajusta a lista de páginas de busca no site.js."""
    clean_base = "/" + base_path.strip("/")
    # Ajusta searchPages
    pattern = r'const searchPages = \[\s*([\s\S]*?)\s*\];'
    match = re.search(pattern, content)
    if match:
        items = match.group(1)
        updated_items = re.sub(r'"(/[^"]*)"', rf'"{clean_base}\1"', items)
        content = content[:match.start(1)] + updated_items + content[match.end(1):]
    return content


def prepare(base_path: str = "", permitir_dados_sinteticos: bool = False) -> None:
    check_synthetic_content(base_path, permitir_dados_sinteticos)
    if SITE.exists():
        shutil.rmtree(SITE)
    shutil.copytree(DIST, SITE)

    # Remove eventuais fragmentos HTML que não sejam páginas completas
    for frag in SITE.rglob("portarias*.html"):
        frag.unlink()

    base_path = base_path.strip().strip("/")
    if not base_path:
        print(f"Deploy preparado em {SITE} na raiz do domínio (sem subcaminho).")
        return

    print(f"Ajustando caminhos para base_path: /{base_path}")
    for html_file in SITE.rglob("*.html"):
        original = html_file.read_text(encoding="utf-8")
        updated = adjust_html(original, base_path)
        if updated != original:
            html_file.write_text(updated, encoding="utf-8")

    site_js = SITE / "assets" / "js" / "site.js"
    if site_js.exists():
        original_js = site_js.read_text(encoding="utf-8")
        updated_js = adjust_js(original_js, base_path)
        if updated_js != original_js:
            site_js.write_text(updated_js, encoding="utf-8")

    print(f"Deploy preparado com sucesso em {SITE} com prefixo /{base_path}.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-path", default="", help="Subcaminho base (ex: /transparencia.sergipeprevidencia)")
    parser.add_argument("--permitir-dados-sinteticos", action="store_true", help="Permite somente o ensaio na base fixa do GitHub Pages de teste, sem CNAME")
    args = parser.parse_args()
    try:
        prepare(args.base_path, args.permitir_dados_sinteticos)
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
