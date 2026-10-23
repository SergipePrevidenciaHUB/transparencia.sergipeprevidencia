"""Geração de 4.1/4.2: fonte consolidada CGE, sem modificar empenhos."""
import argparse,json,re
from collections import Counter,defaultdict
from html import escape as e
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'dados-entrada/despesas/despesas-consolidadas-cge.json'
PAGE=ROOT/'dist/Portal-da-Transparencia/Despesas/index.html'
MEASURES=['empenhado','liquidado','pago']
HEADERS=['Ano/Mês','Unidade orçamentária / gestora','Função','Sub-função','Categoria econômica','Grupo','Ação','Programa','Modalidade de aplicação','Elemento','Fonte','Empenhado (R$)','Liquidado (R$)','Pago (R$)']
FIELDS=['unidade_origem','funcao','subfuncao','categoria','grupo','acao','programa','modalidade_aplicacao','elemento','fonte']
ITEMS=['unidadeDespesa','funcaoDespesa','subFuncaoDespesa','categoriaDespesa','grupoDespesa','','','','elementoDespesa','fonteRecursosDespesa']
MONTHS=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
def money(n):
    sign='-' if n<0 else '';n=abs(n)
    return sign+format(n//100,',').replace(',','.')+','+str(n%100).zfill(2)
def label(r,f):
    value=str(r.get(f) or '');code=r.get(f+'_codigo')
    return (str(code)+' — '+value) if code and not value.startswith(str(code)) else value
def cells(r):return [f'{r["ano"]}/{r["mes"]:02d}']+[label(r,f) for f in FIELDS]+[money(r[m+'_centavos']) for m in MEASURES]
def load():
    d=json.loads(SOURCE.read_text(encoding='utf-8-sig'));rows=d['registros']
    assert len(rows)==3338 and Counter(r['entidade'] for r in rows)==Counter({'SergipePrevidência':1736,'FINANPREV':1574,'FUNPREV':28})
    sums=defaultdict(lambda:[0,0,0,0])
    for r in rows:
        v=sums[(r['ano'],r['mes'],r['entidade'])]
        for i,m in enumerate(MEASURES):assert isinstance(r[m+'_centavos'],int);v[i]+=r[m+'_centavos']
        v[3]+=1
    assert len(sums)==len(d['totais_mensais'])==97
    for t in d['totais_mensais']:assert sums[(t['ano'],t['mes'],t['entidade'])]==[t[m+'_centavos'] for m in MEASURES]+[t['registros']]
    return d
def block(doc,name):return re.search(r'<section id="'+name+r'"[\s\S]*?</section>',doc)[0]
def generate(doc,d):
    rows=d['registros'];initial=[r for r in rows if (r['ano'],r['mes'],r['entidade'])==(2026,9,'SergipePrevidência')]
    totals=[sum(r[m+'_centavos'] for r in initial) for m in MEASURES]
    assert len(initial)==40 and totals==[7042773023,7262959159,4664571608]
    def select(name,title,options,default='',history=False):
        opts=''.join('<option value="'+e(str(v),quote=True)+'"'+(' serigyValue="'+str(v)+'"' if history else '')+(' selected' if str(v)==default else '')+'>'+e(str(t))+'</option>' for v,t in options)
        return f'<div class="field"><label for="dc-{name}">{title}</label><select id="dc-{name}" name="{name}"'+(' serigyItem="historicoExercicio"' if history else '')+' serigyExecuteWaitSection="despesasConsolidadasTabela">'+opts+'</select></div>'
    schema=' serigySchema="https://serigy.tce.se.gov.br/comum/despesas.html"'
    date='<div class="update-info" serigyItem="dataUltimaAtualizacao">Informações atualizadas em <time datetime="2026-10-22">22/10/2026</time></div>'
    controls=select('ano','Exercício',[(y,y) for y in [2026,2025,2024,2023]],'2026',True)+select('mes','Mês',[('','Todos os meses disponíveis')]+[(i+1,v) for i,v in enumerate(MONTHS)],'9')+select('entidade','Entidade',[('','Todas as entidades')]+[(v,v) for v in d['unidades_filtro']],'SergipePrevidência')+select('elemento','Elemento',[('','Todos os elementos')]+[(v,v) for v in sorted({label(r,'elemento') for r in rows})])
    top='<section id="totais" class="content-box despesas-consolidadas"'+schema+'><h2 id="titulo-totais">Totais das despesas</h2><form id="dc-filtro" class="filter-panel" serigyItem="filtroPesquisa" aria-label="Consultar despesas" aria-describedby="dc-status">'+controls+'<div class="filter-actions"><button type="submit" serigyExecuteWaitSection="despesasConsolidadasTabela">Pesquisar</button><button type="reset" serigyClearForm>Limpar</button></div></form><div class="dc-indicadores">'+''.join('<div><span>'+t+'</span><strong id="dc-'+m+'" serigyItem="'+item+'">R$ '+money(v)+'</strong></div>' for m,t,item,v in zip(MEASURES,['Empenhado','Liquidado','Pago'],['valorEmpenhado','valorLiquidado','valorPago'],totals))+'</div>'+date+'</section>'
    rendered=[]
    for r in rows:
        attrs=' '.join('data-'+k+'="'+e(str(v),quote=True)+'"' for k,v in [('ano',r['ano']),('mes',r['mes']),('entidade',r['entidade']),('elemento',label(r,'elemento'))]+[(m,r[m+'_centavos']) for m in MEASURES])
        marks=['']+ITEMS+['','','']
        tds=''.join('<td'+(' data-serigy-item="'+item+'"'+(' serigyItem="'+item+'"' if r in initial else '') if item and value else '')+(' class="dc-money"' if i>=11 else '')+'>'+e(value)+'</td>' for i,(item,value) in enumerate(zip(marks,cells(r))))
        rendered.append('<tr '+attrs+(' hidden' if r not in initial else '')+'>'+tds+'</tr>')
    table='<section id="classificacao" class="content-box despesas-consolidadas"'+schema+'><h2 id="titulo-classificacao">Despesas por classificação orçamentária</h2><p id="dc-status" role="status" aria-live="polite">40 registros no recorte.</p><button type="button" id="dc-csv" serigyItem="salvarRelatorio" serigyValue="csv">Exportar CSV</button><div class="dc-table-wrap" tabindex="0" role="region" aria-label="Classificação orçamentária"><table id="dc-tabela" serigyLoadSection="despesasConsolidadasTabela"><caption>Classificação orçamentária por competência e entidade</caption><thead><tr>'+''.join('<th scope="col">'+e(h)+'</th>' for h in HEADERS)+'</tr></thead><tbody>\n'+'\n'.join(rendered)+'\n</tbody></table></div>'+date+'</section>'
    untouched=block(doc,'empenhos')
    for name,value in [('totais',top),('classificacao',table)]:
        value=value.replace('id="'+name+'"','id="'+name+'" data-despesas-reais="true"',1)
        doc=doc.replace(block(doc,name),value,1)
    if '/assets/css/despesas-consolidadas.css' not in doc:doc=doc.replace('</head>','<link rel="stylesheet" href="/assets/css/despesas-consolidadas.css">\n<script defer src="/assets/js/despesas-consolidadas.js"></script>\n</head>',1)
    assert block(doc,'empenhos')==untouched
    return doc
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    raw=PAGE.read_bytes();doc=raw.decode('utf-8').replace('\r\n','\n');result=generate(doc,load())
    if args.check:
        if result!=doc:p.error('Página difere da preparação consolidada.')
    elif result!=doc:PAGE.write_bytes(result.replace('\n','\r\n' if b'\r\n' in raw else '\n').encode('utf-8'))
    print('OK: 3.338 registros; 97 totais mensais conciliados; início com 40 linhas e três totais confirmados; 4.3 preservado.')
if __name__=='__main__':main()
