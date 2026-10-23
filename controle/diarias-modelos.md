# Diárias — modelos não publicados

## Complemento atual — consulta real de 7.1 em dist

Este complemento atualiza somente **Relação de Diárias**; não modifica Valores das Diárias (7.2) nem os modelos originais. A consulta em `/Portal-da-Transparencia/Diarias/Relacao/` usa `dados-entrada/diarias/DIARIAS_CONSOLIDADAS_2023_2026.xlsx`, aba **Plan1**: 209 linhas físicas (cabeçalho + **208 registros**), 11 colunas, sem campos vazios, fórmulas, linhas de total/subtotal ou duplicatas exatas identificadas. São 54 registros de 2023, 40 de 2024, 72 de 2025 e 42 de 2026. As colunas ANO/MÊS contêm 45 referências, de janeiro/2023 a setembro/2026; todos os registros trazem SITUAÇÃO = PAGO. Presença dos anos não comprova completude ou fechamento.

Fontes novamente conferidas somente no recorte 7.1: Cartilha PETP 2026 pp. 61–62 e Serigy Docs, seção 7.1, tabela 7.1.1–12, p. 1. A Cartilha inclui expressamente Previdências Municipais e Estadual. Exige os oito campos abaixo, atualidade de até 30 dias, histórico de pelo menos três anos anteriores, filtros mínimos por nome/mês/ano e exportação do recorte em pelo menos um formato editável. **CSV é escolha técnica entre os formatos aceitos; não se usa PDF como substituto.**

| Origem Plan1 | Campo público | Cartilha / Serigy |
| --- | --- | --- |
| C — NOME DO SERVIDOR | Nome completo do beneficiário | C p. 61; S 7.1.1 `nomeBeneficiario` (Texto). |
| D — CARGO | Cargo/função | C; S 7.1.2 `cargoBeneficiario` (Texto). Não atualizar pelo cargo atual. |
| I — Nº DE DIÁRIAS | Quantidade, inclusive frações | C; S 7.1.3 `numeroDiaria` (Numérico). Não é número de portaria. |
| G — DATA DE SAÍDA | Início do afastamento | C; S 7.1.4 `dataInicioAfastamento` (Data), somente em datas válidas. G13 é preservada literalmente sem essa marcação. |
| H — DATA DE RETORNO | Fim do afastamento | C; S 7.1.5 `dataFimAfastamento` (Data). Não calcular pela quantidade. |
| F — DESCRIÇÃO DO EVENTO | Motivo do afastamento | C; S 7.1.6 `motivoAfastamento` (Texto). |
| E — DESTINO | Destino/cidades, conforme a fonte | C; S 7.1.7 `localDestino` (Texto). Destinos múltiplos não geram novas linhas nem repetição de valores. |
| J — TOTAL RECEBIDO | Valor total recebido | C; S 7.1.8 `valorTotal` (Monetário). Decimal exato, sem multiplicar por tabela normativa. J7 = 25.003 mantém três casas. |

**DT — campos de contexto:** A/ANO e B/MÊS são exibidos e usados pelos seletores como referências explícitas da planilha; não se presume mês de pagamento. K/SITUAÇÃO é preservada para contextualizar a fonte. Não se criam propriedades Serigy para essas três colunas. As saídas válidas coincidem com as referências ANO/MÊS, mas isso não define seu significado contábil.

**Controles S:** `filtroPesquisa` (7.1.11) no formulário funcional; `historicoExercicio` (7.1.10) no seletor, com opções reais 2023–2026 e `serigyValue`; `salvarRelatorio` (7.1.12) no link CSV com `serigyValue="csv"`. `serigyExecuteWaitSection="resultados-relacao-diarias"` no botão corresponde ao `serigyLoadSection` dos resultados. Schema no `main`: `https://serigy.tce.se.gov.br/comum/diarias.html`. Não foi aplicado `dataUltimaAtualizacao` (7.1.9), pois a data institucional não foi fornecida; metadados do XLSX/geração não são atualização comprovada.

**Reaproveitamento:** cabeçalho, rodapé, acessibilidade, `site.css`/`portal.css` e filtro de `tabelas.js`, sem modificar componentes comuns. DT: o input rotulado Nome usa `name="palavra"`, já suportado; somente o nome recebe `data-search-text`, com busca por termos sem distinção de acentos/maiúsculas. `diarias.js` acompanha os filtros e exporta somente as linhas selecionadas. `diarias.css` limita-se à tabela e ao input em contraste. As 208 linhas permanecem no HTML inicial, sem paginação ou remoção dos nós. Sem JavaScript, a relação e o CSV completos continuam acessíveis.

**Geração:** `.\.venv\Scripts\python.exe -B tools\integrar_diarias.py`; conferir sem gravar com `--check`. Saídas: página existente, `dist/dados/diarias/relacao-diarias.csv` e relatório local ignorado `trabalho/diarias-conferencia.json`. O CSV contém os onze campos de cada registro, sem subtotais, com datas legíveis e números em notação decimal pt-BR. O XLSX não é publicado ou alterado. Não se criam links para autorizações/comprovantes, que não são anexos mínimos autônomos de 7.1.

**C**: Cartilha PETP 2026, critérios 7.1 (pp. 61–62) e 7.2 (pp. 62–63), aplicáveis à Previdência Estadual. **S**: seção 7 do Serigy Docs, pp. 1–2. **DT**: escolha técnica de estrutura, sem criar exigência normativa. Foram lidos `AGENTS.md` e somente as fichas 7.1–7.2 do inventário; o modelo de Terceirizados foi usado apenas para o visual e componentes comuns.

## Caminhos e isolamento

| Critério C / seção S | Modelo versionável | Rota prevista |
| --- | --- | --- |
| 7.1 / 7.1 Relação de Diárias | `modelos/Portal-da-Transparencia/Diarias/Relacao/index.html` | `/Portal-da-Transparencia/Diarias/Relacao/` |
| 7.2 / 7.2 Valores Diária | `modelos/Portal-da-Transparencia/Diarias/TabelaValores/index.html` | `/Portal-da-Transparencia/Diarias/TabelaValores/` |

Os segmentos após o prefixo do Portal são os literais de S. Ambos os modelos ficam fora de `dist`, origem publicada pelo preparador existente; não recebem entrada no menu, mapa ou manifesto públicos. Cabeçalho, rodapé, navegação e acessibilidade são reutilizados sem alterar outros arquivos. O schema confirmado está no `main`: `https://serigy.tce.se.gov.br/comum/diarias.html`.

As tabelas têm somente cabeçalhos e `tbody` vazio, sem linhas fictícias. Controles estão desativados, reservas de atualização estão vazias e sem `serigyItem`. Nenhum dado, link documental ou declaração de não ocorrência/vigência foi inventado. As marcações dos componentes gerais reais foram preservadas; as de dados abaixo são instruções de aplicação futura, não marcações sobre campos vazios.

## Relação de Diárias — 7.1

DT: tabela HTML, com todos os mínimos visíveis na mesma linha por afastamento/concessão, em seção própria. C admite detalhes complementares, mas exige todos os campos na exportação e não aceita apenas a consulta de despesas como substituta desta seção. Não é obrigação C anexar autorizações ou comprovantes individuais.

| Coluna de `#tabela-relacao-diarias` | Exigência C p. 61 | Item S / `serigyItem` futuro | Tipo S |
| --- | --- | --- | --- |
| Nome completo do beneficiário | Nome de quem recebeu | 7.1.1 `nomeBeneficiario` | Texto |
| Cargo/função | Cargo ou função do beneficiário | 7.1.2 `cargoBeneficiario` | Texto |
| Número de diárias | Quantidade utilizada por afastamento; não é número da portaria | 7.1.3 `numeroDiaria` | Numérico |
| Início do afastamento | Data inicial | 7.1.4 `dataInicioAfastamento` | Data |
| Fim do afastamento | Data final | 7.1.5 `dataFimAfastamento` | Data |
| Motivo do afastamento | Finalidade | 7.1.6 `motivoAfastamento` | Texto |
| Destino (cidade) | Local com identificação do nome da cidade | 7.1.7 `localDestino` | Texto |
| Valor total recebido | Total efetivamente informado pela fonte | 7.1.8 `valorTotal` | Monetário |

| Controle / requisito C p. 62 | Reserva | S / ativação futura |
| --- | --- | --- |
| Filtro mínimo: nome, mês e ano | `#filtro-relacao-diarias`; campos `#nome-relacao-diarias`, `#mes-relacao-diarias`, `#ano-relacao-diarias` | 7.1.11 `filtroPesquisa` no formulário funcional. Não criar itens para mês/nome do formulário sem documentação. |
| Pelo menos os três anos anteriores ao da consulta | `#ano-relacao-diarias` | 7.1.10 `historicoExercicio`, opções reais com `serigyValue`; os anos do exemplo S não limitam o acervo. |
| Exportar conjunto selecionado em pelo menos um formato editável, com todos os mínimos | `#exportar-relacao-diarias` | 7.1.12 `salvarRelatorio`, `serigyValue` do formato efetivo. DT a implementar: CSV ou outro editável. O PDF exemplificado em S não substitui o editável exigido por C 7.1. |
| Atualidade: dados mais recentes de até 30 dias da consulta | `#atualizacao-relacao-diarias` | 7.1.9 `dataUltimaAtualizacao`, somente após receber e preencher a referência real; não usar a data de geração do HTML. |

A origem precisa definir qual fato/data determina o mês/ano da consulta, sem presumir pagamento, início do afastamento ou concessão. Preservar o valor recebido e a quantidade reais; não calcular total automaticamente a partir da tabela normativa. Múltiplos pagamentos/ajustes relativos ao mesmo afastamento exigem regra da fonte para evitar contagem repetida; não foi criada solução contábil nem totalizador.

## Valores das Diárias — 7.2

C exige tabela ou relação dos valores previstos para dentro do Estado, fora do Estado e fora do país; aceita a tabela da própria normativa, desde que localizada na seção específica de diárias. DT: tabela HTML com reserva para norma e vigência, sem exigir transcrição de toda a lei ou PDF novo.

| Coluna de `#tabela-valores-diarias` | Origem | Item S / `serigyItem` futuro | Tipo S |
| --- | --- | --- | --- |
| Faixa de aplicação, conforme a norma | DT: associar valores às condições/faixas que a fonte efetivamente estabelecer | Sem item específico documentado; não inventar propriedade | Texto de contexto, se aplicável |
| Dentro do Estado | C 7.2 | 7.2.1 `valorEstadual` | Monetário |
| Fora do Estado (Brasil) | C 7.2; S denomina nacional | 7.2.2 `valorNacional` | Monetário |
| Fora do país | C 7.2 | 7.2.3 `valorInternacional` | Monetário |

A coluna de faixa não impõe cargos, classes ou novos valores: só será preenchida com condições reais da norma; se a tabela for uniforme e não tiver faixas, ajustar essa apresentação na alimentação, sem fabricar categoria. Identificar moeda, unidade e condições conforme a fonte; não copiar reais/dólares ou cifras dos exemplos S nem converter valores por suposição.

| Controle / requisito C p. 63 | Reserva | S / ativação futura |
| --- | --- | --- |
| Filtro específico, sem parâmetros mínimos enumerados | `#filtro-valores-diarias`, `#ano-valores-diarias` | 7.2.6 `filtroPesquisa`. DT: exercício para selecionar versões/valores aplicáveis, não filtro mínimo nominalmente exigido por C. |
| Pelo menos os três anos anteriores ao da consulta | `#ano-valores-diarias` | 7.2.5 `historicoExercicio`, opções com exercícios reais e `serigyValue`. Uma norma pode vigorar por vários anos: vincular ao período real sem inventar revisões anuais. |
| Atualidade: até um ano; se a tabela foi atualizada há mais tempo, informar expressamente que é a versão mais recente e continua vigente | `#atualizacao-valores-diarias` e `#vigencia-valores-diarias` | 7.2.4 `dataUltimaAtualizacao` apenas na data real; declaração de vigência depende de confirmação e não deve ser marcada como se fosse data. |

**Sem gravação de relatórios autônoma em C 7.2 e sem `salvarRelatorio` na tabela S 7.2.** Não há botão de exportação no modelo. Acesso a uma norma/tabela oficial em `#normas-valores-diarias` é documental, não nova obrigação de exportação editável.

Se não houver previsão legal de diárias internacionais, C pp. 62–63 exige informar isso expressamente. A reserva `#previsao-internacional-diarias` só receberá texto após confirmação da legislação; não preencher internacional com zero, data ou traço marcado como valor monetário. Não presumir ausência de previsão da simples falta de documento.

## Marcação e liberação futura

Aplicar os itens de dados às células reais, mantendo a associação por afastamento (7.1) ou faixa/versão da norma (7.2). Reserva de carregamento: `#pesquisar-relacao-diarias` → `#resultados-relacao-diarias`; `#pesquisar-valores-diarias` → `#resultados-valores-diarias`. Usar `serigyExecuteWaitSection` na ação e `serigyLoadSection` no resultado com valor coincidente por consulta; IDs são DT, não nomes obrigatórios dos exemplos. Hoje não há ação funcional anunciada.

Documentos/URLs oficiais só entram após conferência de correspondência, íntegra e acesso público. Não criar caminhos por suposição nem usar `serigyLink` para PDF. Uma declaração de inexistência de pagamentos em 7.1 depende de confirmação institucional e referência de cobertura; não foi gerada a partir de tabela vazia.

Antes de publicar, atender às pendências de `controle/diarias-pendencias.md`, alimentar e conferir dados/documentos, histórico e atualização, implementar filtros e somente a exportação aplicável, aplicar marcações nos valores existentes e testar os recortes. Depois, em tarefa autorizada, mover as páginas completas para `dist` e ajustar navegação. Modelo vazio não comprova atendimento.


## Valores das Diárias — alimentação de C 7.2 / Serigy 7.2

Fonte: `dados-entrada/diarias/tabela-diarias.xlsx`, aba base (48 linhas), e `dados-entrada/diarias/observacoes-tabela-diarias.txt`. A página existente `/Portal-da-Transparencia/Diarias/TabelaValores/` foi alimentada sem alterar Relação de Diárias ou outras seções. Há 12 linhas por exercício de 2023 a 2026; em cada ano, quatro grupos I–IV em cada um dos três âmbitos. Cargo, grupo, ordem e valores foram preservados.

- ANO → exercício da consulta/histórico; TIPO → âmbito; GRUPO e CARGO → identificações da faixa, sem propriedades Serigy inventadas.
- Dentro do Estado: dois valores rotulados com/sem pernoite, cada valor real marcado `valorEstadual` (S 7.2.1). Os quatro sinais “-” do grupo I, um por exercício, são literais sem marcação monetária; não significam zero. Não foi inventada interpretação jurídica para o sinal.
- Fora do Estado: `valorNacional` (S 7.2.2), em reais. Fora do país: `valorInternacional` (S 7.2.3), sem prefixo R$; contexto explícito de euros (€) para União Europeia e dólares (US$) para demais localidades, conforme observações e Anexo I. A tabela não converte moedas nem representa pagamento efetivo.
- Schema `https://serigy.tce.se.gov.br/comum/diarias.html`; filtro por exercício `filtroPesquisa` (S 7.2.6); histórico `historicoExercicio` (S 7.2.5), com `serigyValue` real por opção. Botão e tabela ligados a `tabela-valores-diarias` por `serigyExecuteWaitSection`/`serigyLoadSection`; limpeza `serigyClearForm`. Reutiliza `tabelas.js`, sem alteração do componente compartilhado. As 48 linhas estão no HTML inicial.
- `dataUltimaAtualizacao` (S 7.2.4) permanece sem valor e sem atributo aplicado: exercícios da fonte e importação não substituem data comprovada. C 7.2 não exige gravação autônoma; nenhum download artificial foi criado a partir do exemplo genérico Serigy.

Fundamento público: Decreto nº 239/2023, de 17 de janeiro de 2023, especialmente Anexo I, com a URL exata fornecida nas observações: https://www.se.gov.br/anexos/uploads/download/filename_novo/5589/4fe904f774ae441e53caba484bcfa3a3.pdf . O link foi consultado e abriu PDF de 17 páginas, identificado como esse decreto; Anexo I na página 14 impressa. Sem `serigyLink` para PDF. Decretos 40.743/2020 e 30.956/2018, citados no texto de origem, não são apresentados como fundamento vigente da tabela. A observação interestadual sobre deslocamentos do Distrito Federal foi preservada em texto.

Não foi reproduzida a afirmação genérica da origem de que a norma seria a mais atualizada/em pleno vigor: a conferência institucional de alterações posteriores continua pendente. Os exercícios 2023–2026 reproduzem a planilha, sem inferir vigência desde 1º de janeiro de 2023 ou atualidade em cada data.

Geração: `.\.venv\Scripts\python.exe -B tools/integrar_valores_diarias.py`; conferir sem escrita com `--check`. Conciliação das 48 linhas e valores: `tools/testar_valores_diarias.py`.
