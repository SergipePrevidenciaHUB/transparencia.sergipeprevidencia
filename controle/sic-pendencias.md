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
