"""Concilia a tabela hierárquica, a exportação e os registros do XLSX de teste."""
import csv
import hashlib
import json
import re
from collections import Counter
from decimal import Decimal
from html.parser import HTMLParser

from openpyxl import load_workbook
from integrar_receitas import ROOT, PAGE, reais


class Table(HTMLParser):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.rows = []
        self.row = None
        self.cell = None
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'table':
            self.count += 1
        elif tag == 'tr' and 'data-level' in attrs:
            self.row = dict(attrs=attrs, cells=[])
        elif tag == 'td' and self.row is not None:
            self.cell = ''
    def handle_data(self, data):
        if self.cell is not None:
            self.cell += data
    def handle_endtag(self, tag):
        if tag == 'td' and self.cell is not None:
            self.row['cells'].append(self.cell)
            self.cell = None
        elif tag == 'tr' and self.row is not None:
            self.rows.append(self.row)
            self.row = None


def main():
    path=ROOT/'dados-entrada/receitas/receitas-teste.xlsx'
    sha=hashlib.sha256(path.read_bytes()).hexdigest()
    book=load_workbook(path,read_only=True,data_only=False)
    source=[r for sheet in book for r in sheet.iter_rows(min_row=2,values_only=True)];book.close()
    data=json.loads((ROOT/'dist/dados/receitas/receitas-integracao.json').read_text(encoding='utf-8'))
    base,annual=data['classificacoes'],data['previsao_anual']
    assert len(source)==len(base)==425 and len(annual)==9
    assert len({(r['codigo_uo'],r['ano'],r['mes']) for r in base})==97
    assert sum(Decimal(r['arrecadado'])<0 for r in base)==3
    assert sum('intraor' in r['categoria'].casefold() for r in base)==98
    for raw,row in zip(source,base):
        for field,index in [('codigo_uo',2),('ano',3),('mes',4),('categoria',5),('codigo_categoria',6),('origem',7),('codigo_origem',8),('especie',9),('codigo_especie',10)]:
            assert row[field]==str(raw[index])
        assert Decimal(row['previsto'])==Decimal(str(raw[11]))
        assert Decimal(row['arrecadado'])==Decimal(str(raw[12]))
    fun=[r for r in base if r['codigo_uo']=='37403']
    assert {int(r['mes']) for r in fun}=={6,7,8,9,10} and all(r['ano']=='2026' for r in fun)
    assert next(r['previsao_anual'] for r in annual if r['codigo_uo']=='37403')=='0.00'
    parser=Table();html=PAGE.read_text(encoding='utf-8');parser.feed(html)
    assert parser.count==1 and json.loads(re.search(r'id="receitasDados">(.*?)</script>',html,re.S)[1])==data
    nodes={r['attrs']['id']:r for r in parser.rows}
    expected=set()
    for r in base:
        key=(r['codigo_uo'],r['ano'])
        for field in ('categoria','origem','especie'):
            key+=(r['codigo_'+field],);expected.add(key)
    assert len(nodes)==len(expected)
    leaf_indices=[]
    for row in nodes.values():
        a,c=row['attrs'],row['cells'];level=int(a['data-level'])
        assert len(c)==7 and a['data-uo-confirmada']=='true'
        chain=[c[4]];parent=a['data-parent-id']
        while parent:
            p=nodes[parent];chain.insert(0,p['cells'][4]);parent=p['attrs']['data-parent-id']
        parts=[(i,r) for i,r in enumerate(base) if r['codigo_uo']==a['data-codigo-uo'] and r['ano']==a['data-year'] and [r['codigo_'+k] for k in ('categoria','origem','especie')][:level]==chain]
        assert [i for i,r in parts]==list(map(int,a['data-base-indices'].split()))
        if level==3:leaf_indices.extend(i for i,r in parts)
        assert c[-1]==reais(sum((Decimal(r['arrecadado']) for i,r in parts),Decimal(0)))
        january=[r for i,r in parts if r['mes']=='1']
        forecast=sum((Decimal(r['previsto']) for r in january),Decimal(0)) if january else Decimal(0) if a['data-codigo-uo']=='37403' and a['data-year']=='2026' else None
        assert c[-2]==('—' if forecast is None else reais(forecast))
        # Cada classificação acumula janeiro-fevereiro-março sem incluir o futuro.
        monthly={m:sum((Decimal(r['arrecadado']) for i,r in parts if int(r['mes'])==m),Decimal(0)) for m in range(1,13)}
        feb=sum((Decimal(r['arrecadado']) for i,r in parts if int(r['mes'])<=2),Decimal(0))
        march=sum((Decimal(r['arrecadado']) for i,r in parts if int(r['mes'])<=3),Decimal(0))
        assert feb==monthly[1]+monthly[2] and march==feb+monthly[3]
        if a['data-codigo-uo']=='37403':
            assert all(int(r['mes'])>=6 for i,r in parts)
        ref=max(int(r['mes']) for r in base if r['ano']==a['data-year'])
        assert c[3].endswith('/'+a['data-year']) and ref==(10 if a['data-year']=='2026' else 12)
    assert sorted(leaf_indices)==list(range(425)), 'Cada base pertence a uma unica Especie/UO/ano'
    with (ROOT/'dist/dados/receitas/receitas-integracao.csv').open(encoding='utf-8-sig',newline='') as f:exported=list(csv.DictReader(f,delimiter=';'))
    assert len(exported)==425
    for out,r in zip(exported,base):
        assert out['tipo_recorte']=='acumulado' and out['mes_registro']==r['mes'] and out['ano_referencia']==r['ano']
        assert out['mes_referencia_acumulado']==('10' if r['ano']=='2026' else '12')
        assert out['arrecadado_no_mes']==r['arrecadado'] and out['previsto_na_origem']==r['previsto']
    assert hashlib.sha256(path.read_bytes()).hexdigest()==sha
    print(f'PASS: uma tabela/{len(nodes)} nos; 425 bases/97 competencias/9 previsoes; marco=jan+fev+mar, fevereiro exclui marco em cada classificacao; FUNPREV desde junho; 3 negativos/98 intraorcamentarias; HTML/CSV/JSON sem duplicacao; XLSX preservado.')


if __name__=='__main__':
    main()
