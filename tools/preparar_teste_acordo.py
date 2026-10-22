"""Ativa/remove apenas o ensaio de 5.3; reutiliza o bloqueio genérico do deploy.

Uso: python tools/preparar_teste_acordo.py --ativar (ou --desativar).
Na desativação, o documento é guardado em trabalho/, nunca excluído.
"""
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]
ROUTE = Path('dist/Portal-da-Transparencia/Convenios/SemTransferencia')
NOTICE = 'DADO SINTÉTICO — TESTE SERIGY'
START = '<!-- INICIO ENSAIO ACORDO 5.3 -->'
END = '<!-- FIM ENSAIO ACORDO 5.3 -->'
BLOCK = '''
<!-- INICIO ENSAIO ACORDO 5.3 -->
<section id="ensaio-acordo" data-dado-sintetico="acordo" aria-labelledby="titulo-ensaio-acordo">
<h2 id="titulo-ensaio-acordo">Acordo sintético para teste</h2>
<p class="section-availability" role="note"><strong>DADO SINTÉTICO — TESTE SERIGY</strong>. Este exemplo não representa acordo, partes ou obrigações do SergipePrevidência e não integra os sete instrumentos acima.</p>
<p>O filtro por exercício acima também se aplica a este ensaio separado.</p>
<p id="contagem-ensaio-acordo" role="status" aria-live="polite">1 registro sintético no recorte.</p>
<div class="table-wrap"><table id="tabela-ensaio-acordo"><caption>DADO SINTÉTICO — TESTE SERIGY</caption>
<thead><tr><th scope="col">Natureza dos dados</th><th scope="col">Ano de início fictício</th><th scope="col">Instrumento fictício</th><th scope="col">Partes fictícias</th><th scope="col">Obrigações fictícias</th><th scope="col">Documento de teste</th></tr></thead>
<tbody><tr data-dado-sintetico="acordo" data-year="2026"><td>DADO SINTÉTICO — TESTE SERIGY</td><td>2026</td><td>ENSAIO-SEM-TRANSFERENCIA-001/2026</td><td>ENTIDADE FICTÍCIA ALFA DE ENSAIO — NÃO EXISTE; ENTIDADE FICTÍCIA BETA DE ENSAIO — NÃO EXISTE</td><td serigyItem="obrigacoes">Obrigações explicitamente fictícias: Alfa fornece arquivos artificiais de teste; Beta verifica sua leitura em ambiente de ensaio, sem obrigações ou efeitos reais.</td><td serigyItem="anexoConvenio"><a href="/Portal-da-Transparencia/Convenios/SemTransferencia/documento-sintetico.html">DADO SINTÉTICO — TESTE SERIGY — instrumento de ensaio (HTML)</a></td></tr></tbody></table></div>
<button id="csv-ensaio-acordo" type="button">CSV do recorte sintético — DADO SINTÉTICO — TESTE SERIGY</button>
</section>
<!-- FIM ENSAIO ACORDO 5.3 -->
'''
DOCUMENT = '''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>DADO SINTÉTICO — TESTE SERIGY — acordo de ensaio</title><link rel="stylesheet" href="/assets/css/site.css"></head>
<body><main class="container" data-dado-sintetico="acordo"><h1>DADO SINTÉTICO — TESTE SERIGY</h1>
<p>Instrumento inteiramente artificial ENSAIO-SEM-TRANSFERENCIA-001/2026. Não representa acordo do SergipePrevidência. Sem validade jurídica, assinaturas ou partes reais.</p>
<h2>Partes fictícias</h2><p>ENTIDADE FICTÍCIA ALFA DE ENSAIO — NÃO EXISTE; ENTIDADE FICTÍCIA BETA DE ENSAIO — NÃO EXISTE.</p>
<h2>Obrigações explicitamente fictícias</h2><p>Alfa fornece arquivos artificiais de teste; Beta verifica sua leitura em ambiente de ensaio, sem obrigações ou efeitos reais.</p>
<p>Exercício fictício: 2026. Não há transferência financeira no exemplo.</p>
<p><a href="/Portal-da-Transparencia/Convenios/SemTransferencia/">Voltar aos acordos</a></p></main></body></html>
'''


def set_mode(root=ROOT, active=True):
    page = root / ROUTE / 'index.html'
    doc = page.with_name('documento-sintetico.html')
    text = page.read_text(encoding='utf-8')
    text = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', '', text, flags=re.S)
    if active:
        anchor = '<div id="atualizacao-sem-transferencia"'
        assert text.count(anchor) == 1
        text = text.replace(anchor, BLOCK.strip() + '\n' + anchor)
        doc.write_text(DOCUMENT, encoding='utf-8')
    elif doc.exists():
        saved = root / 'trabalho/acordo-sintetico-removido/documento-sintetico.html'
        saved.parent.mkdir(parents=True, exist_ok=True)
        if saved.exists():
            assert saved.read_bytes() == doc.read_bytes(), 'Backup diferente; preservar ambos e revisar.'
        doc.replace(saved)
    page.write_text(text, encoding='utf-8')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('--ativar', action='store_true')
    g.add_argument('--desativar', action='store_true')
    args = p.parse_args()
    set_mode(active=args.ativar)
    print('Ensaio de acordo ' + ('ativo.' if args.ativar else 'removido; documento preservado em trabalho/.'))
