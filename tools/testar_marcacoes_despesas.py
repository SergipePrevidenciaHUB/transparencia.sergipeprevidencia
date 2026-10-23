"""Regressão pontual das marcações do recorte real, sem executar o Invoker."""
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.request import urlopen
import csv, hashlib, io, json, socket, subprocess, tempfile, time
import despesas_consolidadas as dc
import integrar_empenhos as ep
import preparar_deploy as deploy
from auditar_publicacao_documentos import CDP

ROOT=Path(__file__).resolve().parents[1]
SCHEMA='https://serigy.tce.se.gov.br/comum/despesas.html'
ITEMS=[v for v in dc.ITEMS if v]+list(ep.MARKS.values())

class Initial(HTMLParser):
    def __init__(self):
        super().__init__();self.stack=[];self.first=set();self.wait=[];self.load=[];self.count=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        hidden='hidden' in a or any(x[1] for x in self.stack)
        schema=a.get('serigyschema') or (self.stack[-1][2] if self.stack else '')
        item=a.get('serigyitem');saved=a.get('data-serigy-item')
        if saved:
            self.count+=1
            assert item==(None if hidden else saved), 'Marcação fora do recorte inicial'
        if item in ITEMS:
            assert not hidden and schema==SCHEMA,(item,'oculto/schema')
            self.first.add(item)
        if 'serigyexecutewaitsection' in a:self.wait.append(a['serigyexecutewaitsection'])
        if 'serigyloadsection' in a:self.load.append(a['serigyloadsection'])
        if tag not in ['area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr']:
            self.stack.append((tag,hidden,schema))
    def handle_endtag(self,tag):
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i][0]==tag:del self.stack[i:];break

SNAPSHOT='''(()=>{
const names=ITEMS, schema=SCHEMA;
const visible=e=>!!e&&!e.closest('[hidden]')&&e.getClientRects().length>0&&getComputedStyle(e).visibility==='visible';
const errors=[];
document.querySelectorAll('#dc-tabela [data-serigy-item],#ep-tabela [data-serigy-item]').forEach(e=>{
const active=!e.closest('tr').hidden;
if(e.getAttribute('serigyItem')!==(active?e.dataset.serigyItem:null))errors.push('recorte '+e.dataset.serigyItem);
});
const fields=names.map(name=>{const e=document.querySelector('[serigyItem="'+name+'"]');
if(e&&(!visible(e)||!e.textContent.trim()||e.closest('[serigySchema]').getAttribute('serigySchema')!==schema))errors.push('primeira '+name);
return {item:name,presente:!!e};});
return {fields,errors,counts:['dc','ep'].map(k=>Array.from(document.getElementById(k+'-tabela').tBodies[0].rows).filter(r=>!r.hidden).length),totals:['empenhado','liquidado','pago'].map(k=>document.getElementById('dc-'+k).textContent),consulta:['dc','ep'].map(k=>document.getElementById(k+'-tabela').dataset.consulta)};
})()'''.replace('ITEMS',json.dumps(ITEMS)).replace('SCHEMA',json.dumps(SCHEMA))

def main():
    index=hashlib.sha256((ROOT/'.git/index').read_bytes()).hexdigest()
    data=dc.load();notes=ep.load()
    initial=Initial();initial.feed(dc.PAGE.read_text(encoding='utf-8'))
    assert initial.first==set(ITEMS) and initial.count>0
    assert all(x in initial.load for x in initial.wait)
    record=next(r for r in notes['registros'] if r['ano']==2025 and all(r.get(k) if k!='valor_atualizado' else r.get(k+'_centavos') is not None for k in ep.MARKS))
    year,month,entity=record['ano'],record['mes'],record['entidade']
    selected=[r for r in data['registros'] if (r['ano'],r['mes'],r['entidade'])==(year,month,entity)]
    selected_ep=[r for r in notes['registros'] if (r['ano'],r['mes'],r['entidade'])==(year,month,entity)]
    assert selected and selected_ep
    run=Path(tempfile.mkdtemp(prefix='despesas-marcacoes-',dir=ROOT/'trabalho'))
    old=deploy.SITE;deploy.SITE=run/'pages/transparencia.sergipeprevidencia'
    try:deploy.prepare('/transparencia.sergipeprevidencia',True)
    finally:deploy.SITE=old
    class Handler(SimpleHTTPRequestHandler):
        def log_message(self,*a):pass
        def do_GET(self):
            try:super().do_GET()
            except (ConnectionResetError,ConnectionAbortedError,BrokenPipeError):pass
    probe=socket.socket();probe.bind(('127.0.0.1',0));port=probe.getsockname()[1];probe.close()
    chrome=Path('C:/Program Files/Google/Chrome/Application/chrome.exe')
    process=subprocess.Popen([str(chrome),'--headless','--disable-gpu','--no-sandbox','--no-first-run','--remote-allow-origins=*',f'--remote-debugging-port={port}','--user-data-dir='+str(run/'chrome'),'about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    reports=[]
    try:
        for _ in range(100):
            try:
                with urlopen(f'http://127.0.0.1:{port}/json',timeout=1) as r:targets=json.load(r)
                break
            except OSError:time.sleep(.2)
        else:raise RuntimeError('Chrome/CDP indisponível')
        c=CDP(next(t['webSocketDebuggerUrl'] for t in targets if t['type']=='page'));c.call('Page.enable')
        for name,root,prefix in [('localhost',ROOT/'dist',''),('pages',run/'pages','/transparencia.sergipeprevidencia')]:
            server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(root)));Thread(target=server.serve_forever,daemon=True).start()
            try:
                route=prefix+'/Portal-da-Transparencia/Despesas/'
                c.call('Page.navigate',{'url':f'http://127.0.0.1:{server.server_port}'+route})
                for _ in range(200):
                    if c.js('location.pathname')==route and c.js('document.readyState')=='complete' and c.js('!!document.querySelector("#ep-tabela")'):break
                    time.sleep(.1)
                else:raise RuntimeError('HTTP/página não carregou')
                states=[]
                def check(label,empty=False):
                    snap=c.js(SNAPSHOT);assert not snap['errors'],(label,snap['errors'][:3])
                    assert all(f['presente']!=empty for f in snap['fields']),(label,snap['fields'])
                    if empty:assert snap['counts']==[0,0] and snap['totals']==['—']*3
                    states.append({'estado':label,'contagens':snap['counts'],'primeiras_ocorrencias_visiveis':not empty,'resultado_vazio_legitimo':empty})
                    return snap
                base=check('inicial');assert base['counts']==[40,667]
                for field,value in [('ano',str(year)),('mes',str(month)),('entidade',entity)]:
                    c.js('''(()=>{for(const id of ['dc-filtro','ep-filtro']){const el=document.getElementById(id).elements[FIELD];el.value=VALUE;el.dispatchEvent(new Event('change',{bubbles:true}));}})()'''.replace('FIELD',json.dumps(field)).replace('VALUE',json.dumps(value)))
                    snap=c.js(SNAPSHOT);assert not snap['errors']
                c.js("for(const id of ['dc-filtro','ep-filtro'])document.getElementById(id).dispatchEvent(new Event('submit',{cancelable:true}))")
                filtered=check('pesquisa combinada')
                assert filtered['counts']==[len(selected),len(selected_ep)]
                assert filtered['totals']==['R$ '+dc.money(sum(r[m+'_centavos'] for r in selected)) for m in dc.MEASURES]
                assert all(int(v)>int(old) for v,old in zip(filtered['consulta'],base['consulta']))
                for key,expected in [('dc',[dc.HEADERS]+[dc.cells(r) for r in selected]),('ep',[ep.HEADERS]+[ep.values(r) for r in selected_ep])]:
                    text=c.js('''(async()=>{let blob;const create=URL.createObjectURL,click=HTMLAnchorElement.prototype.click;URL.createObjectURL=b=>{blob=b;return 'blob:teste'};HTMLAnchorElement.prototype.click=function(){};try{document.getElementById(KEY+'-csv').click();return await blob.text()}finally{URL.createObjectURL=create;HTMLAnchorElement.prototype.click=click}})()'''.replace('KEY',json.dumps(key)))
                    assert list(csv.reader(io.StringIO(text.lstrip('\ufeff')),delimiter=';'))==expected
                    assert not ep.CPF.search(text)
                    (run/(name+'-'+key+'.csv')).write_text(text,encoding='utf-8')
                c.js("document.querySelector('#ep-tabela tr:not([hidden]) details summary').click()")
                assert c.js("!!document.querySelector('#ep-tabela tr:not([hidden]) details[open]')")
                c.js("for(const id of ['dc-filtro','ep-filtro']){const f=document.getElementById(id);f.elements.ano.value='2023';f.elements.entidade.value='FUNPREV';f.dispatchEvent(new Event('submit',{cancelable:true}))}")
                check('sem registros no período',True)
                c.js("for(const id of ['dc-filtro','ep-filtro'])document.getElementById(id).reset()")
                time.sleep(.1);reset=check('limpeza');assert reset['counts']==base['counts'] and reset['totals']==base['totals']
                reports.append({'base':name,'estados':states,'csvs_conferidos':2,'totais_conferidos':True})
            finally:server.shutdown();server.server_close()
    finally:process.terminate()
    assert hashlib.sha256((ROOT/'.git/index').read_bytes()).hexdigest()==index
    (run/'resultado.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding='utf-8')
    print('OK: 12 primeiras marcações visíveis no HTML inicial e Chrome; filtro combinado, mudanças de exercício/mês/entidade, vazio legítimo, limpeza, detalhes, totais e CSVs em localhost/Pages. Staging preservado.')
    print('Evidência:',run)

if __name__=='__main__':main()
