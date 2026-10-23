"""Gera a consulta estática de portarias, sem alterar os HTMLs de origem.

Execute com o Python do projeto; --check confere a geração sem gravar.
Só substitui a região delimitada em Atos Normativos. Revise as referências
antes de executar novamente; anos da descrição nunca classificam o registro.
Os vínculos conferidos ficam em controle/portarias-AAAA-vinculos.json;
alterações nos registros de origem exigem revisão desse controle.
"""

import argparse
from collections import Counter
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "referencias/conteudo-institucional/portarias"
PAGE = ROOT / "dist/Portal-da-Transparencia/Institucional/AtosNormativos/index.html"
LINKS = ROOT / "controle/portarias-2026-vinculos.json"
START = "    <!-- PORTARIAS:INICIO -->"
END = "    <!-- PORTARIAS:FIM -->"
# Suspensão de publicação por privacidade. Os novos destinos ficam somente no
# controle interno; liberar apenas após publicação e conferência das versões públicas.
DOCUMENTOS_SUSPENSOS = {(2023, 32), (2023, 36)}


class PortariasParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.records = []
        self.field = None
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ("h4", "p"):
            if self.field:
                raise ValueError("Campo HTML não encerrado na origem")
            self.field, self.parts = tag, []
        elif tag == "br" and self.field:
            self.parts.append("\n")

    def handle_data(self, data):
        if self.field:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if tag != self.field:
            return
        text = "".join(self.parts).strip()
        self.field = None
        if tag == "h4":
            self.records.append([text])
        elif self.records:
            self.records[-1].append(text)
        elif text:
            raise ValueError("Parágrafo sem portaria correspondente")


def read_records():
    records = []
    for year in (2026, 2025, 2024, 2023):
        path = SOURCE / f"portarias{year}.html"
        parser = PortariasParser()
        source = path.read_text(encoding="utf-8-sig")
        parser.feed(source)
        if parser.field or not parser.records:
            raise ValueError(f"{path.name}: campos incompletos ou nenhum registro")
        for index, fields in enumerate(parser.records, 1):
            if len(fields) != 3 or not all(fields):
                raise ValueError(f"{path.name}, registro {index}: esperado título, data e descrição")
            title, date, description = fields
            match = re.fullmatch(r"Portaria\s+(?:N[º°]\s*)?(\d+)(?:/\s*(\d{4}))?", title, re.I)
            if not match or not date.startswith("Data:"):
                raise ValueError(f"{path.name}, registro {index}: número ou data não reconhecido")
            own_year = int(match[2]) if match[2] else year
            date = date.removeprefix("Data:").strip()
            issues = []
            if own_year != year:
                issues.append(f"Ano do número difere do arquivo de origem ({year}).")
            if re.findall(r"\b\d{4}\b", date) != [str(own_year)]:
                issues.append("Ano da data diverge do número; conferir a origem.")
            records.append(dict(title=title, date=date, description=description,
                                year=own_year, number=int(match[1]), issues=issues))
    counts = Counter((r["year"], r["number"]) for r in records)
    for record in records:
        if counts[record["year"], record["number"]] > 1:
            record["issues"].append("Número repetido na origem; registros preservados para conferência.")
    return records


def record_key(record):
    # Número isolado não distingue as duas portarias 79 e as duas 84 de 2026.
    return record["year"], record["number"], record["date"]


def read_links(records):
    """Lê a conferência editorial persistente; não presume URLs nem acessa a rede.

    Mudanças na origem exigem nova revisão: falhar é preferível a perder um
    vínculo aprovado ou associá-lo a outra ementa em uma futura importação.
    """
    links = {}
    for year in sorted({r["year"] for r in records}):
        path = LINKS if year == 2026 else ROOT / f"controle/portarias-{year}-vinculos.json"
        links.update(read_year_links([r for r in records if r["year"] == year], path))
    return {key: url for key, url in links.items() if key[:2] not in DOCUMENTOS_SUSPENSOS}


def read_year_links(records, path):
    audit = json.loads(path.read_text(encoding="utf-8"))
    if audit.get("versao") != 1:
        raise ValueError("Versão desconhecida do controle de vínculos")
    expected = {record_key(r): r for r in records}
    if len(expected) != len(records):
        raise ValueError("Identidade ambígua na origem: mesmo ano, número e data")
    reviewed, links = set(), {}
    for entry in audit["registros"]:
        key = entry["ano"], entry["numero"], entry["data"]
        if key in reviewed or key not in expected:
            raise ValueError(f"Vínculo duplicado ou sem registro de origem: {key}")
        reviewed.add(key)
        record = expected[key]
        if entry["titulo"] != record["title"] or entry["descricao"] != record["description"]:
            raise ValueError(f"Origem alterada; revisar vínculo de {record['title']} ({record['date']})")
        if entry["situacao"] == "PENDENTE":
            if entry.get("url") or not entry.get("motivo"):
                raise ValueError(f"Pendência deve ter motivo e não pode publicar URL: {key}")
            continue
        if entry["situacao"] != "CONFIRMADO":
            raise ValueError(f"Situação desconhecida no controle: {key}")
        url = entry["url"]
        parsed = urlsplit(url)
        if (parsed.scheme != "https" or parsed.hostname not in
                {"sergipeprevidencia.se.gov.br", "www.sergipeprevidencia.se.gov.br"}
                or parsed.username or parsed.password or not parsed.path.lower().endswith(".pdf")):
            raise ValueError(f"URL fora do repositório público oficial de PDFs: {key}")
        evidence = entry["conferencia"]
        if evidence["http_status"] != 200:
            raise ValueError(f"Evidência de conferência incompleta: {key}")
        method = evidence.get("metodo", "PDF_MANUAL")
        if method == "HTML_E_HEAD":
            if (evidence["content_type"] != "application/pdf"
                    or evidence["campos_html"] != dict(numero_ano=True, data=True, descricao=True)
                    or not evidence["href_unico"] or not evidence["nome_arquivo_compativel"]
                    or not re.fullmatch(r"[a-f0-9]{64}", evidence["fonte_sha256"])
                    or evidence["fonte_sha256"] != audit["fonte_sha256"]):
                raise ValueError(f"Evidência HTML/HEAD incompleta: {key}")
        elif method in {"PDF_MANUAL", "HTML_E_PDF"}:
            if (evidence["paginas"] < 1 or not re.fullmatch(r"[a-f0-9]{64}", evidence["sha256"])):
                raise ValueError(f"Evidência PDF incompleta: {key}")
            if method == "HTML_E_PDF" and evidence["campos_pdf"] != dict(numero_ano=True, data=True, descricao=True):
                raise ValueError(f"Correspondência PDF incompleta: {key}")
        else:
            raise ValueError(f"Método de conferência desconhecido: {key}")
        links[key] = url
    if reviewed != set(expected):
        raise ValueError(f"Registros sem conferência; atualizar {path.name}")
    return links


def read_planned_links(records, links):
    """Destinos autorizados de publicação, separados das evidências de PDF conferido."""
    control = (ROOT / 'controle/atos-normativos-verificacao.md').read_text(encoding='utf-8')
    entries = {}
    prefix = 'https://sergipeprevidencia.se.gov.br/wp-content/uploads/2026/10/'
    for line in control.splitlines():
        fields = [v.strip() for v in line.strip('|').split('|')]
        if len(fields) != 3 or not re.match(r'^Portaria\s+N[º°]\s*\d', fields[0]):
            continue
        identity, filename, url = fields
        if identity in entries or url != prefix + filename or not re.fullmatch(r'[a-z0-9-]+\.pdf', filename):
            raise ValueError('Destino planejado inválido ou duplicado no controle de PDFs')
        entries[identity] = url
    planned = {}
    for r in records:
        if (r['year'], r['number']) in DOCUMENTOS_SUSPENSOS:
            continue
        if record_key(r) not in links:
            identity = r['title'] + ' — ' + r['date']
            if identity not in entries:
                raise ValueError(f'Registrar destino planejado antes de gerar: {identity}')
            planned[record_key(r)] = entries[identity]
    if len(set(planned.values())) != len(planned) or set(planned.values()) & set(links.values()):
        raise ValueError('Destinos planejados não são únicos ou repetem PDF já vinculado')
    return planned


def render(records, links):
    planned = read_planned_links(records, links)
    records = [dict(r, type='Portaria', url=links.get(record_key(r)),
                    planned_url=planned.get(record_key(r))) for r in records]
    audit = json.loads((ROOT / 'controle/resolucoes-vinculos.json').read_text(encoding='utf-8'))
    resolutions = [r for r in audit['registros'] if r['situacao'] == 'CONFIRMADO']
    if len({(r['colegiado'], r['ano'], r['numero']) for r in resolutions}) != len(resolutions):
        raise ValueError('Resolução duplicada no controle')
    for r in resolutions:
        group = {'CIRP': 'Comitê de Investimentos dos Recursos Previdenciários (CIRP)',
                 'CD': 'Conselho Deliberativo (CD)'}[r['colegiado']]
        records.append(dict(type='Resolução', year=r['ano'], date=r['data'], url=r['url'],
                            title=f"Resolução {r['colegiado']} {r['numero']:03d}/{r['ano']} — {group}",
                            description=r['ementa']))
    records.sort(key=lambda r: r['year'], reverse=True)
    counts = Counter(r["year"] for r in records)
    summary = "; ".join(f"{year}: {counts[year]}" for year in sorted(counts))
    options = "\n".join(f'            <option value="{year}" serigyValue="{year}">{year}</option>'
                        for year in sorted(counts, reverse=True))
    rows = []
    for r in records:
        full_text = ""
        document_url = r['url'] or r.get('planned_url')
        if r['type'] == 'Portaria' and (r['year'], r['number']) in DOCUMENTOS_SUSPENSOS:
            document_url = None
        if document_url:
            label = f"Íntegra de {r['title']} — {r['date']} (PDF)"
            full_text = (f'<br><a href="{escape(document_url, quote=True)}" '
                         f'serigyItem="atoNormativo" aria-label="{escape(label, quote=True)}">'
                         'Íntegra do ato (PDF)</a>')
        description = f'<td data-search-text>{escape(r["description"])}</td>'
        if full_text:
            # O texto do novo link não passa a integrar a busca de ementas.
            description = f'<td><span data-search-text>{escape(r["description"])}</span>{full_text}</td>'
        title = escape(r['title'])
        rows.append(f'''          <tr data-year="{r['year']}" data-type="{r['type']}">
            <td>{r['type']}</td><th scope="row" data-search-text>{title}</th><td>{escape(r['date'])}</td>
            {description}
          </tr>''')
    return f'''{START}
    <section class="content-box" aria-labelledby="atos-titulo">
      <h2 id="atos-titulo">Atos normativos</h2>
      <p>Registros importados por ano: {summary}. Total: {len(records)}. Dentro de cada ano, foi preservada a ordem da fonte.</p>
      <form class="filter-panel" data-table-filter data-target="atos-tabela" serigyItem="filtroPesquisa" aria-label="Consultar atos normativos próprios">
        <div class="field"><label for="atos-tipo">Tipo de ato</label><select id="atos-tipo" name="tipo"><option value="">Todos</option><option value="Portaria">Portaria</option><option value="Resolução">Resolução</option></select></div>
        <div class="field"><label for="atos-ano">Ano</label><select id="atos-ano" name="ano" serigyItem="historicoExercicio">
            <option value="">Todos os anos disponíveis</option>
{options}
        </select></div>
        <div class="field"><label for="atos-palavra">Palavra-chave (número ou descrição)</label><input id="atos-palavra" type="search" name="palavra" aria-controls="atos-resultados"></div>
        <div class="filter-actions"><button class="button" type="submit" serigyExecuteWaitSection="atos-resultados" aria-controls="atos-resultados">Pesquisar</button><button class="button secondary" type="reset" serigyClearForm>Limpar filtros</button><button type="button" class="button secondary" onclick="exportarAtos('atos-tabela')">Exportar recorte (CSV)</button></div>
      </form>
      <div id="atos-resultados" serigyLoadSection="atos-resultados">
        <p class="result-count" data-count-for="atos-tabela" role="status" aria-live="polite" aria-atomic="true">{len(records)} registro(s) encontrado(s).</p>
        <noscript><p>Os filtros precisam de JavaScript. Todos os registros estão disponíveis na tabela abaixo.</p></noscript>
        <div class="table-wrap" tabindex="0" role="region" aria-labelledby="atos-titulo">
          <table id="atos-tabela">
            <caption>Atos normativos — portarias e resoluções</caption>
            <thead><tr><th scope="col">Tipo</th><th scope="col">Número</th><th scope="col">Data</th><th scope="col">Descrição</th></tr></thead>
            <tbody>
{chr(10).join(rows)}
            </tbody>
          </table>
        </div>
      </div>
    </section>
{render_export()}
{END}'''


def render_auxiliary(year):
    """Envolve o fragmento original sem reescrever seus registros."""
    source = (SOURCE / f"portarias{year}.html").read_text(encoding="utf-8-sig").rstrip()
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Portarias de {year} — SergipePrevidência</title>
</head>
<body>
{source}
</body>
</html>
'''


def render_export():
    export_script = '''<script>
function exportarAtos(id) {
  const table = document.getElementById(id);
  const quote = value => '"' + String(value).replace(/"/g, '""') + '"';
  const lines = [['Tipo', 'Número', 'Data', 'Descrição', 'URL do documento']];
  table.querySelectorAll('tbody tr').forEach(row => {
    if (row.hidden) return;
    const cells = row.querySelectorAll('td, th');
    lines.push([cells[0].textContent, cells[1].textContent, cells[2].textContent,
      (cells[3].querySelector('[data-search-text]') || cells[3]).textContent,
      row.querySelector('a[href]')?.href || '']);
  });
  const blob = new Blob(['\\ufeff' + lines.map(row => row.map(quote).join(';')).join('\\r\\n')], {type: 'text/csv;charset=utf-8'});
  const link = document.createElement('a'); link.href = URL.createObjectURL(blob);
  link.download = id + '.csv'; link.click(); setTimeout(() => URL.revokeObjectURL(link.href), 1000);
}
</script>'''
    return export_script


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Confere a região gerada sem modificar arquivos.")
    args = parser.parse_args()
    try:
        records = read_records()
        links = read_links(records)
        original = PAGE.read_bytes()
        newline = "\r\n" if b"\r\n" in original else "\n"
        page = original.decode("utf-8").replace("\r\n", "\n")
        if page.count(START) != 1 or page.count(END) != 1:
            raise ValueError("Página deve conter um único par de delimitadores PORTARIAS")
        start, end = page.index(START), page.index(END) + len(END)
        updated = page[:start] + render(records, links) + page[end:]
        # A conferência pública é factual; não reinserir avisos internos antigos.
        updated = re.sub(r'      <div class="warning-notice" id="atos-aviso">.*?</div>', '', updated)
        updated = updated.replace(' aria-describedby="atos-aviso"', '')
        updated = updated.replace('<p class="section-availability">Acervo parcial. Os documentos disponíveis podem ser acessados pelos links de íntegra.</p>', '')
        updated = re.sub(r'<!-- RESOLUCOES:INICIO -->.*?<!-- RESOLUCOES:FIM -->\n?', '', updated, flags=re.S)
        updates = [(PAGE, original, updated.replace("\n", newline).encode("utf-8"))]
        for year in sorted({r["year"] for r in records}):
            path = PAGE.parent / f"portarias/{year}/portarias{year}.html"
            content = path.read_bytes()
            ending = "\r\n" if b"\r\n" in content else "\n"
            generated = render_auxiliary(year).replace("\r\n", "\n").replace("\n", ending).encode("utf-8")
            updates.append((path, content, generated))
        for path, current, generated in updates:
            if args.check and generated != current:
                raise ValueError(f"{path.name} difere da geração; execute sem --check e revise o diff")
        if not args.check:
            for path, current, generated in updates:
                if generated != current:
                    path.write_bytes(generated)
        print(f"{'Conferidos' if args.check else 'Importados'}: {len(records)} registros")
        for year, count in sorted(Counter(r["year"] for r in records).items()):
            linked = sum(key[0] == year for key in links)
            print(f"{year}: {count}; íntegras vinculadas: {linked}; pendentes: {count - linked}")
        for r in records:
            if r["issues"]:
                print(f"AVISO: {r['title']} ({r['date']}): {' '.join(r['issues'])}")
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"Erro: {error}\n")


if __name__ == "__main__":
    main()
