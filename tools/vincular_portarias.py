"""Associa automaticamente portarias de 2023–2025 a hrefs do sítio oficial.

Sem OCR, serviços externos ou similaridade semântica. O cache fica em
dados-entrada/outros/cache-portarias, fora do conteúdo publicável e do Git.
O modo --offline repete as conferências sem novas requisições. Os controles
de 2026 não são lidos nem escritos por esta coleta.
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime
import hashlib
from html.parser import HTMLParser
import io
import json
import logging
from pathlib import Path
import re
import time
import unicodedata
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urljoin, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

from pypdf import PdfReader
from importar_portarias import ROOT, read_records

SOURCE_URL = "https://sergipeprevidencia.se.gov.br/transparencia/legislacao/portaria/"
YEARS = (2023, 2024, 2025)
HOSTS = {"sergipeprevidencia.se.gov.br", "www.sergipeprevidencia.se.gov.br"}
MONTHS = {name: i for i, name in enumerate(
    "janeiro fevereiro marco abril maio junho julho agosto setembro outubro novembro dezembro".split(), 1)}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def plain(text):
    return "".join(c for c in unicodedata.normalize("NFD", text.lower())
                   if not unicodedata.combining(c))


def normalized(text):
    # Não remove palavras nem números e não usa aproximação por similaridade.
    return " ".join(re.findall(r"\w+", plain(text).replace("º", "").replace("°", ""), re.UNICODE))


def date_value(text):
    matches = re.findall(r"\b(\d{1,2})\s+de\s+(\w+)\s+de\s+(\d{4})\b", plain(text))
    if len(matches) != 1 or matches[0][1] not in MONTHS:
        return None
    day, month, year = matches[0]
    try:
        return datetime(int(year), MONTHS[month], int(day)).date().isoformat()
    except ValueError:
        return None


def official_url(url, pdf=False):
    parsed = urlsplit(url)
    return (parsed.scheme == "https" and parsed.hostname in HOSTS
            and not parsed.username and not parsed.password
            and (not pdf or parsed.path.lower().endswith(".pdf")))


class OfficialParser(HTMLParser):
    """Conserva a relação entre título, href, data e parágrafos seguintes."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks, self.active, self.parts, self.links = [], None, [], []
        self.anchors, self.anchor_parts, self.anchor_href = [], None, None

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.anchor_parts, self.anchor_href = [], dict(attrs).get("href")
        if tag in {"p", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.active, self.parts, self.links = tag, [], []
        if self.active:
            if tag == "a" and dict(attrs).get("href"):
                self.links.append(dict(attrs)["href"])
            elif tag == "br":
                self.parts.append(" ")

    def handle_data(self, data):
        if self.anchor_parts is not None:
            self.anchor_parts.append(data)
        if self.active:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self.anchor_parts is not None:
            self.anchors.append((" ".join("".join(self.anchor_parts).split()), self.anchor_href))
            self.anchor_parts = None
        if tag == self.active:
            self.blocks.append(dict(tag=tag, text=" ".join("".join(self.parts).split()),
                                    links=list(self.links)))
            self.active = None

    def records(self):
        records, section_year = [], None
        for i, block in enumerate(self.blocks):
            if re.fullmatch(r"20\d{2}", block["text"]):
                section_year = int(block["text"])
            match = re.fullmatch(r"Portaria\s+(?:N[º°o.]\s*)?(\d+)(?:\s*/\s*(20\d{2}))?",
                                 block["text"], re.I)
            if not match:
                continue
            year = int(match[2]) if match[2] else section_year
            if year is None:
                continue
            # A data e a ementa precisam ser os blocos imediatos do mesmo item.
            following = self.blocks[i + 1:i + 3]
            if len(following) != 2:
                continue
            date, description = (b["text"] for b in following)
            links = list(dict.fromkeys(quote(urljoin(SOURCE_URL, u), safe=":/%?=&-._~")
                                       for u in block["links"]))
            records.append(dict(number=int(match[1]), year=year, title=block["text"],
                                date=date, description=description, urls=links,
                                explicit_year=bool(match[2])))
        identities = {(c["number"], c["year"]) for c in records}
        # Um título fora de p/h1–h6 pode fornecer candidato, mas não data ou
        # descrição: só será aceito se o corpo do PDF confirmar os três campos.
        for title, href in self.anchors:
            match = re.fullmatch(r"Portaria\s*(?:N[º°o.]?\s*)?(\d+)\s*[/.-]\s*(20\d{2})", title, re.I)
            if match and href and (int(match[1]), int(match[2])) not in identities:
                records.append(dict(number=int(match[1]), year=int(match[2]), title=title,
                                    date="", description="", explicit_year=True,
                                    urls=[quote(urljoin(SOURCE_URL, href), safe=":/%?=&-._~")]))
        return records


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


class Cache:
    def __init__(self, directory, offline=False, timeout=25, interval=0.35):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.offline, self.timeout, self.interval = offline, timeout, interval
        self.requests, self.pdf_downloads, self.last_request = 0, 0, 0
        self.methods = Counter()
        self.opener = build_opener(NoRedirect())

    def retrieve(self, url, kind, refresh=False):
        method = "HEAD" if kind == "head" else "GET"
        key = digest(url.encode()) + "." + kind
        meta_path = self.directory / (key + ".json")
        body_path = self.directory / (key + (".pdf" if kind == "pdf" else ".html"))
        if meta_path.exists() and not refresh:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            if meta.get("error") or kind == "head":
                return meta, b""
            if body_path.exists():
                data = body_path.read_bytes()
                if digest(data) != meta["sha256"]:
                    raise ValueError("Cache alterado: " + str(body_path))
                return meta, data
        if self.offline:
            return dict(error="Sem resposta em cache; coleta offline", url=url), b""
        meta, data, current = dict(url=url), b"", url
        try:
            for _ in range(6):
                if not official_url(current):
                    raise ValueError("Destino fora do domínio HTTPS oficial")
                time.sleep(max(0, self.interval - (time.monotonic() - self.last_request)))
                self.requests += 1
                self.methods[method] += 1
                self.last_request = time.monotonic()
                try:
                    response = self.opener.open(Request(current, method=method, headers={
                        "User-Agent": "SergipePrevidencia-Portal/1.0 (conferencia de portarias)"}),
                        timeout=self.timeout)
                except HTTPError as error:
                    response = error
                with response:
                    status = response.code
                    self.log(method, current, status)
                    if status in {301, 302, 303, 307, 308}:
                        location = response.headers.get("Location")
                        if not location:
                            raise ValueError("Redirecionamento sem destino")
                        current = quote(urljoin(current, location), safe=":/%?=&-._~")
                        continue
                    meta.update(http_status=status, final_url=current,
                                content_type=response.headers.get_content_type(),
                                verificado_em=datetime.now().astimezone().isoformat(timespec="seconds"))
                    if status != 200:
                        raise ValueError(f"HTTP {status}")
                    if method != "HEAD":
                        data = response.read(20 * 1024 * 1024 + 1)
                        if len(data) > 20 * 1024 * 1024:
                            raise ValueError("Resposta excede o limite de 20 MiB")
                    if kind == "pdf":
                        if not data.startswith(b"%PDF-"):
                            raise ValueError("Resposta não começa com assinatura PDF")
                        self.pdf_downloads += 1
                    meta["sha256"] = digest(data) if data else None
                    break
            else:
                raise ValueError("Excesso de redirecionamentos")
        except (OSError, ValueError, URLError) as error:
            meta["error"] = str(error)
        if data and not meta.get("error"):
            body_path.write_bytes(data)
        meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return meta, data

    def log(self, method, url, status):
        with (self.directory / "requisicoes.jsonl").open("a", encoding="utf-8") as out:
            out.write(json.dumps(dict(method=method, url=url, status=status), ensure_ascii=False) + "\n")


def filename_identity(url, record):
    name = plain(unquote(urlsplit(url).path.rsplit("/", 1)[-1]))
    match = re.search(r"(?:portaria|^n[º°o.]?)[\s_.-]*(?:n[º°o.]?[\s_.-]*)?0*(\d+)\b(?:[\s_.-]+(20\d{2})\b)?", name)
    if not match:
        match = re.match(r"0*(\d+)[\s_.-]+(20\d{2})\b", name)
    # Muitos hrefs oficiais não contêm o ano do ato. Nesse caso o ano vem
    # do título/seção E da data do HTML; não de anos citados depois no slug.
    return bool(match and int(match[1]) == record["number"]
                and (not match[2] or int(match[2]) == record["year"]))


def pdf_evidence(cache, url, record):
    meta, body = cache.retrieve(url, "pdf")
    evidence = dict(metodo="HTML_E_PDF", url_examinada=url, **{
        k: meta.get(k) for k in ("http_status", "content_type", "verificado_em", "sha256", "final_url")})
    if meta.get("error"):
        return False, evidence, meta["error"]
    try:
        reader = PdfReader(io.BytesIO(body))
        if reader.is_encrypted:
            raise ValueError("PDF protegido")
        # Extração somente no processo: nenhum texto de PDF é impresso.
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        evidence["paginas"] = len(reader.pages)
        headings = list(re.finditer(r"^\s*PORTARIA\s*(?:N[º°o.]?\s*)?0*(\d+)\s*/\s*(20\d{2})\b",
                                    text[:1800], re.I | re.M))
        if not headings:
            raise ValueError("Título de número/ano não reconhecido no início do PDF")
        heading = headings[0]
        numbers_match = (int(heading[1]), int(heading[2])) == (record["number"], record["year"])
        # Aceita apenas a data imediatamente seguinte ao primeiro título.
        first_date = re.search(r"\b\d{1,2}\s+de\s+\w+\s+de\s+\d{4}\b",
                               text[heading.end():heading.end() + 250], re.I)
        expected_date = date_value(record["date"])
        date_match = bool(expected_date and first_date and date_value(first_date[0]) == expected_date)
        expected_description = normalized(record["description"])
        description_match = bool(expected_description and expected_description in normalized(text))
        evidence["campos_pdf"] = dict(numero_ano=numbers_match, data=date_match, descricao=description_match)
        evidence["titulo_pdf"] = heading[0].strip()
        evidence["data_pdf"] = first_date[0] if first_date else None
        if not all((numbers_match, date_match, description_match)):
            names = [name for name, ok in evidence["campos_pdf"].items() if not ok]
            return False, evidence, "PDF não confirma literalmente: " + ", ".join(names)
        return True, evidence, "Número/ano, data e descrição confirmados automaticamente no PDF"
    except Exception as error:
        return False, evidence, "Leitura/conferência PDF: " + str(error)


def associate(record, candidates, users, cache, source_hash, sample=False):
    entry = dict(ano=record["year"], numero=record["number"], titulo=record["title"],
                 data=record["date"], descricao=record["description"], situacao="PENDENTE",
                 url=None, motivo="", observacao="", conferencia={})
    expected_date = date_value(record["date"])
    if not expected_date or int(expected_date[:4]) != record["year"]:
        entry["motivo"] = "Data da origem inválida ou incompatível com o ano do ato"
        return entry
    matching = [c for c in candidates if (c["number"], c["year"]) == (record["number"], record["year"])]
    if not matching:
        entry["motivo"] = "Nenhum registro de número/ano correspondente reconhecido no HTML oficial"
        return entry
    exact = [c for c in matching if date_value(c["date"]) == date_value(record["date"])
             and date_value(record["date"]) and normalized(c["description"]) == normalized(record["description"])]
    selected = exact if len(exact) == 1 else matching
    urls = {u for c in selected for u in c["urls"] if official_url(u, pdf=True)}
    if len(urls) != 1:
        entry["motivo"] = "Candidatos sem um único href PDF oficial: " + str(len(urls))
        entry["conferencia"] = dict(urls_candidatas=sorted(urls))
        return entry
    url = urls.pop()
    candidate = selected[0]
    fields = dict(numero_ano=True, data=bool(date_value(record["date"]) and
                  date_value(candidate["date"]) == date_value(record["date"])),
                  descricao=normalized(candidate["description"]) == normalized(record["description"]))
    # Hrefs compartilhados por atos distintos não constituem prova suficiente.
    unique = len(users[url]) == 1
    html_ok = len(exact) == 1 and len(candidate["urls"]) == 1 and unique and filename_identity(url, record)
    evidence = dict(metodo="HTML_E_HEAD", url_examinada=url, fonte_sha256=source_hash,
                    campos_html=fields, titulo_fonte=candidate["title"], data_fonte=candidate["date"],
                    descricao_fonte=candidate["description"], href_unico=unique,
                    nome_arquivo_compativel=filename_identity(url, record))
    if html_ok and not sample:
        meta, _ = cache.retrieve(url, "head")
        evidence.update({k: meta.get(k) for k in ("http_status", "content_type", "verificado_em", "final_url")})
        if not meta.get("error") and meta.get("content_type") == "application/pdf":
            entry.update(situacao="CONFIRMADO", url=url, motivo="Número/ano, data e descrição iguais no HTML; href exclusivo com identidade compatível; HEAD HTTP 200 application/pdf sem autenticação", conferencia=evidence)
            return entry
    ok, pdf, reason = pdf_evidence(cache, url, record)
    pdf.update(fonte_sha256=source_hash, campos_html=fields, titulo_fonte=candidate["title"],
               data_fonte=candidate["date"], descricao_fonte=candidate["description"], href_unico=unique,
               amostra=sample)
    entry.update(situacao="CONFIRMADO" if ok else "PENDENTE", url=url if ok else None,
                 motivo=reason, conferencia=pdf)
    return entry


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-dir", type=Path, default=ROOT / "dados-entrada/outros/cache-portarias")
    parser.add_argument("--offline", action="store_true", help="Usa somente respostas em cache; não acessa a rede.")
    parser.add_argument("--atualizar-html", action="store_true", help="Coleta uma nova cópia do HTML; não apaga PDFs em cache.")
    parser.add_argument("--timeout", type=float, default=25)
    parser.add_argument("--interval", type=float, default=0.35, help="Intervalo mínimo entre requisições, em segundos (mínimo 0,2).")
    parser.add_argument("--dry-run", action="store_true", help="Não grava controles; permite preparar/cachear a conferência.")
    args = parser.parse_args()
    if args.timeout <= 0 or args.interval < 0.2 or (args.offline and args.atualizar_html):
        parser.error("Timeout positivo, intervalo >= 0,2 e --offline sem --atualizar-html são necessários")
    logging.getLogger("pypdf").setLevel(logging.ERROR)
    cache = Cache(args.cache_dir, args.offline, args.timeout, args.interval)
    try:
        meta, html = cache.retrieve(SOURCE_URL, "html", args.atualizar_html)
        if meta.get("error"):
            raise ValueError("HTML oficial indisponível: " + meta["error"])
        source = OfficialParser()
        source.feed(html.decode("utf-8-sig"))
        candidates = source.records()
        records = [r for r in read_records() if r["year"] in YEARS]
        if Counter(r["year"] for r in records) != Counter({2023: 87, 2024: 62, 2025: 74}):
            raise ValueError("Quantidade de origem mudou; revisar antes de associar")
        if any(not any(c["year"] == year for c in candidates) for year in YEARS):
            raise ValueError("HTML não oferece registros reconhecíveis para todos os três anos; nenhum controle gravado")
        users = defaultdict(set)
        for c in candidates:
            for url in c["urls"]:
                users[url].add((c["year"], c["number"], c["date"], normalized(c["description"])))
        entries = []
        sampled = set()
        for record in records:
            # Uma amostra por exercício também confere o corpo, não só o HEAD.
            sample = record["year"] not in sampled
            entry = associate(record, candidates, users, cache, meta["sha256"], sample)
            sampled.add(record["year"])
            entries.append(entry)
        for year in YEARS:
            selected = [e for e in entries if e["ano"] == year]
            confirmed = sum(e["situacao"] == "CONFIRMADO" for e in selected)
            print(f"{year}: {confirmed} vinculadas; {len(selected) - confirmed} pendentes")
            document = dict(versao=1, fonte=SOURCE_URL, conferido_em=meta["verificado_em"],
                            fonte_sha256=meta["sha256"], escopo=f"Somente portarias importadas de {year}",
                            metodo="Correspondência exata normalizada de número/ano, data e descrição no HTML, href exclusivo e nome compatível, com HEAD público PDF. Na insuficiência do HTML ou em amostra: título, data e descrição literal do PDF. Sem correspondência aproximada por similaridade.",
                            limites="Associação automática conservadora; não homologa vigência, completude, atualidade, assinaturas ou conteúdo institucional. Respostas HTTP em cache mantêm a data real de coleta.",
                            resumo=dict(registros=len(selected), vinculados=confirmed, pendentes=len(selected) - confirmed),
                            registros=selected)
            if not args.dry_run:
                path = ROOT / f"controle/portarias-{year}-vinculos.json"
                content = json.dumps(document, ensure_ascii=False, indent=2) + "\n"
                if not path.exists() or path.read_text(encoding="utf-8") != content:
                    path.write_text(content, encoding="utf-8")
        pending = [e for e in entries if e["situacao"] == "PENDENTE"]
        for e in pending[:12]:
            print(f"EXCEÇÃO {e['numero']}/{e['ano']} ({e['data']}): {e['motivo']}")
        if len(pending) > 12:
            print(f"Outras {len(pending) - 12} exceções detalhadas nos controles JSON.")
        print(f"Requisições nesta execução: {cache.requests} ({dict(cache.methods)}); PDFs baixados: {cache.pdf_downloads}")
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"Erro: {error}\nRequisições: {cache.requests}; PDFs baixados: {cache.pdf_downloads}\n")


if __name__ == "__main__":
    main()
