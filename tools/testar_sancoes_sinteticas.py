"""Confere ensaio de Sanções, CSV e bloqueio único de publicação; não executa Invoker."""
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from functools import partial
from urllib.request import urlopen
from html.parser import HTMLParser
import csv,io,tempfile,runpy,re,subprocess,html,json,hashlib
ROOT=Path(__file__).resolve().parents[1];WORK=ROOT/'trabalho/sancoes-sinteticas';WORK.mkdir(parents=True,exist_ok=True);RUN=Path(tempfile.mkdtemp(dir=WORK))
route='/Portal-da-Transparencia/Licitacoes/Sancoes/';source=(ROOT/'dist'/route.strip('/')/'index.html').read_text(encoding='utf-8')
items=['nomeSancionado','idSancionado','filtroPesquisa','salvarRelatorio','dataUltimaAtualizacao','historicoExercicio']
assert all('serigyItem="'+k+'"' in source for k in items)
assert len(re.findall(r'<tr data-dado-sintetico="true"',source))==4
protected={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'dist').rglob('*') if p.is_file()}
deploy=runpy.run_path(str(ROOT/'tools/preparar_deploy.py'));g=deploy['prepare'].__globals__
isolated=RUN/'sic-isolado';isolated.mkdir();(isolated/'index.html').write_text(source,encoding='utf-8');g['DIST']=isolated;g['SITE']=RUN/'nao-tocar';g['SITE'].mkdir();sentinel=g['SITE']/'preservar.txt';sentinel.write_text('preservar')
for base,allow in [('',False),('/Portal-da-Transparencia',True),('/transparencia.sergipeprevidencia',False)]:
 try:deploy['prepare'](base,allow)
 except ValueError:assert sentinel.read_text()=='preservar'
 else:raise AssertionError('SIC isolado não bloqueado')
(isolated/'CNAME').write_text('sergipeprevidencia.se.gov.br')
try:deploy['prepare']('/transparencia.sergipeprevidencia',True)
except ValueError:assert sentinel.exists()
else:raise AssertionError('CNAME permitido')
# Simular retirada do ensaio sem alterar arquivos públicos nem a declaração real.
clean=RUN/'sem-ensaio';clean.mkdir()
without=re.sub(r'<section id="ensaio-sancoes"[\s\S]*?</section>','',source,count=1)
without=without.replace('  <script defer src="/assets/js/sancoes-teste.js"></script>\n','')
assert 'O SergipePrevidência informa que não houve licitantes ou contratados sancionados administrativamente pela própria unidade até 21/10/2026.' in without
assert '<time datetime="2026-10-21">21/10/2026</time>' in without
assert 'data-dado-sintetico' not in without
(clean/'index.html').write_text(without,encoding='utf-8');g['DIST']=clean
deploy['check_synthetic_content']('',False)
g['DIST']=ROOT/'dist';base='/transparencia.sergipeprevidencia';g['SITE']=RUN/'pages'/base.strip('/');deploy['prepare'](base,True)
script=r"""<script>window.addEventListener('load',async()=>{let checks=0;const failures=[];function check(v,m){checks++;if(!v)failures.push(m);}const f=document.getElementById('filtro-sancoes'),table=document.getElementById('tabela-sancoes'),rows=Array.from(table.tBodies[0].rows),status=document.getElementById('contagem-sancoes'),warning=document.getElementById('aviso-sancoes').textContent.trim();const keys=['nomeSancionado','idSancionado','filtroPesquisa','salvarRelatorio','dataUltimaAtualizacao','historicoExercicio'];keys.forEach(k=>check(Array.from(document.querySelectorAll('[serigyItem="'+k+'"]')).every(e=>e.closest('[serigySchema]').getAttribute('serigySchema')==='https://serigy.tce.se.gov.br/comum/licitacoes.html')&&!!document.querySelector('[serigyItem="'+k+'"]'),'marcação '+k));check(rows.length===4,'HTML inicial');check(document.getElementById('aviso-sancoes').getClientRects().length>0,'aviso visível');check(f.elements.exercicio.getAttribute('serigyExecuteWaitSection')===document.getElementById('resultados-sancoes').getAttribute('serigyLoadSection'),'wait/load');for(const o of Array.from(f.elements.exercicio.options)){f.elements.exercicio.value=o.value;f.dispatchEvent(new Event('change',{bubbles:true}));const shown=rows.filter(r=>!r.hidden);check(shown.length===(o.value?1:4),'filtro '+o.value);if(o.value){check(o.getAttribute('serigyValue')===o.value,'histórico '+o.value);check(shown[0].dataset.year===o.value,'ano '+o.value);}const before=status.textContent;f.dispatchEvent(new Event('submit',{cancelable:true,bubbles:true}));check(status.textContent===before,'pesquisa '+o.value);}
async function capture(){let blob,filename;URL.createObjectURL=b=>{blob=b;return 'blob:teste';};URL.revokeObjectURL=()=>{};HTMLAnchorElement.prototype.click=function(){filename=this.download;};document.getElementById('csv-sancoes').click();check(filename.includes('SINTETICOS-TESTE-SERIGY'),'arquivo identificado');const text=await blob.text();check(text.includes(warning),'CSV aviso');return {filename,text};}f.elements.exercicio.value='2024';f.dispatchEvent(new Event('submit',{cancelable:true,bubbles:true}));const selected=await capture();f.reset();await new Promise(r=>setTimeout(r,40));check(rows.every(r=>!r.hidden),'limpar');const all=await capture();check(table.tBodies[0].rows.length===4,'preservar base');const pre=document.createElement('pre');pre.id='teste-sic';pre.textContent=JSON.stringify({checks,failures,selected,all});document.body.append(pre);});</script>"""
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
 def do_GET(self):
  if '?teste' not in self.path:return super().do_GET()
  p=Path(self.directory)/self.path.split('?')[0].lstrip('/')/'index.html';s=p.read_text(encoding='utf-8');self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(s.replace('</body>',script+'</body>').encode())
results=[];http=0
for directory,prefix in [(ROOT/'dist',''),(g['SITE'].parent,base)]:
 server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(directory)));Thread(target=server.serve_forever,daemon=True).start();host='http://127.0.0.1:'+str(server.server_port)
 try:
  with urlopen(host+prefix+route,timeout=10) as r:s=r.read().decode();assert r.status==200
  for link in set(re.findall(r'(?:href|src)="(/[^"#]*)',s)):
   with urlopen(host+link,timeout=10) as r:assert r.status==200;r.read();http+=1
  cmd=['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+str(RUN/('chrome'+str(len(results)))),'--virtual-time-budget=4000','--dump-dom',host+prefix+route+'?teste=1'];b=subprocess.run(cmd,capture_output=True,timeout=45);dom=b.stdout.decode('utf-8',errors='replace');(RUN/('browser'+str(len(results))+'.html')).write_text(dom,encoding='utf-8');m=re.search(r'<pre id="teste-sic">(.*?)</pre>',dom,re.S);assert m,'Chrome sem resultado';v=json.loads(html.unescape(m[1]));assert not v['failures'],v
  for key,length in [('selected',1),('all',4)]:
   exported=v.pop(key);data=list(csv.reader(io.StringIO(exported['text'].lstrip(chr(65279))),delimiter=';'));assert len(data)==length+1 and len(data[0])==4;assert all('DADOS SINTÉTICOS PARA TESTE DO SERIGY' in r[-1] for r in data[1:]);years=[2024] if key=='selected' else list(range(2023,2027))
   for row,y in zip(data[1:],years):i=y-2022;assert row[:3]==[str(y),f'ENTIDADE SINTÉTICA DE TESTE {i} — NÃO EXISTE',f'00.000.000/0000-0{i}']
   (RUN/(key+'-'+str(len(results))+'.csv')).write_text(exported['text'],encoding='utf-8')
  results.append(v)
 finally:server.shutdown();server.server_close()
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in protected.items())
report=dict(checks=sum(v['checks'] for v in results),falhas=[],linhas_html=4,CSV_filtrado=1,CSV_completo=4,links_http=http,bloqueios_Sancoes_isolado=4,demais_paginas_preservadas=True)
(WORK/'resultado.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(report,ensure_ascii=False))
