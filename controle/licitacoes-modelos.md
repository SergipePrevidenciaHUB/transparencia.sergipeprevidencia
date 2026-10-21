# Licitações — modelos não publicados

Fontes da primeira etapa: **C**: Cartilha PETP 2026, critérios 8.1–8.5, pp. 64–71 (sem o trecho de 8.6). **S**: somente seção 8.1 Licitações do Serigy Docs, tabela da p. 1. Foram lidos `AGENTS.md` e somente as fichas correspondentes do inventário. **DT** identifica escolhas técnicas, sem novos mínimos normativos. O modelo recente de Diárias fornece apenas o visual, navegação e componentes comuns; seus campos não foram reutilizados.

## Rota e isolamento

S indica `[Portal da Transparencia]/Licitacoes`. Modelo: `modelos/Portal-da-Transparencia/Licitacoes/index.html`; destino futuro: `dist/Portal-da-Transparencia/Licitacoes/index.html`, rota `/Portal-da-Transparencia/Licitacoes/`. Não há subrota adicional para a listagem principal. A pasta `modelos/` fica fora da origem `dist` publicada pelo preparador existente. Não foram alterados deploy, menu, mapa ou busca públicos. PCA e Sanções são modelos separados, descritos no complemento abaixo; o HTML principal permanece inalterado.

Schema confirmado no `main`: `https://serigy.tce.se.gov.br/comum/licitacoes.html`. Só o contexto está marcado: tabela sem registros, listas documentais vazias, filtros/exportação desativados e reservas de atualização sem `serigyItem`. As marcações dos componentes gerais reais foram preservadas. Sem dados, URLs de documentos, datas, hash ou declarações de não ocorrência inventados.

## Serigy 8.1 ↔ critérios da Cartilha

| Critério C / conteúdo | Itens S 8.1 | Estrutura preparada |
| --- | --- | --- |
| 8.1: relação sequencial, resumo dos procedimentos | 8.1.1–6 | Tabela HTML `#tabela-licitacoes`, com consulta em `#filtro-licitacoes` e resultados em `#resultados-licitacoes` |
| 8.2: editais integrais | 8.1.7 `editalLicitacao` (Anexo) | Grupo `#documentos-editais-licitacoes` dentro do detalhe do procedimento |
| 8.3: demais documentos das fases interna e externa | 8.1.8 `docFasesLicitacao` (Anexo) | Grupo `#documentos-fases-licitacoes` |
| 8.4: documentos de dispensa/inexigibilidade | 8.1.9 `docDispensaLicitacao` (Anexo) | Grupo `#documentos-contratacoes-diretas` |
| 8.5: atas de adesão — SRP | 8.1.10 `atasLicitacao` (Anexo/Link) | Grupo `#documentos-atas-adesao` |
| 8.1–8.5: filtro, atualização, histórico | 8.1.11 `filtroPesquisa`; 8.1.13 `dataUltimaAtualizacao`; 8.1.14 `historicoExercicio` | Reservas descritas abaixo; ativar apenas sobre dados reais |
| Apenas 8.1: gravação do recorte da relação | 8.1.12 `salvarRelatorio` | `#exportar-licitacoes`; não criar gravação autônoma de 8.2–8.5 |

## Listagem e campos

C 8.1 exige tabela estruturada em HTML, com licitações em andamento e encerradas, em ordem numérica sequencial. Devem constar também dispensas e inexigibilidades, com a exceção das compras diretas de pequeno valor descrita na C p. 64. Não extrapolar essa ressalva para toda contratação direta.

| Coluna | Origem | Item S / marcação futura | Tipo literal S |
| --- | --- | --- | --- |
| Sequência | S: sequência da licitação; DT: posição na ordenação real | 8.1.6 `sequencia` | Numérico |
| Número/ano do procedimento | Número exigido por C 8.1; ano como DT para identificação inequívoca | Sem item próprio na tabela S consultada | Não inventar `numeroLicitacao` |
| Modalidade | C 8.1 | 8.1.1 `modalidadeLicitacao` | Texto |
| Objeto | C 8.1 | 8.1.2 `objetoLicitacao` | Texto |
| Data da sessão de abertura | C 8.1 | 8.1.3 `dataLicitacao` | Texto |
| Valor estimado ou homologado | C 8.1 | 8.1.4 `valorLicitacao` | Número |
| Situação | C 8.1 | 8.1.5 `faseLicitacao` | Texto |
| Documentos | DT: acesso ao detalhe do mesmo procedimento | Ação/associação, sem novo item de dados | Não substituir os quatro itens documentais por um item inventado |

O inventário alerta que `sequencia` é exemplificada como ordinal, sem propriedade própria para o número do certame. Preservar o número oficial em coluna própria e não tratar posição de linha como identificação. Data é tipada Texto e valor como Número em S: manter os conteúdos exigidos por C sem inventar tipos/atributos. Confirmar se o valor é estimado ou homologado e identificá-lo na apresentação real; não assumir que ambos são iguais ou que um valor faltante seja zero.

## Filtros, histórico, exportação e atualização

- **C 8.1:** mínimos ano, mês, situação e modalidade (p. 65). Reservas `#ano-licitacoes`, `#mes-licitacoes`, `#situacao-licitacoes`, `#modalidade-licitacoes`; opções somente de dados reais. Confirmar a referência temporal para procedimentos sem sessão de abertura, sem inventar data ou competência.
- **C 8.2–8.5:** filtro específico genérico, sem os quatro parâmetros enumerados como mínimos próprios. DT: reaproveitar a seleção dos procedimentos para localizar seus documentos, mantendo identidade/tipo e acesso ao acervo documental. Não transportar automaticamente os mínimos de 8.1 como novas obrigações documentais.
- **S:** aplicar `filtroPesquisa` ao formulário funcional. `#pesquisar-licitacoes` poderá usar `serigyExecuteWaitSection` com o mesmo valor de `serigyLoadSection` em `#resultados-licitacoes`. A ação de documentos de uma linha real deverá ter referência única ao respectivo detalhe; não anunciar uma ação inexistente no modelo.
- **Histórico C de todos os cinco critérios:** pelo menos os três anos anteriores ao da consulta. S `historicoExercicio` no seletor de exercício, com `serigyValue` em cada opção real. Conferir cobertura da relação **e de cada grupo documental**; histórico de resumos não comprova histórico dos PDFs. Não limitar acervo aos anos de exemplos.
- **Gravação C 8.1:** conjunto selecionado em pelo menos um formato editável. Aplicar `salvarRelatorio` e `serigyValue` do formato realmente implementado em `#exportar-licitacoes`. DT: CSV ou outro editável. Incluir todos os mínimos do resumo; não duplicar linhas/valores por cada documento vinculado. Não prometer exportação dos inteiros teores como se CSV substituísse os documentos de 8.2–8.5.
- **Atualidade C 8.1–8.5:** dados mais recentes de até 30 dias da consulta. Reservas separadas: `#atualizacao-licitacoes`, `#atualizacao-editais-licitacoes`, `#atualizacao-fases-licitacoes`, `#atualizacao-contratacoes-diretas`, `#atualizacao-atas-adesao`. Receber data/cobertura reais e só então aplicar `dataUltimaAtualizacao` no contexto correto. Não usar geração do HTML ou atualização do resumo para simular atualização de documentos.

## Documentos: íntegra e associação ao procedimento

DT: `#detalhes-procedimento` é a reserva de detalhe; `#identificacao-procedimento` receberá identificação real. Ao alimentar, associar cada grupo e documento à chave real do procedimento selecionado, com IDs únicos por registro se houver vários detalhes no HTML. A área vazia atual não representa certame. Não usar uma lista global de PDFs sem vínculo com a linha, nem criar botão/link vazio na tabela.

| Critério | Documentos necessários conforme C | Condições e distinções |
| --- | --- | --- |
| 8.2, pp. 66–67 | Editais integrais dos certames em andamento e encerrados, com anexos integrantes | Resumo do objeto ou ementa não substitui edital. |
| 8.3, pp. 67–68 | TR/projeto básico/equivalente; justificativa; pareceres técnicos/jurídicos; orçamento/formação do preço de referência; edital/anexos; atas de abertura/julgamento e outras ocorridas; impugnações/recursos e resultados de análise quando houver; adjudicação e homologação | Justificativa pode estar em outro documento, como o TR. Reutilizar o mesmo edital em 8.2/8.3, sem duplicar arquivo. Não criar recurso ou ata quando não existente. |
| 8.4, pp. 69–70 | TR/projeto básico/equivalente; justificativa de fornecedor/preço; caracterização de emergência/calamidade/grave risco quando for o caso; pareceres quando couber; homologação/ratificação da autoridade | Observar a ressalva específica de dispensas de pequeno valor e o regime aplicável descritos em C p. 69, sem excluir toda dispensa/inexigibilidade. Links externos diretos são admitidos. |
| 8.5, p. 71 | Atas integrais de adesão de registro de preços | Não confundir ata geral de registro de preços com comprovação da adesão da Unidade. C admite acesso em licitações e/ou contratos; neste recorte fica em Licitações, quando aplicável. |

Os itens S de documento serão aplicados somente a contêineres/links com conteúdo real e correspondente, sob o schema, preservando o vínculo ao procedimento. URLs absolutas do sítio oficial podem ser usadas após conferência individual. Não criar URLs por número/ano, não usar `href="#"` ou `serigyLink` para PDF, nem apontar somente para a capa do PNCP/outro portal.

C 8.3 exige pesquisa/seleção de texto; C 8.4 exige pesquisa/seleção de texto ou valor nos documentos. As ressalvas do filtro de documentos de terceiros (C pp. 68/70) não eliminam as exigências de conteúdo nem autorizam arquivos ilegíveis. Não impor automaticamente a todos os documentos a exceção de filtros ou um formato editável autônomo não previsto em 8.2–8.5.

## Antes de publicar o modelo principal (8.1–8.5)

Receber o catálogo oficial e documentos, esclarecer as dúvidas em `controle/licitacoes-pendencias.md`, conferir vínculos e acesso, cobertura histórica e datas. Alimentar linhas e documentos reais, implementar filtros, associação de detalhes e exportação apenas da relação, aplicar marcações e testar recortes/extração/acessibilidade. Eventual não ocorrência exige confirmação e referência institucional; falta de arquivos não comprova que não houve licitações, dispensas, recursos ou adesões. O modelo não contém declaração de não ocorrência nem atesta atendimento. Somente depois mover para `dist` em tarefa autorizada e ajustar navegação pública.


## Complemento — PCA e Sanções

Fontes deste complemento: `AGENTS.md`; C 8.6, pp. 71–72, e C 8.7, pp. 73–74; S, seções 8.2 e 8.3, tabelas da p. 1 e exemplo de Sanções/atualização da p. 3. Mantém-se a distinção **C** / **S** / **DT**. Não houve leitura/trabalho nos modelos de Diárias nesta rodada. O modelo principal foi usado somente como referência dos componentes visuais e não foi modificado.

| Seção S ↔ critério C | Novo modelo versionável | Rota futura |
| --- | --- | --- |
| S 8.2 Plano de Contratações Anual ↔ C 8.6 | `modelos/Portal-da-Transparencia/Licitacoes/PlanoAnualContratacoes/index.html` | `/Portal-da-Transparencia/Licitacoes/PlanoAnualContratacoes/` |
| S 8.3 Sanções ↔ C 8.7 | `modelos/Portal-da-Transparencia/Licitacoes/Sancoes/index.html` | `/Portal-da-Transparencia/Licitacoes/Sancoes/` |

São os caminhos literais de S após o prefixo do Portal. Ambos estão fora de `dist`, sem links novos na navegação pública. Reutilizam visual, cabeçalho, rodapé e acessibilidade do modelo principal. O schema `https://serigy.tce.se.gov.br/comum/licitacoes.html` está no `main`; as propriedades abaixo são reservadas para aplicação somente com conteúdo real. Não foram marcadas listas/células vazias, datas desconhecidas ou controles desativados como dados disponíveis.

### PCA — C 8.6 / S 8.2

**C:** possibilidade de consultar o PCA do exercício atual na seção de licitações e/ou contratos; disponibilidade e atualidade são os únicos itens enumerados. O modelo oferece um índice documental na seção específica, sem transcrever demandas ou criar tabela de itens sem fonte.

| Conteúdo / origem | Reserva | Marcação S futura |
| --- | --- | --- |
| Plano oficial e documentos que efetivamente o integrem — C 8.6; apresentação em lista é DT | `#documentos-pca` | 8.2.1 `contratacoesAnual` (Anexo/Link), no documento/link real sob o schema |
| Exercício ao qual o plano se refere — contexto do requisito C de exercício atual; exibição é DT | `#exercicio-pca` | Sem item específico documentado; não inventar propriedade para exercício |
| Data real de atualização — S; atualidade C aferida pelo PCA do exercício atual | `#atualizacao-pca` | 8.2.2 `dataUltimaAtualizacao` (Data), somente após preencher a referência real |

Não há filtro, série histórica ou gravação de relatórios próprios em C 8.6 nem propriedades correspondentes em S 8.2. Por isso o modelo não tem seletor, formulário de consulta, botão de exportação ou marcações de carregamento fictícias. A data de upload/geração não demonstra que o plano corresponde ao exercício exigido.

**Ressalva expressa C p. 72:** declaração de não elaboração ou inexistência do PCA não é suficiente para atendimento. Não aplicar uma declaração genérica de não ocorrência para marcar 8.6 como atendido. O modelo não contém tal declaração. Não criar plano ou linhas de contratações a partir de exemplos S, licitações já realizadas ou dados não fornecidos.

A URL/arquivo deve levar ao plano pertinente e completo, não à capa genérica de outro portal. Eventuais anexos/versões só entram se fornecidos e confirmados como integrantes do plano; não são categorias documentais novas impostas como mínimos. Não usar `serigyLink` para PDF nem gerar URL por suposição.

### Sanções — C 8.7 / S 8.3

C p. 73 exige nomes dos licitantes/contratados sancionados **pela Unidade**, nas hipóteses dos incisos III e IV do art. 156 indicadas no critério. Não importar indiscriminadamente sanções aplicadas por outras unidades. A menção ao CEIS na dica C não torna uma consulta nacional genérica equivalente à relação contextualizada da Unidade.

**DT:** relação em tabela HTML, como no exemplo S, sem novos campos obrigatórios de dosimetria, prazo de sanção, fundamento ou número de processo. Não há obrigação autônoma de anexar o inteiro teor do ato sancionatório neste critério; os atos de origem podem apoiar a conferência interna, sem exigir um documento público fictício.

| Coluna de `#tabela-sancoes` | Origem | Item S / marcação futura | Tipo S |
| --- | --- | --- | --- |
| Nome do licitante ou contratado | Mínimo nominal C 8.7 | 8.3.1 `nomeSancionado` | Texto |
| CNPJ/CPF | Identificação técnica adicional de S; não enumerada no mínimo C | 8.3.2 `idSancionado` | Texto |

**DÚVIDA — REVISÃO NECESSÁRIA:** receber identificação confiável e confirmar a versão publicável de CPF/CNPJ com a instituição. Não inventar documento, inferir CPF por nome, copiar exemplos S ou presumir forma de mascaramento sem fonte. Manter identificação como texto, preservando zeros/pontuação significativos. O modelo só tem os cabeçalhos, sem nomes ou identificadores.

| Controle / exigência C p. 74 | Reserva | S / ativação futura |
| --- | --- | --- |
| Filtro específico genérico, sem parâmetros mínimos enumerados | `#filtro-sancoes`, `#nome-sancoes`, `#ano-sancoes` | 8.3.3 `filtroPesquisa`. **DT:** nome e exercício para facilitar localização/histórico; não são novos mínimos C nem exigem conhecimento prévio de CPF. |
| Histórico de pelo menos três anos anteriores ao da consulta | `#ano-sancoes` | 8.3.6 `historicoExercicio`, opções reais com `serigyValue`; não limitar ao exemplo S ou criar exercícios sem fonte. |
| Gravação do conjunto selecionado em ao menos um editável **ou PDF pesquisável**, alternativa expressa C | `#exportar-sancoes` | 8.3.4 `salvarRelatorio`, com `serigyValue` do formato efetivamente fornecido; não exigir todas as extensões. |
| Atualidade: dados mais recentes de até 30 dias da consulta | `#atualizacao-sancoes` | 8.3.5 `dataUltimaAtualizacao` (Data), somente com referência real, distinta da geração/importação da página |

Após implementar, associar `#pesquisar-sancoes` a `#resultados-sancoes` com `serigyExecuteWaitSection` na ação e `serigyLoadSection` no resultado, de mesmo valor. Os IDs são DT. Aplicar `nomeSancionado`/`idSancionado` às células reais da mesma linha. Atualmente controles estão desativados e o `tbody` está vazio, sem linha de exemplo, `serigyEmpty` ou promessa funcional.

Confirmar a referência temporal das sanções para os exercícios e alterações/revisões da relação, sem confundir ano de importação, situação atual e histórico. A exportação deverá corresponder ao recorte e preservar somente os campos publicáveis confirmados; arquivo estático não pode anunciar filtros que não acompanha. Não declarar inexistência de sanções a partir de ausência de arquivo. Eventual informação de não ocorrência depende de confirmação institucional do período.

### Liberação dos dois novos modelos

As pendências estão no controle próprio de Licitações. Receber PCA oficial do exercício exigido e referências reais; receber relação de sancionados, identificação publicável, recorte histórico e atualização; implementar somente os controles aplicáveis; então alimentar e marcar conteúdo real, conferir documentos/links, extração e acessibilidade. Só depois mover cada página completa para `dist` em tarefa autorizada e ajustar navegação pública. Os modelos vazios não demonstram atendimento ao PETP.
