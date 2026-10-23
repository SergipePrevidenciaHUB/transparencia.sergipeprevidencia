"""Mantém a declaração institucional de Sanções, sem registros sancionatórios."""
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
PAGE=ROOT/'dist/Portal-da-Transparencia/Licitacoes/Sancoes/index.html'
DECLARACAO='O SergipePrevidência informa que não houve licitantes ou contratados sancionados administrativamente pela própria unidade até 21/10/2026.'
PERIODO='Até 21/10/2026; início do período não confirmado.'
def render():
    options=''.join(f'<option value="{y}" serigyValue="{y}">{y}</option>' for y in [2026,2025,2024,2023])
    main=f'''<main id="conteudo" class="container" serigySchema="https://serigy.tce.se.gov.br/comum/licitacoes.html">
    <h1>Sanções</h1>
    <section aria-labelledby="titulo-relacao-sancoes"><h2 id="titulo-relacao-sancoes">Licitantes e contratados sancionados</h2><p id="declaracao-sancoes">{DECLARACAO}</p></section>
    <form id="filtro-sancoes" class="filter-panel" aria-label="Consultar declaração de sanções" serigyItem="filtroPesquisa">
      <div class="field"><label for="exercicio-sancoes">Exercício consultado</label><select id="exercicio-sancoes" name="exercicio" serigyItem="historicoExercicio" serigyExecuteWaitSection="sancoesTabela"><option value="">Todo o período declarado</option>{options}</select></div>
      <div class="filter-actions"><button type="submit" serigyExecuteWaitSection="sancoesTabela">Pesquisar</button><button type="reset" serigyClearForm>Limpar filtros</button></div>
    </form>
    <div id="resultados-sancoes" serigyLoadSection="sancoesTabela">
      <p id="contagem-sancoes" role="status" aria-live="polite">Nenhuma pessoa sancionada na declaração institucional. Consulta: todo o período declarado, até 21/10/2026.</p>
      <div class="table-wrap"><table id="tabela-sancoes" aria-describedby="declaracao-sancoes"><caption>Declaração institucional — todo o período declarado, até 21/10/2026</caption><thead><tr><th scope="col">Nome</th><th scope="col">CPF/CNPJ</th></tr></thead><tbody><tr><td serigyItem="nomeSancionado" serigyEmpty="Não há nome de sancionado a apresentar: a unidade declarou ausência de sanções até 21/10/2026.">Não houve licitantes ou contratados sancionados pela unidade até 21/10/2026, conforme declaração institucional.</td><td serigyItem="idSancionado" serigyEmpty="Não há CPF/CNPJ associado: a declaração institucional não contém pessoa sancionada até 21/10/2026.">Não se aplica à declaração de ausência de sanções.</td></tr></tbody></table></div>
    </div>
    <button id="csv-sancoes" type="button" serigyItem="salvarRelatorio" serigyValue="csv">Exportar declaração em CSV</button>
    <div id="atualizacao-sancoes" class="update-info" serigyItem="dataUltimaAtualizacao">Informações atualizadas em <time datetime="2026-10-22">22/10/2026</time></div>
  </main>'''
    old=PAGE.read_text(encoding='utf-8')
    result=re.sub(r'<main\b.*?</main>',lambda _:main,old,count=1,flags=re.S)
    return result.replace('/assets/js/sancoes-teste.js','/assets/js/sancoes.js')
if __name__=='__main__':
    if '--ativar-teste' in sys.argv:raise SystemExit('Ensaio de Sanções removido; não reativar sem fonte autorizada.')
    text=render()
    if '--check' in sys.argv:assert PAGE.read_text(encoding='utf-8')==text
    else:PAGE.write_text(text,encoding='utf-8')
    print('OK: declaração institucional, zero registros sancionatórios, atualização 22/10/2026.')
