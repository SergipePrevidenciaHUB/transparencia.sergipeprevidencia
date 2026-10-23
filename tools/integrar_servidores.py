"""Gera a relação nominal 6.1 e a remuneração 6.2 conciliada por período e nome."""
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from html import escape
import argparse
import csv
import io
import json
import re
import unicodedata

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'dados-entrada/rh/relacao-servidores.xlsx'
PAGE = ROOT / 'dist/Portal-da-Transparencia/RecursosHumanos/FolhaPagamento/index.html'
CSV = ROOT / 'dist/dados/recursos-humanos/servidores.csv'
PAY_SOURCE = ROOT / 'dados-entrada/rh/remuneracao.xlsx'
PAY_CSV = ROOT / 'dist/dados/recursos-humanos/remuneracao.csv'
PAY_REPORT = ROOT / 'controle/remuneracao-conciliacao.json'
PAY_HEADERS = ['Ano da competência', 'Mês da competência', 'Nome completo', 'Cargo/função', 'Valor de rendimentos do contracheque']
STAGE_LABELS = {'ESTAGIARIO UNIVERSITARIO - RESOL 001/21', 'ESTAGIARIO UNIVERSITARIO - RESOL 001/22'}
HEADERS = ['Ano da relação', 'Mês da relação', 'Nome completo', 'Cargo/função', 'Lotação', 'Data de início de exercício', 'Data de exoneração ou inativação', 'Carga horária informada', 'Valor de rendimentos do contracheque']
MONTHS = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']


def clean(value):
    if value is None or str(value).strip().upper() == 'VAZIO':
        return ''
    return str(value)


def valid_date(value):
    try:
        datetime.strptime(value, '%d/%m/%Y')
        return True
    except ValueError:
        return False


def load():
    book = load_workbook(SOURCE, read_only=True, data_only=False)
    try:
        sheet = book['Plan1']
        assert tuple(next(sheet.values)) == ('Ano', 'Mês', 'Nome do Servidor', 'Local', 'Data de Início de Exercicío', 'Data de Exoneração ou Inativação', 'Função', 'Cargo Efetivo', 'Quantidade de Horas')
        records = []
        for number, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), 2):
            year, month = str(int(row[0])), str(int(row[1]))
            assert 1 <= int(month) <= 12
            role = '; '.join(label + ': ' + clean(value) for label, value in [('Função', row[6]), ('Cargo efetivo', row[7])] if clean(value).strip())
            values = [year, month, clean(row[2]), role, clean(row[3]), clean(row[4]), clean(row[5]), clean(row[8])]
            records.append((number, values))
        return records
    finally:
        book.close()


def csv_text(records):
    output = io.StringIO(newline='')
    writer = csv.writer(output, delimiter=';', quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    writer.writerow(HEADERS)
    writer.writerows(values for _, values in records)
    return '\ufeff' + output.getvalue()


def person_key(year, month, name):
    # Sem aproximação fonética ou remoção de acentos: não juntar homônimos por heurística.
    return str(int(year)), str(int(month)), ' '.join(unicodedata.normalize('NFC', name).split()).casefold()


def reconcile_payroll(records, payroll):
    """Aceita somente chaves únicas dos dois lados; nunca soma linhas duplicadas."""
    relation = defaultdict(list)
    pay = defaultdict(list)
    stages, exceptions, matched = [], [], []
    for row, values in records:
        relation[person_key(values[0], values[1], values[2])].append((row, values))
    for row, values in payroll:
        if clean(values[4]).strip().upper() in STAGE_LABELS:
            stages.append({'linha_remuneracao': row, 'ano': str(int(values[0])), 'mes': str(int(values[1])), 'classificacao': values[4]})
        else:
            pay[person_key(values[0], values[1], values[2])].append((row, values))
    duplicates = []
    precision = []
    for key in sorted(set(relation) | set(pay)):
        left, right = relation[key], pay[key]
        if len(left) > 1 or len(right) > 1:
            duplicates.append({'ano': key[0], 'mes': key[1], 'nome': key[2], 'linhas_relacao': [n for n, _ in left], 'linhas_remuneracao': [n for n, _ in right]})
        for row, raw in right:
            if len(left) != 1 or len(right) != 1:
                exceptions.append({'linha_remuneracao': row, 'ano': key[0], 'mes': key[1], 'nome': raw[2], 'motivo': 'associação ambígua' if len(left) > 1 or len(right) > 1 else 'sem correspondência na relação'})
                continue
            try:
                amount = Decimal(str(raw[5]))
                if not amount.is_finite():
                    raise InvalidOperation
                cents = amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                # A origem exibe duas casas. Não arredondar uma precisão real inesperada.
                if abs(amount - cents) > Decimal('0.00000001'):
                    raise InvalidOperation
            except (InvalidOperation, ValueError):
                exceptions.append({'linha_remuneracao': row, 'ano': key[0], 'mes': key[1], 'nome': raw[2], 'motivo': 'rendimentos inválidos ou precisão além do formato monetário da origem'})
                continue
            relation_row, values = left[0]
            if amount != cents:
                precision.append({'linha_remuneracao': row, 'valor_armazenado': str(amount), 'valor_exibido': str(cents)})
            matched.append({'linha_remuneracao': row, 'linha_relacao': relation_row, 'values': [key[0], key[1], values[2], values[3], format(cents, '.2f').replace('.', ',')]})
    matched.sort(key=lambda r: r['linha_remuneracao'])
    totals = {year: format(sum((Decimal(r['values'][4].replace(',', '.')) for r in matched if r['values'][0] == year), Decimal(0)), '.2f') for year in sorted({r['values'][0] for r in matched})}
    report = {'fontes': ['dados-entrada/rh/relacao-servidores.xlsx', 'dados-entrada/rh/remuneracao.xlsx'], 'chave': ['ano', 'mes', 'nome (NFC, espaços e caixa normalizados; acentos preservados)'], 'linhas_fonte_remuneracao': len(payroll), 'estagios_excluidos': stages, 'estagios_por_ano': dict(Counter(r['ano'] for r in stages)), 'conciliados': len(matched), 'conciliados_por_ano': dict(Counter(r['values'][0] for r in matched)), 'duplicidades': duplicates, 'pendencias': exceptions, 'linhas_relacao_sem_publicacao_remuneratoria': [n for n, _ in records if n not in {r['linha_relacao'] for r in matched}], 'valores_por_ano_reais': totals, 'formato_origem': '#,##0.00_);(#,##0.00)', 'residuos_numericos_de_representacao': precision, 'regra_precisao': 'Centavos conforme formato da fonte; resíduos até 0.00000001 real registrados. Precisão real superior fica pendente.', 'campos_publicados': PAY_HEADERS, 'atualizacao': None}
    assert len(matched) + len(stages) + len(exceptions) == len(payroll)
    return matched, report


def load_payroll(records):
    book = load_workbook(PAY_SOURCE, read_only=True, data_only=False)
    try:
        sheet = book['Plan1']
        assert tuple(next(sheet.values)) == ('Ano', 'Mês', 'Nome do Servidor', 'Função', 'Cargo Efetivo', 'Valor de Rendimento Contra-Cheque', 'Valor de Desconto Contra-Cheque', 'Valor de Líquido Contra-Cheque')
        payroll = []
        for row, cells in enumerate(sheet.iter_rows(min_row=2), 2):
            assert cells[5].number_format == '#,##0.00_);(#,##0.00)', 'Conferir formato monetário alterado na origem'
            payroll.append((row, tuple(c.value for c in cells)))
        return reconcile_payroll(records, payroll)
    finally:
        book.close()


def pay_csv_text(records):
    output = io.StringIO(newline='')
    writer = csv.writer(output, delimiter=';', quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    writer.writerow(PAY_HEADERS)
    writer.writerows(r['values'] for r in records)
    return '\ufeff' + output.getvalue()


def render_payroll(records):
    years = ''.join(f'<option value="{y}" serigyValue="{y}">{y}</option>' for y in sorted({r['values'][0] for r in records}, reverse=True))
    months = ''.join(f'<option value="{m}">{MONTHS[int(m)-1]}</option>' for m in sorted({r['values'][1] for r in records}, key=int))
    rows = []
    for record in records:
        values = record['values']
        amount = Decimal(values[4].replace(',', '.'))
        labels = [values[0], MONTHS[int(values[1])-1], values[2], values[3], 'R$ ' + format(amount, ',.2f').replace(',', '_').replace('.', ',').replace('_', '.')]
        cells = ''.join(f'<td' + (f' serigyItem="{item}"' if item and values[i] else '') + (' class="money"' if i == 4 else '') + f'>{escape(label) if label else "Não informado"}</td>' for i, (label, item) in enumerate(zip(labels, ['', '', 'nomeServidor', 'cargoServidor', 'salarioServidor'])))
        attrs = escape(json.dumps(values, ensure_ascii=False), quote=True)
        rows.append(f'          <tr data-remuneracao-row="{record["linha_remuneracao"]}" data-relacao-row="{record["linha_relacao"]}" data-export-values="{attrs}">' + cells + '</tr>')
    headings = ''.join(f'<th scope="col">{h}</th>' for h in PAY_HEADERS)
    return f'''<section aria-labelledby="titulo-remuneracao">
      <h2 id="titulo-remuneracao">Remuneração nominal</h2>
      <p>Valores de rendimentos informados nos contracheques, por competência.</p>
      <form id="filtro-remuneracao" class="filter-panel" role="search" aria-label="Consultar remuneração nominal" serigyItem="filtroPesquisa">
        <div class="field"><label for="nome-remuneracao">Nome completo</label><input id="nome-remuneracao" name="nome" type="search"></div>
        <div class="field"><label for="mes-remuneracao">Mês da competência</label><select id="mes-remuneracao" name="mes"><option value="">Todos</option>{months}</select></div>
        <div class="field"><label for="ano-remuneracao">Ano da competência</label><select id="ano-remuneracao" name="ano" serigyItem="historicoExercicio"><option value="">Todos</option>{years}</select></div>
        <div class="filter-actions"><button id="pesquisar-remuneracao" type="submit" serigyExecuteWaitSection="tabela-remuneracao">Pesquisar</button><button type="reset" class="secondary" serigyClearForm>Limpar filtros</button></div>
      </form>
      <div id="resultados-remuneracao" role="region" aria-label="Resultados de remuneração nominal">
        <div class="exports"><strong>Baixar registros selecionados:</strong> <a id="exportar-remuneracao" href="/dados/recursos-humanos/remuneracao.csv" download serigyItem="salvarRelatorio" serigyValue="csv">CSV</a></div>
        <p class="result-count" data-count-for="tabela-remuneracao" aria-live="polite">{len(records)} registro(s) encontrado(s).</p>
        <p id="remuneracao-vazio" hidden>Nenhum registro encontrado para os filtros selecionados.</p>
        <div class="table-wrap"><table id="tabela-remuneracao" serigyLoadSection="tabela-remuneracao">
          <caption>Remuneração nominal — valor de rendimentos do contracheque</caption>
          <thead><tr>{headings}</tr></thead>
          <tbody id="registros-remuneracao">
{chr(10).join(rows)}
          </tbody>
        </table></div>
      </div>
    </section>'''


def render(records):
    years = ''.join(f'<option value="{y}" serigyValue="{y}">{y}</option>' for y in sorted({v[0] for _, v in records}, reverse=True))
    months = ''.join(f'<option value="{m}">{MONTHS[int(m)-1]}</option>' for m in sorted({v[1] for _, v in records}, key=int))
    rows = []
    # Equivalência entre início de exercício e admissão confirmada pela instituição para esta relação.
    markers = ['', '', 'nomeServidor', 'cargoServidor', 'lotacaoServidor', 'admissaoServidor', 'exoneracaoServidor', 'cargaHoraria', 'salarioServidor']
    for number, values in records:
        cells = []
        for i, (value, item) in enumerate(zip(values, markers)):
            present = bool(value.strip())
            if i == 6 and value and not valid_date(value):
                item = ''
            marker = f' serigyItem="{item}"' if item and present else ''
            if item and not present:
                reason = 'Rendimento não atribuído: associação ambígua na fonte.' if i == 8 else 'Campo não informado na relação fornecida; não se presume situação do vínculo.'
                marker = f' serigyItem="{item}" serigyEmpty="{escape(reason, quote=True)}"'
            label = MONTHS[int(value)-1] if i == 1 else value
            if i == 8 and present:
                label = 'R$ ' + format(Decimal(value.replace(',', '.')), ',.2f').replace(',', '_').replace('.', ',').replace('_', '.')
            cells.append(f'<td{marker}>{escape(label) if present else ("" if i == 6 else "Não informado")}</td>')
        attrs = escape(json.dumps(values, ensure_ascii=False), quote=True)
        rows.append(f'          <tr data-source-row="{number}" data-year="{values[0]}" data-month="{values[1]}" data-export-values="{attrs}">' + ''.join(cells) + '</tr>')
    headings = ''.join(f'<th scope="col">{h}</th>' for h in HEADERS)
    return f'''<section aria-labelledby="titulo-vinculos">
      <h2 id="titulo-vinculos">Servidores e remuneração nominal</h2>
      <form id="filtro-vinculos" class="filter-panel" role="search" aria-label="Consultar relação nominal de servidores" serigyItem="filtroPesquisa">
        <div class="field"><label for="nome-vinculos">Nome completo</label><input id="nome-vinculos" name="nome" type="search"></div>
        <div class="field"><label for="cargo-vinculos">Cargo/função</label><input id="cargo-vinculos" name="cargo" type="search"></div>
        <div class="field"><label for="ano-vinculos">Ano da relação</label><select id="ano-vinculos" name="ano" serigyItem="historicoExercicio"><option value="">Todos</option>{years}</select></div>
        <div class="field"><label for="mes-vinculos">Mês da relação</label><select id="mes-vinculos" name="mes"><option value="">Todos</option>{months}</select></div>
        <div class="filter-actions"><button id="pesquisar-vinculos" type="submit" serigyExecuteWaitSection="tabela-vinculos">Pesquisar</button><button type="reset" class="secondary" serigyClearForm>Limpar filtros</button></div>
      </form>
      <div id="resultados-vinculos" role="region" aria-label="Resultados da relação nominal de servidores">
        <div class="exports"><strong>Baixar registros selecionados:</strong> <a id="exportar-vinculos" href="/dados/recursos-humanos/servidores.csv" download serigyItem="salvarRelatorio" serigyValue="csv">CSV</a></div>
        <p class="result-count" data-count-for="tabela-vinculos" aria-live="polite">{len(records)} registro(s) encontrado(s).</p>
        <p id="vinculos-vazio" hidden>Nenhum registro encontrado para os filtros selecionados.</p>
        <div class="table-wrap"><table id="tabela-vinculos" serigyLoadSection="tabela-vinculos">
          <caption>Servidores e rendimentos do contracheque por período</caption>
          <thead><tr>{headings}</tr></thead>
          <tbody id="registros-vinculos">
{chr(10).join(rows)}
          </tbody>
        </table></div>
      </div>
    </section>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    records = load()
    report = json.loads(PAY_REPORT.read_text(encoding='utf-8'))
    links = report['associacoes_confirmadas']
    assert len(links) == 1596 and len(records) == 1598
    payroll = links
    mapping = {r['linha_relacao']: r for r in links}
    assert len(mapping) == 1596
    assert set(n for n, _ in records) - set(mapping) == set(report['linhas_relacao_sem_publicacao_remuneratoria'])
    book = load_workbook(PAY_SOURCE, read_only=True, data_only=True)
    raw = {n: v for n, v in enumerate(book['Plan1'].iter_rows(min_row=2, values_only=True), 2)}
    book.close()
    combined = []
    for n, values in records:
        match = mapping.get(n)
        amount = ''
        if match:
            assert match['values'][:4] == values[:4], 'Fonte cadastral mudou; conferir vínculo registrado'
            source = raw[match['linha_remuneracao']]
            assert person_key(*source[:3]) == person_key(*values[:3])
            cents = Decimal(str(source[5])).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            amount = match['values'][4]
            assert cents == Decimal(amount.replace(',', '.')), 'Rendimento mudou; conferir conciliação'
        combined.append((n, values + [amount]))
    records = combined
    page = PAGE.read_text(encoding='utf-8')
    page, count = re.subn(r'<section aria-labelledby="titulo-vinculos">.*?</section>', lambda _: render(records), page, flags=re.S)
    assert count == 1
    page = re.sub(r'<section aria-labelledby="titulo-remuneracao">.*?</section>', '', page, flags=re.S)
    page = page.replace('  <script defer src="/assets/js/remuneracao.js"></script>', '')
    page = page.replace('datetime="2026-10-21">21/10/2026', 'datetime="2026-10-22">22/10/2026')
    if '/assets/js/servidores.js' not in page:
        page = page.replace('</head>', '  <script defer src="/assets/js/servidores.js"></script>\n  <link rel="stylesheet" href="/assets/css/servidores.css">\n</head>')
    page = re.sub(r'(?m)^[ \t]+$', '', page)
    for path, content in [(PAGE, page), (CSV, csv_text(records))]:
        if args.check:
            assert path.read_bytes() == content.encode('utf-8'), f'Divergência: {path}'
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content.encode('utf-8'))
    print(json.dumps({'registros': len(records), 'anos': dict(Counter(v[0] for _, v in records)), 'horas_informadas': dict(Counter(v[7] for _, v in records)), 'exoneracoes_preenchidas': sum(bool(v[6]) for _, v in records), 'datas_nao_reconhecidas': [(n, i) for n, v in records for i in (5, 6) if v[i] and not valid_date(v[i])], 'cargo_funcao_ausentes': sum(not v[3] for _, v in records)}, ensure_ascii=False))
    print(json.dumps({'fonte_remuneracao': report['linhas_fonte_remuneracao'], 'estagios_excluidos': len(report['estagios_excluidos']), 'publicados': len(payroll), 'por_ano': report['conciliados_por_ano'], 'pendencias': len(report['pendencias']), 'chaves_duplicadas': len(report['duplicidades'])}, ensure_ascii=False))


if __name__ == '__main__':
    main()
