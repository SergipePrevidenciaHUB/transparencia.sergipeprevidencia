# Convênios e transferências — conferência interna (21/10/2026)

Fontes: `convenios.zip`, Cartilha PETP 2026 pp. 42–47 e Serigy Docs dimensão 5. Este controle não é conteúdo público.

## Critérios e situação

| Critério | Requisito principal | Material | Estado | Providência |
|---|---|---|---|---|
| 5.1 Recebidas | Número/ano, concedente, objeto, valor total, recebido, vigência, íntegra, atualização, histórico, filtro por exercício e exportação editável. | Ausência confirmada pelo responsável de 01/2018 até 21/10/2026, apresentada como período 01/2018 a 10/2026. | Preparado para publicação | Usar declaração expressa e `dataUltimaAtualizacao` de 21/10/2026; atualizar periodicamente. Outubro ainda está em curso. Não fabricar tabela de instrumentos. |
| 5.2 Realizadas | Número/ano, beneficiário, objeto, valor total, repassado, vigência, íntegra, atualização, histórico, filtro por exercício e exportação editável, em seção separada de 5.1. | Ausência confirmada pelo responsável de 01/2018 até 21/10/2026, apresentada como período 01/2018 a 10/2026. | Preparado para publicação | Usar declaração expressa e `dataUltimaAtualizacao` de 21/10/2026; atualizar periodicamente. Manter revisão da abrangência de auxílios/subvenções em controle interno. |
| 5.3 Sem transferência | Partes, número/ano, objeto, vigência, obrigações, íntegra, atualização, histórico, filtro por exercício e exportação editável. | Sete linhas de convênios de cooperação de estágio, datas, partes, objeto e URLs. | Parcial | Conferir instrumento integral por linha, descrever obrigações efetivas, reconciliar identificadores, aditivos e vigência; ativar controles e publicar apenas dados conferidos. |

A Cartilha orienta declaração expressa de ausência para 5.1/5.2 com **período e data da atualização**; a série histórica mínima é de três anos anteriores. 5.3 não é ausência: existem sete registros. O responsável confirmou em 21/10/2026 a inexistência de ocorrências até essa data. A referência a 10/2026 **não afirma o fechamento de outubro**. A data de 21/10/2026 pode marcar a atualização dessas duas declarações; a seção 5.3 requer data própria quando alimentada.

## Divergências e documentos de 5.3

| Linha Excel | Parte | Identificador na planilha | Constatação | Providência |
|---:|---|---|---|---|
| 2 | IREP/Estácio | 001/2022 | URL não pôde ser consultada pela ferramenta; rótulo `INCLUIR CONTRATO`. | Conferir se PDF abre e se é instrumento integral; confirmar identificação e obrigações. |
| 3 | UFS | 001/2022 | PDF vinculado se intitula Convênio 01/2024 e menciona processo 40/2024. | Corrigir a planilha após validação, sem criar um segundo 001/2022. |
| 4 | FANESE | 002/2023 | PDF disponível se apresenta como Plano de Trabalho vinculado ao Convênio 002/2024. | Obter convênio integral e acertar número/ano. |
| 5 | Pio Décimo | 003/2024 | PDF intitulado Convênio 03/2024. | Conferir assinaturas, obrigações, vigência, alterações. |
| 6 | UNINASSAU | 004/2024 | PDF intitulado Termo de Convênio 04/2024. | Conferir assinaturas, obrigações, vigência, alterações. |
| 7 | UNIT | 005/2024 | PDF abre como Acordo de Cooperação; não foi conciliado integralmente com o identificador da planilha. | Conferir título, assinaturas, prazo e obrigações. |
| 8 | IFS | 006/2024 | PDF de convênio de estágio acessível. | Conferir identificação, assinaturas, prazo e obrigações. |

O campo `TOTAL R$` está em 0,00 nas sete linhas. Isso é indício de inexistência de transferência entre as partes, mas não dispensa a leitura das cláusulas e dos eventuais aditivos. O pagamento de bolsa a estagiário, se previsto no instrumento, não deve ser confundido automaticamente com transferência à instituição de ensino.

A planilha não contém coluna-resumo das **obrigações ajustadas**, exigida por 5.3. O JSON guarda resumos preliminares extraídos dos PDFs acessíveis para UFS, Pio Décimo, UNINASSAU, UNIT e IFS. São sínteses para revisão, não transcrição integral nem valores já aprovados para `obrigacoes`; IREP e FANESE seguem sem síntese validável. O texto `INTEIRO TEOR` em uma linha não é o próprio documento; a URL original foi preservada no JSON como candidata, sem proclamar íntegra conferida. O filtro de exercício deve definir claramente o período usado (ano do ajuste, assinatura ou vigência), pois alguns IDs e datas divergem. Não normalizar os identificadores automaticamente.

## Entrega e próxima alimentação

`convenios-dados-preparados.json` contém as duas declarações atualizadas, com as declarações originais preservadas, e os sete registros rastreáveis por linha Excel. Para o Codex: alimentar 5.1 e 5.2 com as declarações e data 21/10/2026; em 5.3 preservar as sete linhas, mas não publicar os IDs conflitantes nem marcar `obrigacoes` ou `anexoConvenio` onde não há conteúdo conferido. Os resumos preliminares devem ser validados antes da página definitiva. Registrar internamente as exceções, sem avisos internos no portal.

## Tratamento de 5.3 em 21/10/2026

- Espaços duplicados em partes/objetos normalizados para consulta; textos originais permanecem no XLSX. Não removi nem fundi linhas, porque o mesmo identificador na origem pode resultar de erro de digitação.
- UFS: PDF aponta 01/2024, planilha 001/2022; FANESE: plano de trabalho aponta 002/2024, planilha 002/2023. IDs candidatos separados dos originais, sem substituição silenciosa.
- Resumos preliminares das obrigações elaborados somente onde cláusulas acessíveis permitiram; campo publicável `obrigacoes_resumo` permanece vazio até aprovação.
- Para 5.1 e 5.2, confirmar novamente em atualização futura. Ausência declarada de 01/2018 até **21/10/2026**, sem pressupor fechamento do mês.


## Ensaio técnico autorizado — somente 5.1/5.2

Nesta rodada, as duas páginas ainda continham estrutura sem dados; a declaração institucional confirmada no JSON foi incorporada separadamente em cada página, mantendo a redação da fonte e esclarecendo a cobertura de janeiro/2018 até 21/10/2026, sem afirmar fechamento de outubro. dataUltimaAtualizacao marca 21/10/2026 junto dessa informação real. A área de teste explicita preparação em 22/10/2026, sem atribuir à declaração os registros artificiais.

Por solicitação expressa, cada consulta recebeu quatro registros inteiramente sintéticos, exercícios de teste 2023–2026, sem aproveitar qualquer acordo de 5.3 ou nome/valor institucional. Aviso na página, em cada registro e em cada linha do CSV: **DADOS SINTÉTICOS PARA TESTE DO SERIGY — NÃO REPRESENTAM TRANSFERÊNCIAS DO SERGIPEPREVIDÊNCIA**. Números 91001–91004/ano, entidades que declaram não existir, objetos, vigências e valores foram produzidos apenas para o ensaio. Não contradizem a declaração real: os blocos são explicitamente separados. Nenhum dado de 5.3 foi publicado aqui; Convenios/SemTransferencia e o JSON de origem permaneceram intactos.

Campos documentados: identificaTransferencia, orgaoRepassador (5.1) ou orgaoBeneficiario (5.2), vigenciaConvenio, objetoConvenio, valorTotalPrevisto (5.1) ou valorTotalRepasse (5.2), valorRepassado e anexoConvenio. Usados no conteúdo correspondente, sob o schema de Convênios. Filtros, histórico com serigyValue, ação de seleção/pesquisa e seção de resultados têm filtroPesquisa, historicoExercicio, serigyExecuteWaitSection/serigyLoadSection; CSV funcional usa salvarRelatorio/csv. Não foi criado serigyEmpty para a ausência integral real. Persiste a divergência de S5 que tipa vigência como Ano e exemplifica datas; a vigência fictícia é apresentada como período, sem inventar serigyItemType.

Documentos de ensaio: cada página tem um arquivo documentos-sinteticos.html com quatro instrumentos identificados por âncora e aviso individual. Cada link anexoConvenio aponta para o instrumento correspondente existente, em HTML, com todos os metadados sintéticos, sem assinaturas, partes reais ou eficácia jurídica. Não se afirma que sejam instrumentos oficiais ou PDFs. O CSV preserva os campos completos, aviso e URL do instrumento, inclusive na base Pages.

**Mesmo bloqueio de publicação:** reutilizado data-dado-sintetico, já reconhecido pelo preparador de Despesas/SIC. A lógica não mudou: a permissão explícita só vale na base /transparencia.sergipeprevidencia, sem CNAME. Foi ampliada somente a orientação da recusa para incluir Convênios. Sem novo mecanismo ou alteração de workflow. Para publicação oficial, remover/substituir a área sintética, seus registros, exportação e documentos de teste; preservar a declaração institucional e a atualização de 21/10/2026. Os documentos sintéticos também possuem marcador e são recusados pelo mesmo bloqueio, mesmo que não estejam mais vinculados. Não basta apagar os avisos mantendo conteúdo artificial. Nenhuma publicação oficial foi preparada ou realizada nesta rodada.

**Pendências 5.1/5.2:** atualizar periodicamente a confirmação institucional de ausência e seu período; antes de publicação definitiva, retirar integralmente o ensaio técnico e seus documentos ou alimentar somente eventuais instrumentos reais confirmados. O teste não demonstra ocorrência de transferência nem atendimento integral ao PETP. As pendências e a alimentação real de 5.3 ficam para outra tarefa.

**Testes:** tools/testar_convenios_sinteticos.py aprovado com 148 verificações Chrome em localhost e Pages simulado, 188 referências HTTP, 16 verificações de documento/âncora (quatro por página em duas bases), filtros, histórico, espera/carregamento, CSV filtrado de uma linha e completo de quatro linhas por página. Sete recusas de preparo oficial/base incorreta/sem permissão/CNAME aprovadas em origem de Convênios, sem depender de Despesas/SIC, preservando a saída existente. Snapshot confirmou demais arquivos dist intactos, inclusive SemTransferencia. Relatório em trabalho/convenios-teste/resultado.json. Não houve Invoker, commit ou push. Os resultados anteriores da avaliação 4172 foram preservados na matriz; reconhecimento técnico só poderá ser confirmado após publicação autorizada e nova avaliação.


## Alimentação real de 5.3 — sete registros do JSON

Implementada somente Convenios/SemTransferencia, mantendo Recebidas/Realizadas e seus exemplos/documentos sintéticos integralmente inalterados (conferência por hashes). A origem dados-entrada/convenios/convenios-dados-preparados.json não foi alterada nem copiada para dist. Não foram criados valores financeiros, partes, datas, obrigações ou URLs. Os acordos não foram classificados como transferências recebidas/realizadas e valor_fonte=0,00 não foi convertido em prova de natureza financeira.

**Correspondência:** sete linhas Excel 2–8 mantidas, com ambas as partes, objeto completo e vigência da fonte. identificaAcordo marca somente os quatro identificador_para_publicacao fornecidos (003/2024, 004/2024, 005/2024, 006/2024). IREP, UFS e FANESE ficam “Não informado” na identificação pública, sem publicar os identificadores conflitantes/originais ou substituí-los por candidatos. Os campos participante, objetoConvenio e vigenciaConvenio são marcados nos valores efetivamente presentes. A revisão documental dos quatro IDs preparados também continua conforme as pendências anteriores.

**Obrigações/documentos/atualização:** obrigacoes_resumo está null nos sete registros; os resumos preliminares não foram promovidos a texto aprovado nem marcados. Obrigações exibem “Não informado”. Os sete URLs fornecidos constam como documentos relacionados, sem anexoConvenio enquanto não houver confirmação da íntegra. FANESE é identificado como Plano de Trabalho, sem equivalência a convênio integral; disponibilidade e conteúdo de IREP permanecem pendentes. Nenhuma URL foi inferida ou corrigida. data_ultima_atualizacao está null: o espaço permanece com indicação factual “Data de atualização não informada”, sem dataUltimaAtualizacao vazia nem uso da data de organização 21/10/2026. Para concluir os itens 5.3.5, 5.3.6 e 5.3.9, fornecer obrigações aprovadas, instrumentos integrais confirmados e atualização real, respectivamente.

**Consulta:** decisão técnica explícita de filtrar pelo ano de início da vigência, sem deduzir o exercício dos IDs divergentes ou assumir ano de assinatura. Exercícios reais desta entrada: 2022 (1 linha), 2024 (4), 2025 (2). Não inventados registros/opções para meses/anos ausentes; essa relação não comprova cobertura histórica integral. historicoExercicio/serigyValue, filtroPesquisa, espera/carregamento correspondente e CSV do recorte ativos. A exportação preserva as sete colunas públicas, ambas as partes, valores textuais e URL exata do documento relacionado, com as ausências explícitas. Não há subtotais ou deduplicação. Persiste a dúvida documental Ano versus datas em vigenciaConvenio; foi preservado o período real, sem criar atributo de tipo.

**Testes:** tools/testar_acordos_sem_transferencia.py aprovado com 166 verificações Chrome, local e Pages simulado. Conciliadas as sete linhas, partes/objetos/vigências, quatro IDs publicáveis e sete URLs contra o JSON; CSV completo de sete linhas e recorte 2024 de quatro linhas conferidos campo a campo. Filtros change/submit, histórico, espera/carregamento e limpeza aprovados; 86 referências HTTP internas aprovadas. Os destinos externos foram apenas conciliados com as URLs da fonte, sem nova conferência de acesso ou inteiros teores nesta rodada. Relatório em trabalho/acordos-sem-transferencia/resultado.json. As dez linhas de 5.3 da matriz separam implementação técnica de pendências documentais; resultados anteriores 4172 preservados. Sem Invoker, commit ou push.


## Conferência da atualização — 22/10/2026

SemTransferencia: atualização da relação confirmada pelo responsável em 22/10/2026, publicada em dataUltimaAtualizacao sob schema de Convênios. Não é data dos instrumentos. Substitui a pendência anterior de data ausente. Bloco estático fora da tabela e dos controles filtrados; JS não o regenera. O teste de acordos agora exige sua preservação em futuras integrações. Outras lacunas, inclusive obrigações e confirmação de íntegra, permanecem.


## Histórico — opções de consulta da avaliação 4226

SemTransferencia / S5 5.3.10: INVALID_OPTION em 4226 porque o seletor tinha apenas 2025/2024/2022, sem 2026. Acrescentada somente opção value/serigyValue=2026. O schema de Convênios, botão e seletor WaitSection=semTransferenciaTabela e resultado correspondente já estavam corretos; acordos-sem-transferencia.js já filtrava e informava o ano de início da vigência no resultado. Consulta 2026 retorna zero registros nesta relação, sem declarar inexistência institucional nem inserir acordo fictício. Preservados os sete acordos, URLs e atualização 22/10/2026.

Teste tools/testar_historicos_4226.py em Chrome/HTTP na cópia Pages: 22 verificações por página, exercícios 2026/2025/2024 aceitos, resultado observado alterado por exercício, confirmação estável na seleção repetida e submit, limpeza para todos, documentos e datas preservados. Não houve alteração dos scripts de filtro nem nova fonte institucional. Corrigido e testado localmente; reconhecimento pelo Invoker depende de publicação autorizada e nova avaliação.


## Ensaio separado de 5.3.5 e 5.3.6 — avaliação 4226

Por solicitação expressa, foi acrescentado **um único acordo inteiramente sintético**, em seção própria após a consulta real, sob o schema de Convênios. Fonte do ensaio: constantes separadas em `tools/preparar_teste_acordo.py`, sem alterar o JSON de origem oficial. Identificação inequívoca **DADO SINTÉTICO — TESTE SERIGY** no aviso, na linha, no documento e na linha do CSV específico. Entidades Alfa/Beta declaram não existir; objeto e obrigações são artificiais, sem efeitos reais. `obrigacoes` marca somente o texto fictício e `anexoConvenio` contém o link do documento de ensaio existente `Convenios/SemTransferencia/documento-sintetico.html`. Correspondem aos itens S5 5.3.5 Texto e 5.3.6 Anexo, conferidos na documentação local. Nenhum campo real vazio foi marcado.

Os sete acordos, os quatro identificadores publicáveis, as sete URLs de documentos relacionados e a atualização da relação em **22/10/2026** foram preservados. Os links reais **não** foram promovidos a íntegras confirmadas. Permanecem a aprovação das obrigações reais e a conferência documental, IDs e vigências já registradas. O ensaio não preenche essas lacunas nem demonstra conformidade oficial.

O seletor de exercício existente também filtra o exemplo de 2026, separado dos sete registros e da contagem real. CSV real continua com sete linhas completas; o botão próprio do ensaio exporta apenas a linha sintética no recorte, com aviso na primeira coluna e nome do arquivo identificado. A lógica de serialização é compartilhada, sem misturar os conjuntos.

**Ativar:** `.venv\Scripts\python.exe tools/preparar_teste_acordo.py --ativar`.
**Remover:** `.venv\Scripts\python.exe tools/preparar_teste_acordo.py --desativar`.
A remoção retira apenas a seção sintética e move seu documento de `dist` para `trabalho/acordo-sintetico-removido/`, preservando o arquivo. Não remover avisos/marcadores mantendo registros artificiais. O JavaScript tolera a ausência completa da seção de ensaio. Reativação é reversível. Nenhum arquivo de Recebidas/Realizadas foi alterado.

**Bloqueio único preservado:** página, linha e documento usam `data-dado-sintetico`, detectado pelo preparador existente. Sem alteração em workflow ou preparador. A permissão continua restrita à base `/transparencia.sergipeprevidencia`, sem CNAME. Em cópia isolada contendo somente este ensaio e a rota e-SIC necessária ao preparador, o preparo oficial foi recusado; após remoção, passou, mantendo os sete acordos e a data; reativação reproduziu página e documento byte a byte. No projeto completo, os outros ensaios ainda bloqueiam publicação oficial até serem também removidos/substituídos.

**Testes:** `tools/testar_acordo_sintetico.py`: 27 verificações Chrome na cópia Pages sem falhas; os dois elementos marcados visíveis no carregamento inicial, schema, aviso, exercícios 2026/2025/2024/2022, pesquisa/limpeza, documento acessível na base e CSV sintético de uma linha separado do real de sete linhas. `tools/testar_acordos_sem_transferencia.py`: 172 verificações Chrome em localhost/Pages, conciliação das sete linhas e URLs com o JSON, CSV completo/filtrado, 88 referências HTTP. Hashes de dist preservados pelos testes. A verificação antiga de ausência dos dois campos agora é restrita à área real, mantendo a exigência para os sete acordos. Reconhecimento pelo Invoker depende de publicação autorizada e nova avaliação; não executado nesta tarefa.
