# Contratos — modelos não publicados

Fontes da primeira etapa: **C**: Cartilha PETP 2026, critérios 9.1 (p. 75) e 9.2 (pp. 76–77, apenas a continuação do filtro). **S**: Serigy Docs, seção 9.1 Contratos, tabela da p. 1 e exemplos correspondentes da p. 2. **DT**: decisão técnica de apresentação/relacionamento, sem novo requisito normativo. Foram lidos `AGENTS.md` e o modelo de Licitações como referência visual. Esse recorte inicial trata do modelo principal; Fiscais e Ordem Cronológica são descritos no complemento abaixo.

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


## Complemento — Fiscais e Ordem Cronológica

Fontes deste complemento: `AGENTS.md`; C 9.3 (pp. 77–78) e 9.4 (pp. 78–80); S, seções 9.2 Fiscais e 9.3 Ordem Cronológica, tabelas da p. 1, exemplos correspondentes da p. 2 e atualização da p. 3. **C** é requisito da Cartilha, **S** é propriedade/tipo documentado, **DT** é escolha de implementação. O modelo principal de Contratos foi reutilizado apenas como referência visual e permanece inalterado.

| Seção S ↔ critério C | Novo modelo | Rota prevista |
| --- | --- | --- |
| S 9.2 Fiscais ↔ C 9.3 | `modelos/Portal-da-Transparencia/Contratos/GestoresFiscais/index.html` | `/Portal-da-Transparencia/Contratos/GestoresFiscais/` |
| S 9.3 Ordem Cronológica ↔ C 9.4 | `modelos/Portal-da-Transparencia/Contratos/OrdemCronologica/index.html` | `/Portal-da-Transparencia/Contratos/OrdemCronologica/` |

Caminhos literais de S após o prefixo do Portal. Ambos ficam fora de `dist`, sem novos links no menu/mapa/busca públicos. O schema `https://serigy.tce.se.gov.br/comum/contratos.html` está no `main`, mas nenhum item de dados, atualização ou controle inativo é marcado como disponível. Cabeçalhos e `tbody` vazios, listas sem documentos, campos desativados e reservas de atualização sem datas. Componentes gerais reais mantêm suas marcações existentes.

### Fiscais de Contratos — C 9.3 / S 9.2

**C:** relação nominal própria dos fiscais e dos contratos pelos quais respondem, abrangendo contratos vigentes e encerrados. Informação somente no detalhe de cada contrato não atende. **DT:** tabela HTML autônoma, uma associação fiscal–contrato por linha, sem repetir dados financeiros do contrato.

| Coluna de `#tabela-fiscais` | Origem | Item S futuro | Tipo literal S |
| --- | --- | --- | --- |
| Nome do fiscal | C 9.3 | 9.2.1 `fiscalGestor` | Texto |
| Contrato | C 9.3: indicação dos ajustes sob responsabilidade | 9.2.2 `contratoFiscal` | N/A |

`N/A` é o tipo literal documentado, não dispensa de mostrar o contrato nem inaplicabilidade à Previdência. Preservar sua identificação oficial e associação na mesma linha. S usa o nome fiscal/gestor, mas C exige fiscais; não substituir fiscais por gestores nem presumir equivalência de funções. Não acrescentar CPF, remuneração ou outros dados pessoais como mínimos.

| Controle / requisito C | Reserva / DT | S futuro |
| --- | --- | --- |
| Filtro específico genérico, sem parâmetros mínimos enumerados | `#filtro-fiscais`, `#ano-fiscais`, `#busca-fiscais` | 9.2.3 `filtroPesquisa`; exercício e busca por fiscal/contrato são DT de localização, não filtros mínimos novos de C. |
| Pelo menos os três anos anteriores ao da consulta | `#ano-fiscais` | 9.2.6 `historicoExercicio`, opções reais com `serigyValue`. Definir referência temporal com a fonte, sem eliminar encerrados. |
| Gravação da relação em ao menos um editável **ou PDF pesquisável**, alternativa expressa C p. 78 | `#exportar-fiscais` | 9.2.4 `salvarRelatorio`, `serigyValue` do formato efetivo; arquivo correspondente ao recorte. |
| Atualidade: dados mais recentes de até 30 dias | `#atualizacao-fiscais` | 9.2.5 `dataUltimaAtualizacao`, só com referência real preenchida, sem usar data de geração. |

C 9.3 não exige portaria de designação integral como anexo mínimo. A fonte/ato de designação pode apoiar a validação interna; não criar documento ou campo obrigatório fictício. Um vínculo para a consulta do contrato só será inserido se real e conferido, sem substituir a relação própria. Relações com vários fiscais ou mudanças de responsáveis exigem cobertura temporal confirmada, não inferida do contrato atual.

### Ordem Cronológica — C 9.4 / S 9.3

**C:** publicar mensalmente os créditos na ordem cronológica de pagamentos, observando fonte dos recursos e as categorias contratuais de fornecimento de bens, locações, prestação de serviços e obras, com justificativas de eventuais alterações (pp. 78–79). A exceção nominal ao Banese no ciclo não se estende à Previdência Estadual. **DT:** tabela própria organizada pelos grupos reais de fonte/categoria, preservando a ordem da origem validada; não gerar a ordem apenas ordenando datas de pagamento.

| Coluna de `#tabela-ordem` | Origem | Item S futuro | Tipo literal S |
| --- | --- | --- | --- |
| Fonte dos recursos | C 9.4: observar a fonte | Sem propriedade específica na seção S 9.3 | Não inventar item |
| Categoria contratual | C 9.4: as quatro categorias contratuais indicadas | Sem propriedade específica na seção S 9.3 | Não inventar item |
| Data de vencimento | C exemplifica identificação do crédito e define vencimento; S explicita o campo | 9.3.1 `dataVencimento` | Data |
| Data de pagamento | C exemplifica identificação do crédito; S explicita o campo | 9.3.2 `dataPagamento` | Data |
| Credor | C exemplifica identificação do crédito; S explicita o campo | 9.3.3 `credor` | Texto |
| Valor do pagamento | C exemplifica identificação do crédito; S explicita o campo | 9.3.4 `valorPagamento` | Monetário |
| Justificativa de alteração | C 9.4: fundamento da alteração eventual, vinculado ao crédito/grupo afetado | Sem propriedade específica na seção S 9.3 | Não inventar item |

As quatro medidas/identificações que S enumera não substituem fonte, categoria e justificativa exigidas por C. Não exigir novos códigos/classificações de outra dimensão como mínimos aqui. A posição das linhas deve preservar a ordem oficial dentro de cada grupo, sem comparar fontes distintas como uma fila única nem somar valores repetidos de listas mensais cumulativas.

**Vencimento:** C p. 78 o define como data a partir da qual o credor pode exigir legalmente o pagamento; menciona regulamentação local e, na ausência de definição, liquidação ou emissão da nota fiscal. Confirmar a regra/fato aplicável com a fonte; não escolher automaticamente uma das datas alternativas nem deduzi-la do arquivo. Esclarecer como representar créditos ainda não pagos, pagamentos parciais e alterações, se existentes, sem inventar data ou valor zero para completar células.

| Controle / requisito C | Reserva / DT | S futuro |
| --- | --- | --- |
| Filtro específico genérico, sem parâmetros mínimos enumerados | `#filtro-ordem`; `#ano-ordem`, `#mes-ordem`, `#fonte-ordem`, `#categoria-ordem` | 9.3.5 `filtroPesquisa`. Exercício, mês de referência e grupos são escolhas DT de consulta da publicação mensal, não mínimos enumerados de filtro C. |
| Pelo menos os três anos anteriores ao da consulta | `#ano-ordem` | 9.3.8 `historicoExercicio`, opções reais com `serigyValue`, sem limitar aos anos dos exemplos. |
| Gravação do conjunto selecionado em ao menos um formato editável | `#exportar-ordem` | 9.3.6 `salvarRelatorio` com `serigyValue` do formato real. PDF do exemplo genérico não substitui o editável em C 9.4. |
| Publicação mensal e atualidade de até 30 dias | `#atualizacao-ordem` | 9.3.7 `dataUltimaAtualizacao`, apenas após preencher referência real. Mês de referência, cobertura e atualização são informações distintas. |

**Justificativas/documentos:** C admite alterações fundamentadas pela autoridade responsável nas situações descritas nas pp. 78–79. A coluna reserva o conteúdo ou acesso ao fundamento real; `#justificativas-ordem`, `#identificacao-credito-ordem`, `#texto-justificativa-ordem` e `#documentos-justificativas-ordem` reservam detalhe textual e/ou documentos oficiais, se essa for a apresentação adotada. Vincular cada justificativa ao crédito e ao grupo efetivos, com identidade/IDs únicos quando houver vários registros. Não publicar lista global de arquivos sem associação, criar justificativas automáticas ou inferir que não houve alteração da ausência de documentos.

Não há obrigação de criar um PDF novo: texto explícito ou documento da justificativa depende da fonte. Quando houver documento, conferir íntegra, identificação e acesso direto; não gerar URLs por suposição nem usar `serigyLink` para PDF. A exportação editável deve preservar o recorte, fonte, categoria, ordem e fundamentos necessários, inclusive o conteúdo que esteja em detalhe, sem duplicar valores por documento ou por versões cumulativas. Não publicar planilha privada bruta.

### Ativação e publicação dos novos modelos

Aplicar os itens de dados às células reais, associando fiscal/contrato ou dados do mesmo crédito. Campos C sem propriedade S permanecem HTML legível, sem item inventado. Reservas de carregamento: `#pesquisar-fiscais` → `#resultados-fiscais` e `#pesquisar-ordem` → `#resultados-ordem`; após implementar, usar `serigyExecuteWaitSection` e `serigyLoadSection` com valor coincidente por consulta. IDs são DT, não nomes obrigatórios de S. Hoje os controles estão desativados e não anunciam funcionamento.

Receber as fontes, resolver as pendências do controle, conferir registros, documentos e cobertura histórica, alimentar referências reais e então implementar consultas/gravações e marcações. Não há declaração de inexistência ou atendimento. Só mover os modelos completos para `dist` em tarefa autorizada, com testes de recortes, arquivos, extração e acessibilidade; nenhuma navegação pública foi alterada nesta rodada.
