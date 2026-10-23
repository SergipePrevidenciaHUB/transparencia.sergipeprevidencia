"""Gera a consulta pública usando somente o JSON de pagamentos preparado."""
import argparse
from collections import Counter
from datetime import date
from decimal import Decimal
from html import escape
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'dados-entrada/contratos/ordem-cronologica-preparada.json'
PAGE = ROOT / 'dist/Portal-da-Transparencia/Contratos/OrdemCronologica/index.html'
SCHEMA = 'https://serigy.tce.se.gov.br/comum/contratos.html'
MONTHS = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
          'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
HEADERS = ['UG', 'Data de vencimento (liquidação)', 'Data de pagamento', 'Credor',
           'Valor pago ao credor (líquido)', 'Fonte de recursos', 'Categoria contratual',
           'Valor bruto', 'Retenções', 'CO', 'OB', 'Empenho', 'Documento do credor']
CPF = re.compile(r'(?<!\d)\d{3}\.\d{3}\.\d{3}-\d{2}(?!\d)')


def money(cents):
    sign = '-' if cents < 0 else ''
    whole, fraction = divmod(abs(cents), 100)
    return f'R$ {sign}{whole:,}'.replace(',', '.') + f',{fraction:02}'


def display_date(value):
    return date.fromisoformat(value).strftime('%d/%m/%Y')


def load():
    data = json.loads(SOURCE.read_text(encoding='utf-8-sig'))
    rows = data['registros']
    assert len(rows) == len({r['ob'] for r in rows}) == 464
    assert Counter(r['ano'] for r in rows) == {2023: 152, 2024: 112, 2025: 111, 2026: 89}
    assert Counter(r['categoria'] for r in rows) == {
        'Fornecimento de bens': 82, 'Locações': 4, 'Prestação de serviços': 378}
    assert data['serigy']['schema'] == SCHEMA
    assert data['data_atualizacao_portal'] == '2026-10-22'
    for r in rows:
        payment = date.fromisoformat(r['data_pagamento'])
        date.fromisoformat(r['data_vencimento'])
        assert (payment.year, payment.month) == (r['ano'], r['mes'])
        assert r['valor_bruto_centavos'] - r['retido_centavos'] == r['valor_pago_centavos']
        for field, cents in [('valor_pago', 'valor_pago_centavos'),
                             ('valor_bruto', 'valor_bruto_centavos'), ('retido', 'retido_centavos')]:
            assert Decimal(str(r[field])) * 100 == r[cents]
        # A projeção publica somente estes campos; nenhum rastreio/observação livre.
        text = '\n'.join(values(r))
        assert not CPF.search(text), 'CPF sem máscara na projeção pública.'
        digits = re.sub(r'\D', '', r['documento_publico'])
        assert len(digits) != 11, 'Documento de pessoa física sem máscara.'
    data['registros'] = sorted(rows, key=lambda r: tuple(r[k] for k in data['regra_ordenacao']))
    return data


def values(r):
    return [r['ug'], display_date(r['data_vencimento']), display_date(r['data_pagamento']),
            r['nome'], money(r['valor_pago_centavos']), r['fonte'], r['categoria'],
            money(r['valor_bruto_centavos']), money(r['retido_centavos']), r['co'], r['ob'],
            r['empenho'], r['documento_publico']]


def generate(document, data):
    rows = []
    items = {1: 'dataVencimento', 2: 'dataPagamento', 3: 'credor', 4: 'valorPagamento'}
    for r in data['registros']:
        cells = ''.join('<td' + (f' serigyItem="{items[i]}"' if i in items else '') + '>'
                        + escape(str(v)) + '</td>' for i, v in enumerate(values(r)))
        rows.append(f'<tr data-id="{escape(r["id"], quote=True)}" data-ano="{r["ano"]}" '
                    f'data-mes="{r["mes"]}" data-pago="{r["valor_pago_centavos"]}" '
                    f'data-bruto="{r["valor_bruto_centavos"]}" data-retido="{r["retido_centavos"]}">'
                    + cells + '</tr>')
    years = ''.join(f'<option value="{y}" serigyValue="{y}">{y}</option>'
                    for y in [2026, 2025, 2024, 2023])
    months = ''.join(f'<option value="{i}">{m}</option>' for i, m in enumerate(MONTHS, 1))
    sources = ''.join(f'<option value="{escape(s, quote=True)}">{escape(s)}</option>'
                      for s in sorted({r['fonte'] for r in data['registros']}))
    categories = ''.join(f'<option value="{escape(s, quote=True)}">{escape(s)}</option>'
                         for s in data['categorias_filtro'])
    totals = {k: sum(r[k + '_centavos'] for r in data['registros'])
              for k in ['valor_pago', 'valor_bruto', 'retido']}
    main = f'''<main id="conteudo" class="container" serigySchema="{SCHEMA}" data-ordem-reais="true">
    <h1>Ordem Cronológica</h1>
    <p class="lead">Consulte os pagamentos por fonte de recursos e categoria contratual.</p>
    <form id="filtro-ordem" class="filter-panel" role="search" aria-label="Consultar pagamentos" serigyItem="filtroPesquisa">
      <div class="field"><label for="ano-ordem">Exercício</label><select id="ano-ordem" name="ano" serigyItem="historicoExercicio" serigyExecuteWaitSection="ordemTabela"><option value="">Todos os exercícios</option>{years}</select></div>
      <div class="field"><label for="mes-ordem">Mês de pagamento</label><select id="mes-ordem" name="mes"><option value="">Todos os meses</option>{months}</select></div>
      <div class="field"><label for="fonte-ordem">Fonte de recursos</label><select id="fonte-ordem" name="fonte"><option value="">Todas as fontes</option>{sources}</select></div>
      <div class="field"><label for="categoria-ordem">Categoria contratual</label><select id="categoria-ordem" name="categoria"><option value="">Todas as categorias</option>{categories}</select></div>
      <div class="field"><label for="credor-ordem">Nome do credor</label><input type="search" id="credor-ordem" name="credor"></div>
      <div class="filter-actions"><button type="submit" serigyExecuteWaitSection="ordemTabela">Pesquisar</button><button type="reset" class="secondary" serigyClearForm>Limpar filtros</button></div>
    </form>
    <section id="resultados-ordem" serigyLoadSection="ordemTabela" aria-label="Resultado da consulta">
      <p id="contagem-ordem" role="status" aria-live="polite">464 pagamentos.</p>
      <div class="filter-panel" aria-label="Totais do recorte">
        <p>Valor pago (líquido): <strong id="total-pago-ordem">{money(totals['valor_pago'])}</strong></p>
        <p>Valor bruto: <strong id="total-bruto-ordem">{money(totals['valor_bruto'])}</strong></p>
        <p>Retenções: <strong id="total-retido-ordem">{money(totals['retido'])}</strong></p>
      </div>
      <div class="exports"><button type="button" id="exportar-ordem" serigyItem="salvarRelatorio" serigyValue="csv">Exportar CSV</button></div>
      <div class="table-wrap" role="region" aria-label="Tabela de pagamentos" tabindex="0"><table id="tabela-ordem">
        <caption>Pagamentos por fonte de recursos e categoria contratual</caption>
        <thead><tr>{''.join('<th scope="col">' + escape(h) + '</th>' for h in HEADERS)}</tr></thead>
        <tbody>{chr(10).join(rows)}</tbody>
      </table></div>
    </section>
    <p class="update-info">Informações atualizadas em <span serigyItem="dataUltimaAtualizacao">22/10/2026</span></p>
  </main>'''
    updated, count = re.subn(r'<main\b.*?</main>', lambda _: main, document, count=1, flags=re.S)
    assert count == 1
    updated = updated.replace(' class="awaiting-information"', '')
    updated = updated.replace('/assets/js/ordem-teste.js', '/assets/js/ordem-cronologica.js')
    return updated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = load()
    old = PAGE.read_text(encoding='utf-8')
    new = generate(old, data)
    if args.check:
        assert old == new, 'HTML difere da geração da fonte preparada.'
    else:
        PAGE.write_text(new, encoding='utf-8')
    print('OK: 464 pagamentos, 464 OBs únicas; 152/112/111/89 por exercício; geração '
          + ('conferida.' if args.check else 'concluída.'))


if __name__ == '__main__':
    main()
