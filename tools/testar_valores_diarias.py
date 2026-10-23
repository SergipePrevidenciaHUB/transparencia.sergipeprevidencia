"""Concilia as 48 linhas e cada valor/cargo da tabela de diárias com o XLSX."""
from collections import Counter
from decimal import Decimal
from html.parser import HTMLParser
import re

from openpyxl import load_workbook
from integrar_valores_diarias import PAGE, SOURCE, NOTES, STATE, NATIONAL, INTERNATIONAL


class Table(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows, self.row, self.cell = [], None, None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'tr' and 'data-source-row' in attrs:
            self.row = [attrs, []]
        if tag == 'td' and self.row is not None:
            self.cell = ['', []]
        if self.cell is not None and 'serigyitem' in attrs:
            self.cell[1].append([attrs['serigyitem'], ''])

    def handle_data(self, data):
        if self.cell is not None:
            self.cell[0] += data
            if self.cell[1] and self.marked:
                self.cell[1][-1][1] += data

    @property
    def marked(self):
        return getattr(self, '_marked', False)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag == 'span':
            self._marked = False
        if tag == 'td' and self.cell is not None:
            self.row[1].append(self.cell)
            self.cell = None
        if tag == 'tr' and self.row is not None:
            self.rows.append(self.row)
            self.row = None


def main():
    # Coleta somente o texto dos spans marcados para comparar os valores separadamente.
    class ValuesTable(Table):
        def handle_starttag(self, tag, attrs):
            super().handle_starttag(tag, attrs)
            if dict(attrs).get('serigyitem') in ('valorEstadual', 'valorNacional', 'valorInternacional'):
                self._marked = True
    book = load_workbook(SOURCE, read_only=True, data_only=False)
    try:
        source = list(enumerate(book['base'].iter_rows(min_row=2, values_only=True), 2))
    finally:
        book.close()
    parser = ValuesTable()
    text = PAGE.read_text(encoding='utf-8')
    parser.feed(text)
    assert len(source) == len(parser.rows) == 48
    assert Counter(r[0] for _, r in source) == {2023: 12, 2024: 12, 2025: 12, 2026: 12}
    for (number, (year, kind, group, role, value)), (attrs, cells) in zip(source, parser.rows):
        assert attrs['data-source-row'] == str(number) and attrs['data-year'] == str(year)
        assert [v[0] for v in cells[:4]] == [str(year), kind, group, role]
        assert len(cells) == 5
        content, marked = cells[4]
        if kind == STATE and value == '-':
            assert content == '-' and not marked
        elif kind == STATE:
            expected = re.findall(r'R\$ [\d.,]+', value)
            assert marked == [['valorEstadual', v] for v in expected]
            assert 'Com pernoite:' in content and 'Sem pernoite:' in content
        else:
            marker = 'valorNacional' if kind == NATIONAL else 'valorInternacional'
            assert len(marked) == 1 and marked[0][0] == marker
            assert Decimal(marked[0][1].removeprefix('R$ ').replace('.', '').replace(',', '.')) == Decimal(str(value))
            if kind == INTERNATIONAL:
                assert 'R$' not in content and '€' in content and 'US$' in content
    assert text.count('serigyItem="dataUltimaAtualizacao"') == 1 and '22/10/2026' in text
    assert 'serigyLink' not in text
    assert '40.743' not in text and '30.956' not in text
    assert 'Anexo I' in text and '239/2023' in text
    url = re.search(r'id="decreto-valores-diarias" href="([^"]+)"', text)[1]
    assert url in NOTES.read_text(encoding='utf-8-sig')
    print('OK: 48 linhas, 12 por exercício, 16 por âmbito; cargos/grupos e cada valor conciliados; quatro sinais - sem marcação; moedas e URL preservadas.')


if __name__ == '__main__':
    main()
