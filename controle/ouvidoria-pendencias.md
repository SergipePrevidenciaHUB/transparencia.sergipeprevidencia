# Ouvidoria — pendências para alimentação e publicação

## Página publicada — organização visual em 23/10/2026

Conferidos novamente apenas C 13.1–13.3 (pp. 103–106) e S 13.1–13.5 (p. 1), além dos controles SIC/Ouvidoria. A página em `dist/Portal-da-Transparencia/Ouvidoria/index.html` já contém dados institucionais; as reservas vazias descritas no levantamento original abaixo dizem respeito ao modelo histórico, não ao estado atual.

Decisão de apresentação: acesso principal **Registrar manifestação** no SE-Ouv; endereço, telefone e horário em três cartões; titular e substituto em bloco próprio; Carta de Serviços e Manual em cartões distintos. CSS exclusivo `dist/assets/css/ouvidoria.css`, com seletores limitados a `.ouvidoria-content`, grade de uma coluna no celular e foco/cores próprios para alto contraste. Telefone existente tornado clicável (`tel:+557931980800`). Nenhum filtro, histórico, formulário ou data de atualização foi acrescentado: não são exigências enumeradas em C/S 13.

Preservados Lucas Silva Pedrosa e Sérgio Ricardo Sousa Bezerra, contatos, schema `https://serigy.tce.se.gov.br/comum/ouvidoria.html` e os cinco campos visíveis no HTML inicial: `enderecoSetor`, `telefoneSetor`, `horarioFuncionamentoSetor`, `faleConosco`, `servicoUsuario`. Preservados os destinos SE-Ouv (`https://www.ouvidoria.se.gov.br/index`), catálogo estadual (`https://www.se.gov.br/busca?page=1&orgao=12`) e Manual (`https://sergipeprevidencia.se.gov.br/wp-content/uploads/2025/11/Carta-de-Servicos-Ouvidoria-atual.-14.11.25.pdf`). O Manual permanece sem `servicoUsuario`; não equivale ao catálogo geral. Orientação para procurar e-SIC no SE-Ouv substituída por link para a página local `/Portal-da-Transparencia/SIC/eSIC/`, sem modificar essa página ou seu fluxo.

Pendências remanescentes: conferir administrativamente as designações e os contatos na revisão institucional; verificar a disponibilidade/conteúdo do catálogo e a atualização das fichas exigidas em C 13.3, além da versão do Manual. Nenhuma pesquisa administrativa foi realizada nesta rodada; preservado o registro anterior em `controle/sic-ouvidoria-verificacao.md`. Alteração visual não resolve essas conferências nem comprova reconhecimento pelo Invoker.

Conferência pontual local: HTML/IDs/rótulos, cinco campos e URLs; renderização Chrome em 1440 e 390 px, grade responsiva, navegação com Tab, foco visível, alternância de contraste com Espaço e links/recursos locais por HTTP. Evidências e verificação de preservação das páginas SIC/demais arquivos e do índice Git em `trabalho/testar_ouvidoria_design.py` e `trabalho/ouvidoria-design-*/`. Não houve alteração no WordPress, Invoker, commit ou push.

## Levantamento original do modelo — histórico

Fontes: Cartilha PETP 2026, C **13.1–13.3**, pp. 103–106; Serigy Docs **13**, itens **13.1–13.5**, p. 1. Mapeamento detalhado em `controle/ouvidoria-modelos.md`. Todos os três critérios C são aplicáveis à Previdência Estadual.

Modelo: `modelos/Portal-da-Transparencia/Ouvidoria/index.html`; rota prevista `/Portal-da-Transparencia/Ouvidoria/`. Não foi publicada nem ligada ao menu. Nenhuma fonte institucional específica de contato, canal ou Carta foi homologada nesta tarefa.

| Critério / bloco | Informação, documento ou dúvida | Providência |
| --- | --- | --- |
| C 13.1 / atendimento presencial | Endereço físico real da Ouvidoria | Confirmar com a área e preencher `#endereco-ouvidoria`; não copiar endereço geral/SIC sem comprovar equivalência. S 13.1 `enderecoSetor` — Texto. |
| C 13.1 / telefone | Telefone real e eventual ramal confirmado | Receber a fonte específica; não deduzir a partir dos contatos gerais do rodapé. S 13.2 `telefoneSetor` — Telefone. |
| C 13.1 / horário | Horário da unidade de Ouvidoria | Confirmar funcionamento real, sem copiar horários de exemplo ou do SIC. S 13.3 `horarioFuncionamentoSetor` — Texto. |
| C 13.2 / canal eletrônico | URL e vínculo ao SergipePrevidência, tipos de manifestação e funcionamento | Conferir acesso para sugestão, elogio, solicitação de providências, reclamação e denúncia. Não inventar URL ou afirmar que o link do e-SIC atende às manifestações. S 13.4 `faleConosco` — Link ou Formulário. |
| C 13.2 / orientação e SE-Ouv | Fluxo institucional efetivo e orientações de uso do canal | Confirmar se e como a Ouvidoria utiliza a plataforma. Não presumir fluxo, identificação, prazo ou acompanhamento iguais ao e-SIC. Não criar formulário próprio ou novas rotas sem necessidade demonstrada. Consulta de protocolo não foi enumerada como controle obrigatório em C/S 13; instruí-la só se houver funcionalidade confirmada. |
| C 13.3 / Carta integral | Carta de Serviços adotada e atualizada, arquivo/HTML e destino público | Receber documento/conteúdo completo e conferir Unidade, versão, integridade e acesso; não gerar Carta ou endereço público por suposição. S 13.5 `servicoUsuario` — Link. |
| C 13.3 / conteúdo mínimo | Serviços; requisitos/documentos/formas/informações; etapas; prazo máximo; forma de prestação; locais/formas de manifestações | Conferir esses conteúdos serviço a serviço na fonte, sem inventar serviços, prazos, documentos ou compromissos. Não confundir com relatório estatístico ou FAQ. |
| C 13.3 / atualização | Confirmação de que a Carta corresponde aos serviços e orientações vigentes | Obter referência institucional da versão. C exige Carta atualizada, mas não fixa prazo numérico e S não documenta `dataUltimaAtualizacao`; não inserir data automática ou marcação inexistente. |
| Limites do recorte | Consulta filtrada, relatórios, histórico, exportação e prazos próprios não enumerados nas fontes | Não importar componentes/regras de SIC ou outras dimensões. Busca geral e acessibilidade do cabeçalho permanecem componentes comuns. |
| Publicação e marcação | Conteúdo real e funcionalidade ainda pendentes | Depois da alimentação, aplicar itens confirmados no schema Ouvidoria; validar contatos, Carta, links e canal, teclado e acessibilidade antes de mover para dist em tarefa autorizada. Não marcar campos vazios, criar declaração de inexistência ou anunciar atendimento aos critérios. |

Os exemplos municipais de S não foram copiados como dados do SergipePrevidência. Contatos gerais do rodapé não comprovam os específicos da Ouvidoria. Nenhum requerimento, manifestação individual, credencial ou cadastro privado deverá integrar os derivados públicos. SIC e demais modelos, dist, menus e deploy foram preservados.
