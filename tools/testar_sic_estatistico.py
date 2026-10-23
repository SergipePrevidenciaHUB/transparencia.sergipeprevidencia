"""Conferência pontual do relatório LAI preparado, filtros e CSV; sem Invoker."""
from pathlib import Path
from html.parser import HTMLParser
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
import threading,subprocess,tempfile,json,re,csv,io,html
from integrar_sic_estatistico import ROOT,PAGE,CSV,load,render,HEADERS,values
data,records=load();page=PAGE.read_text(encoding='utf-8');assert page==render(data,records)
class Table(HTMLParser):
    def __init__(self):super().__init__();self.rows=[];self.row=None;self.cell=None
    def handle_starttag(self,t,attrs):
        a=dict(attrs)
        if t=='tr' and 'data-year' in a:self.row=[]
        if t=='td' and self.row is not None:self.cell=[a,'']
    def handle_data(self,s):
        if self.cell is not None:self.cell[1]+=s
    def handle_endtag(self,t):
        if t=='td' and self.cell is not None:self.row.append(self.cell);self.cell=None
        if t=='tr' and self.row is not None:self.rows.append(self.row);self.row=None
p=Table();p.feed(page);assert len(p.rows)==4
assert [[c[1] for c in row] for row in p.rows]==[values(r) for r in records]
for row in p.rows:
    assert row[4][0]['serigyitem']=='pedidosIndeferidos' and row[4][1]=='0' and 'serigyempty' not in row[4][0]
    assert [row[i][0]['serigyitem'] for i in [2,3,4,5]]==['pedidosRecebidos','pedidosAtendidos','pedidosIndeferidos','infoGenericas']
assert [r['pedidos_recebidos'] for r in records]==[4,9,3,2] and [r['pedidos_atendidos'] for r in records]==[4,9,3,2]
assert 'Janeiro a Outubro (parcial)' in page and 'datetime="2026-10-22">22/10/2026' in page
for marker in ['filtroPesquisa','historicoExercicio','salvarRelatorio','dataUltimaAtualizacao']:assert 'serigyItem="'+marker+'"' in page
assert 'serigyExecuteWaitSection="sicTabela"' in page and 'serigyLoadSection="sicTabela"' in page
with CSV.open(encoding='utf-8-sig',newline='') as f:assert list(csv.reader(f,delimiter=';'))==[HEADERS]+[values(r) for r in records]
js=(ROOT/'dist/assets/js/sic-relatorio.js').read_text(encoding='utf-8')
assert not re.search('sint[eé]tic|ensaio',page+js,re.I)
assert 'aria-describedby=' not in re.search(r'<main.*?</main>',page,re.S)[0]
script='''<script>window.addEventListener('load',async()=>{try{const f=document.getElementById('filtro-relatorio-sic'),t=document.getElementById('tabela-relatorio-sic'),rows=Array.from(t.tBodies[0].rows);f.elements.exercicio.value='2024';f.dispatchEvent(new Event('submit',{cancelable:true}));if(rows.filter(r=>!r.hidden).length!==1||rows.find(r=>!r.hidden).cells[4].textContent!=='0')throw Error('filtro/zero');let blob;URL.createObjectURL=b=>{blob=b;return 'blob:test';};URL.revokeObjectURL=()=>{};HTMLAnchorElement.prototype.click=function(){};document.getElementById('csv-relatorio-sic').dispatchEvent(new MouseEvent('click',{bubbles:true,cancelable:true}));const selected=await blob.text();f.reset();await new Promise(r=>setTimeout(r,30));if(rows.some(r=>r.hidden))throw Error('limpeza');document.getElementById('csv-relatorio-sic').dispatchEvent(new MouseEvent('click',{bubbles:true,cancelable:true}));const all=await blob.text();const p=document.createElement('pre');p.id='teste-resultado';p.textContent=JSON.stringify({selected,all});document.body.append(p);}catch(e){document.body.dataset.failure=e.message;}});</script>'''
class Handler(SimpleHTTPRequestHandler):
    def log_message(self,*a):pass
    def do_GET(self):
        if self.path=='/teste':
            self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(page.replace('</body>',script+'</body>').encode())
        else:super().do_GET()
work=ROOT/'trabalho/sic-estatistico-real';work.mkdir(exist_ok=True)
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(ROOT/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
try:
    profile=tempfile.mkdtemp(dir=work)
    r=subprocess.run([r'C:\Program Files\Google\Chrome\Application\chrome.exe','--headless','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+profile,'--virtual-time-budget=4000','--dump-dom',f'http://127.0.0.1:{server.server_port}/teste'],capture_output=True,timeout=60)
    dom=r.stdout.decode('utf-8',errors='replace');m=re.search(r'<pre id="teste-resultado">(.*?)</pre>',dom,re.S);assert m,r.stderr[-1500:]
    result=json.loads(html.unescape(m[1]))
    for name,expected in [('selected',[values(r) for r in records if r['ano']==2024]),('all',[values(r) for r in records])]:
        exported=list(csv.reader(io.StringIO(result[name].lstrip('\ufeff')),delimiter=';'));assert exported==[HEADERS]+expected
finally:server.shutdown()
print('OK: quatro registros reais, totais/perfis exatos, quatro zeros sem serigyEmpty, 2026 parcial, oito marcações; Chrome filtro 2024, limpeza, CSV completo/filtrado com período, perfil e zeros.')
