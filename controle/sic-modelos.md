# SIC — modelos não publicados

## Fontes, numeração e escopo

Lidos AGENTS.md; Cartilha PETP 2026, abertura da dimensão e critério 11.1 (p. 88), 11.2 (p. 89), 11.3 (pp. 90–92) e 11.4 (p. 93, somente a solicitação simples); Serigy Docs 11, seções 11.1 e 11.2.1–11.2.2 (p. 1 e exemplos correspondentes da p. 2). **C** = requisito da Cartilha; **S** = marcação técnica; **DT** = decisão de organização. Todos esses critérios incluem a Previdência Estadual e exigem Disponibilidade.

**Distinção da numeração:** a Cartilha tem critérios autônomos 11.1 (setor), 11.2 (contatos), 11.3 (pedido eletrônico) e 11.4 (simplicidade). As subdivisões 11.2.1/11.2.2 são seções técnicas do Serigy, não subdivisões normativas de C 11.2. Não se trata aqui de LAI local, prazos/autoridades/recursos de C 11.6 ou estatísticas; não copiar esses conteúdos dos exemplos.

| Modelo fora de dist | Rota literal S | Correspondência |
| --- | --- | --- |
| `modelos/Portal-da-Transparencia/SIC/Detalhe/index.html` | `/Portal-da-Transparencia/SIC/Detalhe/` | S 11.1 ↔ C 11.1 e 11.2 |
| `modelos/Portal-da-Transparencia/SIC/eSIC/index.html` | `/Portal-da-Transparencia/SIC/eSIC/` | S 11.2.1 ↔ C 11.3 e 11.4, alternativa de redirecionamento |

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
