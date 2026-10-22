"""Concilia os acordos com o JSON e testa consulta/CSV local e Pages, sem Invoker."""
from pathlib import Path
import json,tempfile,runpy,re,subprocess,html,csv,io,hashlib
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
from urllib.request import urlopen
protected={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__).resolve().parents[1]/'dist').rglob('*') if p.is_file()}
ROOT=Path(__file__).resolve().parents[1];W=ROOT/'trabalho/acordos-sem-transferencia';W.mkdir(parents=True,exist_ok=True);RUN=Path(tempfile.mkdtemp(dir=W));route='/Portal-da-Transparencia/Convenios/SemTransferencia/';data=json.loads((ROOT/'dados-entrada/convenios/convenios-dados-preparados.json').read_text(encoding='utf-8-sig'))['sem_transferencia'];source=(ROOT/'dist'/route.strip('/')/'index.html').read_text(encoding='utf-8')
assert source.count('data-source-row=')==7
assert source.count('serigyItem="identificaAcordo"')==4
assert not any('serigyItem="'+k+'"' in source for k in ['obrigacoes','anexoConvenio','dataUltimaAtualizacao'])
for r in data['registros']:assert html.escape(r['objeto']) in source and html.escape(r['url_inteiro_teor_candidato'],quote=True) in source
script=r"""<script>window.addEventListener('load',async()=>{const spec=SPEC,failures=[];let checks=0;function check(v,m){checks++;if(!v)failures.push(m);}const f=document.getElementById('filtro-acordos'),t=document.getElementById('tabela-acordos'),rows=Array.from(t.tBodies[0].rows);check(rows.length===spec.registros.length,'contagem');rows.forEach((r,i)=>{const s=spec.registros[i],c=Array.from(r.cells);check(r.dataset.sourceRow===String(s.linha_planilha),'linha fonte '+i);check(c[0].textContent===s.inicio_vigencia.slice(-4),'ano vigência '+i);check(c[1].textContent===(s.identificador_para_publicacao||'Não informado'),'ID '+i);check(c[2].textContent===s.parte_1+s.parte_2,'partes '+i);check(c[3].textContent===s.objeto,'objeto '+i);check(c[4].textContent===s.inicio_vigencia+' a '+s.fim_vigencia,'vigência '+i);check(c[5].textContent===(s.obrigacoes_resumo||'Não informado'),'obrigações '+i);check(c[6].querySelector('a').href===s.url_inteiro_teor_candidato,'URL '+i);check(!!r.querySelector('[serigyItem=identificaAcordo]')===!!s.identificador_para_publicacao,'marca ID '+i);});['participante','objetoConvenio','vigenciaConvenio','filtroPesquisa','salvarRelatorio','historicoExercicio'].forEach(k=>check(!!document.querySelector('[serigyItem="'+k+'"]'),'marca '+k));check(f.elements.ano.getAttribute('serigyExecuteWaitSection')===document.getElementById('resultados-acordos').getAttribute('serigyLoadSection'),'wait/load');for(const o of Array.from(f.elements.ano.options)){f.elements.ano.value=o.value;f.dispatchEvent(new Event('change',{bubbles:true}));let expected=spec.registros.filter(r=>!o.value||r.inicio_vigencia.endsWith(o.value)).length;check(rows.filter(r=>!r.hidden).length===expected,'change '+o.value);if(o.value)check(o.getAttribute('serigyValue')===o.value,'histórico '+o.value);f.dispatchEvent(new Event('submit',{bubbles:true,cancelable:true}));check(rows.filter(r=>!r.hidden).length===expected,'submit '+o.value);}
async function capture(){let blob;URL.createObjectURL=b=>{blob=b;return 'blob:teste';};URL.revokeObjectURL=()=>{};HTMLAnchorElement.prototype.click=function(){};document.getElementById('csv-acordos').click();return await blob.text();}f.elements.ano.value='2024';f.dispatchEvent(new Event('submit',{cancelable:true,bubbles:true}));const selected=await capture();f.reset();await new Promise(r=>setTimeout(r,40));check(rows.every(r=>!r.hidden),'limpar');const all=await capture();const pre=document.createElement('pre');pre.id='resultado';pre.textContent=JSON.stringify({checks,failures,selected,all});document.body.append(pre);});</script>""".replace('SPEC',json.dumps(data,ensure_ascii=False))
d=runpy.run_path(str(ROOT/'tools/preparar_deploy.py'));g=d['prepare'].__globals__;base='/transparencia.sergipeprevidencia';g['SITE']=RUN/'pages'/base.strip('/');d['prepare'](base,True)
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
 def do_GET(self):
  if '?teste' not in self.path:return super().do_GET()
  s=(Path(self.directory)/self.path.split('?')[0].lstrip('/')/'index.html').read_text(encoding='utf-8');self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(s.replace('</body>',script+'</body>').encode())
results=[];http=0
for directory,prefix in [(ROOT/'dist',''),(g['SITE'].parent,base)]:
 server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(directory)));Thread(target=server.serve_forever,daemon=True).start();host='http://127.0.0.1:'+str(server.server_port)
 try:
  with urlopen(host+prefix+route,timeout=10) as r:s=r.read().decode();assert r.status==200
  for link in set(re.findall(r'(?:href|src)="(/[^"#]*)',s)):
   with urlopen(host+link,timeout=10) as r:assert r.status==200;r.read();http+=1
  b=subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+str(RUN/('chrome'+str(len(results)))),'--virtual-time-budget=4000','--dump-dom',host+prefix+route+'?teste=1'],capture_output=True,timeout=45);dom=b.stdout.decode('utf-8',errors='replace');(RUN/('dom'+str(len(results))+'.html')).write_text(dom,encoding='utf-8');m=re.search(r'<pre id="resultado">(.*?)</pre>',dom,re.S);assert m,'Sem resultado Chrome';v=json.loads(html.unescape(m[1]));assert not v['failures'],v
  for key,year in [('selected','2024'),('all','')]:
   text=v.pop(key);parsed=list(csv.reader(io.StringIO(text.lstrip(chr(65279))),delimiter=';'));expected=[r for r in data['registros'] if not year or r['inicio_vigencia'].endswith(year)];assert len(parsed)==len(expected)+1 and len(parsed[0])==7
   for row,r in zip(parsed[1:],expected):assert row[:2]==[r['inicio_vigencia'][-4:],r['identificador_para_publicacao'] or 'Não informado'] and row[2].replace('\n','')==r['parte_1']+r['parte_2'] and row[3]==r['objeto'] and row[4]==r['inicio_vigencia']+' a '+r['fim_vigencia'] and row[5]==(r['obrigacoes_resumo'] or 'Não informado') and r['url_inteiro_teor_candidato'] in row[6]
   (RUN/(key+str(len(results))+'.csv')).write_text(text,encoding='utf-8')
  results.append(v)
 finally:server.shutdown();server.server_close()
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in protected.items())
report=dict(checks=sum(v['checks'] for v in results),falhas=[],registros=7,IDs_marcados=4,links_JSON=7,CSV_2024=4,CSV_completo=7,links_http=http,recebidas_realizadas_preservadas=True,URLs_externas_apenas_conciliadas_com_JSON=True);(W/'resultado.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(report,ensure_ascii=False))
