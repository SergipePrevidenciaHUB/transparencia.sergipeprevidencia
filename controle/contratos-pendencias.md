# Contratos — pendências dos modelos

Escopo: C 9.1–9.4 / S 9.1–9.3. Mapeamento em `controle/contratos-modelos.md`. As pendências originais da consulta principal são preservadas; Fiscais e Ordem Cronológica são complementados abaixo.

## Consulta principal — C 9.1–9.2

As fontes devem vir das áreas responsáveis, sem dados de exemplo ou declaração de inexistência presumida.

| Seção / requisito | Informação ou arquivo necessário | Providência antes da publicação |
| --- | --- | --- |
| Relação e ordem — C 9.1 / S `numeroContrato`, `sequencia` | Cadastro oficial de contratos, identificação e ordenação sequencial | Conferir universo e números repetidos entre anos/séries. Preservar número como texto e definir ordenação sem transformar posição na identificação do contrato. |
| Resumo — C 9.1 / S `contratado`, `valorContrato`, `objeto`, `inicioContrato`, `fimContrato` | Contratado, valor, objeto e início/fim da vigência, provenientes da fonte | Validar conteúdo e significado dos valores. Não preencher nome, objeto, zero ou datas para completar campos; esclarecer informações faltantes ou eventuais vigências sem termo final. |
| Aditivos — C 9.1 / S `termoAditivo` | Relação dos aditivos efetivamente celebrados, contexto e efeitos documentados | Confirmar vínculo e apresentação do resumo; não presumir aditivo nem sua ausência por falta de arquivo. Definir como distinguir valor original e efeitos reais sem duplicar valores ou inventar colunas normativas. |
| Íntegra do contrato — C 9.2 / S `linkContrato` | Arquivo oficial integral ou URL direta conferida de cada contrato | Conferir identificação, versão e acesso sem login. Resumo/ementa não substitui o documento. Não deduzir URL pelo número do contrato. |
| Íntegra dos aditivos — C 9.2 / S `termoAditivo` | Cada instrumento integral, quando existente, associado ao mesmo contrato | Conferir correspondência e completude; não copiar caminhos de exemplo S ou associar apenas por semelhança de número/nome de arquivo. |
| Associação técnica — DT | Referência estável contrato–aditivo–documento e, se necessário, identificador interno | Evitar junções que gerem um contrato por documento. Não tornar identificador privado nova coluna pública obrigatória nem criar novos `serigyItem`. |
| Filtro de período — C 9.1 / S `filtroPesquisa` | Referência temporal que deve governar início/fim do recorte | Confirmar com a área se corresponde a celebração, vigência ou outro conceito. Não usar datas de upload ou supor igualdade com início/fim de vigência. Validar intervalos e combinação com exercício quando implementar. |
| Consulta documental — C 9.2 | Localização dos documentos pelos contratos do recorte | Implementar associação clara da linha ao detalhe e aos arquivos. C exige filtro genérico, sem parâmetros mínimos enumerados próprios; não copiar filtros de outra dimensão. |
| Histórico — C 9.1 e 9.2 / S `historicoExercicio` | Cadastro e documentos dos pelo menos três anos anteriores à consulta; referência dos exercícios | Conferir cobertura da relação e dos inteiros teores, sem limitar acervo aos exemplos S ou inventar registros para anos ausentes. |
| Gravação — C 9.1 / S `salvarRelatorio` | Pelo menos um formato editável do conjunto selecionado, com mínimos e associação aos aditivos | Implementar exportação coerente com os filtros, sem multiplicar o valor integral por termo/documento. Não confundir download de contrato com gravação editável da relação; C 9.2 não exige exportação autônoma. |
| Atualidade — C 9.1 e 9.2 / S `dataUltimaAtualizacao` | Datas reais, cobertura e responsável da relação e dos documentos | Confirmar o parâmetro de até 30 dias; não usar data de geração ou supor que uma referência do cadastro cubra todos os documentos. |
| Arquivos e dados pessoais | Versões oficiais adequadas à divulgação e derivados públicos necessários | Conferir conteúdo com a instituição; não publicar credenciais, dados privados ou planilha de origem indiscriminadamente. Não acrescentar CPF/CNPJ, contatos ou dados bancários como campos mínimos que estas fontes não enumeram. |

O HTML tem somente cabeçalhos de tabela, listas documentais vazias e controles desativados. Alimentar com dados reais e aplicar marcações após resolver as pendências; depois testar documentos, filtros, histórico, exportação e acessibilidade antes de mover para `dist`. O menu público e o deploy permanecem inalterados. Nenhuma comunicação externa foi enviada.


## GestoresFiscais — C 9.3 / S 9.2

| Requisito | Informação/arquivo faltante | Providência |
| --- | --- | --- |
| Relação autônoma | Nomes oficiais dos fiscais e identificação dos contratos vigentes e encerrados pelos quais respondem | Obter cadastro validado e cobertura, sem restringir aos contratos atuais ou ao detalhe de cada contrato. S diz fiscal/gestor, mas C exige fiscais: confirmar funções, não presumir equivalência. |
| Associação e temporalidade | Referência fiscal–contrato e mudanças/substituições efetivamente existentes | Definir granularidade DT e exercício de referência com a área; não deduzir por homônimos nem duplicar associações por cópias de arquivos. |
| Histórico e atualidade | Acervo de pelo menos três anos anteriores à consulta; data real, cobertura e responsável | Conferir parâmetro de até 30 dias e população incluindo contratos encerrados. Não usar data do HTML nem inventar exercícios sem fonte. |
| Filtro e gravação | Dados reais para seletor de exercício/busca e arquivo do recorte | Implementar o filtro DT e ao menos um editável ou PDF pesquisável aceito por C 9.3. Não anunciar exportação filtrada para arquivo estático que não segue a consulta. |
| Fonte documental e dados pessoais | Evidência funcional necessária para validar os vínculos e derivados publicáveis | Portaria de designação integral não é anexo mínimo deste critério. Não acrescentar CPF, salário ou contatos privados por cópia de cadastro bruto; não ocultar os nomes exigidos nem criar acesso restrito. |

## OrdemCronologica — C 9.4 / S 9.3

| Requisito | Informação/documento faltante | Providência |
| --- | --- | --- |
| Ordem oficial por grupos | Créditos e sua ordem real por fonte dos recursos e categorias de bens, locações, serviços e obras | Obter a fonte validada e a regra de ordenação. Não produzir a fila apenas ordenando pagamentos nem misturar fontes/categorias como uma ordem única. |
| Identificação dos créditos | Credor, valor, vencimento, pagamento e referência interna confiável para associação | Confirmar granularidade, pagamentos parciais/estornos ou créditos não pagos se existentes. Chave interna é DT, não nova coluna pública obrigatória. Não preencher valores ou datas ausentes por suposição. |
| Vencimento | Regulamentação/fato que define a exigibilidade e datas da origem | C menciona regra local e alternativas de liquidação/emissão de nota fiscal; confirmar qual se aplica. Não escolher automaticamente uma alternativa ou usar data do arquivo. |
| Fonte/categoria/justificativa sem item S | Identificações reais e fundamento de cada alteração da ordem | Exibir o conteúdo C em HTML, sem inventar `serigyItem`. A tabela S com quatro campos não dispensa essas informações. |
| Alterações e documentos | Justificativas reais da autoridade responsável, vinculadas ao crédito/grupo, com documentos se utilizados | Obter a explicação e evidências pertinentes; conferir acesso e correspondência. Não criar justificativa-padrão ou declarar ausência de alterações a partir de lacuna. Não usar `serigyLink` para PDF. |
| Publicação mensal e histórico | Listas dos meses reais de referência e acervo de pelo menos três anos anteriores à consulta | Definir cobertura e se listas da fonte são posições cumulativas ou movimentos; não somar novamente créditos repetidos em vários meses. Não inventar meses ausentes ou fechamento. |
| Filtro e exportação | Exercício/mês/fontes/categorias reais e derivado editável do conjunto | Implementar escolhas DT sem tratá-las como filtros mínimos enumerados C. Preservar ordem, grupos e fundamentos na exportação, sem duplicar por anexo ou repetição mensal; PDF sozinho não atende a gravação em 9.4. |
| Atualização | Referência real de atualização/cobertura e responsável | Conferir publicação mensal e parâmetro de até 30 dias, sem preencher com a data de geração. A ressalva nominal ao Banese não se aplica automaticamente à Previdência Estadual. |
| Arquivos de origem | Derivados públicos adequados e URLs oficiais conferidas, quando usados documentos | Não publicar planilhas privadas, dados bancários/credenciais ou campos pessoais adicionais por conveniência. Não inventar normas, links ou documentos para completar o modelo. |

Ambos os modelos continuam fora de `dist`, com dados vazios e controles desativados. Antes de publicar: receber e conferir fontes, resolver referências temporais e associações, alimentar dados/documentos e datas reais, implementar filtros/gravações aplicáveis e só então aplicar marcações e validar. O modelo principal, outras seções, menu e deploy permanecem inalterados; nenhuma comunicação externa foi enviada.


## Fiscais e gestores — alimentação da planilha

Fonte: dados-entrada/contratos/fiscais-e-gestores.xlsx, aba CONTRATAÇÕES EM ACOMPANHAMENTO. 104 linhas de instrumentos, 348 associações nominais. Distribuição: {'Fiscal': 104, 'Fiscal substituto': 73, 'Gestor': 99, 'Gestor substituto': 72}. Nenhuma deduplicação por nome ou número. As linhas 75 e 76 da adesão 015/2024 são mantidas separadamente por contratada, com todas as funções preenchidas. A nota da linha 107 foi ignorada. Vazios e hífen nas quatro colunas de pessoas foram tratados como ausência, sem gerar nome ou associação fictícia. 68 posições ausentes.

A linha 25 traz SIM na coluna VIGÊNCIA; não foi interpretado como data, vigência ou vínculo. Não foram publicados períodos de designação, situação atual, datas de vigência ou EM ACOMPANHAMENTO. Ano extraído somente do identificador do instrumento, explicitado no rótulo e na exportação; não é período de designação nem comprova histórico funcional. Confirmar datas de designação/dispensa e completude das funções com a área. Nomes e grafias foram preservados com remoção apenas de espaços nas bordas; não fundidas variantes (ex.: SOUSA/SOUZA, ACACIA/ACÁCIA). Não foram criados links. A data de atualização da relação foi informada pelo responsável em 22/10/2026 e publicada com dataUltimaAtualizacao sob o schema de Contratos (S9 9.2.5). Não representa designação ou vigência.

Marcação S9 9.2: fiscalGestor no nome e contratoFiscal no instrumento da mesma linha. Filtro por nome, função e ano do instrumento, historicoExercicio/serigyValue e Wait/Load correspondentes, exportação CSV das mesmas cinco colunas do recorte. Nenhum valor financeiro foi incluído.

O ano só é identificado quando há um único ano explícito no identificador. As linhas 31 e 87 não têm ano identificável: suas oito associações permanecem na consulta geral como “Não identificado”. Não foi deduzido ano de outra coluna. Associações por ano do instrumento: 2020=2, 2021=4, 2022=25, 2023=16, 2024=60, 2025=150, 2026=83; sem ano=8.

Conferência automatizada em Chrome por HTTP local: 711 verificações sem falhas, 348 associações comparadas à fonte, quatro funções, anos, filtros combinados, limpeza e CSV integral/filtrado conciliados. Os demais arquivos preexistentes de dist foram comparados por hash e preservados.

## Extração preparatória — relação de contratos com atas

Fonte: `dados-entrada/contratos/relacao-contratos-com-atas.xlsx`, abas `CONTRATOS` e `ADITIVOS`. Preparação em `dados-entrada/contratos/contratos-extraidos.json`, fora de `dist`. Seção Serigy consultada: somente 9.1 Contratos. Não houve alimentação da página pública nesta etapa.

| Grupo | Linhas preservadas | Destinos de hiperlinks F | Sem URL |
| --- | ---: | ---: | ---: |
| Contratos identificados como tais na coluna A | 156 | 122 | 34 |
| Atas, separadas para revisão | 12 | 9 | 3 |
| Outros instrumentos, separados para revisão | 11 | 11 | 0 |
| Aditivos | 36 | 36 | 0 |

Total: 215 linhas, 178 URLs distintas. As URLs foram extraídas do destino real do hiperlink F, não do texto exibido na célula. Destino extraído não significa acesso, inteiro teor ou correspondência documental conferidos. Nenhum PDF foi baixado. Células literais, aba e linha de origem foram preservadas; nenhuma linha foi deduplicada. Atas e demais instrumentos não foram automaticamente transformados em contratos.

Somente oito aditivos receberam associação inequívoca na extração. Critério técnico conservador: referência explícita de número/ano, um único contrato candidato, contratado/CNPJ coincidente e ausência de conflito detectado entre título e objeto. Os 28 restantes estão separados com candidatos e motivo no JSON. A normalização de zeros na chave interna não modifica o número literal da fonte.

- Referência com mais de um candidato: ADITIVOS 9–12, 18–20, 24–26 e 44. Não unir contratos nem escolher uma linha sem confirmação.
- Contratado/CNPJ divergente ou insuficiente: ADITIVOS 13–17, 21–22, 27, 32–34, 39–41 e 43. Conferir identificação das partes; não corrigir dígitos automaticamente.
- ADITIVOS 23: sem contrato candidato com a referência explícita. ADITIVOS 35: título indica 003/2025, mas o objeto cita 003/2024; sem associação.
- Vigência: CONTRATOS 18 tem fim anterior ao início; CONTRATOS 48 e 80 contêm data inválida; ADITIVOS 39 contém `1110/2026`. Literais preservados, sem reparo ou separação presumida em `inicioContrato`/`fimContrato`.
- A coluna A de CONTRATOS 10 informa apenas “Contrato”, sem número. Ausências por campo e linha estão no JSON, incluindo URLs não fornecidas.
- Outros instrumentos: anuências, adesão/filiação, dispensas por valor e inexigibilidade (linhas 18, 22, 24, 30, 45–48, 55, 71 e 134); definir a destinação antes de publicar. Manter as 12 atas separadas, mesmo quando o nome do PDF contém “contrato”.

S9 9.1 prevê `numeroContrato`, `contratado`, `valorContrato`, `objeto`, `inicioContrato`, `fimContrato`, `sequencia`, `termoAditivo` e `linkContrato`. A fonte não tem coluna estruturada de valor do contrato: valores eventualmente mencionados no objeto não foram promovidos a valor original/atualizado. Não foram inventados sequência, início/fim estruturados, atualização ou links. Confirmar significado e cobertura dos períodos de cabeçalho, valores oficiais, classificação dos instrumentos, vínculos pendentes, vigências e acesso/correspondência dos documentos antes da alimentação pública.

## Alimentação da consulta principal de Contratos

A página existente de Contratos recebeu os 156 registros do grupo `contratos` de `contratos-extraidos.json`, com 122 links de íntegra e somente oito aditivos associados (AGENDA: quatro; SMART NX: três; CL LOCAÇÃO: um). Os 34 contratos sem URL permanecem na consulta sem link vazio. Atas, outros instrumentos e os 28 aditivos pendentes não foram incluídos nem associados por aproximação.

Gerador: `tools/integrar_contratos.py`, com `--check` para conciliação. Número literal quando fornecido (`numeroContrato`), contratado (`contratado`), objeto (`objeto`), documentos (`linkContrato`/`termoAditivo`). Vigência mantida literalmente; `inicioContrato`/`fimContrato` apenas quando as duas datas forem válidas, identificáveis e ordenadas. A vigência inválida de CONTRATOS 80 fica sem marcação de data; os demais casos ausentes ou não estruturáveis também não recebem datas presumidas. As ausências por origem continuam detalhadas no JSON. Não há `valorContrato`, `sequencia` nem `dataUltimaAtualizacao`: obter valores, ordem oficial e atualização confirmada antes de marcar esses itens.

Decisão técnica de consulta: exercício extraído exclusivamente do número do instrumento, explicitado na interface, sem representar vigência ou data de celebração; registros sem ano continuam em “Todos os exercícios”. Pesquisa textual combinada por número, contratado e objeto. Histórico (`historicoExercicio`/`serigyValue`), filtro (`filtroPesquisa`) e espera/carregamento com identificador `contratosTabela` correspondentes. CSV (`salvarRelatorio`, `csv`) com uma linha por contrato no recorte e todos os links dos aditivos seguros na mesma célula, sem multiplicação de contratos.

Teste `tools/testar_contratos.py`: HTML inicial conciliado ao JSON, 156 contratos/122 íntegras/oito aditivos; Chrome por HTTP local sem falhas nas 14 verificações de exercícios, pesquisa combinada, vínculo AGENDA, ausência de resultados e limpeza. CSV integral e filtrado conferidos, incluindo todos os links de aditivos (quatro no recorte AGENDA e oito no integral). Testes não comprovam acesso externo, pesquisa de texto ou correspondência dos PDFs, nem cobertura histórica completa. Essas conferências e os campos ausentes permanecem pendentes.


### Ensaio sintético separado de Contratos

Ativar: `python tools/integrar_contratos.py --sinteticos`; conferir com `--check --sinteticos`. Remover: executar o mesmo gerador sem `--sinteticos`. A geração normal omite a seção e seus documentos, preservando 156 contratos, 122 links e oito aditivos. Nenhum arquivo precisa ser excluído.

Fonte independente do JSON real: função `synthetic_section` do gerador, três entidades explicitamente fictícias em 2024–2026, valores R$ 100,00/200,00/300,00 e sequências 1/2/3 somente de ensaio. Cada linha e CSV sintético contém “DADO SINTÉTICO — TESTE SERIGY”. Tabela, filtros, histórico, CSV e documentos HTML locais separados dos reais. `valorContrato` e `sequencia` não foram atribuídos aos registros reais. Atualização oficial continua pendente; nenhuma data foi inventada.

Reutilizado sem alterações o bloqueio genérico por `data-dado-sintetico` de `tools/preparar_deploy.py`. Só permite `--permitir-dados-sinteticos --base-path /transparencia.sergipeprevidencia`, sem CNAME. Outros ensaios continuam sujeitos ao bloqueio mesmo após remover Contratos.

`tools/testar_contratos_sinteticos.py` confere a cópia Pages em Chrome/HTTP, filtros combinados, histórico, limpeza, CSV integral/filtrado com aviso em cada linha, links locais e HTML inicial. Bloqueio oficial testado com Contratos isolado; remover a seção da cópia libera esse bloqueio isolado. Comparação da geração sem ensaio preserva os registros e marcações reais. Reconhecimento pelo Invoker depende de publicação autorizada e nova avaliação; não foi executado.


## Ordem Cronológica — ensaio técnico sintético

Quatro pagamentos inteiramente sintéticos (2023–2026), mantidos no HTML inicial com aviso individual “DADO SINTÉTICO — TESTE SERIGY”. Nomes explicitamente fictícios, sem CPF/CNPJ, datas de vencimento/pagamento e valores de ensaio. Não representam créditos, pagamentos ou ordem oficial do SergipePrevidência. Fonte sintética separada no gerador tools/preparar_teste_ordem.py; não foi utilizada planilha institucional.

S9 9.3.1–8: dataVencimento, dataPagamento, credor e valorPagamento somente nos valores de teste; filtroPesquisa funcional, historicoExercicio/serigyValue nos quatro exercícios sintéticos, espera/carregamento com identificador ordemTabela, salvarRelatorio/csv do recorte. Ano, mês de pagamento e pesquisa de credor são escolhas técnicas do ensaio. CSV contém o aviso em cada linha e nome SINTETICOS-TESTE-SERIGY. dataUltimaAtualizacao=22/10/2026 identifica explicitamente a preparação do ensaio, não atualização de pagamentos reais. Não foram inventados fontes de recursos, categorias contratuais, justificativas ou documentos oficiais.

Ativar: python tools/preparar_teste_ordem.py --ativar. Conferir: acrescentar --check. Desativar: python tools/preparar_teste_ordem.py --desativar. O gerador preserva a estrutura anterior em BASE_MAIN e a restitui sem apagar arquivos nem modificar outras páginas; remove a carga do JS de ensaio. O JS fica inerte sem a tabela sintética. Bloqueio oficial genérico existente reutilizado sem alterações, por data-dado-sintetico. Exceção somente para base /transparencia.sergipeprevidencia com permissão explícita e sem CNAME. Outros ensaios do portal continuam bloqueando a preparação oficial mesmo após retirar Ordem Cronológica.

Teste tools/testar_ordem_sintetica.py: oito marcações conferidas no HTML inicial; Chrome/HTTP local, filtros combinados, histórico, consulta sem resultados, limpeza e CSV integral/filtrado conciliados campo a campo. Remoção em cópia restaura a estrutura anterior e libera o bloqueio isolado; recusas confirmadas para raiz, base incorreta e ausência de permissão. Demais arquivos dist preservados por hash. Invoker não executado: reconhecimento depende de publicação autorizada e nova avaliação.

Fonte real ainda necessária: créditos e ordem oficial por fonte/categoria, credores/valores, vencimento conforme regulamentação e fatos, pagamentos, justificativas de alterações quando houver, cobertura mensal/histórica e atualização real. Não inferir ordem oficial apenas ordenando pagamentos; substituir integralmente os registros sintéticos por fonte conferida antes da publicação definitiva.

## Preparação da tabela real — 22/10/2026

Consulta com dez colunas: exercício, sequência, número, contratado, valor, objeto, início, fim, íntegra e aditivos. Mantidos 156 contratos, 122 íntegras e oito aditivos de associação segura; não refeito o cruzamento dos 28 pendentes. Valor e sequência permanecem ausentes, com células vazias e justificativas serigyEmpty específicas; atributos não comprovam atendimento material desses campos. Não usar ordem da planilha, número de processo, numeração inventada ou zero para preenchê-los. A função data_cell preserva o item e substitui a ausência por conteúdo quando receber valor confirmado; a adaptação da nova fonte deve ser explícita, sem presumir nomes de futuras colunas. Datas separadas somente quando os limites já eram identificáveis e válidos. Demais ausências visivelmente vazias e CSV correspondente. Removidos três contratos fictícios, documentos embutidos e exportação exclusiva; gerador rejeita --sinteticos. Outros ensaios e bloqueio oficial preservados. Atualização da página mantida em 22/10/2026. Reconhecimento pelo Invoker permanece pendente, não executado nesta tarefa.

## Gestores/Fiscais — apresentação dos instrumentos

Retirados somente os asteriscos ornamentais nas extremidades dos identificadores, sem alterar números ou unir linhas. Mantidas 348 associações de 104 instrumentos, nas quatro funções da fonte. Alimentação atual é HTML, sem importador dedicado localizado em tools; a normalização foi incorporada ao script existente fiscais.js antes de consulta e CSV, além da limpeza no HTML inicial. Planilha original preservada. O ano extraído do instrumento não comprova período de designação, vigência ou situação do vínculo. Confirmar cobertura de contratos vigentes/encerrados e histórico das designações; conciliação com a planilha não comprova completude institucional. Preservadas nota de rodapé ignorada (linha 107), associações da adesão 015/2024, ausências de nomes e não interpretação de SIM como vigência. Atualização mantida em 22/10/2026.

### Ordem Cronológica — substituição do ensaio em 23/10/2026

O histórico do ensaio acima fica preservado como registro de trabalho anterior. As instruções de ativação/desativação sintética **não se aplicam mais à página alimentada**: o preparador antigo recusa sobrescrevê-la. A consulta atual contém 464 pagamentos reais preparados, atualização autorizada em 22/10/2026, cinco filtros, totais separados e CSV do recorte. Fonte, conferências e limitações estão em `controle/ordem-cronologica-verificacao.md`. Sem novos cruzamentos, justificativas inventadas ou afirmação de cobertura integral; pendem vínculo OB–LE, definição local de vencimento, cobertura institucional/histórica e fila oficial com justificativas aplicáveis. Reconhecimento pelo Invoker continua pendente de nova avaliação autorizada; bloqueio global de ensaios preservado.

### Valor contratual — estrutura e preenchimento pendente

Coluna pública e CSV denominados **Valor contratual**, com `serigyItem="valorContrato"` nas 156 células, sob o schema de Contratos. A extração atual não fornece valor monetário estruturado: células e CSV permanecem vazios, sem zero, substitutivo ou `serigyEmpty` nesse campo. Não se extrai valor de menções no objeto nem se inventa coluna de origem. O gerador preserva esta apresentação; o CSV reutiliza cabeçalhos e células da tabela. Quando valores oficiais forem fornecidos, mapear e confirmar sua natureza e formatação. **Estrutura implementada não significa aprovação de 9.1.3; preenchimento monetário permanece pendente.**

156 contratos, 122 links e oito aditivos preservados; ensaio sintético já estava removido e não foi reativado. Conferência pontual: geração `--check`, células e cabeçalho, vínculos com a fonte, CSV integral no Chrome e snippet institucional. Nenhum dado, script de filtros ou bloqueio global de publicação foi alterado.


### Privacidade — revisão final

O campo textual de um contrato continha CPF completo formatado. A projeção pública e o gerador agora mascaram esse identificador antes de gerar HTML/CSV; fonte interna preservada, sem excluir registros ou documentos. 156 contratos, 122 links e oito aditivos mantidos.


## 4252 — justificativas de valor e sequência

9.1.3/9.1.7: JSON contratos-extraidos.json e relacao-contratos-com-atas.xlsx conferidos; SHA256 da planilha coincide com a extração. Cabeçalhos: Tipo da Celebração, Modalidade/Nº da Licitação, Órgão/Entidade, Período de Vigência, Descrição Sucinta do Objeto e Links Contratos. Não há campos confirmados de valor ou sequência para os 156 contratos. Não inferir sequência do número contratual, modalidade, posição ou linha da planilha. As 156 células valorContrato e 156 sequencia continuam vazias, sem zero, agora com serigyEmpty verdadeiro e único por campo/id_origem; demais ausências intencionais da tabela também individualizadas. Mantidos 122 links e oito aditivos. A rotina retira serigyEmpty quando recebe conteúdo confirmado; as propriedades opcionais valorContrato/sequencia no registro de entrada não são novos dados nem nomes presumidos de colunas da futura planilha. Obter os dados oficiais e mapear sua origem continua pendente. HTML e CSV não recebem textos substitutivos. Reconhecimento técnico e atendimento material continuam distintos. Evidências: trabalho/conferencia-4252-campos/testes.json.
