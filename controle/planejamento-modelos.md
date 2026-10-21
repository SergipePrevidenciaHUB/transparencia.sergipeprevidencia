# Planejamento e Prestação de Contas — modelos 10.1 e 10.2

**C**: Cartilha PETP 2026, 10.1 (pp. 81–82) e 10.2 (pp. 82–84, somente sua continuação). **S**: seções 10.1 e 10.2 do Serigy Docs, tabela da p. 1 e exemplos correspondentes/atualização da p. 2. **DT**: decisão técnica, sem novo requisito normativo. Foram lidos `AGENTS.md` e o modelo não publicado de PCA apenas como referência visual. Escopo exclusivo destes dois modelos; não há alimentação institucional ou declaração de atendimento.

## Rotas, isolamento e marcações

| Critério C / seção S | Modelo não publicado | Rota prevista |
| --- | --- | --- |
| 10.1 / Prestação de Contas (Balanço Geral) | `modelos/Portal-da-Transparencia/PlanejamentoPrestacaoContas/BalancoGeral/index.html` | `/Portal-da-Transparencia/PlanejamentoPrestacaoContas/BalancoGeral/` |
| 10.2 / Relatório de Gestão ou Atividades | `modelos/Portal-da-Transparencia/PlanejamentoPrestacaoContas/RelatorioGestao/index.html` | `/Portal-da-Transparencia/PlanejamentoPrestacaoContas/RelatorioGestao/` |

São os caminhos literais de S após o prefixo do Portal. `modelos/` está fora de `dist`, origem publicada pelo preparador existente. Nenhuma mudança em navegação pública, deploy, Receitas, Contratos ou outras seções. Cabeçalho, rodapé, acessibilidade e componentes visuais existentes foram reutilizados.

O `main` usa apenas o contexto `serigySchema="https://serigy.tce.se.gov.br/comum/planejamento-prestacao-contas.html"`, conforme o cabeçalho de S e seus exemplos documentais. Não há `serigyItem`, `serigyValue`, `serigyEmpty` ou marcações de carregamento em dados/controles vazios. As marcações dos componentes gerais reais foram preservadas. Os seletores e botões de pesquisa/limpeza estão desativados; `tbody` vazio, sem registros ou URLs documentais.

**DÚVIDA — REVISÃO NECESSÁRIA:** S p. 1 e os exemplos documentais usam `planejamento-prestacao-contas.html`, enquanto o exemplo de atualização na p. 2 usa `gestao-fiscal-planejamento.html`. O contexto do modelo segue a identificação do cabeçalho, mas não resolve nem presume equivalência entre os schemas. Confirmar a representação antes de ativar marcações de documentos, filtros, histórico e atualização. Não repetir o alias divergente automaticamente na reserva de data nem criar novos atributos para contornar a dúvida.

## Estrutura documental por exercício

**DT:** tabela de índice documental, sem transcrição de balanços ou decomposição de relatórios. O campo Exercício identifica o período a que o conteúdo se refere, não o ano de upload. A identificação do documento e o conteúdo abrangido só serão preenchidos após conferência da fonte. Não há propriedades S específicas para criar itens de exercício/título/demonstrativo.

| Página / reserva | Conteúdo exigido C | Marcação S futura / tipo |
| --- | --- | --- |
| Balanço: documentos em `#tabela-balanco-geral` | Balanço Geral da Unidade, no mínimo Balanço Orçamentário, Balanço Financeiro, Balanço Patrimonial e Demonstrações das Variações Patrimoniais | 10.1.1 `balancoGeralAnoAnterior` — Link, no acesso real ao documento/conjunto correspondente |
| Balanço: coluna Demonstrativos abrangidos | DT de localização e conferência da cobertura mínima C; não é novo demonstrativo obrigatório | Sem item específico; manter texto legível com os conteúdos reais |
| Relatório: documentos em `#tabela-relatorio-gestao` | Relatório de gestão/atividades relativo ao exercício anterior, elaborado pelo chefe da Unidade, com principais resultados finalísticos e/ou de gestão | 10.2.1 `relatorioGestao` — Anexo, no conteúdo documental real associado ao exercício |

Em 10.1, um PDF integral pode conter os quatro demonstrativos; não exigir quatro arquivos separados nem duplicar o arquivo artificialmente. Se houver vários documentos, manter a associação ao mesmo exercício e identificar os conteúdos efetivos. A coluna de abrangência não pode marcar automaticamente os quatro como presentes sem conferência.

Em 10.2, os temas que C pp. 82–83 diz serem abordados em geral orientam a leitura, não impõem novas colunas de indicadores/metas, orçamento, governança ou resultados numéricos no índice. Não substituir o relatório por um resumo inventado, planilha financeira ou documento de outra finalidade.

**Formatos C:** para 10.1, se publicado em PDF, deve ser pesquisável (p. 81). Para 10.2, o documento deve ser pesquisável, inclusive quando não editável, como PDF (p. 82). Não basta aparência legível sem possibilidade de pesquisa. **Não há gravação de relatórios autônoma** nos itens C desses critérios nem `salvarRelatorio` nas tabelas S 10.1/10.2; os modelos não têm botão de exportação, CSV fictício ou promessa de versão editável. O acesso/download do próprio documento é distinto dessa gravação.

## Filtros, histórico e atualização

| Requisito | Balanço Geral — 10.1 | Relatório de Gestão — 10.2 |
| --- | --- | --- |
| Filtro C | Específico genérico, sem parâmetros mínimos enumerados (p. 82) | Específico genérico, sem parâmetros mínimos enumerados (p. 84) |
| Escolha DT | `#filtro-balanco-geral`, seletor `#exercicio-balanco-geral` por exercício real | `#filtro-relatorio-gestao`, seletor `#exercicio-relatorio-gestao` por exercício real |
| Item de filtro S | 10.1.2 `filtroPesquisa` (N/A), após confirmação do schema e implementação | 10.2.2 `filtroPesquisa` (N/A), nas mesmas condições |
| Histórico S | 10.1.4 `historicoExercicio` (N/A), seletor e opções reais com `serigyValue` | 10.2.4 `historicoExercicio` (N/A), seletor e opções reais com `serigyValue` |
| Atualidade C | Demonstrativos do **último exercício exigível**. C p. 82 indica prazos variáveis e faz menção geral a abril, sem fixar prazo local uniforme. | Relatório relativo ao **último exercício encerrado** (C p. 83). Não importar prazo de balanços ou máximo de 30 dias de outra dimensão. |
| Reserva de data / S | `#atualizacao-balanco-geral`; 10.1.3 `dataUltimaAtualizacao` (Data) | `#atualizacao-relatorio-gestao`; 10.2.3 `dataUltimaAtualizacao` (Data) |

**Série histórica especial C:** em 10.1 (p. 82) e 10.2 (p. 83), C menciona os três exercícios encerrados imediatamente anteriores ao último exercício encerrado e explica que, sendo X o exercício do documento mais atual, a série será X-1, X-2 e X-3. Preservar o documento de referência **X e os três precedentes**, sem reduzir toda a cobertura a três exercícios ou aos três anos anteriores ao ano da consulta. Em 10.1, confirmar com a contabilidade a referência exigível e os prazos locais diante dessas formulações; não presumir que exercício exigível, último encerrado e último arquivo recebido sejam sempre iguais. O resumo de S “últimos 3 anos” não substitui a formulação detalhada C.

Os exercícios dos exemplos S não limitam a cobertura. População de opções e indicação de completude dependem do acervo real; não criar anos sem fonte, declarações genéricas de inexistência ou registros substitutos para lacunas.

As reservas de atualização estão vazias e sem marcação de data. Receber a referência real do conjunto e sua cobertura; só então preencher a informação e, após esclarecer o schema, aplicar `dataUltimaAtualizacao`. A data de geração/importação/upload não comprova, por si, a atualização do conteúdo. Aferir também o exercício do documento conforme C, independentemente da data apresentada.

Reservas de carregamento, apenas para futura consulta funcional: `#pesquisar-balanco-geral` → `#resultados-balanco-geral`; `#pesquisar-relatorio-gestao` → `#resultados-relatorio-gestao`. Usar `serigyExecuteWaitSection` na ação e `serigyLoadSection` no contêiner correspondente, com valor coincidente. IDs são DT, não nomes obrigatórios de S. Não anunciar carregamento inexistente.

## Alimentação e publicação futura

Receber documentos oficiais e metadados reais por exercício, conferir Unidade, integridade, conteúdo e pesquisabilidade, resolver cobertura/prazos e divergência do schema, implementar consulta e aplicar marcações apenas no conteúdo existente. URLs externas oficiais podem ser usadas após conferência individual; não construir caminhos por ano, copiar URLs dos exemplos, usar `href="#"` ou `serigyLink` para PDF. Não publicar fontes privadas por cópia bruta.

Pendências em `controle/planejamento-pendencias.md`. Antes de mover cada modelo para `dist`, concluir essas conferências e testar filtros, documentos, histórico, extração e acessibilidade. Somente depois ajustar navegação pública em tarefa autorizada. Modelos vazios e datas de referência isoladas não comprovam atendimento aos critérios.
