"""Extrai texto de PDFs com marcação de página e preservação de layout."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pypdf import PdfReader


def extrair_documento(caminho: Path) -> tuple[str | None, str | None]:
    """Retorna o texto do PDF ou uma mensagem de erro adequada."""
    if not caminho.exists():
        return None, f"Arquivo não encontrado: {caminho}"
    if not caminho.is_file():
        return None, f"O caminho não é um arquivo: {caminho}"
    if caminho.suffix.lower() != ".pdf":
        return None, f"O arquivo não tem extensão PDF: {caminho}"

    try:
        with caminho.open("rb") as arquivo:
            cabecalho = arquivo.read(1024)
            if b"%PDF-" not in cabecalho:
                return None, f"O arquivo não parece ser um PDF: {caminho}"
            arquivo.seek(0)
            leitor = PdfReader(arquivo)
            if leitor.is_encrypted:
                return None, f"PDF protegido por senha; não foi possível abri-lo: {caminho}"

            paginas: list[str] = []
            encontrou_texto = False
            falhas = 0
            for numero, pagina in enumerate(leitor.pages, start=1):
                try:
                    texto = pagina.extract_text(extraction_mode="layout")
                except Exception:
                    try:
                        texto = pagina.extract_text()
                    except Exception:
                        texto = None
                        falhas += 1

                if texto and texto.strip():
                    encontrou_texto = True
                paginas.append(f"\n========== PÁGINA {numero} ==========\n\n{texto or ''}")

            if not encontrou_texto:
                return (
                    None,
                    "Nenhuma camada de texto pôde ser extraída. "
                    "O documento pode ser digitalizado e exigir OCR.",
                )

            resultado = f"========== DOCUMENTO: {caminho.name} =========="
            resultado += "\n" + "\n".join(paginas)
            if falhas:
                resultado += (
                    f"\n\n[AVISO: não foi possível extrair o texto de "
                    f"{falhas} página(s).]"
                )
            return resultado, None
    except Exception as erro:
        return None, f"Não foi possível abrir ou ler o PDF {caminho}: {erro}"


def criar_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Extrai texto de PDFs, preservando o layout quando possível e "
            "identificando cada página."
        ),
        epilog=(
            "Com vários PDFs, o conteúdo de cada documento é separado no "
            "terminal. --output aceita somente um PDF por vez; para extrair "
            "vários, omita --output e redirecione o terminal se desejar."
        ),
    )
    parser.add_argument("pdf", nargs="+", type=Path, help="caminho(s) dos PDFs")
    parser.add_argument(
        "--output",
        type=Path,
        help="grava em texto UTF-8 (permitido somente com um PDF)",
    )
    return parser


def main() -> int:
    # Terminais Windows com codificações legadas podem não representar todos
    # os caracteres extraídos; substituí-los evita interromper a impressão.
    for fluxo in (sys.stdout, sys.stderr):
        if hasattr(fluxo, "reconfigure"):
            fluxo.reconfigure(errors="replace")

    parser = criar_parser()
    args = parser.parse_args()

    if args.output is not None and len(args.pdf) != 1:
        parser.error("--output aceita exatamente um PDF; informe um único arquivo.")
    if args.output is not None and args.output.resolve() == args.pdf[0].resolve():
        parser.error("--output não pode apontar para o mesmo arquivo PDF de origem.")

    resultados: list[str] = []
    erros: list[str] = []
    for caminho in args.pdf:
        texto, erro = extrair_documento(caminho)
        if erro:
            erros.append(f"ERRO: {erro}")
        elif texto:
            resultados.append(texto)

    conteudo = "\n\n".join(resultados)
    if args.output is None:
        if conteudo:
            print(conteudo)
    else:
        try:
            args.output.write_text(conteudo + "\n", encoding="utf-8")
        except OSError as erro:
            erros.append(f"ERRO: não foi possível gravar {args.output}: {erro}")

    for erro in erros:
        print(erro, file=sys.stderr)
    return 1 if erros or not resultados else 0


if __name__ == "__main__":
    raise SystemExit(main())
