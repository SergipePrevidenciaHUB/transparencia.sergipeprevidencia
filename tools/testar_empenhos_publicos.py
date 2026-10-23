"""Conciliação pública e privacidade; imprime somente contagens, nunca documentos."""
from html.parser import HTMLParser
import re
import integrar_empenhos as gen
class Rows(HTMLParser):
    def __init__(self):super().__init__();self.rows=[];self.row=None;self.cell=None;self.details=0
    def handle_starttag(self,t,attrs):
        if t=='tr' and 'data-id' in dict(attrs):self.row=[]
        if t=='td' and self.row is not None:self.cell=[]
        if t=='details':self.details+=1
    def handle_data(self,s):
        if self.cell is not None:self.cell.append(s)
    def handle_endtag(self,t):
        if t=='td' and self.cell is not None:self.row.append(''.join(self.cell));self.cell=None
        if t=='tr' and self.row is not None:self.rows.append(self.row);self.row=None
def main():
    d=gen.load();doc=gen.PAGE.read_text(encoding='utf-8');section=gen.block(doc,'empenhos')
    assert gen.generate(doc,d)==doc
    p=Rows();p.feed(section)
    assert [r[:19] for r in p.rows]==[gen.values(r) for r in d['registros']]
    assert len(p.rows)==p.details==4517 and not gen.CPF.search(section)
    assert 'sintétic' not in section.lower() and '22/10/2026' in section
    repeats=[r for r in d['registros'] if r['entidade']!='SergipePrevidência' and r['linhas_gerenciais']>1][:3]
    assert len(repeats)==3 and all(sum(v['id']==r['id'] for v in d['registros'])==1 for r in repeats)
    assert all(r['valor_atualizado_centavos']==r['valor_original_centavos']+r['valor_reforcado_centavos']-r['valor_anulado_centavos'] for r in repeats)
    for item in gen.MARKS.values():assert f'serigyItem="{item}"' in section
    print('OK: 4517 notas/19 campos iguais à projeção; três notas repetidas uma vez cada; atualização, cinco marcações e máscaras conferidas.')
if __name__=='__main__':main()
