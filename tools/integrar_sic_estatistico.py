"""Gera o relatório LAI somente da fonte preparada, sem reprocessar arquivos brutos."""
from pathlib import Path
from html import escape
import csv,io,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'dados-entrada/sic-ouvidoria/sic-complementos.json'
PAGE=ROOT/'dist/Portal-da-Transparencia/SIC/RelatorioAnualEstatistico/index.html'
CSV=ROOT/'dist/dados/sic/relatorio-anual.csv'
HEADERS=['Ano','Período','Pedidos recebidos','Pedidos atendidos','Pedidos indeferidos','Informações genéricas sobre solicitantes']
def load():
    data=json.loads(SOURCE.read_text(encoding='utf-8'))
    rows=data['relatorio_anual']
    assert len(rows)==4 and {r['ano'] for r in rows}=={2023,2024,2025,2026}
    for r in rows:
        for field in ['pedidos_recebidos','pedidos_atendidos','pedidos_indeferidos']:
            assert type(r[field]) is int and r[field]>=0
        assert r['pedidos_indeferidos']==0, 'Alteração da confirmação exige conferência da fonte preparada'
    return data,rows
def values(r):
    return [str(r['ano']),r['periodo']+(' (parcial)' if r['parcial'] else ''),str(r['pedidos_recebidos']),str(r['pedidos_atendidos']),str(r['pedidos_indeferidos']),r['informacoes_genericas']]
def csv_text(rows):
    out=io.StringIO(newline='');w=csv.writer(out,delimiter=';',quoting=csv.QUOTE_ALL,lineterminator='\r\n');w.writerow(HEADERS);w.writerows(values(r) for r in rows);return '\ufeff'+out.getvalue()
def render(data,rows):
    options=''.join(f'<option value="{r["ano"]}" serigyValue="{r["ano"]}">{r["ano"]}</option>' for r in sorted(rows,key=lambda r:r['ano'],reverse=True))
    marked=['','','pedidosRecebidos','pedidosAtendidos','pedidosIndeferidos','infoGenericas']
    body='\n'.join('<tr data-year="'+str(r['ano'])+'">'+''.join('<td'+(f' serigyItem="{item}"' if item else '')+'>'+escape(value)+'</td>' for item,value in zip(marked,values(r)))+'</tr>' for r in rows)
    main=f'''<main id="conteudo" class="container sic-content" serigySchema="{data['schema']}">
    <h1>Relatório Anual Estatístico</h1>
    <p class="lead">Pedidos de acesso à informação e informações agregadas sobre os solicitantes.</p>
    <form id="filtro-relatorio-sic" class="filter-panel" role="search" aria-label="Consultar relatório estatístico por exercício" serigyItem="filtroPesquisa">
      <div class="field"><label for="exercicio-relatorio-sic">Exercício</label><select id="exercicio-relatorio-sic" name="exercicio" serigyItem="historicoExercicio" serigyExecuteWaitSection="sicTabela"><option value="">Todos os exercícios</option>{options}</select></div>
      <div class="filter-actions"><button type="submit" serigyExecuteWaitSection="sicTabela">Pesquisar</button><button type="reset" class="secondary" serigyClearForm>Limpar filtros</button></div>
    </form>
    <section id="resultados-relatorio-sic" class="sic-card" aria-labelledby="titulo-relatorios-sic" serigyLoadSection="sicTabela">
      <h2 id="titulo-relatorios-sic">Relatórios por exercício</h2>
      <p id="contagem-relatorio-sic" role="status" aria-live="polite">4 relatórios no recorte.</p>
      <div class="table-wrap" tabindex="0" role="region" aria-label="Estatísticas de pedidos de informação"><table id="tabela-relatorio-sic"><caption>Pedidos de acesso à informação por exercício e período</caption><thead><tr>{''.join('<th scope="col">'+h+'</th>' for h in HEADERS)}</tr></thead><tbody id="registros-relatorio-sic">{body}</tbody></table></div>
    </section>
    <div class="sic-actions"><a id="csv-relatorio-sic" href="/dados/sic/relatorio-anual.csv" download serigyItem="salvarRelatorio" serigyValue="csv">Baixar recorte em CSV</a></div>
    <div id="atualizacao-relatorio-sic" class="update-info" serigyItem="dataUltimaAtualizacao">Informações atualizadas em <time datetime="2026-10-22">22/10/2026</time></div>
  </main>'''
    assert data['data_atualizacao_portal']=='2026-10-22'
    old=PAGE.read_text(encoding='utf-8');page=re.sub(r'<main\b.*?</main>',lambda _:main,old,count=1,flags=re.S)
    if '/assets/css/sic.css' not in page:page=page.replace('</head>','  <link rel="stylesheet" href="/assets/css/sic.css">\n</head>')
    return page
def main():
    data,rows=load()
    for p,content in [(PAGE,render(data,rows)),(CSV,csv_text(rows))]:
        if '--check' in sys.argv:assert p.read_bytes()==content.encode('utf-8'),str(p)
        else:p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(content.encode('utf-8'))
    print(json.dumps({'registros':len(rows),'por_ano':{r['ano']:[r['pedidos_recebidos'],r['pedidos_atendidos'],r['pedidos_indeferidos']] for r in rows},'2026_parcial':True},ensure_ascii=False))
if __name__=='__main__':main()
