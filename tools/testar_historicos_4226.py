"""Testa os dois históricos da avaliação 4226 na cópia Pages."""
from pathlib import Path
import tempfile,subprocess,re,html,json,hashlib
from functools import partial
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
import preparar_deploy as deploy
root=Path(__file__).resolve().parents[1]
work=root/'trabalho/historicos-4226';work.mkdir(parents=True,exist_ok=True);run=Path(tempfile.mkdtemp(dir=work))
protected={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (root/'dist').rglob('*') if p.is_file()}
base='/transparencia.sergipeprevidencia';deploy.SITE=run/'pages'/base.strip('/');deploy.prepare(base,True)
reports=[]
for name,route,formid,tableid in [('tce','PlanejamentoPrestacaoContas/TCE','filtro-tce','tabela-tce'),('acordos','Convenios/SemTransferencia','filtro-acordos','tabela-acordos')]:
 page=(deploy.SITE/'Portal-da-Transparencia'/route/'index.html').read_text(encoding='utf-8')
 script='''<script>window.addEventListener('load',async()=>{
const form=document.getElementById(FORM),table=document.getElementById(TABLE),rows=Array.from(table.tBodies[0].rows),select=form.elements.ano,failures=[];let checks=0;const ok=(v,m)=>{checks++;if(!v)failures.push(m);};
const load=table.closest('[serigyLoadSection]');const initialLinks=Array.from(table.querySelectorAll('a')).map(a=>a.href);const marks=Array.from(document.querySelectorAll('[serigyItem="dataUltimaAtualizacao"]')).map(x=>x.textContent);
let previous=load.innerHTML;
for(const year of ['2026','2025','2024']){
const o=Array.from(select.options).find(o=>o.value===year);ok(!!o&&o.getAttribute('serigyValue')===year,'option '+year);select.value=year;form.dispatchEvent(new Event('change',{bubbles:true}));ok(select.value===year,'accepted '+year);ok(rows.filter(r=>!r.hidden).length===rows.filter(r=>r.dataset.year===year).length,'count '+year);ok(load.innerHTML!==previous,'result changed '+year);previous=load.innerHTML;form.dispatchEvent(new Event('submit',{cancelable:true}));ok(load.innerHTML===previous,'repeat submit '+year);select.dispatchEvent(new Event('change',{bubbles:true}));ok(load.innerHTML===previous,'repeat select '+year);
}
form.reset();await new Promise(r=>setTimeout(r,20));ok(!select.value&&rows.every(r=>!r.hidden),'clear');ok(JSON.stringify(initialLinks)===JSON.stringify(Array.from(table.querySelectorAll('a')).map(a=>a.href)),'links preserved');ok(JSON.stringify(marks)===JSON.stringify(Array.from(document.querySelectorAll('[serigyItem="dataUltimaAtualizacao"]')).map(x=>x.textContent)),'dates preserved');ok(select.getAttribute('serigyExecuteWaitSection')===load.getAttribute('serigyLoadSection'),'wait');const p=document.createElement('pre');p.id='result';p.textContent=JSON.stringify({checks,failures,records:rows.length});document.body.append(p);
});</script>'''.replace('FORM',json.dumps(formid)).replace('TABLE',json.dumps(tableid))
 class Handler(SimpleHTTPRequestHandler):
  def log_message(self,*a):pass
  def do_GET(self):
   if '?test=1' in self.path:
    self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(page.replace('</body>',script+'</body>').encode())
   else:
    try:super().do_GET()
    except (ConnectionAbortedError,BrokenPipeError):pass
 server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(deploy.SITE.parent)));Thread(target=server.serve_forever,daemon=True).start()
 try:
  url='http://127.0.0.1:'+str(server.server_port)+base+'/Portal-da-Transparencia/'+route+'/?test=1'
  r=subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+str(run/(name+'-chrome')),'--virtual-time-budget=4000','--dump-dom',url],capture_output=True,timeout=60);dom=r.stdout.decode('utf-8',errors='replace');(run/(name+'.html')).write_text(dom,encoding='utf-8');m=re.search(r'<pre id="result">(.*?)</pre>',dom,re.S);assert m;report=json.loads(html.unescape(m[1]));assert not report['failures'],report;reports.append(dict(page=name,**report))
 finally:server.shutdown();server.server_close()
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in protected.items())
print(json.dumps(reports,ensure_ascii=True))
