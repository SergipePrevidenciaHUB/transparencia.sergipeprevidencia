"""Testa apenas o ensaio 8.1.6, sua remoção e o bloqueio oficial existente."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from urllib.request import urlopen
import csv, hashlib, html, io, json, re, runpy, shutil, subprocess, tempfile
from integrar_licitacoes import ROOT, PAGE, render, TEST_START

W=ROOT/'trabalho/licitacao-sintetica';W.mkdir(parents=True,exist_ok=True)
RUN=Path(tempfile.mkdtemp(dir=W));route='/Portal-da-Transparencia/Licitacoes/'
source=PAGE.read_text(encoding='utf-8')
assert render()[0]==source
def real_parts(text):
    rows=re.findall(r'<tr data-source-row=.*?</tr>',text,re.S)
    atas=re.findall(r'<li data-ata-origem=.*?</li>',text,re.S)
    assert len(rows)==96 and len(atas)==8
    assert sum(len(re.findall(r'<a\b',r)) for r in rows)==107
    assert all('serigyItem="sequencia"' not in r for r in rows)
    assert text.count('serigyItem="dataUltimaAtualizacao">22/10/2026')==1
    return rows,atas
original=real_parts(source)
assert source.count('serigyItem="sequencia"')==1
snapshot={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'dist').rglob('*') if p.is_file()}
fixture=RUN/'isolado/dist';dest=fixture/route.strip('/')/'index.html';dest.parent.mkdir(parents=True);dest.write_text(source,encoding='utf-8')
cadastro=Path('Portal-da-Transparencia/SIC/eSIC/Cadastro/index.html')
(fixture/cadastro).parent.mkdir(parents=True);shutil.copy2(ROOT/'dist'/cadastro,fixture/cadastro)
deploy=runpy.run_path(str(ROOT/'tools/preparar_deploy.py'));g=deploy['prepare'].__globals__;g['DIST']=fixture;g['SITE']=RUN/'oficial'
try:
    deploy['prepare']('',False)
    raise AssertionError('Ensaio não bloqueado')
except ValueError as e:assert 'bloqueada' in str(e)
clean=render(synthetic=False)[0];assert real_parts(clean)==original and TEST_START not in clean
dest.write_text(clean,encoding='utf-8');deploy['prepare']('',False)
active=render(synthetic=True)[0];assert active==source
dest.write_text(active,encoding='utf-8')
try:
    deploy['prepare']('',False)
    raise AssertionError('Reativação não bloqueada')
except ValueError as e:assert 'bloqueada' in str(e)

base='/transparencia.sergipeprevidencia';g['DIST']=ROOT/'dist';g['SITE']=RUN/'pages'/base.strip('/');deploy['prepare'](base,True)
script=r'''<script>window.addEventListener('load',async()=>{
let checks=0;const failures=[];const ok=(v,m)=>{checks++;if(!v)failures.push(m);};
const f=document.getElementById('filtro-licitacoes'),r=document.querySelector('#tabela-ensaio-licitacao tbody tr'),seq=r.querySelector('[serigyItem=sequencia]'),real=[...document.querySelectorAll('#tabela-licitacoes tbody tr')],button=document.getElementById('exportar-ensaio-licitacao');
ok(real.length===96,'96 reais');ok(document.querySelectorAll('#tabela-licitacoes a').length===107,'107 links reais');ok(document.querySelectorAll('#atas-adesao-srp a').length===8,'oito atas');
ok(seq.getClientRects().length>0&&!r.hidden,'sequência visível inicialmente');ok(seq.textContent==='900001','sequência numérica fictícia');ok(seq.closest('[serigySchema]').getAttribute('serigySchema').endsWith('/licitacoes.html'),'schema');ok(r.textContent.includes('DADO SINTÉTICO — TESTE SERIGY'),'aviso na linha');
function apply(){f.dispatchEvent(new Event('change',{bubbles:true}));}
for(const key of ['ano','modalidade','situacao','mes']){for(const opt of f.elements[key].options){f.elements[key].value=opt.value;apply();const expected=!opt.value||r.dataset[key==='ano'?'year':key]===opt.value;ok(!r.hidden===expected,key+opt.value);ok(button.disabled===!expected,'CSV '+key+opt.value);}f.elements[key].value='';}
f.elements.ano.value='2026';f.elements.modalidade.value=r.dataset.modalidade;f.elements.situacao.value=r.dataset.situacao;f.elements.texto.value='ENSAIO-FICTICIO-001';f.dispatchEvent(new Event('input',{bubbles:true}));ok(!r.hidden&&real.every(x=>x.hidden),'filtros combinados distinguem ensaio');
f.dispatchEvent(new Event('submit',{bubbles:true,cancelable:true}));ok(!r.hidden,'pesquisa');
let blob;URL.createObjectURL=b=>{blob=b;return 'blob:teste';};URL.revokeObjectURL=()=>{};HTMLAnchorElement.prototype.click=function(){};button.click();const synthetic=await blob.text();
f.elements.texto.value='nao-existe-ensaio';apply();ok(r.hidden&&button.disabled,'sem resultado');f.reset();await new Promise(r=>setTimeout(r,50));ok(!r.hidden&&real.every(x=>!x.hidden),'limpar');document.getElementById('exportar-licitacoes').click();const official=await blob.text();
const p=document.createElement('pre');p.id='resultado-ensaio';p.textContent=JSON.stringify({checks,failures,synthetic,official});document.body.append(p);
});</script>'''
class Handler(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
    def do_GET(self):
        if '?teste' not in self.path:return super().do_GET()
        s=(Path(self.directory)/self.path.split('?')[0].lstrip('/')/'index.html').read_text(encoding='utf-8')
        self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(s.replace('</body>',script+'</body>').encode())
s=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(g['SITE'].parent)));Thread(target=s.serve_forever,daemon=True).start()
try:
    url=f'http://127.0.0.1:{s.server_port}'+base+route
    initial=urlopen(url,timeout=10).read().decode('utf-8');assert real_parts(initial)==original and 'serigyItem="sequencia">900001' in initial
    b=subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+str(RUN/'chrome'),'--virtual-time-budget=5000','--dump-dom',url+'?teste=1'],capture_output=True,timeout=60)
    dom=b.stdout.decode('utf-8',errors='replace');(RUN/'chrome.html').write_text(dom,encoding='utf-8');m=re.search(r'<pre id="resultado-ensaio">(.*?)</pre>',dom,re.S);assert m,'Chrome sem resultado'
    result=json.loads(html.unescape(m[1]));assert not result['failures'],result['failures']
    syn=list(csv.reader(io.StringIO(result.pop('synthetic').lstrip('\ufeff')),delimiter=';'));off=list(csv.reader(io.StringIO(result.pop('official').lstrip('\ufeff')),delimiter=';'))
    assert len(syn)==2 and syn[1][0]=='DADO SINTÉTICO — TESTE SERIGY' and syn[1][2]=='900001'
    assert len(off)==97 and not any('DADO SINTÉTICO' in str(r) for r in off)
finally:s.shutdown();s.server_close()
assert all(hashlib.sha256(p.read_bytes()).hexdigest()==h for p,h in snapshot.items())
result.update(procedimentos_reais=96,links_originais=107,atas=8,csv_sintetico=1,csv_real=96,bloqueio_isolado=True,remocao_reversivel=True)
(RUN/'resultado.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False))
