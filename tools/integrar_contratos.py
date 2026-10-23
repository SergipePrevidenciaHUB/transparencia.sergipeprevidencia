"""Gera somente a consulta de contratos a partir da extração conferida."""
from pathlib import Path
import datetime as dt
import html
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'dados-entrada/contratos/contratos-extraidos.json'
PAGE = ROOT / 'dist/Portal-da-Transparencia/Contratos/index.html'

def public_text(value):
    """Mascara CPFs completos identificáveis na projeção pública, sem mudar a fonte."""
    def mask(match):
        digits = re.sub(r'\D', '', match.group())
        valid = len(set(digits)) > 1 and all(int(digits[n]) == ((sum(int(digits[i]) * (n+1-i) for i in range(n)) * 10) % 11) % 10 for n in [9, 10])
        return '***.***.***-' + digits[-2:] if valid else match.group()
    return re.sub(r'(?<!\d)\d{3}\.\d{3}\.\d{3}-\d{2}(?!\d)', mask, str(value))

def data_cell(value, item, reason, record_id):
    # A futura adaptação da fonte fornece o valor confirmado aqui, sem inferir colunas.
    # Zero numérico é conteúdo; None/texto vazio são ausência justificada.
    esc = lambda v: html.escape(public_text(v), quote=True).replace('\r', '&#13;').replace('\n', '&#10;')
    if value is None or str(value).strip() == '':
        reason += ' Campo '+item+'; registro '+str(record_id)+'.'
        return '<td serigyItem="'+item+'" serigyEmpty="'+esc(reason)+'"></td>'
    return '<td serigyItem="'+item+'">'+esc(value)+'</td>'

def render(sinteticos=False):
    if sinteticos:raise ValueError('Ensaio de Contratos removido; não reativar registros sintéticos.')
    data = json.loads(SOURCE.read_text(encoding='utf-8'))
    contracts = data['contratos']
    additions = {a['id_origem']: a for a in data['aditivos']}
    esc = lambda s: html.escape(public_text(s), quote=True).replace('\r', '&#13;').replace('\n', '&#10;')
    rows, years = [], set()
    for c in contracts:
        found = set(re.findall(r'/((?:19|20)\d{2})\b', c['numero_literal'] or ''))
        year = next(iter(found)) if len(found) == 1 else ''
        if year:
            years.add(year)
        number = ('<span serigyItem="numeroContrato">' + esc(c['numero_literal']) + '</span>') if c['numero_literal'] else ''
        dates = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', str(c['vigencia_literal'] or ''))
        valid = []
        for date in dates:
            try:
                dt.datetime.strptime(date, '%d/%m/%Y')
                valid.append(date)
            except ValueError:
                valid.append(None)
        # Só marcar limites quando os dois forem identificáveis, válidos e ordenados.
        if len(dates) == 2 and all(valid) and dt.datetime.strptime(dates[0], '%d/%m/%Y') <= dt.datetime.strptime(dates[1], '%d/%m/%Y'):
            start, end = dates
        else:
            start, end = None, None
        url = c['url_integra']
        doc = '<a serigyItem="linkContrato" href="' + esc(url) + '">Íntegra do contrato</a>' if url else ''
        links = []
        for ident in c['aditivos_associados']:
            a = additions[ident]
            assert a['contrato_associado'] == c['id_origem'] and a['url_integra']
            links.append('<li><a serigyItem="termoAditivo" href="' + esc(a['url_integra']) + '">' + esc(a['identificacao_literal']) + '</a></li>')
        ad = '<ul>' + ''.join(links) + '</ul>' if links else ''
        cells = '<td>'+year+'</td>'
        cells += data_cell(c.get('sequencia'), 'sequencia', 'Sequência não fornecida na fonte conferida; aguarda informação confirmada, sem usar ordem da planilha ou número do contrato.', c['id_origem'])
        cells += data_cell(c['numero_literal'], 'numeroContrato', 'Número do contrato ausente na fonte fornecida.', c['id_origem'])
        cells += data_cell(c['contratado_literal'], 'contratado', 'Contratado ausente na fonte fornecida.', c['id_origem'])
        cells += data_cell(c.get('valorContrato'), 'valorContrato', 'Valor contratual não fornecido na fonte conferida; ausência não representa valor zero.', c['id_origem'])
        cells += data_cell(c['objeto_literal'], 'objeto', 'Objeto ausente na fonte fornecida.', c['id_origem'])
        cells += data_cell(start, 'inicioContrato', 'Início da vigência não identificável com segurança na fonte fornecida.', c['id_origem'])
        cells += data_cell(end, 'fimContrato', 'Fim da vigência não identificável com segurança na fonte fornecida.', c['id_origem'])
        cells += '<td>'+doc+'</td><td>'+ad+'</td>'
        rows.append('<tr data-source-row="'+str(c['linha_origem'])+'" data-year="'+year+'">'+cells+'</tr>')

    options = ''.join('<option value="' + y + '" serigyValue="' + y + '">' + y + '</option>' for y in sorted(years, reverse=True))
    main = '''<main id="conteudo" class="container" serigySchema="https://serigy.tce.se.gov.br/comum/contratos.html">
    <h1>Contratos</h1>
    <form id="filtro-contratos" class="filter-panel" role="search" aria-label="Consultar contratos" serigyItem="filtroPesquisa">
      <div class="field"><label for="ano-contratos">Exercício do instrumento</label><select id="ano-contratos" name="ano" serigyItem="historicoExercicio" serigyExecuteWaitSection="contratosTabela"><option value="">Todos os exercícios</option>''' + options + '''</select></div>
      <div class="field"><label for="texto-contratos">Pesquisar número, contratado ou objeto</label><input id="texto-contratos" name="texto" type="search"></div>
      <div class="filter-actions"><button type="submit" serigyExecuteWaitSection="contratosTabela">Pesquisar</button><button type="reset" serigyClearForm>Limpar filtros</button></div>
    </form>
    <section id="resultados-contratos" serigyLoadSection="contratosTabela" aria-labelledby="titulo-relacao-contratos"><h2 id="titulo-relacao-contratos">Relação de contratos</h2>
    <p id="contagem-contratos" role="status" aria-live="polite">''' + str(len(contracts)) + ''' contratos.</p>
    <div class="exports"><button id="exportar-contratos" type="button" serigyItem="salvarRelatorio" serigyValue="csv">Baixar recorte em CSV</button></div>
    <div class="table-wrap"><table id="tabela-contratos"><caption>Contratos e aditivos associados</caption><thead><tr>''' + ''.join('<th scope="col">' + x + '</th>' for x in ['Exercício','Sequência','Número do contrato','Contratado','Valor contratual','Objeto','Início da vigência','Fim da vigência','Íntegra','Aditivos']) + '</tr></thead><tbody>' + '\n'.join(rows) + '</tbody></table></div></section></main>'
    main = main.replace('</main>', '<p class="update-info">Informações atualizadas em <span serigyItem="dataUltimaAtualizacao">22/10/2026</span></p></main>')
    old = PAGE.read_text(encoding='utf-8')
    new = re.sub(r'<main\b.*?</main>', lambda _: main, old, count=1, flags=re.S)
    if '/assets/js/contratos.js' not in new:
        new = new.replace('</head>', '  <script defer src="/assets/js/contratos.js"></script>\n</head>')
    return new

if __name__ == '__main__':
    content = render('--sinteticos' in sys.argv)
    if '--check' in sys.argv:
        assert PAGE.read_text(encoding='utf-8') == content, 'HTML diverge da fonte'
        print('Contratos: HTML conciliado com a fonte.')
    else:
        PAGE.write_text(content, encoding='utf-8')
        print('Contratos: página gerada.')
