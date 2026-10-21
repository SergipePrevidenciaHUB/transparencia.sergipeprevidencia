# LGPD e Governo Digital — modelos não publicados

## Escopo, fontes e aplicabilidade

Esta etapa prepara **somente LGPD**, critérios **14.1 e 14.2 da Cartilha PETP 2026**, pp. 107–109 (apenas a continuação de 14.2 na p. 109). Lidos `AGENTS.md`, esses trechos, Serigy Docs **14. LGPD e Governo Digital**, seção **14.1. LGPD**, p. 1 e exemplos correspondentes das pp. 1–2, e o modelo não publicado de Ouvidoria apenas como padrão visual. **C** = requisito da Cartilha; **S** = marcação técnica; **DT** = decisão de apresentação. Não houve consulta externa nem validação de nome, contato, política ou documento institucional.

Os dois critérios incluem expressamente **Previdências Municipais e Estadual** no quadro de aplicabilidade e exigem somente **Disponibilidade**. C 14.1 é classificado obrigatório; C 14.2, recomendado. Essa classificação não elimina o segundo do escopo nem autoriza presumir política inexistente.

## Rota e isolamento

Caminho literal de S 14.1: `[Portal da Transparencia]/LGPDeGovernoDigital`. Modelo: `modelos/Portal-da-Transparencia/LGPDeGovernoDigital/index.html`. Rota prevista: `/Portal-da-Transparencia/LGPDeGovernoDigital/`. **Não adicionar `/LGPD`** por dedução do título da seção. Não há coincidência com modelos de SIC/Ouvidoria; nenhum deles foi alterado.

O modelo fica fora de dist, sem menu público ou alteração de deploy. Reutiliza visual, cabeçalho, rodapé, breadcrumb, busca e acessibilidade existentes. O main contém apenas `serigySchema="https://serigy.tce.se.gov.br/comum/lgpd-governo-digital.html"`. Reservas de dados estão vazias, sem serigyItem, serigyValue, serigyEmpty, serigyLink ou atributos funcionais. Contatos gerais do rodapé permanecem gerais e não foram declarados como canal do encarregado.

## Correspondência exata Cartilha–Serigy

| Critério C / fonte | Item S / tipo literal | Reserva e conteúdo necessário |
| --- | --- | --- |
| 14.1, p. 107: identificação do encarregado/responsável pelo tratamento de dados pessoais | 14.1.1 `nomeResponsavel` — Nome | `#nome-encarregado-lgpd`: nome confirmado pela instituição |
| 14.1: canal de comunicação com esse servidor, telefone e/ou e-mail | 14.1.2 `contatoResponsavel` — Telefone ou E-mail | `#contato-encarregado-lgpd`: contato institucional confirmado para essa função |
| 14.2, pp. 108–109: Política de Privacidade e Proteção de Dados adotada pela Unidade | 14.1.3 `politicaPrivacidade` — Link | `#identificacao-politica-lgpd` e `#acesso-politica-lgpd`: identificação e acesso integral à política real |

S 14.1.1 e 14.1.2 atendem **C 14.1**; S 14.1.3 atende **C 14.2**, não um critério C 14.1.3. Os itens técnicos não são critérios normativos novos. As propriedades só serão aplicadas ao conteúdo/acesso real e no contexto do schema correto.

### Encarregado e comunicação

**C:** publicar nome do encarregado/responsável e canal de comunicação com ele. A redação é **telefone e/ou e-mail**, não obrigação cumulativa dos dois contatos. **DT:** lista editorial de definições, mantendo nome e comunicação associados na mesma seção; não há tabela obrigatória ou cadastro público em planilha. Se houver ambos os meios confirmados, podem ser apresentados e marcados individualmente com `contatoResponsavel`, sem inventar propriedades específicas.

Não deduzir o encarregado do gestor, da Ouvidoria, do SIC ou dos contatos gerais. Não copiar nome/telefone/e-mail do exemplo municipal S. A fonte da designação pode ser solicitada para conferir a identidade, mas C 14.1 não exige neste recorte anexar um ato de designação, fotografia, currículo, CPF ou telefone pessoal. Nenhum desses campos foi criado.

### Normas legais, atos e política institucional

**Distinção das fontes:** C 14.1 cita a LGPD (Lei nº 13.709/2018) e a Lei nº 14.129/2021 como fundamentação. Isso não é a mesma coisa que a **Política de Privacidade e Proteção de Dados adotada pela Unidade**, exigida em C 14.2. Publicar apenas a lei federal, uma referência genérica à LGPD ou um ato de designação não substitui essa política.

C 14.2 exige a política adotada; S documenta `politicaPrivacidade` como Link. **DT:** acesso identificado à versão integral em HTML ou documento oficial, conforme a fonte institucional. O modelo reserva identificação e acesso, sem inventar cláusulas ou gerar política genérica. Não impor dois documentos separados (“privacidade” e “proteção de dados”) se a política real é única, nem presumir sua estrutura, conteúdo, versão ou URL.

Não há item S específico de norma geral ou ato de designação nesta seção; não foram criados bloco de biblioteca normativa, propriedades para normas ou anexos obrigatórios adicionais. Se uma fonte institucional distinguir vários instrumentos, registrar a relação e a finalidade antes de decidir como apresentá-los; não confundir o suporte normativo com a política adotada. Receber e conferir política e destino oficial; não copiar `local/arquivo` do exemplo ou criar URL por nome/ano. Não usar serigyLink para PDF.

## Limites dos controles e do restante da dimensão

C 14.1/14.2 não listam filtro, histórico, gravação de relatórios, data de atualização autônoma ou periodicidade numérica. S 14.1.1–14.1.3 também não documenta esses controles. Não há formulário de coleta, botão de exportação, seletor de exercício ou data fictícia. Se futuramente for útil indicar versão/data como metadado editorial, será DT com fonte real, não novo mínimo C ou serigyItem inventado.

A seção S 14.1 também relaciona **14.1.4 `pesquisaSatisfacao` e 14.1.5 `resultadoSatisfacao` ao critério C 14.5**. Isso não os torna requisitos de C 14.1/14.2: pesquisas e resultados não foram modelados nesta rodada. Quando forem preparados, respeitar a rota compartilhada e preservar os blocos LGPD, sem inventar nova rota ou sobrescrever o modelo. Serviços Públicos (S 14.2 ↔ C 14.3) e Dados Abertos (S 14.3 ↔ C 14.4) também ficam fora deste recorte; não foram criados outros modelos.

## Alimentação e publicação

Pendências em `controle/lgpd-governo-digital-pendencias.md`. Receber identificação do encarregado, canal para sua função e política adotada; conferir identidade, vinculação, integridade, versão e acesso público. Preencher apenas conteúdo confirmado e aplicar os três itens S correspondentes. Testar comunicação e destino documental sem enviar mensagens ou dados reais sem autorização. Validar teclado, rótulos e acesso antes de mover para dist em tarefa autorizada. A existência de campos vazios ou de um link não declara conformidade LGPD nem atendimento aos critérios.
