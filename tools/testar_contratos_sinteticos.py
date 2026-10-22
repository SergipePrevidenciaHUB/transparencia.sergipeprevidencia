"""Testa ensaio isolado, pacote Pages e bloqueio oficial, sem publicação."""
from pathlib import Path
import csv, html, io, json, re, subprocess, tempfile
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from urllib.request import urlopen
import integrar_contratos as gen
import preparar_deploy as deploy

root=gen.ROOT
work=root/'trabalho/contratos-sinteticos'
work.mkdir(parents=True,exist_ok=True)
run=Path(tempfile.mkdtemp(dir=work))
real=gen.render(False)
page=gen.PAGE.read_text(encoding='utf-8')
assert page==gen.render(True)
assert re.findall(r'<tr data-source-row=.*?</tr>',page,re.S)==re.findall(r'<tr data-source-row=.*?</tr>',real,re.S)
assert real.count('data-source-row=')==156 and real.count('serigyItem="linkContrato"')==122 and real.count('serigyItem="termoAditivo"')==8
assert 'data-dado-sintetico' not in real
assert all(real.count('serigyItem="'+x+'"')==0 for x in ['valorContrato','sequencia'])
assert page.count('serigyItem="valorContrato"')==page.count('serigyItem="sequencia"')==3
# Isolar o contrato: outros ensaios não podem mascarar a eficácia do bloqueio.
fixture=run/'somente-contratos';fixture.mkdir();(fixture/'index.html').write_text(page,encoding='utf-8')
original_dist=deploy.DIST;deploy.DIST=fixture
try:
    for base,allow in [('',False),('/Portal-da-Transparencia',True),('/transparencia.sergipeprevidencia',False)]:
        try: deploy.check_synthetic_content(base,allow)
        except ValueError: pass
        else: raise AssertionError('Bloqueio oficial falhou')
    deploy.check_synthetic_content('/transparencia.sergipeprevidencia',True)
    (fixture/'index.html').write_text(real,encoding='utf-8')
    deploy.check_synthetic_content('',False)
finally:deploy.DIST=original_dist
base='/transparencia.sergipeprevidencia'
deploy.SITE=run/'pages'/base.strip('/')
deploy.prepare(base,True)
route=base+'/Portal-da-Transparencia/Contratos/'
prepared=(deploy.SITE/'Portal-da-Transparencia/Contratos/index.html').read_text(encoding='utf-8')
script='''<script>window.addEventListener('load',async()=>{
const failures=[];function ok(x,m){if(!x)failures.push(m);}
const f=document.getElementById('filtro-contratos-teste'),t=document.getElementById('tabela-contratos-teste'),b=document.getElementById('exportar-contratos-teste');const rows=Array.from(t.tBodies[0].rows);const apply=()=>f.dispatchEvent(new Event('change'));const visible=()=>rows.filter(r=>!r.hidden);
ok(rows.length===3,'rows');ok(rows.every(r=>r.textContent.includes('DADO SINTÉTICO — TESTE SERIGY')),'notice');
for(const y of ['2024','2025','2026']){f.elements.ano.value=y;apply();ok(visible().length===1&&visible()[0].dataset.year===y,'year '+y);}
f.elements.texto.value='FICTÍCIA';apply();ok(visible().length===1,'combined');f.elements.texto.value='no-match';apply();ok(!visible().length&&b.disabled,'no result');
f.reset();await new Promise(r=>setTimeout(r,10));ok(visible().length===3,'reset');
let blob;URL.createObjectURL=x=>{blob=x;return 'blob:test';};URL.revokeObjectURL=()=>{};HTMLAnchorElement.prototype.click=function(){};
b.click();const all=await blob.text();f.elements.ano.value='2025';apply();b.click();const selected=await blob.text();
for(const a of t.querySelectorAll('a')){ok(a.hash&&document.getElementById(a.hash.slice(1)),'document target');ok((await fetch(a.href)).ok,'document HTTP');}
ok(document.querySelectorAll('#tabela-contratos tbody tr').length===156,'real rows');
const p=document.createElement('pre');p.id='result';p.textContent=JSON.stringify({failures,all,selected});document.body.append(p);
});</script>'''
class Handler(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
    def do_GET(self):
        if self.path==route+'?test=1':
            self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(prepared.replace('</body>',script+'</body>').encode())
        else:
            try:super().do_GET()
            except (ConnectionAbortedError, BrokenPipeError):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(deploy.SITE.parent)))
Thread(target=server.serve_forever,daemon=True).start()
host='http://127.0.0.1:'+str(server.server_port)
try:
    assert urlopen(host+route,timeout=10).status==200
    for path in re.findall(r'(?:href|src)="('+re.escape(base)+r'/[^"]+)"',prepared):
        assert urlopen(host+path,timeout=10).status==200,path
    browser=subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+str(run/'chrome'),'--virtual-time-budget=6000','--dump-dom',host+route+'?test=1'],capture_output=True,timeout=60)
    dom=browser.stdout.decode('utf-8',errors='replace');(run/'browser.html').write_text(dom,encoding='utf-8')
    match=re.search(r'<pre id="result">(.*?)</pre>',dom,re.S);assert match,'Chrome sem resultado';report=json.loads(html.unescape(match[1]));assert not report['failures'],report['failures']
    for key,count in [('all',3),('selected',1)]:
        text=report[key];records=list(csv.reader(io.StringIO(text.lstrip('\ufeff')),delimiter=';'))
        assert len(records)==count+1 and all(len(r)==9 for r in records)
        assert all(gen.NOTICE in r[1] for r in records[1:])
        (run/(key+'.csv')).write_text(text,encoding='utf-8')
finally:server.shutdown();server.server_close()
assert gen.render(False)==real
print('OK: 3 sintéticos; filtros/histórico/CSV/documentos HTTP no pacote Pages; bloqueio oficial isolado; remoção preserva 156/122/8.')
