"""Concilia os cinco índices documentais com o consolidado e suas exclusões obrigatórias."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json
import re

from integrar_planejamento import BASE, CONFIG, SOURCE, PC, FISCAL


class Index(HTMLParser):
    def __init__(self):
        super().__init__()
        self.main = False
        self.anchors, self.rows, self.markers = [], [], Counter()
        self.row = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'main':
            self.main = True
            assert attrs['serigyschema'] == PC
        if not self.main:
            return
        if attrs.get('serigyitem'):
            self.markers[attrs['serigyitem']] += 1
        if tag == 'tr' and 'data-record' in attrs:
            self.row = (attrs, [])
        if tag == 'a':
            self.anchors.append(attrs)
            if self.row:
                self.row[1].append(attrs)

    def handle_endtag(self, tag):
        if tag == 'main':
            self.main = False
        if tag == 'tr' and self.row:
            self.rows.append(self.row)
            self.row = None


def main():
    data = json.loads(SOURCE.read_text(encoding='utf-8-sig'))
    summary = {}
    for route, (section, _, _, marker) in CONFIG.items():
        source = data['secoes'][section]
        text = (BASE / route / 'index.html').read_text(encoding='utf-8')
        parser = Index()
        parser.feed(text)
        assert text.count('Informações atualizadas em <time datetime="2026-10-21">21/10/2026</time>') == 1
        assert f'serigySchema="{FISCAL}" serigyItem="dataUltimaAtualizacao"' in text
        assert 'serigyLink' not in text
        assert not re.search(r'href="(?:#|null|None)"', text)
        if route == 'PlanoEstrategico':
            plans = [r for r in source if r['tipo'] == 'planoEstrategico']
            extra = [r for r in source if r['tipo'] != 'planoEstrategico']
            assert [a['href'] for a in parser.anchors] == [r['url'] for r in plans + extra]
            assert [a['href'] for a in parser.anchors if a.get('serigyitem') == marker] == [r['url'] for r in plans]
            assert parser.markers['filtroPesquisa'] == parser.markers['historicoExercicio'] == 0
            summary[route] = {'plano_institucional': len(plans), 'complementares': len(extra)}
            continue
        assert len(parser.rows) == len(source)
        expected_all = []
        for (attrs, links), row in zip(parser.rows, source):
            assert attrs['data-year'] == str(row['ano'])
            if row.get('unidade'):
                assert attrs['data-unit'] == row['unidade']
            if route == 'Balancetes':
                assert attrs['data-month'] == str(row['mes'])
                invalid_pdf = row['unidade'] == 'SergipePrevidência' and row['ano'] == 2023 and row['mes'] == 6
                expected = ([row['pdf']] if row.get('pdf') and not invalid_pdf else []) + ([row['editavel']] if row.get('editavel') else [])
                edits = [a for a in links if a.get('serigyitem') == 'salvarRelatorio']
                assert len(edits) == bool(row.get('editavel'))
                if edits:
                    assert edits[0]['href'] == row['editavel']
                    assert edits[0]['serigyvalue'] == Path(urlsplit(row['editavel']).path).suffix[1:].lower()
                if invalid_pdf:
                    assert row['pdf'] not in [a['href'] for a in links]
            elif route == 'TCE' and row['unidade'] == 'SergipePrevidência' and row['ano'] in (2022, 2023):
                expected = []
                assert all(a['href'] != row['url_origem_para_conferencia'] for a in links)
            else:
                expected = [row['url']] if row.get('url') else []
                assert all(a.get('serigyitem') == marker for a in links)
            assert [a['href'] for a in links] == expected
            expected_all += expected
        assert [a['href'] for a in parser.anchors] == expected_all
        assert parser.markers['historicoExercicio'] == 1
        assert parser.markers['filtroPesquisa'] == (0 if route == 'TCE' else 1)
        if route == 'BalancoGeral':
            assert '2026' not in {a['data-year'] for a, _ in parser.rows}
        summary[route] = {'registros': len(source), 'links': len(expected_all)}
    print(json.dumps({'conciliacao_integral': 'OK', 'schemas_e_exclusoes': 'OK', 'paginas': summary}, ensure_ascii=False))


if __name__ == '__main__':
    main()
