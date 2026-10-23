"""Confere resoluções, preservação das portarias, filtros e CSV em Chrome local."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
import hashlib, html, json, re, subprocess, tempfile
import importar_portarias as gen

root=Path(__file__).resolve().parents[1]
page=gen.PAGE.read_text(encoding='utf-8')
records=gen.read_records();links=gen.read_links(records)
planned=gen.read_planned_links(records,links)
assert len(planned)==9 and len(set(planned.values()))==9
assert all(html.escape(url,quote=True) in page for url in planned.values())
assert page.count('data-type="Portaria"')==323
assert all(html.escape(url,quote=True) in page for url in links.values())
audit=json.loads((root/'controle/resolucoes-vinculos.json').read_text(encoding='utf-8'))['registros']
confirmed=[r for r in audit if r['situacao']=='CONFIRMADO']
assert page.count('data-type="Resolução"')==len(confirmed)
assert all(html.escape(r['url'],quote=True) in page for r in confirmed)
assert all(r.get('url_planejada','URL_PLANEJADA_AUSENTE') not in page for r in audit)
assert page.count('dataUltimaAtualizacao')==1
assert page.count('<table ')==1
assert page.count('serigyItem="atoNormativo"')==381
outside=page.split(gen.START)[0]+page.split(gen.END)[-1]
assert not re.search(r'acervo parcial|protótipo|pendente|validação|acervo incompleto',outside,re.I)
assert len(confirmed)==58
for r in records:
 assert html.escape(r['title']) in page and html.escape(r['date']) in page and html.escape(r['description']) in page
for r in confirmed:
 assert html.escape(r['ementa']) in page and html.escape(r['data']) in page
 assert f"Resolução {r['colegiado']} {r['numero']:03d}/{r['ano']}" in page
work=root/'trabalho/atos-testes';work.mkdir(parents=True,exist_ok=True)
run=Path(tempfile.mkdtemp(dir=work))
index_hash=hashlib.sha256((root/'.git/index').read_bytes()).hexdigest()
script='''<script>
function reportFailure(message){const p=document.createElement('pre');p.id='test-result';p.textContent=JSON.stringify({checks:0,errors:[String(message)]});document.body.append(p);}
window.addEventListener('error',e=>reportFailure(e.message));
window.addEventListener('unhandledrejection',e=>reportFailure(e.reason));
window.addEventListener('load',async()=>{
let checks=0;const errors=[];const ok=(v,m)=>{checks++;if(!v)errors.push(m);};
let blob;URL.createObjectURL=b=>{blob=b;return 'blob:test';};HTMLAnchorElement.prototype.click=function(){};
const NativeBlob=window.Blob;window.Blob=class extends NativeBlob{constructor(parts,options){super(parts,options);this.csv=parts.join('');}};
const id='atos-tabela',table=document.getElementById(id),form=document.querySelector('[data-target="'+id+'"]'),rows=Array.from(table.tBodies[0].rows);
ok(rows.length===381,'initial total');
ok(rows.filter(r=>r.dataset.type==='Portaria').every(r=>r.querySelector('a[href]')),'all portarias linked');
ok(rows.filter(r=>r.querySelector('th a')).length===9,'nine planned title links');
const apply=()=>form.dispatchEvent(new Event('submit',{cancelable:true}));
const visible=()=>rows.filter(r=>!r.hidden);
const quote=v=>'"'+v.replace(/"/g,'""')+'"';
async function csvCheck(label){
 exportarAtos(id);const csv=blob.csv.replace(/^\\uFEFF/,'');
 ok(csv.split('\\r\\n').length===visible().length+1,label+' CSV count');
 const expected=visible().map(r=>{const c=r.querySelectorAll('td, th');return [c[0].textContent,c[1].textContent,c[2].textContent,(c[3].querySelector('[data-search-text]')||c[3]).textContent,r.querySelector('a[href]')?.href||''].map(quote).join(';');});
 ok(csv.split('\\r\\n').slice(1).join('\\r\\n')===expected.join('\\r\\n'),label+' CSV exact rows');
 ok(parseInt(document.querySelector('[data-count-for="atos-tabela"]').textContent)===visible().length,label+' status');
}
for(const [type,count] of [['',381],['Portaria',323],['Resolução',58]]){
 form.reset();await new Promise(r=>setTimeout(r,20));form.elements.tipo.value=type;apply();
 ok(visible().length===count,'type '+type);await csvCheck('type '+type);
 form.elements.ano.value='2026';apply();
 ok(visible().length===rows.filter(r=>(!type||r.dataset.type===type)&&r.dataset.year==='2026').length,'type/year '+type);await csvCheck('year '+type);
 form.elements.palavra.value=type==='Portaria'?'98/2026':'CIRP';apply();
 ok(visible().length>0,'combined nonempty '+type);
 ok(visible().every(r=>r.dataset.year==='2026'&&(!type||r.dataset.type===type)&&r.textContent.includes(form.elements.palavra.value)),'combined '+type);await csvCheck('combined '+type);
 form.elements.palavra.value='PALAVRA_INEXISTENTE_XYZ';apply();ok(visible().length===0,'empty '+type);await csvCheck('empty '+type);
 form.reset();await new Promise(r=>setTimeout(r,20));ok(visible().length===381,'clear '+type);
}
await csvCheck('all restored');
const p=document.createElement('pre');p.id='test-result';p.textContent=JSON.stringify({checks,errors});document.body.append(p);
});</script>'''
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
 def do_GET(self):
  if self.path.endswith('?test=1'):
   self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(page.replace('</body>',script+'</body>').encode())
  else:super().do_GET()
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(root/'dist')))
Thread(target=server.serve_forever,daemon=True).start()
try:
 url=f'http://127.0.0.1:{server.server_port}/Portal-da-Transparencia/Institucional/AtosNormativos/?test=1'
 result=subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+str(run/'chrome'),'--virtual-time-budget=4000','--dump-dom',url],capture_output=True,timeout=60)
 dom=result.stdout.decode('utf-8',errors='replace');m=re.search(r'<pre id="test-result">(.*?)</pre>',dom,re.S)
 (run/'dom.html').write_text(dom,encoding='utf-8')
 assert m, result.stderr.decode(errors='replace')[-1000:]
 report=json.loads(html.unescape(m[1]));assert not report['errors'],report
 assert hashlib.sha256((root/'.git/index').read_bytes()).hexdigest()==index_hash
 print(json.dumps(dict(portarias=323,links_portarias=len(links),resolucoes=len(confirmed),**report)))
finally:server.shutdown();server.server_close()
