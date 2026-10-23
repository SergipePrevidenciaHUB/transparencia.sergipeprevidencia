"""Conferência pontual dos três módulos: fonte, ausência, consulta e CSV."""
from functools import partial
from html.parser import HTMLParser
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread
from urllib.request import urlopen
import html,json,re,subprocess,tempfile
import integrar_convenios as gen

class Cells(HTMLParser):
    def __init__(self):super().__init__();self.rows=[];self.row=None;self.cell=None
    def handle_starttag(self,t,a):
        if t=='tr':self.row=[]
        if t=='td':self.cell=[dict(a),[]]
    def handle_data(self,s):
        if self.cell:self.cell[1].append(s)
    def handle_endtag(self,t):
        if t=='td' and self.cell:self.row.append((self.cell[0],''.join(self.cell[1])));self.cell=None
        if t=='tr' and self.row:self.rows.append(self.row);self.row=None

def main():
    data=gen.load();reports=[];links=set()
    for route in ['Recebidas','Realizadas','SemTransferencia']:
        s=(gen.BASE/route/'index.html').read_text(encoding='utf-8')
        assert gen.generate(s,route,data)==s
        assert not re.search(r'sint[ée]tic|file://',s,re.I)
        assert s.count('serigyItem="dataUltimaAtualizacao"')==1 and '22/10/2026' in s
        cells=Cells();cells.feed(s)
        if route!='SemTransferencia':
            assert len(cells.rows)==1 and len(cells.rows[0])==7
            marked={a['serigyitem']:a['serigyempty'] for a,t in cells.rows[0]}
            assert set(marked)=={f for f,_,_ in gen.fields(route)} and len(set(marked.values()))==7
            assert gen.statement(route) in s and not re.search(r'<td[^>]*>\s*(?:R\$|0,00)',s)
        else:
            assert len(cells.rows)==8
            for row,source in zip(cells.rows,data['registros']):
                assert row[1][1]==source['numero_ano'] and row[2][1]=='\n'.join(source['partes'])
                assert row[3][1]==source['objeto'] and row[4][1]==source['vigencia_planilha']
                assert row[5][1]==source['obrigacoes_texto'] and row[5][0]['serigyitem']=='obrigacoes'
            assert s.count('serigyItem="anexoConvenio"')==8
        links.update(re.findall(r'(?:href|src)="(/[^"#]*)',s))
    # Conferir o bloqueio já existente, sem preparar ou publicar qualquer pacote.
    import preparar_deploy as deploy
    try:deploy.check_synthetic_content('',False)
    except ValueError:pass
    else:raise AssertionError('Outras áreas ainda exigem bloqueio oficial')
    work=gen.ROOT/'trabalho/convenios-revisados';work.mkdir(parents=True,exist_ok=True)
    run=Path(tempfile.mkdtemp(dir=work));index=(gen.ROOT/'.git/index').read_bytes()
    fixture=[]
    for r in data['registros']:
        first,last=gen.agreement_years(r)
        if first<=2024<=last:fixture.append([str(first),r['numero_ano'],'\n'.join(r['partes']),r['objeto'],r['vigencia_planilha'],r['obrigacoes_texto'],'Íntegra do instrumento (PDF) — '+(r.get('documento_url') or r['documento_url_planejada'])])
    script=r'''<script>
function fatal(e){const p=document.createElement('pre');p.id='convenios-test';p.textContent=JSON.stringify({checks:0,errors:[String(e)]});document.body.append(p);}
window.addEventListener('error',e=>fatal(e.message));window.addEventListener('unhandledrejection',e=>fatal(e.reason));
window.addEventListener('load',async()=>{
const errors=[];let checks=0;const ok=(v,m)=>{checks++;if(!v)errors.push(m);};
let parts;const NB=Blob;window.Blob=class extends NB{constructor(p,o){super(p,o);parts=p;}};URL.createObjectURL=()=> 'blob:test';HTMLAnchorElement.prototype.click=function(){};
const agreement=!!document.getElementById('filtro-acordos'),f=document.getElementById(agreement?'filtro-acordos':'filtro-convenios'),table=document.getElementById(agreement?'tabela-acordos':'tabela-convenios'),rows=Array.from(table.tBodies[0].rows);
ok(rows.length===(agreement?8:1),'initial rows');
for(const y of ['2026','2025','2024','2023']){const o=Array.from(f.elements.ano.options).find(o=>o.value===y);ok(o&&o.getAttribute('serigyValue')===y,'option '+y);}
const load=document.querySelector('[serigyLoadSection]');ok(f.elements.ano.getAttribute('serigyExecuteWaitSection')===load.getAttribute('serigyLoadSection'),'select wait/load');ok(f.querySelector('[type=submit]').getAttribute('serigyExecuteWaitSection')===load.getAttribute('serigyLoadSection'),'button wait/load');
const initial=load.innerHTML;f.elements.ano.value='2024';f.dispatchEvent(new Event('submit',{cancelable:true}));
ok(load.innerHTML!==initial,'result changes');
ok(rows.filter(r=>!r.hidden).length===(agreement?FIXTURE.length:1),'filter count');
if(!agreement){ok(document.getElementById('contagem-convenios').textContent.startsWith('0 transferências.'),'absence not counted');ok(table.caption.textContent.includes('2024'),'absence year');}
document.getElementById(agreement?'csv-acordos':'csv-convenios').click();const csv=parts.join('').replace(/^﻿/,'');
const quote=s=>'"'+s.trim().replace(/"/g,'""')+'"';
if(agreement){const header=Array.from(table.tHead.rows[0].cells).map(c=>c.textContent.trim());const expected=[header].concat(FIXTURE).map(r=>r.map(quote).join(';')).join('\r\n')+'\r\n';ok(csv===expected,'CSV exact source and obligations');}
else{ok(csv.split('\r\n').length===3,'one declaration CSV');ok(csv.includes('"2024";"01/2018 até 21/10/2026"'),'CSV year and fixed period');ok(csv.includes(document.getElementById('texto-declaracao').textContent),'CSV declaration');}
ok(!csv.includes('SINTÉTICO')&&!csv.includes('file:'),'no artificial CSV');
f.reset();await new Promise(r=>setTimeout(r,30));ok(f.elements.ano.value===''&&rows.every(r=>!r.hidden),'clear');ok(agreement||table.caption.textContent.includes('Todos os exercícios'),'clear confirms result');
const p=document.createElement('pre');p.id='convenios-test';p.textContent=JSON.stringify({checks,errors});document.body.append(p);
});</script>'''.replace('FIXTURE',json.dumps(fixture,ensure_ascii=False)).replace(r'\\r\\n',r'\r\n')
    # The injected script is kept exclusively in the local HTTP response.
    class Handler(SimpleHTTPRequestHandler):
        def log_message(self,*args):pass
        def do_GET(self):
            if '?teste=1' in self.path:
                p=gen.ROOT/'dist'/self.path.split('?')[0].lstrip('/')/'index.html'
                text=p.read_text(encoding='utf-8');self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(text.replace('</body>',script+'</body>').encode())
            else:super().do_GET()
    server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(gen.ROOT/'dist')));Thread(target=server.serve_forever,daemon=True).start()
    host=f'http://127.0.0.1:{server.server_port}'
    try:
        for url in links:
            with urlopen(host+url,timeout=10) as r:assert r.status==200
        for route in ['Recebidas','Realizadas','SemTransferencia']:
            url=host+'/Portal-da-Transparencia/Convenios/'+route+'/?teste=1'
            r=subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+str(run/route),'--virtual-time-budget=5000','--dump-dom',url],capture_output=True,timeout=60)
            dom=r.stdout.decode('utf-8',errors='replace');(run/(route+'.html')).write_text(dom,encoding='utf-8')
            m=re.search(r'<pre id="convenios-test">(.*?)</pre>',dom,re.S);assert m,route+': '+r.stderr.decode(errors='replace')[-500:]
            report=json.loads(html.unescape(m[1]));assert not report['errors'],(route,report);reports.append(dict(route=route,**report))
        assert (gen.ROOT/'.git/index').read_bytes()==index
        print(json.dumps(dict(paginas=reports,links_internos=len(links),acordos=8,resumos=8,bloqueio_oficial=True),ensure_ascii=True))
    finally:server.shutdown();server.server_close()

if __name__=='__main__':main()
