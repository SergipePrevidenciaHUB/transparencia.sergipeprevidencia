# Recursos Humanos — modelos não publicados

## Escopo e fontes

Critérios 6.1, 6.2, 6.3, 6.5, 6.6 e 6.7, aplicáveis à Previdência Estadual. Estagiários (6.4) permanece fora deste recorte de modelos. **C** = exigência da Cartilha PETP 2026; **S** = propriedade/estrutura do Serigy; **DT** = decisão técnica do modelo, sem criar obrigação normativa. Não há dados institucionais homologados ou declaração de atendimento.

Fontes: `AGENTS.md`; Cartilha local, pp. 48–53, nos trechos de 6.1–6.3; S6, `6. Recursos Humanos _ Serigy Docs.pdf`, tabelas das seções 6.1 e 6.2 na p. 1 e exemplos correspondentes; fichas 6.1–6.3 de `controle/inventario-tabelas.md`. A organização e o visual são reutilizados dos modelos de Convênios. Não foram copiados nomes, salários, cargos ou datas dos exemplos S como registros da Unidade.

## Rotas e isolamento

| Página / seção S | Critério C | Modelo versionável | Rota futura após o domínio |
| --- | --- | --- | --- |
| 6.1 Folha de Pagamento / Remuneração Nominal | 6.1 e 6.2 | `modelos/Portal-da-Transparencia/RecursosHumanos/FolhaPagamento/index.html` | `/Portal-da-Transparencia/RecursosHumanos/FolhaPagamento/` |
| 6.2 Padrão Remuneratório para Cargos e Funções | 6.3 | `modelos/Portal-da-Transparencia/RecursosHumanos/PadraoRemuneratorio/index.html` | `/Portal-da-Transparencia/RecursosHumanos/PadraoRemuneratorio/` |
| 6.4 Terceirizados | 6.5 | `modelos/Portal-da-Transparencia/RecursosHumanos/Terceirizados/index.html` | `/Portal-da-Transparencia/RecursosHumanos/Terceirizados/` |
| 6.5 Concurso | 6.6 e 6.7 | `modelos/Portal-da-Transparencia/RecursosHumanos/Concurso/index.html` | `/Portal-da-Transparencia/RecursosHumanos/Concurso/` |

São os segmentos literais de S após `[Portal da Transparencia]`. Os números de seções S não são novos critérios C: **S 6.2 corresponde a C 6.3; S 6.4 a C 6.5; S 6.5 a C 6.6–6.7**.

Os modelos ficam fora de `dist`, origem publicada pelo preparador existente, sem mudar deploy, menu, mapa ou busca públicos. Não foram criadas páginas públicas. Os quatro modelos permanecem na área não publicada. Cabeçalho, rodapé, breadcrumb, busca e acessibilidade seguem os componentes existentes. As URLs de recursos são as mesmas do Portal, destinadas à futura publicação; os modelos não constituem um site independente.

Schema confirmado no `main` dos quatro modelos: `https://serigy.tce.se.gov.br/comum/recursos-humanos.html`. Nenhum item de dados, atualização ou controle de consulta foi marcado em posições vazias/inativas. As marcações dos componentes gerais reais foram preservadas. Não há hash novo, dados fictícios, opções de exercícios inventadas ou declaração de não ocorrência.

## FolhaPagamento — duas consultas na mesma página

**DT:** separar vínculos funcionais e remuneração por competência em duas seções na rota única. Isso permite tratar a temporalidade do cadastro e a da folha sem multiplicar vínculos em uma junção de pagamentos. Os exemplos S admitem dados em linha e em detalhe associado. O modelo escolhe todos os mínimos diretamente nas tabelas, sem exigir abrir detalhes para conhecer a remuneração.

Cada tabela tem somente cabeçalho e `tbody` vazio. Os controles de consulta e exportação estão desativados, sem marcar funcionamento inexistente. Não há autenticação, CPF obrigatório ou formulário de identificação do visitante. Quando alimentada, a relação deve ser aberta, consultável também sem preenchimento prévio de nome/cargo; o filtro não pode substituir a relação por busca exclusivamente individual (C p. 50).

### Vínculos funcionais — C 6.1, pp. 48–49

**C:** tabela estruturada em HTML contendo todos os servidores/autoridades/membros do universo funcional da Unidade. Uma linha futura representa um vínculo no recorte temporal confirmado; a granularidade e o histórico dependem da fonte, sem presumir fotografias mensais ou datas de desligamento.

| Coluna de `#tabela-vinculos` | Origem do conteúdo | Item S / marcação futura | Tipo S |
| --- | --- | --- | --- |
| Nome completo | C 6.1 | S 6.1.1 `nomeServidor` | Texto |
| Cargo/função | C 6.1 | S 6.1.2 `cargoServidor` | Texto |
| Lotação | C 6.1 | S 6.1.4 `lotacaoServidor` | Texto |
| Data de admissão | C 6.1 | S 6.1.5 `admissaoServidor` | Data |
| Data de exoneração ou inativação | C 6.1, quando aplicável | S 6.1.6 `exoneracaoServidor` | Data |
| Carga horária | C 6.1 | S 6.1.7 `cargaHoraria` | Numérico |

Confirmar a unidade da carga horária (por exemplo, referência semanal ou outra), sem presumir valor/unidade. Não preencher exoneração/inativação desconhecida com data, zero ou traço marcado. Para vínculo comprovadamente ativo, a apresentação futura da ausência aplicável precisa distinguir esse fato de dado não recebido; não foi aplicado `serigyEmpty` preventivamente. A propriedade `exoneracaoServidor` cobre também inativação segundo a descrição S; não criar item novo.

### Remuneração nominal — C 6.2, pp. 50–51

**C:** relação/tabela de nome completo, cargo e remuneração; HTML é preferencial. O modelo adota HTML, associado à competência real. Uma linha futura corresponde ao vínculo/competência na granularidade validada da folha, evitando repetir o mesmo pagamento ao relacionar vínculos e rubricas.

| Coluna de `#tabela-remuneracao` | Origem do conteúdo | Item S / marcação futura | Tipo S |
| --- | --- | --- | --- |
| Nome completo | C 6.2 | S 6.1.1 `nomeServidor` | Texto |
| Cargo | C 6.2 | S 6.1.2 `cargoServidor` | Texto |
| Mês da competência | DT: identificar o período exigido para filtro/histórico C | Sem item específico documentado | Não criar propriedade |
| Ano da competência | DT: identificar o período exigido para filtro/histórico C | Sem item específico documentado | Não criar propriedade |
| Remuneração nominal | C 6.2 | S 6.1.3 `salarioServidor` | Monetário |

S denomina a propriedade `salarioServidor`; C pede remuneração nominal. Confirmar o conceito e a composição do valor na origem, sem supor bruto/líquido, introduzir rubricas ou obrigar colunas de descontos/vencimento básico que estas fontes não enumeram. Não confundir o valor efetivamente informado na folha com o padrão legal do cargo de C 6.3.

### Controles, histórico, atualização e exportação

| Requisito C | Reserva no modelo | Marcação S futura / alcance |
| --- | --- | --- |
| 6.1: filtro mínimo por nome e cargo/função | `#filtro-vinculos`, `#nome-vinculos`, `#cargo-vinculos` | S 6.1.11 `filtroPesquisa` no formulário funcional. Não inventar itens para campos do formulário. |
| 6.2: filtro mínimo por nome, mês e ano | `#filtro-remuneracao`, `#nome-remuneracao`, `#mes-remuneracao`, `#ano-remuneracao` | Mesmo S 6.1.11, na consulta de remuneração. Opções somente de períodos reais, sem tornar nome obrigatório. |
| Ambos: pelo menos os três anos anteriores ao da consulta | `#ano-vinculos` e `#ano-remuneracao` | S 6.1.9 `historicoExercicio` e opções reais com `serigyValue`. Em vínculos, o seletor de exercício é DT para apresentar histórico, além dos dois filtros mínimos C. Os anos do exemplo S não limitam a cobertura C. |
| Ambos: gravação do conjunto selecionado em pelo menos um formato editável | `#exportar-vinculos` e `#exportar-remuneracao` | S 6.1.10 `salvarRelatorio`, com `serigyValue` do formato efetivamente gerado. DT: implementar CSV ou outro editável; não prometer todos os formatos do exemplo. PDF sozinho não atende a esta exigência C. |
| Ambos: dados mais recentes de até 30 dias anteriores à consulta | `#atualizacao-vinculos` e `#atualizacao-remuneracao` | S 6.1.8 `dataUltimaAtualizacao`, somente após inserir a data real. Competência, cobertura e data de geração não comprovam atualização. Referências separadas evitam atribuir à folha a data de um cadastro diferente. |

Ao implementar a busca, associar `#pesquisar-vinculos` a `#resultados-vinculos` e `#pesquisar-remuneracao` a `#resultados-remuneracao`: `serigyExecuteWaitSection` na ação e `serigyLoadSection` no resultado, com valor coincidente por consulta. Os identificadores são DT; não precisam copiar os IDs de exemplo S. O schema é herdado do `main`.

Aplicar os `serigyItem` às células reais do mesmo registro, preservando pessoa/cargo/período e seus valores associados. Exportação deve corresponder ao filtro de cada consulta e incluir todos os mínimos C, mesmo se algum vier a ser exibido em detalhe. Não exportar dados privados adicionais por aproveitar uma planilha de origem. A sugestão C de acesso automatizado não transforma todos os formatos S em obrigatórios. Não há inteiro teor de contracheques ou atos individuais exigido como anexo nestes critérios.

## PadraoRemuneratorio — C 6.3, pp. 51–53

Tabela `#tabela-padroes` com todas as faixas reais dos cargos/funções previstos na estrutura. Pode ser extraída da legislação remuneratória atualizada; não é relação de pagamentos nominais.

| Coluna | Origem | Item S / marcação futura | Tipo S |
| --- | --- | --- | --- |
| Cargo/função | C 6.3 | S 6.2.1 `cargo` | Texto |
| Nível, classe ou padrão | C: todas as faixas conforme cada cargo; S explicita a descrição | S 6.2.3 `descricao` | Texto |
| Remuneração/salário | C 6.3 | S 6.2.2 `salario` | Monetário |

Não inventar níveis/classes para cargos que não os possuam; confirmar a descrição aplicável à faixa e a maneira de representar casos sem escalonamento. Uma linha por faixa real é DT, com valores e vigência provenientes da fonte. Reservas `#normas-padroes` e `#vigencia-padroes` permitem identificar/vincular a legislação de suporte e informar a vigência quando comprovadas; hoje estão vazias, sem links ou declarações.

**Atualidade C:** referência de até um ano. Se a tabela não tiver sido atualizada nesse intervalo, a seção deve informar expressamente, com confirmação institucional, que continua vigente para o exercício atual (C p. 53). Não alterar a data para simular revisão. Em `#atualizacao-padroes`, inserir a referência real e só então `serigyItem="dataUltimaAtualizacao"` (S 6.2.4). Uma declaração de vigência não deve ser marcada como se fosse uma data.

**Sem filtro, série histórica ou exportação autônomos exigidos por C 6.3.** A tabela S 6.2 enumera apenas `cargo`, `salario`, `descricao` e atualização. Por isso este modelo não tem controles de busca, histórico ou exportação, nem reaproveita os controles da folha como se fossem obrigação própria. O `serigyLoadSection` do exemplo de tabela não implica criar uma ação de pesquisa fictícia para conteúdo estático.

## Preparação para alimentação e publicação futura

São necessários: cadastro funcional e sua cobertura histórica; folha por competência com definição dos valores; vínculo técnico confiável entre fontes; tabela remuneratória completa e legislação/vigências; datas reais e responsabilidade de atualização. IDs internos para relacionar vínculo, cargo e competência são DT a definir com a fonte, não novas colunas públicas obrigatórias e não motivo para publicar CPF/matrícula automaticamente.

As pendências específicas, inclusive pessoais, estão em `controle/recursos-humanos-pendencias.md`. Não publicar cadastro de segurados do RPPS como se fosse quadro funcional da autarquia. Nomes e remuneração integram a transparência nominal exigida; isso não autoriza divulgar CPF, endereço residencial, dados bancários, dependentes, saúde ou outras informações da origem não exigidas. Conferir quais campos efetivamente comporão HTML e exportação, sem criar login para o cidadão.

Antes de mover cada modelo para `dist`: validar abrangência, registros e temporalidade; alimentar tabelas sem exemplos; implementar os controles da folha e exportações do recorte; aplicar marcações somente ao conteúdo existente; confirmar atualidade/vigência do padrão; testar acessibilidade, filtros e extração; depois atualizar navegação pública em tarefa autorizada. A existência do modelo não comprova atendimento aos critérios. Não foram alterados `dist`, Estagiários, Receitas ou deploy.


## Complemento — Terceirizados e Concurso

Fontes adicionais conferidas: C 6.5 (pp. 55–56), 6.6 (pp. 56–58) e 6.7 (pp. 58–60); S6, tabelas das seções 6.4 e 6.5 (pp. 1–2) e respectivos exemplos tabulares/atualização (p. 3). Nenhum registro ou documento dos exemplos foi incorporado. As estruturas de Folha e Padrão Remuneratório permanecem inalteradas.

### Terceirizados — C 6.5 / S 6.4

**C:** relação com nome completo, função/atividade e nome/razão social da empregadora. C admite lista documental em PDF ou XLS. **DT:** adotar tabela HTML com esses três campos, conforme o exemplo S, sem exigir HTML como única forma normativa nem criar colunas de CPF, salário, admissão ou número de contrato.

| Coluna de `#tabela-terceirizados` | Origem C | Item S / `serigyItem` futuro | Tipo S |
| --- | --- | --- | --- |
| Nome completo | C 6.5, p. 55 | 6.4.1 `nomeTerceirizado` | Texto |
| Função ou atividade exercida | C 6.5, p. 55 | 6.4.2 `funcaoTerceirizado` | Texto |
| Empresa empregadora | C 6.5, p. 55 | 6.4.3 `empresaTerceirizado` | Texto |

A referência de exercício/cobertura pertence à fonte para selecionar registros do histórico (DT); não se deve deduzi-la da data de importação. Definir com a área como representar mudanças de atividade/empregadora ao longo do tempo sem duplicar indevidamente pessoas nem apagar vínculos reais.

| Requisito C, p. 56 | Reserva | S / aplicação futura |
| --- | --- | --- |
| Filtro mínimo por ano | `#filtro-terceirizados`, seletor `#ano-terceirizados` | 6.4.7 `filtroPesquisa` no formulário funcional |
| Pelo menos os três anos anteriores ao da consulta | Mesmo seletor | 6.4.5 `historicoExercicio`, com `serigyValue` em opções de exercícios reais. Não limitar ao ano corrente ou aos anos do exemplo S. |
| Gravação do conjunto selecionado em pelo menos um editável **ou PDF pesquisável**, alternativa expressa C | `#exportar-terceirizados` | 6.4.6 `salvarRelatorio` e `serigyValue` do formato efetivamente fornecido. Não exigir todas as extensões exemplificadas. |
| Atualidade: até 180 dias da consulta | `#atualizacao-terceirizados` | 6.4.4 `dataUltimaAtualizacao`, somente com data real preenchida e cobertura confirmada |

Não há obrigação autônoma de anexar contratos de trabalho, contracheques ou contratos administrativos em C 6.5. Uma lista oficial pode ser usada como apresentação documental, se completa e acessível; o download não dispensa conferir histórico, filtro e atualidade aplicáveis. Se a gravação for PDF, precisa ser pesquisável e corresponder ao conjunto selecionado; uma lista estática não deve anunciar que segue filtros que não aplica.

### Concurso — C 6.6 e 6.7 / S 6.5

**DT:** uma página com duas seções, editais e demais atos, ambas organizadas por certame. Os índices são tabelas de metadados e documentos; não impõem transcrição de candidatos. Os documentos de cada seção devem manter associação inequívoca ao mesmo certame, mesmo estando em tabelas distintas. A identificação de certame é DT para associação/localização, sem novo `serigyItem` para número, título ou ano.

| Reserva de conteúdo | Exigência C | Item S / marcação futura | Tipo S |
| --- | --- | --- | --- |
| Identificação do certame nas duas tabelas | DT: contexto e associação dos documentos | Sem propriedade específica nestas seções S | Não inventar item |
| Editais integrais em `#tabela-editais` | 6.6: concursos e seleções da Unidade para provimento de cargos/empregos públicos | 6.5.1 `editalConcurso` | Link |
| Aprovados com respectivas classificações em `#tabela-atos-concurso` | 6.7: relação/lista completa dos aprovados e suas classificações | 6.5.2 `aprovadosConcurso` | Link / Numérico |
| Nomeações, associadas ao mesmo certame | 6.7: atos/listas de nomeação | 6.5.3 `nomeadosConcurso` | Link / Texto |

Como no exemplo S, aplicar o item à célula real com seu link identificado, ou ao conteúdo efetivamente apresentado segundo o tipo documentado; não marcar cabeçalhos ou células vazias. A alternativa Numérico de `aprovadosConcurso` não autoriza substituir a lista ranqueada por mero total de aprovados, pois C exige a lista com classificações. Nomeação não pode ser inferida da aprovação.

C 6.7 admite planilha ou acesso aos dados hospedados no executor do certame. Índices documentais completos são a escolha inicial, sem impor uma base nominal extra. As URLs devem levar diretamente aos documentos/dados do certame, não à capa genérica de um site. Não criar URLs pelo número/ano nem usar `serigyLink` para PDF. Retificações e outros atos só serão indexados se existentes e pertinentes; não inventar categorias de documentos como novas obrigações C.

| Controle / exigência | Editais — C 6.6 | Demais atos — C 6.7 |
| --- | --- | --- |
| Filtro C | Filtro específico genérico, sem parâmetros mínimos enumerados. **DT:** exercício e identificação do certame em `#filtro-editais`, `#ano-editais`, `#busca-editais`. | Filtro específico genérico. **DT:** identificação do certame em `#filtro-atos-concurso`, `#busca-atos-concurso`; não exigir nome/CPF de candidato. |
| Marcação do filtro S | 6.5.6 `filtroPesquisa` | 6.5.6 `filtroPesquisa` |
| Histórico C | Pelo menos os três anos anteriores à consulta. C p. 58 acrescenta que, quando o dado mais recente é do ano imediatamente anterior à consulta (X), a série deve contemplar X-1/X-2/X-3. Preservar essa formulação e confirmar o recorte, sem reduzir automaticamente a três exercícios. | Não há série histórica autônoma na lista de itens C 6.7; não transportar a obrigação de 6.6 para os demais atos. Manter a associação e o acervo real dos certames disponíveis. |
| Marcação do histórico S | 6.5.5 `historicoExercicio` em `#ano-editais`, opções com exercícios reais e `serigyValue` | S 6.5.5 refere-se somente a C 6.6; não foi reservado seletor histórico próprio aqui. |
| Atualidade C | Informações mais recentes registradas em até um ano da consulta (C p. 57) | Até 30 dias **quando houver concurso/processo seletivo em andamento** (C p. 59). Não generalizar esse prazo para qualquer acervo encerrado. |
| Atualização S | 6.5.4 `dataUltimaAtualizacao`, reserva `#atualizacao-editais` | Mesmo item S, reserva `#atualizacao-atos-concurso`; referências separadas porque prazos e conjuntos diferem. |
| Exportação | C não lista gravação de relatórios; S não documenta `salvarRelatorio` nesta seção. Downloads são dos próprios editais. | C não lista gravação de relatórios; S não documenta `salvarRelatorio`. Downloads/acesso às listas e atos não criam obrigação de exportação editável autônoma. |

C 6.6 (p. 58) e 6.7 (p. 59) admitem, na avaliação do filtro, documentos facilmente identificáveis e acessíveis, inclusive os de terceiros não pesquisáveis nas condições descritas. Isso não autoriza publicar arquivos ilegíveis, dispensar a íntegra dos editais ou substituir resultados por links genéricos. Os campos de busca escolhidos são DT, não mínimos normativos enumerados.

### Ativação dos novos modelos

Os três formulários e a exportação de Terceirizados estão desativados. Os `tbody` estão vazios, sem linhas ou links fictícios. Não há avisos internos nas páginas nem `serigyItem`/`serigyEmpty` em dados ausentes ou controles inativos. Reservas de atualização estão vazias e sem marcação de data; só preenchê-las com referências reais, nunca automaticamente com a data de geração.

Após implementar as consultas: `#pesquisar-terceirizados` → `#resultados-terceirizados`; `#pesquisar-editais` → `#resultados-editais`; `#pesquisar-atos-concurso` → `#resultados-atos-concurso`. Usar `serigyExecuteWaitSection` na ação e `serigyLoadSection` no resultado, com valor coincidente por consulta. IDs são DT, não nomes obrigatórios de S.

Não ocorrência depende de confirmação institucional: para terceirizados, informar explicitamente os exercícios sem contratação (C p. 56); para editais, período e referência atualizada conforme C p. 58; para 6.7, a ausência de concursos/processos seletivos deve ser expressamente informada, quando verdadeira (C p. 59). Não confundir arquivo não recebido, certame sem nomeação conhecida e inexistência de certames. Nenhuma declaração foi inserida nos modelos.

Antes de publicação: receber relação e referências históricas de terceirizados; catálogo real dos certames, editais integrais, listas ranqueadas e nomeações; conferir correspondências e acesso público; confirmar cobertura/datas; implementar filtros e gravação aplicável; alimentar e marcar somente dados reais. Não acrescentar os modelos vazios ao menu público. Modelos e pendências não atestam atendimento.


## Alimentação real de Padrão Remuneratório — somente C 6.3

A página de `dist/Portal-da-Transparencia/RecursosHumanos/PadraoRemuneratorio/index.html` recebe a aba **Padrão Remuneratório** de `dados-entrada/rh/Padrao_Remuneratorio.xlsx`: 18 linhas físicas (cabeçalho + **17 registros**), cinco colunas. Cargos, símbolos, ordem e valores são preservados. Não se alteram outros critérios, modelos, planilha ou componentes comuns.

Fontes efetivamente conferidas nesta alimentação: Cartilha PETP 2026, C 6.3, pp. 51–53; Serigy Docs de Recursos Humanos, tabela S 6.2.1–4 na p. 1 e trecho do exemplo correspondente nas pp. 2–3. O quadro C inclui Previdências Municipais e Estadual. C exige disponibilidade de todas as faixas dos cargos/funções e atualidade; para tabela sem revisão no intervalo de um ano, a declaração de vigência no exercício atual exige confirmação. Não há filtro, série histórica ou exportação autônomos neste critério; não foram acrescentados.

| Coluna da origem | Apresentação e marcação | Distinção de origem / decisão técnica |
| --- | --- | --- |
| Cargo/Denominação | Texto integral em `cargo` (S 6.2.1) | Campo C/S; não corrigir denominações nem deduzir outros cargos. |
| Símbolo/Nível | Texto em `descricao` (S 6.2.3), somente quando diferente de “-” | A fonte identifica símbolo/nível; é a descrição da classificação disponível, sem inventar faixas ou novos atributos. |
| Remuneração Base / Vencimento (R$) | Coluna própria; valores numéricos em `salario` (S 6.2.2) | Modalidade explícita na fonte. Não somar às demais nem convertê-la em remuneração nominal de servidor. |
| Remuneração CC Sem Vínculo 100% (R$) | Coluna própria; valores numéricos em `salario` | Preservar título e valor originais; não recalcular percentuais. |
| Remuneração CC Com Vínculo 60% (R$) | Coluna própria; valores numéricos em `salario` | Preservar título e valor originais, sem calcular 60% da outra coluna ou presumir composição. |

Schema no `main`: `https://serigy.tce.se.gov.br/comum/recursos-humanos.html`; tabela com `serigyLoadSection="padraoRemuneratorio"`, conforme o exemplo S. Os três valores de remuneração possíveis continuam associados ao cargo/símbolo na mesma linha; cabeçalhos e atributos `headers` distinguem cada modalidade. Não se criam propriedades como salarioBase/semVinculo/comVinculo. Há 17 marcações `cargo`, 15 `descricao` e 25 `salario`. Os 28 sinais “-” (26 nas remunerações e dois nos símbolos) permanecem literais e sem marcação de valor disponível; não viram zero, N/A ou declaração de inexistência.

A tabela usa caption, cabeçalhos `scope="col"`, associações explícitas de cabeçalho por célula e a rolagem/acessibilidade já existente no Portal. Nenhum CSS ou JavaScript é alterado. Não se inventa data, norma ou declaração de vigência; `dataUltimaAtualizacao` (S 6.2.4) não é aplicado sem data comprovada.


## Estagiários — alimentação de C 6.4 / Serigy 6.3

A página existente em `/Portal-da-Transparencia/RecursosHumanos/Estagiarios/` recebe `dados-entrada/rh/estagiarios.xlsx`, aba Plan1: 714 registros, preservados na ordem da fonte, sem deduplicação. Ano da relação: 2023=54; 2024=197; 2025=242; 2026=221. A fonte substitui somente a demonstração anterior da página; seus arquivos de teste antigos permanecem preservados, sem links nesta consulta.

- Nome → `nomeEstagiario`; Data de Contratação → `admissaoEstagiario`; término/desligamento preenchido → `terminoEstagiario`. Os 605 términos vazios não recebem essa marcação.
- Ano/Mês da origem representam o período da relação. Não são contratação. O filtro obrigatório de ano de contratação é derivado da Data de Contratação: 2022=1; 2023=234; 2024=168; 2025=247; 2026=64. Ano e mês da relação são filtros complementares (DT); `historicoExercicio` identifica o controle anual da relação e os exercícios reais usam `serigyValue`.
- Setor/Local e Houve Aditivo? são complementares, sem propriedades Serigy inventadas. Vazios são exibidos como “Não informado”, preservados vazios no CSV. Não se deduz situação contratual.
- Schema RH; formulário `filtroPesquisa`; ação `serigyExecuteWaitSection` / tabela `serigyLoadSection` associadas a `estagiarioTabela`; limpeza `serigyClearForm`; exportação `salvarRelatorio`, formato `csv`. CSV editável do recorte, sem eliminação de repetições. Linhas completas no HTML inicial e somente ocultadas pelos filtros.
- Não há `dataUltimaAtualizacao` sobre valor ausente. A data real continua pendente. Não se declara atualidade ou cobertura histórica completa.

Geração reproduzível: `.\.venv\Scripts\python.exe -B tools/integrar_estagiarios.py`; conferência sem escrita: acrescentar `--check`. O gerador trabalha somente no conteúdo da página e no CSV correspondente; o importador genérico anterior não suporta esta estrutura de sete colunas.


## Terceirizados — carga real de C 6.5 / Serigy 6.4

Fonte: `dados-entrada/rh/terceirizados.xlsx`, aba Plan1, 3.078 registros de relações mensais: 2023=673; 2024=747; 2025=902; 2026=756. Página existente: `/Portal-da-Transparencia/RecursosHumanos/Terceirizados/`. A alimentação substitui a estrutura sem dados dessa rota, sem alterar os modelos não publicados.

| Coluna pública | Fonte e marcação |
| --- | --- |
| Ano | ANO: período da relação; controle anual obrigatório, `historicoExercicio` e opções com `serigyValue` real. |
| Mês | MÊS: período da relação; filtro complementar DT, sem propriedade de dados inventada. |
| Nome completo | NOME → `nomeTerceirizado`, S 6.4.1. |
| Função ou atividade exercida | CARGO → `funcaoTerceirizado`, S 6.4.2. |
| Empresa empregadora | EMPRESA → `empresaTerceirizado`, S 6.4.3. |

Schema RH: `https://serigy.tce.se.gov.br/comum/recursos-humanos.html`. Filtro `filtroPesquisa` (S 6.4.7); ação e resultados associados a `tabela-terceirizados` por `serigyExecuteWaitSection`/`serigyLoadSection`; limpeza `serigyClearForm`. CSV editável (C 6.5; S 6.4.6 `salvarRelatorio`, `serigyValue="csv"`) com exatamente as cinco colunas, nomes e ordem da tabela. O download dinâmico segue o recorte ano/mês; o arquivo estático contém a relação completa.

Todas as linhas permanecem no HTML inicial; filtros somente alteram sua visibilidade. Repetições e empresas foram preservadas, sem seleção por natureza contratual. LOTAÇÃO, DATA DE ADMISSÃO e DATA DE DEMISSÃO não são publicadas nem incorporadas aos atributos ou CSV. Campos vazios são mostrados como “Não informado”, sem marcação Serigy de valor; no CSV permanecem vazios. Não há `dataUltimaAtualizacao` sem referência real (S 6.4.4). A carga não atesta completude histórica/atualidade ou atendimento integral.

Geração: `.\.venv\Scripts\python.exe -B tools/integrar_terceirizados.py`; conferência sem escrita: `--check`. Conciliação integral: `tools/testar_terceirizados.py`.


## Relação nominal de servidores — alimentação de C 6.1 / Serigy 6.1

Fonte: `dados-entrada/rh/relacao-servidores.xlsx`, aba Plan1, 1.598 registros: 2023=430; 2024=449; 2025=416; 2026=303. Ano/Mês representam o período da relação, não admissão. A rota existente `/Portal-da-Transparencia/RecursosHumanos/FolhaPagamento/` reúne a relação nominal e a estrutura ainda sem remuneração. Esta alimentação atua somente no bloco 6.1; não consulta outra planilha nem preenche C 6.2.

| Coluna pública | Fonte, marcação e limites |
| --- | --- |
| Ano/Mês da relação | Ano/Mês da fonte; consulta temporal e `historicoExercicio` no ano com `serigyValue` dos exercícios reais. |
| Nome completo | Nome do Servidor → `nomeServidor` (S 6.1.1). |
| Cargo/função | Função e Cargo Efetivo identificados separadamente dentro da célula, quando preenchidos → `cargoServidor` (S 6.1.2). O literal VAZIO não compõe cargo/função nem o CSV. |
| Lotação | Local → `lotacaoServidor` (S 6.1.4). |
| Data de início de exercício | Data de Início de Exercicío, com rótulo fiel. Equivalência à data de admissão confirmada pela instituição para esta relação; `admissaoServidor` (S 6.1.5) aplicado às 1.598 datas, preservando valores e rótulo. |
| Data de exoneração ou inativação | Campo homônimo → `exoneracaoServidor` (S 6.1.6) somente para data válida preenchida; ausência não prova situação ativa. |
| Carga horária informada | Quantidade de Horas → `cargaHoraria` (S 6.1.7), preservando o número sem atribuir periodicidade ou converter valores. |

Schema RH `https://serigy.tce.se.gov.br/comum/recursos-humanos.html`. Filtros de nome e cargo/função exigidos para C 6.1; ano/mês da relação permitem o recorte temporal. Busca textual simples desconsidera acentos/caixa e combina palavras no próprio campo. Formulário `filtroPesquisa`; ação/resultados ligados a `tabela-vinculos` por `serigyExecuteWaitSection`/`serigyLoadSection`; limpeza `serigyClearForm`. Exportação CSV editável do mesmo recorte (`salvarRelatorio`, `serigyValue="csv"`), com as oito colunas da tabela e sem remuneração.

As linhas completas estão no HTML inicial e são apenas ocultadas pelos filtros. Não há deduplicação de pessoas ou períodos nem criação de meses ausentes. Datas/cargos vazios usam “Não informado” sem marcação de valor; CSV mantém vazio. Nenhum `dataUltimaAtualizacao` foi atribuído sem fonte real.

Geração: `.\.venv\Scripts\python.exe -B tools/integrar_servidores.py`; conferência: `--check`; conciliação integral: `tools/testar_servidores.py`. O gerador preserva o bloco de remuneração, limitando o aviso de conteúdo pendente a esse bloco.


## Remuneração nominal — alimentação de C 6.2 / Serigy 6.1

Situação atual: o gerador `tools/integrar_servidores.py` alimenta os dois blocos da rota `/Portal-da-Transparencia/RecursosHumanos/FolhaPagamento/`. A etapa anterior descrita acima era restrita ao 6.1; sua relação, CSV, filtros, datas e 1.598 marcações `admissaoServidor` são preservados.

Fonte de rendimentos: `dados-entrada/rh/remuneracao.xlsx`, Plan1, 2.312 linhas. Associar a `relacao-servidores.xlsx` por Ano, Mês e Nome do Servidor; a normalização limita-se a Unicode NFC, espaços e caixa. Acentos não são removidos no vínculo, nem se usam aproximações por nome. Exigir chave única dos dois lados; não somar linhas duplicadas nem decidir a associação por cargo.

- **714 linhas excluídas da consulta de servidores:** Cargo Efetivo identificado literalmente como `ESTAGIARIO UNIVERSITARIO - RESOL 001/21` (6) ou `ESTAGIARIO UNIVERSITARIO - RESOL 001/22` (708). Por ano: 2023=147, 2024=170, 2025=209, 2026=188. Não se trata de remuneração da relação de servidores e nenhuma dessas linhas foi transferida para outro módulo. Os índices físicos das 714 linhas e a classificação estão em `controle/remuneracao-conciliacao.json`.
- **Chave ambígua:** dezembro/2024, José Roberto de Lima Andrade: linhas 859/860 da relação e 1170/1171 da remuneração. Ambos os rendimentos ficam fora do bloco 6.2 até decisão institucional; os vínculos originais do 6.1 permanecem.
- **1.596 registros conciliados:** 2023=430; 2024=447; 2025=416; 2026=303. A conta de cobertura da fonte é 2.312 = 714 estágios + 2 pendências ambíguas + 1.596 publicados.

| Coluna pública | Origem e marcação confirmada |
| --- | --- |
| Ano/Mês da competência | Ano/Mês da remuneração, associados ao mesmo período da relação; ano com `historicoExercicio` e opções reais `serigyValue`. |
| Nome completo | Nome da relação conciliada → `nomeServidor`, S 6.1.1 / C 6.2. |
| Cargo/função | Função e Cargo Efetivo da relação conciliada, sem VAZIO → `cargoServidor`, S 6.1.2 / C 6.2. Nesta origem, os cargos dos registros conciliados coincidem entre as duas fontes. |
| Valor de rendimentos do contracheque | `Valor de Rendimento Contra-Cheque` → `salarioServidor`, S 6.1.3 / C 6.2. A propriedade técnica não transforma esse valor em salário-base nem comprova a composição das rubricas. |

Schema RH já existente. Filtros combináveis de nome/mês/ano: `filtroPesquisa`; ação/resultados correspondentes `tabela-remuneracao` em `serigyExecuteWaitSection`/`serigyLoadSection`; limpeza `serigyClearForm`. CSV editável do recorte com exatamente as cinco colunas (`salvarRelatorio`, `serigyValue="csv"`), sem descontos, valor líquido ou planilha de origem. Não se exige cadastro/conhecimento de CPF para abrir a relação. Dados presentes no HTML inicial, somente ocultados pelos filtros; não há marcação de atualização sem data comprovada.

**DT monetária:** todas as células de rendimentos da fonte têm formato `#,##0.00_);(#,##0.00)`. Há resíduos de representação numérica menores ou iguais a 8E-12 real em parte dos valores armazenados. HTML e CSV usam os centavos exibidos na origem, calculados com Decimal e arredondamento HALF_UP, sem alterar o XLSX. O JSON registra valor armazenado/exibido por linha afetada. O gerador recusa uma precisão monetária efetiva superior à tolerância 1E-8 real e registra pendência, em vez de ocultar casas significativas por arredondamento. As somas são conciliadas em centavos com a fonte, sem agregar registros da chave ambígua.

`controle/remuneracao-conciliacao.json` é interno e reproduzível: índices excluídos, duplicidades, pendências, contagens, somas por ano e evidências de precisão; não entra em `dist`. Conferência de geração: `tools/integrar_servidores.py --check`. Testes específicos: `tools/testar_servidores.py` e `tools/testar_remuneracao.py`.
