"""Concilia as cinco colunas públicas com a fonte, incluindo vazios e repetições."""
import csv
import json
from collections import Counter
from html.parser import HTMLParser

from integrar_terceirizados import CSV, HEADERS, PAGE, load


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
    source = load()
    parsed = Table()
    text = PAGE.read_text(encoding='utf-8')
    parsed.feed(text)
    assert len(source) == len(parsed.rows) == 3009
    expected = {'2023': 661, '2024': 735, '2025': 875, '2026': 738}
    assert Counter(v[0] for _, v in source) == expected
    assert Counter(a['data-year'] for a, _ in parsed.rows) == expected
    for (number, values), (attrs, cells) in zip(source, parsed.rows):
        assert attrs['data-source-row'] == str(number)
        assert attrs['data-year'] == values[0] and attrs['data-month'] == values[1]
        assert json.loads(attrs['data-export-values']) == values
        assert len(cells) == 5
        assert [value for _, value in cells] == [v if v.strip() else 'Não informado' for v in values]
        for i, item in [(2, 'nomeTerceirizado'), (3, 'funcaoTerceirizado'), (4, 'empresaTerceirizado')]:
            assert cells[i][0].get('serigyitem') == (item if values[i].strip() else None)
    with CSV.open(encoding='utf-8-sig', newline='') as file:
        exported = list(csv.reader(file, delimiter=';'))
    assert exported == [HEADERS] + [v for _, v in source]
    assert Counter(v[0] for v in exported[1:]) == expected
    assert [(n, i) for n, values in source for i in (2, 3, 4) if not values[i].strip()] == [(954, 3), (1888, 2), (1963, 2)]
    assert text.count('serigyItem="dataUltimaAtualizacao"') == 1
    assert 'datetime="2026-10-22">22/10/2026</time>' in text
    assert all(label not in text.upper() for label in ('LOTAÇÃO', 'DATA DE ADMISSÃO', 'DATA DE DEMISSÃO'))
    print('OK: XLSX/HTML/CSV = 3009; anos 661/735/875/738; cinco colunas e todas as células conciliadas; três vazios preservados sem marcação; todas as empresas e repetições preservadas.')


if __name__ == '__main__':
    main()
