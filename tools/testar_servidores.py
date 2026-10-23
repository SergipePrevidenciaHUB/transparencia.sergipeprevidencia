"""Concilia a relação nominal publicada com todas as linhas e campos da fonte atual."""
import csv
import json
import re
from decimal import Decimal
from collections import Counter
from html.parser import HTMLParser

from openpyxl import load_workbook
from integrar_servidores import SOURCE, PAGE, CSV, HEADERS, MONTHS, valid_date


class Table(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows, self.row, self.cell = [], None, None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'tr' and 'data-source-row' in attrs:
            self.row = [attrs, []]
        if tag == 'td' and self.row is not None:
            self.cell = [attrs, '']

    def handle_data(self, data):
        if self.cell is not None:
            self.cell[1] += data

    def handle_endtag(self, tag):
        if tag == 'td' and self.cell is not None:
            self.row[1].append(self.cell)
            self.cell = None
        if tag == 'tr' and self.row is not None:
            self.rows.append(self.row)
            self.row = None


def main():
    book = load_workbook(SOURCE, read_only=True, data_only=False)
    try:
        raw = list(book['Plan1'].iter_rows(min_row=2, values_only=True))
    finally:
        book.close()
    def value(v):
        return '' if v is None or str(v).strip().upper() == 'VAZIO' else str(v)
    source = []
    for r in raw:
        parts = [('Função', value(r[6])), ('Cargo efetivo', value(r[7]))]
        role = '; '.join(label + ': ' + content for label, content in parts if content.strip())
        source.append([str(int(r[0])), str(int(r[1])), value(r[2]), role, value(r[3]), value(r[4]), value(r[5]), value(r[8])])
    report = json.loads((SOURCE.parents[2] / 'controle/remuneracao-conciliacao.json').read_text(encoding='utf-8'))
    links = {r['linha_relacao']: r['values'][4] for r in report['associacoes_confirmadas']}
    source = [v + [links.get(n, '')] for n, v in enumerate(source, 2)]
    assert len(source) == 1598 and len(links) == 1596
    assert {n for n,v in enumerate(source, 2) if not v[-1]} == {859, 860}
    parser = Table()
    text = PAGE.read_text(encoding='utf-8')
    parser.feed(text)
    assert len(parser.rows) == len(source)
    for number, ((attrs, cells), values) in enumerate(zip(parser.rows, source), 2):
        assert attrs['data-source-row'] == str(number)
        assert attrs['data-year'] == values[0] and attrs['data-month'] == values[1]
        assert json.loads(attrs['data-export-values']) == values
        expected = values.copy()
        expected[1] = MONTHS[int(expected[1])-1]
        if expected[8]:
            expected[8] = 'R$ ' + format(Decimal(expected[8].replace(',', '.')), ',.2f').replace(',', '_').replace('.', ',').replace('_', '.')
        assert cells[8][0]['serigyitem'] == 'salarioServidor'
        assert bool(cells[8][0].get('serigyempty')) == (not bool(values[8]))
        assert [v for _, v in cells] == [v if v.strip() or i == 6 else 'Não informado' for i, v in enumerate(expected)]
        for i, item in [(2, 'nomeServidor'), (3, 'cargoServidor'), (4, 'lotacaoServidor'), (6, 'exoneracaoServidor'), (7, 'cargaHoraria')]:
            present = bool(values[i].strip()) and (i != 6 or valid_date(values[i]))
            assert cells[i][0].get('serigyitem') == item
            assert bool(cells[i][0].get('serigyempty')) == (not present)
        assert cells[5][0].get('serigyitem') == ('admissaoServidor' if values[5].strip() else None), 'Equivalência institucional confirmada para esta relação'
    with CSV.open(encoding='utf-8-sig', newline='') as file:
        exported = list(csv.reader(file, delimiter=';'))
    assert exported == [HEADERS] + source
    years = Counter(v[0] for v in source)
    assert years == Counter(a['data-year'] for a, _ in parser.rows) == Counter(v[0] for v in exported[1:])
    assert 'VAZIO' not in text
    assert text.count('serigyItem="dataUltimaAtualizacao"') == 1
    assert 'datetime="2026-10-22">22/10/2026</time>' in text
    nominal = re.search(r'<section aria-labelledby="titulo-vinculos">.*?</section>', text, re.S)[0]
    assert nominal.count('serigyItem="salarioServidor"') == 1598
    print(json.dumps({'registros': len(source), 'por_ano': dict(years), 'conciliacao_celulas_HTML_CSV': 'OK', 'funcoes_cargos_repeticoes': 'preservados', 'tabela_unica_com_remuneracao_e_ausencias_justificadas': True}, ensure_ascii=False))


if __name__ == '__main__':
    main()
