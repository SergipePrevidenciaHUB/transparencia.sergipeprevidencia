"""Atualiza a página existente de Receitas a partir do XLSX de teste."""
import contextlib
import csv
import io
import json
import re
from collections import defaultdict
from decimal import Decimal
from html import escape

from previa_receitas import ROOT, UNIDADES, gerar, moeda

PAGE = ROOT / 'dist/Portal-da-Transparencia/Receitas/PrevistaArrecada/index.html'
OUT = ROOT / 'dist/dados/receitas'
SCHEMA = 'https://serigy.tce.se.gov.br/comum/receitas.html'
MESES = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
LEVELS = [('categoria', 'Categoria Econômica'), ('origem', 'Origem'), ('especie', 'Espécie')]
FIELDS = ['codigo_uo', 'unidade', 'ano', 'mes', 'categoria', 'codigo_categoria', 'origem', 'codigo_origem', 'especie', 'codigo_especie', 'previsto', 'arrecadado']
AVISO = 'Receitas do SergipePrevidência por Unidade Orçamentária e competência.'


def reais(value):
    text = moeda(Decimal(value))
    sign = '-' if text.startswith('-') else ''
    inteiro, dec = text.lstrip('-').split('.')
    return 'R$ ' + sign + format(int(inteiro), ',').replace(',', '.') + ',' + dec


def total(rows, field):
    return sum((Decimal(r[field]) for r in rows), Decimal(0))


def annual_forecast(base):
    january = [r for r in base if r['mes'] == '1']
    if january:
        return str(total(january, 'previsto'))
    if base and base[0]['codigo_uo'] == '37403' and base[0]['ano'] == '2026':
        return '0'
    return None


def build_tree(details):
    """Um nó por UO/ano/classificação; índices apontam só para a base mensal."""
    nodes = {}
    references = {r['ano']: max(int(v['mes']) for v in details if v['ano'] == r['ano']) for r in details}
    for index, row in enumerate(details):
        prefix = (row['codigo_uo'], row['ano'])
        parent = None
        for level, (field, label) in enumerate(LEVELS, 1):
            prefix += (row['codigo_' + field],)
            node = nodes.setdefault(prefix, dict(key=prefix,parent=parent,level=level,
                code=row['codigo_' + field],description=row[field],label=label,
                codigo_uo=row['codigo_uo'],unidade=row['unidade'],ano=row['ano'],indices=[]))
            if node['description'] != row[field]:
                raise ValueError(f'Descrições divergentes para os mesmos códigos: {prefix}')
            node['indices'].append(index)
            parent = prefix
    ordered = sorted(nodes.values(),key=lambda n:(n['codigo_uo'],-int(n['ano']),tuple(int(c) for c in n['key'][2:])))
    for index,node in enumerate(ordered):
        node['id'] = f'receita-{index+1}'
        base = [details[i] for i in node['indices']]
        node['arrecadado'] = str(total(base,'arrecadado'))
        node['previsto_anual'] = annual_forecast(base)
        node['mes_referencia'] = references[node['ano']]
    for node in ordered:
        node['parent_id'] = nodes[node['parent']]['id'] if node['parent'] else ''
    return ordered


def render_rows(nodes,year):
    children = defaultdict(list)
    for n in nodes:
        children[n['parent_id']].append(n['id'])
    rows=[]
    for n in nodes:
        attrs=(f'id="{n["id"]}" data-level="{n["level"]}" data-parent-id="{n["parent_id"]}" '
            f'data-codigo-uo="{n["codigo_uo"]}" data-uo-confirmada="true" data-year="{n["ano"]}" '
            f'data-base-indices="{" ".join(map(str,n["indices"]))}" data-expanded="false"')
        description=escape(n['description'])
        if children[n['id']]:
            description=(f'<button type="button" class="receita-toggle" data-receita-toggle aria-expanded="false" aria-controls="{" ".join(children[n["id"]])}">'
                f'<span data-toggle-icon aria-hidden="true">▸</span><span>{description}</span><span class="receita-acao">Abrir</span></button>')
        pm=' serigyItem="valorPrevistoReceita"' if n['level']==3 and n['previsto_anual'] is not None else ''
        am=' serigyItem="valorArrecadadoReceita"' if n['level']==3 else ''
        forecast=reais(n['previsto_anual']) if n['previsto_anual'] is not None else '—'
        rows.append(f'<tr {attrs}{"" if n["level"]==1 and n["ano"]==year else " hidden"}>'
            f'<td class="receita-uo">{n["codigo_uo"]} — {escape(n["unidade"])}</td>'
            f'<td class="receita-descricao receita-nivel-{n["level"]}"><span class="receita-nivel">{n["label"]}</span>{description}</td>'
            f'<td>{n["ano"]}</td><td data-reference-label>{MESES[n["mes_referencia"]-1]}/{n["ano"]}</td><td><code>{escape(n["code"])}</code></td>'
            f'<td class="money"{pm}>{forecast}</td><td class="money" data-accum-value{am}>{reais(n["arrecadado"])}</td></tr>')
    return '\n'.join(rows)


def render_main(payload, nodes):
    details, annual = payload['classificacoes'], payload['previsao_anual']
    years = sorted({r['ano'] for r in details}, reverse=True)
    year = years[0]
    selected = [r for r in details if r['ano'] == year]
    forecast = total([r for r in annual if r['ano'] == year], 'previsao_anual')
    reference = max(int(r['mes']) for r in selected)
    reference_label = MESES[reference-1] + '/' + year
    year_options = ''.join(f'<option value="{y}" serigyValue="{y}">{y}</option>' for y in years)
    month_options = ''.join(f'<option value="{m:02d}">{name}</option>' for m, name in enumerate(MESES, 1))
    uo_options = ''.join(f'<option value="{code}">{code} — {name}</option>' for code, name in UNIDADES.items())
    data = json.dumps(payload, ensure_ascii=False).replace('<', '\\u003c')
    return f"""
    <h1>Receitas previstas e arrecadadas</h1>
    <p class="lead">Consulte as receitas por ano, mês e unidade.</p>
    <form class="filter-panel" id="receitasFiltro" data-uo-codes="37201 37401 37403" serigySchema="{SCHEMA}" serigyItem="filtroPesquisa">
      <div class="field"><label for="receita-ano">Ano</label><select id="receita-ano" name="ano" required serigyItem="historicoExercicio">{year_options}</select></div>
      <div class="field"><label for="receita-mes">Acumular até</label><select id="receita-mes" name="mes"><option value="">Todos os meses disponíveis</option>{month_options}</select></div>
      <div class="field"><label for="receita-uo">Unidade Orçamentária</label><select id="receita-uo" name="codigo_uo" data-uo-filter><option value="">Todas as unidades</option>{uo_options}</select></div>
      <div class="filter-actions"><button type="submit" serigyExecuteWaitSection="receitasResultados">Pesquisar</button><button class="secondary" type="reset" serigyClearForm>Limpar filtros</button></div>
    </form>
    <section id="receitasResultados" serigySchema="{SCHEMA}" serigyLoadSection="receitasResultados" aria-label="Resultado da consulta">
      <div class="receitas-totais" aria-live="polite">
        <div class="receitas-total"><h2>Previsão anual</h2><p id="receitasTotalPrevisto" class="receitas-valor" serigyItem="valorPrevistoReceita">{reais(forecast)}</p></div>
        <div class="receitas-total"><h2 id="receitasTituloArrecadado">Arrecadação acumulada até {reference_label}</h2><p id="receitasTotalArrecadado" class="receitas-valor" serigyItem="valorArrecadadoReceita">{reais(total(selected, 'arrecadado'))}</p><p id="receitasSomaBruta">Soma bruta, incluindo receitas intraorçamentárias.</p></div>
      </div>



      <div class="exports"><strong>Exportar:</strong><a href="/dados/receitas/receitas-integracao.csv" download serigyItem="salvarRelatorio" serigyValue="csv" data-receitas-export="csv">CSV</a> | <a href="/dados/receitas/receitas-integracao.json" download serigyItem="salvarRelatorio" serigyValue="json" data-receitas-export="json">JSON</a></div>

      <noscript><style>#receitaTabela tr[hidden]{{display:table-row}}</style></noscript>

      <p id="receitasVazio" hidden>Nenhum registro de arrecadação para o recorte selecionado.</p>

      <div class="table-wrap receitas-tabela" tabindex="0" role="region" aria-label="Tabela de receitas acumuladas, com rolagem horizontal"><table id="receitaTabela">
        <caption>Receitas acumuladas por UO, exercício e classificação</caption>
        <thead><tr><th scope="col">UO</th><th scope="col">Descrição da receita</th><th scope="col">Ano</th><th scope="col">Referência do acumulado</th><th scope="col">Código da receita</th><th scope="col">Previsão anual</th><th scope="col">Arrecadação acumulada</th></tr></thead>
        <tbody>
{render_rows(nodes, year)}
        </tbody>
      </table></div>
    </section>
    <div class="update-info" serigySchema="{SCHEMA}" serigyItem="dataUltimaAtualizacao">Informações atualizadas em <time datetime="2026-10-21">21/10/2026</time></div>
    <script type="application/json" id="receitasDados">{data}</script>"""


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Confere sem alterar HTML ou exportações publicados.')
    args = parser.parse_args()
    private = ROOT / 'trabalho/receitas-integracao'
    with contextlib.redirect_stdout(io.StringIO()):
        gerar(ROOT / 'dados-entrada/receitas/receitas-teste.xlsx', private)
    def read(name):
        with (private / name).open(encoding='utf-8-sig', newline='') as file:
            return list(csv.DictReader(file, delimiter=';'))
    details = [{k: r[k] for k in FIELDS if k != 'previsto_mes'} for r in read('classificacoes-origem.csv')]
    annual = [{k: r[k] for k in ('codigo_uo', 'unidade', 'ano', 'previsao_anual')} for r in read('previsao-anual.csv')]
    assert (len(details), len(annual), len(read('arrecadacao-mensal.csv'))) == (425, 9, 97)
    nodes = build_tree(details)
    scale = max(2, max(-Decimal(r[k]).as_tuple().exponent for r in details for k in ('previsto', 'arrecadado')))
    payload = dict(aviso=AVISO, metodo='Acumulado: somar registros mensais uma vez, ate a referencia; sem fechamento presumido.', escala_decimal=scale, previsao_anual=annual, classificacoes=details)
    page = PAGE.read_text(encoding='utf-8')
    page, count = re.subn(r'(<main\b[^>]*>).*?(</main>)', lambda m: m[1] + '\n    ' + render_main(payload, nodes).strip() + '\n  ' + m[2], page, count=1, flags=re.S)
    if count != 1:
        raise ValueError('Regiao de Receitas nao encontrada; pagina nao alterada.')
    css = '<link rel="stylesheet" href="/assets/css/receitas.css">'
    if css not in page:
        page = page.replace('<link rel="stylesheet" href="/assets/css/site.css">', '<link rel="stylesheet" href="/assets/css/site.css">\n  ' + css)
    OUT.mkdir(exist_ok=True, parents=True)
    json_content = json.dumps(payload, ensure_ascii=False, indent=2) + '\n'
    csv_fields=['tipo_recorte','ano_referencia','mes_referencia_acumulado']+[('mes_registro' if k=='mes' else 'previsto_na_origem' if k=='previsto' else 'arrecadado_no_mes' if k=='arrecadado' else k) for k in FIELDS]
    refs={r['ano']:max(int(v['mes']) for v in details if v['ano']==r['ano']) for r in details}
    buffer = io.StringIO(newline='')
    writer=csv.writer(buffer,delimiter=';')
    writer.writerow(csv_fields)
    for r in details:
        writer.writerow(['acumulado',r['ano'],f'{refs[r["ano"]]:02d}']+[r[k] for k in FIELDS])
    page = re.sub(r'[ \t]+$', '', page, flags=re.M)
    outputs = [(OUT / 'receitas-integracao.json', json_content, 'utf-8'),
               (OUT / 'receitas-integracao.csv', buffer.getvalue(), 'utf-8-sig'),
               (PAGE, page, 'utf-8')]
    for path, content, encoding in outputs:
        if args.check:
            assert path.read_text(encoding=encoding) == content.replace('\r\n', '\n'), f'Arquivo diverge da geração: {path.name}'
        else:
            with path.open('w', encoding=encoding, newline='' if path.suffix == '.csv' else None) as file:
                file.write(content)
    print(f'Integracao: 425 registros de base, 97 competencias por UO, 9 previsoes anuais; {len(nodes)} nos em uma tabela. Sem duplicacao nos totais/exportacoes.')


if __name__ == '__main__':
    main()
