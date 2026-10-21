# SIC — modelos não publicados

## Fontes, numeração e escopo

Lidos AGENTS.md; Cartilha PETP 2026, abertura da dimensão e critério 11.1 (p. 88), 11.2 (p. 89), 11.3 (pp. 90–92) e 11.4 (p. 93, somente a solicitação simples); Serigy Docs 11, seções 11.1 e 11.2.1–11.2.2 (p. 1 e exemplos correspondentes da p. 2). **C** = requisito da Cartilha; **S** = marcação técnica; **DT** = decisão de organização. Todos esses critérios incluem a Previdência Estadual e exigem Disponibilidade.

**Distinção da numeração:** a Cartilha tem critérios autônomos 11.1 (setor), 11.2 (contatos), 11.3 (pedido eletrônico) e 11.4 (simplicidade). As subdivisões 11.2.1/11.2.2 são seções técnicas do Serigy, não subdivisões normativas de C 11.2. Não se trata aqui de LAI local, prazos/autoridades/recursos de C 11.6 ou estatísticas; não copiar esses conteúdos dos exemplos.

| Modelo fora de dist | Rota literal S | Correspondência |
| --- | --- | --- |
| `modelos/Portal-da-Transparencia/SIC/Detalhe/index.html` | `/Portal-da-Transparencia/SIC/Detalhe/` | S 11.1 ↔ C 11.1 e 11.2 |
| `modelos/Portal-da-Transparencia/SIC/eSIC/index.html` | `/Portal-da-Transparencia/SIC/eSIC/` | S 11.2.1 ↔ C 11.3 e 11.4, alternativa de redirecionamento; S 11.4 ↔ C 11.6, informações complementares já integradas |

Reutilizados visual, cabeçalho, rodapé, busca e acessibilidade do modelo existente. Apenas o contexto `serigySchema="https://serigy.tce.se.gov.br/comum/sic.html"` foi aplicado ao main. Não há itens sobre campos vazios. Links entre os dois modelos são navegação interna DT; não foram acrescentados ao menu público. Não há filtros de conjuntos, histórico, exportação ou data de atualização autônomos exigidos por C/S neste recorte.

## Conteúdo local conferido e reaproveitamento

Não há HTML específico de SIC/e-SIC em `referencias/conteudo-institucional`. Foi conferido `endereco-horario.html`: endereço geral Praça General Valadão, 32, Centro, Aracaju/SE, CEP 49010-520; atendimento geral segunda a sexta, 7h–13h; atendimento@sergipeprevidencia.se.gov.br; telefones gerais (79) 3198-0801 e (79) 3198-0800. São dados institucionais presentes no rodapé reutilizado, **não confirmação de atendimento SIC**. Não foram transferidos para os campos específicos do SIC. Confirmar equivalência com a área antes de reaproveitá-los ali.

O mesmo arquivo contém `https://ouvidoria.se.gov.br`, identificado apenas como acesso à Ouvidoria. É um candidato existente para conferência, **não URL comprovada do formulário de acesso à informação nem de acompanhamento**; por isso não foi promovido a link e-SIC no main. A busca textual local também encontrou referência à Ouvidoria em `competencias.html`, sem comprovar designação de SIC. Não foram usados contatos de gestores ou ementas de portarias para deduzir responsáveis.

**Fonte do nome SE-Ouv:** informação expressa do solicitante nesta tarefa. Reaproveitada apenas como identificação do canal eletrônico no modelo; não confirma URL, fluxo, unidade selecionada, procedimento, autenticação ou funcionamento. As orientações gerais sobre finalidade do SIC e distinção da Ouvidoria vêm de C p. 88. Nenhum exemplo municipal ou Fala.BR foi copiado como dado da Unidade. Não houve teste externo ou consulta à internet.

## SIC presencial — reservas de conteúdo

Apresentação editorial em lista de definições (DT), sem tabela ou planilha obrigatória. Os elementos dd estão vazios e sem serigyItem; preencher após confirmação institucional.

| Reserva | C | S futuro / tipo |
| --- | --- | --- |
| `#setor-sic` | 11.1: unidade/setor responsável | 11.1.1 `setorResponsavel` — Texto |
| `#endereco-sic` | 11.2: endereço do SIC | 11.1.2 `enderecoSetor` — Endereço |
| `#telefone-sic` | 11.2: telefone do SIC | 11.1.3 `telefoneSetor` — Numérico |
| `#email-sic` | 11.2: e-mail do responsável | 11.1.4 `emailSetor` — E-mail |
| `#horario-sic` | 11.2: horário da unidade responsável | 11.1.5 `horarioFuncionamentoSetor` — Hora |

`#orientacao-presencial-sic` reserva instruções locais realmente confirmadas. Não inventar formulários impressos, documentos exigidos, agendamento ou identificação do responsável. Tipo técnico de telefone não justifica remover DDD ou inventar ramal; apresentar o contato real. Setor SIC não se presume igual à Ouvidoria ou ao atendimento geral.

## e-SIC — sistema existente versus formulário próprio

**Escolha DT nesta rodada:** preparar acesso ao SE-Ouv existente, sem criar cadastro ou envio próprio. `#acesso-se-ouv` reserva o link conferido de pedidos e `#acesso-acompanhamento` o acesso real ao acompanhamento, que pode integrar o mesmo sistema. Se um único destino atender às duas funções, não exigir duas URLs distintas. `#orientacao-pedido-eletronico` e `#orientacao-acompanhamento` receberão instruções comprovadas; não inventar protocolo, senha, passos ou prazos.

**C 11.3:** canal eletrônico com formulário específico de pedido, contendo identificação do solicitante, contato e conteúdo. Se o sistema estiver na Ouvidoria, deve permitir selecionar especificamente “Pedido de Acesso à Informação”. C p. 88 também exige possibilidade de acompanhar posteriormente. Isso deve ser validado **no sistema de destino**; um link genérico ou o nome SE-Ouv não comprova essas funções. Cadastro operacional é distinto da publicação aberta do Portal.

**C 11.3/11.4:** não exigir envio de documentos, assinatura reconhecida, declaração de responsabilidade, maioridade ou motivação do pedido. C p. 93 esclarece que cadastro prévio por si só não configura dificuldade. Não presumir que o SE-Ouv já satisfaz esses controles: validar o fluxo.

**S 11.2.1.1:** `cadastroESIC` (Link), com exemplo de `serigyLink` e href para Fala.BR. A nota cita redirecionamento gov.br. **DÚVIDA — REVISÃO NECESSÁRIA:** a documentação consultada não explicita a representação de outro sistema, como SE-Ouv. Não aplicar automaticamente `serigyLink`/`cadastroESIC`, nem trocar o canal institucional por Fala.BR. Confirmar a marcação para o destino real antes da ativação. Não existe item específico de acompanhamento nas seções consultadas; não inventá-lo.

**Alternativa S 11.2.2**, somente se comprovadamente necessária e autorizada em tarefa futura: rota `/Portal-da-Transparencia/SIC/eSIC/Cadastro`, formulário `cadastroESIC` e campos `nomeCadastro`, `emailCadastro`, `conteudoPedido` (11.2.2.1–11.2.2.4). **Não foi criado esse modelo ou formulário.** Um formulário apenas visual não recebe nem acompanha pedidos e não equivale a serviço; eventual solução própria precisaria de operação, tratamento autorizado dos dados e validação de simplicidade, sem publicar requerimentos/cadastros pessoais.

## Condições para publicação

Resolver as pendências de `controle/sic-pendencias.md`; confirmar contatos/setor e acesso específico ao SE-Ouv, testar solicitação e acompanhamento, validar orientação e marcações. Preencher somente os dados reais e conferir leitura por teclado, rótulos e links. Não publicar o modelo presencial sem contatos ou o eletrônico sem acesso funcional. Mover para dist e ajustar navegação somente em tarefa autorizada. Nenhuma declaração de atendimento, inexistência, data ou URL de canal foi inventada.


## Complemento — Regulamentação local da LAI e Informações e-SIC

**Fontes efetivamente consultadas:** AGENTS.md; C 11.5 (pp. 93–94, continuação) e 11.6 (pp. 94–95, somente sua continuação); S 11.3 e 11.4 (p. 1, exemplos das pp. 2–3); estes dois controles; modelo existente de acesso ao e-SIC como referência visual. Foi conferida somente a identificação da primeira página de `referencias/legislacao/DECRETO ESTADUAL LAI.pdf`, sem extrair dele prazos ou procedimentos para os modelos. **C** determina conteúdo; **S**, itens técnicos; **DT**, organização do modelo.

### Correspondência exata e rotas

| Critério Cartilha | Seção / item Serigy | Conteúdo / tipo | Rota documentada |
| --- | --- | --- | --- |
| 11.5 — instrumento normativo local que regulamenta a LAI | 11.3 / 11.3.1 `lai` | Texto ou Link | `/Portal-da-Transparencia/SIC/LAI/` |
| 11.6 — prazos de resposta | 11.4 / 11.4.1 `prazoResposta` | Texto | `/Portal-da-Transparencia/SIC/eSIC/` |
| 11.6 — prazo recursal | 11.4 / 11.4.2 `recursal` | Texto | Mesma rota e-SIC |
| 11.6 — autoridades competentes para exame dos pedidos | 11.4 / 11.4.3 `autoridadeExame` | Texto | Mesma rota e-SIC |
| 11.6 — procedimento de pedido e eventual recurso | 11.4 / 11.4.4 `procedimentoPedido` | Texto | Mesma rota e-SIC |

Os códigos 11.3/11.4 de S **não** correspondem aos critérios 11.3/11.4 de C: os critérios desta etapa são **C 11.5 e 11.6**, ambos aplicáveis à Previdência Estadual e com somente Disponibilidade. Não estão enumerados filtros, histórico, exportação ou data de atualização autônomos; não foram criados. O contexto de ambos os modelos é `https://serigy.tce.se.gov.br/comum/sic.html`; os itens da tabela só serão aplicados quando existir conteúdo confirmado, nunca aos contêineres vazios.

### Arquivos e coincidência da rota e-SIC

- LAI: `modelos/Portal-da-Transparencia/SIC/LAI/index.html`.
- Informações e-SIC: blocos já integrados a `modelos/Portal-da-Transparencia/SIC/eSIC/index.html`; a variante `modelos/variantes/sic-informacoes/Portal-da-Transparencia/SIC/eSIC/index.html` permanece intacta como referência.

**DT de integração:** S 11.4 utiliza a mesma rota `/SIC/eSIC` de S 11.2.1. Os quatro blocos informativos da variante foram incorporados ao main do modelo principal, após acompanhamento e antes do link para SIC presencial. A árvore `variantes/sic-informacoes` é referência não publicada, não outra rota pública. Não foi criada `/SIC/Informacoes` ou rota de cadastro próprio; o arquivo original da variante foi preservado.

A estrutura de acesso/seguimento do SE-Ouv e informações de C 11.6 já está reunida na **mesma página e-SIC não publicada**, sem substituir ou apagar os blocos anteriores. Foram copiadas somente as quatro seções complementares, sem duplicar main, h1, cabeçalho, rodapé ou busca. Não copiar a variante completa sobre a página principal nem reinserir os blocos duplicando IDs. A publicação continua dependente de alimentação real, confirmação do destino/fluxo e marcações. Nenhuma mudança em dist, menus ou deploy foi feita.

### LAI — apresentação e documento identificado

**C 11.5:** disponibilizar instrumento normativo local legal/infralegal que regulamenta a Lei nº 12.527/2011, em texto ou link visível, identificado e associado à Transparência/LAI. Não basta usar a lei federal como substituto da regulamentação local. **DT:** seção editorial com reservas `#identificacao-norma-lai` e `#conteudo-norma-lai`, para identificação e acesso ao inteiro teor ou texto integral; não criar tabela de artigos.

**Documento local encontrado:** `referencias/legislacao/DECRETO ESTADUAL LAI.pdf` (16 páginas). A primeira página identifica **Decreto nº 30.947, de 28 de dezembro de 2017**, do Governo de Sergipe, cuja ementa regulamenta o acesso a documentos e informações públicas nos termos da Lei Federal nº 12.527/2011, no âmbito do Poder Executivo Estadual. Essa conferência serve somente para identificar o documento disponível. Não houve homologação de vigência, auditoria integral, conferência de alterações posteriores ou definição do arquivo público definitivo.

O PDF não foi copiado, vinculado por caminho de referencias ou publicado. **URL pública definitiva pendente:** não construir `/legislacao/decreto-lai.pdf` a partir do exemplo S nem presumir endereço no futuro Portal. Confirmar vigência/completude e destino oficial antes de inserir acesso real. `lai` (Texto | Link) será aplicado ao conteúdo/acesso correspondente, sem `serigyLink` para PDF e sem marcar apenas uma identificação como se o inteiro teor estivesse disponível. Nenhum link fictício ou conteúdo normativo parcial foi preenchido no modelo.

### Informações e-SIC — apresentação sem procedimentos presumidos

C 11.6 exige em destaque, na seção e-SIC, prazos de resposta e recursal, autoridades competentes para examinar pedidos e procedimento de realização do pedido e eventual recurso. A organização em quatro seções é DT, sem criar novas exigências ou instâncias recursais.

| Reserva HTML | Alimentação necessária | S futuro |
| --- | --- | --- |
| `#prazo-resposta-esic` | Prazo de resposta confirmado na norma/fluxo aplicável | `prazoResposta` |
| `#prazo-recursal-esic` | Prazo recursal confirmado | `recursal` |
| `#autoridades-esic` | Autoridades efetivamente competentes, identificadas conforme fonte institucional | `autoridadeExame` |
| `#procedimentos-esic`, subdividido em `#procedimento-pedido-esic` e `#procedimento-recurso-esic` | Instruções validadas de pedido e eventual recurso no fluxo adotado | `procedimentoPedido` no conjunto real; sem inventar `procedimentoRecurso` |

Os contêineres de C 11.6 já estão no modelo principal, vazios e sem marcação de dados. Não foram copiados prazos/autoridades municipais dos exemplos S nem deduzidos prazos ou recursos do PDF do decreto, cuja leitura anterior foi apenas identificadora. Não há formulário próprio, contato novo, URL, data ou declaração de funcionamento. O acesso previsto ao SE-Ouv e seus conteúdos originais foram preservados; destino, instruções e marcação de redirecionamento continuam pendentes conforme o controle.

### Alimentação e publicação deste complemento

Receber norma vigente e conteúdo institucional validado; conferir vigência, inteiro teor, acesso público e orientações/autoridades reais; preencher somente os blocos respaldados e aplicar os itens S. Para e-SIC, a integração estrutural na rota única já está concluída; falta alimentar os blocos e testar pedido, recurso e acompanhamento sem publicar dados de solicitantes. Validar HTML, teclado e destinos antes de mover conteúdo para dist. A reunião das reservas vazias não comprova atendimento aos critérios.


## Complemento — Relatório Anual Estatístico de acesso à informação

**Fontes efetivamente consultadas:** AGENTS.md; Cartilha PETP 2026, **critério 11.7, pp. 95–97**; Serigy Docs 11, **seção 11.5**, tabela da p. 1 e exemplos de pesquisa/exportação/dados/atualização das pp. 2–3; estes dois controles e o modelo LAI como referência visual. **C** = exigência da Cartilha; **S** = marcação técnica; **DT** = organização proposta. A classificação C é obrigatória e o quadro inclui expressamente a Previdência Estadual.

**Códigos exatos:** C **11.7** corresponde a S **11.5**, itens **11.5.1–11.5.8**. Não confundir S 11.5 com o critério C 11.5, que trata da regulamentação local da LAI.

**Rota literal S:** `/Portal-da-Transparencia/SIC/RelatorioAnualEstatistico/`. Modelo: `modelos/Portal-da-Transparencia/SIC/RelatorioAnualEstatistico/index.html`. A rota é própria, distinta de `/SIC/eSIC`, `/SIC/Detalhe` e `/SIC/LAI`; **não requer variante nem reunião de blocos** com páginas anteriores. Nenhum modelo existente foi alterado. O arquivo fica fora de dist e não recebeu link no menu público. Reutiliza visual, cabeçalho, rodapé, acessibilidade e contexto `serigySchema="https://serigy.tce.se.gov.br/comum/sic.html"`.

### Conteúdo e apresentação

C exige relatório anual com quantidades de pedidos recebidos, atendidos e indeferidos e informações genéricas dos solicitantes. Gráficos são admitidos se todos os dados forem claros e acessíveis. **DT:** tabela de resumo por exercício, com acesso ao relatório integral em HTML ou arquivo real; o perfil agregado fica associado ao respectivo exercício em `#perfil-solicitantes-sic`. O índice ou um resumo incompleto não substitui o conteúdo anual mínimo. Não impor PDF separado quando a apresentação HTML integral atender ao conteúdo; a coluna de acesso documental é uma organização proposta, sem item S específico para um link de relatório.

| Conteúdo / reserva | Origem | Item S / tipo futuro |
| --- | --- | --- |
| Exercício em `#tabela-relatorio-sic` | DT para organizar o relatório anual exigido C | Sem item de dado específico; não inventar `anoRelatorio` |
| Pedidos recebidos | C 11.7 | 11.5.1 `pedidosRecebidos` — Numérico |
| Pedidos atendidos | C 11.7 | 11.5.2 `pedidosAtendidos` — Numérico |
| Pedidos indeferidos | C 11.7 | 11.5.3 `pedidosIndeferidos` — Numérico |
| Informações genéricas e perfil agregado por exercício | C 11.7 | 11.5.4 `infoGenericas` — N/A |
| Relatório integral em HTML/arquivo | C: conteúdo completo; índice/acesso na tabela é DT | Sem propriedade própria de documento nessa tabela S; não inventar `relatorioAnual` |

Categoria do solicitante, idade e sexo são **exemplos C**, não colunas obrigatórias cumulativas. Receber apenas categorias e agregações efetivamente existentes na fonte, protegendo sigilo e dados pessoais. Não publicar requerimentos, contatos ou cadastros individuais. Não impor percentuais, denominadores ou igualdade `recebidos = atendidos + indeferidos`: confirmar conceitos, saldos e critérios de contagem da origem. Totais zero dependem de fonte; campos vazios não significam zero.

O tbody e o perfil estão vazios, sem dados ou itens Serigy. Na alimentação, manter a associação entre totais, informações genéricas, documento e exercício. Se o perfil for detalhado por interação, só aplicar `serigyExecuteWaitSection`/`serigyLoadSection` com valores coincidentes após implementar o carregamento real; não copiar o sinal “+”, anos ou percentuais ilustrativos como conteúdo institucional. O exemplo S de ausência menciona informações desclassificadas: não transportá-lo como declaração de inexistência de pedidos.

### Consulta, histórico, gravação e atualização

| Requisito C | Reserva / decisão DT | S futuro |
| --- | --- | --- |
| Filtro específico genérico, sem parâmetros mínimos enumerados (p. 97) | Formulário `#filtro-relatorio-sic` e seletor por exercício `#exercicio-relatorio-sic`; este parâmetro é DT, não mínimo nominal C | 11.5.5 `filtroPesquisa` — N/A |
| Pelo menos os três anos anteriores ao ano da consulta (p. 96) | Exercícios reais, documentos e dados anuais correspondentes | 11.5.8 `historicoExercicio` — N/A; opções reais com `serigyValue` |
| Gravação das informações em pelo menos um formato editável (p. 97) | `#exportacao-relatorio-sic`, conjunto selecionado com totais e informações genéricas; formato a definir conforme fonte real | 11.5.6 `salvarRelatorio` — N/A, `serigyValue` do formato efetivamente disponível |
| Atualidade: dados mais recentes relativos ao último exercício encerrado (p. 96) | `#atualizacao-relatorio-sic`, reservado para referência real e cobertura | 11.5.7 `dataUltimaAtualizacao` — Data |

Não exigir todas as extensões exemplificadas em C/S. PDF no exemplo S não substitui a gravação editável C; arquivo de origem privado não é automaticamente o derivado público. Conferir que a exportação representa o recorte e o conteúdo anual, sem incluir linhas de subtotal como registros duplicados nem dados pessoais de base.

Formulário, seletores e botões estão desativados, sem anos fabricados, URLs, formato presumido ou marcações funcionais. A associação futura `#pesquisar-relatorio-sic` → `#resultados-relatorio-sic` poderá usar os atributos de espera/carregamento somente após implementação. Não há gravação funcional neste modelo sem dados.

**Cobertura e atualização são verificações independentes:** um relatório isolado não comprova os três anos anteriores nem que o último exercício encerrado esteja disponível. Conferir cada período, conceitos, conteúdo mínimo e fonte do relatório mais recente. A data da geração, do upload ou uma data recente no rodapé não torna o conjunto atualizado; não preencher automaticamente com a data atual. Não aplicar a série especial X/X-1/X-2/X-3 de Planejamento a este critério.

### Alimentação e publicação

Receber relatórios/totalizações anuais oficiais e informações genéricas agregadas, identificar os exercícios efetivamente cobertos, obter URL oficial ou conteúdo integral, derivado editável e data real de atualização. Conferir acesso e correspondência dos arquivos individualmente, sem construir URLs por exercício e sem `serigyLink` para PDF. Validar publicação dos agregados, implementar consulta/exportação, preencher apenas dados reais e aplicar os itens S correspondentes. Testar seleção, histórico, documento, exportação e acessibilidade antes de mover para dist em tarefa autorizada. Nenhum número, declaração de inexistência, link documental ou data foi criado.


## Estado da integração estrutural do e-SIC

Rota única mantida: `/Portal-da-Transparencia/SIC/eSIC/`. Modelo principal: `modelos/Portal-da-Transparencia/SIC/eSIC/index.html`. A estrutura reúne S 11.2.1 (C 11.3–11.4: redirecionamento) e S 11.4 (C 11.6: informações), com as quatro seções importadas da variante **sem dados ou marcações sobre campos vazios**.

Ordem no main: solicitação → acompanhamento → prazo de resposta → prazo recursal → autoridades → procedimentos de pedido e recurso → link para atendimento presencial. Os blocos originais, títulos, texto SE-Ouv, marcações, cabeçalho, rodapé e navegação foram preservados. A variante original permanece intacta, apenas como referência. Não foi importado o h1 ou o lead da variante nem criado formulário próprio, endereço, contato, prazo ou data.

Reservas complementares: `#prazo-resposta-esic` (S 11.4.1 prazoResposta), `#prazo-recursal-esic` (S 11.4.2 recursal), `#autoridades-esic` (S 11.4.3 autoridadeExame) e `#procedimentos-esic` (S 11.4.4 procedimentoPedido, incluindo pedido e recurso). Esses itens só serão aplicados após receber as informações oficiais. Permanecem as dúvidas de representação do redirecionamento para SE-Ouv: a integração de layout não homologa `cadastroESIC`/`serigyLink` por analogia com o exemplo Fala.BR.

A escolha continua sendo acesso ao sistema institucional existente. A alternativa S 11.2.2 de formulário próprio não foi implementada e não se confunde com a busca comum do cabeçalho. Para publicação faltam URL e fluxo confirmados, acesso específico a pedidos de informação e acompanhamento, simplicidade, prazos, autoridades e procedimentos validados, aplicação das marcações reais e testes de funcionamento/acessibilidade. LAI, Relatório Anual, dist e demais seções não foram alterados.
