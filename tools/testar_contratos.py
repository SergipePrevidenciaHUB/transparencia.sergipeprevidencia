"""Conciliação da consulta de contratos e teste funcional em Chrome local."""
from pathlib import Path
import csv
import html
import io
import json
import re
import subprocess
import tempfile
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from urllib.request import urlopen
from integrar_contratos import render, PAGE, SOURCE, ROOT

page = PAGE.read_text(encoding='utf-8')
assert page == render('data-dado-sintetico="contratos"' in page)
real_page = page.split('<section data-dado-sintetico="contratos"')[0]
assert real_page.count('serigyItem="dataUltimaAtualizacao">22/10/2026') == 1
data = json.loads(SOURCE.read_text(encoding='utf-8'))
assert len(data['contratos']) == 156
assert page.count('data-source-row=') == 156
assert real_page.count('serigyItem="linkContrato"') == 122
assert real_page.count('serigyItem="termoAditivo"') == 8
assert not any('serigyItem="' + x + '"' in real_page for x in ['valorContrato', 'sequencia'])
for c in data['contratos']:
    match = re.search(r'<tr data-source-row="' + str(c['linha_origem']) + r'".*?</tr>', page, re.S)
    assert match
    row = match[0]
    for field in ['contratado_literal', 'objeto_literal']:
        assert html.escape(c[field], quote=True).replace('\r', '&#13;').replace('\n', '&#10;') in row
    if c['url_integra']:
        assert html.escape(c['url_integra'], quote=True) in row
    for aid in c['aditivos_associados']:
        a = next(a for a in data['aditivos'] if a['id_origem'] == aid)
        assert a['contrato_associado'] == c['id_origem']
        assert html.escape(a['url_integra'], quote=True) in row

script = '''<script>window.addEventListener('load', async () => {
const failures=[];let checks=0;function check(v,m){checks++;if(!v)failures.push(m);}
const f=document.getElementById('filtro-contratos'),t=document.getElementById('tabela-contratos'),rows=Array.from(t.tBodies[0].rows),b=document.getElementById('exportar-contratos');
const apply=()=>f.dispatchEvent(new Event('change',{bubbles:true}));
const visible=()=>rows.filter(r=>!r.hidden);
check(rows.length===156,'initial rows');
for(const o of f.elements.ano.options){f.elements.ano.value=o.value;apply();check(visible().length===rows.filter(r=>!o.value||r.dataset.year===o.value).length,'year '+o.value);}
f.elements.ano.value='2022';f.elements.texto.value='agenda';apply();check(visible().length===1,'combined agenda');check(visible()[0].querySelectorAll('[serigyItem="termoAditivo"]').length===4,'agenda additions');
let blob;URL.createObjectURL=x=>{blob=x;return 'blob:test';};URL.revokeObjectURL=()=>{};HTMLAnchorElement.prototype.click=function(){};
b.click();const selected=await blob.text();
f.elements.texto.value='no-match-impossible';apply();check(visible().length===0&&b.disabled,'no matches');
f.reset();await new Promise(r=>setTimeout(r,20));check(visible().length===156,'reset');b.click();const all=await blob.text();
const result={checks,failures,selected,all};const p=document.createElement('pre');p.id='test-result';p.textContent=JSON.stringify(result);document.body.append(p);
});</script>'''
class Handler(SimpleHTTPRequestHandler):
    def log_message(self, *args): pass
    def do_GET(self):
        if self.path.endswith('?test=1'):
            self.send_response(200); self.send_header('Content-Type','text/html; charset=utf-8'); self.end_headers()
            self.wfile.write(page.replace('</body>',script+'</body>').encode('utf-8'))
        else: super().do_GET()

work = ROOT/'trabalho/contratos'
work.mkdir(parents=True,exist_ok=True)
run = Path(tempfile.mkdtemp(dir=work))
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(ROOT/'dist')))
Thread(target=server.serve_forever,daemon=True).start()
url='http://127.0.0.1:'+str(server.server_port)+'/Portal-da-Transparencia/Contratos/'
try:
    assert urlopen(url,timeout=10).status==200
    result=subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+str(run/'chrome'),'--virtual-time-budget=5000','--dump-dom',url+'?test=1'],capture_output=True,timeout=60)
    dom=result.stdout.decode('utf-8',errors='replace')
    (run/'browser.html').write_text(dom,encoding='utf-8')
    m=re.search(r'<pre id="test-result">(.*?)</pre>',dom,re.S);assert m,'Chrome sem resultado'
    report=json.loads(html.unescape(m[1]));assert not report['failures'],report['failures']
    for name,count in [('selected',1),('all',156)]:
        text=report.pop(name);parsed=list(csv.reader(io.StringIO(text.lstrip('\ufeff')),delimiter=';'))
        assert len(parsed)==count+1 and all(len(r)==7 for r in parsed)
        assert sum('http' in r[5] for r in parsed[1:])==(1 if name=='selected' else 122)
        assert sum(r[6].count('https://') for r in parsed[1:])==(4 if name=='selected' else 8)
        (run/(name+'.csv')).write_text(text,encoding='utf-8')
finally:
    server.shutdown();server.server_close()
print(json.dumps(dict(report,contratos=156,integra=122,aditivos=8,CSV='integral e filtrado conferidos'),ensure_ascii=True))
