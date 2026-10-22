"""Ativa/remove somente o ensaio sintético de Despesas 4.1/4.2/4.3, sem usar Git."""
from __future__ import annotations

import argparse
import datetime
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "dist/Portal-da-Transparencia/Despesas/index.html"
SOURCE = ROOT / "dados-entrada/testes-serigy/despesas-sinteticas.json"
BASE = SOURCE.with_name("despesas-base-sem-dados.json")
WARNING = "DADOS SINTÉTICOS PARA TESTE DO SERIGY — NÃO REPRESENTAM DESPESAS DO SERGIPEPREVIDÊNCIA"
FIELDS = ["unidadeDespesa", "funcaoDespesa", "subFuncaoDespesa", "categoriaDespesa", "grupoDespesa", "elementoDespesa", "fonteRecursosDespesa"]
EMPENHO_FIELDS = ["credorEmpenho", "valorEmpenhoIndividual", "objetoEmpenho", "modalidadeEmpenho", "numeroProcedimento"]
BLOCKS = ("totais", "classificacao", "empenhos")


def block(document: str, name: str) -> str:
    match = re.search(r'<section\b[^>]*\bid="' + name + r'"[^>]*>[\s\S]*?</section>', document)
    if not match:
        raise ValueError(f"Bloco ausente: {name}")
    return match[0]


def tag(document: str, identifier: str, attributes: dict, remove=()) -> str:
    pattern = r'<[^<>]*\bid="' + re.escape(identifier) + r'"[^<>]*>'
    def replace(match):
        value = match[0]
        for key in list(attributes) + list(remove):
            value = re.sub(r'\s+' + re.escape(key) + r'(?:="[^"]*")?(?=[\s>])', '', value, flags=re.I)
        return value[:-1] + ''.join(' ' + key + '="' + html.escape(str(item), quote=True) + '"' for key, item in attributes.items()) + '>'
    result, count = re.subn(pattern, replace, document, count=1)
    if count != 1:
        raise ValueError(f"Elemento ausente: {identifier}")
    return result


def load_source() -> dict:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    if data.get("natureza") != "sintetica" or data.get("aviso") != WARNING:
        raise ValueError("Fonte sem identificação sintética obrigatória")
    datetime.date.fromisoformat(data["atualizacao_pagina_teste"])
    for name in BLOCKS:
        if not data[name]:
            raise ValueError("Conjunto sintético vazio")
        for row in data[name]:
            if str(row["codigo_uo"]) not in data["uos"] or not 1 <= row["mes"] <= 12:
                raise ValueError("UO ou mês inválido na fonte sintética")
            required = ["unidade", "valorEmpenhado", "valorLiquidado", "valorPago"] if name == "totais" else FIELDS
            if name == "empenhos":
                required = ["unidade", "numero_empenho", "credor_documento"] + EMPENHO_FIELDS
            if not all(str(row.get(key, "")).strip() for key in required):
                raise ValueError("Campo ausente na fonte sintética")
    keys = [(r["exercicio"], r["codigo_uo"], r["numero_empenho"]) for r in data["empenhos"]]
    if len(keys) != len(set(keys)):
        raise ValueError("Empenho sintético duplicado na mesma UO/exercício")
    if any(not r["numero_empenho"].startswith("TESTE-EMP-") or "SINTÉTICO" not in r["credorEmpenho"] or not r["credor_documento"].startswith("CPF/CNPJ FICTÍCIO TESTE-") for r in data["empenhos"]):
        raise ValueError("Empenhos de ensaio exigem identificadores e credores inequivocamente fictícios")
    return data


def render_block(base: str, name: str, data: dict) -> str:
    prefix = "despesas-" + name
    rows = data[name]
    esc = lambda value: html.escape(str(value), quote=True)
    result = tag(base, name, {"data-despesas-sinteticas": "true", "data-aviso-sintetico": WARNING})
    notice = '<p id="' + prefix + '-aviso" class="section-availability" role="note"><strong>' + esc(WARNING) + '</strong></p>'
    result = re.sub(r'<p>[\s\S]*?</p>', lambda _: notice, result, count=1)
    result = tag(result, prefix + "-filtro", {"serigyItem": "filtroPesquisa", "aria-describedby": prefix + "-status " + prefix + "-aviso"})
    result = re.sub(r'\s+disabled(?=[\s>])', '', result)
    years = '<option value="">Todos os exercícios sintéticos</option>' + ''.join('<option value="' + str(year) + '" serigyValue="' + str(year) + '">' + str(year) + '</option>' for year in sorted({r["exercicio"] for r in rows}, reverse=True))
    result = re.sub(r'(<select id="' + prefix + r'-ano"[^>]*>)[\s\S]*?(</select>)', lambda m: m[1] + years + m[2], result)
    result = tag(result, prefix + "-ano", {"serigyItem": "historicoExercicio"})
    units = '<option value="">Todas as unidades sintéticas</option>' + ''.join('<option value="' + esc(code) + '">' + esc(label) + '</option>' for code, label in data["uos"].items())
    result = re.sub(r'(<select id="' + prefix + r'-uo"[^>]*>)[\s\S]*?(</select>)', lambda m: m[1] + units + m[2], result)
    if name == "classificacao":
        elements = '<option value="">Todos os elementos sintéticos</option>' + ''.join('<option value="' + esc(value) + '">' + esc(value) + '</option>' for value in sorted({r["elementoDespesa"] for r in rows}))
        result = re.sub(r'(<select id="' + prefix + r'-elemento"[^>]*>)[\s\S]*?(</select>)', lambda m: m[1] + elements + m[2], result)
    rendered = []
    for row in rows:
        if name == "totais":
            values = [("", row["unidade"]), ("", row["exercicio"]), ("", row["mes"])] + [(key, row[key]) for key in ("valorEmpenhado", "valorLiquidado", "valorPago")]
        elif name == "classificacao":
            values = [(FIELDS[0], row[FIELDS[0]]), ("", row["exercicio"]), ("", row["mes"])] + [(key, row[key]) for key in FIELDS[1:]]
        else:
            values = [("", row["unidade"]), ("", row["exercicio"]), ("", row["mes"]), ("", row["numero_empenho"]), ("credorEmpenho", row["credorEmpenho"]), ("", row["credor_documento"])] + [(key, row[key]) for key in EMPENHO_FIELDS[1:]]
        rendered.append('<tr data-dado-sintetico="true" data-exercicio="' + esc(row["exercicio"]) + '" data-mes="' + esc(row["mes"]) + '" data-codigo-uo="' + esc(row["codigo_uo"]) + '" data-uo-confirmada="true">' + ''.join('<td' + (' serigyItem="' + key + '"' if key else '') + '>' + esc(value) + '</td>' for key, value in values) + '</tr>')
    result = re.sub(r'<tbody>[\s\S]*?</tbody>', lambda _: '<tbody>\n' + '\n'.join(rendered) + '\n</tbody>', result, count=1)
    result = tag(result, prefix + "-resultados", {}, remove=("hidden",))
    result = tag(result, prefix + "-tabela", {"aria-describedby": prefix + "-aviso"})
    result = tag(result, prefix + "-csv", {"serigyItem": "salvarRelatorio", "serigyValue": "csv", "aria-describedby": prefix + "-aviso"})
    result = result.replace("Baixar recorte em CSV — indisponível", "Baixar recorte sintético em CSV")
    result = re.sub(r'(<p id="' + prefix + r'-status"[^>]*>)[\s\S]*?(</p>)', lambda m: m[1] + str(len(rows)) + ' registros sintéticos disponíveis para ensaio técnico.' + m[2], result)
    result = tag(result, prefix + "-atualizacao", {"serigyItem": "dataUltimaAtualizacao"}, remove=("hidden",))
    date = data["atualizacao_pagina_teste"]
    label = datetime.date.fromisoformat(date).strftime("%d/%m/%Y")
    result = re.sub(r'(<div id="' + prefix + r'-atualizacao"[^>]*>)[\s\S]*?(</div>)', lambda m: m[1] + 'Conjunto sintético de teste preparado em <time datetime="' + date + '">' + label + '</time>. Esta não é a data de atualização de despesas oficiais.' + m[2], result)
    return result


def render(document: str, baseline: dict, data: dict, active: bool) -> str:
    for name in BLOCKS:
        current = block(document, name)
        if 'data-despesas-sinteticas="true"' not in current and current != baseline[name]:
            raise ValueError("Bloco alterado fora do modo sintético; recusado sobrescrever conteúdo")
        document = document.replace(current, render_block(baseline[name], name, data) if active else baseline[name], 1)
    return document


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--ativar", action="store_true")
    action.add_argument("--desativar", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = load_source()
    original = PAGE.read_bytes().decode("utf-8")
    newline = "\r\n" if "\r\n" in original else "\n"
    document = original.replace("\r\n", "\n")
    if not BASE.exists():
        if not args.ativar:
            parser.error("Base sem dados não foi preparada")
        baseline = {name: block(document, name) for name in BLOCKS}
        if any('data-despesas-sinteticas' in value or re.search(r'<tbody>\s*<tr', value) for value in baseline.values()):
            parser.error("Só é permitido preparar a base a partir dos blocos sem dados")
        BASE.write_text(json.dumps(baseline, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    baseline = json.loads(BASE.read_text(encoding="utf-8"))
    active = args.ativar or args.check and 'data-despesas-sinteticas="true"' in document
    expected = render(document, baseline, data, active)
    if args.check:
        if document != expected:
            parser.error("HTML diverge da fonte/base sintética; confira antes de regenerar")
        print("CONFERÊNCIA OK: modo " + ("sintético ativo" if active else "sem dados sintéticos"))
    else:
        PAGE.write_bytes(expected.replace("\n", newline).encode("utf-8"))
        print("Modo sintético " + ("ativado: " + ", ".join(str(len(data[name])) + " " + name for name in BLOCKS) + "." if active else "desativado; blocos sem dados preservados."))


if __name__ == "__main__":
    main()
