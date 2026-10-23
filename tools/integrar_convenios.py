"""Gera apenas os três módulos de Convênios; --check não modifica arquivos."""
import argparse
from datetime import datetime
from html import escape
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'dist/Portal-da-Transparencia/Convenios'
SOURCE=ROOT/'dados-entrada/convenios/convenios-revisados.json'
SCHEMA='https://serigy.tce.se.gov.br/comum/convenios-transferencias.html'
PERIOD='01/2018 até 21/10/2026'
DATES='Informações atualizadas em <time datetime="2026-10-22">22/10/2026</time>'

def load():
    data=json.loads(SOURCE.read_text(encoding='utf-8-sig'))
    assert data['schema']==SCHEMA and data['data_atualizacao_portal']=='2026-10-22'
    assert len(data['registros'])==8
    assert len({r['numero_ano'] for r in data['registros']})==8
    for r in data['registros']:
        assert len(r['partes'])==2 and r['obrigacoes_texto']
        assert all(x in r['obrigacoes_texto'] for x in ['SergipePrevidência:', 'Instituição parceira:', 'Compromissos conjuntos:'])
        url=r.get('documento_url') or r.get('documento_url_planejada')
        assert url and url.startswith('https://sergipeprevidencia.se.gov.br/wp-content/uploads/') and url.lower().endswith('.pdf')
    return data

def years(first=2023):
    return '<option value="">Todos os exercícios disponíveis</option>'+''.join(f'<option value="{y}" serigyValue="{y}">{y}</option>' for y in range(2026,first-1,-1))

def fields(route):
    return [('identificaTransferencia','Número/ano','identificação de instrumento'),
            ('orgaoRepassador' if route=='Recebidas' else 'orgaoBeneficiario','Órgão repassador' if route=='Recebidas' else 'Beneficiário','órgão repassador associado a uma transferência' if route=='Recebidas' else 'beneficiário associado a uma transferência'),
            ('objetoConvenio','Objeto','objeto de transferência'),('vigenciaConvenio','Vigência','vigência de instrumento'),
            ('valorTotalPrevisto' if route=='Recebidas' else 'valorTotalRepasse','Valor total previsto (R$)','valor total previsto para transferência'),
            ('valorRepassado','Valor repassado (R$)','valor repassado'),('anexoConvenio','Instrumento integral','instrumento integral de transferência')]

def statement(route):
    return ('Não foram recebidas transferências voluntárias' if route=='Recebidas' else 'Não foram realizados repasses ou transferências voluntárias de recursos')+' no período de '+PERIOD+'.'

def absence(route):
    title='Transferências '+route
    cells=[]
    for item,_,label in fields(route):
        reason=f'{route} — {item}: não há {label} a apresentar, pois não houve transferências voluntárias no período de {PERIOD}.'
        cells.append(f'<td serigyItem="{item}" serigyEmpty="{escape(reason,quote=True)}" data-motivo-ausencia="{escape(reason,quote=True)}">—</td>')
    return f'''<h1>{title}</h1>
<section id="declaracao-oficial"><h2>Informação institucional</h2><p id="texto-declaracao">{statement(route)}</p></section>
<section id="consulta-transferencias" data-transferencias-ausentes="true" aria-labelledby="titulo-consulta">
<h2 id="titulo-consulta">Consulta por exercício</h2>
<form id="filtro-convenios" class="filter-panel" aria-label="Consultar declaração de ausência de transferências" serigyItem="filtroPesquisa"><div class="field"><label for="exercicio-convenios">Exercício</label><select id="exercicio-convenios" name="ano" serigyItem="historicoExercicio" serigyExecuteWaitSection="convenioTabela">{years()}</select></div><div class="filter-actions"><button type="submit" serigyExecuteWaitSection="convenioTabela">Pesquisar</button><button type="reset" serigyClearForm>Limpar filtros</button></div></form>
<p id="contagem-convenios" role="status" aria-live="polite">0 transferências. Declaração referente ao período de {PERIOD}.</p>
<div class="table-wrap"><table id="tabela-convenios" serigyLoadSection="convenioTabela"><caption>Declaração de ausência de transferências — período de {PERIOD}</caption><thead><tr>{''.join('<th scope="col">'+label+'</th>' for _,label,_ in fields(route))}</tr></thead><tbody><tr data-declaracao-ausencia="true">{''.join(cells)}</tr></tbody></table></div>
<button id="csv-convenios" type="button" serigyItem="salvarRelatorio" serigyValue="csv">Exportar declaração em CSV</button>
</section><div class="update-info" serigyItem="dataUltimaAtualizacao">{DATES}</div>'''

def agreement_years(r):
    dates=re.findall(r'\d{2}/\d{2}/\d{4}',r['vigencia_planilha'])
    assert len(dates)==2
    start,end=[datetime.strptime(d,'%d/%m/%Y') for d in dates]
    assert start<=end
    return start.year,end.year

def agreements(data):
    rows=[]
    for r in data['registros']:
        start,end=agreement_years(r)
        url=r.get('documento_url') or r.get('documento_url_planejada')
        rows.append(f'''<tr data-year="{start}" data-inicio="{start}" data-fim="{end}"><td>{start}</td><td serigyItem="identificaAcordo">{escape(r['numero_ano'])}</td><td serigyItem="participante" style="white-space: pre-line">{escape(chr(10).join(r['partes']))}</td><td serigyItem="objetoConvenio" style="white-space: pre-line">{escape(r['objeto'])}</td><td serigyItem="vigenciaConvenio">{escape(r['vigencia_planilha'])}</td><td serigyItem="obrigacoes" style="white-space: pre-line">{escape(r['obrigacoes_texto'])}</td><td><a serigyItem="anexoConvenio" href="{escape(url,quote=True)}">Íntegra do instrumento (PDF)</a></td></tr>''')
    return f'''<h1>Acordos Sem Transferência</h1><p class="lead">Acordos e instrumentos de cooperação sem transferência de recursos financeiros.</p>
<form id="filtro-acordos" class="filter-panel" serigyItem="filtroPesquisa" aria-label="Consultar acordos por exercício de vigência"><div class="field"><label for="exercicio-acordos">Exercício de vigência</label><select id="exercicio-acordos" name="ano" serigyItem="historicoExercicio" serigyExecuteWaitSection="semTransferenciaTabela">{years(2022)}</select></div><div class="filter-actions"><button type="submit" serigyExecuteWaitSection="semTransferenciaTabela">Pesquisar</button><button type="reset" serigyClearForm>Limpar filtros</button></div></form>
<section id="resultados-acordos" serigyLoadSection="semTransferenciaTabela" aria-labelledby="titulo-acordos"><h2 id="titulo-acordos">Instrumentos de cooperação</h2><p id="contagem-acordos" role="status" aria-live="polite">8 acordos no recorte.</p><div class="table-wrap"><table id="tabela-acordos"><caption>Acordos sem transferência</caption><thead><tr><th scope="col">Ano de início da vigência</th><th scope="col">Número/ano do instrumento</th><th scope="col">Partes participantes</th><th scope="col">Objeto</th><th scope="col">Vigência</th><th scope="col">Obrigações ajustadas</th><th scope="col">Instrumento integral</th></tr></thead><tbody>{chr(10).join(rows)}</tbody></table></div></section>
<button id="csv-acordos" type="button" serigyItem="salvarRelatorio" serigyValue="csv">Baixar recorte em CSV</button>
<div id="atualizacao-sem-transferencia" class="update-info" serigyItem="dataUltimaAtualizacao">{DATES}</div>'''

def generate(original,route,data):
    body=agreements(data) if route=='SemTransferencia' else absence(route)
    result,n=re.subn(r'(<main\b[^>]*>)[\s\S]*?(</main>)',lambda m:m[1]+'\n'+body+'\n'+m[2],original,count=1)
    assert n==1
    result=result.replace('src="/assets/js/convenios-teste.js"','src="/assets/js/convenios.js"')
    if 'data-convenios-revisados="true"' not in result:result=result.replace('<main ','<main data-convenios-revisados="true" ',1)
    assert SCHEMA in result and not re.search(r'sint[ée]tic|ENSAIO|file://',result,re.I)
    return result

def run(check=False):
    data=load()
    for route in ['Recebidas','Realizadas','SemTransferencia']:
        p=BASE/route/'index.html';old=p.read_bytes();s=old.decode('utf-8').replace('\r\n','\n');new=generate(s,route,data)
        if check:assert s==new,f'Regeneração pendente: {route}'
        elif s!=new:p.write_bytes(new.replace('\n','\r\n' if b'\r\n' in old else '\n').encode('utf-8'))
    print('OK: declarações sem operações em 5.1/5.2; oito acordos e oito resumos em 5.3; atualização 22/10/2026.')

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');run(p.parse_args().check)

if __name__=='__main__':main()
