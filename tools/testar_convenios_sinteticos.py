"""Teste local de 5.1/5.2 sintéticos; não publica nem executa Invoker."""
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
from urllib.request import urlopen
from urllib.parse import urlsplit
import json,re,runpy,tempfile,subprocess,html,csv,io,hashlib
protected={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__).resolve().parents[1]/'dist').rglob('*') if p.is_file()}
ROOT=Path(__file__).resolve().parents[1];W=ROOT/'trabalho/convenios-teste';W.mkdir(parents=True,exist_ok=True);run=Path(tempfile.mkdtemp(dir=W));d=runpy.run_path(str(ROOT/'tools/preparar_deploy.py'));g=d['prepare'].__globals__;iso=run/'isolado';iso.mkdir();base='/transparencia.sergipeprevidencia'
for n in ['Recebidas','Realizadas']:
 s=(ROOT/'dist/Portal-da-Transparencia/Convenios'/n/'index.html').read_text(encoding='utf-8');(iso/(n+'.html')).write_text(s,encoding='utf-8');assert '01/2018 a 10/2026' in s and '21/10/2026' in s;assert s.count('<tr data-dado-sintetico="true"')==4
 g['DIST']=iso;g['SITE']=run/'preservar';g['SITE'].mkdir(exist_ok=True);sentinel=g['SITE']/'anterior.txt';sentinel.write_text('preservar')
 for b,a in [('',False),('/Portal-da-Transparencia',True),(base,False)]:
  try:d['prepare'](b,a)
  except ValueError:assert sentinel.read_text()=='preservar'
  else:raise AssertionError('Origem isolada não bloqueada')
(iso/'CNAME').write_text('sergipeprevidencia.se.gov.br')
try:d['prepare'](base,True)
except ValueError:assert sentinel.exists()
else:raise AssertionError('CNAME permitido')
g['DIST']=ROOT/'dist';g['SITE']=run/'pages'/base.strip('/');d['prepare'](base,True)
script=r"""<script>window.addEventListener('load',async()=>{let checks=0;const failures=[];function check(v,m){checks++;if(!v)failures.push(m);}const f=document.getElementById('filtro-convenios'),table=document.getElementById('tabela-convenios'),rows=Array.from(table.tBodies[0].rows),isReceived=document.querySelector('h1').textContent.includes('Recebidas');const fields=['identificaTransferencia',isReceived?'orgaoRepassador':'orgaoBeneficiario','vigenciaConvenio','objetoConvenio',isReceived?'valorTotalPrevisto':'valorTotalRepasse','valorRepassado','anexoConvenio'];fields.concat(['filtroPesquisa','salvarRelatorio','dataUltimaAtualizacao','historicoExercicio']).forEach(k=>check(!!document.querySelector('[serigyItem="'+k+'"]')&&Array.from(document.querySelectorAll('[serigyItem="'+k+'"]')).every(e=>e.closest('[serigySchema]').getAttribute('serigySchema')==='https://serigy.tce.se.gov.br/comum/convenios-transferencias.html'),'marca '+k));check(rows.length===4,'HTML inicial');check(rows.every(r=>r.lastElementChild.textContent.includes('DADOS SINTÉTICOS PARA TESTE DO SERIGY')),'aviso por registro');check(document.getElementById('aviso-convenios').getClientRects().length>0,'aviso visível');check(document.getElementById('declaracao-oficial').getClientRects().length>0,'declaração separada');check(f.elements.ano.getAttribute('serigyExecuteWaitSection')===document.querySelector('[serigyLoadSection]').getAttribute('serigyLoadSection'),'wait/load');for(const o of Array.from(f.elements.ano.options)){f.elements.ano.value=o.value;f.dispatchEvent(new Event('change',{bubbles:true}));let shown=rows.filter(r=>!r.hidden);check(shown.length===(o.value?1:4),'change '+o.value);if(o.value){check(shown[0].dataset.year===o.value,'ano '+o.value);check(o.getAttribute('serigyValue')===o.value,'histórico '+o.value);}f.dispatchEvent(new Event('submit',{cancelable:true,bubbles:true}));check(rows.filter(r=>!r.hidden).length===shown.length,'submit '+o.value);}
async function capture(){let blob,name;URL.createObjectURL=b=>{blob=b;return 'blob:teste';};URL.revokeObjectURL=()=>{};HTMLAnchorElement.prototype.click=function(){name=this.download;};document.getElementById('csv-convenios').click();check(name.includes('SINTETICOS-TESTE-SERIGY'),'nome CSV');return await blob.text();}f.elements.ano.value='2024';f.dispatchEvent(new Event('submit',{cancelable:true,bubbles:true}));const selected=await capture();f.reset();await new Promise(r=>setTimeout(r,40));check(rows.every(r=>!r.hidden),'limpar');const all=await capture();const pre=document.createElement('pre');pre.id='resultado';pre.textContent=JSON.stringify({checks,failures,selected,all});document.body.append(pre);});</script>"""
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
 def do_GET(self):
  if '?teste' not in self.path:return super().do_GET()
  s=(Path(self.directory)/self.path.split('?')[0].lstrip('/')/'index.html').read_text(encoding='utf-8');self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(s.replace('</body>',script+'</body>').encode())
results=[];links=0;documents=0
for directory,prefix in [(ROOT/'dist',''),(g['SITE'].parent,base)]:
 server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(directory)));Thread(target=server.serve_forever,daemon=True).start();host='http://127.0.0.1:'+str(server.server_port)
 try:
  for n in ['Recebidas','Realizadas']:
   route=prefix+'/Portal-da-Transparencia/Convenios/'+n+'/'
   with urlopen(host+route,timeout=10) as r:s=r.read().decode();assert r.status==200
   for link in set(re.findall(r'(?:href|src)="(/[^\"]*)',s)):
    u=urlsplit(link)
    with urlopen(host+u.path,timeout=10) as r:doc=r.read().decode('utf-8',errors='replace');assert r.status==200;links+=1
    if u.fragment:assert 'id="'+u.fragment+'"' in doc and 'data-dado-sintetico' in doc;documents+=1
   b=subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+str(run/('chrome'+str(len(results)))),'--virtual-time-budget=4000','--dump-dom',host+route+'?teste=1'],capture_output=True,timeout=45);dom=b.stdout.decode('utf-8',errors='replace');(run/('dom'+str(len(results))+'.html')).write_text(dom,encoding='utf-8');m=re.search(r'<pre id="resultado">(.*?)</pre>',dom,re.S);assert m,'Sem resultado Chrome';v=json.loads(html.unescape(m[1]));assert not v['failures'],v
   for key,count in [('selected',1),('all',4)]:
    text=v.pop(key);data=list(csv.reader(io.StringIO(text.lstrip(chr(65279))),delimiter=';'));assert len(data)==count+1 and len(data[0])==8;assert all('DADOS SINTÉTICOS PARA TESTE DO SERIGY' in row[-1] and 'documentos-sinteticos.html#instrumento-' in row[-2] for row in data[1:]);years=[2024] if key=='selected' else list(range(2023,2027))
    for row,y in zip(data[1:],years):i=y-2022;assert row[0]==f'{91000+i}/{y}' and row[4:6]==[f'{i}.000,00',f'{i}00,00']
    (run/(n+prefix.replace('/','-')+'-'+key+'.csv')).write_text(text,encoding='utf-8')
   results.append(v)
 finally:server.shutdown();server.server_close()
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in protected.items())
report=dict(checks=sum(v['checks'] for v in results),falhas=[],links_http=links,documentos_com_ancora=documents,bloqueios=7,linhas_recebidas=4,linhas_realizadas=4,demais_arquivos_dist_preservados=True);(W/'resultado.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(report,ensure_ascii=False))
