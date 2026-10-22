# Concursos e seleções — verificação interna (21/10/2026)

Fonte: `concursos.txt`; Cartilha PETP 2026, critérios 6.6 e 6.7 (pp. 56–60); Serigy Docs PETP 2026, Recursos Humanos, seção Concurso.

| Critério | Exigência quando há certame | Situação do Instituto | Tratamento |
|---|---|---|---|
| 6.6 | Íntegra dos editais, atualização, histórico e acesso pesquisável. | Declaração de ausência desde a criação (20/03/2006) até 21/10/2026. | Publicar declaração expressa, com período e data, abrangendo histórico superior a três anos; não gerar editais ou links artificiais. |
| 6.7 | Lista de aprovados com classificação e nomeações, atualização e acesso pesquisável. | Não houve certame ao qual tais atos se vinculem. | Usar a mesma declaração, com frase de que não existem listas e nomeações decorrentes de certames próprios no período. |

A Cartilha expressamente orienta declarar a não ocorrência no 6.6 e diz que, para 6.7, o critério é considerado atendido quando a ausência de concurso ou seleção da unidade é expressamente indicada. O Serigy lista `editalConcurso`, `aprovadosConcurso` e `nomeadosConcurso` para registros existentes, além de `dataUltimaAtualizacao`, `historicoExercicio` e `filtroPesquisa`; não há atributo específico para declaração negativa. Não preencher marcações de documentos com texto de ausência nem criar links fictícios. Uma declaração textual pode atender à Cartilha, mas a leitura automatizada deve ser testada no Invoker.

O texto recebido contém a data real de referência 21/10/2026 e abrange desde 2006. Na atualização futura, confirmar se surgiram editais ou seleções promovidas pela unidade ou por outro órgão para seu provimento; preservar histórico de eventuais fatos posteriores. Não inferir que ausência de concurso implica ausência de quadro de pessoal, vínculos cedidos ou estagiários.


## Publicação da declaração — 21/10/2026

Fonte efetivamente aplicada: `dados-entrada/rh/concursos-dados-preparados.json`, declaração integral preservada literalmente em quatro parágrafos no conteúdo HTML inicial. Período: 20/03/2006 a 21/10/2026. Os blocos de editais (6.6) e aprovados/classificações/nomeações (6.7) explicitam separadamente o alcance da declaração, sem afirmar inexistência de servidores ou de nomeações de outra natureza.

Aplicado somente `dataUltimaAtualizacao`, item Serigy 6.5.4 (6.6/6.7), sob o schema de Recursos Humanos, à data confirmada da declaração. Removidos os espaços e controles sem dados; não foram criados filtros, documentos, pessoas ou links.

**Dúvida de leitura automatizada:** Definições documenta `serigyEmpty` com motivo único por ocorrência, acompanhado de `serigyItem` na tag sem conteúdo; o exemplo usa um item de exportação. Não há exemplo específico de declaração de não realização de concursos. Não se aplicou `serigyEmpty` isolado nem se marcou a declaração com `editalConcurso`, `aprovadosConcurso` ou `nomeadosConcurso`, em respeito à orientação expressa do arquivo preparado. Confirmar o reconhecimento dessa declaração no Invoker antes de inferir atendimento automatizado. Preservadas as demais pendências de revisão institucional futura.


## Ajuste técnico da consulta da declaração — 22/10/2026

A rota `/Portal-da-Transparencia/RecursosHumanos/Concurso/`, o schema `https://serigy.tce.se.gov.br/comum/recursos-humanos.html` e a única `dataUltimaAtualizacao` (21/10/2026) já existiam e foram preservados. A data continua associada à declaração, não a certames ou documentos inexistentes.

- **6.5.5 / histórico:** acrescentado seletor `historicoExercicio` com `serigyValue` de 2006 a 2026, exercícios efetivamente abrangidos pela declaração. O resultado é a mesma declaração para cada exercício coberto, não um certame por ano. A interface explicita os limites parciais de 2006 e 2026 (20/03/2006 a 21/10/2026); não implica cobertura até dezembro/2026.
- **6.5.6 / filtro:** `filtroPesquisa` envolve consulta funcional por exercício e palavra-chave, com botão `serigyExecuteWaitSection="concursoDeclaracao"`, resultado `serigyLoadSection="concursoDeclaracao"` e limpeza `serigyClearForm`. Não há requisição assíncrona: a consulta local mostra ou oculta a declaração já presente no HTML inicial, com mensagem acessível de resultado. Estrutura baseada nos exemplos de pesquisa de Recursos Humanos e nas definições de espera/carregamento; confirmação no Invoker ainda necessária para esse conjunto sem certames.
- **6.5.1–6.5.3:** continuam sem `editalConcurso`, `aprovadosConcurso` e `nomeadosConcurso`, pois não existem tais conteúdos no período declarado. A seção 6.5 não traz exemplo de `serigyEmpty` para inexistência integral de concursos. A definição geral e o exemplo de campo individual intencionalmente vazio não comprovam o tratamento de todo esse conjunto. Não aplicado por analogia. Solicitar ao TCE/SE orientação sobre reconhecimento da declaração para esses três itens.

Os resultados e mensagens da avaliação anterior foram preservados na matriz. Correção local não altera os resultados do Invoker; dependem de publicação autorizada e nova avaliação. Os testes locais e seus resultados são registrados nas linhas pertinentes da matriz, sem declaração de conformidade automatizada.


**Testes locais em 22/10/2026:** HTTP 200 na rota com e sem barra final e nos 42 links/recursos internos referenciados. Chrome headless executou 11 verificações, sem falhas: conteúdo inicial, consulta em 2006/2023/2024/2026, palavra-chave com acentos e maiúsculas, ausência de resultado, reexibição, rejeição de ano fora da cobertura e limpeza dos campos. A opção de ano fora da cobertura foi criada apenas pela cópia de teste em `trabalho/concurso-verificacao/`, nunca em `dist`. Não foram necessários certames ou documentos fictícios. IDs, rótulos, schema RH, data única e correspondência entre ação e seção de carregamento conferidos. A comparação com o HTML anterior confirmou declaração, cabeçalho, rodapé e marcações preexistentes sem mudanças. Resultado do Invoker continua pendente de nova avaliação.


## Avaliação 4226 — ausência marcada e histórico

Por solicitação expressa do responsável nesta rodada, tabela visível com serigyLoadSection=concursoTabela, cabeçalhos Edital/Aprovados/Nomeados e uma linha de ausência com editalConcurso, aprovadosConcurso e nomeadosConcurso. Cada td usa serigyEmpty com motivo distinto vinculado à declaração institucional; não são links, documentos ou pessoas fictícias. A seção 6.5 documenta os itens, mas não traz exemplo específico dessa ausência integral: a aplicação aqui atende à instrução expressa, sem apresentar interpretação como homologada pelo TCE. Mantidas declaração e data 21/10/2026. Seletor e botão apontam à tabela; change/submit atualizam caption e células para o exercício consultado, incluindo 2026/2025/2024. Seleção repetida é estável; limpeza restaura o período declarado; busca sem resultado não gera ausência institucional nova. Chrome local: 26 verificações sem falhas. Reconhecimento depende de nova avaliação autorizada; Invoker não executado.
