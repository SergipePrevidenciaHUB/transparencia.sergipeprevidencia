# Planejamento e Prestação de Contas — modelos não publicados

Fontes da primeira etapa: **C**: Cartilha PETP 2026, 10.1 (pp. 81–82) e 10.2 (pp. 82–84, somente sua continuação). **S**: seções 10.1 e 10.2 do Serigy Docs, tabela da p. 1 e exemplos correspondentes/atualização da p. 2. **DT**: decisão técnica, sem novo requisito normativo. Foram lidos `AGENTS.md` e o modelo não publicado de PCA apenas como referência visual. Esse recorte inicial trata de 10.1–10.2; o complemento de 10.3–10.4 está abaixo. Não há alimentação institucional ou declaração de atendimento.

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


## Complemento — Julgamento pelo Tribunal de Contas e RGF

Fontes adicionais efetivamente consultadas: `AGENTS.md`; C 10.3 (p. 84) e 10.4 (p. 85); S 10.3 e 10.4 (tabelas da p. 1 e exemplos documentais/atualização da p. 2). Mantém-se **C** como requisito, **S** como propriedade/tipo documentado e **DT** como decisão técnica. Os HTMLs de 10.1–10.2 não foram alterados.

| Critério C / seção S | Novo modelo não publicado | Rota prevista |
| --- | --- | --- |
| 10.3 / Julgamento pelo Tribunal de Contas | `modelos/Portal-da-Transparencia/PlanejamentoPrestacaoContas/TCE/index.html` | `/Portal-da-Transparencia/PlanejamentoPrestacaoContas/TCE/` |
| 10.4 / Relatório de Gestão Fiscal | `modelos/Portal-da-Transparencia/PlanejamentoPrestacaoContas/RGF/index.html` | `/Portal-da-Transparencia/PlanejamentoPrestacaoContas/RGF/` |

Caminhos literais de S, sem criar subrotas de nomes deduzidos. Os modelos ficam fora de `dist`, sem links novos na navegação pública. Reutilizam visual, cabeçalho, rodapé e acessibilidade existentes. O `main` usa somente o contexto `planejamento-prestacao-contas.html`, respaldado pelo cabeçalho e exemplos documentais S; permanece a dúvida já registrada sobre `gestao-fiscal-planejamento.html` no exemplo de atualização. Confirmar o schema antes de ativar itens e controles. Nenhum item de dados, atualização, ausência ou carregamento foi aplicado a conteúdo vazio.

### TCE — C 10.3 / S 10.3

C exige a íntegra da decisão de apreciação/julgamento, não apenas a conclusão de Acórdão/Parecer, e indicação das contas cuja apreciação permanece pendente. Admite link direto ao documento/informação no próprio Tribunal. **DT:** índice por exercício das contas, com situação e acesso documental associado; não é transcrição do processo nem tabela de resultados financeiros.

| Coluna / reserva de `#tabela-tce` | Origem | Marcação S futura |
| --- | --- | --- |
| Exercício das contas | DT para associar documento, histórico e contas pendentes exigidos por C | Sem item específico; não confundir com ano da decisão/upload |
| Situação da apreciação ou julgamento | C: indicar contas pendentes; apresentação na linha é DT | Sem item específico; não inventar `situacaoJulgamento` |
| Documento integral do Tribunal | C: íntegra, com acesso direto | 10.3.1 `integraJulgamentoTCE` (Anexo), apenas no acesso/conteúdo real |

**Atualidade C:** disponibilizar o último Acórdão/Parecer relativo às contas, observadas as especificidades da Corte. C p. 84 admite a última manifestação opinativa quando o último julgamento não compreende o exercício atual ou os três anos da série descrita. Confirmar a manifestação e sua relação com as contas; não criar decisão para ano ainda pendente, não deduzir pendência por falta de arquivo e não atribuir prazo de julgamento inexistente na fonte. A referência não é um máximo de 30 dias ou o último exercício exigível dos balanços.

**Histórico C:** preservar a formulação dos três exercícios encerrados imediatamente anteriores ao último encerrado e a explicação de referência X com X-1/X-2/X-3. Manter X e os três precedentes pertinentes, sem cortar o acervo para três arquivos totais; conferir contas pendentes e a ressalva da última manifestação com a fonte institucional. A última decisão não é necessariamente do mesmo ano das contas.

**Controles S:** 10.3.3 `historicoExercicio` (N/A), futura marcação de `#exercicio-tce` com opções reais e `serigyValue`. O seletor é navegação histórica DT, em `#historico-tce`, sem formulário/botão de busca. **C 10.3 não lista filtro de pesquisa nem gravação; S 10.3 não contém `filtroPesquisa`/`salvarRelatorio`.** Por isso não se copiam os controles completos das outras páginas. Implementar a seleção histórica só sobre o acervo real, sem opções de exercícios inventadas.

10.3.2 `dataUltimaAtualizacao` (Data) está reservado em `#atualizacao-tce`, hoje vazio e sem marcação. Receber data real e cobertura do conjunto; não usar a data da geração nem uma situação genérica como valor de data. Não marcar ausência de documento de conta pendente como se houvesse íntegra disponível.

### RGF — C 10.4 / S 10.4

**Periodicidade expressamente conferida:** C p. 85 exige o RGF do **último quadrimestre exigível**, com publicação em até **30 dias após o encerramento do quadrimestre**. A fonte consultada não define estrutura trimestral, mensal ou semestral para este modelo. Não converter periodicidade ou criar exceção por analogia. O seletor é de quadrimestre, sem opções reais antes da alimentação.

**Demonstrativos expressamente conferidos:** C exige o **RGF com todos os anexos obrigatórios**, e S 10.4.1 também descreve o conjunto com anexos. **Esses trechos não enumeram nomes, números ou quantidade dos demonstrativos aplicáveis a cada emissor.** Não foram criados cabeçalhos fixos de anexos financeiros por conhecimento externo nem presumido um pacote universal. Confirmar com a contabilidade o emissor/regime, a composição aplicável e o conjunto completo. Uma coluna de abrangência identifica os anexos reais, sem afirmar previamente sua presença ou criar novo requisito.

**Aplicabilidade — DÚVIDA — REVISÃO NECESSÁRIA:** o quadro C inclui Previdência Estadual, mas o parágrafo da p. 85 ressalva os emissores dos arts. 54/20 da LRF. Para unidade que não emite RGF próprio, admite situação fundamentada de não aplicação ou link direto ao RGF do Poder/órgão no qual esteja consolidada. Confirmar a condição jurídica/contábil da Unidade e a cobertura do consolidado; não presumir dispensa, relatório próprio ou entidade emissora. O modelo é neutro, sem declaração de inexistência/não aplicação.

| Coluna de `#tabela-rgf` | Origem / conteúdo | Marcação S futura |
| --- | --- | --- |
| Exercício | DT: identificação do período de referência exigido por C | Sem item específico |
| Quadrimestre | C: período exigível; identificação no índice é DT | Sem item específico |
| Emissor e abrangência | DT: contextualizar o RGF próprio/consolidado e sua cobertura confirmada | Sem item específico |
| RGF e documentos integrantes | C: relatório integral e anexos obrigatórios aplicáveis | 10.4.1 `RGF` (Anexo), **grafia maiúscula**, somente em documentos reais |
| Demonstrativos e anexos abrangidos | DT: identificação da composição real para conferir completude | Sem item específico; não inventar propriedades por demonstrativo |

Um documento integral pode reunir os anexos; se houver vários arquivos, associar todos ao mesmo exercício/quadrimestre e emissor sem duplicar o relatório nem supor que um link parcial cobre o conjunto. Não confundir RGF com balanço, RREO, balancete ou mera tabela do índice. Não impor formato editável ou pesquisabilidade específicos como novos requisitos desta página sem respaldo adicional nas fontes consultadas.

| Controle / requisito | Reserva / escolha DT | S futuro |
| --- | --- | --- |
| C: filtro específico genérico, sem parâmetros mínimos enumerados | `#filtro-rgf`, `#exercicio-rgf`, `#quadrimestre-rgf`; escolha DT para organizar os períodos | 10.4.2 `filtroPesquisa` (N/A), após implementação e esclarecimento do schema |
| C: pelo menos os três anos anteriores ao da consulta | `#exercicio-rgf`, com períodos efetivamente disponíveis | 10.4.4 `historicoExercicio` (N/A), opções reais com `serigyValue`; não usar automaticamente a série especial X dos julgamentos/balanços |
| C: último quadrimestre exigível, prazo de até 30 dias após seu encerramento | `#atualizacao-rgf`, sem conteúdo/data atribuída | 10.4.3 `dataUltimaAtualizacao` (Data), só após obter referência real e cobertura |

C 10.4 não lista gravação de relatórios e S 10.4 não documenta `salvarRelatorio`: não há botão de exportação autônoma. Download/acesso dos documentos é parte do conteúdo. Na consulta futura, `#pesquisar-rgf` poderá corresponder a `#resultados-rgf`, com `serigyExecuteWaitSection` e `serigyLoadSection` coincidentes, após implementação; IDs são DT. Hoje formulário e controles estão desativados, sem marcações funcionais.

### Alimentação dos dois novos modelos

Receber informações e documentos institucionais, conferir referência das contas ou períodos fiscais, validar acervo, correspondência e acesso público. URLs do TCE ou do emissor/consolidado só entram após conferência direta; não gerar URL por exercício, copiar links de exemplos ou usar `serigyLink` para PDF. Não declarar pendência, inexistência, não aplicação ou cobertura de anexos por dedução de tabelas vazias.

As reservas de atualização continuam vazias até haver conteúdo real. Antes de mover para `dist`, resolver as dúvidas no controle, alimentar e marcar somente conteúdo existente, implementar a navegação histórica de 10.3 e a consulta de 10.4 e testar recortes, documentos, extração e acessibilidade. A simples existência do modelo não atesta atendimento; os modelos anteriores, menus e deploy permanecem inalterados.


## Complemento — Plano Estratégico e Balancetes Mensais

Fontes efetivamente consultadas: AGENTS.md; Cartilha PETP 2026 **10.5, p. 86**, e **10.6, p. 87**; Serigy Docs, dimensão 10, seções **10.5 e 10.6**, tabelas da p. 1 e exemplos correspondentes da p. 2. **C** = exigência da Cartilha; **S** = marcação técnica; **DT** = organização proposta. Os quatro modelos anteriores não foram alterados.

| C / S | Modelo não publicado | Rota literal prevista |
| --- | --- | --- |
| 10.5 / 10.5 | `modelos/Portal-da-Transparencia/PlanejamentoPrestacaoContas/PlanoEstrategico/index.html` | `/Portal-da-Transparencia/PlanejamentoPrestacaoContas/PlanoEstrategico/` |
| 10.6 / 10.6 | `modelos/Portal-da-Transparencia/PlanejamentoPrestacaoContas/Balancetes/index.html` | `/Portal-da-Transparencia/PlanejamentoPrestacaoContas/Balancetes/` |

Os modelos estão fora de `dist`, sem inclusão em menu público. Reutilizam a estrutura visual e os componentes gerais existentes. O `main` mantém somente o schema de cabeçalho/documentos `planejamento-prestacao-contas.html`. Não há marcações de dados, datas, formatos, ausência ou carregamento sobre conteúdo vazio. Permanece a divergência S entre esse schema e `gestao-fiscal-planejamento.html` nos exemplos de filtro/atualização; esclarecer antes de ativar os itens.

### Plano Estratégico — 10.5

**C:** aplicável às Previdências Municipais e Estadual; somente Disponibilidade. O plano deve conter objetivos estratégicos, indicadores e respectivas metas; não se confunde com PPA. **S 10.5.1:** `planoEstrategico` (Anexo), no acesso real ao plano integral. **DT:** apresentação documental em `#conteudo-plano-estrategico`, dentro da seção `#documento-plano-estrategico`, sem transcrever indicadores ou criar tabela financeira.

Nem C 10.5 nem S 10.5 prescrevem filtro, série histórica, gravação de relatórios ou `dataUltimaAtualizacao`. Portanto, não há seletores, exportação ou reserva de data obrigatória neste modelo. A Cartilha menciona atualização conforme necessário, sem periodicidade numérica ou horizonte fixo. A vigência e a identificação da versão devem vir do plano real; não copiar as datas do exemplo S, nem impor formato editável ou PDF pesquisável como exigência autônoma deste critério. Obter o plano integral e conferir os três conteúdos mínimos antes da alimentação; não produzir um plano a partir do PPA ou do relatório de gestão.

### Balancetes — 10.6: aplicabilidade confirmada

**Conclusão expressa:** C p. 87 inclui nominalmente **Previdências Municipais e Estadual** no quadro de aplicabilidade de 10.6. Assim, o critério está no escopo da Previdência Estadual. A observação S p. 1 de aplicação apenas à **Matriz II** não afasta essa exigência C; sua correspondência técnica permanece **DÚVIDA — REVISÃO NECESSÁRIA**, sem presumir dispensa ou excluir a página. S 10.6.4–10.6.5 menciona “critérios dos contratos” nas descrições; registrar provável inconsistência editorial, sem transportar conteúdo/prazos de Contratos para Balancetes e sem alterar os nomes documentados dos itens.

**C — conteúdo:** balancetes mensais da Unidade em seção própria, identificados por mês e exercício, abrangendo no mínimo execução orçamentária e financeira do mês, receitas e despesas. O índice não substitui os demonstrativos. Se PDF, deve ser pesquisável. Documento oficial assinado deve ser preservado, acompanhado de editável sem assinaturas. **Gravação:** salvar o conjunto selecionado em pelo menos um formato editável; txt/csv/ods/json são exemplos, não obrigação de oferecer todos. O exemplo S em PDF não elimina o editável C. Não publicar planilhas privadas por cópia bruta.

| Reserva / conteúdo | Origem | S futuro |
| --- | --- | --- |
| Exercício e mês em `#tabela-balancetes` | C: identificação por período; índice tabular é DT | Sem item específico de célula; não inventar propriedades |
| Balancete oficial | C: conteúdo mensal integral, PDF pesquisável se utilizado | 10.6.1 `balanceteMensal` (Anexo), apenas em acesso/conteúdo real |
| Versão editável associada | C: editável junto da versão oficial assinada; coluna é DT | Sem propriedade nova; controlar correspondência por período e conteúdo |
| `#filtro-balancetes`, `#exercicio-balancetes`, `#mes-balancetes` | C: localização por exercício e mês | 10.6.2 `filtroPesquisa` (N/A), quando funcional |
| `#exportacao-balancetes` | C: gravação do conjunto selecionado em pelo menos um editável | 10.6.3 `salvarRelatorio` (N/A), com `serigyValue` do formato realmente oferecido |
| `#atualizacao-balancetes` | C: indicar publicação ou última atualização real | 10.6.4 `dataUltimaAtualizacao` (Data), somente após alimentação |
| Seletor de exercício e opções reais | C: pelo menos os três anos anteriores à consulta, por mês/exercício | 10.6.5 `historicoExercicio` (N/A), opções reais com `serigyValue` |

**Atualidade:** último mês exigível disponível. C **recomenda** publicação em até 30 dias após encerramento do mês; não converter a recomendação em prazo absoluto. Confirmar o mês exigível com a contabilidade. Data da geração/importação não comprova atualidade. **Histórico:** três anos anteriores à consulta, sem reduzir ao total de três arquivos ou aplicar a série especial X de 10.1–10.3.

**Consulta:** C admite também organização única facilmente localizável por Ctrl+F; o modelo prepara seletores por exercício e mês, sem declarar essa alternativa proibida. Seletores/botões estão desativados, sem opções de períodos fabricados. A associação futura `#pesquisar-balancetes` → `#resultados-balancetes` poderá usar `serigyExecuteWaitSection`/`serigyLoadSection` coincidentes após implementação; IDs são DT. Não há exportação funcional ou formato escolhido antes de receber o conjunto editável real. Conferir o recorte salvo e sua equivalência aos documentos; se vários arquivos compõem um período, manter a associação e a cobertura, sem duplicar conteúdo.

### Antes da publicação de 10.5–10.6

Receber os documentos e metadados institucionais; conferir integridade, vigência/referência, cobertura e acesso público; resolver as dúvidas S; preencher apenas conteúdo real e aplicar os itens confirmados. Em Balancetes, implementar e testar pesquisa, histórico, exportação editável e atualização real. URLs oficiais só após conferência individual; não criar caminhos por ano/mês nem usar `serigyLink` para PDF. Só mover para `dist` e ajustar navegação em tarefa autorizada, após validação. Nenhum dos modelos vazios comprova atendimento.
