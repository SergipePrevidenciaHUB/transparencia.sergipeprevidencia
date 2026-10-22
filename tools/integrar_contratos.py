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

NOTICE = 'DADO SINTÉTICO — TESTE SERIGY'

def synthetic_section():
    # Fonte de ensaio independente do JSON institucional. Nunca mesclar ao grupo contratos.
    rows, docs = [], []
    for seq, year in enumerate([2024, 2025, 2026], 1):
        ident = 'ENSAIO-SEM-VALIDADE-' + str(seq) + '/' + str(year)
        anchor = 'documento-sintetico-' + str(year)
        rows.append(f'<tr data-dado-sintetico="contratos" data-year="{year}"><td>{year}</td><td>{NOTICE}: <span serigyItem="numeroContrato">{ident}</span></td><td serigyItem="contratado">ENTIDADE FICTÍCIA DE ENSAIO {seq} — {NOTICE}</td><td serigyItem="objeto">Simulação técnica sem efeitos jurídicos — {NOTICE}</td><td><span serigyItem="inicioContrato">01/01/{year}</span> a <span serigyItem="fimContrato">31/12/{year}</span></td><td><a href="#{anchor}" serigyItem="linkContrato">Documento sintético — {NOTICE}</a></td><td>Não aplicável ao ensaio</td><td serigyItem="sequencia">{seq}</td><td serigyItem="valorContrato">R$ {seq * 100},00</td></tr>')
        docs.append(f'<article id="{anchor}"><h3>{ident} — {NOTICE}</h3><p>Documento HTML inteiramente sintético para verificar navegação. Não é contrato do SergipePrevidência e não tem validade jurídica. Entidade fictícia {seq}; objeto: simulação técnica; valor sintético R$ {seq * 100},00; período sintético 01/01/{year} a 31/12/{year}.</p></article>')
    options = ''.join(f'<option value="{y}" serigyValue="{y}">{y}</option>' for y in [2026,2025,2024])
    heads = ['Exercício de teste','Identificação de teste','Contratado fictício','Objeto sintético','Vigência sintética','Documento sintético','Aditivos','Sequência de teste','Valor sintético']
    return '<section data-dado-sintetico="contratos" aria-labelledby="titulo-ensaio"><h2 id="titulo-ensaio">Ensaio separado dos contratos reais</h2><p role="note"><strong>' + NOTICE + '</strong> — registros sem relação com despesas ou contratos do SergipePrevidência.</p><form id="filtro-contratos-teste" class="filter-panel" serigyItem="filtroPesquisa"><div class="field"><label for="ano-teste">Exercício sintético</label><select name="ano" id="ano-teste" serigyItem="historicoExercicio" serigyExecuteWaitSection="contratosEnsaio"><option value="">Todos</option>' + options + '</select></div><div class="field"><label for="texto-teste">Pesquisa no ensaio</label><input type="search" name="texto" id="texto-teste"></div><button type="submit" serigyExecuteWaitSection="contratosEnsaio">Pesquisar ensaio</button><button type="reset" serigyClearForm>Limpar ensaio</button></form><div serigyLoadSection="contratosEnsaio"><p id="contagem-contratos-teste" role="status" aria-live="polite">3 registros sintéticos.</p><button id="exportar-contratos-teste" type="button" serigyItem="salvarRelatorio" serigyValue="csv">CSV sintético</button><div class="table-wrap"><table id="tabela-contratos-teste"><caption>' + NOTICE + '</caption><thead><tr>' + ''.join('<th scope="col">'+h+'</th>' for h in heads) + '</tr></thead><tbody>' + ''.join(rows) + '</tbody></table></div></div>' + ''.join(docs) + '</section>'

def render(sinteticos=False):
    data = json.loads(SOURCE.read_text(encoding='utf-8'))
    contracts = data['contratos']
    additions = {a['id_origem']: a for a in data['aditivos']}
    esc = lambda s: html.escape(str(s), quote=True).replace('\r', '&#13;').replace('\n', '&#10;')
    rows, years = [], set()
    for c in contracts:
        found = set(re.findall(r'/((?:19|20)\d{2})\b', c['numero_literal'] or ''))
        year = next(iter(found)) if len(found) == 1 else ''
        if year:
            years.add(year)
        number = ('<span serigyItem="numeroContrato">' + esc(c['numero_literal']) + '</span>') if c['numero_literal'] else 'Não informado'
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
            vig = esc(c['vigencia_literal'])
            vig = vig.replace(dates[0], '<span serigyItem="inicioContrato">' + dates[0] + '</span>', 1)
            pos = vig.rfind(dates[1])
            vig = vig[:pos] + '<span serigyItem="fimContrato">' + dates[1] + '</span>' + vig[pos + len(dates[1]):]
        else:
            vig = esc(c['vigencia_literal']) if c['vigencia_literal'] else 'Não informada'
        url = c['url_integra']
        doc = '<a serigyItem="linkContrato" href="' + esc(url) + '">Íntegra do contrato</a>' if url else 'Não disponibilizada'
        links = []
        for ident in c['aditivos_associados']:
            a = additions[ident]
            assert a['contrato_associado'] == c['id_origem'] and a['url_integra']
            links.append('<li><a serigyItem="termoAditivo" href="' + esc(a['url_integra']) + '">' + esc(a['identificacao_literal']) + '</a></li>')
        ad = '<ul>' + ''.join(links) + '</ul>' if links else 'Não disponibilizados nesta relação'
        rows.append('<tr data-source-row="' + str(c['linha_origem']) + '" data-year="' + year + '"><td>' + (year or 'Não identificado') + '</td><td>' + number + '</td><td serigyItem="contratado">' + esc(c['contratado_literal']) + '</td><td serigyItem="objeto">' + esc(c['objeto_literal']) + '</td><td>' + vig + '</td><td>' + doc + '</td><td>' + ad + '</td></tr>')
    options = ''.join('<option value="' + y + '" serigyValue="' + y + '">' + y + '</option>' for y in sorted(years, reverse=True))
    main = '''<main id="conteudo" class="container" serigySchema="https://serigy.tce.se.gov.br/comum/contratos.html">
    <h1>Contratos</h1>
    <p>Contratos e documentos disponíveis na relação fornecida. O exercício corresponde ao ano identificado no número do contrato, não ao período de vigência. A ausência de documento ou aditivo nesta relação não significa inexistência.</p>
    <form id="filtro-contratos" class="filter-panel" role="search" aria-label="Consultar contratos" serigyItem="filtroPesquisa">
      <div class="field"><label for="ano-contratos">Exercício do instrumento</label><select id="ano-contratos" name="ano" serigyItem="historicoExercicio" serigyExecuteWaitSection="contratosTabela"><option value="">Todos os exercícios</option>''' + options + '''</select></div>
      <div class="field"><label for="texto-contratos">Pesquisar número, contratado ou objeto</label><input id="texto-contratos" name="texto" type="search"></div>
      <div class="filter-actions"><button type="submit" serigyExecuteWaitSection="contratosTabela">Pesquisar</button><button type="reset" serigyClearForm>Limpar filtros</button></div>
    </form>
    <section id="resultados-contratos" serigyLoadSection="contratosTabela" aria-labelledby="titulo-relacao-contratos"><h2 id="titulo-relacao-contratos">Relação de contratos</h2>
    <p id="contagem-contratos" role="status" aria-live="polite">''' + str(len(contracts)) + ''' contratos.</p>
    <div class="exports"><button id="exportar-contratos" type="button" serigyItem="salvarRelatorio" serigyValue="csv">Baixar recorte em CSV</button></div>
    <div class="table-wrap"><table id="tabela-contratos"><caption>Contratos e aditivos associados</caption><thead><tr>''' + ''.join('<th scope="col">' + x + '</th>' for x in ['Exercício do instrumento','Número do contrato','Contratado(a)','Objeto','Vigência informada','Íntegra','Aditivos associados']) + '</tr></thead><tbody>' + '\n'.join(rows) + '</tbody></table></div></section></main>'
    main = main.replace('</main>', '<p class="update-info">Informações atualizadas em <span serigyItem="dataUltimaAtualizacao">22/10/2026</span></p></main>')
    if sinteticos:
        main = main.replace('</main>', synthetic_section() + '</main>')
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
