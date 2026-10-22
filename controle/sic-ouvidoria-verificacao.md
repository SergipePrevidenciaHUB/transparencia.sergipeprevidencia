# SIC e Ouvidoria — verificação interna (21/10/2026)

Fontes: `11 - sic GPT.zip` e `13 - ouvidorias GPT.zip`; Cartilha PETP 2026, dimensões 11 e 13; Serigy Docs, páginas SIC e Ouvidorias. Este controle não integra o conteúdo público do portal.

## SIC

| Cartilha | Serigy | Material disponível | Estado | Providência |
|---|---|---|---|---|
| 11.1 | `setorResponsavel` | O responsável pelo SIC é Lucas Silva Pedrosa, da Ouvidoria-Geral do SergipePrevidência, conforme informação institucional recebida em 21/10/2026. | Conteúdo e marcação implementados | Conferir a designação na revisão final. |
| 11.2 | `enderecoSetor`, `telefoneSetor`, `emailSetor`, `horarioFuncionamentoSetor` | Endereço Praça General Valadão, 32; (79) 3198-0800; atendimento@sergipeprevidencia.se.gov.br; 7h–13h, dias úteis. | Conteúdo e marcações implementados | Confirmar os dados institucionais na revisão final. |
| 11.3 e 11.4 | `cadastroESIC` (redirecionamento ou formulário) | HTML aponta para página inicial do SE-Ouv, que distingue e-SIC de manifestações de Ouvidoria. | Parcial | Verificar o clique até o formulário específico, sua simplicidade e a leitura pelo Serigy. Docs exemplificam Fala.BR; não marcar um formulário próprio inexistente nem substituir o SE-Ouv por Fala.BR. Esclarecer equivalência com TCE/SE se o Invoker não reconhecer o fluxo. |
| 11.5 | `lai` | HTML contém link para o Decreto Estadual nº 30.947/2017. | Ato local e marcação implementados | Conferir disponibilidade do link e vigência do ato. |
| 11.6 | `prazoResposta`, `recursal`, `autoridadeExame`, `procedimentoPedido` | HTML e-SIC traz fluxos, prazos e instâncias. | Parcial | Conferir redação com o decreto e a designação efetiva da autoridade de monitoramento. |
| 11.7 | `pedidosRecebidos`, `pedidosAtendidos`, `pedidosIndeferidos`, `infoGenericas`, `filtroPesquisa`, `salvarRelatorio`, `historicoExercicio`, `dataUltimaAtualizacao` | 40 CSVs de 2023–2026 e links para relatório e consulta do SE-Ouv. | Pendente para o atendimento integral | Registrar zero indeferido informado pelo responsável como provisório e conferir depois em extração oficial por exercício; confirmar que a exportação se restringe a pedidos LAI, conferir último exercício encerrado e produzir tabela/CSV com filtro. 2026 é parcial (jan–out) e não substitui relatório anual 2025. |

### Conciliação preliminar dos CSVs do SIC

| Exercício | Soma por mês | Linha `Atendidas` | Indeferidos | Situação |
|---|---:|---:|---|---|
| 2023 | 4 | 4 | 0 informado, não comprovado no CSV | Total candidato; origem específica LAI ainda não comprovada. |
| 2024 | 9 | 9 | 0 informado, não comprovado no CSV | Total candidato; origem específica LAI ainda não comprovada. |
| 2025 | 3 | 3 | 0 informado, não comprovado no CSV | Total candidato; origem específica LAI ainda não comprovada. |
| 2026 jan–out | 2 | 2 | 0 informado, não comprovado no CSV | Período parcial, apenas complementar. |

**Problema de nomenclatura:** arquivos chamados `Manifestacoes-por-Escolaridade` contêm a coluna `Gênero`; `Manifestacoes-por-Estado`, `Escolaridade`; `Manifestacoes-por-Faixa-Etaria`, `Órgão`; `Manifestacoes-por-Genero`, `Renda`; `Manifestacoes-por-Renda`, `Faixa Etária`. Para qualquer perfil, usar o cabeçalho e conferir a origem. Os arquivos chamados `Manifestacoes-por-Orgao` apresentam números de situação muito superiores aos totais anuais (por exemplo, 934 `Finalizada` em 2023 versus quatro manifestações por mês somadas); não os somar nem tomar `Indeferido` dessas linhas como negativa LAI. O valor zero de indeferidos foi informado pelo responsável em 21/10/2026; não foi calculado pela ausência de coluna. Conferir o dado por exercício em extração oficial posterior.

## Ouvidoria

| Cartilha | Serigy | Material disponível | Estado | Providência |
|---|---|---|---|---|
| 13.1 | `enderecoSetor`, `telefoneSetor`, `horarioFuncionamentoSetor` | Endereço, telefone e 7h–13h constam em HTMLs e no Manual de Ouvidoria. | Conteúdo e marcações implementados | Confirmar os dados atuais na revisão final. |
| 13.2 | `faleConosco` | SE-Ouv dispõe de opções específicas de manifestação, distintas do e-SIC. | Parcial | Testar o trajeto da URL genérica até a modalidade de Ouvidoria, sem confundir pedido de informação com manifestação. |
| 13.3 | `servicoUsuario` | O PDF chamado “Carta” contém Manual de Normas e Procedimentos da Ouvidoria; o endereço estadual `https://www.se.gov.br/busca?page=1&orgao=12` lista serviços do SergipePrevidência. Há também Carta de Serviço ao Usuário no site institucional `/servicos/`. | Parcial | Catálogo estadual incluído por instrução do responsável com `servicoUsuario`; conferir posteriormente fichas, requisitos, etapas, prazos e canais e disponibilidade do destino. O PDF permanece como manual complementar, sem `servicoUsuario`. |

**Nomes:** o HTML de Ouvidoria indica Lucas Silva Pedrosa como titular e Sérgio Ricardo Sousa Bezerra como substituto. O responsável informou em 21/10/2026 que Lucas Silva Pedrosa é também responsável pelo SIC e pela Ouvidoria-Geral. O PDF do Manual de novembro/2025 identifica Ângela Maria Lemos de Araújo Campos como titular na época; confirmar o ato de designação vigente na revisão final; os três critérios da dimensão 13 não exigem nominalmente esses nomes.

**Carta estadual localizada para análise, ainda não homologada:** PDF da SEAD de 2021, 469 páginas, contém seção SergipePrevidência, mas não comprova versão institucional vigente de 2026: `https://gestao.se.gov.br/uploads/download/filename_midia/994/d54a0593acff668380bdbdf30f926634.pdf`.

## Ordem recomendada

1. Testar o percurso do SE-Ouv até a modalidade de manifestação da Ouvidoria e até o formulário específico do e-SIC; confirmar a leitura pelo Serigy.
2. Conferir atos de designação e autoridades dos recursos na revisão final. Verificar conteúdo das fichas da Carta de Serviços e disponibilidade do catálogo já marcado `servicoUsuario`.
3. Conferir posteriormente em extração oficial anual **exclusiva de pedidos LAI/e-SIC** os recebidos, atendidos e o zero indeferido informado para 2023–2025; conciliar perfil genérico e CSVs. 2026 permanece parcial.
4. Na data real de alimentação/publicação, registrar `dataUltimaAtualizacao` do relatório estatístico. A organização deste índice em 21/10/2026 não substitui a data efetiva da página.


## Avaliação 4172 — e-SIC e Acessibilidade (22/10/2026)

CSV `dados-entrada/outros/respostas-avaliacao-4172.csv`: redirecionamento 11.2.1.1 aprovado. Os quatro itens de formulário próprio e os cinco de Acessibilidade foram procurados em `https://www.ouvidoria.se.gov.br/index`, não na página local. Não se trata mais do 404 anterior. Não criar formulário fictício nem marcar conteúdo externo. A documentação local SIC pp. 1–3 distingue alternativas 11.2.1/11.2.2 e exemplifica href/serigyLink para Fala.BR; confirmar com TCE/SE a avaliação da alternativa real SE-Ouv.

Verificação pública sem envio: `https://falabr.cgu.gov.br/web/home` depende de JavaScript e a leitura disponível não demonstrou a seleção do SergipePrevidência para pedidos LAI. As pesquisas institucionais não confirmaram essa habilitação. A página oficial `https://sergipeprevidencia.se.gov.br/sic-e-sic/`, consultada nesta rodada, orienta expressamente usar SE-Ouv. Mantidos os dois destinos locais já existentes e a Ouvidoria intacta. Confirmar habilitação e fluxo destinatário no Fala.BR com a instituição antes de qualquer troca; uso pela CGE ou exemplo técnico não comprova atendimento ao Instituto.

Os quatro blocos 11.4 foram preenchidos e marcados conforme a página institucional acima (seções Prazos/Recursos) e o JSON preparado (procedimentos): prazoResposta, recursal, autoridadeExame e procedimentoPedido sob schema SIC. Autoridades identificadas pelas funções publicadas, sem atribuir designação nominal ou confundir Lucas, responsável pelo SIC, com autoridade recursal. Permanece confirmar designações, texto vigente do Decreto 30.947/2017 e alterações das instâncias; a tentativa de abrir o PDF pelo navegador de pesquisa falhou, portanto não se declarou conferência do inteiro teor. Nenhuma data de atualização foi inventada. A antiga linha 11.6 deste controle deve ser lida com esta atualização: os quatro textos agora constam do HTML, com pendências institucionais remanescentes.

As linhas pertinentes da matriz registram os resultados reais 4172 e separam implementação local de reconhecimento futuro. Sem execução do Invoker, commit, push ou alterações no índice de Despesas.

Validação final desta rodada: HTML das duas rotas e dos quatro blocos 11.4 conferido; nenhum campo de formulário próprio fictício. Cópia preparada com o preparador existente para /transparencia.sergipeprevidencia, sem modificar deploy. Chrome fora do ambiente restrito aprovou contraste, escala e foco nas duas páginas, em localhost e Pages simulado (quatro visitas); 170 referências internas HTTP aprovadas, cinco itens de Acessibilidade presentes sob schema próprio e IDs sem duplicidade. As tentativas restritas não retornaram resultado conclusivo do navegador; o resultado aprovado está em trabalho/sic-4172/resultado.json. Validador: 43 páginas aprovadas. Índice Git idêntico ao início; sem Invoker, commit ou push.


## Ajuste pontual solicitado — cadastro Fala.BR

Por instrução expressa, somente o link cadastroESIC em SIC/eSIC foi ajustado: href e serigyLink apontam exatamente para https://falabr.cgu.gov.br, conforme a seção 11.2.1 e seu exemplo local. O texto do link identifica Fala.BR. Os quatro blocos 11.4, as demais orientações existentes e a página de Ouvidoria (SE-Ouv) foram preservados. A confirmação do encaminhamento institucional ao SergipePrevidência no Fala.BR permanece obrigatória antes da publicação definitiva e não foi investigada nesta tarefa. A troca técnica do link não comprova essa habilitação nem altera os resultados do Invoker. As orientações remanescentes sobre o SE-Ouv deverão ser conciliadas com o fluxo confirmado antes da publicação definitiva.


## Relatório Anual Estatístico — ensaio sintético autorizado (S11 11.5.1–11.5.8)

Por solicitação expressa, a página SIC/RelatorioAnualEstatistico recebeu quatro registros inteiramente artificiais, exercícios de teste 2023–2026. Aviso visível: **DADOS SINTÉTICOS PARA TESTE DO SERIGY — NÃO REPRESENTAM PEDIDOS LAI DO SERGIPEPREVIDÊNCIA**. Nenhum número de manifestações da Ouvidoria foi reutilizado como pedido LAI. Não há pessoas reais: perfis “grupo de teste A/B” são categorias artificiais, sem atributos pessoais. Os números de teste (101/202/303/404 recebidos e demais valores próprios do ensaio) não são consolidações institucionais nem comprovação de período completo.

As oito marcações documentadas na seção 11.5 estão presentes no HTML inicial sob schema SIC: pedidosRecebidos, pedidosAtendidos, pedidosIndeferidos, infoGenericas, filtroPesquisa, salvarRelatorio (CSV), dataUltimaAtualizacao e historicoExercicio. Os exercícios efetivos de teste têm serigyValue; a ação no seletor e no botão usa serigyExecuteWaitSection correspondente ao serigyLoadSection do contêiner de resultados. Seleção, pesquisa e limpeza alteram as linhas e o status de resultados; linhas não são removidas do HTML. O CSV contém exatamente o recorte, sem totais adicionais, com a coluna Natureza dos dados repetindo o aviso integral em cada registro e identificação SINTETICOS-TESTE-SERIGY no nome. A data 22/10/2026 é a preparação efetiva deste ensaio nesta rodada, explicitamente distinta da atualização de estatísticas oficiais.

**Bloqueio único:** reutilizado o marcador genérico data-dado-sintetico já reconhecido pelo preparador de Despesas. A regra permanece idêntica: somente a base /transparencia.sergipeprevidencia, com --permitir-dados-sinteticos e sem CNAME, admite o ensaio. A mensagem da recusa passou a orientar também a substituição do SIC. Não houve segundo modo de deploy nem alteração do workflow. Desativar o modo de Despesas não remove os registros sintéticos do SIC: o preparo oficial continua bloqueado enquanto qualquer conjunto marcado permanecer. Antes de publicação definitiva, substituir integralmente estes números e perfis por dados oficiais LAI conferidos (ou repor estrutura sem dados com controles indisponíveis), remover a identificação sintética somente depois dessa substituição e informar atualização/cobertura reais. Não basta retirar aviso ou marcador mantendo números artificiais. A versão anterior está preservada no histórico Git e em trabalho/sic-estatistico-teste/pagina-antes.html; não foi excluído arquivo.

**Pendências oficiais:** consolidar e conciliar pedidos LAI recebidos/atendidos/indeferidos por exercício, comprovar o escopo LAI separado das manifestações, conferir o zero indeferido anteriormente informado, perfil genérico agregado e anonimização, períodos completos e data real de atualização. As pendências anteriores permanecem; o ensaio não as resolve nem demonstra atendimento ao critério.

**Testes:** tools/testar_sic_estatistico.py aprovado com 70 verificações Chrome, oito marcações no HTML inicial, quatro linhas, filtros/ação de pesquisa, histórico, limpeza e CSV (uma linha no recorte e quatro no completo), tanto localhost quanto base Pages simulada. Foram conferidas 86 referências HTTP e quatro bloqueios usando uma origem que contém SOMENTE o SIC sintético — sem depender da presença de Despesas — incluindo raiz, permissão em base errada, ausência de permissão e CNAME. Recusas preservaram a saída anterior. Outras páginas SIC e índice Git preservados. Resultado em trabalho/sic-estatistico-teste/resultado.json. Nenhum Invoker, commit ou push executado; reavaliar somente após publicação autorizada.


## Alinhamento do acesso em Cadastro

/SIC/eSIC/Cadastro/ passou a usar https://falabr.cgu.gov.br em href e serigyLink de cadastroESIC, como a entrada /SIC/eSIC/. Rota local, cabeçalho, acessibilidade e retorno às informações preservados; nenhum formulário próprio ou marcação em site externo. Não alterada a Ouvidoria. A confirmação do encaminhamento institucional e a revisão das orientações ainda vinculadas ao SE-Ouv na página principal continuam pendentes antes da publicação definitiva. O teste de rotas agora espera Fala.BR e prepara apenas a base fixa de teste com a permissão sintética existente, sem afrouxar o bloqueio oficial. Resultados 4172 não mudaram; nova avaliação depende de publicação autorizada.


## Ouvidoria — catálogo de serviços (Serigy 13.5, avaliação 4226)

Incluído, por solicitação expressa, o link “Carta de Serviços ao Usuário — catálogo de serviços do SergipePrevidência” para `https://www.se.gov.br/busca?page=1&orgao=12`, com `servicoUsuario` sob o schema de Ouvidoria. O PDF permanece identificado separadamente como Manual de Normas e Procedimentos, sem essa marcação. A URL foi preservada exatamente (o HTML usa `&amp;`). A ferramenta de navegação não conseguiu abrir o destino nesta rodada; disponibilidade e conteúdo das fichas continuam pendentes de conferência. A inclusão não declara validação integral da Carta nem altera o resultado histórico do Invoker; reconhecimento depende de nova avaliação após publicação autorizada.
