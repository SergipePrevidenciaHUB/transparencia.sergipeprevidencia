"""Concilia os sete reais e testa o único ensaio de 5.3 na cópia Pages."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from urllib.request import urlopen
import csv, hashlib, html, io, json, re, runpy, shutil, subprocess, tempfile

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / 'trabalho/acordo-sintetico'
W.mkdir(parents=True, exist_ok=True)
RUN = Path(tempfile.mkdtemp(dir=W))
route = '/Portal-da-Transparencia/Convenios/SemTransferencia/'
page = ROOT / 'dist' / route.strip('/') / 'index.html'
source = page.read_text(encoding='utf-8')
snapshot = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'dist').rglob('*') if p.is_file()}
real = re.findall(r'<tr data-year="[^"]+" data-source-row=.*?</tr>', source)
assert len(real) == 7
assert all('serigyItem="obrigacoes"' not in r and 'serigyItem="anexoConvenio"' not in r for r in real)
assert source.count('serigyItem="obrigacoes"') == source.count('serigyItem="anexoConvenio"') == 1
assert source.count('serigyItem="dataUltimaAtualizacao">22/10/2026') == 1

mode = runpy.run_path(str(ROOT/'tools/preparar_teste_acordo.py'))
fixture = RUN/'isolado'
dest = fixture/mode['ROUTE']
dest.mkdir(parents=True)
shutil.copy2(page, dest/'index.html')
shutil.copy2(page.with_name('documento-sintetico.html'), dest/'documento-sintetico.html')
cadastro = Path('Portal-da-Transparencia/SIC/eSIC/Cadastro/index.html')
(fixture/'dist'/cadastro).parent.mkdir(parents=True)
shutil.copy2(ROOT/'dist'/cadastro, fixture/'dist'/cadastro)
deploy = runpy.run_path(str(ROOT/'tools/preparar_deploy.py'))
g = deploy['prepare'].__globals__
g['DIST'] = fixture/'dist'
g['SITE'] = RUN/'oficial'
try:
    deploy['prepare']('', False)
    raise AssertionError('Ensaio não bloqueado')
except ValueError as e:
    assert 'bloqueada' in str(e)
mode['set_mode'](fixture, False)
clean = (dest/'index.html').read_text(encoding='utf-8')
assert re.findall(r'<tr data-year="[^"]+" data-source-row=.*?</tr>', clean) == real
assert 'serigyItem="dataUltimaAtualizacao">22/10/2026' in clean
assert not (dest/'documento-sintetico.html').exists()
assert (fixture/'trabalho/acordo-sintetico-removido/documento-sintetico.html').is_file()
deploy['prepare']('', False)
mode['set_mode'](fixture, True)
assert (dest/'index.html').read_bytes() == page.read_bytes()
assert (dest/'documento-sintetico.html').read_bytes() == page.with_name('documento-sintetico.html').read_bytes()

base = '/transparencia.sergipeprevidencia'
g['DIST'] = ROOT/'dist'
g['SITE'] = RUN/'pages'/base.strip('/')
deploy['prepare'](base, True)
script = r'''<script>window.addEventListener('load',async()=>{
let checks=0;const failures=[];function check(v,m){checks++;if(!v)failures.push(m);}
const f=document.getElementById('filtro-acordos'),real=[...document.querySelectorAll('#tabela-acordos tbody tr')],row=document.querySelector('#tabela-ensaio-acordo tbody tr');
check(real.length===7,'sete reais');check(!row.hidden,'ensaio inicial visível');
for(const key of ['obrigacoes','anexoConvenio']) {const e=row.querySelector('[serigyItem='+key+']');check(!!e&&e.getClientRects().length>0,'visibilidade '+key);check(e.closest('[serigySchema]').getAttribute('serigySchema').endsWith('/convenios-transferencias.html'),'schema '+key);}
check(row.textContent.includes('DADO SINTÉTICO — TESTE SERIGY'),'aviso linha');
check(document.querySelectorAll('[serigyItem=dataUltimaAtualizacao]').length===1,'data única');
for(const y of ['2026','2025','2024','2022']) {f.elements.ano.value=y;f.dispatchEvent(new Event('change',{bubbles:true}));check(row.hidden===(y!=='2026'),'filtro ensaio '+y);check(real.filter(r=>!r.hidden).length===real.filter(r=>r.dataset.year===y).length,'filtro real '+y);check(document.getElementById('csv-ensaio-acordo').disabled===(y!=='2026'),'CSV habilitado '+y);f.dispatchEvent(new Event('submit',{bubbles:true,cancelable:true}));check(row.hidden===(y!=='2026'),'pesquisa '+y);}
f.reset();await new Promise(r=>setTimeout(r,50));check(!row.hidden&&real.every(r=>!r.hidden),'limpar');
let blob;URL.createObjectURL=b=>{blob=b;return 'blob:ensaio';};URL.revokeObjectURL=()=>{};HTMLAnchorElement.prototype.click=function(){};
document.getElementById('csv-ensaio-acordo').click();const synthetic=await blob.text();
document.getElementById('csv-acordos').click();const official=await blob.text();
const link=row.querySelector('[serigyItem=anexoConvenio] a');const response=await fetch(link.href);const doc=await response.text();check(response.ok&&doc.includes('DADO SINTÉTICO — TESTE SERIGY'),'documento acessível');check(link.pathname.startsWith('/transparencia.sergipeprevidencia/'),'link base Pages');
const p=document.createElement('pre');p.id='resultado-ensaio';p.textContent=JSON.stringify({checks,failures,synthetic,official});document.body.append(p);
});</script>'''

class Handler(SimpleHTTPRequestHandler):
    def log_message(self, *args): pass
    def do_GET(self):
        if '?teste' not in self.path:
            return super().do_GET()
        h=(Path(self.directory)/self.path.split('?')[0].lstrip('/')/'index.html').read_text(encoding='utf-8')
        self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers()
        self.wfile.write(h.replace('</body>',script+'</body>').encode())

s=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(g['SITE'].parent)))
Thread(target=s.serve_forever,daemon=True).start()
try:
    url=f'http://127.0.0.1:{s.server_port}'+base+route
    initial=urlopen(url,timeout=10).read().decode('utf-8')
    assert initial.count('data-source-row=')==7 and 'serigyItem="obrigacoes"' in initial
    b=subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+str(RUN/'chrome'),'--virtual-time-budget=5000','--dump-dom',url+'?teste=1'],capture_output=True,timeout=60)
    dom=b.stdout.decode('utf-8',errors='replace');(RUN/'chrome.html').write_text(dom,encoding='utf-8')
    m=re.search(r'<pre id="resultado-ensaio">(.*?)</pre>',dom,re.S)
    assert m,'Chrome sem resultado: '+b.stderr.decode(errors='replace')[-400:]
    result=json.loads(html.unescape(m[1]));assert not result['failures'],result['failures']
    syn=list(csv.reader(io.StringIO(result.pop('synthetic').lstrip('\ufeff')),delimiter=';'))
    off=list(csv.reader(io.StringIO(result.pop('official').lstrip('\ufeff')),delimiter=';'))
    assert len(syn)==2 and syn[1][0]==mode['NOTICE'] and base in syn[1][-1]
    assert len(off)==8 and not any(mode['NOTICE'] in str(r) for r in off)
finally:
    s.shutdown();s.server_close()
assert all(hashlib.sha256(p.read_bytes()).hexdigest()==v for p,v in snapshot.items())
result.update(reais=7,sinteticos=1,csv_real=7,csv_sintetico=1,bloqueio_isolado=True,remocao_reversivel=True)
(RUN/'resultado.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
