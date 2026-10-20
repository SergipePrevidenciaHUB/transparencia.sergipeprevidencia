# Despesas — estrutura inicial e pendências

## Escopo desta rodada

Fonte consultada: somente as fichas 4.1, 4.2 e 4.3 (Dimensão 4 — Despesas) de `controle/inventario-tabelas.md`, com suas referências já levantadas à Cartilha e ao Serigy. Não houve nova auditoria dos PDFs normativos.

**Decisão técnica:** uma página em `dist/Portal-da-Transparencia/Despesas/index.html`, com três seções e navegação por âncoras, reutilizando os componentes de Receitas. Entrada no Portal, no mapa e no manifesto da busca. Não foram definidos modelos, colunas de tabelas ou importação nesta rodada.

**Situação:** estrutura editorial em preparação. Não há dados de despesas, tabelas vazias, controles de consulta simulados, exportações ou declaração de atendimento ao PETP. Os avisos de espera não são declarações institucionais de não ocorrência.

## Critérios representados e dados pendentes

| Critério | Conteúdo previsto nas fichas | Pendência de dados |
| --- | --- | --- |
| 4.1 | Totais empenhados, liquidados e pagos no período, comparáveis na mesma página/arquivo. | Fonte contábil, período e valores conciliados dos três estágios. |
| 4.2 | Unidade orçamentária, função, subfunção, categoria econômica, grupo, elemento e fonte; códigos e descrições. | Classificações oficiais associadas à execução da despesa e respectivas descrições. |
| 4.3 | Relação e detalhe dos empenhos: credor, valor, objeto, modalidade e número do procedimento ou contratação direta/fundamentação pertinente. | Identificação efetiva dos empenhos, credores e procedimentos, com documentos de identificação necessários à consulta previstos na ficha. |

**Exigências oficiais registradas nas fichas, ainda não implementadas:** atualidade de até 30 dias; histórico de pelo menos três anos anteriores à consulta; exportação do conjunto selecionado em pelo menos um formato editável; filtros próprios. Em 4.1: exercício, mês ou período; em 4.2: exercício, mês ou período e elemento de despesa; em 4.3: número do empenho, nome e CPF/CNPJ do credor, mês e exercício. Datas de atualização e de cobertura deverão vir da fonte real, sem usar a data de criação da página como referência dos dados.

## Dúvidas e cuidados antes da implementação dos dados

- **DÚVIDA — REVISÃO NECESSÁRIA:** definir com a contabilidade a granularidade da base. Movimentos e saldos cumulativos não podem ser somados indistintamente, nem repetir o total do empenho a cada liquidação/pagamento. Os três estágios precisam de valores próprios e conciliação.
- **DÚVIDA — REVISÃO NECESSÁRIA:** número do empenho e CPF/CNPJ são necessários ao filtro de 4.3, mas a ficha informa que não possuem item próprio na tabela Serigy levantada. Não inventar `serigyItem`; confirmar a representação técnica quando a consulta for implementada.
- Confirmar o vínculo real entre despesa e procedimento de contratação; não deduzir por semelhança de valores ou números. Classificações precisam manter os códigos e as descrições, inclusive na exportação.
- O desenho de conjunto compartilhado entre 4.1–4.3 é decisão técnica proposta no inventário (M03), não obrigação de usar uma tabela HTML única ou de criar uma planilha nesta rodada.

## Marcações Serigy

Foram reutilizadas somente as marcações existentes de busca geral e acessibilidade do cabeçalho, breadcrumb e rodapé. Não foram aplicados itens de despesas aos títulos, avisos ou valores ausentes, nem `serigyEmpty` para simular não ocorrência.

Para a etapa com dados, as fichas confirmam: `valorEmpenhado`, `valorLiquidado`, `valorPago`; `unidadeDespesa`, `funcaoDespesa`, `subFuncaoDespesa`, `categoriaDespesa`, `grupoDespesa`, `elementoDespesa`, `fonteRecursosDespesa`; `credorEmpenho`, `objetoEmpenho`, `modalidadeEmpenho`, `numeroProcedimento`, `valorEmpenhoIndividual`; controles `filtroPesquisa`, `salvarRelatorio`, `dataUltimaAtualizacao` e `historicoExercicio`. Aplicar somente ao conteúdo ou controle real, no contexto DESP confirmado, preservando as associações entre registros.
