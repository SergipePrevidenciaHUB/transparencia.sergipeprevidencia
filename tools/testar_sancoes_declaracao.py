"""Conferência pontual da declaração, filtro, limpeza e CSV por HTTP/Chrome."""
import re,subprocess,tempfile,threading,html,json,csv,io
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from integrar_sancoes import ROOT,PAGE,render,DECLARACAO
page=PAGE.read_text(encoding='utf-8');assert render()==page
assert 'data-dado-sintetico' not in page and 'SINTÉTIC' not in page.upper()
assert len(re.findall(r'<tbody><tr>',page))==1
for item in ['nomeSancionado','idSancionado']:assert re.search(f'serigyItem="{item}" serigyEmpty="[^"]+"',page)
for y in [2026,2025,2024,2023]:assert f'value="{y}" serigyValue="{y}"' in page
assert 'serigyExecuteWaitSection="sancoesTabela"' in page and 'serigyLoadSection="sancoesTabela"' in page
pca=(ROOT/'dist/Portal-da-Transparencia/Licitacoes/PlanoAnualContratacoes/index.html').read_text(encoding='utf-8')
assert pca.count('serigyItem="contratacoesAnual"')==2 and 'Data de atualização desta relação' not in pca
assert 'datetime="2026-10-22">22/10/2026' in pca
script='''<script>window.addEventListener('load',async()=>{try{
const f=document.getElementById('filtro-sancoes'),t=document.getElementById('tabela-sancoes');
f.elements.exercicio.value='2024';f.dispatchEvent(new Event('change'));
if(!t.caption.textContent.includes('2024')||t.tBodies[0].rows.length!==1)throw Error('filtro');
let blob;URL.createObjectURL=b=>{blob=b;return 'blob:test';};URL.revokeObjectURL=()=>{};HTMLAnchorElement.prototype.click=function(){};
document.getElementById('csv-sancoes').click();const csv=await blob.text();
f.reset();await new Promise(r=>setTimeout(r,30));if(!t.caption.textContent.includes('todo o período declarado'))throw Error('limpeza');
const p=document.createElement('pre');p.id='teste-resultado';p.textContent=JSON.stringify({csv});document.body.append(p);
}catch(e){document.body.dataset.failure=e.message;}});</script>'''
class Handler(SimpleHTTPRequestHandler):
    def log_message(self,*a):pass
    def do_GET(self):
        if self.path=='/teste':
            self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(page.replace('</body>',script+'</body>').encode())
        else:super().do_GET()
work=ROOT/'trabalho/sancoes-declaracao';work.mkdir(exist_ok=True)
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(ROOT/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
try:
    run=Path(tempfile.mkdtemp(dir=work))
    r=subprocess.run([r'C:\Program Files\Google\Chrome\Application\chrome.exe','--headless','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+str(run),'--virtual-time-budget=4000','--dump-dom',f'http://127.0.0.1:{server.server_port}/teste'],capture_output=True,timeout=60)
    m=re.search(r'<pre id="teste-resultado">(.*?)</pre>',r.stdout.decode('utf-8',errors='replace'),re.S);assert m,r.stderr[-1000:]
    data=json.loads(html.unescape(m[1]));rows=list(csv.reader(io.StringIO(data['csv'].lstrip('\ufeff')),delimiter=';'))
    assert len(rows)==2 and rows[1]==[DECLARACAO,'2024','Até 21/10/2026; início do período não confirmado.','22/10/2026']
finally:server.shutdown()
print('OK: PCA e dois links preservados; Sanções sem ensaio, duas ausências justificadas, filtro 2024, limpeza e CSV declaratório; datas e períodos distintos.')
