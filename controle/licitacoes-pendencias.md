# Licitações — pendências dos modelos

Escopo dos controles: C 8.1–8.7 / S 8.1–8.3. Mapeamento em `controle/licitacoes-modelos.md`. Não há dados ou documentos institucionais homologados nos modelos. As pendências originais de C 8.1–8.5 são preservadas abaixo; o HTML principal permanece inalterado.

## Modelo principal — C 8.1–8.5 / S 8.1

| Seção / requisito | Dado ou documento faltante | Providência |
| --- | --- | --- |
| Relação — C 8.1 | Catálogo real de licitações em andamento e encerradas, dispensas e inexigibilidades pertinentes; número/ano, modalidade, objeto, abertura, valor e situação | Receber fonte oficial e confirmar universo e exceção das compras diretas de pequeno valor, sem assumir que a autarquia não licita. |
| Ordem e identidade — C 8.1 / S `sequencia` | Regra de ordenação numérica e chave inequívoca entre procedimentos, anos/modalidades e documentos | Confirmar números repetidos e ordenação; não usar ordinal como número do certame nem colapsar registros por número isolado. Chave interna é DT, não novo item S. |
| Data e filtro — C 8.1 | Data real de abertura e referência de mês/ano para diretas sem sessão | Esclarecer com a área a apresentação desses casos; não inventar abertura, usar data de arquivo como fato ou marcar data desconhecida como disponível. |
| Valor e situação — C 8.1 | Valor estimado ou homologado devidamente identificado, situação real e referência | Confirmar conceitos e atualizações; não deduzir homologação da presença de arquivo nem substituir ausência por zero. S tipa data como Texto e valor como Número: não criar tipos/propriedades extras. |
| Editais — C 8.2 / S `editalLicitacao` | Íntegras e anexos integrantes dos certames em andamento e encerrados | Conferir documento por procedimento e acesso público direto. Ementa ou link à capa do PNCP não basta. |
| Fases — C 8.3 / S `docFasesLicitacao` | TR/projeto/equivalente, justificativa, pareceres, orçamento/preço, edital/anexos, atas, recursos/impugnações e análises quando houver, adjudicação/homologação | Inventariar por fase/documento e apontar quais existem ou estão em outro documento; conferir íntegra e pesquisa/seleção de texto. Não inventar etapas nem declarar inexistência por arquivo ausente. |
| Diretas — C 8.4 / S `docDispensaLicitacao` | TR/projeto/equivalente, justificativa de fornecedor/preço, caracterização da emergência/calamidade/risco e pareceres quando cabíveis, homologação/ratificação | Confirmar regime e alcance da ressalva de pequeno valor; não aplicá-la a toda contratação direta. Conferir pesquisa/seleção de texto ou valor e vínculos externos admitidos. |
| Adesões — C 8.5 / S `atasLicitacao` | Atas integrais das adesões realmente realizadas e referência ao procedimento | Confirmar que o documento é de adesão da Unidade, não apenas ata geral SRP. Não presumir adesão por contrato semelhante. |
| Histórico — C 8.1–8.5 | Acervo de pelo menos três anos anteriores ao da consulta, inclusive os documentos de cada grupo | Conferir cobertura por critério; publicar documentos reais sem preencher anos com fatos fictícios. Esclarecer lacunas e eventual não ocorrência com a instituição. |
| Filtros — C 8.1–8.5 / S `filtroPesquisa` | Opções reais de ano, mês, situação e modalidade e identificação dos documentos associados | Implementar recortes combináveis da relação e localização dos documentos; não transformar filtros mínimos de 8.1 em parâmetros normativos novos para 8.2–8.5. |
| Exportação — somente C 8.1 / S `salvarRelatorio` | Arquivo editável do recorte com todos os mínimos | Implementar ao menos um formato; evitar multiplicar procedimentos/valores pelo número de anexos. Downloads dos documentos continuam próprios, não substituídos pela exportação do resumo. |
| Atualização — C 8.1–8.5 / S `dataUltimaAtualizacao` | Datas reais, coberturas e responsáveis da relação e de cada grupo documental | Conferir o parâmetro de até 30 dias separadamente; não usar geração/importação nem uma data do resumo para todo o acervo. |
| Associação, documentos e dados pessoais | Chave procedimento–documento; versões oficiais adequadas e URLs conferidas | Validar correspondência, íntegra, legibilidade e acesso sem login. Não publicar arquivos privados/credenciais ou dados pessoais adicionais por cópia bruta. Não construir URLs ou usar `serigyLink` para PDF. |

Antes de mover para `dist`: resolver as pendências pertinentes, receber e conferir dados/documentos, implementar controles e vínculo por registro, preencher datas e só então marcar conteúdo real. A tabela e as listas vazias atuais não comprovam não ocorrência nem atendimento. O modelo não foi adicionado ao menu público; nenhuma comunicação externa foi enviada.


## PlanoAnualContratacoes — C 8.6 / S 8.2

| Requisito | Dado/documento necessário | Providência antes da publicação |
| --- | --- | --- |
| Plano consultável | PCA oficial do exercício atual, completo e com eventuais anexos integrantes confirmados | Obter o arquivo ou URL direta conferida; validar Unidade, exercício e versão com a área responsável. Não criar plano ou itens de contratação sem fonte. |
| Atualidade C / S `dataUltimaAtualizacao` | Exercício do plano e data real de atualização/cobertura | Conferir que é o PCA do exercício exigido. Data de geração/upload não substitui a referência real nem torna um plano antigo atual. |
| Documento / S `contratacoesAnual` | Arquivo/URL pública correspondente, sem login | Conferir destino e íntegra; não construir URL ou usar `serigyLink` para PDF. Identificar versões/anexos sem inventá-los. |
| Ausência de PCA | Esclarecimento institucional se o plano não for disponibilizado | Registrar a lacuna: C p. 72 rejeita declaração de inexistência/não elaboração como atendimento. Não publicar declaração fictícia nem marcar o critério como atendido por ausência. |
| Controles | Nenhuma exigência própria de filtro, histórico ou exportação em C 8.6 / S 8.2 | Preservar a apresentação documental; não copiar controles de Sanções/listagem como obrigações do PCA. |

## Sancoes — C 8.7 / S 8.3

| Requisito | Dado/arquivo necessário | Providência antes da publicação |
| --- | --- | --- |
| Universo de sanções / S `nomeSancionado` | Relação oficial dos licitantes/contratados sancionados pela Unidade nas hipóteses indicadas em C p. 73 | Confirmar autoria e enquadramento com a área responsável. Não importar indiscriminadamente registros de outros órgãos nem copiar nomes S. |
| Identificação adicional S `idSancionado` | CNPJ/CPF confiável e versão publicável, associada ao mesmo sancionado | **DÚVIDA — REVISÃO NECESSÁRIA:** confirmar origem e tratamento com a instituição; não inventar identificação ou máscara. C exige mínimo nominal; S acrescenta a identificação. Não publicar cadastro bruto com informações pessoais adicionais. |
| Histórico / S `historicoExercicio` | Acervo de pelo menos três anos anteriores ao da consulta e referência temporal das ocorrências | Definir com a fonte como representar sanções, alterações e recortes anuais sem repetir dados por cópias de arquivos ou deduzir vigência. Popular somente exercícios reais. |
| Filtro / S `filtroPesquisa` | Registros reais e parâmetros DT de nome/exercício | Implementar consulta do conjunto; C não enumera filtros mínimos específicos neste critério. Não exigir CPF conhecido pelo visitante nem copiar filtros de modalidade/situação da listagem. |
| Gravação / S `salvarRelatorio` | Editável ou PDF pesquisável correspondente ao conjunto selecionado | Implementar pelo menos uma alternativa aceita em C p. 74, incluindo os campos publicáveis confirmados. Não anunciar recorte para download estático sem correspondência. |
| Atualidade / S `dataUltimaAtualizacao` | Data real da relação, cobertura e responsável | Confirmar o parâmetro de até 30 dias; não usar a data de importação/geração. |
| Documentos de origem | Evidência oficial para conferência dos registros quando necessária | Obter apoio da área sem transformar ato sancionatório integral em anexo mínimo não enumerado em C 8.7. Não criar documento/URL fictício para preencher a relação. |
| Eventual não ocorrência | Confirmação institucional do período sem sanções, se verdadeira | Não inferir inexistência a partir da tabela/arquivo ausente nem publicar nomes substitutos. Nenhuma declaração foi inserida no modelo. |

PCA e Sanções permanecem fora de `dist`, sem links novos no menu público. Liberar cada página somente após receber e conferir suas fontes, preencher referências reais e implementar os controles aplicáveis, sem atribuir marcações de dados a posições vazias. O modelo principal, Diárias e o deploy não são alterados por este complemento.


## PCA — inclusão de links na página pública em 21/10/2026

A página `dist/Portal-da-Transparencia/Licitacoes/PlanoAnualContratacoes/index.html` recebeu os endereços literais de `dados-entrada/licitacoes/pca.txt`, para PCA 2026 e 2025, com `contratacoesAnual` (S 8.2.1 / C 8.6) sob o schema de Licitações. A atualização da relação no Portal, informada para 21/10/2026, foi marcada com `dataUltimaAtualizacao` (S 8.2.2); não corresponde à emissão dos documentos.

**Pendência:** os PDFs ainda serão carregados nesses endereços. Conferir acesso público sem login, conteúdo integral, anexos pertinentes e correspondência de cada documento com seu exercício e com a Unidade. Os links fornecidos não constituem documentos validados nem comprovam atendimento integral ao critério. A referência anterior a modelos fora de `dist` é histórica; esta inclusão diz respeito somente à página pública do PCA.

- PCA 2026: https://sergipeprevidencia.se.gov.br/wp-content/uploads/2026/05/pca-2026-comprasnet.pdf
- PCA 2025: https://sergipeprevidencia.se.gov.br/wp-content/uploads/2026/05/pca-2025-comprasnet.pdf


## Sanções — declaração recebida e publicada em 21/10/2026

Informação institucional recebida nesta tarefa: não houve licitantes ou contratados sancionados administrativamente pela própria unidade até 21/10/2026. Publicada na página `dist/Portal-da-Transparencia/Licitacoes/Sancoes/index.html`, com `dataUltimaAtualizacao` (Serigy 8.3.5 / Cartilha 8.7) sob o schema de Licitações. A data identifica a atualização da informação, não o início da série histórica.

**Pendências:** obter confirmação institucional formal da ausência de sanções e do período exato abrangido, inclusive seu início e cobertura dos três anos anteriores à consulta; não presumir ausência desde a criação nem declarar série histórica integralmente atendida. Confirmar o alcance das hipóteses de sanções previstas no critério 8.7. Revisar a informação quando houver fatos posteriores.

**Marcação de conjunto sem registros:** a seção Serigy 8.3 apresenta campos nominais e de identificação para registros existentes, mas não exemplifica declaração de não ocorrência. Definições prevê `serigyEmpty` em um item sem conteúdo, com motivo único e `serigyItem`, exemplificando formato de exportação ausente; não define atributo de conjunto vazio para Sanções. Não foram criados `serigyEmpty`, nomes/identificações, filtros, exportações ou históricos fictícios. Confirmar no Invoker a leitura da declaração textual, sem inferir homologação ou atendimento integral. As referências anteriores a modelos fora de `dist` são históricas; esta atualização se limita à página pública de Sanções.


## Sanções — ensaio técnico sintético autorizado (S8 8.3.1–8.3.6)

Por solicitação expressa desta rodada, foram acrescentados quatro registros inteiramente sintéticos, exercícios de teste 2023–2026, em bloco separado da declaração institucional. A declaração de que a própria unidade não aplicou sanções até 21/10/2026 e o bloco dataUltimaAtualizacao de 21/10/2026 foram preservados integralmente, sem duplicação ou nova data. Os exercícios de teste não comprovam o início da série histórica oficial. Continua pendente a confirmação formal do período abrangido pela declaração, inclusive seu início e a ausência de sanções.

Aviso na página, em cada linha e no CSV: **DADOS SINTÉTICOS PARA TESTE DO SERIGY — NÃO REPRESENTAM SANÇÕES DO SERGIPEPREVIDÊNCIA**. Os nomes “ENTIDADE SINTÉTICA DE TESTE … — NÃO EXISTE” não representam pessoas/empresas reais. Os CNPJs 00.000.000/0000-01 a -04 são exemplos fictícios inválidos; não foram usados documentos reais ou dígitos verificadores válidos. nomeSancionado e idSancionado marcam somente estes dados de teste, sob o schema de Licitações.

filtroPesquisa, historicoExercicio/serigyValue, serigyExecuteWaitSection correspondente ao serigyLoadSection de resultados e salvarRelatorio/csv estão ativos. O filtro por exercício é escolha técnica para o conjunto de teste; não foi inventado requisito formal de filtros adicionais. Seleção, pesquisa e limpeza alteram os resultados sem remover os registros do HTML inicial. CSV mantém exatamente as quatro colunas e o aviso individual, nomeado SINTETICOS-TESTE-SERIGY. A declaração real não é exportada como linha sancionatória nem transformada em registro de teste. Não foi criado serigyEmpty ou ato sancionatório fictício.

**Mesmo bloqueio oficial:** data-dado-sintetico e o aviso são reconhecidos pela proteção já existente no preparador. Nenhuma regra, flag ou modo de deploy adicional foi criado; somente a orientação da recusa passou a incluir Sanções. Permissão continua limitada à base /transparencia.sergipeprevidencia, com --permitir-dados-sinteticos e sem CNAME. Para retirar o ensaio, remover o bloco ensaio-sancoes e sua carga de script, preservando o restante da página — especialmente a declaração e atualização — ou substituí-lo por fonte oficial se houver alteração institucional. Não basta retirar marcadores/avisos mantendo exemplos. Em cópia, a retirada do bloco preservou a declaração e a data, e o mesmo bloqueio aceitou a página sem sintéticos. Outros conjuntos de teste ainda ativos continuam impedindo o preparo oficial global.

**Testes:** tools/testar_sancoes_sinteticas.py aprovado com 66 verificações Chrome em localhost e Pages simulado, seis marcações no HTML inicial, quatro registros, filtros change/submit, histórico, espera/carregamento, limpeza e CSV filtrado (uma linha) e completo (quatro), conferidos em todos os campos. Conferidas 86 referências HTTP internas e quatro recusas de preparo com Sanções isoladas, sem depender de Despesas/SIC/Convênios: raiz, base errada com permissão, Pages sem permissão e CNAME. A saída anterior foi preservada nas recusas; demais arquivos dist permaneceram inalterados. Relatório em trabalho/sancoes-sinteticas/resultado.json. Resultados reais 4172 preservados na matriz; o ponto aprovado de atualização não foi tratado como novo resultado. Sem Invoker, commit ou push.


## Alimentação da consulta principal — relação de licitações

Fonte: `dados-entrada/licitacoes/relacao-licitacoes.xlsx`, aba Plan1, linhas 2–97. Integração por `tools/integrar_licitacoes.py`, conferência por `--check`. Publicados os 96 registros: 2023=3, 2024=40, 2025=31, 2026=22, sem deduplicação ou exclusão de modalidades. Histórico pelo Ano literal da fonte; mês exclusivamente da abertura válida, sem deduzi-lo de outra data. Número identificador e processo são preservados, sem criar numeroLicitacao ou sequência ordinal a partir da posição na planilha. Não há campo confirmado de sequência: `sequencia` permanece pendente.

Mapeamento S8 8.1: Modalidade → modalidadeLicitacao; Objeto → objetoLicitacao; Situação / Etapa → faseLicitacao; Valor-Total-Referência → valorLicitacao, identificado como referência (confirmar natureza estimada e cobertura). Valor-Total-Arrematado é apresentado separadamente sem ser chamado de homologado e sem assumir equivalência ao valor de referência. Precisão decimal e zeros preservados; ausências não viraram zero. Data-Abertura → dataLicitacao somente nas 11 datas válidas. Nenhuma data de publicação, início, término, adjudicação ou homologação foi usada como abertura. Confirmar as lacunas indicadas abaixo.

Links preservados com destino real de hiperlinks quando existentes, ou URL textual efetivamente fornecida: Edital (AD): 11 editalLicitacao; Documentos Fase Licitação (AE): 11 docFasesLicitacao; Documentos Fase Dispensa e Inexigibilidade (AG): 85 docDispensaLicitacao. Total 107 links associados às próprias linhas. Não foi fornecida classificação documental confirmada para atasLicitacao. Não criar vínculo por nome de PDF ou modalidade. Os PDFs ainda dependem de carregamento/conferência nos endereços indicados: verificar acesso, inteiro teor, pesquisa de texto e correspondência antes de afirmar sua disponibilidade. Os testes desta tarefa não consultaram documentos externos nem os declararam validados.

Atualização da relação informada pelo responsável: 22/10/2026, em dataUltimaAtualizacao sob schema https://serigy.tce.se.gov.br/comum/licitacoes.html; não é data de emissão dos documentos. Filtros combináveis de ano, modalidade, situação, texto e mês de abertura; filtroPesquisa, historicoExercicio/serigyValue e Wait/Load com identificador licitacoesTabela. CSV do recorte com todas as dez colunas e URLs, sem duplicação por documento. Registros mantidos no HTML inicial.

Validação: 28 verificações em Chrome/HTTP local sem falhas; filtros, histórico, pesquisa combinada, limpeza, recorte sem resultados, CSV integral e filtrado. CSV integral conciliado campo a campo com os 96 registros e 107 URLs da fonte; destinos internos HTTP conferidos. Validador: 45 páginas. PCA, Sanções e demais arquivos dist comparados por hash e preservados. Conferência não comprova completude histórica ou atendimento integral.

Lacunas por linha de origem (sem corrigir a fonte):

- referencia_ausente_ou_invalida: [2, 7, 8, 9, 10, 11, 12, 13, 14, 16, 63, 77].
- arrematado_ausente_ou_invalido: [16, 69].
- abertura_ausente: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86].
- abertura_invalida: [].
- hiperlinks_reais: 0.


## Adesões/SRP provenientes da extração de Contratos — S8 8.1.10

Acrescentados oito links em seção documental própria de Licitações, com atasLicitacao: linhas CONTRATOS 19, 61, 62, 63, 129, 184, 185 e 186 do JSON contratos-extraidos.json. Evidência de adesão explícita na coluna B (Termo de Adesão) ou no objeto (linha 19), não inferida do nome do PDF. Identificações, partes e URLs preservadas; as três linhas da ata 018/2024 continuam separadas por contratada. Acesso e correspondência integral dos PDFs continuam pendentes de conferência, inclusive aqueles cujo nome sugere contrato. A classificação nesta etapa decorre da indicação explícita da fonte, não de auditoria do documento.

Separados, sem marcação nem link na seção de adesões: linha 17 (ata 001/2022 com URL, mas sem evidência de adesão); linha 49 (ata 004/2021 sem URL e sem confirmação de adesão). Preservadas como pendências sem documento fictício as três linhas sem URL: 49, 59 e 60; estas duas últimas explicitam Termo de Adesão 004/2022 e 005/2022. Obter os documentos e confirmar natureza e cobertura antes de incluir. Não associar esses registros aos 96 procedimentos por aproximação.

O gerador de Licitações preserva a seção na regeneração. Consulta e CSV existentes continuam restritos aos 96 procedimentos e 107 links originais; as oito adesões ficam em índice documental autônomo, sem serem duplicadas como certames ou misturadas aos totais. Atualização de 22/10/2026 preservada.
