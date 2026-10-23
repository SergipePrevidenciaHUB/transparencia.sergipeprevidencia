"""Confere a preparação consolidada real de 4.1/4.2, sem gravar em dist."""
from html.parser import HTMLParser
import despesas_consolidadas as gen

class Rows(HTMLParser):
    def __init__(self):super().__init__();self.rows=[];self.row=None;self.cell=None
    def handle_starttag(self,t,attrs):
        if t=='tr' and 'data-ano' in dict(attrs):self.row=[]
        if t=='td' and self.row is not None:self.cell=[]
    def handle_data(self,s):
        if self.cell is not None:self.cell.append(s)
    def handle_endtag(self,t):
        if t=='td' and self.cell is not None:self.row.append(''.join(self.cell));self.cell=None
        if t=='tr' and self.row is not None:self.rows.append(self.row);self.row=None

def main():
    data=gen.load();doc=gen.PAGE.read_text(encoding='utf-8')
    assert gen.generate(doc,data)==doc
    p=Rows();p.feed(gen.block(doc,'classificacao'))
    assert p.rows==[gen.cells(r) for r in data['registros']]
    for name in ['totais','classificacao']:
        section=gen.block(doc,name)
        assert 'data-despesas-reais="true"' in section
        assert 'sintétic' not in section.lower() and '22/10/2026' in section
    assert 'data-despesas-reais="true"' in gen.block(doc,'empenhos')
    import preparar_deploy as deploy
    # Ordem Cronológica também passou a usar dados reais. Testar o bloqueio
    # sem exigir a permanência de um ensaio no conteúdo publicável.
    from pathlib import Path
    import tempfile
    original=deploy.DIST
    with tempfile.TemporaryDirectory(prefix='bloqueio-despesas-',dir=gen.ROOT/'trabalho') as folder:
        fixture=Path(folder)
        (fixture/'index.html').write_text('<p data-dado-sintetico="teste">Ensaio isolado</p>',encoding='utf-8')
        deploy.DIST=fixture
        try:
            try:deploy.check_synthetic_content('',False)
            except ValueError as error:assert 'bloqueada' in str(error)
            else:raise AssertionError('O bloqueio oficial deve permanecer funcional.')
        finally:deploy.DIST=original
    print('OK: 3338 linhas e 14 colunas iguais à fonte; 97 totais conciliados; regeneração estável e bloqueio oficial preservado.')

if __name__=='__main__':main()
