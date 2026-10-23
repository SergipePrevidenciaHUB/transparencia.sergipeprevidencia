# Receitas — pendências de conferência

**Pendências de conferência que não impedem o prosseguimento**, registradas por orientação do projeto para avaliação posterior pela instituição. Os valores devem ser preservados, inclusive os negativos e as receitas intraorçamentárias, sem correção, descarte ou compensação presumida. Este registro não homologa os conceitos contábeis nem declara atendimento ao PETP.

Referências: `controle/receitas-layout.md` e a prévia local `trabalho/receitas-previa/conferencia.json`, gerada de `dados-entrada/receitas/receitas-teste.xlsx`. O resumo conciliou 425 linhas em 97 grupos mensais e nove grupos UO/ano, com diferenças zero entre os agrupamentos e as linhas de origem. Essa conferência aritmética não resolve as dúvidas contábeis abaixo. A pasta `trabalho/` é local e ignorada pelo Git; não constitui fonte versionada.

## Arrecadações negativas — FINANPREV, UO 37401, exercício 2023

| Competência | Valor arrecadado | Referência na origem |
| --- | ---: | --- |
| Junho/2023 | −R$ 340,76 | `Planilha1!M25` |
| Julho/2023 | −R$ 28.930.331,12 | `Planilha1!M30` |
| Novembro/2023 | −R$ 2.855,09 | `Planilha1!M47` |

Confirmar com a contabilidade a natureza e a competência desses valores, inclusive eventual relação com restituições, deduções, estornos ou reclassificações. Essas hipóteses são perguntas, não causas identificadas. Manter os valores e seus sinais na arrecadação mensal enquanto a conferência estiver pendente; não zerar, inverter o sinal ou excluir os registros.

## Demais questões para avaliação posterior

| Assunto | Conferência pendente | Tratamento durante o prosseguimento |
| --- | --- | --- |
| Receitas intraorçamentárias | Confirmar abrangência, apresentação e eventuais regras oficiais de eliminação em uma futura consolidação. O resumo identifica 98 linhas intraorçamentárias preservadas. | Manter todas as linhas e suas classificações. Não gerar total consolidado entre UOs nem eliminar ou compensar valores por suposição. |
| Alterações da previsão | Confirmar se a previsão anual de janeiro de 37201/37401 é inicial ou atualizada e como identificar alterações posteriores e reentregas, evitando duplicação. | Considerar as rubricas de janeiro uma única vez por UO/ano, sem repetir ou dividir a previsão pelos meses. Preservar a previsão anual de R$ 0,00 do FUNPREV/2026, já confirmada pela instituição, e apenas os meses existentes desde junho. |
| Fechamento de outubro/2026 | Confirmar se o mês está encerrado ou parcial e as datas reais de cobertura e atualização por UO. | Preservar os registros existentes sem presumir fechamento mensal ou completude; não fabricar meses ou usar a data da geração da prévia como atualização contábil. |

Nenhum valor foi corrigido ou descartado neste registro. A planilha de origem e os arquivos de `dist` não foram alterados.


## Esclarecimento institucional sobre a origem e os avisos públicos

A instituição confirmou nesta solicitação que os 425 registros de `dados-entrada/receitas/receitas-teste.xlsx` são dados reais do SergipePrevidência. O nome do arquivo identificava o primeiro teste de importação; não caracteriza dados fictícios. Retirar da interface os rótulos de teste sem declarar homologação contábil, fechamento ou completude. As pendências acima continuam de conferência e não impedem o prosseguimento.

Preservar a indicação de soma bruta entre UOs, incluindo receitas intraorçamentárias, e as explicações da previsão anual e arrecadação acumulada. A confirmação da origem não altera as dúvidas de negativos, revisão da previsão, intraorçamentárias e fechamento de outubro/2026. Datas reais de atualização e cobertura ainda precisam ser fornecidas; não usar a data de geração do HTML.

**Pendência técnica fora desta rodada:** atualizar o metadado `aviso` nos JSONs e os textos de teste em `tools/integrar_receitas.py`, sem alterar valores. Nesta revisão restrita a HTML/controles, o JSON externo e o incorporado permanecem idênticos, preservando exportações e a conciliação do teste existente. A exportação JSON ainda reproduz esse rótulo antigo. As instruções de revisão deixam a interface e permanecem neste controle e em `controle/avisos-interface-pendencias.md`.


## Conferência pontual Serigy — atualização pública de Receitas

Consultados somente a definição S3 item 3.5 (C 3.1) e seu exemplo de `dataUltimaAtualizacao`. O exemplo envolve a marcação em `https://serigy.tce.se.gov.br/comum/receitas.html`, no próprio contêiner que apresenta a informação de atualização. A página `Receitas/PrevistaArrecada/index.html` recebeu “Informações atualizadas em 21/10/2026”, com esse contexto e item, e elemento `time` com data ISO. A referência foi informada pelo responsável para atualização da página no Portal, não deduzida da geração do HTML, da competência, de emissão documental ou de fechamento contábil.

**Marcações já existentes e preservadas:** `filtroPesquisa`, `historicoExercicio`, `salvarRelatorio` (CSV/JSON), associação pesquisa/resultados e campos `valorPrevistoReceita`/`valorArrecadadoReceita` nos totais e no detalhamento de Espécie. Na inspeção estática inicial, há 51 valores previstos marcados e 61 arrecadados marcados (incluindo um total de cada); as 110 células monetárias do nível Espécie estão marcadas. Ausências de previsão representadas por “—” não foram convertidas em valores ou marcadas como dinheiro.

**Agregados da hierarquia — revisão técnica pendente:** 46 células monetárias de Categoria Econômica e 97 de Origem (143 ao todo) não têm item monetário, enquanto repetem agregações dos mesmos registros detalhados e dos totais. Não foi promovida uma correção em massa: confirmar a estratégia de leitura Serigy desses níveis antes de marcar novamente seus valores e induzir dupla contagem semântica. Não se afirma que todo agregado de apresentação exige um novo registro marcado. Não foram criadas propriedades Serigy para UO, códigos ou descrições sem item documentado.

**Limites preservados:** a data de atualização da página não resolve negativos, intraorçamentárias, alterações da previsão, cobertura por UO ou fechamento de outubro/2026; permanecem as pendências anteriores. A marcação não homologa o conjunto nem altera previsão anual, acumulados, competências, cálculos ou exportações.

**Regeneração/testes fora desta rodada:** o escopo foi limitado ao HTML e a este controle. O gerador e os testes não foram alterados; revisar numa tarefa própria as expectativas/geração que ainda reservam a data como comentário, para preservar a referência real sem preenchê-la automaticamente com o dia da importação. Não executar uma regeneração supondo que já incorpora esta atualização.

## Simplificação dos textos públicos de consulta

- A arrecadação do SPSM integra a UO 37201; não há opção separada de SPSM em Receitas.
- Categoria, Origem e Espécie agregam os mesmos registros de base: não somar os níveis entre si.
- A exportação contém cada registro mensal de base uma única vez, sem subtotais da hierarquia. O JSON mantém a previsão anual separada; no CSV, mês do registro e referência do acumulado são colunas distintas.
- As instruções de toque/clique, Tab e Enter/Espaço e rolagem horizontal foram retiradas da apresentação; preservar os botões com nomes acessíveis, aria-expanded, aria-controls e foco pelo teclado.
- Por solicitação do responsável, as regras, meses presentes por UO e contagens técnicas deixam a interface; as regras contábeis e ressalvas anteriores permanecem internas. A data 21/10/2026 identifica a atualização da página, sem afirmar fechamento. O resumo mantém apenas a indicação curta de soma bruta com intraorçamentárias.


### Amostras legadas retiradas da publicação

Os CSV/JSON antigos receitas-teste (12 registros fictícios sem UO) e estagiarios-teste (oito registros fictícios), identificados no inventário original, continuavam em dist sem links ativos. Foram retirados do pacote e preservados em trabalho/revisao-final/amostras-legadas. Não se confundem com a planilha receitas-teste.xlsx de 425 registros reais, nem com os 714 estagiários reais. O texto legado de teste nos metadados de Receitas foi substituído por descrição factual, sem declaração de homologação ou completude.
