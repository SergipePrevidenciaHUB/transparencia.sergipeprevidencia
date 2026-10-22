"""Confere ensaio 4.1/4.2/4.3, bloqueio oficial e pacote Pages; não publica nem altera dist."""
from pathlib import Path
from html.parser import HTMLParser
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
from urllib.request import urlopen
from urllib.parse import urlsplit
import csv
import html
import hashlib
import io
import json
import re
import runpy
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "trabalho/despesas-serigy-publicacao"
WORK.mkdir(parents=True, exist_ok=True)
RUN = Path(tempfile.mkdtemp(prefix="validacao-", dir=WORK))
generator = runpy.run_path(str(ROOT / "tools/preparar_teste_despesas.py"))
data = generator["load_source"]()
warning = generator["WARNING"]
baseline = json.loads(generator["BASE"].read_text(encoding="utf-8"))
document = generator["PAGE"].read_text(encoding="utf-8")
assert document == generator["render"](document, baseline, data, True)
without = generator["render"](document, baseline, data, False)
for name in generator["BLOCKS"]:
    assert generator["block"](without, name) == baseline[name]
protected = {str(p.resolve()): hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT / "dist").rglob("*") if p.is_file()}
assert generator["render"](without, baseline, data, True) == document
changed_official = without.replace("<tbody></tbody>", "<tbody><tr><td>Conteúdo fora do contrato</td></tr></tbody>", 1)
try:
    generator["render"](changed_official, baseline, data, True)
    raise AssertionError("Gerador sobrescreveria conteúdo fora do contrato")
except ValueError:
    pass


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.items, self.tables = [], [], [], {}
        self.table, self.body, self.row, self.cell = None, False, None, None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        for key in ("href", "src"):
            if a.get(key, "").startswith("/"):
                self.links.append(a[key])
        if "serigyitem" in a:
            self.items.append(a["serigyitem"])
        if tag == "table" and a.get("id") in ("despesas-totais-tabela", "despesas-classificacao-tabela", "despesas-empenhos-tabela"):
            self.table = a["id"]
            self.tables[self.table] = []
        if self.table and tag == "tbody":
            self.body = True
        if self.body and tag == "tr":
            assert a.get("data-dado-sintetico") == "true"
            self.row = []
        if self.row is not None and tag == "td":
            self.cell = ""

    def handle_data(self, text):
        if self.cell is not None:
            self.cell += text

    def handle_endtag(self, tag):
        if tag == "td" and self.cell is not None:
            self.row.append(self.cell.strip())
            self.cell = None
        if tag == "tr" and self.row is not None:
            self.tables[self.table].append(self.row)
            self.row = None
        if tag == "tbody":
            self.body = False
        if tag == "table":
            self.table = None


def check_initial(text):
    parser = Parser()
    parser.feed(text)
    assert len(parser.ids) == len(set(parser.ids))
    assert len(parser.tables["despesas-totais-tabela"]) == 8
    assert len(parser.tables["despesas-classificacao-tabela"]) == 10
    for row, source in zip(parser.tables["despesas-totais-tabela"], data["totais"]):
        assert row == [source["unidade"], str(source["exercicio"]), str(source["mes"])] + [source[k] for k in ("valorEmpenhado", "valorLiquidado", "valorPago")]
    for row, source in zip(parser.tables["despesas-classificacao-tabela"], data["classificacao"]):
        assert row == [source["unidadeDespesa"], str(source["exercicio"]), str(source["mes"])] + [source[k] for k in generator["FIELDS"][1:]]
    assert len(parser.tables["despesas-empenhos-tabela"]) == 6
    for row, source in zip(parser.tables["despesas-empenhos-tabela"], data["empenhos"]):
        assert row == [source["unidade"], str(source["exercicio"]), str(source["mes"]), source["numero_empenho"], source["credorEmpenho"], source["credor_documento"]] + [source[k] for k in generator["EMPENHO_FIELDS"][1:]]
    for item in generator["EMPENHO_FIELDS"]:
        assert parser.items.count(item) == 6
    for item in ("filtroPesquisa", "historicoExercicio", "salvarRelatorio", "dataUltimaAtualizacao"):
        assert parser.items.count(item) == 3
    assert text.count(html.escape(warning)) >= 3
    for name in generator["BLOCKS"]:
        assert ' hidden' not in re.search(r'<div id="despesas-' + name + r'-resultados"[^>]*>', text)[0]
    return parser


check_initial(document)
deploy = runpy.run_path(str(ROOT / "tools/preparar_deploy.py"))
globals_ = deploy["prepare"].__globals__
guard_target = RUN / "saida-protegida"
guard_target.mkdir()
sentinel = guard_target / "preservar.txt"
sentinel.write_text("Saída anterior não deve ser alterada", encoding="utf-8")
globals_["SITE"] = guard_target
for base, allow in (("", False), ("/Portal-da-Transparencia", False), ("/transparencia.sergipeprevidencia", False), ("/Portal-da-Transparencia", True)):
    try:
        deploy["prepare"](base, allow)
        raise AssertionError("Publicação oficial/teste sem autorização foi permitida")
    except ValueError:
        assert sentinel.read_text(encoding="utf-8") == "Saída anterior não deve ser alterada"
cname_source = RUN / "origem-com-cname"
cname_source.mkdir()
(cname_source / "index.html").write_text(document, encoding="utf-8")
(cname_source / "CNAME").write_text("sergipeprevidencia.se.gov.br", encoding="utf-8")
globals_["DIST"] = cname_source
try:
    deploy["prepare"]("/transparencia.sergipeprevidencia", True)
    raise AssertionError("CNAME oficial foi permitido no ensaio")
except ValueError:
    assert sentinel.exists()
globals_["DIST"] = ROOT / "dist"
base_path = "/transparencia.sergipeprevidencia"
pages = RUN / "pages" / base_path.strip("/")
globals_["SITE"] = pages
assert not pages.exists()
deploy["prepare"](base_path, True)
assert all(not (pages / name).exists() for name in ("dados-entrada", "controle", "tools", "modelos"))
page_route = "/Portal-da-Transparencia/Despesas/"
prepared = (pages / page_route.strip("/") / "index.html").read_text(encoding="utf-8")
parser = check_initial(prepared)
# Simular desativação somente na cópia: não alterar o modo solicitado em dist.
official_source = RUN / "origem-sem-sinteticos"
shutil.copytree(ROOT / "dist", official_source)
(official_source / page_route.strip("/") / "index.html").write_text(without, encoding="utf-8")
globals_["DIST"] = official_source
globals_["SITE"] = RUN / "pacote-oficial-sem-teste"
assert not globals_["SITE"].exists()
remaining = any(any(marker in p.read_text(encoding="utf-8-sig").lower() for marker in ("data-dado-sintetico", "data-despesas-sinteticas")) for p in official_source.rglob("*.html"))
if remaining:
    try:
        deploy["prepare"]()
    except ValueError:
        assert not globals_["SITE"].exists()
    else:
        raise AssertionError("Outros ensaios foram liberados indevidamente")
    isolated = RUN / "despesas-limpas-isoladas"
    isolated.mkdir()
    (isolated / "index.html").write_text(without, encoding="utf-8")
    globals_["DIST"] = isolated
    deploy["check_synthetic_content"]("", False)
else:
    deploy["prepare"]()
    assert (globals_["SITE"] / page_route.strip("/") / "index.html").read_text(encoding="utf-8") == without

harness = r'''<script>
window.addEventListener('load', async function(){
const spec=SPEC, warning=spec.aviso, failures=[];let checks=0;
function check(v,m){checks++;if(!v)failures.push(m);}
function query(prefix,y,m,u,e){const f=document.getElementById(prefix+'-filtro');f.elements.ano.value=y;f.elements.mes.value=m;f.elements.codigo_uo.value=u;if(f.elements.elemento)f.elements.elemento.value=e||'';f.dispatchEvent(new Event('submit',{cancelable:true,bubbles:true}));}
function baseRows(table){return Array.from(table.tBodies[0].rows).filter(r=>r.hasAttribute('data-exercicio'));}
const total=document.getElementById('despesas-totais-tabela'),table=document.getElementById('despesas-classificacao-tabela');
check(baseRows(total).length===8&&baseRows(table).length===10,'dados presentes');
check(Array.from(document.querySelectorAll('[data-despesas-sinteticas="true"]')).length===3,'escopo sintético');
check(['totais','classificacao','empenhos'].every(n=>{const p=document.getElementById('despesas-'+n+'-aviso');return p.textContent===warning&&p.getClientRects().length>0;}),'aviso visível nos três blocos');
for(const y of ['2023','2024','2025','2026']){query('despesas-totais',y,'','');check(baseRows(total).filter(r=>!r.hidden).length===spec.totais.filter(r=>String(r.exercicio)===y).length,'ano '+y);}
for(const u of Object.keys(spec.uos)){query('despesas-totais','2026','',u);check(baseRows(total).filter(r=>!r.hidden).length===spec.totais.filter(r=>r.exercicio===2026&&r.codigo_uo===u).length,'UO '+u);}
query('despesas-totais','2026','2','37201');check(baseRows(total).filter(r=>!r.hidden).length===1,'filtros totais combinados');
query('despesas-totais','2026','3','37201');check(document.getElementById('despesas-totais-csv').disabled,'CSV recorte vazio');query('despesas-totais','2026','2','37201');
function nodes(level){return Array.from(table.querySelectorAll('[data-classificacao-nivel="'+level+'"]'));}function shown(rows){return rows.filter(r=>!r.hidden);}
query('despesas-classificacao','2026','1','37201');const roots=shown(nodes('categoria'));check(roots.length===1,'categoria no recorte');const root=roots[0].querySelector('button');check(root.getAttribute('aria-expanded')==='false','categoria recolhida');root.click();const groups=shown(nodes('grupo'));check(groups.length===2,'grupos corretos');const group=groups[0].querySelector('button');group.focus();check(document.activeElement===group,'foco');group.click();check(shown(baseRows(table)).length===2,'elementos do primeiro grupo');root.click();check(shown(baseRows(table)).length===0&&shown(nodes('grupo')).length===0,'fechar hierarquia');root.click();check(shown(baseRows(table)).length===2,'reabrir hierarquia');root.click();
query('despesas-classificacao','2026','1','37201','919992 — ELEMENTO SINTÉTICO B');check(shown(nodes('categoria')).length===1,'elemento combinado');query('despesas-classificacao','2026','1','37201');
async function exportCsv(prefix){let blob,filename;URL.createObjectURL=function(value){blob=value;return 'blob:teste';};URL.revokeObjectURL=function(){};HTMLAnchorElement.prototype.click=function(){filename=this.download;};document.getElementById(prefix+'-csv').click();check(!!blob,'download '+prefix);check(filename.includes('SINTETICOS-TESTE-SERIGY'),'nome sintético '+prefix);const text=await blob.text();check(text.includes(warning),'aviso no CSV '+prefix);return {filename,text};}
const empenhos=document.getElementById('despesas-empenhos-tabela'), ef=document.getElementById('despesas-empenhos-filtro');
function empenho(y,m,u,n,c,d){ef.elements.numero_empenho.value=n||'';ef.elements.credor.value=c||'';ef.elements.documento.value=d||'';query('despesas-empenhos',y,m,u);return shown(baseRows(empenhos));}
check(baseRows(empenhos).length===6,'empenhos no HTML');
for(const y of ['2023','2024','2025','2026'])check(empenho(y,'','').length===spec.empenhos.filter(r=>String(r.exercicio)===y).length,'histórico empenhos '+y);
check(empenho('2026','','37201').length===2,'UO empenhos');
check(empenho('2026','2','37201').length===1,'período combinado empenhos');
check(empenho('','','','TESTE-EMP-2026-004').length===1,'número do empenho');
check(empenho('2026','','','','alfa').length===2,'nome credor sem diferença de caixa');
check(empenho('2026','','','','','TESTE-BETA').length===1,'documento fictício credor');
check(empenho('2026','2','37201','TESTE-EMP-2026-005','alfa','TESTE-ALFA').length===1,'todos os filtros empenhos');
check(empenho('2026','2','37401').length===0&&document.getElementById('despesas-empenhos-csv').disabled,'empenhos vazios sem exportar');
empenho('2026','2','37201');
check(['credorEmpenho','objetoEmpenho','modalidadeEmpenho','numeroProcedimento','valorEmpenhoIndividual'].every(k=>baseRows(empenhos).every(r=>r.querySelector('[serigyItem="'+k+'"]').textContent.trim())),'campos marcados empenhos');
ef.elements.credor.focus();check(document.activeElement===ef.elements.credor,'foco filtro credor');
const wait=ef.querySelector('[serigyExecuteWaitSection]').getAttribute('serigyExecuteWaitSection');check(empenhos.getAttribute('serigyLoadSection')===wait,'espera/carregamento empenhos');
check(ef.elements.ano.getAttribute('serigyItem')==='historicoExercicio'&&Array.from(ef.elements.ano.options).filter(o=>o.value).every(o=>o.getAttribute('serigyValue')===o.value),'marcação histórico empenhos');
const exports={totais:await exportCsv('despesas-totais'),classificacao:await exportCsv('despesas-classificacao'),empenhos:await exportCsv('despesas-empenhos')};
ef.reset();await new Promise(r=>setTimeout(r,40));check(shown(baseRows(empenhos)).length===6,'limpar empenhos');

for(const prefix of ['despesas-totais','despesas-classificacao'])document.getElementById(prefix+'-filtro').reset();await new Promise(r=>setTimeout(r,40));check(shown(baseRows(total)).length===8,'limpar totais');check(shown(nodes('categoria')).length===8,'limpar classificação');check(baseRows(total).length===8&&baseRows(table).length===10,'sem eliminar base');
const pre=document.createElement('pre');pre.id='teste-publicacao';pre.textContent=JSON.stringify({checks,failures,exports});document.body.append(pre);
});</script>'''.replace("SPEC", json.dumps(data, ensure_ascii=False))
fixture = prepared.replace("</body>", harness + "</body>")


class Handler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        if urlsplit(self.path).path == base_path + "/__teste-despesas.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(fixture.encode("utf-8"))
        else:
            super().do_GET()


server = ThreadingHTTPServer(("127.0.0.1", 0), partial(Handler, directory=str(pages.parent)))
Thread(target=server.serve_forever, daemon=True).start()
host = "http://127.0.0.1:" + str(server.server_port)
try:
    for url in [base_path + page_route, base_path + page_route.rstrip("/")] + sorted(set(parser.links)):
        assert url.startswith(base_path + "/")
        with urlopen(host + url, timeout=10) as response:
            assert response.status == 200
            response.read()
    profile = RUN / "chrome"
    command = ["C:/Program Files/Google/Chrome/Application/chrome.exe", "--headless", "--disable-gpu", "--no-sandbox", "--no-first-run", "--disable-extensions", "--user-data-dir=" + str(profile), "--virtual-time-budget=4000", "--dump-dom", host + base_path + "/__teste-despesas.html"]
    browser = subprocess.run(command, capture_output=True, timeout=45)
    dom = browser.stdout.decode("utf-8", errors="replace")
    (RUN / "resultado-browser.html").write_text(dom, encoding="utf-8")
    match = re.search(r'<pre id="teste-publicacao">(.*?)</pre>', dom, re.S)
    assert match, "Chrome não concluiu a validação do pacote Pages"
    report = json.loads(html.unescape(match[1]))
    assert not report["failures"], report["failures"]
finally:
    server.shutdown()
    server.server_close()
for name, count in (("totais", 1), ("classificacao", 3), ("empenhos", 1)):
    exported = report["exports"][name]
    parsed = list(csv.reader(io.StringIO(exported["text"].lstrip(chr(65279))), delimiter=";"))
    assert len(parsed) == count + 1
    assert len(parsed[0]) == {"totais": 7, "classificacao": 10, "empenhos": 11}[name]
    assert parsed[0][-1] == "Natureza dos dados" and all(row[-1] == warning for row in parsed[1:])
    if name == "totais":
        row = data["totais"][4]
        assert parsed[1][:-1] == [row["unidade"], "2026", "2", row["valorEmpenhado"], row["valorLiquidado"], row["valorPago"]]
    elif name == "classificacao":
        expected = [data["classificacao"][i] for i in (3, 8, 9)]
        assert [row[:-1] for row in parsed[1:]] == [[row["unidadeDespesa"], "2026", "1"] + [row[k] for k in generator["FIELDS"][1:]] for row in expected]
    else:
        row = data["empenhos"][4]
        assert parsed[1][:-1] == [row["unidade"], "2026", "2", row["numero_empenho"], row["credorEmpenho"], row["credor_documento"]] + [row[k] for k in generator["EMPENHO_FIELDS"][1:]]
    (RUN / exported["filename"]).write_text(exported["text"], encoding="utf-8")
report.pop("exports")
assert all(Path(name).is_file() and hashlib.sha256(Path(name).read_bytes()).hexdigest() == digest for name, digest in protected.items())
report.update(html_inicial={"totais": 8, "classificacao": 10, "empenhos": 6}, links_http=len(set(parser.links)), bloqueios=5, remocao_reversivel=True, bloqueio_isolado_apos_remocao=True, arquivos_preservados=len(protected), artefato=str(pages), invoker_executado=False)
(WORK / "resultado.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
