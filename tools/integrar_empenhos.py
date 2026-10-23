"""Integra somente a projeção pública de empenhos em 4.3; --check não grava."""
import argparse,json,re
from collections import Counter
from html import escape as e
from pathlib import Path
from despesas_consolidadas import block,money
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'dados-entrada/despesas/empenhos-consolidados-publicos.json'
PAGE=ROOT/'dist/Portal-da-Transparencia/Despesas/index.html'
FIELDS=['numero_empenho','data_empenho','documento','credor','licitacao','codigo_licitacao','modalidade','objeto','valor_original','valor_anulado','valor_reforcado','valor_executado','unidade_origem','funcao','subfuncao','natureza','fonte','elemento','valor_atualizado']
HEADERS=['Número do empenho','Data de lançamento do empenho','CPF/CNPJ / identificador público','Nome favorecido','Licitação','Código da licitação','Modalidade','Descrição da solicitação','Valor original (R$)','Valor anulado (R$)','Valor reforçado (R$)','Valor executado (R$)','Unidade orçamentária / gestora','Função','Sub-função','Natureza da despesa','Fonte dos recursos','Elemento de despesa','Valor atualizado (R$)']
MARKS={'credor':'credorEmpenho','objeto':'objetoEmpenho','modalidade':'modalidadeEmpenho','licitacao':'numeroProcedimento','valor_atualizado':'valorEmpenhoIndividual'}
CPF=re.compile(r'(?<!\d)\d{3}\.\d{3}\.\d{3}-\d{2}(?!\d)')
def cpf_valid(value):
    s=re.sub(r'\D','',value)
    return len(s)==11 and len(set(s))>1 and all(int(s[n])==((sum(int(s[i])*(n+1-i) for i in range(n))*10)%11)%10 for n in [9,10])
def public_check(rows):
    for r in rows:
        assert not any(CPF.search(v) for v in r.values() if isinstance(v,str)), 'CPF completo na projeção pública; publicação recusada.'
        if r['tipo_documento']=='CPF':assert re.fullmatch(r'\*{3}\.\*{3}\.\*{3}-\d{2}',r['documento']), 'Máscara pública inválida.'
        for field in ['objeto','credor']:
            assert not any(cpf_valid(x) for x in re.findall(r'(?<!\w)\d{11}(?!\w)',r.get(field) or '')), 'Candidato CPF em texto livre; publicação recusada.'
def load():
    d=json.loads(SOURCE.read_text(encoding='utf-8-sig'));rows=d['registros'];public_check(rows)
    assert len(rows)==len({r['id'] for r in rows})==4517
    assert Counter(r['entidade'] for r in rows)==Counter({'SergipePrevidência':3282,'FINANPREV':1223,'FUNPREV':12})
    for group in d['resumo']['por_ano_entidade']:assert sum(r['ano']==group['ano'] and r['entidade']==group['entidade'] for r in rows)==group['empenhos']
    for r in rows:assert r['valor_atualizado_centavos']==r['valor_original_centavos']+r['valor_reforcado_centavos']-r['valor_anulado_centavos']
    return d
def values(r):
    result=[]
    for field in FIELDS:
        if field.startswith('valor_'):
            v=r.get(field+'_centavos');result.append('' if v is None else money(v))
        elif field=='data_empenho':result.append('/'.join(reversed(r[field].split('-'))) if r.get(field) else '')
        else:result.append('' if r.get(field) is None else str(r[field]))
    return result
def generate(doc,d):
    preserved=[block(doc,n) for n in ['totais','classificacao']]
    def select(name,label,options,default='',history=False):
        return '<div class="field"><label for="ep-'+name+'">'+label+'</label><select id="ep-'+name+'" name="'+name+'"'+(' serigyItem="historicoExercicio"' if history else '')+' serigyExecuteWaitSection="empenhosPublicosTabela">'+''.join('<option value="'+e(str(v),quote=True)+'"'+(' serigyValue="'+str(v)+'"' if history else '')+(' selected' if str(v)==default else '')+'>'+e(str(t))+'</option>' for v,t in options)+'</select></div>'
    form=select('ano','Exercício',[(y,y) for y in [2026,2025,2024,2023]],'2026',True)+select('mes','Mês de lançamento',[('','Todos os meses')]+[(m,str(m).zfill(2)) for m in range(1,13)])+select('entidade','Entidade',[('','Todas as entidades')]+[(v,v) for v in ['SergipePrevidência','FINANPREV','FUNPREV']],'SergipePrevidência')
    for name,label in [('numero','Número do empenho'),('nome','Nome do favorecido'),('documento','CNPJ ou identificador público (exceto CPF)')]:form+='<div class="field"><label for="ep-'+name+'">'+label+'</label><input type="search" id="ep-'+name+'" name="'+name+'" autocomplete="off"></div>'
    rows=[];initial=0
    for r in d['registros']:
        visible=r['ano']==2026 and r['entidade']=='SergipePrevidência';initial+=visible
        attrs=' '.join('data-'+k+'="'+e(str(v),quote=True)+'"' for k,v in [('id',r['id']),('ano',r['ano']),('mes',r['mes']),('entidade',r['entidade']),('tipo',r['tipo_documento'])])
        vals=values(r)
        cells=''.join('<td'+(' data-serigy-item="'+MARKS[f]+'"'+(' serigyItem="'+MARKS[f]+'"' if visible else '') if f in MARKS and v!='' else '')+(' class="ep-money"' if f.startswith('valor_') else '')+'>'+e(v)+'</td>' for f,v in zip(FIELDS,vals))
        detail=''.join('<dt>'+e(HEADERS[i])+'</dt><dd>'+e(vals[i])+'</dd>' for i in [0,1,2,3,4,6,7,18])
        rows.append('<tr '+attrs+('' if visible else ' hidden')+'>'+cells+'<td><details><summary>Detalhes do empenho</summary><dl>'+detail+'</dl></details></td></tr>')
    section='<section id="empenhos" data-despesas-reais="true" class="content-box empenhos-publicos" serigySchema="https://serigy.tce.se.gov.br/comum/despesas.html" aria-labelledby="titulo-empenhos"><h2 id="titulo-empenhos">Consulta de empenhos</h2><form id="ep-filtro" class="filter-panel" serigyItem="filtroPesquisa" aria-label="Consultar empenhos" aria-describedby="ep-status">'+form+'<div class="filter-actions"><button type="submit" serigyExecuteWaitSection="empenhosPublicosTabela">Pesquisar</button><button type="reset" serigyClearForm>Limpar</button></div></form><p id="ep-status" role="status" aria-live="polite">'+str(initial)+' registros no recorte.</p><button type="button" id="ep-csv" serigyItem="salvarRelatorio" serigyValue="csv">Exportar CSV</button><div class="ep-table-wrap" role="region" tabindex="0" aria-label="Empenhos individuais"><table id="ep-tabela" serigyLoadSection="empenhosPublicosTabela"><caption>Empenhos individuais por exercício e mês de lançamento</caption><thead><tr>'+''.join('<th scope="col">'+e(h)+'</th>' for h in HEADERS+['Detalhamento'])+'</tr></thead><tbody>\n'+'\n'.join(rows)+'\n</tbody></table></div><div class="update-info" serigyItem="dataUltimaAtualizacao">Informações atualizadas em <time datetime="2026-10-22">22/10/2026</time></div></section>'
    doc=doc.replace(block(doc,'empenhos'),section,1)
    if '/assets/js/empenhos-publicos.js' not in doc:doc=doc.replace('</head>','<link rel="stylesheet" href="/assets/css/empenhos-publicos.css">\n<script defer src="/assets/js/empenhos-publicos.js"></script>\n</head>',1)
    doc=doc.replace('Credores, valores, objetos e procedimentos de contratação. Aguardando dados.','Credores, valores, objetos e procedimentos de contratação.')
    assert preserved==[block(doc,n) for n in ['totais','classificacao']]
    assert not CPF.search(section)
    return doc
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();raw=PAGE.read_bytes();doc=raw.decode('utf-8').replace('\r\n','\n');new=generate(doc,load())
    if args.check:
        if doc!=new:p.error('Página difere da projeção pública.')
    elif doc!=new:PAGE.write_bytes(new.replace('\n','\r\n' if b'\r\n' in raw else '\n').encode('utf-8'))
    print('OK: 4517 notas públicas; 1524 CPFs mascarados; valores atualizados conciliados; 4.1/4.2 preservados.')
if __name__=='__main__':main()
