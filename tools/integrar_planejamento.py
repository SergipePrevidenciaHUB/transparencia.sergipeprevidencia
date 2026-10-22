"""Alimenta somente 10.1/10.3/10.4/10.5/10.6; preserva RelatorioGestao."""
from pathlib import Path
from collections import Counter
from html import escape
from urllib.parse import urlsplit
import argparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'dados-entrada/planejamento/planejamento-prestacao-contas-consolidado.json'
BASE = ROOT / 'dist/Portal-da-Transparencia/PlanejamentoPrestacaoContas'
PC = 'https://serigy.tce.se.gov.br/comum/planejamento-prestacao-contas.html'
FISCAL = 'https://serigy.tce.se.gov.br/comum/gestao-fiscal-planejamento.html'
MONTHS = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
CONFIG = {
    'BalancoGeral': ('balancoGeral', 'Prestação de Contas (Balanço Geral)', 'balanco-geral', 'balancoGeralAnoAnterior'),
    'TCE': ('integraJulgamentoTCE', 'Julgamento pelo Tribunal de Contas', 'tce', 'integraJulgamentoTCE'),
    'RGF': ('RGF', 'Relatório de Gestão Fiscal (RGF)', 'rgf', 'RGF'),
    'PlanoEstrategico': ('planoEstrategico', 'Plano Estratégico Institucional', 'plano-estrategico', 'planoEstrategico'),
    'Balancetes': ('balanceteMensal', 'Balancetes Mensais', 'balancetes', 'balanceteMensal'),
}


def load():
    data = json.loads(SOURCE.read_text(encoding='utf-8-sig'))
    assert data['data_ultima_atualizacao_portal'] == '21/10/2026'
    return data


def pending_tce(row):
    return row.get('unidade') == 'SergipePrevidência' and row['ano'] in (2022, 2023)


def pending_pdf(row):
    return row['unidade'] == 'SergipePrevidência' and row['ano'] == 2023 and row['mes'] == 6


def link(url, title, item=None, fmt=None):
    if not url:
        return 'Não disponibilizado nesta relação'
    attrs = f' serigyItem="{item}"' if item else ''
    if fmt:
        attrs += f' serigyValue="{escape(fmt, quote=True)}"'
    return f'<a href="{escape(url, quote=True)}"{attrs}>{escape(title)}</a>'


def update(slug):
    return f'<div id="atualizacao-{slug}" class="update-info" serigySchema="{FISCAL}" serigyItem="dataUltimaAtualizacao">Informações atualizadas em <time datetime="2026-10-21">21/10/2026</time></div>\n    <p>A data acima refere-se à atualização desta relação no Portal.</p>'


def filter_form(route, rows, slug):
    fields = []
    years = sorted({r['ano'] for r in rows}, reverse=True)
    options = ''.join(f'<option value="{y}" serigyValue="{y}">{y}</option>' for y in years)
    fields.append(f'<div class="field"><label for="exercicio-{slug}">Exercício</label><select id="exercicio-{slug}" name="ano" serigyItem="historicoExercicio"><option value="">Todos</option>{options}</select></div>')
    units = sorted({r['unidade'] for r in rows if r.get('unidade')})
    if len(units) > 1:
        options = ''.join(f'<option value="{escape(u, quote=True)}">{escape(u)}</option>' for u in units)
        fields.append(f'<div class="field"><label for="unidade-{slug}">Unidade</label><select id="unidade-{slug}" name="unidade"><option value="">Todas as unidades</option>{options}</select></div>')
    if route == 'Balancetes':
        options = ''.join(f'<option value="{m}">{MONTHS[m-1]}</option>' for m in sorted({r['mes'] for r in rows}))
        fields.append(f'<div class="field"><label for="mes-{slug}">Mês de referência</label><select id="mes-{slug}" name="mes"><option value="">Todos</option>{options}</select></div>')
    # 10.3 não tem item filtroPesquisa: consulta adicional DT, sem inventar exigência.
    marker = '' if route == 'TCE' else ' serigyItem="filtroPesquisa"'
    return f'''<form id="filtro-{slug}" class="filter-panel" role="search" aria-label="Consultar documentos" data-planejamento-filter data-target="tabela-{slug}" serigySchema="{FISCAL}"{marker}>
      {''.join(fields)}
      <div class="filter-actions"><button type="submit" serigyExecuteWaitSection="tabela-{slug}">Pesquisar</button><button type="reset" class="secondary" serigyClearForm>Limpar filtros</button></div>
    </form>
    <p class="result-count" data-count-for="tabela-{slug}" aria-live="polite">{len(rows)} registro(s) encontrado(s).</p>'''


def render(route, data):
    key, title, slug, item = CONFIG[route]
    rows = data['secoes'][key]
    beginning = f'<main id="conteudo" class="container" serigySchema="{PC}">\n    <h1>{title}</h1>'
    if route == 'PlanoEstrategico':
        plan = [r for r in rows if r['tipo'] == 'planoEstrategico']
        complementary = [r for r in rows if r['tipo'] != 'planoEstrategico']
        content = '<section aria-labelledby="titulo-plano-institucional"><h2 id="titulo-plano-institucional">Plano institucional</h2><ul>' + ''.join('<li>' + link(r['url'], r['titulo'], item) + '</li>' for r in plan) + '</ul></section>'
        content += '<section aria-labelledby="titulo-materiais-complementares"><h2 id="titulo-materiais-complementares">Materiais complementares</h2><ul>' + ''.join('<li>' + link(r['url'], r['titulo']) + '</li>' for r in complementary) + '</ul></section>'
        return beginning + '\n    ' + content + '\n    ' + update(slug) + '\n  </main>'
    unit_column = any(r.get('unidade') for r in rows)
    headings = ['Exercício'] + (['Unidade'] if unit_column else [])
    if route == 'Balancetes':
        headings += ['Mês de referência', 'Balancete (PDF)', 'Formato editável']
    elif route == 'RGF':
        headings += ['Quadrimestre', 'Documento']
    else:
        headings += ['Documento']
    table_rows = []
    for index, row in enumerate(rows):
        attrs = f'data-record="{index}" data-year="{row["ano"]}"'
        if unit_column:
            attrs += f' data-unit="{escape(row["unidade"], quote=True)}"'
        cells = [str(row['ano'])] + ([escape(row['unidade'])] if unit_column else [])
        if route == 'Balancetes':
            attrs += f' data-month="{row["mes"]}"'
            pdf = None if pending_pdf(row) else row.get('pdf')
            edit = row.get('editavel')
            cells += [MONTHS[row['mes']-1], link(pdf, 'PDF', item)]
            if edit:
                fmt = Path(urlsplit(edit).path).suffix.lstrip('.').lower()
                anchor = link(edit, f'Editável ({fmt.upper()})', 'salvarRelatorio', fmt)
                # O editável de junho existe; o PDF desse mês não pode ser vinculado.
                cells.append(anchor if pdf else f'<span serigyItem="{item}">{anchor}</span>')
            else:
                cells.append('Não disponibilizado nesta relação')
        elif route == 'RGF':
            cells += [f'{row["quadrimestre"]}º quadrimestre', link(row.get('url'), row['titulo'], item)]
        elif route == 'TCE' and pending_tce(row):
            cells.append('Documento ainda não disponibilizado nesta relação')
        else:
            cells.append(link(row.get('url'), row['titulo'], item))
        table_rows.append(f'<tr {attrs}>' + ''.join(f'<td>{cell}</td>' for cell in cells) + '</tr>')
    return beginning + '\n    ' + filter_form(route, rows, slug) + f'''
    <div class="table-wrap"><table id="tabela-{slug}" serigyLoadSection="tabela-{slug}">
      <caption>{title} — documentos por período</caption>
      <thead><tr>{''.join(f'<th scope="col">{h}</th>' for h in headings)}</tr></thead>
      <tbody>
        {chr(10).join(table_rows)}
      </tbody>
    </table></div>
    {update(slug)}
  </main>'''


def stats(data):
    summary = {}
    for route, (key, _, _, _) in CONFIG.items():
        rows = data['secoes'][key]
        if route == 'Balancetes':
            pdf = sum(bool(r.get('pdf')) and not pending_pdf(r) for r in rows)
            edit = sum(bool(r.get('editavel')) for r in rows)
            summary[route] = {'registros': len(rows), 'PDF': pdf, 'editaveis': edit, 'links': pdf + edit, 'editaveis_ausentes': sum(not r.get('editavel') for r in rows)}
        else:
            available = sum(bool(r.get('url')) and not (route == 'TCE' and pending_tce(r)) for r in rows)
            summary[route] = {'registros': len(rows), 'documentos_ou_destinos': available, 'sem_vinculo': len(rows) - available}
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = load()
    for route in CONFIG:
        path = BASE / route / 'index.html'
        page = path.read_text(encoding='utf-8')
        page, count = re.subn(r'<main id="conteudo".*?</main>', lambda _: render(route, data), page, flags=re.S)
        assert count == 1
        page = page.replace('<body class="awaiting-information">', '<body>')
        if route != 'PlanoEstrategico' and '/assets/js/planejamento.js' not in page:
            page = page.replace('</head>', '  <script defer src="/assets/js/planejamento.js"></script>\n</head>')
        if args.check:
            assert path.read_bytes() == page.encode('utf-8'), f'Página divergente: {route}'
        else:
            path.write_bytes(page.encode('utf-8'))
    print(json.dumps(stats(data), ensure_ascii=False))


if __name__ == '__main__':
    main()
