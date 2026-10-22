"""Conciliação com XLSX e teste de filtros/CSV em Chrome por HTTP local."""
from pathlib import Path
import csv,html,io,json,re,subprocess,tempfile,hashlib
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from threading import Thread
from urllib.request import urlopen
from integrar_licitacoes import ROOT,PAGE,render,records,date,money
page,data,opening=render();assert PAGE.read_text(encoding='utf-8')==page
assert page.count('data-source-row=')==len(data)
assert page.count('serigyItem="dataLicitacao"')==opening
assert 'serigyItem="sequencia"' not in page
for r in data:
    row=re.search(r'<tr data-source-row="'+str(r['linha'])+r'".*?</tr>',page,re.S)[0]
    for l in r['links']:assert html.escape(l['url'],quote=True) in row
protected={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'dist').rglob('*') if p.is_file()}
script='''<script>window.addEventListener('load',async()=>{
const f=document.getElementById('filtro-licitacoes'),t=document.getElementById('tabela-licitacoes'),rows=Array.from(t.tBodies[0].rows),b=document.getElementById('exportar-licitacoes');let checks=0;const failures=[];const ok=(x,m)=>{checks++;if(!x)failures.push(m);};const apply=()=>f.dispatchEvent(new Event('change'));const vis=()=>rows.filter(r=>!r.hidden);
for(const key of ['ano','modalidade','situacao','mes']){for(const opt of f.elements[key].options){f.elements[key].value=opt.value;apply();ok(vis().length===rows.filter(r=>!opt.value||r.dataset[key==='ano'?'year':key]===opt.value).length,key+opt.value);}f.elements[key].value='';}
const first=rows[0];f.elements.ano.value=first.dataset.year;f.elements.modalidade.value=first.dataset.modalidade;f.elements.situacao.value=first.dataset.situacao;f.elements.texto.value=first.cells[1].textContent;apply();ok(vis().length>=1,'combined');
let blob;URL.createObjectURL=x=>{blob=x;return 'blob:test';};URL.revokeObjectURL=()=>{};HTMLAnchorElement.prototype.click=function(){};b.click();const selected=await blob.text();const selectedCount=vis().length;
f.elements.texto.value='no-match-impossible';apply();ok(vis().length===0&&b.disabled,'no-match');f.reset();await new Promise(r=>setTimeout(r,20));ok(vis().length===rows.length,'reset');b.click();const all=await blob.text();
const p=document.createElement('pre');p.id='test-result';p.textContent=JSON.stringify({checks,failures,selected,selectedCount,all});document.body.append(p);
});</script>'''
class Handler(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
    def do_GET(self):
        if self.path.endswith('?test=1'):
            self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(page.replace('</body>',script+'</body>').encode())
        else:
            try:super().do_GET()
            except (ConnectionAbortedError,BrokenPipeError):pass
work=ROOT/'trabalho/licitacoes';work.mkdir(parents=True,exist_ok=True);run=Path(tempfile.mkdtemp(dir=work))
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(ROOT/'dist')));Thread(target=server.serve_forever,daemon=True).start();host='http://127.0.0.1:'+str(server.server_port);route='/Portal-da-Transparencia/Licitacoes/'
try:
    assert urlopen(host+route,timeout=10).status==200
    for path in set(re.findall(r'(?:src|href)="(/[^"#]*)"',page)):assert urlopen(host+path,timeout=10).status==200,path
    r=subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+str(run/'chrome'),'--virtual-time-budget=5000','--dump-dom',host+route+'?test=1'],capture_output=True,timeout=60);dom=r.stdout.decode('utf-8',errors='replace');(run/'browser.html').write_text(dom,encoding='utf-8');m=re.search(r'<pre id="test-result">(.*?)</pre>',dom,re.S);assert m,'Chrome sem resultado';report=json.loads(html.unescape(m[1]));assert not report['failures'],report['failures']
    for name,count in [('all',len(data)),('selected',report['selectedCount'])]:
        text=report.pop(name);parsed=list(csv.reader(io.StringIO(text.lstrip('\ufeff')),delimiter=';'));assert len(parsed)==count+1 and all(len(r)==10 for r in parsed)
        if name=='all':
            def value(v):return str(v).strip() if v is not None and str(v).strip() not in ('','-') else 'Não informado'
            for r,cells in zip(data,parsed[1:]):
                v=r['valores'];expected=[value(v[0]),value(v[6]),value(v[7]),value(v[9]),value(v[11]),value(date(v[14])),value(money(v[23])),value(money(v[24])),value(v[5])];assert cells[:9]==expected,(r['linha'],cells[:9],expected)
                for l in r['links']:assert l['url'] in cells[9]
        (run/(name+'.csv')).write_text(text,encoding='utf-8')
finally:server.shutdown();server.server_close()
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in protected.items())
print(json.dumps(dict(report,registros=len(data),aberturas=opening,links=sum(len(r['links']) for r in data),CSV='conciliado campo a campo; links preservados',demais_paginas='preservadas'),ensure_ascii=True))
