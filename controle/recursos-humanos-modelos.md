# Recursos Humanos — modelos de folha e padrão remuneratório

## Escopo e fontes

Somente os critérios 6.1, 6.2 e 6.3, aplicáveis à Previdência Estadual. **C** = exigência da Cartilha PETP 2026; **S** = propriedade/estrutura do Serigy; **DT** = decisão técnica do modelo, sem criar obrigação normativa. Não há dados institucionais homologados ou declaração de atendimento.

Fontes: `AGENTS.md`; Cartilha local, pp. 48–53, nos trechos de 6.1–6.3; S6, `6. Recursos Humanos _ Serigy Docs.pdf`, tabelas das seções 6.1 e 6.2 na p. 1 e exemplos correspondentes; fichas 6.1–6.3 de `controle/inventario-tabelas.md`. A organização e o visual são reutilizados dos modelos de Convênios. Não foram copiados nomes, salários, cargos ou datas dos exemplos S como registros da Unidade.

## Rotas e isolamento

| Página / seção S | Critério C | Modelo versionável | Rota futura após o domínio |
| --- | --- | --- | --- |
| 6.1 Folha de Pagamento / Remuneração Nominal | 6.1 e 6.2 | `modelos/Portal-da-Transparencia/RecursosHumanos/FolhaPagamento/index.html` | `/Portal-da-Transparencia/RecursosHumanos/FolhaPagamento/` |
| 6.2 Padrão Remuneratório para Cargos e Funções | 6.3 | `modelos/Portal-da-Transparencia/RecursosHumanos/PadraoRemuneratorio/index.html` | `/Portal-da-Transparencia/RecursosHumanos/PadraoRemuneratorio/` |

São os segmentos literais de S após `[Portal da Transparencia]`. Os números de seções S não são novos critérios C: em particular, **S 6.2 corresponde a C 6.3**.

Os modelos ficam fora de `dist`, origem publicada pelo preparador existente, sem mudar deploy, menu, mapa ou busca públicos. Não foram criadas páginas públicas nem uma terceira página de Recursos Humanos. Cabeçalho, rodapé, breadcrumb, busca e acessibilidade seguem os componentes existentes. As URLs de recursos são as mesmas do Portal, destinadas à futura publicação; os modelos não constituem um site independente.

Schema confirmado no `main` das duas páginas: `https://serigy.tce.se.gov.br/comum/recursos-humanos.html`. Nenhum item de dados, atualização ou controle de consulta foi marcado em posições vazias/inativas. As marcações dos componentes gerais reais foram preservadas. Não há hash novo, dados fictícios, opções de exercícios inventadas ou declaração de não ocorrência.

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
