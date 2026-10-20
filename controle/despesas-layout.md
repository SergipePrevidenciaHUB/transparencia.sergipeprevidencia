# Despesas — proposta mínima de entrada (4.1, 4.2 e 4.3)

## 1. Escopo, fontes e grau de definição

Proposta de desenho, ainda dependente de confronto com a exportação contábil real. Não define um formato oficial PETP de entrada nem homologa dados ou atendimento. A página atual de Despesas contém somente seções editoriais e avisos de espera; este documento não a altera.

Fontes consultadas:

- `AGENTS.md`; fichas 4.1–4.3 de `controle/inventario-tabelas.md`; `controle/despesas-pendencias.md`; `dist/Portal-da-Transparencia/Despesas/index.html`.
- **C:** `referencias/petp/Cartilha PETP 2026 Sergipe VERSÃO FINAL v2.pdf`, somente pp. 36–41: disponibilidade, atualização, histórico, exportação e filtros de Despesas. Página do PDF e paginação impressa coincidem.
- **S:** `referencias/serigy/4. Despesas _ Serigy Docs.pdf`, pp. 1–2: tabela dos itens 4.1.1–4.1.19 e exemplos correspondentes. A p. 3 contém apenas a continuação da navegação do documento.
- **Decisão do projeto informada pelo usuário nesta revisão:** identificação das quatro UOs e futura consulta por unidade ou por todas as unidades. Os códigos e rótulos abaixo não foram deduzidos dos exemplos normativos.

Legenda de origem: **C** = conteúdo ou funcionalidade exigidos pela Cartilha; **S** = estrutura técnica documentada pelo Serigy; **DT** = decisão técnica proposta para nossa entrada. Uma informação exigida por C não torna obrigatório o nome de coluna, o arquivo ou a normalização propostos aqui. Os nomes de entrada não são nomes de atributos HTML.

## 2. O que as fontes determinam

Todos os três critérios são aplicáveis à Previdência Estadual.

| Critério | Conteúdo mínimo | Filtros mínimos | Fonte |
| --- | --- | --- | --- |
| 4.1 | Totais empenhado, liquidado e pago no período, consolidados ou obtidos do detalhamento; comparáveis em uma página/arquivo. | Exercício (ano), mês ou período. | C, pp. 36–37. |
| 4.2 | Unidade orçamentária, função, subfunção, natureza (categoria econômica, grupo e elemento) e fonte dos recursos, com códigos e descrições por extenso. Detalhe acessível na mesma seção; exportação com o conteúdo mínimo completo. | Exercício (ano), mês ou período e elemento de despesa. | C, pp. 38–40. |
| 4.3 | Lista de empenhos e detalhe individual: credor, valor (título do critério; S 4.1.19), objeto, modalidade e número do procedimento. Para contratação direta, número da dispensa/inexigibilidade ou fundamentação na hipótese de pequena monta descrita na Cartilha. Identificação do procedimento a partir da despesa; essa exigência recai sobre despesas licitáveis. | Número do empenho, nome e CPF ou CNPJ do credor, mês e exercício (ano). | C, pp. 40–41; S, pp. 1–2. |

Regras comuns expressas em C, pp. 37, 39 e 41:

- Atualização com intervalo não superior a 30 dias corridos anteriores à avaliação. O parâmetro PETP não dispensa a atualização contábil em tempo real mencionada expressamente nas pp. 37 e 39.
- Histórico de pelo menos três anos que antecedem a pesquisa; não limitar o acervo aos anos ilustrativos do Serigy nem excluir o exercício corrente disponível.
- Gravar o conjunto selecionado em pelo menos um formato editável. As extensões citadas são exemplos; não há obrigação de disponibilizar todas. PDF isolado não substitui esse requisito. Acesso estruturado automatizado aparece como sugestão nesses trechos.
- As fontes não fixam os arquivos/abas de entrada, sua chave, granularidade de movimentos ou nomes de colunas. Tampouco impõem uma tabela HTML única para os três critérios.

## 3. Organização proposta — DT, sujeita às dúvidas da seção 8

Dois conjuntos de dados relacionados e um conjunto pequeno de metadados de publicação:

| Entrada lógica | Uma linha representa | Uso |
| --- | --- | --- |
| `empenhos` | Um empenho de uma UO, identificado de forma estável, com credor, valor individual, objeto, contratação e classificação. | Conteúdo de 4.2 e 4.3; referência comum para os movimentos. Pressupõe classificação única por empenho, a confirmar. |
| `movimentos` | Um movimento contábil real, de uma UO, uma etapa e um empenho, no exercício/mês fornecidos pela origem. | Valores e recortes de 4.1; associação à classificação de 4.2 e à consulta de 4.3. Não é uma linha por fotografia de saldo acumulado. |
| `metadados` | A referência real de atualização/cobertura de cada conjunto entregue para uma UO. | Informação de atualização compartilhada por 4.1–4.3, sem ocultar diferenças entre unidades; não é uma transação financeira. |

**DT de transporte:** cada entrada pode ser um CSV UTF-8 separado ou uma aba de um futuro XLSX. Os exemplos abaixo usam `;` como separador. Nenhum desses arquivos foi criado. Não se exige XLSX como entrada nem publicação da planilha interna. Tipos, nomes, separação dos conjuntos e convenções de transporte são propostas técnicas.

Não é necessário digitar outro conjunto de totais de 4.1 ou outra cópia da execução para 4.2: os totais podem resultar dos movimentos, e a classificação pode vir da relação com os empenhos, conforme permitido por C. Essa reutilização depende de conciliação e de cobertura real da fonte; não se presume que toda exportação contábil já tenha essa granularidade.

### 3.1. Identificação das unidades e opção de consulta — decisão do projeto

`codigo_uo` identifica a unidade orçamentária à qual o registro pertence. Proposta de tipo: texto, preservando o código informado pela origem. Para o escopo definido nesta revisão, a correspondência com o nome exibido é:

| `codigo_uo` | Nome exibido |
| --- | --- |
| `37201` | SergipePrevidência |
| `37202` | SPSM |
| `37401` | FINANPREV |
| `37403` | FUNPREV |

Os rótulos de consulta acima foram fornecidos pelo usuário. A descrição orçamentária por extenso continua sendo informação de origem em `unidade_orcamentaria_descricao`; não inventar a expansão de siglas nem substituir a descrição oficial por um rótulo abreviado. Código e descrição recebidos devem identificar a mesma UO. Divergência, código ausente ou fora do escopo exige revisão; não atribuir automaticamente à UO 37201.

**Exigência documentada:** C 4.2 prevê a unidade orçamentária na classificação; S 4.1.4 documenta `unidadeDespesa` como campo de conteúdo. **DT de interface:** oferecer um seletor por UO, além dos filtros já exigidos, com as quatro opções e “Todas as unidades”. Os trechos consultados não estabelecem esse seletor como filtro mínimo nem criam um `serigyItem` chamado `codigo_uo` ou um item específico para esse seletor. O nome da coluna é DT; a identificação da UO em Despesas é conteúdo documentado.

Na futura opção **“Todas as unidades”**, serão exibidos os registros das quatro UOs no recorte selecionado, com **código e nome da unidade identificados em cada linha** e preservados na exportação. Essa opção é um estado da consulta, não uma UO adicional: não inserir `Todas` como `codigo_uo` nem criar registros consolidados junto dos registros individuais.

Qualquer total deverá respeitar **exercício, mês/período e etapa da despesa**, além do conjunto de UOs selecionado. Empenhado, liquidado e pago permanecem medidas distintas. Não somar um total consolidado novamente aos seus componentes por UO, misturar totais de períodos sobrepostos, repetir o valor integral do empenho após junções ou contar reentregas como movimentos novos. A identificação por UO evita colisões entre chaves locais, mas não resolve a semântica contábil: movimentos, saldos, ajustes e eventuais relações entre UOs continuam dependentes da conciliação e dos esclarecimentos da seção 8. Não presumir regras de compensação ou eliminação entre unidades.

## 4. Entrada `empenhos`

**Chave proposta:** (`codigo_uo`, `id_empenho`) — DT. Preferir o identificador estável da origem, com unicidade validada dentro da UO ao longo dos exercícios. Se ele não existir, a composição de uma chave precisa ser validada com a área, considerando exercício e unidade pertinente; número isolado não é presumido único. A chave interna não vira uma nova coluna obrigatória da consulta pública.

Os campos de classificação têm conteúdo obrigatório em C, mas a divisão em duas colunas, código e descrição, é **DT** para evitar interpretação de texto e permitir agrupamentos. Não criar classificações ou completar códigos por suposição.

| Coluna proposta | Tipo de entrada — DT | Origem e uso | Condição ou esclarecimento |
| --- | --- | --- | --- |
| `id_empenho` | Texto | **DT:** parte da chave com `codigo_uo`, para relacionar movimentos sem depender de nomes/valores. | Validar identidade e unicidade por UO na origem, inclusive entre exercícios. |
| `numero_empenho` | Texto | **C 4.3, p. 41:** filtro por número. Sem item próprio na tabela S. | Preservar identificação e ano, quando integrantes do número original; não usar como chave isolada. |
| `credor_nome` | Texto | **C 4.3, pp. 40–41:** identificação e filtro; **S 4.1.11:** `credorEmpenho`. | Nome/razão social oficial, sem deduzir do documento. |
| `credor_cpf_cnpj` | Texto | **C 4.3, p. 41:** filtro por CPF ou CNPJ. Sem item próprio em S. | Preservar zeros; forma pública e tratamento do CPF dependem de validação institucional, sem definir máscara por suposição. |
| `valor_empenho` | Decimal monetário | **C 4.3**, valor referido no título; **S 4.1.19:** `valorEmpenhoIndividual`. | Confirmar valor original ou atualizado/líquido e sua referência. Não substituir por valor pago. |
| `objeto` | Texto | **C 4.3, p. 40; S 4.1.12:** `objetoEmpenho`. | Bem fornecido ou serviço prestado, conforme a fonte. |
| `modalidade_contratacao` | Texto | **C 4.3, p. 40; S 4.1.13:** `modalidadeEmpenho`. | Modalidade, dispensa ou inexigibilidade quando pertinentes; não atribuir a despesas não licitáveis. |
| `procedimento_ou_fundamentacao` | Texto | **C 4.3, p. 40; S 4.1.14:** `numeroProcedimento`. A coluna única é **DT**, seguindo as alternativas documentadas. | Número/ano do procedimento ou fundamentação na hipótese de pequena monta prevista em C. Não exigir simultaneamente número e fundamentação para todos. Ver conflito de tipo em S na seção 8. |
| `codigo_uo` | Texto | **C 4.2, p. 38; S 4.1.4:** conteúdo de `unidadeDespesa`; nome e uso como chave **DT**. | Substitui o nome proposto anteriormente, `unidade_orcamentaria_codigo`, sem duplicar a coluna. Identificar a UO real conforme seção 3.1. |
| `unidade_orcamentaria_descricao` | Texto | **C 4.2, p. 38; S 4.1.4:** conteúdo de `unidadeDespesa`; separação **DT**. | Denominação por extenso. |
| `funcao_codigo` | Texto | **C 4.2, p. 38; S 4.1.5:** `funcaoDespesa`; separação **DT**. | Código oficial. |
| `funcao_descricao` | Texto | **C 4.2, p. 38; S 4.1.5:** `funcaoDespesa`; separação **DT**. | Descrição por extenso. |
| `subfuncao_codigo` | Texto | **C 4.2, p. 38; S 4.1.6:** `subFuncaoDespesa`; separação **DT**. | Código oficial. |
| `subfuncao_descricao` | Texto | **C 4.2, p. 38; S 4.1.6:** `subFuncaoDespesa`; separação **DT**. | Descrição por extenso. |
| `categoria_economica_codigo` | Texto | **C 4.2, p. 38; S 4.1.7:** `categoriaDespesa`; separação **DT**. | Código oficial. |
| `categoria_economica_descricao` | Texto | **C 4.2, p. 38; S 4.1.7:** `categoriaDespesa`; separação **DT**. | Descrição por extenso. |
| `grupo_despesa_codigo` | Texto | **C 4.2, p. 38; S 4.1.8:** `grupoDespesa`; separação **DT**. | Código oficial. |
| `grupo_despesa_descricao` | Texto | **C 4.2, p. 38; S 4.1.8:** `grupoDespesa`; separação **DT**. | Descrição por extenso. |
| `elemento_despesa_codigo` | Texto | **C 4.2, pp. 38 e 40:** conteúdo e filtro; **S 4.1.9:** `elementoDespesa`; separação **DT**. | Código oficial; filtro usa a classificação real. |
| `elemento_despesa_descricao` | Texto | **C 4.2, p. 38; S 4.1.9:** `elementoDespesa`; separação **DT**. | Descrição por extenso, inclusive no relatório exportado. |
| `fonte_recursos_codigo` | Texto | **C 4.2, p. 38; S 4.1.10:** `fonteRecursosDespesa`; separação **DT**. | Código oficial. |
| `fonte_recursos_descricao` | Texto | **C 4.2, p. 38; S 4.1.10:** `fonteRecursosDespesa`; separação **DT**. | Descrição por extenso. |

Exemplo somente de cabeçalho:

```csv
id_empenho;numero_empenho;credor_nome;credor_cpf_cnpj;valor_empenho;objeto;modalidade_contratacao;procedimento_ou_fundamentacao;codigo_uo;unidade_orcamentaria_descricao;funcao_codigo;funcao_descricao;subfuncao_codigo;subfuncao_descricao;categoria_economica_codigo;categoria_economica_descricao;grupo_despesa_codigo;grupo_despesa_descricao;elemento_despesa_codigo;elemento_despesa_descricao;fonte_recursos_codigo;fonte_recursos_descricao
```

Não se propõem como mínimos anexos de nota fiscal, cópia integral de processo, datas de liquidação/pagamento individuais ou novas colunas jurídicas: esses conteúdos não são exigidos como colunas nos trechos consultados. A identificação do procedimento precisa permanecer acessível a partir da despesa. Uma futura navegação por vínculo pode resolver esse acesso por identificadores reais; não inventar URLs na entrada.

## 5. Entrada `movimentos`

Este é o desenho mínimo **condicionado à disponibilidade de movimentos**, coerente com a proposta M03 do inventário. A Cartilha permite dados consolidados e não obriga esse livro de eventos. Se a origem só fornecer saldos acumulados ou totais sem relação com os empenhos, interromper a definição desse layout e revisar o desenho; não fabricar eventos, chaves, datas ou rateios para encaixá-la.

**DT de relacionamento:** a identidade do movimento é (`codigo_uo`, `id_movimento`), com unicidade temporal a confirmar na origem. A referência ao cadastro é (`codigo_uo`, `id_empenho`); exigir coerência de UO nos dois lados da associação. Identificadores iguais de UOs diferentes não são automaticamente o mesmo registro. Um eventual evento entre unidades não pode ser modelado ou compensado por suposição.

| Coluna proposta | Tipo de entrada — DT | Origem e uso | Condição ou esclarecimento |
| --- | --- | --- | --- |
| `codigo_uo` | Texto | **DT de atribuição e relacionamento:** manter a UO do movimento, reutilizando a identificação orçamentária prevista em C 4.2/S 4.1.4. | Mesma UO do empenho referenciado; valores conforme seção 3.1. Não é um novo item Serigy. |
| `id_movimento` | Texto | **DT:** identificar o fato e impedir duplicação em reentregas. | Preferir chave da origem; composição depende de validação, sem deduplicar somente por valor e mês. |
| `id_empenho` | Texto | **DT:** referência ao registro de `empenhos` junto de `codigo_uo`, para classificação e credor. | Mesma chave do cadastro e mesma UO; não relacionar por semelhança. |
| `exercicio` | Ano informado pela origem | **C 4.1–4.3**, filtros de exercício; **DT:** representação em coluna do recorte da execução. | Não confundir exercício do movimento com ano do empenho original. Referência de 4.3 ainda precisa de confirmação. |
| `mes` | Mês informado pela origem | **C 4.1–4.3**, filtros de mês/período; **DT:** representação em coluna. | Não inventar dia de registro a partir de um fechamento mensal. |
| `etapa` | Texto controlado | **DT:** forma longa de separar os três estágios de **C 4.1**, pp. 36–37. | Distinguir empenho, liquidação e pagamento; mapear eventos de origem e ajustes antes de usar. Não é novo `serigyItem`. |
| `valor_movimento` | Decimal monetário | **C 4.1**, valores por estágio; armazenamento longo **DT**. Totais resultantes correspondem a **S 4.1.1–4.1.3**. | Valor do movimento, com sinal/ajuste conforme conceito contábil confirmado. Nunca saldo cumulativo repetido nem valor integral do empenho em toda etapa. |

Exemplo somente de cabeçalho:

```csv
codigo_uo;id_movimento;id_empenho;exercicio;mes;etapa;valor_movimento
```

**DT de apresentação:** obter os três totais por exercício/mês ou intervalo de meses a partir de `etapa` e `valor_movimento`, respeitando a UO ou as UOs selecionadas e os cuidados da seção 3.1; associar cada movimento à classificação para 4.2. Não é necessário armazenar as mesmas medidas novamente em três colunas de uma base de totais manual. O modelo mensal de filtro proposto não significa que atualização mensal seja suficiente ou que a fonte esteja dispensada da atualização exigida.

Para 4.3, a proposta provisória é selecionar os empenhos relacionados aos movimentos do período, apresentando cada empenho uma vez por sua identidade (`codigo_uo`, `id_empenho`), com seu detalhe e identificação da unidade. **A Cartilha não esclarece nesses trechos se o mês/ano desse filtro deve corresponder à emissão do empenho ou à execução financeira. Essa decisão permanece aberta.** Se a referência for emissão, a origem deverá fornecer essa competência, e o layout precisará ser revisto antes de criar o modelo. Não deduzir o mês do número do empenho nem converter ausência de movimento em inexistência do empenho.

O `valor_empenho` é atributo individual de 4.3; não o somar depois de uma junção que produza várias linhas por empenho. Totais de 4.1 vêm dos movimentos conciliados. Pagamentos referentes a empenhos de exercícios anteriores exigem preservar a identidade original e a competência real do movimento.

## 6. Entrada `metadados`

Separação **DT** para não repetir datas em cada registro nem confundir atualização editorial/importação com referência dos dados. Não substitui o histórico financeiro. Uma linha por conjunto e UO entregues; se houver lotes com referências diferentes, a granularidade dos metadados deve acompanhar a entrega real, sem divulgar só a data mais recente e ocultar partes ou unidades desatualizadas. Na consulta “Todas as unidades”, preservar as referências de cada UO, sem atribuir uma atualização comum sem comprovação. Não criar uma linha com UO `Todas`.

| Coluna proposta | Tipo de entrada — DT | Origem e uso | Condição ou esclarecimento |
| --- | --- | --- | --- |
| `conjunto` | Texto | **DT:** associar a referência ao conjunto de entrada. | Identificação de `empenhos` ou `movimentos`, conforme entrega; não é propriedade Serigy. |
| `codigo_uo` | Texto | **DT:** atribuir atualização e cobertura ao conjunto da respectiva UO. | Correspondência da seção 3.1; chave mínima de referência (`conjunto`, `codigo_uo`), a detalhar se houver lotes distintos. |
| `data_atualizacao` | Data real, proposta ISO `AAAA-MM-DD` | **C**, atualidade; **S 4.1.17**, `dataUltimaAtualizacao`, e exemplo da p. 2. Coluna separada **DT**. | Confirmar com a fonte o significado da data de atualização do conjunto. Não preencher automaticamente com o dia da importação ou da edição do site. |
| `dados_ate` | Data real, proposta ISO `AAAA-MM-DD` | **S**, p. 2: exemplo distingue atualização e dados até determinada data. Armazenamento separado **DT**; C não cria essa coluna nominal. | Cobertura real informada pela origem; não presumir último dia do mês nem usar a maior data como prova de completude. |

Exemplo somente de cabeçalho:

```csv
conjunto;codigo_uo;data_atualizacao;dados_ate
```

Manter o acervo efetivo dos exercícios anteriores e suas referências, sem sobrescrever o histórico por uma fotografia atual. O formato de arquivo/particionamento por exercício é **DT a definir com a origem**, não uma coluna normativa adicional. Competências sem registros e períodos sem fonte precisam de esclarecimento institucional; não gerar linhas zeradas ou declaração automática de não ocorrência.

## 7. Marcações e saída pública — não são colunas de entrada

Schema confirmado em S, p. 1: `https://serigy.tce.se.gov.br/comum/despesas.html`; caminho documentado: `[Portal da Transparencia]/Despesas`.

- `valorEmpenhado`, `valorLiquidado` e `valorPago` marcam os valores reais dos totais resultantes; `valorEmpenhoIndividual` identifica o valor individual do empenho. Não marcar todo movimento bruto como se fosse o total consolidado da consulta.
- Os itens de classificação e detalhe listados na seção 4 devem permanecer associados ao registro correspondente. Código e descrição podem compor o mesmo conteúdo marcado; dividir as colunas de entrada não cria novos atributos.
- `unidadeDespesa` é o item de conteúdo de unidade orçamentária documentado em S 4.1.4. A coluna `codigo_uo`, sua repetição nas entradas para relacionamento e o seletor por UO são decisões de desenho; não inventar marcação específica para o seletor nem tratar “Todas as unidades” como uma unidade orçamentária.
- `filtroPesquisa` marca o controle real. O exemplo usa `historicoExercicio` no seletor e `serigyValue` nos exercícios; seus anos ilustrativos não limitam o histórico exigido por C.
- A ação `serigyExecuteWaitSection` e o contêiner `serigyLoadSection` devem se corresponder quando utilizados, como nos exemplos de resultados e detalhes. Não são chaves financeiras nem colunas do arquivo.
- `salvarRelatorio` e `serigyValue` do formato referem-se à exportação funcional do recorte selecionado. O relatório precisa conservar campos acessíveis no detalhe, inclusive os de 4.2; a planilha interna normalizada não é automaticamente esse relatório público.
- `dataUltimaAtualizacao` marca referências reais apresentadas ao usuário; não decorre do simples carregamento do arquivo. Não há item próprio para as chaves internas, número do empenho, CPF/CNPJ ou `etapa` na tabela consultada.
- A página atual permanece sem dados e sem novos itens de Despesas. Este desenho não autoriza marcar títulos/avisos como valores, criar `serigyItem` ou inserir hash.

## 8. Esclarecimentos necessários antes dos modelos

1. **Granularidade da fonte:** eventos ou saldos? Como identificar anulações, estornos, reforços e reentregas sem duplicar os três totais? Se só houver dados consolidados, como obter classificação e ligação aos empenhos? O layout de movimentos não está homologado sem essa resposta.
2. **Cardinalidade:** há uma classificação, um credor e um procedimento por empenho? Se houver vários itens, classificações, fontes ou procedimentos, a estrutura deverá ser desdobrada por chaves reais antes da criação dos modelos, sem repetir valor integral nem ratear por suposição.
3. **Identidade e tempo:** qual chave estável distingue empenhos entre unidades/exercícios e movimentos entre reentregas? `codigo_uo` passa a integrar as relações propostas, mas não resolve repetições internas à mesma UO nem a granularidade contábil. Qual evento determina exercício/mês do filtro de 4.3? A referência fiscal é sempre a mesma do mês calendário informado? Não impor essa equivalência sem confirmação.
4. **Valor individual:** o valor de 4.3 é original, atualizado ou líquido após ajustes, e em qual referência? C e S consultados não resolvem essa semântica contábil. Não confundir esse valor com total pago ou total de movimentos.
5. **Procedimento/fundamentação:** S 4.1.14 tipa `numeroProcedimento` como numérico, mas inclui fundamentação na descrição e exemplifica número/ano na p. 2. **DT proposta:** texto na entrada para preservar o conteúdo; **DÚVIDA — REVISÃO NECESSÁRIA:** confirmar a representação de fundamentação no contexto marcado. Não reduzir o dado a número puro nem inventar atributo alternativo.
6. **Número e CPF/CNPJ:** C exige os filtros; S não define itens próprios. Confirmar a implementação técnica da consulta e a forma pública de identificação, mantendo a entrada interna distinta da exportação pública quando necessário. Não inventar regra de mascaramento ou expor automaticamente a origem bruta.
7. **Cobertura e atualização:** confirmar referências de cada entrega, universo contábil, competências abrangidas e série disponível, inclusive a relação entre execução atual e empenhos anteriores. A existência de chaves e datas não prova completude ou atualidade.
8. **Consulta conjunta das UOs:** confirmar como a origem distingue fatos, reentregas, saldos e eventuais relações entre unidades antes de qualquer total conjunto. Os quatro códigos e a opção “Todas as unidades” não definem regras de consolidação, compensação ou eliminação contábil, nem autorizam misturar registros agregados e detalhados do mesmo fato.

## 9. Limites desta entrega

Nesta revisão foi alterado somente este documento, para identificar as quatro UOs nas entradas e descrever a consulta por unidade ou por todas elas. Os cabeçalhos são exemplos sem registros. Não foram criados CSV, XLSX, tabelas HTML ou importadores; não houve mudança em Receitas, `dist` nem em outros controles. A definição final da entrada depende da fonte institucional e dos esclarecimentos acima. A conferência aplicável a esta entrega documental é `git diff --check`; não se trata de validação dos dados ou do atendimento PETP.
