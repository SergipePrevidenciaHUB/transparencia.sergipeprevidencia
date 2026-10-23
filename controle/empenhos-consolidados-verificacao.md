# Empenhos 4.3 - conferência interna

## Consolidação e fontes
- Base principal: empenhos-final.xlsx, Plan1, 3.282 linhas CGE do SergipePrevidência. Mantidos números, datas, nomes, procedimentos, identificadores, modalidades, objetos e valores. Os quatro campos monetários foram convertidos de texto BRL para números, sem mudar seus valores.
- Complementos FINANPREV/FUNPREV: RelatorioDemonstrativoGerencialEmpenhos como âncora. Chave UG + gestão/UO + número completo da NE + exercício da própria nota. Há 1.223 notas FINANPREV e 12 FUNPREV: total principal de 4.517 notas.
- Foram evitadas 2.761 repetições de notas provenientes de liquidações/itens. Data, credor e totais financeiros são invariáveis em cada nota nas linhas gerenciais; os totais foram tomados uma única vez, sem somar seus valores repetidos.
- Enriquecimento de objeto e modalidade: cruzamento exato com Emitidos, exigindo também documento do credor correspondente. Objetos distintos da mesma nota foram preservados concatenados, sem repetir valores. Nenhum cruzamento aproximado/fuzzy nem atribuição inventada de licitação.
- 1.054 notas existem em Emitidos e não na âncora Gerencial. Foram preservadas para conferência no CSV e na aba “Emitidos sem gerencial”, com documentos mascarados. Não foram integradas à tabela principal: falta data de geração e total atualizado comprovados na base Gerencial. Valor original B não foi tomado automaticamente como atualizado.
- As contagens por ano/entidade e os hashes dos arquivos estão no JSON e na aba Fontes. A cobertura não prova completude da extração contábil.

## Pendências essenciais
1. O arquivo Emitidos-FINANPREV-2024 contém notas 2023. Foi usado somente para as chaves reais 2023; não reclassificar por causa do nome do arquivo. Faltam os objetos de 229 notas FINANPREV/2024. Solicitar o relatório Emitidos correto desse exercício.
2. Solicitar o Gerencial correspondente às 1.054 notas adicionais de Emitidos para decidir sua incorporação, preservando todas as informações recebidas no controle enquanto isso.
3. Não declarar que todas as despesas dos fundos são não licitáveis. Há sete notas com modalidade de concorrência ou inexigibilidade na fonte B; conferir antes de afirmar não aplicabilidade. Outras naturezas de serviços/restituições/exercícios anteriores também exigem análise.
4. Nos fundos, 1.035 notas foram classificadas sem procedimento aplicável com suporte em natureza de benefício previdenciário, sentença judicial, obrigação tributária ou compensação previdenciária. Em 200 a aplicabilidade ficou a confirmar; procedimento permanece vazio, sem zero ou número inventado. A natureza e a justificativa foram registradas. “DISPENSADO/ISENTO”, isoladamente, não foi tratado como prova.
5. Preservar os procedimentos e modalidades originais CGE do Instituto. A existência de um número na origem não equivale a nova conferência da íntegra da contratação. Ausências nas despesas licitáveis seguem na aba Pendencias; não completar por associação textual.
6. FUNPREV só tem dados 2026 nestes arquivos. Não criar anos ou meses artificiais. Exercício da NE e data de geração foram preservados, sem imputar meses a Emitidos sem Gerencial.
7. A exportação CGE do Instituto informa unidade como “SERGIPE PREVID.”, compatível com o agrupamento da UG 372011 já trabalhado. Não afirmar uma única UO nem somar novamente dados antigos do Instituto/SPSM.
8. A base Gerencial não fornece função e subfunção nesses arquivos; esses campos suplementares ficam vazios nos fundos. A ausência não foi preenchida por suposição. Elemento, fonte, ação e unidade reais foram preservados em campos próprios.
9. Valor atualizado foi calculado como original + reforçado - anulado para o Instituto. Nos fundos, essa fórmula confere com TOTAL EMPENHADO em todas as 1.235 notas. A planilha mantém fórmula auditável e o JSON mantém centavos inteiros. Valor executado não foi tratado como pago, liquidado ou atualizado.
10. Totais de empenhos individuais são saldos por nota; não usar para sobrescrever totais mensais de 4.1/4.2. O mês identifica o lançamento da NE, não o mês dos movimentos de reforço, anulação, liquidação ou pagamento.

## Privacidade da preparação
- 1.524 linhas da base principal contêm CPF e estão mascaradas: ***.***.***-NN. É máscara de divulgação, não anonimização: os nomes e demais informações públicas continuam vinculáveis.
- CNPJ (2.756 linhas) e identificadores IG/outros (237) foram preservados conforme origem. Documento foi mantido como texto para não perder zeros iniciais.
- CPFs completos não fazem parte do JSON, CSV ou XLSX preparados, inclusive abas internas de conferência e adicionais. As descrições livres foram submetidas a redação preventiva de padrões de CPF. Não foram incluídos índices de hash de CPF, chaves ou versões ocultas do documento.
- Arquivos originais não foram alterados e não estão dentro do pacote. Mantê-los sob controle de acesso fora do repositório público, de dist, _site, artefatos de CI e downloads.
- Inspeção da versão publicada: a página tem filtro genérico por documento; o JavaScript despesas-totais.js filtra no navegador e não contém chamada fetch para uma API de consulta de CPF. Não é prova do estado atual dos arquivos locais do Codex. Ele deverá conferir o código local antes de alterar.
- Não basta esconder o CPF no DOM, usar CSS, input password, Base64, cifra com chave no JS, hash simples ou salted hash público. Não disponibilizar o original no cliente.
- Consulta por CPF completo depende do servidor descrito em empenhos-api-cpf-requisitos.md. Enquanto não houver backend real, esse filtro específico deve permanecer ausente/inativo, com pendência expressa somente no controle. Não simular pesquisa com os dois dígitos visíveis da máscara.

## Conformidade e teste
Cartilha 4.3 exige credor, objeto, valor e procedimento/modalidade quando aplicável, detalhe individual, atualidade em 30 dias, três exercícios anteriores, exportação editável e filtros por NE, nome, CPF/CNPJ, mês e exercício. A preparação supre a estrutura e os dados existentes, mas falta o complemento 2024, confirmação das despesas licitáveis, completude e uma consulta segura por CPF no servidor. A data de alimentação autorizada é 22/10/2026; não prova atualização contábil em 30 dias.
Serigy: https://serigy.tce.se.gov.br/petp/comum/despesas.html. Campos credorEmpenho, objetoEmpenho, modalidadeEmpenho, numeroProcedimento e valorEmpenhoIndividual. O CPF não possui serigyItem próprio nessa dimensão. Não inventar marcadores de CPF. Ausências legítimas não devem ser marcadas como documentos ou valores reais; usar serigyEmpty somente conforme regra aplicável documentada.
Verificações da preparação: 4.517 chaves públicas únicas, totais gerenciais invariáveis e não duplicados, cálculo atualizado conciliado em 1.235 notas dos fundos, rastreio exato e projeção pública mascarada. Exportação XLSX e inspeção das fórmulas realizadas; servidor, aplicação local do usuário e Invoker não executados.


## Integração pública de 4.3 — 23/10/2026

Integradas somente as 4.517 notas da projeção pública: 3.282 SergipePrevidência, 1.223 FINANPREV e 12 FUNPREV, conforme as nove contagens por exercício/entidade do resumo. As 1.054 notas adicionais não foram incorporadas. Não houve reextração ou associação aproximada. Os 18 campos da origem foram conservados, com valor atualizado em coluna adicional e detalhe individual acessível. Campos ausentes permanecem vazios e sem marcação como fato disponível. Valor executado não foi apresentado como pago/liquidado; os saldos por nota não alteram 4.1/4.2.

Gerador `tools/integrar_empenhos.py`, com `--check`, utiliza somente `empenhos-consolidados-publicos.json` e valida máscaras antes de produzir HTML. Não lê originais completos nem produz índices de CPF. Rejeita CPF completo formatado nas strings e candidatos de CPF não formatado em nome/objeto, além de máscara inválida no campo tipado CPF. Mantidos 1.524 documentos mascarados, 2.756 CNPJs e 237 identificadores de outra natureza. Projeção pública e CSV não contêm documentos completos desses titulares. A máscara continua não sendo anonimização.

Pesquisa por CPF completo **não está implementada** e depende da infraestrutura de `empenhos-api-cpf-requisitos.md`. Não foi criada API fictícia. O campo público busca CNPJ/identificador, exclui registros tipados CPF e recusa entrada numérica com 11 dígitos ou máscara; não usa os dois dígitos da máscara como pesquisa. Nenhum envio de CPF, chave, índice derivado, armazenamento ou consulta remota foi adicionado. A consulta por nome e NE permanece disponível. Dados preparados não permitem reconstruir uma base privada; originais restritos fora do repositório não foram fornecidos/conferidos nesta rodada.

Atualização da alimentação mantida em 22/10/2026, sem afirmar fechamento/atualidade contábil. Filtros por exercício, mês de lançamento, entidade, NE, nome e documento público; histórico 2026/2025/2024/2023 com value/serigyValue e espera/carregamento alinhados. As cinco marcações de dados são usadas apenas em conteúdos presentes. Ausências de objeto/procedimento e aplicabilidade continuam nas pendências da preparação, sem números inventados.

Conferidos HTML e CSV contra os 4.517 registros; valores atualizados de todas as notas e três exemplos de notas dos fundos com linhas gerenciais repetidas; filtro combinado, CSV, detalhe, limpeza e recusa de documento fictício de 11 dígitos. Cópia real do preparador Pages em pasta nova sob trabalho; nenhum arquivo de origem foi copiado por esta integração. Conferidos desktop/celular e integridade de 4.1/4.2, demais alterações e staging por hashes. O preparador sintético antigo não foi executado sobre dist; seu bloqueio por divergência do conteúdo real foi preservado. Ensaios de outras áreas continuam bloqueando o preparo oficial global. Não houve Invoker, commit ou push.

### Auditoria de exposição preexistente — pendência antes de publicação definitiva

Varredura textual dos arquivos públicos e extração automática de texto dos PDFs no pacote Pages identificaram **três candidatos a CPF completo com dígitos verificadores válidos, uma ocorrência por arquivo**, fora da nova consulta:

- `Portal-da-Transparencia/Contratos/index.html`;
- `Portal-da-Transparencia/Institucional/AtosNormativos/portarias/2023/Portaria Nº 032-2023.pdf`;
- `Portal-da-Transparencia/Institucional/AtosNormativos/portarias/2023/Portaria Nº 036-2023.pdf`.

Não foram reproduzidos documentos nos logs/relatórios e esses arquivos não foram alterados. A validade dos dígitos não comprova identidade ou natureza real/fictícia; revisar a divulgação e providenciar redação/substituição autorizada em tarefa própria antes da publicação definitiva. A varredura não reescreve histórico Git nem demonstra que nunca houve exposição anterior. Não houve PDF sem texto ou falha de extração nessa execução; não foi realizado OCR de eventuais números existentes somente em imagens. Relatório com caminhos/contagens, sem documentos, em `trabalho/empenhos-publicos-x1ho57ed/privacidade.json`.

Nenhum CPF completo formatado foi encontrado na nova página de Despesas ou no CSV exportado no ensaio. Originais completos não foram lidos ou adicionados ao pacote; `.gitignore` não foi usado como prova de remoção de arquivos rastreados. A publicação definitiva depende também da resolução dos candidatos acima e das demais pendências institucionais, não só das marcações locais.


## Correção de visibilidade após avaliação 4252 — Empenhos: 4.1.11–4.1.14 e 4.1.19 do Serigy

A avaliação 4252 registrou SERIGYITEM_NOT_VISIBLE: as primeiras células marcadas pertenciam a linhas hidden fora do recorte inicial, não a falta de conteúdo nem a painel de detalhes. Geradores agora mantêm os campos elegíveis em data-serigy-item e aplicam serigyItem somente às células com conteúdo do recorte visível; os dois scripts removem/restauram a marcação ao filtrar e limpar. data-serigy-item é metadado interno de restauração, não um atributo de avaliação Serigy. Todos os registros continuam no HTML inicial, sem duplicação ou alteração de valores, máscaras, ordem ou CSV. Schema de Despesas preservado nos ancestrais; ações/espera e tabelas de resultados permanecem alinhadas. Conferidos HTML antes de JavaScript e Chrome em localhost/base Pages: 12 primeiras ocorrências visíveis no início, pesquisa combinada, mudanças de exercício/mês/entidade e limpeza; recorte 2023/FUNPREV vazio legítimo sem marcações de dados ou total zero inventado; dois CSVs por base iguais à fonte e três totais em centavos conciliados. Detalhes individuais preservados. A avaliação 4252 continua como resultado histórico reprovado; correção local ainda não publicada e reconhecimento depende de nova execução autorizada do Invoker. Evidência: trabalho/despesas-marcacoes-p8gu_ge6/resultado.json.
