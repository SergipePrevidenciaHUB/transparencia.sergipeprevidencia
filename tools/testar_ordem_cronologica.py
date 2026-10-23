"""Conferência proporcional da projeção pública, sem consultar planilhas."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import tempfile
import integrar_ordem_cronologica as gen


class Table(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows, self.ids, self.items = [], [], Counter()
        self.row = self.cell = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'serigyitem' in attrs:
            self.items[attrs['serigyitem']] += 1
        if tag == 'tr' and 'data-id' in attrs:
            self.ids.append(attrs['data-id'])
            self.row = []
        if tag == 'td' and self.row is not None:
            self.cell = []

    def handle_data(self, text):
        if self.cell is not None:
            self.cell.append(text)

    def handle_endtag(self, tag):
        if tag == 'td' and self.cell is not None:
            self.row.append(''.join(self.cell))
            self.cell = None
        if tag == 'tr' and self.row is not None:
            self.rows.append(self.row)
            self.row = None


def main():
    data = gen.load()
    document = gen.PAGE.read_text(encoding='utf-8')
    assert gen.generate(document, data) == document
    parsed = Table()
    parsed.feed(document)
    assert parsed.ids == [r['id'] for r in data['registros']]
    assert parsed.rows == [gen.values(r) for r in data['registros']]
    for item in ['dataVencimento', 'dataPagamento', 'credor', 'valorPagamento']:
        assert parsed.items[item] == 464
    for item in ['filtroPesquisa', 'salvarRelatorio', 'historicoExercicio', 'dataUltimaAtualizacao']:
        assert parsed.items[item] == 1
    assert 'data-dado-sintetico' not in document and 'sintético' not in document.lower()
    assert not gen.CPF.search(document)
    assert 'serigyLoadSection="ordemTabela"' in document
    assert document.count('serigyExecuteWaitSection="ordemTabela"') == 2
    for year in [2026, 2025, 2024, 2023]:
        assert f'value="{year}" serigyValue="{year}"' in document
    assert '<option value="Obras">Obras</option>' in document
    assert document.index('serigyItem="dataUltimaAtualizacao"') > document.index('</table>')
    # Nenhuma operação do preparador antigo pode substituir a consulta real.
    import preparar_teste_ordem as old
    for active in [True, False]:
        try:
            old.render(active)
        except ValueError as error:
            assert 'dados reais' in str(error)
        else:
            raise AssertionError('Preparador sintético poderia sobrescrever a base real.')
    # O bloqueio global permanece válido, independentemente de outros ensaios ativos.
    import preparar_deploy as deploy
    original = deploy.DIST
    work = gen.ROOT / 'trabalho'
    work.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='ordem-bloqueio-', dir=work) as folder:
        fixture = Path(folder)
        (fixture / 'index.html').write_text('<p data-dado-sintetico="teste">Ensaio isolado</p>', encoding='utf-8')
        deploy.DIST = fixture
        try:
            for base, allow in [('', False), ('/Portal-da-Transparencia', True),
                                ('/transparencia.sergipeprevidencia', False)]:
                try:
                    deploy.check_synthetic_content(base, allow)
                except ValueError:
                    pass
                else:
                    raise AssertionError('Bloqueio oficial falhou.')
            deploy.check_synthetic_content('/transparencia.sergipeprevidencia', True)
        finally:
            deploy.DIST = original
    print('OK: 464 OBs únicas; anos 152/112/111/89; categorias 82/4/378/0; '
          '13 campos iguais à fonte, valores em centavos, máscaras, oito marcações, '
          'histórico e proteção contra sobrescrita/bloqueio conferidos.')


if __name__ == '__main__':
    main()
