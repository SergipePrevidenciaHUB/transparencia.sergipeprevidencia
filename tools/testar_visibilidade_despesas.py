"""Verifica a apresentação inicial de 4.1.4–10 em localhost e Pages."""
from pathlib import Path
import tempfile,subprocess,re,json,html,csv,io,hashlib
from functools import partial
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
import preparar_deploy as deploy
ROOT=Path(__file__).resolve().parents[1]
route='/Portal-da-Transparencia/Despesas/'
protected={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'dist').rglob('*') if p.is_file()}
work=ROOT/'trabalho/despesas-visibilidade';work.mkdir(parents=True,exist_ok=True);run=Path(tempfile.mkdtemp(dir=work))
deploy.SITE=run/'pages'/'transparencia.sergipeprevidencia';deploy.prepare('/transparencia.sergipeprevidencia',True)
script='''<script>window.addEventListener('load',async()=>{
const failures=[];let checks=0;const ok=(x,m)=>{checks++;if(!x)failures.push(m);};const t=document.getElementById('despesas-classificacao-tabela'),f=document.getElementById('despesas-classificacao-filtro'),rows=Array.from(t.querySelectorAll('tr[data-dado-sintetico]'));const visible=e=>!!e&&e.getClientRects().length>0&&getComputedStyle(e).visibility==='visible'&&!e.closest('[hidden]');
const fields=['unidadeDespesa','funcaoDespesa','subFuncaoDespesa','categoriaDespesa','grupoDespesa','elementoDespesa','fonteRecursosDespesa'];
fields.forEach(k=>ok(visible(rows[0].querySelector('[serigyItem="'+k+'"]')),'initial '+k));ok(rows.every(visible),'initial all rows');ok(document.querySelector('[data-despesas-sinteticas]').textContent.includes('DADOS SINTÉTICOS'),'warning');
const category=t.querySelector('[data-classificacao-nivel="categoria"] button');category.click();ok(!visible(rows[0]),'collapse category');category.click();ok(visible(rows[0]),'expand category');const group=t.querySelector('[data-classificacao-nivel="grupo"] button');group.click();ok(!visible(rows[0]),'collapse group');group.click();ok(visible(rows[0]),'expand group');
f.elements.ano.value='2026';f.elements.mes.value='1';f.elements.codigo_uo.value='37201';f.elements.elemento.value=rows[8].querySelector('[serigyItem="elementoDespesa"]').textContent;f.dispatchEvent(new Event('submit',{cancelable:true}));ok(rows.filter(visible).length===1,'combined filters');
let blob;URL.createObjectURL=x=>{blob=x;return 'blob:test';};URL.revokeObjectURL=()=>{};HTMLAnchorElement.prototype.click=function(){};document.getElementById('despesas-classificacao-csv').click();const selected=await blob.text();f.reset();await new Promise(r=>setTimeout(r,20));ok(rows.every(visible),'reset');document.getElementById('despesas-classificacao-csv').click();const all=await blob.text();ok(document.querySelectorAll('#despesas-totais-tabela tbody tr').length===8,'4.1 preserved');
const p=document.createElement('pre');p.id='result';p.textContent=JSON.stringify({checks,failures,selected,all});document.body.append(p);
});</script>'''
reports=[]
for name,source,prefix in [('local',ROOT/'dist',''),('pages',deploy.SITE,'/transparencia.sergipeprevidencia')]:
 page=(source/route.strip('/')/'index.html').read_text(encoding='utf-8')
 class Handler(SimpleHTTPRequestHandler):
  def log_message(self,*args):pass
  def do_GET(self):
   if '?test=1' in self.path:
    self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(page.replace('</body>',script+'</body>').encode())
   else:
    try:super().do_GET()
    except (ConnectionAbortedError,BrokenPipeError):pass
 server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(source.parent if prefix else source)));Thread(target=server.serve_forever,daemon=True).start()
 try:
  url='http://127.0.0.1:'+str(server.server_port)+prefix+route+'?test=1'
  result=subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+str(run/(name+'-chrome')),'--virtual-time-budget=5000','--dump-dom',url],capture_output=True,timeout=60);dom=result.stdout.decode('utf-8',errors='replace');(run/(name+'.html')).write_text(dom,encoding='utf-8');m=re.search(r'<pre id="result">(.*?)</pre>',dom,re.S);assert m,'Chrome sem resultado';r=json.loads(html.unescape(m[1]));assert not r['failures'],r['failures']
  for key,count in [('all',10),('selected',1)]:
   text=r.pop(key);parsed=list(csv.reader(io.StringIO(text.lstrip('\ufeff')),delimiter=';'));assert len(parsed)==count+1 and all(len(v)==10 for v in parsed);assert all('DADOS SINTÉTICOS' in v[-1] for v in parsed[1:]);(run/(name+'-'+key+'.csv')).write_text(text,encoding='utf-8')
  reports.append(dict(base=name,**r))
 finally:server.shutdown();server.server_close()
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in protected.items())
print(json.dumps(reports,ensure_ascii=True))
