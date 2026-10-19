#!/usr/bin/env python3
"""Importa CSV, XLS, XLSX ou JSON e atualiza as tabelas estáticas do protótipo.

Uso:
  python tools/importar_dados.py receitas arquivo.xlsx
  python tools/importar_dados.py estagiarios arquivo.csv

O arquivo de receitas deve possuir ano, mês, valor previsto e valor arrecadado.
O arquivo de estagiários deve possuir nome, data de contratação e data de término.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import unicodedata
from datetime import datetime
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


def normalize(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value)).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def load_table(path: Path) -> pd.DataFrame:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(path, dtype=str, sep=None, engine="python")
    if suffix in {".xls", ".xlsx"}:
        return pd.read_excel(path, dtype=str)
    if suffix == ".json":
        return pd.read_json(path, dtype=False).astype(str)
    raise ValueError("Formato não aceito. Utilize CSV, XLS, XLSX ou JSON.")


def rename_columns(df: pd.DataFrame, aliases: dict[str, set[str]]) -> pd.DataFrame:
    normalized = {column: normalize(column) for column in df.columns}
    rename: dict[str, str] = {}
    for target, possibilities in aliases.items():
        match = next((original for original, norm in normalized.items() if norm in possibilities), None)
        if match is not None:
            rename[match] = target
    return df.rename(columns=rename)


def require_columns(df: pd.DataFrame, fields: list[str]) -> None:
    missing = [field for field in fields if field not in df.columns]
    if missing:
        raise ValueError("Colunas obrigatórias não identificadas: " + ", ".join(missing))


def parse_date(value: object) -> str:
    text = str(value).strip()
    if not text or text.lower() in {"nan", "nat", "-", "—"}:
        raise ValueError("Foi encontrada data vazia. Complete a informação antes de gerar a página.")
    parsed = pd.to_datetime(text, dayfirst=True, errors="coerce")
    if pd.isna(parsed):
        raise ValueError(f"Data inválida: {text}")
    return parsed.strftime("%d/%m/%Y")


def parse_currency(value: object) -> float:
    text = str(value).replace("R$", "").replace("\xa0", "").replace(" ", "").strip()
    if not text or text.lower() == "nan":
        raise ValueError("Foi encontrado valor monetário vazio.")
    if "," in text:
        text = text.replace(".", "").replace(",", ".")
    return float(text)


def brl(value: float) -> str:
    base = f"{value:,.2f}"
    return "R$ " + base.replace(",", "X").replace(".", ",").replace("X", ".")


def replace_block(page: Path, start: str, end: str, rows: str) -> None:
    content = page.read_text(encoding="utf-8")
    pattern = re.compile(rf"({re.escape(start)}).*?({re.escape(end)})", re.S)
    if not pattern.search(content):
        raise ValueError(f"Marcadores de importação não encontrados em {page}")
    replacement = f"{start}\n{rows}\n          {end}"
    page.write_text(pattern.sub(replacement, content), encoding="utf-8")


def import_revenues(df: pd.DataFrame) -> None:
    aliases = {
        "ano": {"ano", "exercicio"},
        "mes": {"mes", "mes_referencia", "competencia"},
        "valor_previsto": {"valor_previsto", "valor_previsto_r", "previsao", "receita_prevista"},
        "valor_arrecadado": {"valor_arrecadado", "valor_arrecadado_r", "realizacao", "receita_realizada"},
    }
    df = rename_columns(df, aliases)
    require_columns(df, ["ano", "mes", "valor_previsto", "valor_arrecadado"])
    month_map = {
        "1": ("01", "Janeiro"), "01": ("01", "Janeiro"), "janeiro": ("01", "Janeiro"),
        "2": ("02", "Fevereiro"), "02": ("02", "Fevereiro"), "fevereiro": ("02", "Fevereiro"),
        "3": ("03", "Março"), "03": ("03", "Março"), "marco": ("03", "Março"),
        "4": ("04", "Abril"), "04": ("04", "Abril"), "abril": ("04", "Abril"),
        "5": ("05", "Maio"), "05": ("05", "Maio"), "maio": ("05", "Maio"),
        "6": ("06", "Junho"), "06": ("06", "Junho"), "junho": ("06", "Junho"),
        "7": ("07", "Julho"), "07": ("07", "Julho"), "julho": ("07", "Julho"),
        "8": ("08", "Agosto"), "08": ("08", "Agosto"), "agosto": ("08", "Agosto"),
        "9": ("09", "Setembro"), "09": ("09", "Setembro"), "setembro": ("09", "Setembro"),
        "10": ("10", "Outubro"), "outubro": ("10", "Outubro"),
        "11": ("11", "Novembro"), "novembro": ("11", "Novembro"),
        "12": ("12", "Dezembro"), "dezembro": ("12", "Dezembro"),
    }
    records = []
    rows = []
    for _, row in df.iterrows():
        year = str(row["ano"]).strip().replace(".0", "")
        month_key = normalize(row["mes"]).lstrip("0") or "0"
        if month_key not in month_map:
            month_key = str(row["mes"]).strip().lower()
        if month_key not in month_map:
            raise ValueError(f"Mês inválido: {row['mes']}")
        month_number, month_name = month_map[month_key]
        expected = parse_currency(row["valor_previsto"])
        collected = parse_currency(row["valor_arrecadado"])
        records.append({"mes": month_name, "mes_numero": month_number, "ano": int(year), "valor_previsto": expected, "valor_arrecadado": collected})
        rows.append(f'          <tr data-year="{html.escape(year)}" data-month="{month_number}"><td>{month_name}</td><td>{year}</td><td class="money" serigyItem="valorPrevistoReceita">{brl(expected)}</td><td class="money" serigyItem="valorArrecadadoReceita">{brl(collected)}</td></tr>')

    data_dir = DIST / "dados" / "receitas"
    data_dir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(records).to_csv(data_dir / "receitas.csv", index=False, encoding="utf-8-sig")
    (data_dir / "receitas.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    page = DIST / "Portal-da-Transparencia" / "Receitas" / "PrevistaArrecada" / "index.html"
    replace_block(page, "<!-- DADOS_RECEITAS_INICIO -->", "<!-- DADOS_RECEITAS_FIM -->", "\n".join(rows))


def import_interns(df: pd.DataFrame) -> None:
    aliases = {
        "nome_completo": {"nome", "nome_completo", "estagiario"},
        "data_contratacao": {"data_contratacao", "data_admissao", "admissao", "inicio_do_contrato"},
        "data_termino": {"data_termino", "fim_de_contrato", "fim_do_contrato", "termino_do_contrato"},
    }
    df = rename_columns(df, aliases)
    require_columns(df, ["nome_completo", "data_contratacao", "data_termino"])
    records = []
    rows = []
    for _, row in df.iterrows():
        name = str(row["nome_completo"]).strip()
        if not name or name.lower() == "nan":
            raise ValueError("Foi encontrado nome de estagiário vazio.")
        admission = parse_date(row["data_contratacao"])
        termination = parse_date(row["data_termino"])
        year = admission[-4:]
        records.append({"nome_completo": name, "data_contratacao": admission, "data_termino": termination, "ano_contratacao": int(year)})
        rows.append(f'          <tr data-year="{year}"><td serigyItem="nomeEstagiario">{html.escape(name)}</td><td serigyItem="admissaoEstagiario">{admission}</td><td serigyItem="terminoEstagiario">{termination}</td></tr>')

    data_dir = DIST / "dados" / "recursos-humanos"
    data_dir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(records).to_csv(data_dir / "estagiarios.csv", index=False, encoding="utf-8-sig")
    (data_dir / "estagiarios.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    page = DIST / "Portal-da-Transparencia" / "RecursosHumanos" / "Estagiarios" / "index.html"
    replace_block(page, "<!-- DADOS_ESTAGIARIOS_INICIO -->", "<!-- DADOS_ESTAGIARIOS_FIM -->", "\n".join(rows))


def main() -> None:
    parser = argparse.ArgumentParser(description="Importador local do protótipo PETP 2026")
    parser.add_argument("tipo", choices=["receitas", "estagiarios"])
    parser.add_argument("arquivo", type=Path)
    args = parser.parse_args()
    if not args.arquivo.exists():
        raise SystemExit(f"Arquivo não encontrado: {args.arquivo}")
    frame = load_table(args.arquivo)
    if args.tipo == "receitas":
        import_revenues(frame)
    else:
        import_interns(frame)
    print(f"Importação concluída em {datetime.now():%d/%m/%Y %H:%M}.")
    print("Revise os dados gerados e execute: python tools/validar_prototipo.py")


if __name__ == "__main__":
    main()
