# Diárias — pendências para alimentação dos modelos

## Complemento atual — Relação de Diárias com dados reais (7.1)

A descrição inicial abaixo é histórica. A rota de Relação passa a usar os 208 registros da aba Plan1 de `DIARIAS_CONSOLIDADAS_2023_2026.xlsx`, com os oito campos mínimos disponíveis em colunas próprias. CSV e consulta correspondem à mesma base. Não se altera 7.2 nem se declara conformidade integral.

| Pendência concreta | Evidência | Providência e tratamento atual |
| --- | --- | --- |
| Data inicial inválida | **Plan1!G13 = `30/03/20213`**; H13 = 31/03/2023; referência = MARÇO/2023 | Confirmar saída com a instituição. Não corrigir para 2023 por dedução. Literal preservado no HTML e CSV; apenas esse campo não recebe `dataInicioAfastamento`. Demais campos e registros continuam implementados. |
| Precisão monetária | **Plan1!J7 = 25.003**, número com três casas decimais | Confirmar se o terceiro decimal é intencional. Preservado exatamente: HTML R$ 25,003 e CSV 25,003. Não arredondar para R$ 25,00 nem interpretar como 25 mil. |
| Natureza da referência | ANO/MÊS presentes; todas as saídas válidas coincidem com esses períodos | Filtros usam as colunas explícitas, identificadas como referência da planilha. Confirmar se representam afastamento, concessão ou outro fato; não afirmar mês de pagamento. |
| Atualização institucional | A planilha não contém data real de atualização dos dados | Solicitar referência e responsável. Não usar modificação do XLSX (21/10/2026), geração do HTML ou último afastamento como `dataUltimaAtualizacao`. Não declarar a exigência de atualidade atendida. |
| Completude e granularidade | 2023: 54; 2024: 40; 2025: 72; 2026: 42; janeiro/2023–setembro/2026; todos PAGO | Confirmar cobertura, eventuais ajustes/devoluções/pagamentos posteriores e se cada linha é concessão/afastamento completo. Não inventar outubro–dezembro/2026, não deduplicar por nome/data/evento e não declarar não ocorrência para meses ausentes. |

Conferência inicial dos valores subjacentes, antes de arredondamento: 2023 = 41025.003; 2024 = 35450.00; 2025 = 75925.00; 2026 = 55300.00. A precisão especial de J7 é mantida nesses totais de conciliação; não são totalizadores novos na interface. Fonte SHA-256: `4db9b1e2f06bb4e1111192067021cb831952e39ad7b9fc1c24c743f5a42d152d` (integridade do arquivo, não hash do Invoker).

As pendências não interrompem os demais campos. A interface traz explicação factual da referência e da precisão, sem avisos internos de validação, datas presumidas ou declarações de atendimento. Campos ausentes/invalidamente tipados não recebem marcação de dado disponível. Os modelos originais e a página de Valores das Diárias permanecem preservados.

Escopo: C 7.1–7.2 e S7. Correspondência em `controle/diarias-modelos.md`. Pendências são internas; os modelos não contêm avisos de revisão, dados fictícios ou declarações de atendimento.

## Diarias/Relacao — C 7.1

| Requisito | Dado/arquivo faltante | Providência |
| --- | --- | --- |
| Beneficiário e afastamento | Relação oficial com nome completo, cargo/função, número de diárias, início/fim, motivo, cidade de destino e valor total recebido | Receber fonte validada pela área responsável, com cobertura identificada. Não usar autorizações genéricas ou dados de despesas como substituição automática da relação específica. |
| Granularidade e valores | Identificação confiável do afastamento/concessão e tratamento de ajustes, devoluções ou vários pagamentos, se existentes | Confirmar a composição de cada registro com a fonte. Preservar quantidades/valores; não deduzir total multiplicando tabela de referência nem duplicar o afastamento em cada movimento. Não impor campo extra público como obrigação. |
| Filtro nome/mês/ano | Referência temporal que define mês e ano; períodos realmente disponíveis | Confirmar qual data governa a consulta. Implementar filtros combináveis sobre a relação sem inventar competências ou preencher meses ausentes. |
| Histórico | Acervo de pelo menos três anos anteriores ao da consulta | Conferir cobertura; se não houve pagamentos, obter confirmação e período pertinente para informação expressa, sem tratar falta de arquivo como não ocorrência. |
| Gravação | Arquivo editável correspondente ao recorte, com os oito campos mínimos | Implementar pelo menos um formato editável; PDF do exemplo S não basta para 7.1. Preservar mínimos mesmo se houver detalhes complementares. |
| Atualidade | Data real da informação, cobertura e responsável | Confirmar referência de até 30 dias; não preencher automaticamente com a data de geração. |
| Dados adicionais da fonte | Derivado público restrito ao conteúdo necessário | Não publicar CPF, conta bancária, documentos pessoais ou planilha bruta por conveniência. Autorizações/comprovantes não são anexos mínimos autônomos em 7.1. |

## Diarias/TabelaValores — C 7.2

| Requisito | Dado/documento faltante | Providência |
| --- | --- | --- |
| Valores legais | Norma/tabela oficial vigente com valores dentro do Estado, fora do Estado e fora do país, nas faixas e moedas reais | Obter conteúdo e conferir valores e condições. Não copiar exemplo S, presumir faixas/cargos, converter moeda ou inventar valores. |
| Faixas de aplicação | Condições, unidades e categorias efetivamente previstas na norma | Identificar cada valor sem misturar faixas. A coluna contextual do modelo é DT e deve ser ajustada se a norma não estabelecer faixas. |
| Previsão internacional | Confirmação do regime legal para viagens ao exterior | Se inexistente, obter fundamento para informação expressa exigida por C; não apresentar zero como se houvesse valor legal nem marcar texto de ausência como monetário. |
| Normas e vigências | Versões, períodos de validade e arquivos ou URLs oficiais conferidas | Associar a tabela à norma correta. Não deduzir vigência pelo nome do arquivo ou criar URLs. Documento da norma é aceito se a tabela estiver localizável nesta seção. |
| Histórico e filtro | Valores/normas aplicáveis a pelo menos três anos anteriores à consulta | Mapear períodos e mudanças; uma mesma norma pode cobrir vários anos sem revisão. Implementar o seletor de exercício proposto como DT, sem transformá-lo em filtro mínimo enumerado pela Cartilha. |
| Atualidade | Data real da tabela e confirmação de que continua sendo a versão mais recente e vigente, quando mais antiga que um ano | Obter confirmação antes de exibir vigência; não alterar artificialmente a data. Manter data de atualização separada do texto de vigência. |
| Exportação | Nenhuma gravação autônoma exigida em C 7.2 / S 7.2 | Não criar botão ou promessa de exportação por copiar o outro modelo. Acesso à norma deve funcionar quando fornecido. |

## Condição de publicação

Os dois modelos permanecem fora de `dist`. Para liberar cada página: receber e validar suas fontes; resolver as referências temporais e normativas; preencher tabelas/documentos e datas reais; ativar controles e marcações somente quando funcionais; testar recortes, links e acessibilidade. Não há consulta ou exportação implementada nesta rodada, nem declaração de atendimento ao PETP. Nenhuma comunicação externa ou solicitação à instituição foi enviada.


## Valores das Diárias — pendências após alimentação de C 7.2

A planilha forneceu 48 linhas para 2023–2026 e as observações forneceram o fundamento e a URL. A consulta foi alimentada; permanecem estas conferências institucionais, sem presumir sua conclusão:

- **Alterações posteriores ao Decreto nº 239/2023:** solicitar à área responsável a conferência institucional de eventuais normas posteriores, alterações do Anexo I e respectivas datas de vigência. Confirmar que os valores fornecidos para cada exercício correspondem às versões efetivamente aplicáveis. O PDF e a planilha não comprovam isoladamente que não houve alterações posteriores. Registrar a resposta/documentos antes de declarar tabela vigente no exercício atual.
- **Cobertura temporal:** confirmar os períodos de aplicação, especialmente a transição normativa em janeiro/2023. O exercício na planilha não foi convertido em data de início ou término de vigência. Se houver outras versões, obtê-las e associá-las ao período real sem substituir a história silenciosamente.
- **Data de atualização:** obter referência institucional real do conjunto antes de marcar `dataUltimaAtualizacao`; não utilizar data da importação, da consulta ao PDF ou do decreto como atualização dos dados.
- **Sinal “-”:** mantido literalmente para o grupo I dentro do Estado, em quatro linhas, sem converter para zero ou atribuir marcação monetária. Eventual explicação jurídica do sinal depende de confirmação, não de dedução.
- **Moedas e limites:** internacionais são valores de referência em € ou US$ conforme destino. Não converter em reais nem extrapolar a tabela para cálculo de concessões, cotação, período ou pagamento sem fontes próprias. A observação interestadual foi preservada; não criar novas exceções.
- **Fundamento:** usar Decreto nº 239/2023 / Anexo I na página pública. Não apresentar Decretos 40.743/2020 e 30.956/2018 das observações como fundamento vigente desta tabela. A frase genérica da origem sobre pleno vigor/última versão não foi promovida a declaração pública.
- **Serigy:** conferir posteriormente a extração dos dois valores estaduais por faixa e o contexto das moedas internacionais. Não se declara atendimento integral ou homologação a partir da conferência local.

Fontes preservadas. Nenhuma alteração na Relação de Diárias ou em dados/páginas de outras dimensões.


## Conferência pontual Serigy — atualização pública de Diárias

Consultados somente os itens S7 7.1.9 (Relação) e 7.2.4 (Valores) e o exemplo correspondente de `dataUltimaAtualizacao`. Ambos usam `https://serigy.tce.se.gov.br/comum/diarias.html`; a informação de atualização fica no contêiner marcado, sob esse schema. As páginas `Diarias/Relacao/index.html` e `Diarias/TabelaValores/index.html` receberam “Informações atualizadas em 21/10/2026”, com data ISO no elemento `time`. A referência foi fornecida para atualização das páginas no Portal, não é emissão dos documentos, data de afastamento, competência, início de vigência da tabela ou prova de ausência de alterações normativas posteriores. A pendência anterior de obter referência da atualização pública foi resolvida somente nesse sentido.

**Relação — existentes e preservadas:** filtros/histórico, gravação CSV e associação entre pesquisa/resultados; 208 nomes `nomeBeneficiario`, cargos `cargoBeneficiario`, destinos `localDestino`, motivos `motivoAfastamento`, fins `dataFimAfastamento`, quantidades `numeroDiaria` e totais `valorTotal`; 207 inícios `dataInicioAfastamento`. O início da linha 13 da origem (`30/03/20213`) permanece literal e sem marcação de data válida. Não corrigir seu ano por dedução. Os três decimais de Plan1!J7 (`25.003`, exibido R$ 25,003) permanecem, com a pendência monetária já documentada. Situação e período da fonte são complementares; não foram inventados itens para eles.

**Valores — existentes e preservadas:** `filtroPesquisa`, `historicoExercicio`, ação/resultados e 24 valores `valorEstadual` (dois por faixa com/sem pernoite), 16 `valorNacional` e 16 `valorInternacional`. Quatro sinais “-” estaduais do grupo I continuam sem marcação monetária; internacionais mantêm contexto € / US$, sem prefixo R$. Grupo e cargo não receberam propriedades inventadas. Nenhuma outra falta inequívoca pequena foi identificada nesses campos publicados. Não foi criada exportação autônoma para 7.2.

**Pendências que continuam:** corrigir a data inicial inválida mediante fonte institucional, conferir a precisão de J7, conteúdo e pesquisa de texto documental, vigência da tabela e eventuais alterações posteriores ao Decreto nº 239/2023. A atualização da página não encerra essas conferências nem declara atualidade material/atendimento integral.

**Regeneração/testes fora desta rodada:** somente os dois HTMLs e este controle foram ajustados. Geradores e testes anteriores que ainda pressupõem ausência de `dataUltimaAtualizacao` precisam ter essas expectativas e a preservação da referência fornecida revistos em tarefa própria. Não foram alterados ou executados nesta correção; o validador do projeto foi executado. Não substituir a referência por data automática de importação.
