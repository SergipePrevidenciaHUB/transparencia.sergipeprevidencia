# Receitas previstas e arrecadadas — proposta mínima de entrada

## 1. Escopo e fontes

Desenho das entradas para o critério **3.1**, aplicável à Previdência Estadual, e para a futura alimentação de `dist/Portal-da-Transparencia/Receitas/PrevistaArrecada/index.html`. Não homologa valores, conceitos contábeis ou atendimento ao PETP. Nenhum arquivo de dados ou alteração na página acompanha este documento.

Fontes consultadas:

- `AGENTS.md`; somente a ficha de Receitas, 3.1, de `controle/inventario-tabelas.md`; página atual de receitas previstas e arrecadadas.
- **C — Cartilha:** `referencias/petp/Cartilha PETP 2026 Sergipe VERSÃO FINAL v2.pdf`, pp. 32–35, paginação impressa e do PDF coincidentes.
- **S — Serigy:** `referencias/serigy/3. Receitas _ Serigy Docs.pdf`, pp. 1–2, itens 3.1–3.6 e exemplos de filtros, resultados, exportação e atualização.
- **I — informação institucional fornecida pelo usuário nesta tarefa:** UOs 37201, 37401 e 37403; a arrecadação do SPSM é registrada na UO 37201, sem opção própria de SPSM em Receitas.
- **I — confirmação institucional desta revisão:** FUNPREV/37403 iniciou operações em junho de 2026 e tem previsão anual de receita de **R$ 0,00 em 2026**, pois não constou da LOA elaborada em 2025. Para 37201 e 37401, mantém-se a regra observada na planilha: previsão anual nas linhas de janeiro e arrecadação por mês. A regra específica está detalhada na seção 3.1; não é dedução dos exemplos Serigy.

**DT** identifica decisão técnica de preparação/relacionamento dos dados. C e S definem conteúdo ou funcionalidades de publicação; não fixam esses nomes de colunas, arquivos ou abas. A informação I não foi inferida dos dados fictícios ou dos exemplos normativos.

## 2. O que as fontes determinam

| Assunto | Determinação ou orientação | Fonte |
| --- | --- | --- |
| Conteúdo | Previsão e realização da receita/duodécimos, incluindo recursos extraordinários na receita realizada; as duas medidas na mesma página ou arquivo, permitindo comparação. | C, p. 32; S, p. 1, `valorPrevistoReceita` e `valorArrecadadoReceita`, ambos monetários. |
| Documentos substitutivos | A simples publicação do RGF ou da LOA não substitui as informações previstas e realizadas na mesma tela/documento. | C, p. 33. |
| Filtro mínimo | Período, por mês e ano, dentro do conjunto de receitas. | C, p. 35; S, p. 1, `filtroPesquisa`. |
| Atualidade | Intervalo de atualização não superior a 30 dias corridos anteriores à avaliação. O parâmetro PETP não dispensa a atualização contábil em tempo real mencionada na Cartilha. | C, p. 33; S 3.5, `dataUltimaAtualizacao`. |
| Particularidade da origem | A avaliação considera unidades com receitas próprias contínuas e unidades com repasses/duodécimos em datas fixas programadas. Isso não define qual é a origem concreta de cada valor desta instituição. | C, p. 33. |
| Histórico | Pelo menos os três anos anteriores à pesquisa; os anos do exemplo Serigy não limitam a série. Preservar também o exercício corrente disponível. | C, p. 34; S 3.6, `historicoExercicio`. |
| Exportação | Gravar o conjunto selecionado em pelo menos um formato editável. As extensões são exemplos, não obrigação de oferecer todas. Acesso estruturado automatizado aparece como sugestão. PDF isolado no exemplo S não elimina o editável exigido em C. | C, p. 34; S 3.4, `salvarRelatorio`. |

Os trechos consultados não definem chave de entrada, granularidade por lançamento ou mês, previsão inicial versus atualizada, valores líquidos versus brutos ou regras de consolidação entre UOs. A confirmação institucional da seção 3.1 esclarece como a previsão anual e a arrecadação mensal aparecem nesta entrada. A preparação do resumo continua sendo **DT condicionada à conciliação da fonte**, sem transformar a previsão anual em previsão mensal nem essas escolhas em exigências oficiais.

## 3. Unidades orçamentárias e futura consulta — I e DT

| `codigo_uo` | Nome exibido |
| --- | --- |
| `37201` | SergipePrevidência |
| `37401` | FINANPREV |
| `37403` | FUNPREV |

O código é texto; o nome exibido é obtido dessa correspondência, sem necessidade de repetir o nome como outra coluna da entrada mínima. Divergências de identificação na origem precisam de revisão, sem atribuição automática de registros a uma UO.

**Orientação institucional:** a arrecadação do SPSM já integra o registro na UO 37201. Não criar uma quarta opção SPSM, não introduzir a UO 37202 nesta entrada e não acrescentar ao total de 37201 uma cópia desses valores identificada separadamente como SPSM. A orientação não autoriza presumir valores, previsão própria ou rateio de componentes dentro de 37201.

**Filtro exigido versus seletor proposto:** mês e ano são o mínimo previsto em C. Oferecer um seletor de UO com as três unidades e **“Todas as unidades”** é uma **decisão técnica do projeto**, adicional ao filtro temporal. A tabela S de Receitas não documenta item de UO ou um `serigyItem` próprio para esse seletor. Não reutilizar um item do schema de Despesas para criar uma marcação inexistente em Receitas.

“Todas as unidades” exibirá os registros das três UOs no recorte de mês/ano, identificando **código e nome da UO em cada linha**, inclusive no relatório exportado. É um estado da consulta: não gravar `Todas` como código, nem adicionar uma linha financeira consolidada ao mesmo conjunto de linhas individuais.

Qualquer total deverá manter separados valor previsto e valor arrecadado e respeitar exercício, período, unidades selecionadas e a mesma base de comparação. Não somar consolidados aos componentes, meses a acumulados que já os incluem, versões sucessivas do mesmo valor ou uma cópia da arrecadação do SPSM ao registro de 37201. A opção conjunta não autoriza compensar ou eliminar repasses entre unidades sem regra contábil validada.

### 3.1. Previsão anual, arrecadação mensal e início do FUNPREV — I

- **SergipePrevidência/37201 e FINANPREV/37401:** a previsão anual aparece nas linhas de janeiro, detalhada pelas classificações da fonte. Nos meses seguintes, `Valor Previsto` permanece em `0,00`; `Valor Arrecadado` contém os valores de cada mês. Não repetir a previsão anual em cada mês nem dividi-la por doze. O zero dos meses posteriores não significa inexistência da previsão anual.
- **FUNPREV/37403 em 2026:** as operações começaram em **junho de 2026**. A previsão anual de receita é **R$ 0,00**, confirmada pela instituição, porque o fundo não constou da LOA elaborada em 2025. Esse zero é dado conhecido, não valor faltante, e não deve ficar pendente por ausência de janeiro. A ausência de linhas de janeiro a maio corresponde ao período anterior ao início das operações; não fabricar esses registros para representar a previsão anual zero.
- A arrecadação do FUNPREV deve ser registrada nos meses a que pertencem os valores informados, a partir do início das operações. Não antecipar ou distribuir esses valores pelos meses anteriores. A confirmação sobre a previsão de 2026 não permite presumir a previsão de exercícios posteriores.
- **DT de apresentação futura:** identificar explicitamente a previsão como anual e a arrecadação como mensal ou do recorte selecionado. Para 37201 e 37401, a referência anual vem das rubricas de janeiro, consideradas uma única vez por UO/ano após conciliação; consultar outro mês não transforma o zero dessa linha em previsão anual inexistente. Para FUNPREV/2026, a referência anual zero é a confirmação institucional, sem necessidade de criar janeiro. Não somar uma referência anual apresentada como contexto novamente aos registros de janeiro, nem comparar as medidas como se ambas fossem previsões/realizações mensais.

O início do FUNPREV e sua previsão de 2026 estão esclarecidos. Permanecem pendentes as alterações posteriores da previsão, a conferência dos valores arrecadados negativos, o tratamento das receitas intraorçamentárias e o fechamento de outubro de 2026.

## 4. Entrada lógica `receitas`

**DT de granularidade:** uma linha de resumo por UO, ano e mês, respeitando a diferença entre previsão anual e arrecadação mensal descrita na seção 3.1. Chave candidata: (`codigo_uo`, `ano`, `mes`). A chave identifica o resumo preparado para a página, não o lançamento contábil original. Não interpretar o `valor_previsto` desse registro como uma previsão mensal.

Quando a fonte trouxer várias naturezas, repasses ou classificações por competência, a agregação precisa ser definida e conciliada antes de gerar esse resumo. Preservar a previsão anual nas linhas de janeiro de 37201/37401 e os zeros posteriores; no resumo, considerar cada rubrica uma única vez. Para FUNPREV/2026, preservar o zero confirmado e os meses efetivamente informados desde junho. Não repetir, ratear ou fabricar previsão/movimentos. Uma eventual fonte futura de saldos acumulados exigirá revisão própria; a entrada aqui descrita registra arrecadação mensal, conforme a regra institucional.

| Coluna proposta | Tipo de entrada — DT | Origem do conteúdo e uso | Dependência de esclarecimento |
| --- | --- | --- | --- |
| `codigo_uo` | Texto | **I:** identifica uma das três UOs. **DT:** atribuição do registro, parte da chave e suporte ao seletor; sem item próprio em S Receitas. | Confirmar a identificação efetiva da UO na origem. A arrecadação SPSM permanece em 37201. |
| `ano` | Ano informado pela origem | **C, p. 35:** filtro de ano. **DT:** coluna e parte da chave do resumo. | Definir a referência fiscal/temporal usada pela instituição, sem inferir do nome do arquivo ou da data de importação. |
| `mes` | Mês informado pela origem | **C, p. 35:** filtro de mês. **DT:** coluna e granularidade do resumo. | Arrecadação por mês; em 37201/37401, janeiro também carrega a previsão anual. FUNPREV/2026 tem registros desde junho. Não derivar competência da publicação. |
| `valor_previsto` | Decimal monetário | **C, p. 32:** receita prevista; **S 3.1:** `valorPrevistoReceita`; **I:** regra da seção 3.1. Nome e armazenamento são **DT**. | 37201/37401: anual em janeiro e zero nos meses seguintes, sem repetição/rateio. FUNPREV/2026: previsão anual zero confirmada, não faltante. Continua pendente como alterações posteriores da previsão são registradas. Não converter outras ausências em zero por suposição. |
| `valor_arrecadado` | Decimal monetário | **C, p. 32:** receita realizada, incluindo recursos extraordinários; **S 3.2:** `valorArrecadadoReceita`; **I:** valores por mês. Nome e armazenamento são **DT**. | Preservar os valores nos meses informados. Permanecem pendentes competência contábil detalhada, abrangência, bruto/líquido, deduções, restituições e ajustes, inclusive valores negativos e receitas intraorçamentárias. |

Exemplo somente de cabeçalho, sem registros:

```csv
codigo_uo;ano;mes;valor_previsto;valor_arrecadado
```

**DT de transporte:** entrada em CSV UTF-8, com `;` no exemplo, ou aba de um futuro XLSX. Não há exigência de XLSX na Cartilha. Preservar códigos como texto e valores como números, sem símbolos monetários na entrada; formato decimal e representação do mês devem ser acordados com a origem antes do modelo. A interface poderá formatar os valores e apresentar o nome do mês sem alterar seu significado.

Duplicidade da chave candidata exige revisar se há reentrega, versão da previsão, abertura por natureza ou outra granularidade. Não somar automaticamente nem selecionar a última linha sem identificar a entrega válida. Guardar a rastreabilidade real da preparação é **DT a definir com a fonte**, sem inventar identificadores ou exigir novas colunas normativas nesta rodada.

## 5. Entrada lógica `metadados_receitas`

**DT:** separar as referências de atualização/cobertura dos valores financeiros. Uma linha por UO na entrega; chave candidata `codigo_uo`. Se a entrega tiver lotes com referências distintas, a granularidade desses metadados também precisará de revisão. Não criar uma linha `Todas` e não ocultar uma UO desatualizada usando a data mais recente de outra.

| Coluna proposta | Tipo de entrada — DT | Origem do conteúdo e uso | Dependência de esclarecimento |
| --- | --- | --- | --- |
| `codigo_uo` | Texto | **I + DT:** relacionar as referências ao conjunto `receitas` da unidade correspondente. | Mesma correspondência da seção 3; não representa uma nova propriedade Serigy. |
| `data_atualizacao` | Data real, proposta ISO `AAAA-MM-DD` | **C, p. 33:** atualidade; **S 3.5 e exemplo da p. 2:** `dataUltimaAtualizacao`. Coluna separada e formato são **DT**. | Confirmar a data de atualização efetiva do conjunto, sem substituí-la pelo dia de importar ou editar a página. |
| `dados_ate` | Data real, proposta ISO `AAAA-MM-DD` | **S, p. 2:** exemplo distingue atualização e dados até uma data. Armazenamento separado é **DT**; C não exige uma coluna com esse nome. | Cobertura real informada pela instituição. Não presumir fechamento no último dia do mês nem usar a maior data como prova de completude. |

Exemplo somente de cabeçalho, sem registros:

```csv
codigo_uo;data_atualizacao;dados_ate
```

Os dois conjuntos lógicos podem ser arquivos separados ou abas de uma entrega futura; essa separação é DT. A existência desses metadados não comprova a série histórica: os dados dos exercícios anteriores e suas referências precisam estar efetivamente disponíveis. Não criar meses/anos zerados para preencher lacunas, nem declaração automática de não ocorrência. No FUNPREV/2026, janeiro a maio são anteriores ao início das operações e não devem ser fabricados; isso não invalida a previsão anual zero confirmada. Atualização mensal da entrada não é, por si, garantia de cumprimento das regras contábeis de atualização. O fechamento e a cobertura de outubro de 2026 permanecem pendentes de confirmação, sem presumir mês encerrado.

## 6. Relação com a página e as marcações existentes

A página atual contém 12 registros expressamente fictícios, com mês, ano, previsto e arrecadado, filtros de mês/ano e downloads CSV/JSON de teste. Não há identificação por UO na tabela nem seletor correspondente. As opções de mês existentes são apenas janeiro a março, e os downloads estáticos não representam automaticamente o filtro aplicado. Essas condições foram observadas, sem alteração ou inferência de valores reais, cobertura ou semântica contábil a partir dos exemplos.

O layout proposto acrescenta a atribuição por UO aos quatro conceitos já exibidos; **não comprova compatibilidade com um importador existente**, que não foi alterado ou inspecionado para implementar este desenho. O seletor, a identificação por UO nas linhas, as opções temporais reais e a exportação do recorte dependerão de tarefa posterior.

Schema documentado: `https://serigy.tce.se.gov.br/comum/receitas.html`; caminho S: `[Portal da Transparencia]/Receitas/PrevistaArrecada`.

- Associar `valorPrevistoReceita` e `valorArrecadadoReceita` às medidas reais do registro, explicitando a referência anual da previsão e a mensal da arrecadação conforme a seção 3.1. O zero confirmado de previsão do FUNPREV/2026 não deve receber tratamento de informação ausente.
- `filtroPesquisa` marca a consulta funcional. O exemplo usa `historicoExercicio` no seletor de exercício e `serigyValue` nos anos; esses anos não limitam o histórico C. Os campos de mês/ano não recebem novos itens inventados.
- A ação `serigyExecuteWaitSection` e o contêiner `serigyLoadSection` precisam se corresponder quando usados. São estrutura de interface, não colunas financeiras de entrada.
- `salvarRelatorio` e `serigyValue` do formato devem corresponder ao arquivo funcional do conjunto selecionado. A entrada privada não é automaticamente o relatório público, e o PDF do exemplo S não substitui o editável C.
- `dataUltimaAtualizacao` deve apresentar datas reais. A separação de metadados por UO é DT; não criar atributos específicos para `codigo_uo`, `dados_ate` ou para o seletor de unidades.
- O exemplo S de `serigyEmpty` não autoriza fabricar ausência, zerar valores ou declarar não ocorrência. Nenhuma marcação ou hash foi inserido nesta tarefa.

## 7. Dúvidas a resolver com a instituição antes dos modelos

1. **Origem e abrangência dos valores:** qual exportação oficial fornece previsão e realização por UO? Contém receitas próprias, repasses, duodécimos e recursos extraordinários? Como confirmar completude sem incluir receitas de outra natureza ou duplicar fontes?
2. **Competência contábil:** a arrecadação é mensal, mas o mês/ano corresponde ao registro contábil, efetivo ingresso, repasse programado ou outro referencial? Há competências reabertas ou correções de exercícios anteriores? A previsão anual não deve ser interpretada como mensal para compará-la à arrecadação.
3. **Alterações da previsão:** para 37201/37401, está estabelecido o registro anual em janeiro; falta esclarecer se o valor ali apresentado é inicial ou atualizado e como alterações posteriores são identificadas. FUNPREV/2026 tem previsão anual zero confirmada: sua ausência na LOA elaborada em 2025 e o início em junho não são mais dúvidas. Não repetir nem ratear a previsão anual e não presumir regras para outros exercícios.
4. **Arrecadação negativa e ajustes:** permanece pendente a conferência dos valores arrecadados negativos identificados na planilha. Confirmar se os valores mensais são brutos ou líquidos e como entram restituições, deduções, estornos, reclassificações e receitas extraordinárias. Não descartar negativos, zerá-los ou criar critérios de reconhecimento por suposição.
5. **Ajustes e reentregas:** os arquivos substituem períodos anteriores ou acrescentam fatos novos? Como identificar a versão válida sem somar a mesma arrecadação ou previsão duas vezes? A regra de arrecadação mensal não resolve o tratamento de revisões e ajustes.
6. **Receitas intraorçamentárias e consolidação das UOs:** permanece pendente definir seu tratamento na apresentação e em eventual consolidação. Há repasses entre as três unidades ou totais consolidados junto dos componentes? Qual é o universo conciliável e quais regras oficiais se aplicam? O registro do SPSM na UO 37201 é orientação já fornecida; resta conferir que as entregas não acrescentem uma segunda cópia desses mesmos valores. Não inventar eliminações ou compensações.
7. **Fechamento de outubro de 2026 e referências de atualização:** confirmar se outubro está encerrado ou parcial e qual a data de cobertura por UO, além das referências e exercícios disponíveis. O início do FUNPREV em junho de 2026 está confirmado; a ausência de janeiro a maio não é falha a preencher. A particularidade C de repasses em datas fixas não autoriza presumir ausência de arrecadação nem dispensar atualização.

## 8. Limites desta entrega

Nesta revisão foi atualizado somente `controle/receitas-layout.md`, com a regra institucional sobre a previsão anual, o início do FUNPREV e o zero confirmado de 2026. Cabeçalhos preservados, sem linhas fictícias; nenhum CSV, XLSX, importador, dado existente ou arquivo de `dist` foi criado/alterado. As demais pendências contábeis indicadas acima permanecem abertas. A conferência desta entrega documental é `git diff --check`, sem declaração de validação financeira ou atendimento integral ao PETP.
