# Diárias — pendências para alimentação dos modelos

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
