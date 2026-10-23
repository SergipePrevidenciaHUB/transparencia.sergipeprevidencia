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


## Preparação técnica somente de C 4.1 — 22/10/2026

**Escopo:** S4 4.1.1–4.1.3 (totais) e 4.1.15–4.1.18 (controles compartilhados), somente no bloco `#totais`. S4 chama a seção inteira de “4.1 Despesas Comum”, mas os itens 4.1.4–4.1.14 e 4.1.19 correspondem a C 4.2/4.3 e ficaram fora desta implementação. As subseções de classificação e empenhos foram preservadas. Os registros anteriores deste controle descrevem a preparação inicial.

**Implementado:** schema `https://serigy.tce.se.gov.br/comum/despesas.html` na seção de totais; formulário com exercício, mês e UO; botão `serigyExecuteWaitSection="despesasTotaisTabela"` e tabela `serigyLoadSection="despesasTotaisTabela"`; limpeza `serigyClearForm`. Seletor UO é DT conforme layout, não exigência nem item Serigy novo: 37201 SergipePrevidência, 37202 SPSM, 37401 FINANPREV, 37403 FUNPREV e Todas. Todas lista linhas identificadas, sem somar UOs ou períodos. Novo script restrito ao bloco: `dist/assets/js/despesas-totais.js`.

**Estado público sem dados:** controles explicitamente desabilitados, tabela sem linhas e oculta, mensagem factual de indisponibilidade; nenhum valor, exercício de acervo, total zerado, data ou arquivo fictício. Não há `valorEmpenhado`, `valorLiquidado`, `valorPago` ou `dataUltimaAtualizacao` em campos vazios, nem `serigyEmpty`. Reservado `#despesas-totais-atualizacao`, oculto e sem marca, para referência real sob o schema. `filtroPesquisa`, `historicoExercicio` e `salvarRelatorio` não marcam controles inativos. Esses itens serão associados pelo componente apenas quando os registros reais estiverem no HTML e os controles forem funcionais; não considerar a preparação como atendimento ao Invoker.

**Contrato técnico de apresentação (DT, não novo layout de entrada):** futuras linhas HTML já conciliadas terão seis células (UO, exercício, mês e três totais) e atributos `data-exercicio`, `data-mes` (1–12), `data-codigo-uo`, `data-uo-confirmada="true"`. Os três totais reais deverão vir marcados como valorEmpenhado/valorLiquidado/valorPago, em texto monetário com duas casas. O componente não calcula nem agrega: filtra e exporta as mesmas linhas, preservadas no HTML. Se faltar código confirmado, período ou valor esperado em qualquer linha, a consulta permanece indisponível; não descarta silenciosamente o registro nem atribui UO. Anos/opções serigyValue derivam somente das linhas presentes. A ativação não deve exigir interação prévia para disponibilizar dados ao robô. CSV do recorte usa UTF-8 BOM, separador ponto e vírgula e as mesmas seis colunas, sem total adicional. Não foi criado CSV estático vazio.

**Dependências de dados não resolvidas:** a apresentação por UO/período pressupõe totais previamente conciliados; não converte movimentos/saldos em totais e não homologa essa granularidade para a fonte contábil. Receber fonte, cobertura e valores reais antes de alimentar; confirmar movimentos versus saldos, anulações, estornos, reentregas, referência de período e prevenção de dupla contagem conforme layout. Receber data real de atualização/cobertura, por UO quando pertinente. Não usar o dia da geração nem uma data editorial presumida. Validar histórico mínimo com o acervo real. Exportação e controles preparados somente para C 4.1 não resolvem os campos ou exportações de C 4.2/4.3.

**Invoker:** permanecem os resultados e mensagens da avaliação anterior. Corrigido o escopo do schema para 4.1 e preparado comportamento; conteúdo e ativação públicos dependem de dados oficiais. Nova medição somente após publicação autorizada e nova execução do Invoker. Testes com valores identificados como fictícios devem ficar exclusivamente em `trabalho/despesas-41-verificacao/`, sem cópia para dist ou deploy.


### Resultado dos testes locais de C 4.1 — 22/10/2026

Três cópias identificadas como testes fictícios em `trabalho/despesas-41-verificacao/`, sem inclusão em dist ou no deploy: sem dados (6 verificações), sete registros de exemplo (20) e conjunto com UO inválida (6). **32 verificações aprovadas no Chrome headless.** Conferidos exercício/mês/UO combinados; quatro UOs em linhas separadas; anos e serigyValue somente das linhas; ação/resultado correspondentes; limpeza; recorte vazio com download bloqueado; permanência das linhas no HTML; CSV com cabeçalho e exatamente duas linhas do recorte de teste, sem soma conjunta ou duplicação, preservando também o negativo fictício. Cópia com UO não confirmada mantém consulta e exportação indisponíveis, sem excluir a linha. Nenhum desses valores foi publicado.

HTTP 200 na rota `/Portal-da-Transparencia/Despesas/`, com e sem barra final, e em 43 links/recursos internos da página. Validador do projeto: 43 páginas verificadas. IDs e marcações conferidos; nenhuma marcação de conteúdo em campos vazios na página pública. Preservados cabeçalho, rodapé, navegação e todo o HTML a partir da subseção `#classificacao`. Snapshot confirmou 752 arquivos fora do escopo inalterados e exatamente sete linhas pertinentes da matriz modificadas. Ausência de dados oficiais, data real de atualização e questões contábeis continuam pendentes; testes locais e inserção do schema não substituem nova avaliação pelo Invoker.


## Preparação técnica somente de C 4.2 — 22/10/2026

**Fontes e escopo:** layout interno e S4 pp. 1–2: itens 4.1.4–4.1.10 correspondem a C 4.2 (unidadeDespesa, funcaoDespesa, subFuncaoDespesa, categoriaDespesa, grupoDespesa, elementoDespesa, fonteRecursosDespesa). A consulta fica em `#classificacao`, com schema Despesas próprio e nove colunas: UO, exercício, mês e os seis demais campos de classificação. Código e descrição deverão permanecer juntos em cada campo real, conforme a fonte, sem deduzir um a partir do outro. O HTML de #totais e #empenhos foi preservado.

**Reutilização:** o script existente `dist/assets/js/despesas-totais.js` passa a inicializar as duas consultas por configuração. Filtro por exercício/mês/UO, histórico, limpeza, validação de prontidão e CSV são a mesma lógica, sem cópia para um segundo script. Em 4.2 há filtro adicional de elemento, com opções derivadas do texto real código/descrição, não de exemplos. Ação `serigyExecuteWaitSection="despesasClassificacaoTabela"` e tabela `serigyLoadSection="despesasClassificacaoTabela"` independentes das de 4.1. Controles públicos continuam desabilitados; tabela vazia oculta e lugar de atualização oculto sem marcação. Nenhum campo vazio ou controle inativo recebe item de dado/consulta/histórico/exportação; nenhuma data criada.

**Hierarquia — DT de apresentação, não obrigação de árvore ou regra contábil nova:** Categoria Econômica → Grupo → Elemento organiza a natureza documentada. Função/Subfunção formam a classificação funcional, exibida nas linhas; Fonte é outra dimensão, não filho do elemento. Os agrupadores visuais isolam UO, exercício/mês, função, subfunção e fonte para não juntar contextos diferentes. São botões sem marca de dado financeiro, com aria-expanded/aria-controls, foco e ativação nativos de teclado. A abertura não realiza somas. As linhas completas de base continuam no HTML; somente sua visibilidade muda. CSV exporta as linhas de base do filtro, mesmo com grupos fechados, sem incluir cabeçalhos de categoria/grupo como novos registros ou repetir subtotais. Não foi implementado valor por classificação ou ligação a empenhos por suposição.

**Alimentação futura:** além dos atributos DT já usados por 4.1 (exercício, mês, código UO e confirmação), cada linha de classificação deverá ter nove células na ordem do cabeçalho e os sete campos reais marcados. Se faltar período, UO confirmada ou conteúdo, o componente mantém consulta indisponível, sem atribuição nem descarte silencioso. Validar código e descrição, relação função/subfunção e natureza, fonte, cardinalidade, correspondência com movimentos/empenhos e referência temporal antes de publicar. Questões sobre saldos, movimentos, valores por classificação, dupla contagem e atualização/cobertura por UO permanecem abertas no layout. O preparo da tabela de classificação não homologa dados contábeis nem conclui C 4.2.

**Matriz e Invoker:** atualizadas somente as sete linhas de C 4.2 (S4 4.1.4–4.1.10); resultados e mensagens anteriores preservados. Não foram reescritas as linhas de C 4.1 nem de C 4.3, ou suas pendências. Testes fictícios exclusivamente em `trabalho/despesas-42-verificacao/`; reconhecimento da estrutura e dos controles com dados oficiais depende de publicação autorizada e nova avaliação do Invoker.


### Validação concluída de C 4.2 — 22/10/2026

A retomada conferiu o estado atual antes de agir e aproveitou a implementação existente. Não houve alteração no HTML nem no JavaScript durante esta validação. Os testes novos ficaram em `trabalho/despesas-42-verificacao/testar.py`, reutilizando o harness anterior de 4.1, sem reescrever o componente.

**Chrome headless: 72 verificações aprovadas**, sendo 40 de 4.2 e 32 de regressão de 4.1. Três cenários locais: sem dados, exemplos fictícios identificados e conjunto com informação inválida. Em 4.2 foram conferidos filtros combináveis de exercício, mês, UO e elemento; opções derivadas das linhas; expansão e recolhimento Categoria → Grupo → Elemento com os filhos corretos; aria-expanded/aria-controls e foco; separação de contextos por UO, período e fonte; limpeza; manutenção das seis linhas de base; recorte sem registros com CSV bloqueado; e indisponibilidade do conjunto quando falta um campo necessário, sem descarte silencioso.

O CSV fictício de classificação contém exatamente cabeçalho e três linhas do recorte em nove colunas, com campos completos, mesmo com grupos fechados. Agrupadores não são exportados como novos registros e não se criam subtotais. Na regressão 4.1, o CSV manteve exatamente duas linhas filtradas e seus valores, inclusive o negativo de teste. Todos os exemplos e exportações ficaram fora de dist e do deploy.

HTTP 200 na rota com/sem barra e em 43 links/recursos internos. Conferidos schema, correspondência entre espera/carregamento, IDs e rótulos; ausência de marcas de dados/atualização em espaços vazios na página pública. A comparação com o estado anterior confirma preservação do bloco 4.1, do bloco de empenhos, cabeçalho, navegação e rodapé. Snapshot da retomada: 752 arquivos fora do escopo inalterados; somente as sete linhas de C 4.2 (S4 4.1.4–4.1.10) diferem do snapshot anterior da matriz. Resultados reais em `trabalho/despesas-42-verificacao/resultado.json`.

Continuam pendentes os dados/classificações oficiais, sua ligação à execução, granularidade e valores contábeis, cobertura e data real de atualização. Os controles públicos continuam explicitamente indisponíveis. Os testes locais não homologam C 4.2 nem alteram os resultados anteriores do Invoker; confirmar somente após publicação autorizada e nova avaliação.


## Modo sintético autorizado para o Pages de teste — 22/10/2026

Esta etapa foi expressamente solicitada para avaliação técnica pública em GitHub Pages, alterando a restrição das rodadas anteriores, que permitiam exemplos somente em trabalho. Não houve commit, push, publicação nem nova execução do Invoker nesta etapa. O último commit consultado é `ec18c7c` (“Publica estrutura completa do portal para teste no Serigy”); SIC e LGPD estão nesse histórico e não figuravam como modificações pendentes. Nenhum arquivo foi restaurado.

**Separação e aviso:** fonte exclusivamente artificial em `dados-entrada/testes-serigy/despesas-sinteticas.json`, com 8 registros de totais e 10 de classificação, exercícios de ensaio 2023–2026, meses 1/2 e quatro identificadores técnicos de UO. Os nomes de unidades, classificações e todos os valores são sintéticos. Os códigos de UO são reutilizados apenas para exercitar os controles do projeto; `data-uo-confirmada` confirma a identidade técnica do código do teste, não a existência de despesa oficial. A fonte não é a futura entrada contábil e não é copiada para dist. Os blocos apresentam exatamente: **DADOS SINTÉTICOS PARA TESTE DO SERIGY — NÃO REPRESENTAM DESPESAS DO SERGIPEPREVIDÊNCIA**. Os CSVs têm identificação SINTETICOS-TESTE-SERIGY no nome e a coluna “Natureza dos dados” com o aviso integral em cada linha; as linhas de agrupamento não são exportadas.

**Marcação e HTML inicial:** dados de 4.1 e 4.2 presentes diretamente no HTML, com schema e itens documentados, controles ativos, histórico com exercícios efetivos do conjunto sintético, espera/carregamento e CSV. `dataUltimaAtualizacao` identifica explicitamente a preparação deste conjunto de teste em 22/10/2026, registrada na fonte; não é data de atualização de despesas oficiais nem fechamento contábil. Nenhum dado de 4.3 foi criado. A árvore Categoria/Grupo/Elemento continua uma decisão de apresentação, sem somas ou interpretação contábil. Conteúdo de 4.3 e demais páginas são preservados.

### Ativar, conferir e remover

- Ativar/regenerar: `.\.venv\Scripts\python.exe tools/preparar_teste_despesas.py --ativar`.
- Conferir sem alterar: `.\.venv\Scripts\python.exe tools/preparar_teste_despesas.py --check`.
- Remover o modo: `.\.venv\Scripts\python.exe tools/preparar_teste_despesas.py --desativar`, seguido de `--check`. Isso repõe somente os dois blocos sem dados, preservando a preparação técnica, 4.3, navegação e demais alterações; não usa git restore/reset e não exclui arquivos.
- A base anterior, sem dados, fica versionada em `dados-entrada/testes-serigy/despesas-base-sem-dados.json`. Ela contém apenas os dois blocos, não outra página pública. Não sobrescrever essa base com dados de teste ou oficiais. Se a página sem modo tiver sido alimentada/alterada fora desse contrato, o gerador recusa sobrescrevê-la; revisar antes de novo ensaio.
- Preparar o Pages de teste: `.\.venv\Scripts\python.exe tools/preparar_deploy.py --base-path /transparencia.sergipeprevidencia --permitir-dados-sinteticos`. Essa opção é exclusiva dessa base e exige ausência de CNAME; o workflow do Pages recebe a permissão explícita, não uma liberação global.
- Preparação oficial: remover o modo, conferir e executar `tools/preparar_deploy.py` sem a permissão de teste. O preparador bloqueia marcadores/aviso de dados sintéticos em HTML/CSV/JSON antes de tocar na saída; rejeita também a permissão em outra base ou com CNAME. Isso protege o fluxo deste preparador, não uma cópia manual que o ignore. Nenhuma publicação oficial deve conter esse conjunto artificial.

**Pendências:** permanecem todas as fontes, referências, valores e conciliações oficiais descritos acima. A avaliação do Invoker poderá medir somente o comportamento técnico com esse ensaio identificado; não prova conteúdo real, completude, atualidade financeira ou atendimento integral. Resultados antigos na matriz continuam preservados até nova avaliação após publicação autorizada. Os testes do pacote Pages e da proteção contra publicação oficial serão registrados após sua execução.


### Resultado do ensaio sintético do pacote Pages

`tools/testar_despesas_sinteticas.py` preparou e serviu uma cópia com base `/transparencia.sergipeprevidencia/`. **30 verificações Chrome aprovadas**, incluindo aviso visível nos dois blocos, filtros, quatro UOs, histórico, hierarquia, limpeza, bloqueio de recorte vazio e CSV com aviso integral em cada linha. O HTML inicial foi conciliado com as 8 linhas de totais e 10 de classificação; os CSVs filtrados contêm exatamente uma e três linhas de base, respectivamente, com o aviso na coluna adicional e no nome do arquivo. Grupos recolhidos não removem registros da exportação. HTTP 200 na rota com/sem barra e em 43 links/recursos internos.

**Proteção de publicação:** cinco recusas aprovadas (padrão/raiz, base oficial, Pages sem permissão explícita, permissão em base errada e CNAME). A recusa ocorre antes de tocar na saída existente. Em cópia, a remoção foi reversível e idêntica ao estado anterior dos dois blocos; o preparador aceitou o pacote sem sintéticos após a remoção. O gerador também recusou sobrescrever um bloco fora do contrato de teste. Os dados/fontes privadas não foram incluídos no artefato. Teste reproduzível: `.\.venv\Scripts\python.exe tools/testar_despesas_sinteticas.py`.

A `.gitignore` ganhou somente duas exceções explícitas para versionar a fonte sintética e sua base sem dados em `dados-entrada/testes-serigy/`. Confirmado por git check-ignore: esses dois JSONs são versionáveis, enquanto o XLSX real de Receitas e as demais fontes internas continuam ignorados. Isso permite ativar/remover o ensaio em outra cópia do projeto sem expor fontes oficiais.

Snapshot confirmou 751 arquivos fora do escopo preservados. A matriz mudou somente nos 14 itens pertinentes a C 4.1/4.2, mantendo os resultados/mensagens anteriores; C 4.3, SIC, LGPD e demais páginas foram preservados. Validador local: 43 páginas verificadas. Os resultados locais não substituem a publicação autorizada e a nova medição pelo Invoker, nem homologam qualquer despesa real.


## Extensão do mesmo ensaio a 4.3 — 22/10/2026

Autorização desta rodada: completar somente a consulta de empenhos com poucos registros inteiramente sintéticos, sem modificar 4.1/4.2. Foram acrescentados **6 empenhos de teste**, exercícios 2023–2026, meses 1/2, com número `TESTE-EMP-…`, credores “CREDOR SINTÉTICO … — NÃO EXISTE”, documentos “CPF/CNPJ FICTÍCIO TESTE-…” (identificadores inválidos, sem pessoas/empresas reais), objetos e procedimentos artificiais. O ensaio não define solução contábil, não concilia esses exemplos independentes com os conjuntos de totais/classificação e não substitui fonte oficial.

**Estrutura:** detalhes na própria linha HTML, sob o schema de Despesas: `credorEmpenho`, `objetoEmpenho`, `modalidadeEmpenho`, `numeroProcedimento` e `valorEmpenhoIndividual`. Não foi inventado atributo para número do empenho ou CPF/CNPJ. O número do procedimento usa número/ano, conforme o exemplo da p. 2 de S4; permanece a dúvida já registrada sobre o tipo Numérico versus alternativas textuais de fundamentação. Não existem processos/documentos externos sintéticos: toda a informação do ensaio está na tabela; nenhum link externo foi fabricado.

**Consulta:** filtros combináveis de exercício, mês, UO, número do empenho, nome e documento do credor; histórico `historicoExercicio` com `serigyValue` dos exercícios existentes; `filtroPesquisa`, botão com `serigyExecuteWaitSection` correspondente ao `serigyLoadSection` da tabela, limpeza e CSV do recorte. As pesquisas textuais usam trecho do valor, sem diferenciar maiúsculas/minúsculas. O CSV contém as dez colunas da tabela e a coluna “Natureza dos dados” com o aviso integral em cada registro; nome de arquivo identifica o ensaio. Nenhuma soma ou deduplicação foi adicionada. `dataUltimaAtualizacao` informa explicitamente a preparação do conjunto sintético em 22/10/2026, não a atualização financeira oficial.

**Ativação/remoção:** continuam os mesmos comandos e o mesmo bloqueio do preparador descritos acima; não há outro modo de deploy. A partir desta extensão, `--ativar`, `--check` e `--desativar` abrangem os **três blocos**. A base sem dados ganhou somente a estrutura vazia de `empenhos`, preservando as duas bases anteriores. Desativar repõe os três blocos técnicos sem dados, sem excluir arquivos ou usar restauração Git. O gerador recusa identificadores de empenhos/credores sem identificação inequívoca de teste. A fonte sintética continua separada da futura origem oficial, fora de dist.

**Validação realizada:** `tools/testar_despesas_sinteticas.py` aprovado com **50 verificações no Chrome**, usando a cópia exata preparada para `/transparencia.sergipeprevidencia/`. HTML inicial conciliado com 8 totais, 10 classificações e 6 empenhos; filtros de 4.3 isolados/combinados, histórico, campos marcados, foco, limpeza, recorte vazio sem download e CSV filtrado conferido campo a campo, com aviso. Mantidas todas as verificações de hierarquia/filtros/CSV de 4.1/4.2. HTTP 200 na página com/sem barra e nos 43 links/recursos internos. As cinco recusas do preparo oficial continuam aprovadas; remoção reversível e preparo sem sintéticos aprovados em cópia. Nenhuma publicação nem avaliação nova do Invoker foi executada. Relatório em `trabalho/despesas-serigy-publicacao/resultado.json`.

**Pendências remanescentes de 4.3:** fonte oficial de empenhos e sua referência temporal, documentos públicos dos credores e tratamento institucional do CPF, vínculos reais aos procedimentos quando aplicáveis, significado do valor individual, chave/UO, conciliação e granularidade com movimentos/saldos, cobertura histórica e atualização reais. O ensaio não resolve essas questões. As cinco linhas próprias de 4.3 na matriz registram correção técnica/teste local e reconhecimento ainda pendente do Invoker; resultados e mensagens da avaliação anterior foram preservados.


## Conferência da atualização — 22/10/2026

Conferência pontual: os três blocos de Despesas já contêm dataUltimaAtualizacao sob https://serigy.tce.se.gov.br/comum/despesas.html com preparação em 22/10/2026 e ressalva explícita de que não é atualização de despesas oficiais. tools/preparar_teste_despesas.py preserva a marcação ao gerar o ensaio. Nenhuma alteração em Despesas nem no bloqueio oficial foi necessária.


## Avaliação 4226 — visibilidade inicial dos sete campos de classificação

Arquivo disponível no projeto: dados-entrada/outros/respostas-avaliacao-4226.csv (sem o sufixo (1)). Confirmados exatamente os sete SERIGYITEM_NOT_VISIBLE de S4 4.1.4–4.1.10, correspondentes a C 4.2. Campos: unidadeDespesa, funcaoDespesa, subFuncaoDespesa, categoriaDespesa, grupoDespesa, elementoDespesa e fonteRecursosDespesa.

Causa concreta: despesas-totais.js reconstruía a hierarquia com node.open=false para Categoria e Grupo. A aplicação inicial aplicava row.hidden=true aos registros de base; as células marcadas só surgiam após abrir os dois níveis. Não faltavam dados no HTML, nem havia dependência de carregamento remoto ou regra CSS própria ocultando esses campos. As linhas de título geradas não substituem as células marcadas.

Correção mínima: iniciar Categoria e Grupo expandidos, com aria-expanded=true e indicador de expansão coerente. Botões continuam recolhendo e reabrindo os mesmos registros; filtros e exportação continuam usando apenas as linhas de base, sem duplicar grupos. Dados sintéticos, avisos e bloqueio oficial preservados. O gerador de dados não sobrescreve esse JS, portanto a regeneração preserva o comportamento.

Teste direcionado tools/testar_visibilidade_despesas.py: 16 verificações em localhost e 16 na cópia Pages, todos os sete elementos da primeira linha visíveis antes de clique, recolhimento/reabertura Categoria e Grupo, filtros combinados, limpeza, CSV integral de dez registros e recorte de um, com aviso individual. Nenhuma alteração nos dados de 4.1 ou 4.3. A regressão anterior passou a conferir as sete visibilidades iniciais e depois recolher explicitamente os níveis para testar o percurso já existente. Reconhecimento pelo Invoker depende de publicação autorizada e nova avaliação; não executado nesta tarefa.
