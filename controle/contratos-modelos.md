# Contratos — modelo principal não publicado

**C**: Cartilha PETP 2026, critérios 9.1 (p. 75) e 9.2 (pp. 76–77, apenas a continuação do filtro). **S**: Serigy Docs, seção 9.1 Contratos, tabela da p. 1 e exemplos correspondentes da p. 2. **DT**: decisão técnica de apresentação/relacionamento, sem novo requisito normativo. Foram lidos `AGENTS.md` e o modelo de Licitações como referência visual. Não há trabalho nas consultas de Fiscais ou Ordem Cronológica.

## Rota e escopo

S indica `[Portal da Transparencia]/Contratos`. Modelo: `modelos/Portal-da-Transparencia/Contratos/index.html`. Destino futuro: `dist/Portal-da-Transparencia/Contratos/index.html`, rota `/Portal-da-Transparencia/Contratos/`. O modelo fica fora de `dist`, origem publicada pelo preparador existente, sem alterar deploy, menu, mapa ou busca públicos.

Schema confirmado no `main`: `https://serigy.tce.se.gov.br/comum/contratos.html`. Só o contexto está marcado; não há itens de dados em cabeçalhos/células vazias, controles inativos ou datas desconhecidas. Busca geral e acessibilidade preservam as marcações de componentes reais. Não há nomes, valores, números de contratos, links documentais, datas ou declarações de inexistência inventados.

## Correspondência C / S e estrutura

C 9.1 exige relação em ordem sequencial, com resumo do contratado, valor, objeto e vigência, incluindo os aditivos decorrentes, se houver. **DT:** tabela HTML para o resumo, com acesso aos documentos do mesmo contrato. A redação consultada de C 9.1 não impõe por si uma tabela HTML universal; esta escolha reaproveita o padrão e os exemplos S. Resumo e inteiro teor são conteúdos distintos: C 9.2 exige íntegras dos contratos e, se houver, de seus termos aditivos.

| Coluna de `#tabela-contratos` | Origem | Item S / marcação futura | Tipo literal S |
| --- | --- | --- | --- |
| Sequência | C: ordem sequencial; S explicita sequência; posição exibida é DT | 9.1.7 `sequencia` | Numérico |
| Número do contrato | S: identificação do contrato | 9.1.1 `numeroContrato` | Texto |
| Contratado(a) | C 9.1 | 9.1.2 `contratado` | Texto |
| Valor | C 9.1 | 9.1.3 `valorContrato` | Monetário |
| Objeto | C 9.1 | 9.1.4 `objeto` | Texto |
| Início da vigência | C: vigência; S separa os limites | 9.1.5 `inicioContrato` | Data |
| Fim da vigência | C: vigência; S separa os limites | 9.1.6 `fimContrato` | Data |
| Aditivos decorrentes (resumo) | C 9.1: informação dos aditivos existentes; resumo/associação na linha é DT | Não criar item para resumo; `termoAditivo` aplica-se ao link/arquivo real, descrito abaixo | Não inventar propriedade |
| Documentos integrais | DT: acesso ao detalhe do mesmo contrato | Ação/contexto, sem novo item de dados | Não substituir documentos por botão vazio |

Preservar a identificação oficial como texto, com zeros, ano e pontuação quando constarem da fonte; não deduzir número/ano pelo nome de arquivo. A sequência de apresentação não substitui o número do contrato. A natureza e o alcance do valor precisam ser esclarecidos com a área: não somar novamente o valor integral a cada aditivo nem inferir que valor original e atualizado sejam iguais.

| Documento / contexto | Critério C | Item S / marcação futura | Reserva |
| --- | --- | --- | --- |
| Contrato integral | 9.2 | 9.1.9 `linkContrato` (Link/Arquivo) | `#documentos-integra-contrato` |
| Cada termo aditivo integral, se houver | 9.1 e 9.2 | 9.1.8 `termoAditivo` (Link/Arquivo) | `#documentos-integra-aditivos`; o resumo permanece associado à linha |

**DT:** `#detalhes-contrato` e `#identificacao-contrato` reservam o detalhe/contexto de um registro real. Ao alimentar, relacionar contrato, resumos dos aditivos e documentos por referência confiável, com IDs únicos por contrato quando houver vários detalhes. O modelo vazio não representa um contrato selecionado. Aplicar os itens S a células/contêineres com links ou arquivos reais, como no exemplo S; não marcar listas vazias ou o cabeçalho. Os exemplos não comprovam correspondência entre seus números e nomes de arquivos: conferir cada documento institucional.

Os aditivos são uma relação de um para muitos; não repetir o contrato como novo registro por documento nem fundir vários instrumentos apenas por número semelhante. Exibir resumo dos efeitos documentados, sem criar colunas obrigatórias de aditivos não enumeradas nas fontes. Falta de arquivo não comprova inexistência de aditivos. Não preencher vigência desconhecida ou eventual condição especial com uma data presumida.

## Filtros, histórico, gravação e atualização

| Requisito C | Reserva / DT | S / futura aplicação funcional |
| --- | --- | --- |
| 9.1: filtro mínimo por período | `#filtro-contratos`, `#periodo-inicial-contratos`, `#periodo-final-contratos` | 9.1.10 `filtroPesquisa` no formulário funcional. Campos de início/fim do recorte são DT, não novos mínimos específicos nomeados por C. |
| 9.2: filtro específico genérico | DT: reaproveitar a consulta dos contratos para localizar seus inteiros teores e aditivos associados | Mesmo 9.1.10, sem transformar período ou outros parâmetros em mínimos próprios de 9.2 |
| 9.1 e 9.2: histórico de pelo menos os três anos anteriores ao da consulta | `#ano-contratos`; seletor de exercício é DT de acesso ao acervo | 9.1.13 `historicoExercicio`, opções reais com `serigyValue`; não limitar ao exemplo S. Conferir também a íntegra dos documentos do histórico. |
| 9.1: relação selecionada em ao menos um formato editável | `#exportar-contratos`; DT a implementar: CSV ou outro editável | 9.1.11 `salvarRelatorio` e `serigyValue` do formato efetivo; PDF sozinho não substitui o editável neste critério. |
| 9.1 e 9.2: informações mais recentes de até 30 dias da consulta | `#atualizacao-contratos` e `#atualizacao-documentos-contratos` | 9.1.12 `dataUltimaAtualizacao`, somente após preencher referências reais aplicáveis aos respectivos conjuntos |

A fonte deve esclarecer a referência temporal do período e do exercício (celebração, vigência ou outro recorte adotado), sem presumir que filtro e limites da vigência são o mesmo conceito. Não inventar datas para permitir filtros. Atualização/cobertura dos documentos precisa ser confirmada; atualização do resumo ou geração do HTML não prova atualização dos inteiros teores. Se contrato e aditivos tiverem coberturas distintas, explicitar as referências pertinentes na alimentação.

C 9.2 não lista gravação de relatórios própria; S 9.1.11 refere-se apenas a C 9.1. A exportação da relação deve manter os mínimos e a associação dos aditivos, sem multiplicar o valor do contrato por cada arquivo. Ela não substitui as íntegras dos contratos/termos nem exige transcrever documentos completos em CSV. Não publicar planilhas brutas privadas como derivado público.

Após implementar a busca, associar `#pesquisar-contratos` a `#resultados-contratos` por `serigyExecuteWaitSection` na ação e `serigyLoadSection` no resultado, com valor coincidente. A ação real de cada contrato deverá apontar para seu próprio detalhe, preservando a identidade; IDs são DT. Hoje não há ação de detalhe fictícia nem controle de consulta/exportação ativo. O título do exemplo S que menciona ordem cronológica não amplia este modelo para a consulta de pagamentos; as propriedades usadas aqui são exclusivamente da seção 9.1.

## Documentos e publicação futura

Receber arquivos oficiais ou URLs diretas confirmadas, inclusive as versões dos aditivos efetivamente celebrados. O WordPress pode ser o repositório oficial quando a correspondência for conferida. Não construir URL por número/ano, copiar os links ilustrativos S, usar `href="#"` ou `serigyLink` para PDF, nem substituir a íntegra por ementa ou capa genérica de portal.

Pendências em `controle/contratos-pendencias.md`. Antes de mover para `dist`: validar cadastro, valores, vigências, documentos e correspondências; conferir histórico e datas reais; alimentar resumo/documentos; implementar filtro de período, histórico, detalhe e gravação editável da relação; aplicar marcações só ao conteúdo real e testar recortes, extração, acesso e acessibilidade. O modelo vazio não comprova inexistência de contratos/aditivos ou atendimento aos critérios. Navegação pública só será ajustada em tarefa posterior de publicação autorizada.
