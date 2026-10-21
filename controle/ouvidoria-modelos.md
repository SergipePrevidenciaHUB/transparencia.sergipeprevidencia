# Ouvidoria — modelo não publicado

## Fontes e aplicabilidade

Lidos `AGENTS.md`, **Cartilha PETP 2026, dimensão 13, pp. 103–106**, e **Serigy Docs, seção 13. Ouvidorias, p. 1**, além do modelo LAI existente apenas como referência visual. **C** = requisito da Cartilha; **S** = marcação técnica; **DT** = organização proposta. Não foram consultados canais externos ou homologados dados institucionais nesta rodada.

Os critérios **13.1, 13.2 e 13.3 da Cartilha incluem expressamente Previdências Municipais e Estadual**; todos são classificados como obrigatórios e listam somente Disponibilidade. Os códigos de itens S não são critérios adicionais C.

**Caminho literal S:** `[Portal da Transparencia]/Ouvidoria`. Rota prevista `/Portal-da-Transparencia/Ouvidoria/`; arquivo `modelos/Portal-da-Transparencia/Ouvidoria/index.html`. Não há coincidência com as rotas SIC/e-SIC e não foi necessária variante. Modelo fora de dist, sem inclusão no menu público ou alteração de deploy.

Reutilizados visual, cabeçalho, rodapé, busca, breadcrumb e acessibilidade dos modelos existentes. O main tem somente o contexto `serigySchema="https://serigy.tce.se.gov.br/comum/ouvidoria.html"`; não há `serigyItem`, `serigyValue`, `serigyLink`, `serigyEmpty` ou atributos de carregamento em campos/ações vazios. Os contatos do rodapé continuam **gerais**, sem serem promovidos a dados da Ouvidoria. Não foram alterados os modelos de SIC ou outras seções.

## Correspondência Cartilha–Serigy

| Critério C / fonte | Item S / tipo literal | Conteúdo e reserva do modelo |
| --- | --- | --- |
| 13.1, pp. 103–104: endereço físico para atendimento presencial | 13.1 `enderecoSetor` — Texto | `#endereco-ouvidoria`, vazio e sem item |
| 13.1: telefone da Ouvidoria | 13.2 `telefoneSetor` — Telefone | `#telefone-ouvidoria`, vazio e sem item |
| 13.1: horário de funcionamento | 13.3 `horarioFuncionamentoSetor` — Texto | `#horario-ouvidoria`, vazio e sem item |
| 13.2, pp. 104–105: canal eletrônico para manifestações | 13.4 `faleConosco` — Link ou Formulário | `#acesso-canal-ouvidoria`, sem URL, link fictício ou formulário próprio |
| 13.3, pp. 105–106: Carta de Serviços ao Usuário atualizada | 13.5 `servicoUsuario` — Link | `#identificacao-carta-servicos` e `#acesso-carta-servicos`, sem documento ou destino presumido |

**Atenção à numeração:** S 13.1–13.3 são três itens técnicos de **C 13.1**; S 13.4 é **C 13.2**; S 13.5 é **C 13.3**. As propriedades de contato também existem em outros schemas, mas aqui devem ficar no contexto Ouvidoria e conter dados realmente confirmados para essa unidade. Não inventar item de setor responsável/e-mail/prazo porque aparece em outra dimensão.

### Atendimento presencial — C 13.1

C exige endereço, telefone e horário da unidade de Ouvidoria para facilitar o acesso físico. **DT:** lista de definições, sem tabela ou cadastro público em planilha. A fonte institucional específica dos três dados deve ser recebida e conferida. Atendimento geral, SIC e Ouvidoria não são automaticamente o mesmo setor, endereço ou horário. Não usar dados municipais dos exemplos S. Telefones, ramais, horários e endereço permanecem vazios; não criar contato por analogia.

### Canal eletrônico — C 13.2

C exige canal para receber **sugestão, elogio, solicitação, reclamação e denúncia**. A solicitação mencionada é de providências diante de problema, não pedido de acesso à informação. O texto genérico de distinção no modelo deriva de C p. 104; não descreve passos de um sistema nem afirma funcionalidades já testadas.

S admite `faleConosco` como Link ou Formulário. **DT desta etapa:** reservar acesso ao sistema institucional existente, quando seu destino e fluxo forem confirmados; não criar formulário próprio sem necessidade comprovada, operação ou fonte. `#orientacao-canal-ouvidoria` receberá apenas orientação validada. Não foram criados campos de nome, documento, contato ou texto de manifestação, nem atribuída URL de exemplo à Unidade.

**SE-Ouv e e-SIC:** o uso eventual da mesma plataforma não torna os fluxos equivalentes. Confirmar o acesso de Ouvidoria, encaminhamento à Unidade, tipos de manifestação e interação reais. Não copiar URL de formulário, autenticação, procedimento, protocolo, prazo ou acompanhamento do e-SIC como se fossem de Ouvidoria. C 13.2 não enumera uma URL separada de consulta de protocolo, painel estatístico ou formulário próprio; se houver acompanhamento, orientar somente conforme o sistema confirmado, sem inventar requisito ou rota. A confirmação do canal e de suas funções é pendência, não afirmação de atendimento.

### Carta de Serviços — C 13.3

C exige divulgação e manutenção de Carta atualizada, com serviços prestados, acesso, compromissos e padrões de qualidade de atendimento. Conteúdo mínimo a conferir na fonte, sem gerar serviços ou prazos:

- Serviços oferecidos.
- Requisitos, documentos, formas e informações necessárias ao acesso.
- Principais etapas de processamento.
- Previsão do prazo máximo para prestação.
- Forma de prestação.
- Locais e formas de manifestação sobre a prestação do serviço.

**DT:** acesso identificado à Carta integral, cujo conteúdo pode estar em HTML ou documento conferido; não criar catálogo com serviços inventados nem exigir transcrição de documento para tabela. S documenta `servicoUsuario` como Link, sem propriedades para cada campo da Carta. Identificar a versão real e a forma de acesso antes de aplicar a marcação no conteúdo existente. Não presumir URL definitiva ou copiar `local/arquivo` do exemplo S.

## Consulta, relatórios, formatos e atualização

| Tema | O que as fontes desta dimensão efetivamente determinam | Decisão no modelo |
| --- | --- | --- |
| Consulta/pesquisa | C 13.1–13.3 não listam filtro de pesquisa; S 13 não tem `filtroPesquisa` | Sem consulta tabular, seletores ou filtros específicos. A busca comum do cabeçalho é componente geral preservado, não comprovação deste item. |
| Relatórios | C/S 13 consultados não exigem relatório estatístico ou anual de Ouvidoria | Nenhum bloco de relatório, número, documento ou gráfico foi fabricado. O relatório estatístico SIC é outro conjunto; não foi reaproveitado. |
| Histórico/exportação | C não lista série histórica nem gravação e S não documenta `historicoExercicio`/`salvarRelatorio` | Sem seletor histórico ou exportação autônoma. O acesso à Carta integral não se confunde com botão de exportar conjunto. |
| Atualização | C 13.3 exige Carta atualizada como conteúdo; não fixa periodicidade numérica. S 13 não tem `dataUltimaAtualizacao` | Sem campo de data fictícia, reserva marcada ou prazo automático. Confirmar versão vigente e atualização da Carta e revisar contatos com a fonte real. Se futuramente houver indicação de versão/data como metadado editorial DT, usar apenas referência comprovada, sem atribuir item S inexistente. |
| Formatos/documentos | C exige a Carta; não enumera aqui formato editável, PDF pesquisável ou relatório adicional | Receber conteúdo integral e acesso real, sem impor novas extensões ou documentos e sem publicar fontes privadas. |

O nome “atualizada” não autoriza preencher a data do dia ou marcar uma reserva vazia. Ausência de dados não comprova inexistência de atendimento, canal ou Carta, nem justifica declaração fictícia.

## Alimentação e publicação

Pendências em `controle/ouvidoria-pendencias.md`. Receber e confirmar dados presenciais, URL/fluxo de manifestações e Carta integral atualizada; verificar acesso público, correspondência e conteúdo; alimentar somente dados reais e aplicar os cinco itens S pertinentes. URLs devem ser conferidas individualmente, sem construção por suposição e sem `serigyLink` para PDF. Testar navegação, funcionamento do canal e acessibilidade antes de mover para dist em tarefa autorizada. O modelo não recebe manifestações, não comprova atendimento e não foi adicionado ao menu público.
