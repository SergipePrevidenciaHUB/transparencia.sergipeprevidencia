r"""Gera e confere a prévia local; use --servir para abrir em localhost:8765.

Uso: .\.venv\Scripts\python.exe -B tools\preview_portal.py --servir
Não modifica fontes, não inclui variantes e não remove arquivos existentes.
"""
import argparse
import functools
import json
import re
import shutil
import threading
from collections import defaultdict
from html import escape
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import URLError
from urllib.parse import quote, unquote, urljoin, urlsplit
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'trabalho/preview-portal'


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids = [], set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append(attrs[key])


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass


def route(path):
    name = path.as_posix()
    return '/' + (name[:-10] if name.endswith('index.html') else name)


def build():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    sources, models, collisions = {}, set(), []
    for source in sorted((ROOT / 'dist').rglob('*')):
        if source.is_file():
            relative = source.relative_to(ROOT / 'dist')
            sources[relative] = source
    for source in sorted((ROOT / 'modelos/Portal-da-Transparencia').rglob('index.html')):
        relative = source.relative_to(ROOT / 'modelos')
        if relative in sources:
            collisions.append({'rota': route(relative), 'preservado': str(sources[relative]),
                               'modelo_nao_copiado': str(source)})
            continue
        sources[relative] = source
        models.add(relative)
    pages = [p for p in sources if p.suffix.lower() == '.html']
    catalog = []
    for relative in pages:
        text = sources[relative].read_text(encoding='utf-8-sig')
        title = re.search(r'<h1\b[^>]*>(.*?)</h1>', text, re.S | re.I)
        title = re.sub('<[^>]+>', '', title[1]).strip() if title else relative.as_posix()
        catalog.append({'arquivo': relative.as_posix(), 'rota': route(relative),
                        'titulo': title, 'modelo': relative in models})
    groups = defaultdict(list)
    for entry in catalog:
        groups['Modelos ainda sem dados oficiais' if entry['modelo'] else 'Páginas de dist'].append(entry)
    lists = ''.join('<h3>' + escape(label) + '</h3><ul>' + ''.join(
        '<li><a href="' + quote(e['rota'], safe='/') + '">' + escape(e['titulo']) + '</a> <small>(' +
        escape(e['rota']) + ')</small></li>' for e in entries) + '</ul>' for label, entries in groups.items())
    navigation = ('<aside class="container" aria-label="Navegação da prévia local" '
                  'style="margin-block:1rem;padding:1rem;border:1px solid currentColor;border-radius:6px">'
                  '<details><summary>Prévia local — todas as seções (' + str(len(pages)) + ' páginas)</summary>'
                  '<p>Conteúdo de dist e modelos não publicados. As variantes não estão incluídas.</p>' +
                  lists + '</details></aside>')
    for relative, source in sources.items():
        target = OUTPUT / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if relative not in pages:
            shutil.copy2(source, target)
            continue
        text = source.read_text(encoding='utf-8-sig')
        notice = ('<p class="container" role="note" style="padding:.75rem;border-inline-start:3px solid currentColor">'
                  '<strong>Modelo não publicado.</strong> Estrutura ainda sem dados oficiais completos; '
                  'não representa página concluída.</p>') if relative in models else ''
        text, count = re.subn(r'(<body\b[^>]*>)', lambda m: m[1] + navigation + notice,
                             text, count=1, flags=re.I)
        if count != 1:
            raise ValueError('Página sem body: ' + str(relative))
        target.write_text(text, encoding='utf-8')
    extras = [p.relative_to(OUTPUT).as_posix() for p in OUTPUT.rglob('*')
              if p.is_file() and p.relative_to(OUTPUT) not in sources
              and p.name != 'conferencia-preview.json']
    return catalog, collisions, extras


def check(server, catalog):
    """GET de todas as páginas e destinos locais; inclui recursos url() do CSS."""
    base = 'http://127.0.0.1:' + str(server.server_port)
    cache, parsed, issues = {}, {}, []

    def fetch(path):
        if path not in cache:
            try:
                with urlopen(base + quote(unquote(path), safe='/%:@'), timeout=15) as response:
                    cache[path] = (response.status, response.read(), response.headers.get_content_type())
            except (URLError, OSError) as error:
                cache[path] = (0, b'', str(error))
        return cache[path]

    def inspect_link(source, link):
        url = urlsplit(urljoin(base + source, link))
        if url.netloc != urlsplit(base).netloc or url.scheme not in ('http', 'https'):
            return
        path = url.path or '/'
        status, body, mime = fetch(path)
        if status != 200:
            issues.append({'origem': source, 'destino': link, 'problema': 'HTTP local indisponível'})
        elif url.fragment and mime == 'text/html':
            if path not in parsed:
                parsed[path] = Page(body.decode('utf-8-sig'))
            if unquote(url.fragment) not in parsed[path].ids:
                issues.append({'origem': source, 'destino': link, 'problema': 'Fragmento sem ID'})

    for entry in catalog:
        path = entry['rota']
        status, body, mime = fetch(path)
        if status != 200 or mime != 'text/html':
            issues.append({'origem': path, 'problema': 'Página não abriu como HTML'})
            continue
        parsed[path] = Page(body.decode('utf-8-sig'))
        for link in parsed[path].links:
            inspect_link(path, link)
    for path, (_, body, mime) in list(cache.items()):
        if mime == 'text/css':
            for link in re.findall(r'url\(\s*[\'"]?([^\)\'"\s]+)', body.decode('utf-8-sig')):
                inspect_link(path, link)
    return issues, len(cache), sum(v[0] == 200 and v[2] == 'text/html' for v in cache.values())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--servir', action='store_true', help='Mantém servidor apenas em 127.0.0.1')
    parser.add_argument('--porta', type=int, default=8765)
    args = parser.parse_args()
    catalog, collisions, extras = build()
    handler = functools.partial(QuietHandler, directory=str(OUTPUT))
    with ThreadingHTTPServer(('127.0.0.1', args.porta if args.servir else 0), handler) as server:
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()
        try:
            issues, requests, opened = check(server, catalog)
            report = dict(paginas=len(catalog), modelos=sum(e['modelo'] for e in catalog),
                          paginas_http_ok=opened, destinos_http_verificados=requests,
                          colisoes=collisions, links_com_problema=issues,
                          arquivos_preexistentes_fora_desta_geracao=extras, catalogo=catalog,
                          limite='Conferência HTTP de HTML, links e recursos; não executa JavaScript nem testa sistemas externos.')
            (OUTPUT / 'conferencia-preview.json').write_text(
                json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            print(f'Prévia: {len(catalog)} páginas, {report["modelos"]} modelos; '
                  f'{opened} páginas HTTP OK; {requests} destinos locais conferidos.', flush=True)
            print(f'Colisões: {len(collisions)}; links com problema: {len(issues)}; '
                  f'arquivos extras preservados: {len(extras)}.', flush=True)
            print('Relatório: trabalho/preview-portal/conferencia-preview.json', flush=True)
            if args.servir:
                print(f'URL local: http://127.0.0.1:{server.server_port}/Portal-da-Transparencia/', flush=True)
                print('Ctrl+C encerra o servidor. Somente acesso local.', flush=True)
                worker.join()
        except KeyboardInterrupt:
            pass
        finally:
            server.shutdown()
            worker.join()


if __name__ == '__main__':
    main()
