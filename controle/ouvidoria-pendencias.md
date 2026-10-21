# Ouvidoria — pendências para alimentação e publicação

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
