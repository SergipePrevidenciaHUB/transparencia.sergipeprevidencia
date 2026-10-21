# SIC — pendências para alimentação e publicação

Escopo: C 11.1–11.4 ↔ S 11.1 e 11.2.1/11.2.2. Modelos em `SIC/Detalhe` e `SIC/eSIC`, fora de dist. Requisitos e fontes detalhados em `controle/sic-modelos.md`.

| Seção / requisito | Informação faltante ou dúvida | Providência |
| --- | --- | --- |
| Presencial / C 11.1 | Unidade/setor efetivamente responsável pelo SIC | Confirmar identificação institucional; não deduzir que Ouvidoria ou atendimento geral sejam o SIC. |
| Presencial / C 11.2 | Endereço, telefone, e-mail do responsável e horário específicos do SIC | Validar se os dados gerais de `referencias/conteudo-institucional/endereco-horario.html` também se aplicam; até lá, manter campos específicos vazios e sem marcação. |
| Presencial / orientação | Forma real de atendimento e instruções necessárias ao cidadão | Receber conteúdo validado; não inventar agendamento, formulários, documentos, etapas ou prazos. |
| Eletrônico / destino | URL específica de solicitação SE-Ouv e vinculação ao SergipePrevidência | Nome do canal fornecido pelo solicitante. O HTML local contém apenas `https://ouvidoria.se.gov.br`, rotulado Ouvidoria; conferir se conduz ao formulário correto e à opção Pedido de Acesso à Informação. Não construir URL ou publicar acesso genérico como e-SIC validado. |
| Eletrônico / C 11.3 | Formulário de pedido específico com identificação, contato e conteúdo | Validar no sistema existente; selecionar acesso à informação deve ser possível mesmo se a plataforma reúne Ouvidoria. Não criar formulário próprio por falta de URL. |
| Eletrônico / acompanhamento | Destino e instruções reais para consulta posterior do pedido | Conferir a funcionalidade e os passos; não presumir protocolo, senha ou URL distinta de solicitação. |
| Eletrônico / C 11.3–11.4 | Simplicidade e ausência de exigências impeditivas ou motivação obrigatória | Avaliar fluxo real sem supor conformidade pelo nome do sistema. Cadastro prévio, por si, não é impedimento segundo C. Não enviar pedidos de teste reais sem autorização. |
| Eletrônico / S 11.2.1.1 | Marcação `cadastroESIC`/`serigyLink` para SE-Ouv | **DÚVIDA — REVISÃO NECESSÁRIA:** S exemplifica Fala.BR/gov.br, sem detalhar SE-Ouv. Confirmar representação técnica; não inserir atributo por analogia. |
| Alternativa própria / S 11.2.2 | Necessidade de cadastro/formulário próprio não comprovada | Não criar `/SIC/eSIC/Cadastro`, coleta ou backend nesta rodada. Se houver necessidade futura, tratar em tarefa específica, com operação e proteção dos dados. |
| Publicação | Conteúdo institucional, URLs, orientações e marcações confirmados | Conferir acesso, solicitação/acompanhamento, teclado e rotas antes de mover os modelos para dist. Não publicar fontes privadas ou dados de requerentes; não adicionar modelos vazios ao menu. |

Não foram encontrados HTMLs locais específicos de SIC/e-SIC; nenhum contato geral foi homologado como SIC. Os dados gerais do rodapé e os componentes visuais existentes foram preservados. Não há exigência autônoma de histórico, exportação, filtro de dados ou data de atualização nestas seções C/S. Prazos, recursos, norma LAI e estatísticas ficam fora deste recorte; não importar os exemplos Serigy como orientação institucional. Sem confirmação de atendimento aos critérios e sem comunicação externa.


## Complemento — C 11.5 / S 11.3 e C 11.6 / S 11.4

Fontes: Cartilha pp. 93–95 nos trechos 11.5/11.6; Serigy seções 11.3/11.4 e exemplos correspondentes; primeira página do PDF local do decreto para identificação. Mapeamento exato em `controle/sic-modelos.md`. Os modelos anteriores não foram alterados.

| Seção / requisito | Fonte disponível ou lacuna | Providência antes de publicar |
| --- | --- | --- |
| LAI / instrumento local | `referencias/legislacao/DECRETO ESTADUAL LAI.pdf`: primeira página confirma Decreto nº 30.947, de 28/12/2017, regulamentação no Executivo Estadual | Usar somente como identificação do documento. Conferir versão integral, vigência e alterações com a área; não presumir homologação pelo arquivo local. |
| LAI / acesso integral e identificação | Documento encontrado, mas URL pública definitiva não definida | Confirmar destino oficial e acesso sem login ou texto integral validado; não construir URL ou copiar caminho ilustrativo S. Não publicar link para referencias ou copiar PDF nesta tarefa. |
| LAI / S 11.3.1 | `lai` — Texto ou Link, vinculado a C 11.5 | Marcar somente conteúdo/acesso real da norma. Não aplicar serigyLink a PDF nem marcar identificação isolada como inteiro teor disponível. |
| Informações e-SIC / resposta | Prazo aplicável não conferido para preenchimento | Obter fonte normativa e orientação institucional validada; não copiar exemplo S ou prazo conhecido por analogia. Item futuro `prazoResposta` (11.4.1 ↔ C 11.6). |
| Informações e-SIC / recurso | Prazo recursal e instruções efetivas não conferidos | Confirmar fluxo adotado e prazo; não criar instâncias ou prazos. Item futuro `recursal` (11.4.2 ↔ C 11.6). |
| Informações e-SIC / autoridades | Identificação das autoridades competentes para exame dos pedidos não recebida | Confirmar com fonte institucional, sem deduzir pelo cargo de Ouvidoria/SIC nem copiar autoridade municipal S. Item futuro `autoridadeExame` (11.4.3 ↔ C 11.6). |
| Informações e-SIC / procedimentos | Passos de pedido e eventual recurso no SE-Ouv não validados | Receber conteúdo e testar o fluxo autorizado; não inventar contatos, URLs ou instruções. Item futuro `procedimentoPedido` (11.4.4 ↔ C 11.6), incluindo pedido e recurso. |
| Rota compartilhada / montagem | S 11.4 e S 11.2.1 usam `/SIC/eSIC`; o modelo de acesso existente deve ser preservado | A variante em `modelos/variantes/sic-informacoes/Portal-da-Transparencia/SIC/eSIC/index.html` é apenas área de preparação, não outra rota pública. Integrar blocos à mesma página em tarefa futura, sem sobrescrever o acesso pelo modelo informativo isolado. |
| Validação e publicação | Norma e orientações ainda sem alimentação homologada | Resolver pendências, alimentar conteúdo real, aplicar itens confirmados e validar documentos, navegação, teclado e fluxo. Não acrescentar filtros, histórico, exportação ou data autônomos que C 11.5/11.6 e S 11.3/11.4 não exigem. |

Continuam válidas as pendências anteriores de URL, acesso e acompanhamento SE-Ouv e sua representação Serigy. Não foram criadas novas rotas de cadastro, formulário, declarações de inexistência ou atendimento. Os dois novos modelos permanecem fora de dist; nenhuma informação do decreto foi convertida automaticamente em instrução local.
