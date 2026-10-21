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

A seção S 14.1 também relaciona **14.1.4 `pesquisaSatisfacao` e 14.1.5 `resultadoSatisfacao` ao critério C 14.5**. Isso não os torna requisitos de C 14.1/14.2. O complemento 14.5 abaixo registra sua preparação e a integração estrutural ao modelo raiz, preservando encarregado e política. Os modelos Serviços Públicos (S 14.2 ↔ C 14.3) e Dados Abertos (S 14.3 ↔ C 14.4) permanecem em suas rotas próprias.

## Alimentação e publicação

Pendências em `controle/lgpd-governo-digital-pendencias.md`. Receber identificação do encarregado, canal para sua função e política adotada; conferir identidade, vinculação, integridade, versão e acesso público. Preencher apenas conteúdo confirmado e aplicar os três itens S correspondentes. Testar comunicação e destino documental sem enviar mensagens ou dados reais sem autorização. Validar teclado, rótulos e acesso antes de mover para dist em tarefa autorizada. A existência de campos vazios ou de um link não declara conformidade LGPD nem atendimento aos critérios.


## Complemento — Serviços Públicos Digitais

**Fontes efetivamente consultadas:** AGENTS.md; **C 14.3, pp. 109–110** da Cartilha PETP 2026; Serigy Docs 14, **seção 14.2. Serviços Públicos**, item **14.2.1**, p. 1 e continuação do exemplo na p. 2; estes dois controles e o modelo LGPD existente como padrão visual. Mantêm-se C (requisito), S (item técnico) e DT (organização proposta). Esta etapa trata apenas de Serviços Públicos; não altera o escopo executado da etapa anterior de LGPD.

**Código e aplicabilidade:** C **14.3** corresponde a S **14.2.1 `servicoPublico` (Link)**, na seção S **14.2**. C o classifica como obrigatório, inclui expressamente Previdências Municipais e Estadual e exige somente **Disponibilidade**. Não confundir S 14.2 com o critério C 14.2 de política de privacidade.

### Rota própria, sem variante

S documenta `[Portal da Transparencia]/LGPDeGovernoDigital/Servicos`, portanto a rota prevista é **`/Portal-da-Transparencia/LGPDeGovernoDigital/Servicos/`**. Modelo: `modelos/Portal-da-Transparencia/LGPDeGovernoDigital/Servicos/index.html`.

É uma subpágina própria, **não o mesmo caminho de `/LGPDeGovernoDigital/`**. Não foi criada variante em `modelos/variantes/servicos-publicos/` e não é necessário reunir os blocos ao HTML de LGPD para respeitar a rota. O modelo de LGPD permanece inalterado. O breadcrumb do novo modelo aponta à rota pai existente na árvore de modelos; isso não cria link no menu público nem declara a rota pai publicada. Eventual navegação futura será tratada quando houver conteúdo autorizado para dist.

Modelo fora de dist, sem alteração de menus ou deploy. Reutiliza cabeçalho, rodapé, tipografia, cores e acessibilidade. O main contém somente `serigySchema="https://serigy.tce.se.gov.br/comum/lgpd-governo-digital.html"`; não há itens de dados, URLs de serviços, marcação de ausência ou ações sobre conteúdo vazio.

### O que o critério exige e o que será preparado

C 14.3 exige possibilidade de **demandar e acessar serviços públicos por meio digital, sem necessidade de solicitação presencial**. São atendimentos e procedimentos administrativos/operacionais, distintos de pedidos de acesso à informação do e-SIC. Os exemplos de medicamentos, agendamento, guias e débitos em C são ilustrativos; não foram convertidos em serviços do SergipePrevidência. Os links de contribuinte, protocolo, servidor e imóvel em S também não são dados institucionais.

| Elemento do modelo | Origem / finalidade | Marcação futura |
| --- | --- | --- |
| `#lista-servicos-digitais` | DT: lista dos serviços efetivamente confirmados, com nome identificável e acesso ao destino pertinente; C exige funcionalidade digital, não tabela de cadastro | S 14.2.1 `servicoPublico` (Link) nos acessos reais aos serviços, sob o schema da dimensão |
| Identificação e eventual descrição breve de cada serviço | DT para que o cidadão reconheça o atendimento antes de abrir o destino; conteúdo deve vir da área responsável | Sem propriedade própria de nome/descrição na seção S; não inventar atributos |
| `#orientacao-acesso-servicos` | DT: orientação de acesso validada, associada a cada serviço quando necessária; não contém procedimentos presumidos | Sem item técnico próprio documentado para etapas, requisitos ou prazos |
| Eventuais documentos/instruções vinculados | Apenas se fornecidos e pertinentes ao serviço real; C/S consultados não impõem anexo documental adicional neste critério | Não marcar documento genérico como se fosse o acesso digital ao serviço; não inventar item de anexo |

O ul está vazio, sem li fictício, links `#`, destinos exemplificativos ou `servicoPublico` em contêiner vazio. O bloco de orientação também está vazio. O texto geral de distinção dos serviços e do e-SIC deriva de C, sem afirmar que algum serviço institucional esteja funcionando.

**Verificação funcional pendente:** lista ou botão isolados não comprovam o critério. Para cada serviço fornecido, conferir destino e vínculo à Unidade e verificar a demanda/acesso digital previsto, sem presumir atendimento pela presença de link ou página inicial de plataforma. Conferir as condições reais de utilização; não inventar cadastro, forma de identificação, canal, autenticação, prazos, passos ou conclusão de atendimento. Não realizar solicitação administrativa real sem autorização.

### Relação com Carta de Serviços e limites

Pode haver reaproveitamento futuro da identificação e das orientações de um catálogo institucional validado, preservando suas finalidades. **Não transportar automaticamente os seis conteúdos mínimos da Carta de Serviços (C 13.3) como novas colunas obrigatórias de C 14.3.** Carta ou documento descritivo não prova a existência do canal digital. e-SIC ou canal de manifestações de Ouvidoria tampouco substituem serviços administrativos e operacionais por terem acesso eletrônico.

C 14.3 e S 14.2.1 não exigem filtro específico, consulta tabular, histórico, exportação, relatório, formato documental, data de atualização autônoma ou periodicidade numérica. Esses elementos não foram criados. A busca comum do cabeçalho é recurso geral preservado. Nenhum serviço, documento ou URL institucional foi recebido/validado nesta tarefa; os contatos gerais do rodapé não foram transformados em canal de prestação.

### Alimentação e publicação

Receber catálogo real, identificação, URLs oficiais de serviços e orientações necessárias; conferir finalidade, vínculo, acesso digital e condições reais com a área responsável. Aplicar `servicoPublico` somente aos links funcionais e confirmados. Conferir documentos eventualmente fornecidos sem gerar endereço presumido ou usar serigyLink para PDF. Resolver pendências do controle, testar destinos e acessibilidade, alimentar dados reais e só então mover para dist em tarefa autorizada. Nenhuma afirmação de atendimento ou de completude foi criada, nem conteúdo da LGPD sobrescrito.


## Complemento — Dados Abertos

**Fontes efetivamente consultadas:** AGENTS.md; Cartilha PETP 2026, **critério 14.4, pp. 111–112**; Serigy Docs 14, **seção 14.3. Dados Abertos**, tabela e exemplo da p. 1; estes dois controles e o modelo de Serviços como referência visual. A tabela S da dimensão foi conferida também para o quadro de cobertura abaixo. **C** = requisito formal; **S** = marcação técnica; **DT** = escolha de apresentação. Não foram auditados conjuntos reais ou arquivos de outras dimensões nesta rodada.

### Código, aplicabilidade e rota

**C 14.4 ↔ S 14.3.1 `dadosAbertos` (Texto)**. O critério C é obrigatório, exige somente Disponibilidade e inclui expressamente Previdências Municipais e Estadual. A seção técnica S 14.3 não corresponde ao critério C 14.3 (Serviços Públicos).

Caminho literal S: `[Portal da Transparencia]/LGPDeGovernoDigital/DadosAbertos`. Rota prevista: **`/Portal-da-Transparencia/LGPDeGovernoDigital/DadosAbertos/`**. Modelo: `modelos/Portal-da-Transparencia/LGPDeGovernoDigital/DadosAbertos/index.html`. É rota própria, não compartilhada com o HTML raiz LGPD ou Serviços; não foi criada variante e nenhum modelo anterior foi sobrescrito.

O arquivo está fora de dist, sem link no menu público e sem alteração de deploy. Reutiliza visual, cabeçalho, rodapé, breadcrumb e acessibilidade. O link do breadcrumb ao pai é referência à rota já preparada na árvore de modelos, não promessa de publicação. O main contém apenas o contexto `serigySchema="https://serigy.tce.se.gov.br/comum/lgpd-governo-digital.html"`, sem marcação de dados ou ações sobre conteúdo vazio.

### Requisitos formais e organização técnica

**C p. 111:** dados divulgados devem ser legíveis por máquina e em formato aberto; deve haver acesso automatizado por sistemas externos, e a página deve conter regras de utilização com seções detalhadas e exemplos. Neste ciclo, C considera o mínimo atendido quando houver pelo menos um caso de dados legível por máquina; isso não elimina as regras e exemplos nem comprova os outros critérios do Portal. O modelo vazio não constitui esse caso e não declara atendimento.

| Elemento preparado | Exigência C / escolha DT | Marcação S futura |
| --- | --- | --- |
| `#catalogo-dados-abertos`, tbody `#conjuntos-dados-abertos` | Catálogo tabular é **DT**, não formato de apresentação obrigatório. Organiza os conjuntos realmente aprovados | Não há itens próprios S para cada coluna ou arquivo |
| Colunas Conjunto e Descrição | **DT** para identificação do conteúdo disponível, sem inventar nome ou assunto institucional | Não criar propriedades como `nomeConjunto` ou `descricaoConjunto` |
| Coluna Formato | **DT** de identificação do formato realmente disponibilizado; **C** exige aberto e legível por máquina | Sem propriedade específica de formato; não selecionar extensões sem arquivo real |
| Coluna Acesso aos dados | **C** exige acesso automatizado; a apresentação como link para arquivo ou acesso real é **DT** | `dadosAbertos` é Texto, não propriedade de endpoint ou download por coluna |
| `#regras-dados-abertos` | **C** exige regras de utilização em seções detalhadas; títulos e conteúdo específicos dependem da fonte validada | Aplicar `dadosAbertos` ao conteúdo real correspondente, no contexto da página, nunca a um bloco vazio |
| `#exemplos-dados-abertos` | **C** exige exemplos; preparar depois de conhecer arquivos/URLs e regras reais | Não inventar novo item de exemplo nem copiar chamadas ilustrativas S |

O catálogo tem somente cabeçalhos e tbody vazio, sem linhas de dados, nomes de conjuntos, links, formatos ou datas. Regras e exemplos também estão vazios. Os títulos são reservas de estrutura, não conteúdo de uso já existente. Na alimentação, associar cada conjunto, formato, acesso e instrução de maneira clara. O escopo do item S deverá conter informação real de dados abertos/regras/acesso; não marcar apenas um título de seção como evidência de disponibilização.

### Formatos, consulta, atualização, licenças e acesso

- **C não fixa lista cumulativa de extensões.** Escolher e validar formato aberto realmente legível por máquina, conforme os dados autorizados. Não inserir CSV, JSON ou qualquer outra extensão como obrigação autônoma, nem produzir catálogo de arquivos inexistentes. PDF isolado ou apenas descrição de arquivo não comprova acesso a dados estruturados legíveis por máquina.
- **API não é obrigatória nos trechos consultados.** O exemplo S com GET e caminhos de API é ilustrativo; não comprova endpoint institucional nem impõe servidor, rotas, botões GET, autenticação ou parâmetros. Arquivos públicos adequados podem ser uma solução DT, desde que o acesso automatizado e as regras sejam verificados. Não gerar URL por suposição ou usar serigyLink para PDF/JSON.
- **Consulta:** C 14.4 não lista filtro específico, campos mínimos de pesquisa ou consulta tabular; S 14.3.1 não documenta filtroPesquisa. A tabela é apenas índice DT, sem formulário de consulta. A busca comum é componente geral preservado.
- **Atualização e histórico:** não há item autônomo de atualidade, periodicidade, série ou `dataUltimaAtualizacao`/`historicoExercicio` nesta seção. Não inventar data, frequência ou cobertura; eventual referência temporal de um conjunto será metadado DT com fonte real. As regras de atualização/histórico do critério de origem do conjunto não são dispensadas por sua inclusão neste catálogo.
- **Gravação:** não há `salvarRelatorio` documentado nem item autônomo de exportação em C 14.4. Acesso aos arquivos abertos é conteúdo desta página, não promessa de exportação filtrada. Não confundir catálogo de dados abertos com requisitos de gravação dos demais critérios.
- **Licença/regras:** C exige regras de utilização, mas não estabelece licença nominal, texto-padrão ou obrigação de adotar uma licença específica. Receber regras institucionais e exemplos validados; não inventar licença, atribuição, restrição, cobrança ou condição de reutilização. Se houver política/licença efetivamente adotada, registrar a fonte e a relação com os conjuntos antes de publicá-la.

Não publicar automaticamente planilha de origem, dados pessoais, credenciais ou cadastros operacionais. A aprovação de derivados e a proteção do conteúdo são controles de publicação do projeto; não são novos campos normativos de C 14.4. Arquivos de teste existentes não foram homologados nem reaproveitados como prova de dados abertos reais.

### Cobertura da dimensão 14 após esta etapa

Este quadro é **cobertura de modelos e mapeamento**, não declaração de atendimento, dados disponíveis ou validação para publicação.

| Critério C | Itens S correspondentes | Modelo / situação |
| --- | --- | --- |
| 14.1 — encarregado e comunicação | 14.1.1 nomeResponsavel; 14.1.2 contatoResponsavel | Raiz `LGPDeGovernoDigital/index.html`, preparado anteriormente; sem alimentação homologada |
| 14.2 — política de privacidade | 14.1.3 politicaPrivacidade | Mesmo modelo raiz, preservado; política e acesso pendentes |
| 14.3 — serviços públicos digitais | 14.2.1 servicoPublico | `LGPDeGovernoDigital/Servicos/index.html`, preparado e preservado; catálogo/funcionalidade pendentes |
| 14.4 — dados abertos | 14.3.1 dadosAbertos | `LGPDeGovernoDigital/DadosAbertos/index.html`, criado nesta etapa; conjuntos/regras/exemplos pendentes |
| 14.5 — pesquisas e resultados de satisfação | 14.1.4 pesquisaSatisfacao; 14.1.5 resultadoSatisfacao | Bloco integrado ao modelo raiz após a política; fragmento de origem preservado em `modelos/variantes/pesquisas-satisfacao/bloco-satisfacao.html`; pesquisa e resultados oficiais pendentes |

São três modelos de página para a dimensão: a raiz reúne a estrutura de 14.1, 14.2 e 14.5; Servicos contempla 14.3 e DadosAbertos contempla 14.4. A cobertura é estrutural e não publicada, sem alimentação ou atendimento comprovado. O fragmento de satisfação permanece como referência, sem página ou rota adicional.

### Alimentação e publicação

Receber conjunto(s) autorizado(s), arquivos/acesso reais, formato confirmado, regras em seções e exemplos coerentes com os destinos. Validar leitura por máquina e acesso automatizado, conteúdo público, integridade e relação com o período/fonte. Escolher metadados e organização conforme a origem sem transformar DT em obrigação C. Aplicar `dadosAbertos` somente após haver conteúdo real, testar acesso e exemplos, HTML e acessibilidade antes de mover para dist em tarefa autorizada. As pendências abaixo e no controle específico não estão resolvidas pelo desenho do modelo.


## Complemento — 14.5: pesquisas e resultados de satisfação

**Fontes efetivamente consultadas:** AGENTS.md; **Cartilha PETP 2026, p. 113**, critério 14.5; Serigy Docs 14, seção **14.1. LGPD**, itens **14.1.4 e 14.1.5** (p. 1) e exemplo correspondente (p. 2); estes dois controles e modelo raiz existente. Mantém-se C (requisito), S (item técnico) e DT (apresentação/integração).

### Texto exato, aplicabilidade e verificação

**Redação C:** “14.5 Realiza e divulga resultados de pesquisas de satisfação?”

**Classificação:** obrigatória. **Aplicabilidade:** Administração Direta e Indireta do Estado, Administração Indireta de Aracaju e **Previdências Municipais e Estadual**. **Itens exigidos:** somente **Disponibilidade**.

**Conteúdo C:** divulgar resultados de pesquisas de satisfação aplicadas regularmente, para participação dos usuários na avaliação dos serviços, identificação de lacunas/deficiências e reorientação da prestação. As frequências anual, semestral ou após interação relevante são exemplos, não um prazo único obrigatório. Pesquisas de Ouvidoria, cursos/treinamentos e atendimento em unidades são exemplos de aplicação; não impor pesquisas separadas para todos esses públicos como novos critérios.

| Critério C | Item S / descrição | Tipo literal S | Reserva futura |
| --- | --- | --- | --- |
| 14.5 | 14.1.4 `pesquisaSatisfacao` — realiza pesquisas de satisfação | Link ou Forms | `#acesso-pesquisa-satisfacao`, hoje vazio e sem item |
| 14.5 | 14.1.5 `resultadoSatisfacao` — divulga resultados de pesquisas | Link, Imagem ou Texto | `#conteudo-resultados-satisfacao`, hoje vazio e sem item |

O instrumento/acesso à pesquisa e seus resultados são conteúdos distintos. **Um link para responder, sozinho, não comprova divulgação de resultados**; dados de SIC ou manifestações de Ouvidoria não são automaticamente pesquisa de satisfação. Não copiar o endereço ou a referência temporal ilustrativa S como dados da Unidade.

### Localização: bloco na rota já prevista, sem página nova

S coloca ambos os itens na seção 14.1, caminho `[Portal da Transparencia]/LGPDeGovernoDigital`. A estrutura de 14.5 já está integrada ao modelo dessa rota **`/Portal-da-Transparencia/LGPDeGovernoDigital/`**, após a política e junto aos blocos de encarregado, **não** em nova rota `/Satisfacao`. A página continua não publicada e sem conteúdo oficial de pesquisa/resultados.

**Fragmento de origem preservado:** `modelos/variantes/pesquisas-satisfacao/bloco-satisfacao.html`. É referência de seção, não documento HTML independente ou página pública. Sua estrutura foi incorporada ao modelo principal; o arquivo de origem não foi alterado nem excluído. A classe `content-box`, títulos e contexto do schema foram mantidos, sem itens de dados em campos vazios.

**Integração estrutural concluída (DT):** a seção `#pesquisas-satisfacao` foi inserida no main de `modelos/Portal-da-Transparencia/LGPDeGovernoDigital/index.html`, após a seção da política e antes do fechamento de main. Cabeçalho, rodapé, estilos, acessibilidade, breadcrumb, blocos LGPD e marcações anteriores foram preservados. Há somente um main e um h1; os IDs e rótulos foram validados sem colisões. Não publicar a árvore variantes como destino próprio nem reinserir o fragmento duplicando IDs. A alimentação com pesquisa e resultados oficiais permanece pendente.

### Alimentação: conteúdo real e escolhas de apresentação

**DT:** bloco de acesso à pesquisa e bloco de resultados, com identificação que permita associar cada resultado à pesquisa e ao período ou aplicação reais. A identificação do período/serviço, metodologia, categorias e bases de cálculo deve vir da fonte institucional quando necessária para compreender o resultado; não transforma exemplos em colunas normativas fixas.

Receber instrumento/forma real de aplicação, evidência da regularidade adotada e resultados efetivamente produzidos. Definir Link/Forms ou Link/Imagem/Texto conforme a fonte e a apresentação real. S admite essas alternativas; não obriga PDF, planilha, gráfico, formulário próprio ou todas as modalidades simultaneamente. Não criar formulário de coleta sem necessidade comprovada, operação ou dados de origem.

Resultados podem ser apresentados em texto, imagem/gráfico ou documento realmente existente, conforme S e fonte. Garantir leitura e acesso ao conteúdo real, sem produzir notas, escalas, percentuais, NPS, respondentes, datas ou relatórios fictícios. Não misturar populações ou períodos; não publicar respostas individuais identificáveis ou base privada. A aplicação regular deve ser confirmada pela área; um arquivo isolado não prova regularidade nem representa todas as pesquisas existentes.

C 14.5 não enumera série histórica mínima, filtros, gravação, escala de avaliação, periodicidade fixa ou item autônomo de atualização. S 14.1.4–14.1.5 não documenta esses controles. Não foram criados seletor de exercício, tabela vazia de notas, formatos obrigatórios, botão exportar ou `dataUltimaAtualizacao`. Ausência desses controles autônomos não elimina a exigência de pesquisas regularmente aplicadas e resultados divulgados. Referências temporais editoriais futuras usarão somente dados reais da aplicação, sem data do dia por geração.

### Cobertura atual consolidada de 14.1–14.5

| Critério C | Itens S | Estrutura preparada | Pendência de alimentação |
| --- | --- | --- | --- |
| 14.1 | 14.1.1 nomeResponsavel; 14.1.2 contatoResponsavel | Modelo raiz, preservado | Identidade do encarregado e canal confirmado |
| 14.2 | 14.1.3 politicaPrivacidade | Modelo raiz, preservado | Política adotada e acesso integral |
| 14.3 | 14.2.1 servicoPublico | Modelo Servicos, preservado | Serviços, URLs, orientações e funcionamento digital |
| 14.4 | 14.3.1 dadosAbertos | Modelo DadosAbertos, preservado | Conjuntos autorizados, arquivos/acesso, regras e exemplos |
| 14.5 | 14.1.4 pesquisaSatisfacao; 14.1.5 resultadoSatisfacao | Integrado ao modelo raiz após a política; fragmento preservado como referência | Pesquisa/instrumento, acesso real, regularidade, resultados oficiais e referências da aplicação |

A sequência de preparação estrutural contempla agora os cinco critérios, mas nenhum campo vazio comprova atendimento e as pendências institucionais permanecem. Não se declara a dimensão homologada, completa em dados ou pronta para publicação.

### Antes da publicação de 14.5

Receber e validar pesquisas/aplicações e resultados oficiais, definir apresentação real e conferir eventuais URLs/arquivos. Associar resultado e pesquisa, preencher conteúdo e aplicar apenas os dois itens S nos elementos reais. A integração estrutural já foi concluída no modelo não publicado; falta alimentar e testar acesso, legibilidade e acessibilidade antes da publicação autorizada. Não enviar resposta ou contato externo para testar sem autorização. Nesta integração foram alterados somente o modelo principal e os dois controles; dist, menus, deploy, demais modelos e fragmento de origem foram preservados.
