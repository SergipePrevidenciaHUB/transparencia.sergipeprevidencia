# Despesas 4.1 e 4.2 — dados preparados

## Resultado

- Fonte: `Despesas_Unificadas.xlsx`, aba `Sheet1`, 3.935 registros.
- Dicionário: `Base_de_Conhecimento.xlsx`, aba `Sheet1`, 610 entradas.
- Saída: `dados-entrada/despesas/despesas-41-42-preparadas.json`.
- 143 totais por exercício/mês/UO e 3.637 combinações de classificação.
- Todas as descrições obrigatórias encontradas no dicionário; nenhuma classificação preenchida por suposição.
- As 3.935 linhas possuem referência válida, dados preenchidos e valores numéricos. Nenhuma chave orçamentária completa repetida e nenhum valor negativo nas colunas financeiras da origem.
- Categoria e grupo coerentes com a natureza da despesa em todas as linhas.
- Os três valores de cada período/UO conciliam integralmente entre a fonte, a classificação preparada e a tabela de totais.

## Requisitos e integração

Cartilha PETP 2026, pp. 36–40: 4.1 exige empenhado, liquidado e pago comparáveis na mesma página; 4.2 exige unidade, função, subfunção, categoria, grupo, elemento e fonte, com códigos e descrições. Ambos exigem atualidade, histórico de pelo menos três exercícios anteriores, exportação editável e filtros. Filtros mínimos: ano e mês/período; em 4.2, também elemento.

Serigy: https://serigy.tce.se.gov.br/petp/comum/despesas.html. Preservar o schema `https://serigy.tce.se.gov.br/comum/despesas.html` e usar as associações de campos incluídas no JSON. Códigos e descrições devem permanecer associados na página e no CSV. Não inventar itens Serigy para programa, ação, mês ou seletor de UO.

O JSON contém somente as estruturas necessárias à integração; não repetir a soma da tabela de totais com os seus componentes classificados. A classificação consolida linhas que diferiam somente por programa/ação ou outra dimensão não exigida para esta apresentação. As linhas originais agrupadas estão em `linhas_origem`, conservando o rastreio ao XLSX. As três medidas financeiras foram somadas uma única vez por grupo. A natureza completa da origem, por exemplo `3.3.90.39`, foi preservada como código do elemento/natureza; não reduzir apenas aos dois dígitos finais.

Cada registro conserva seu mês de referência. O material preparado não calcula acumulados anuais nem soma períodos para preencher meses ausentes. Usar o rótulo curto “Mês de referência” e manter os valores do registro selecionado. A definição contábil de movimento mensal versus saldo deve ser confirmada com a origem antes de qualquer nova transformação ou opção de acumulado.

Atualização da página no JSON: **22/10/2026**, seguindo a orientação expressa já dada pelo responsável no projeto. Exibir com `dataUltimaAtualizacao`. Isso não define a data de atualização do sistema contábil nem o fechamento do último mês. Preparação do arquivo: 23/10/2026. Não trocar automaticamente uma data pela outra.

## Cobertura

- UO 37201: SergipePrevidência; UO 37202: SPSM; UO 37401: FINANPREV; UO 37403: FUNPREV. Nomes conforme correspondência fornecida no projeto; o dicionário anexo não possui categoria própria de UOs.
- SergipePrevidência, SPSM e FINANPREV: janeiro–dezembro de 2023, 2024 e 2025; janeiro–outubro de 2026.
- FUNPREV: abril e junho–setembro de 2026. Abril tem dois registros com empenhado, liquidado e pago iguais a zero na fonte; foram preservados como dados existentes, sem presumir início operacional em abril. Maio e outubro não constam e não receberam registros artificiais.

## Pendências internas

1. Confirmar a referência de atualização do conjunto contábil e se outubro/2026 é parcial. Não atribuir data de fechamento por suposição.
2. Confirmar a ausência de maio e outubro/2026 do FUNPREV, e o significado dos registros orçamentários zerados de abril. Preservar os dados recebidos até esclarecimento.
3. A categoria “Ações”, código 1078, tem descrições que diferem apenas em maiúsculas/minúsculas. Não afeta 4.1/4.2 porque ação não é campo obrigatório desta integração; nenhum registro foi alterado por essa diferença.
4. A origem contém dotação, créditos, programa, ação e modalidade de aplicação, mas esses campos não foram acrescentados à interface nesta preparação. Os arquivos originais permanecem como fonte para eventual uso posterior.
5. Remover os exemplos sintéticos somente dos blocos 4.1 e 4.2 ao inserir os dados reais. O bloco 4.3 ainda é um ensaio independente e deve ser preservado; seu aviso e o bloqueio de publicação oficial não devem ser retirados por esta integração.
6. O antigo preparador sintético abrange três blocos. Não executá-lo para regenerar os blocos reais. Garantir que nenhuma regeneração subsequente substitua os dados reais por exemplos.
7. Marcação implementada e teste local não comprovam reconhecimento pelo Invoker; não executar nova avaliação nesta tarefa.

Estas notas são exclusivamente internas. A interface deve manter somente os títulos, rótulos, dados, controles e data de atualização necessários à consulta, sem avisos editoriais de validação ou explicações do processamento.

## Integração de 4.1/4.2 no Portal

`tools/integrar_despesas.py` usa diretamente este JSON, sem transformar meses em acumulados e sem preencher períodos ausentes. Publica 143 totais e 3.637 classificações no HTML inicial, incluindo as quatro UOs. Códigos e descrições ficam associados; as três medidas aparecem também em 4.2. O JavaScript existente foi ajustado somente para reconhecer as 12 colunas dessa tabela e seus valores monetários. Agrupadores da hierarquia são visuais e não contêm novos valores ou linhas financeiras no CSV.

Regeneração: `.\.venv\Scripts\python.exe tools\integrar_despesas.py`; conferência sem gravação: o mesmo comando com `--check`. O importador concilia empenhado, liquidado e pago das classificações com cada um dos 143 totais por ano/mês/UO antes de gravar. A atualização pública é 22/10/2026, extraída do campo próprio do JSON; não se usa a data de preparação de 23/10/2026.

Os exemplos e avisos sintéticos foram removidos somente de 4.1/4.2. O bloco 4.3 permanece integralmente sintético, com seus avisos e registros originais. O bloqueio oficial existente continua obrigatório. O antigo `preparar_teste_despesas.py` não deve ser usado para regenerar esta página: sua proteção contra sobrescrever blocos alterados fora do modo sintético recusa os blocos reais. Não se criou outro modo de deploy nem foi alterada a regra de publicação.

Verificações proporcionais estão em `tools/testar_despesas_reais.py`: correspondência dos campos de todas as linhas com o JSON, conciliação das três medidas, uma consulta combinada e CSV por bloco, abertura/fechamento de um agrupador e preservação de 4.3. As pendências contábeis e de cobertura listadas acima permanecem; a integração não comprova fechamento de período ou reconhecimento no Invoker.
