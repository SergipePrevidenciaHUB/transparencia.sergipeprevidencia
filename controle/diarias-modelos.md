# Diárias — modelos não publicados

**C**: Cartilha PETP 2026, critérios 7.1 (pp. 61–62) e 7.2 (pp. 62–63), aplicáveis à Previdência Estadual. **S**: seção 7 do Serigy Docs, pp. 1–2. **DT**: escolha técnica de estrutura, sem criar exigência normativa. Foram lidos `AGENTS.md` e somente as fichas 7.1–7.2 do inventário; o modelo de Terceirizados foi usado apenas para o visual e componentes comuns.

## Caminhos e isolamento

| Critério C / seção S | Modelo versionável | Rota prevista |
| --- | --- | --- |
| 7.1 / 7.1 Relação de Diárias | `modelos/Portal-da-Transparencia/Diarias/Relacao/index.html` | `/Portal-da-Transparencia/Diarias/Relacao/` |
| 7.2 / 7.2 Valores Diária | `modelos/Portal-da-Transparencia/Diarias/TabelaValores/index.html` | `/Portal-da-Transparencia/Diarias/TabelaValores/` |

Os segmentos após o prefixo do Portal são os literais de S. Ambos os modelos ficam fora de `dist`, origem publicada pelo preparador existente; não recebem entrada no menu, mapa ou manifesto públicos. Cabeçalho, rodapé, navegação e acessibilidade são reutilizados sem alterar outros arquivos. O schema confirmado está no `main`: `https://serigy.tce.se.gov.br/comum/diarias.html`.

As tabelas têm somente cabeçalhos e `tbody` vazio, sem linhas fictícias. Controles estão desativados, reservas de atualização estão vazias e sem `serigyItem`. Nenhum dado, link documental ou declaração de não ocorrência/vigência foi inventado. As marcações dos componentes gerais reais foram preservadas; as de dados abaixo são instruções de aplicação futura, não marcações sobre campos vazios.

## Relação de Diárias — 7.1

DT: tabela HTML, com todos os mínimos visíveis na mesma linha por afastamento/concessão, em seção própria. C admite detalhes complementares, mas exige todos os campos na exportação e não aceita apenas a consulta de despesas como substituta desta seção. Não é obrigação C anexar autorizações ou comprovantes individuais.

| Coluna de `#tabela-relacao-diarias` | Exigência C p. 61 | Item S / `serigyItem` futuro | Tipo S |
| --- | --- | --- | --- |
| Nome completo do beneficiário | Nome de quem recebeu | 7.1.1 `nomeBeneficiario` | Texto |
| Cargo/função | Cargo ou função do beneficiário | 7.1.2 `cargoBeneficiario` | Texto |
| Número de diárias | Quantidade utilizada por afastamento; não é número da portaria | 7.1.3 `numeroDiaria` | Numérico |
| Início do afastamento | Data inicial | 7.1.4 `dataInicioAfastamento` | Data |
| Fim do afastamento | Data final | 7.1.5 `dataFimAfastamento` | Data |
| Motivo do afastamento | Finalidade | 7.1.6 `motivoAfastamento` | Texto |
| Destino (cidade) | Local com identificação do nome da cidade | 7.1.7 `localDestino` | Texto |
| Valor total recebido | Total efetivamente informado pela fonte | 7.1.8 `valorTotal` | Monetário |

| Controle / requisito C p. 62 | Reserva | S / ativação futura |
| --- | --- | --- |
| Filtro mínimo: nome, mês e ano | `#filtro-relacao-diarias`; campos `#nome-relacao-diarias`, `#mes-relacao-diarias`, `#ano-relacao-diarias` | 7.1.11 `filtroPesquisa` no formulário funcional. Não criar itens para mês/nome do formulário sem documentação. |
| Pelo menos os três anos anteriores ao da consulta | `#ano-relacao-diarias` | 7.1.10 `historicoExercicio`, opções reais com `serigyValue`; os anos do exemplo S não limitam o acervo. |
| Exportar conjunto selecionado em pelo menos um formato editável, com todos os mínimos | `#exportar-relacao-diarias` | 7.1.12 `salvarRelatorio`, `serigyValue` do formato efetivo. DT a implementar: CSV ou outro editável. O PDF exemplificado em S não substitui o editável exigido por C 7.1. |
| Atualidade: dados mais recentes de até 30 dias da consulta | `#atualizacao-relacao-diarias` | 7.1.9 `dataUltimaAtualizacao`, somente após receber e preencher a referência real; não usar a data de geração do HTML. |

A origem precisa definir qual fato/data determina o mês/ano da consulta, sem presumir pagamento, início do afastamento ou concessão. Preservar o valor recebido e a quantidade reais; não calcular total automaticamente a partir da tabela normativa. Múltiplos pagamentos/ajustes relativos ao mesmo afastamento exigem regra da fonte para evitar contagem repetida; não foi criada solução contábil nem totalizador.

## Valores das Diárias — 7.2

C exige tabela ou relação dos valores previstos para dentro do Estado, fora do Estado e fora do país; aceita a tabela da própria normativa, desde que localizada na seção específica de diárias. DT: tabela HTML com reserva para norma e vigência, sem exigir transcrição de toda a lei ou PDF novo.

| Coluna de `#tabela-valores-diarias` | Origem | Item S / `serigyItem` futuro | Tipo S |
| --- | --- | --- | --- |
| Faixa de aplicação, conforme a norma | DT: associar valores às condições/faixas que a fonte efetivamente estabelecer | Sem item específico documentado; não inventar propriedade | Texto de contexto, se aplicável |
| Dentro do Estado | C 7.2 | 7.2.1 `valorEstadual` | Monetário |
| Fora do Estado (Brasil) | C 7.2; S denomina nacional | 7.2.2 `valorNacional` | Monetário |
| Fora do país | C 7.2 | 7.2.3 `valorInternacional` | Monetário |

A coluna de faixa não impõe cargos, classes ou novos valores: só será preenchida com condições reais da norma; se a tabela for uniforme e não tiver faixas, ajustar essa apresentação na alimentação, sem fabricar categoria. Identificar moeda, unidade e condições conforme a fonte; não copiar reais/dólares ou cifras dos exemplos S nem converter valores por suposição.

| Controle / requisito C p. 63 | Reserva | S / ativação futura |
| --- | --- | --- |
| Filtro específico, sem parâmetros mínimos enumerados | `#filtro-valores-diarias`, `#ano-valores-diarias` | 7.2.6 `filtroPesquisa`. DT: exercício para selecionar versões/valores aplicáveis, não filtro mínimo nominalmente exigido por C. |
| Pelo menos os três anos anteriores ao da consulta | `#ano-valores-diarias` | 7.2.5 `historicoExercicio`, opções com exercícios reais e `serigyValue`. Uma norma pode vigorar por vários anos: vincular ao período real sem inventar revisões anuais. |
| Atualidade: até um ano; se a tabela foi atualizada há mais tempo, informar expressamente que é a versão mais recente e continua vigente | `#atualizacao-valores-diarias` e `#vigencia-valores-diarias` | 7.2.4 `dataUltimaAtualizacao` apenas na data real; declaração de vigência depende de confirmação e não deve ser marcada como se fosse data. |

**Sem gravação de relatórios autônoma em C 7.2 e sem `salvarRelatorio` na tabela S 7.2.** Não há botão de exportação no modelo. Acesso a uma norma/tabela oficial em `#normas-valores-diarias` é documental, não nova obrigação de exportação editável.

Se não houver previsão legal de diárias internacionais, C pp. 62–63 exige informar isso expressamente. A reserva `#previsao-internacional-diarias` só receberá texto após confirmação da legislação; não preencher internacional com zero, data ou traço marcado como valor monetário. Não presumir ausência de previsão da simples falta de documento.

## Marcação e liberação futura

Aplicar os itens de dados às células reais, mantendo a associação por afastamento (7.1) ou faixa/versão da norma (7.2). Reserva de carregamento: `#pesquisar-relacao-diarias` → `#resultados-relacao-diarias`; `#pesquisar-valores-diarias` → `#resultados-valores-diarias`. Usar `serigyExecuteWaitSection` na ação e `serigyLoadSection` no resultado com valor coincidente por consulta; IDs são DT, não nomes obrigatórios dos exemplos. Hoje não há ação funcional anunciada.

Documentos/URLs oficiais só entram após conferência de correspondência, íntegra e acesso público. Não criar caminhos por suposição nem usar `serigyLink` para PDF. Uma declaração de inexistência de pagamentos em 7.1 depende de confirmação institucional e referência de cobertura; não foi gerada a partir de tabela vazia.

Antes de publicar, atender às pendências de `controle/diarias-pendencias.md`, alimentar e conferir dados/documentos, histórico e atualização, implementar filtros e somente a exportação aplicável, aplicar marcações nos valores existentes e testar os recortes. Depois, em tarefa autorizada, mover as páginas completas para `dist` e ajustar navegação. Modelo vazio não comprova atendimento.
