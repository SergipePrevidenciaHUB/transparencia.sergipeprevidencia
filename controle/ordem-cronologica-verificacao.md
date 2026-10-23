# Ordem cronológica — preparação dos dados

Preparação em 23/10/2026. Data autorizada para atualização da página: **22/10/2026**. Cartilha PETP 2026: critério **9.4**; Serigy: módulo **9.3**. Situação: **implementação local parcial**; 464 pagamentos integrados ao portal a partir do JSON preparado, sem novo cruzamento das planilhas. Reconhecimento das marcações ainda depende de nova avaliação autorizada do Invoker.

## Fontes e integridade

Foram utilizados pagamentos.xlsx, liquidacao.xlsx e base-conhecimento-elemento.xlsx, aba Plan1. Os hashes SHA-256 estão na aba Fontes e no JSON preparado. Todos os dados pertencem à UG 372011; estes arquivos não comprovam cobertura de FINANPREV ou FUNPREV.

A origem de pagamentos tem 19.078 linhas após o cabeçalho: três cabeçalhos repetidos foram retirados, restando **19.075 OBs únicas**. A origem de liquidações contém **4.507 LEs únicas**. Não houve exclusão silenciosa de pagamento válido. O rastreio conserva uma linha por pagamento e sua linha de origem. Bruto menos retenções corresponde ao líquido em todos os pagamentos; bruto menos estornos corresponde ao líquido em todas as liquidações.

| Resultado exclusivo | Pagamentos |
|---|---:|
| Preparados para integração | 464 |
| Categoria identificada, cruzamento de liquidação pendente | 874 |
| Classificação pendente | 12.683 |
| Fora das quatro categorias contratuais nesta preparação | 4.644 |
| Pagamento não concluído | 410 |
| Total preservado | 19.075 |

Existem **12.342 pagamentos sem empenho e natureza** na origem. Não foi preenchido para baixo nem herdado o conteúdo de linhas vizinhas. A relação detalhada de pendências contratuais tem 1.462 registros com natureza disponível; ela é um subconjunto das pendências, não a relação integral. As demais OBs permanecem localizáveis no rastreio geral e no arquivo original, pela linha de origem.

## Critério e estrutura

A Cartilha exige, pelo menos, vencimento, pagamento, credor e valor; organização por fonte e pelas quatro categorias; atualização mensal, dados recentes, histórico de três exercícios anteriores, filtro e exportação editável. Exige também justificativas das alterações de ordem, quando ocorridas.

A Cartilha permite usar liquidação ou emissão da nota fiscal como vencimento **na ausência de definição específica na regulamentação local**. A data de liquidação foi adotada como referência conforme solicitado. A existência de definição local permanece para conferência; não se afirmou que liquidação é sempre o vencimento legal.

A fonte de recursos foi preservada, com CO em coluna separada. A ordenação é UG, fonte, categoria, vencimento, pagamento e OB. CO não foi transformado automaticamente em uma fila contratual separada. Não foi fabricado um número de posição oficial na fila.

O histórico preparado cobre pagamentos de 2023 a 2026. A origem completa vai de 06/01/2023 a 22/10/2026; o subconjunto conciliado vai até **15/10/2026**. A data de atualização da página não comprova fechamento contábil nem completude desses períodos.

## Classificação

| Categoria com data conciliada | Quantidade |
|---|---:|
| Fornecimento de bens | 82 |
| Locações | 4 |
| Prestação de serviços | 378 |
| Obras | 0 |

Por exercício: 2023 = 152; 2024 = 112; 2025 = 111; 2026 = 89.

O código de natureza de oito dígitos foi preservado; os seis primeiros foram consultados no dicionário. Materiais e equipamentos foram classificados como bens; obras e instalações, como obras quando identificadas; consultoria e TI, como serviços. **Locação de mão de obra é serviço, não locação de bens.** Elementos genéricos de serviços exigiram apoio da observação do pagamento; menções ambíguas de locação, reforma ou nome de fornecedor ficaram pendentes. Despesas de exercícios anteriores não receberam a categoria do sufixo do subitem.

Pessoal, benefícios, encargos, diárias, tributos e outras naturezas sem contratação comprovada não foram incluídos automaticamente nas quatro categorias. Os enquadramentos são regras de preparação, passíveis de revisão pelo contrato/objeto; não são parecer jurídico. A ausência de obras no subconjunto preparado não comprova inexistência de obras nas pendências.

## Cruzamento de pagamentos e liquidações

Chave usada: **UG + empenho completo com exercício + fonte|CO + natureza de oito dígitos + documento completo do credor**, este último somente durante o processamento restrito.

As origens não trazem vínculo explícito de cada OB à sua LE. As datas foram reconstruídas de forma conservadora: candidata única com valor coincidente; pagamento parcial com única liquidação na chave; ou candidatas de valor coincidente com a mesma data. Neste último caso, que ocorre em um pagamento preparado, a data é unívoca, mas a LE específica não foi atribuída. Os IDs candidatos estão no rastreio de conciliação da planilha.

Comparou-se o **bruto do pagamento** ao saldo líquido da liquidação após estornos. Não se confundiu o líquido após retenções do pagamento com o líquido após estornos da liquidação. Capacidades compartilhadas foram conferidas pelos vínculos candidatos, em centavos, sem consumir repetidamente o mesmo saldo. Dois pagamentos com conflito foram devolvidos às pendências. Não foi escolhida arbitrariamente a liquidação mais recente nem criado rateio FIFO.

Os 874 cruzamentos pendentes compreendem: 759 valores divergentes ou várias liquidações sem vínculo explícito; 99 valores iguais em datas diferentes; dois conflitos de capacidade; uma liquidação posterior ou estornada; 13 chaves sem liquidação. As associações reconstruídas precisam de conferência com documento que vincule OB à LE para comprovação administrativa definitiva.

## Ordem e justificativas

O resultado é um **histórico parcial de pagamentos efetuados com referência de vencimento conciliada**. Os três arquivos não fornecem a fila oficial integral dos créditos, inclusive os ainda não pagos, nem justificativas assinadas de alteração da ordem. Não é possível concluir atendimento integral à Cartilha apenas ordenando estes pagamentos.

Foram separados dez sinais para revisão interna: pagamento posterior de crédito com referência anterior a outro já pago, dentro da mesma fonte e categoria do subconjunto. São indícios limitados pela cobertura, não constatação de irregularidade. Não foram publicadas acusações nem inventadas justificativas ou declaração de ausência de inversões.

## Privacidade

CPFs foram mascarados antes da geração dos arquivos de saída. Observações livres, domicílios e contas bancárias não integram o pacote. O rastreio geral não inclui nomes ou documentos dos credores. O XLSX contém abas internas de conferência: **não copiar esse arquivo integral para dist nem oferecê-lo como download público**. Para o portal, usar somente o JSON público preparado e o CSV do recorte. O tratamento não transforma os registros em dados anônimos.

## Matriz de implementação

| Exigência | Dados preparados / providência |
|---|---|
| Vencimento, pagamento, credor e valor | 464 registros; referência de vencimento reconstruída conforme regras acima |
| Fonte e quatro categorias | Fonte e CO preservados; três categorias com registros conciliados, Obras sem registro comprovado |
| Histórico | Há registros em 2023/2024/2025/2026; cobertura integral ainda não comprovada |
| Atualização | Página autorizada em 22/10/2026; último pagamento conciliado em 15/10/2026 |
| Filtros e exportação | Consulta HTML, cinco filtros combináveis, limpeza, três totais separados e CSV do recorte implementados e testados localmente e na cópia Pages |
| Justificativas de alteração | Não fornecidas; obter quando existentes e aplicáveis |
| Fila integral e regularidade da ordem | Não comprovadas por estas três origens |
| Reconhecimento do Serigy | Oito itens implementados e conferidos localmente; depende de futura avaliação autorizada, sem alterar os resultados históricos |

Fonte técnica: https://serigy.tce.se.gov.br/petp/comum/contratos.html. Schema: https://serigy.tce.se.gov.br/comum/contratos.html. Marcações: dataVencimento, dataPagamento, credor, valorPagamento, filtroPesquisa, salvarRelatorio, dataUltimaAtualizacao e historicoExercicio. Não inventar atributos específicos para fonte, categoria ou justificativa.

## Complementações prioritárias

1. Exportação/documento que vincule explicitamente cada OB à LE correspondente, inclusive pagamentos agrupados/parciais e retenções.
2. Empenho, natureza e objeto dos pagamentos sem detalhamento; contrato e fundamento de enquadramento dos casos ambíguos.
3. Relação oficial dos créditos a pagar, inclusive os não pagos, por fonte e categoria; definição local da data de vencimento.
4. Justificativas oficiais de eventuais alterações, com os respectivos documentos e datas, quando aplicáveis.
5. Confirmação da cobertura institucional e de cada exercício, sem presumir que a UG 372011 abrange todos os fundos.

## Integração da consulta pública — 23/10/2026

- Fonte exclusiva: `dados-entrada/contratos/ordem-cronologica-preparada.json`; não foram refeitos cruzamentos. Importador `tools/integrar_ordem_cronologica.py`, conferência `--check`; teste `tools/testar_ordem_cronologica.py`.
- 464 registros no HTML inicial, sem duplicação por OB: 2023 = 152, 2024 = 112, 2025 = 111, 2026 = 89. Categorias: bens = 82, locações = 4, serviços = 378; Obras permanece como opção de consulta sem registros preparados, sem declaração de inexistência institucional.
- Ordenação UG, fonte, categoria, vencimento, pagamento e OB, preservando CO separadamente. Os 13 campos públicos do HTML e do CSV reproduzem a fonte: UG, vencimento (liquidação), pagamento, credor, líquido, fonte, categoria, bruto, retenções, CO, OB, empenho e documento mascarado do credor. Sem posição oficial de fila, observações livres, dados bancários ou planilhas internas.
- Totais independentes da base: líquido **R$ 5.790.001,01**, bruto **R$ 5.805.615,51**, retenções **R$ 15.614,50**. Bruto e líquido não foram somados entre si. Valores tratados em centavos; datas e máscaras preservadas.
- Histórico 2026/2025/2024/2023 com `value`/`serigyValue`; seleção, pesquisa e resultados associados a `ordemTabela`. Filtros combináveis por exercício, mês de pagamento, fonte, categoria e nome. CSV somente com pagamentos do recorte, sem duplicar totais.
- Data de atualização da página **22/10/2026**, autorizada pelo responsável, fora da tabela filtrada. Os quatro campos de dados e os quatro controles Serigy estão sob o schema de Contratos. Nenhum atributo de fonte/categoria foi inventado.
- Ensaios deste módulo removidos da página. `preparar_teste_ordem.py` recusa ativação e desativação sobre a base real; sua antiga entrada de teste agora confere os dados reais. O mecanismo global de bloqueio sintético foi preservado e testado em cópia isolada; os demais módulos não foram alterados.
- Conferências: contagens, 13 campos de todas as linhas, datas/valores, máscaras, oito itens, geração estável, um filtro combinado, quatro exercícios, Obras sem resultado, limpeza, CSV integral/filtrado e totais. Rotas, recursos e marcações conferidos por HTTP e Chrome em localhost e na cópia exata com base `/transparencia.sergipeprevidencia`. Sem publicação ou execução do Invoker.

Não restaram marcadores de ensaio ativo nos HTML/CSV/JSON de `dist` após esta substituição. O bloqueio do preparador continua rejeitando sintéticos para publicação oficial, conforme teste em fixture isolada. O teste legado de Despesas foi ajustado somente para conferir esse bloqueio em fixture, sem exigir que um ensaio permaneça na versão publicável; a conciliação dos dados de Despesas foi preservada.

Permanecem **pendências de conteúdo/comprovação**, sem correção por suposição: cobertura dos fundos e dos períodos; vínculo administrativo OB–LE; definição local de vencimento; fila integral dos créditos ainda não pagos; classificação dos registros pendentes e justificativas oficiais de alterações quando aplicáveis. A consulta não comprova completude institucional ou regularidade da ordem apenas por estar ordenada. O XLSX e os registros pendentes continuam fora da projeção pública.
