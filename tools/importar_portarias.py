"""Gera a consulta estática de portarias, sem alterar os HTMLs de origem.

Execute com o Python do projeto; --check confere a geração sem gravar.
Só substitui a região delimitada em Atos Normativos. Revise as referências
antes de executar novamente; anos da descrição nunca classificam o registro.
"""

import argparse
from collections import Counter
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "referencias/conteudo-institucional/portarias"
PAGE = ROOT / "dist/Portal-da-Transparencia/Institucional/AtosNormativos/index.html"
START = "    <!-- PORTARIAS:INICIO -->"
END = "    <!-- PORTARIAS:FIM -->"


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


def render(records):
    counts = Counter(r["year"] for r in records)
    summary = "; ".join(f"{year}: {counts[year]}" for year in sorted(counts))
    options = "\n".join(f'            <option value="{year}" serigyValue="{year}">{year}</option>'
                        for year in sorted(counts, reverse=True))
    rows = []
    for r in records:
        rows.append(f'''          <tr data-year="{r['year']}" data-type="Portaria">
            <td>Portaria</td><th scope="row" data-search-text>{escape(r['title'])}</th><td>{escape(r['date'])}</td>
            <td data-search-text>{escape(r['description'])}</td>
          </tr>''')
    return f'''{START}
    <section class="content-box" aria-labelledby="atos-titulo">
      <h2 id="atos-titulo">Atos normativos próprios — Portarias</h2>
      <div class="warning-notice" id="atos-aviso"><strong>Acervo parcial de protótipo:</strong> as ementas abaixo reproduzem as fontes fornecidas e dependem de conferência institucional. Os documentos integrais ainda serão vinculados. A listagem não comprova a completude do acervo, sua atualidade ou a abrangência histórica exigida. Os dados precisam de validação institucional antes da publicação definitiva.</div>
      <p>Registros importados por ano: {summary}. Total: {len(records)}. Dentro de cada ano, foi preservada a ordem da fonte.</p>
      <form class="filter-panel" data-table-filter data-target="atos-tabela" serigyItem="filtroPesquisa" aria-label="Consultar atos normativos próprios" aria-describedby="atos-aviso">
        <div class="field"><label for="atos-tipo">Tipo de ato</label><select id="atos-tipo" name="tipo"><option value="">Todos os tipos disponíveis</option><option value="Portaria">Portaria</option></select></div>
        <div class="field"><label for="atos-ano">Ano</label><select id="atos-ano" name="ano" serigyItem="historicoExercicio">
            <option value="">Todos os anos disponíveis</option>
{options}
        </select></div>
        <div class="field"><label for="atos-palavra">Palavra-chave (número ou descrição)</label><input id="atos-palavra" type="search" name="palavra" aria-controls="atos-resultados"></div>
        <div class="filter-actions"><button class="button" type="submit" serigyExecuteWaitSection="atos-resultados" aria-controls="atos-resultados">Pesquisar</button><button class="button secondary" type="reset" serigyClearForm>Limpar filtros</button></div>
      </form>
      <div id="atos-resultados" serigyLoadSection="atos-resultados">
        <p class="result-count" data-count-for="atos-tabela" role="status" aria-live="polite" aria-atomic="true">{len(records)} registro(s) encontrado(s).</p>
        <noscript><p>Os filtros precisam de JavaScript. Todos os registros estão disponíveis na tabela abaixo.</p></noscript>
        <div class="table-wrap" tabindex="0" role="region" aria-labelledby="atos-titulo">
          <table id="atos-tabela">
            <caption>Portarias — número, data e descrição conforme as fontes; inteiro teor pendente</caption>
            <thead><tr><th scope="col">Tipo</th><th scope="col">Número</th><th scope="col">Data</th><th scope="col">Descrição</th></tr></thead>
            <tbody>
{chr(10).join(rows)}
            </tbody>
          </table>
        </div>
      </div>
    </section>
{END}'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Confere a região gerada sem modificar arquivos.")
    args = parser.parse_args()
    try:
        records = read_records()
        original = PAGE.read_bytes()
        newline = "\r\n" if b"\r\n" in original else "\n"
        page = original.decode("utf-8").replace("\r\n", "\n")
        if page.count(START) != 1 or page.count(END) != 1:
            raise ValueError("Página deve conter um único par de delimitadores PORTARIAS")
        start, end = page.index(START), page.index(END) + len(END)
        updated = page[:start] + render(records) + page[end:]
        if args.check and updated != page:
            raise ValueError("Região publicada difere da geração; execute sem --check e revise o diff")
        if not args.check and updated != page:
            PAGE.write_bytes(updated.replace("\n", newline).encode("utf-8"))
        print(f"{'Conferidos' if args.check else 'Importados'}: {len(records)} registros")
        for year, count in sorted(Counter(r["year"] for r in records).items()):
            print(f"{year}: {count}")
        for r in records:
            if r["issues"]:
                print(f"AVISO: {r['title']} ({r['date']}): {' '.join(r['issues'])}")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Erro: {error}\n")


if __name__ == "__main__":
    main()
