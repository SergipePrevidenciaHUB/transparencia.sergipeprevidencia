"""Verifica HTML, Chrome/CSV, bloqueio oficial e desativação em cópia."""
from pathlib import Path
import hashlib,json,re,subprocess,tempfile,html,csv,io
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from functools import partial
from threading import Thread
from urllib.request import urlopen
import preparar_teste_ordem as gen
import preparar_deploy as deploy
page=gen.PAGE.read_text(encoding='utf-8');assert page==gen.render(True)
for item,count in [('dataVencimento',4),('dataPagamento',4),('credor',4),('valorPagamento',4),('filtroPesquisa',1),('salvarRelatorio',1),('historicoExercicio',1),('dataUltimaAtualizacao',1)]:assert page.count('serigyItem="'+item+'"')==count,item
protected={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (gen.ROOT/'dist').rglob('*') if p.is_file()}
work=gen.ROOT/'trabalho/ordem-sintetica';work.mkdir(parents=True,exist_ok=True);run=Path(tempfile.mkdtemp(dir=work));fixture=run/'isolado';fixture.mkdir();(fixture/'index.html').write_text(page,encoding='utf-8')
original_dist=deploy.DIST;deploy.DIST=fixture
try:
    for base,allow in [('',False),('/Portal-da-Transparencia',True),('/transparencia.sergipeprevidencia',False)]:
        try:deploy.check_synthetic_content(base,allow)
        except ValueError:pass
        else:raise AssertionError('Bloqueio falhou')
    deploy.check_synthetic_content('/transparencia.sergipeprevidencia',True)
    clean=gen.render(False);assert 'data-dado-sintetico' not in clean and 'ordem-teste.js' not in clean;assert gen.BASE_MAIN in clean
    (fixture/'index.html').write_text(clean,encoding='utf-8');deploy.check_synthetic_content('',False)
finally:deploy.DIST=original_dist
script='''<script>window.addEventListener('load',async()=>{
const failures=[];let checks=0;const ok=(v,m)=>{checks++;if(!v)failures.push(m);};const f=document.getElementById('filtro-ordem'),t=document.getElementById('tabela-ordem'),rows=Array.from(t.tBodies[0].rows),b=document.getElementById('exportar-ordem');const apply=()=>f.dispatchEvent(new Event('change'));const vis=()=>rows.filter(r=>!r.hidden);
ok(rows.length===4,'rows');for(const y of ['2023','2024','2025','2026']){f.elements.ano.value=y;apply();ok(vis().length===1&&vis()[0].dataset.year===y,'history '+y);}
f.elements.mes.value='10';f.elements.credor.value='ensaio 4';apply();ok(vis().length===1,'combined');
let blob;URL.createObjectURL=x=>{blob=x;return 'blob:test';};URL.revokeObjectURL=()=>{};HTMLAnchorElement.prototype.click=function(){};b.click();const selected=await blob.text();
f.elements.credor.value='no-match';f.dispatchEvent(new Event('submit',{cancelable:true}));ok(vis().length===0&&b.disabled,'submit empty');f.reset();await new Promise(r=>setTimeout(r,20));ok(vis().length===4,'reset');b.click();const all=await blob.text();
const p=document.createElement('pre');p.id='result';p.textContent=JSON.stringify({checks,failures,selected,all});document.body.append(p);
});</script>'''
class Handler(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
    def do_GET(self):
        if self.path.endswith('?test=1'):
            self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(page.replace('</body>',script+'</body>').encode())
        else:
            try:super().do_GET()
            except (ConnectionAbortedError,BrokenPipeError):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(gen.ROOT/'dist')));Thread(target=server.serve_forever,daemon=True).start();host='http://127.0.0.1:'+str(server.server_port);route='/Portal-da-Transparencia/Contratos/OrdemCronologica/'
try:
    assert urlopen(host+route,timeout=10).status==200
    for path in set(re.findall(r'(?:href|src)="(/[^"#]*)"',page)):assert urlopen(host+path,timeout=10).status==200,path
    p=subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+str(run/'chrome'),'--virtual-time-budget=5000','--dump-dom',host+route+'?test=1'],capture_output=True,timeout=60);dom=p.stdout.decode('utf-8',errors='replace');(run/'browser.html').write_text(dom,encoding='utf-8');m=re.search(r'<pre id="result">(.*?)</pre>',dom,re.S);assert m,'Chrome sem resultado';report=json.loads(html.unescape(m[1]));assert not report['failures'],report
    for name,count in [('all',4),('selected',1)]:
        text=report.pop(name);parsed=list(csv.reader(io.StringIO(text.lstrip('\ufeff')),delimiter=';'));assert len(parsed)==count+1 and all(len(r)==5 for r in parsed)
        for r in parsed[1:]:
            assert r[0]==gen.NOTICE;idx=int(r[3].split('ENSAIO ')[1].split()[0]);year=2022+idx;assert r[1:]==[f'10/10/{year}',f'12/10/{year}',f'CREDOR FICTÍCIO DE ENSAIO {idx} — NÃO EXISTE',f'R$ {idx*100},00']
        (run/(name+'.csv')).write_text(text,encoding='utf-8')
finally:server.shutdown();server.server_close()
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in protected.items())
print(json.dumps(dict(report,registros=4,CSV='conciliado',bloqueio='isolado aprovado',remocao='reversivel em copia',dist='preservado'),ensure_ascii=True))
