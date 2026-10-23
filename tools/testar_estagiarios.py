"""Concilia todas as células publicadas de estágio com o XLSX, sem gravar."""
import csv
from collections import Counter
from html.parser import HTMLParser

from integrar_estagiarios import CSV, HEADERS, MONTHS, PAGE, load


class Table(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows = []
        self.row = None
        self.cell = None

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
    import json
    source = load()
    parsed = Table()
    parsed.feed(PAGE.read_text(encoding='utf-8'))
    assert len(source) == len(parsed.rows) == 714
    assert Counter(v[0] for _, _, v in source) == {'2023': 54, '2024': 197, '2025': 242, '2026': 221}
    for (number, hired, values), (attrs, cells) in zip(source, parsed.rows):
        assert attrs['data-source-row'] == str(number)
        assert attrs['data-ano-contratacao'] == hired
        assert attrs['data-ano-relacao'] == values[0]
        assert attrs['data-mes-relacao'] == values[1]
        assert json.loads(attrs['data-export-values']) == values
        display = values.copy()
        display[1] = MONTHS[int(values[1])-1]
        display[5] = display[5] or 'Não informado'
        display[6] = display[6] or 'Não informado'
        assert [text for _, text in cells] == display
        assert cells[2][0]['serigyitem'] == 'nomeEstagiario'
        assert cells[4][0]['serigyitem'] == 'admissaoEstagiario'
        assert cells[5][0].get('serigyitem') == ('terminoEstagiario' if values[5] else None)
    with CSV.open(encoding='utf-8-sig', newline='') as file:
        data = list(csv.reader(file, delimiter=';'))
    assert data == [HEADERS] + [v for _, _, v in source]
    assert sum(not v[5] for _, _, v in source) == 605
    assert PAGE.read_text(encoding='utf-8').count('serigyItem="dataUltimaAtualizacao"') == 1
    assert 'datetime="2026-10-22">22/10/2026</time>' in PAGE.read_text(encoding='utf-8')
    print('OK: 714 registros e todas as células HTML/CSV; contagens anuais; contratação derivada; 605 términos sem marcação; ordem e repetições preservadas.')


if __name__ == '__main__':
    main()
