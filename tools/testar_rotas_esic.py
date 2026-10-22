"""Confere acesso e-SIC por HTTP, base Pages e caminhos sensíveis à caixa.

Usa apenas a biblioteca padrão. Os artefatos permanecem em trabalho/, sem
publicação e sem tocar no _site eventualmente existente.
"""
from contextlib import contextmanager
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.error import HTTPError
from urllib.parse import unquote, urljoin, urlsplit
from urllib.request import urlopen
import mimetypes
import tempfile
import subprocess
import re
import html
import json

KEYBOARD_SCRIPT = '''<script>window.addEventListener('load',()=>{
const failures=[];const ok=(v,m)=>{if(!v)failures.push(m);};
const link=document.querySelector('a[serigyitem="cadastroESIC"]');link.focus();ok(document.activeElement===link,'focus link');ok(link.tabIndex>=0,'keyboard link');
const contrast=document.querySelector('[data-action="contrast"]');contrast.focus();ok(document.activeElement===contrast,'focus contrast');const before=document.body.classList.contains('high-contrast');contrast.click();ok(document.body.classList.contains('high-contrast')!==before,'contrast');contrast.click();
const inc=document.querySelector('[data-action="increase"]');const initial=getComputedStyle(document.documentElement).fontSize;inc.focus();ok(document.activeElement===inc,'focus size');inc.click();ok(getComputedStyle(document.documentElement).fontSize!==initial,'size');document.querySelector('[data-action="reset-font"]').click();
ok(!document.querySelector('[tabindex="-1"][serigyitem="cadastroESIC"]'),'native keyboard link');
const p=document.createElement('pre');p.id='keyboard-result';p.textContent=JSON.stringify(failures);document.body.append(p);
});</script>'''

def browser_check(url):
    work=ROOT/'trabalho';work.mkdir(exist_ok=True)
    run=Path(tempfile.mkdtemp(prefix='esic-teclado-',dir=work))
    result=subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+str(run/'chrome'),'--virtual-time-budget=2000','--dump-dom',url+'?teclado'],capture_output=True,timeout=60)
    dom=result.stdout.decode('utf-8',errors='replace');(run/'browser.html').write_text(dom,encoding='utf-8');m=re.search(r'<pre id="keyboard-result">(.*?)</pre>',dom,re.S);assert m,'Chrome sem resultado';assert json.loads(html.unescape(m[1]))==[],m[1]

import preparar_deploy as deploy


ROOT = Path(__file__).resolve().parents[1]
CANONICAL = "/Portal-da-Transparencia/SIC/eSIC/Cadastro"
LITERAL = "/portal-da-transparencia/sic/esic/cadastro"
ESIC = "/Portal-da-Transparencia/SIC/eSIC/"
EXTERNAL = "https://falabr.cgu.gov.br"
ACCESSIBILITY = {
    "acessibilidadeSimbolo", "acessibilidadeCaminhoPaginas",
    "acessibilidadeAltoContraste", "acessibilidadeRedimensionamentoTexto",
    "acessibilidadeMapaSite",
}


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


class CasePath:
    """Sistema de arquivos mínimo para testar o alias como em Linux e Windows."""
    def __init__(self, files, path="", sensitive=True):
        self.files, self.path, self.sensitive = files, path, sensitive

    def __truediv__(self, other):
        return CasePath(self.files, "/".join(filter(None, [self.path, str(other)])), self.sensitive)

    def __str__(self):
        return self.path

    @property
    def parent(self):
        return CasePath(self.files, self.path.rpartition("/")[0], self.sensitive)

    def key(self):
        if self.sensitive:
            return self.path
        return next((p for p in self.files if p.lower() == self.path.lower()), self.path)

    def exists(self):
        return self.key() in self.files

    is_file = exists

    def samefile(self, other):
        return self.key() == other.key()

    def mkdir(self, **kwargs):
        pass

    def read_bytes(self):
        value = self.files[self.key()]
        return value.read_bytes() if isinstance(value, Path) else value

    def write_bytes(self, content):
        self.files[self.key()] = content


def alias_checks():
    alias, canonical = next(iter(deploy.ESIC_COMPAT_ROUTES.items()))
    for sensitive in (True, False):
        files = {canonical: b"pagina real"}
        deploy.prepare_compat_routes(CasePath(files, sensitive=sensitive))
        assert len(files) == (2 if sensitive else 1)
        assert CasePath(files, alias, sensitive).read_bytes() == b"pagina real"
    for files in ({}, {canonical: b"real", alias: b"nao sobrescrever"}):
        before = files.copy()
        try:
            deploy.prepare_compat_routes(CasePath(files))
        except ValueError:
            pass
        else:
            raise AssertionError("Fonte ausente ou colisão não detectada")
        assert files == before


@contextmanager
def server(handler):
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        yield "http://127.0.0.1:" + str(httpd.server_port)
    finally:
        httpd.shutdown()
        httpd.server_close()
        thread.join()


def fetch(url):
    with urlopen(url, timeout=15) as response:
        assert response.status == 200, url
        return response.read(), response.url


def check_page(origin, prefix, route):
    raw, reached = fetch(origin + prefix + route)
    parser = Document()
    parser.feed(raw.decode("utf-8"))
    items = {a["serigyitem"] for _, a in parser.elements if "serigyitem" in a}
    assert ACCESSIBILITY <= items
    assert not {"nomeCadastro", "emailCadastro", "conteudoPedido"} & items
    assert not any(tag in {"textarea"} for tag, _ in parser.elements)
    assert not any(tag == "form" and a.get("serigyitem") == "cadastroESIC" for tag, a in parser.elements)
    links = [a for tag, a in parser.elements if tag == "a" and a.get("serigyitem") == "cadastroESIC"]
    assert len(links) == 1
    assert links[0]["href"] == links[0]["serigylink"] == EXTERNAL
    assert any(a.get("data-action") == "contrast" for _, a in parser.elements)
    assert {"increase", "decrease", "reset-font"} <= {a.get("data-action") for _, a in parser.elements}
    ids = [a["id"] for _, a in parser.elements if "id" in a]
    assert len(ids) == len(set(ids))
    assert any(a.get("href") == "#conteudo" for _, a in parser.elements)
    visited = set()
    for tag, attrs in parser.elements:
        for attr in ("href", "src"):
            value = attrs.get(attr, "")
            if not value or value.startswith(("#", "mailto:", "tel:")):
                continue
            target = urljoin(reached, value)
            if urlsplit(target).netloc != urlsplit(origin).netloc:
                continue
            if value.startswith("/"):
                assert value.startswith(prefix + "/"), value
            if target not in visited:
                fetch(target)
                visited.add(target)
    return len(visited)


def main():
    alias_checks()

    class Local(SimpleHTTPRequestHandler):
        def do_GET(self):
            if '?teclado' in self.path:
                path=Path(self.translate_path(urlsplit(self.path).path))/'index.html'
                content=path.read_text(encoding='utf-8').replace('</body>',KEYBOARD_SCRIPT+'</body>').encode()
                self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(content)
            else:super().do_GET()
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(ROOT / "dist"), **kwargs)

        def log_message(self, *args):
            pass

    with server(Local) as origin:
        browser_check(origin+ESIC)
        browser_check(origin+CANONICAL+'/')
        for route in (ESIC, CANONICAL, CANONICAL + "/"):
            check_page(origin, "", route)
        # No Windows o servidor local também resolve a caixa literal do CSV.
        # O teste seguinte é obrigatório e verifica a caixa como no Pages/Linux.
        if (ROOT / "dist" / LITERAL.lstrip("/") / "index.html").is_file():
            check_page(origin, "", LITERAL)

    work = ROOT / "trabalho"
    work.mkdir(exist_ok=True)
    output = Path(tempfile.mkdtemp(prefix="esic-rotas-", dir=work)) / "artifact"
    assert output.resolve().is_relative_to(work.resolve()) and not output.exists()
    previous = deploy.SITE
    try:
        deploy.SITE = output
        deploy.prepare("/transparencia.sergipeprevidencia/", permitir_dados_sinteticos=True)
    finally:
        deploy.SITE = previous

    # Representa o artefato em filesystem sensível à caixa, mesmo no Windows.
    # O mesmo helper que roda no Linux cria o alias, com o conteúdo já prefixado.
    files = {p.relative_to(output).as_posix(): p for p in output.rglob("*") if p.is_file()}
    deploy.prepare_compat_routes(CasePath(files))
    prefix = "/transparencia.sergipeprevidencia"

    class Pages(SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_GET(self):
            path = unquote(urlsplit(self.path).path)
            if not path.startswith(prefix + "/"):
                self.send_error(404)
                return
            key = path[len(prefix) + 1:]
            if not key.endswith("/") and key + "/index.html" in files:
                self.send_response(301)
                self.send_header("Location", path + "/")
                self.end_headers()
                return
            if key.endswith("/"):
                key += "index.html"
            if key not in files:
                self.send_error(404)
                return
            content = CasePath(files, key).read_bytes()
            if '?teclado' in self.path:
                content=content.decode('utf-8').replace('</body>',KEYBOARD_SCRIPT+'</body>').encode()
            self.send_response(200)
            self.send_header("Content-Type", mimetypes.guess_type(key)[0] or "application/octet-stream")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)

    with server(Pages) as origin:
        browser_check(origin+prefix+CANONICAL+'/')
        browser_check(origin+prefix+LITERAL+'/')
        for route in (ESIC, CANONICAL, CANONICAL + "/", LITERAL, LITERAL + "/"):
            check_page(origin, prefix, route)
        try:
            fetch(origin + prefix + "/portal-da-transparencia/sic/esic/nao-existe")
        except HTTPError as error:
            assert error.code == 404
        else:
            raise AssertionError("Rota inexistente mascarada")
    print("OK: HTTP local e Pages sensível à caixa; rota literal e canônica; links/assets; cinco marcações de acessibilidade; Fala.BR sem formulário fictício.")
    print("Artefato local:", output)


if __name__ == "__main__":
    main()
