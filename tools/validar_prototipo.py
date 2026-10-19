#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

EXPECTED = {
    "index.html": ["sitioOficial", "acessoPortal", "pesquisaConteudo", "acessibilidadeSimbolo", "acessibilidadeAltoContraste", "acessibilidadeRedimensionamentoTexto", "acessibilidadeCaminhoPaginas", "acessibilidadeMapaSite"],
    "Portal-da-Transparencia/Institucional/Informacoes/index.html": ["estruturaOrganizacional", "normaEstruturaOrganizacional", "acessibilidadeCaminhoPaginas"],
    "Portal-da-Transparencia/Receitas/PrevistaArrecada/index.html": ["valorPrevistoReceita", "valorArrecadadoReceita", "filtroPesquisa", "salvarRelatorio", "dataUltimaAtualizacao", "historicoExercicio"],
    "Portal-da-Transparencia/RecursosHumanos/Estagiarios/index.html": ["nomeEstagiario", "admissaoEstagiario", "terminoEstagiario", "filtroPesquisa", "salvarRelatorio", "dataUltimaAtualizacao", "historicoExercicio"],
}


def local_target(url: str) -> Path | None:
    parsed = urlparse(url)
    if parsed.scheme or parsed.netloc or url.startswith(("mailto:", "tel:", "#", "javascript:")):
        return None
    path = unquote(parsed.path)
    target = DIST / path.lstrip("/")
    if path.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target


errors: list[str] = []
html_files = sorted(DIST.rglob("*.html"))
for page in html_files:
    content = page.read_text(encoding="utf-8")
    rel = page.relative_to(DIST).as_posix()
    if '<html lang="pt-BR">' not in content:
        errors.append(f"{rel}: idioma pt-BR ausente")
    for attr in ("href", "src"):
        for value in re.findall(rf'{attr}="([^"]+)"', content):
            target = local_target(value)
            if target is not None and not target.exists():
                errors.append(f"{rel}: destino inexistente: {value}")

for rel, markers in EXPECTED.items():
    page = DIST / rel
    if not page.exists():
        errors.append(f"Página obrigatória inexistente: {rel}")
        continue
    content = page.read_text(encoding="utf-8")
    for marker in markers:
        if marker not in content:
            errors.append(f"{rel}: marcação ausente: {marker}")

if errors:
    print("VALIDAÇÃO COM PENDÊNCIAS")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print(f"VALIDAÇÃO LOCAL CONCLUÍDA: {len(html_files)} páginas HTML verificadas.")
print("Este resultado não substitui a execução oficial do Invoker do TCE/SE.")
