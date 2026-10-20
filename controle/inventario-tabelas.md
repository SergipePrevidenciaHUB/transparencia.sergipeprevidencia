# Inventário e desenho dos dados — tabelas, documentos e estatísticas

## 1. Escopo e método

Levantamento do site institucional e Portal da Transparência do SergipePrevidência, exclusivamente para a **Previdência Estadual**. Foram percorridos os **66 critérios** da Cartilha PETP 2026 e os PDFs Serigy PETP 2026 disponíveis no projeto. Todos os quadros de aplicabilidade incluem as previdências; ressalvas de natureza jurídica/emissão de documentos são preservadas, especialmente em 10.4. Ausência de implementação ou de fatos não foi tratada como inaplicabilidade.

Há **55 fichas**: **43 critérios centrais** de conjuntos consultáveis, documentos ou estatísticas e **12 complementares** de cadastros, conteúdo editorial e índices. Os 11 critérios funcionais restantes estão discriminados na cobertura da seção 8: sua exclusão deste recorte não significa dispensa de atendimento.

Categorias deste levantamento: **A** — dados estruturados para consulta; **B** — relações/índices e conteúdo de documentos; **C** — relatórios/resultados estatísticos apresentáveis em tabela. São categorias editoriais, não novos critérios PETP. Um cadastro complementar não exige automaticamente planilha ou tabela pública.

- **C — exigência oficial:** redação, aplicabilidade, conteúdo, filtros, atualidade, histórico e formatos expressos na Cartilha.
- **S — requisito técnico:** propriedades, tipos e estruturas documentados no Serigy. Seus códigos de itens não são novos critérios da Cartilha.
- **DT — decisão técnica proposta:** conjuntos/abas, entrada e reaproveitamento para o nosso site, sem inventar informações institucionais ou novas obrigações.
- **Lacuna:** dependência de fonte institucional ou divergência; quando não resolvida, **DÚVIDA — REVISÃO NECESSÁRIA**.

As redações oficiais são preservadas com normalização apenas de quebras de linha/espaçamento. Nenhum XLSX foi criado. Este levantamento não homologa informações, prazos locais ou links externos.

## 2. Fontes efetivamente consultadas

Os 18 PDFs listados abaixo foram extraídos pela função de `tools/extrair_pdf.py`, com o Python do ambiente virtual e sem instalação. Todas as extrações foram legíveis. Textos e conferências intermediárias ficaram em pasta temporária do sistema, fora do projeto. A paginação citada usa os separadores da extração e coincide com a impressa na Cartilha.

- **C:** `referencias/petp/Cartilha PETP 2026 Sergipe VERSÃO FINAL v2.pdf` — 116 página(s).
- **S1:** `referencias/serigy/1. Informações Prioritárias _ Serigy Docs.pdf` — 1 página(s).
- **S10:** `referencias/serigy/10. Planejamento e Prestação de Contas _ Serigy Docs.pdf` — 2 página(s).
- **S11:** `referencias/serigy/11. Serviço de Informação ao Cidadão - SIC _ Serigy Docs.pdf` — 3 página(s).
- **S12:** `referencias/serigy/12. Acessibilidade _ Serigy Docs.pdf` — 1 página(s).
- **S13:** `referencias/serigy/13. Ouvidorias _ Serigy Docs.pdf` — 1 página(s).
- **S14:** `referencias/serigy/14. LGPD e Governo Digital _ Serigy Docs.pdf` — 2 página(s).
- **S2:** `referencias/serigy/2. Institucional _ Serigy Docs.pdf` — 3 página(s).
- **S3:** `referencias/serigy/3. Receitas _ Serigy Docs.pdf` — 2 página(s).
- **S4:** `referencias/serigy/4. Despesas _ Serigy Docs.pdf` — 3 página(s).
- **S5:** `referencias/serigy/5. Convênios e Transferências _ Serigy Docs.pdf` — 3 página(s).
- **S6:** `referencias/serigy/6. Recursos Humanos _ Serigy Docs.pdf` — 4 página(s).
- **S7:** `referencias/serigy/7. Diárias _ Serigy Docs.pdf` — 2 página(s).
- **S8:** `referencias/serigy/8. Licitações _ Serigy Docs.pdf` — 3 página(s).
- **S9:** `referencias/serigy/9. Contratos _ Serigy Docs.pdf` — 3 página(s).
- **SD:** `referencias/serigy/Definições _ Serigy Docs.pdf` — 3 página(s).
- **S0:** `referencias/serigy/Introdução _ Serigy Docs.pdf` — 1 página(s).
- **SI:** `referencias/serigy/Invoker _ Serigy Docs.pdf` — 1 página(s).

Também foram consultados `AGENTS.md`, os 12 HTMLs atuais de `dist` (oito páginas principais e quatro auxiliares de portarias), `dist/assets/js/site.js`, `dist/assets/js/tabelas.js`, `tools/importar_dados.py`, `tools/importar_portarias.py`, `tools/extrair_pdf.py` e os quatro CSV/JSON de teste de receitas/estagiários em `dist/dados`.

Páginas principais: `dist/index.html`, `dist/Portal-da-Transparencia/index.html`, `dist/mapa-do-site/index.html` e, abaixo de `dist/Portal-da-Transparencia/`, `Institucional/Informacoes/index.html`, `Institucional/AtosNormativos/index.html`, `Institucional/LegislacaoInterna/index.html`, `Receitas/PrevistaArrecada/index.html`, `RecursosHumanos/Estagiarios/index.html`. Auxiliares: os quatro `portariasAAAA.html` em `Institucional/AtosNormativos/portarias/AAAA/`, anos 2023–2026.

Não houve consulta à internet, documentos da CGE ou planilhas privadas. A presença dos PDFs de portarias foi observada pelos caminhos do acervo, mas os seus inteiros teores não foram auditados neste levantamento.

## 3. Regras comuns

### 3.1. Cartilha

- **Disponibilidade:** todos os elementos mínimos precisam estar presentes; atendimento parcial interno não equivale a atendimento oficial (C, pp. 20–21).
- **Não ocorrência:** somente declaração verdadeira, na seção própria, com período abrangido e atualização. Seção vazia não atende. A exceção de 8.6 rejeita declaração de inexistência do PCA como atendimento (C, p. 19 e pp. 71–72).
- **H3:** neste arquivo significa pelo menos os três anos anteriores à consulta, quando exigidos. 10.1–10.3 têm regra específica com X e X-1/X-2/X-3; 6.6 também tem formulação própria. Não reduzir todos os acervos a três exercícios.
- **E:** exportar o conjunto selecionado em pelo menos um formato editável. As extensões exemplificadas não obrigam a oferecer todas. Entre estas fichas, 6.4, 6.5, 8.7 e 9.3 aceitam expressamente PDF pesquisável como alternativa. Exemplo Serigy de PDF não elimina o editável nos demais casos.
- **Documento assinado:** quando aplicável a gravação, o editável acompanha a versão oficial, sem suas assinaturas; preservar a versão oficial assinada (C, p. 20; 10.6, p. 87).
- **Filtros:** busca geral não substitui filtro do conjunto. “Filtro genérico” significa que a C não enumera parâmetros mínimos; não inventá-los como obrigação. Existe a regra geral de pequeno acervo facilmente localizável por Ctrl+F, sem dispensa automática dos filtros específicos; 10.6 traz aceitação expressa da organização única por exercício/mês (C, pp. 20 e 87).
- **Publicação:** transparência ativa sem identificação prévia/login; informação externa com acesso direto e contextualizado à Unidade (C, p. 21). Cadastro operacional e-SIC é distinto de publicação de tabelas abertas.
- **HTML:** 6.1 e 8.1 exigem tabela estruturada em HTML; 6.2 exige relação/tabela e prefere HTML. 6.3 e 7.2 exigem tabela ou relação de valores, admitindo formas documentais descritas. Não transportar essas regras para todos os índices de normas, relatórios ou serviços.
- **Atualidade:** importação, cópia e atualização do site não comprovam atualização do conjunto. Usar a referência real dos dados, sem preencher automaticamente com a data do dia. O parâmetro PETP de 30 dias para finanças não dispensa regras contábeis de tempo real (C, pp. 33 e 37–39).
- **Aplicabilidade:** ressalvas de Matriz II de S2/S10 não autorizam excluir critérios expressamente aplicáveis à Previdência na C. Esclarecer a ressalva específica de emissores/consolidação de RGF em 10.4.

### 3.2. Serigy: schemas e estrutura

A sigla da ficha representa exatamente o valor literal de `serigySchema` abaixo, no mesmo elemento ou em ancestral dos `serigyItem` correspondentes. As siglas não são atributos HTML.

| Sigla | URL literal | Fonte |
| --- | --- | --- |
| INST | `https://serigy.tce.se.gov.br/comum/institucional.html` | S2, p. 1 |
| REC | `https://serigy.tce.se.gov.br/comum/receitas.html` | S3, p. 1 |
| DESP | `https://serigy.tce.se.gov.br/comum/despesas.html` | S4, p. 1 |
| CONV | `https://serigy.tce.se.gov.br/comum/convenios-transferencias.html` | S5, p. 1 |
| RH | `https://serigy.tce.se.gov.br/comum/recursos-humanos.html` | S6, p. 1 |
| DIA | `https://serigy.tce.se.gov.br/comum/diarias.html` | S7, p. 1 |
| LIC | `https://serigy.tce.se.gov.br/comum/licitacoes.html` | S8, p. 1 |
| CONT | `https://serigy.tce.se.gov.br/comum/contratos.html` | S9, p. 1 |
| PC | `https://serigy.tce.se.gov.br/comum/planejamento-prestacao-contas.html` | S10, p. 1; divergência em exemplos |
| SIC | `https://serigy.tce.se.gov.br/comum/sic.html` | S11, p. 1 |
| ACESS | `https://serigy.tce.se.gov.br/comum/acessibilidade.html` | S12, p. 1 |
| OUV | `https://serigy.tce.se.gov.br/comum/ouvidoria.html` | S13, p. 1 |
| LGPD | `https://serigy.tce.se.gov.br/comum/lgpd-governo-digital.html` | S14, p. 1 |

Controles **S**: **F** = `filtroPesquisa`; **G** = `salvarRelatorio`; **A** = `dataUltimaAtualizacao`; **H** = `historicoExercicio`. Cada ficha lista somente os documentados naquele critério. `N/A` é tipo literal do Serigy, não inaplicabilidade da Previdência.

Regras de estrutura (SD, pp. 1–3; exemplos S2–S14):

1. Associar campos do mesmo registro: responsável/currículo, valores da receita, documentos do certame/contrato. Os exemplos tabulares usam campos em células da mesma linha; detalhes devem continuar associados ao registro. Índices podem usar links, listas e contêineres conforme a documentação, sem tabela obrigatória universal.
2. `serigyExecuteWaitSection` na ação corresponde ao `serigyLoadSection` no contêiner que contém os resultados/detalhes. IDs de exemplos não são nomes obrigatórios para o site; usar o componente real.
3. Nos seletores históricos documentados, `historicoExercicio` marca o controle e `serigyValue` identifica os exercícios reais. 2026/2025/2024 nos exemplos não limita o histórico C.
4. Exportação usa `salvarRelatorio` e `serigyValue` do formato efetivamente oferecido. Arquivo funcional e correspondente ao conjunto; não marcar botão vazio ou publicar a planilha privada automaticamente.
5. `serigyClearForm`, quando usado, vai no controle real de limpeza, sem valor. `serigyItemType`/`serigyValue` de formulários seguem a estrutura documentada; não criar nomes de propriedades para campos não previstos.
6. `serigyEmpty` explica ausência intencional de um item, com valor distinto por ocorrência. Não substitui declaração C de não ocorrência com período/atualização.
7. `serigyLink` aponta para HTML externo marcado conforme SD; não presumir extração semântica de PDF/JSON por esse atributo.
8. S0 orienta observar a versão. SI descreve Invoker e não cria critério de dados nem autoriza inserir hash. Nenhum hash foi gerado/inserido.

## 4. Evidência atual e limites do protótipo

| Conjunto/código | Evidência inspecionada | Consequência |
| --- | --- | --- |
| Receitas | 12 registros fictícios com mês/ano/previsto/arrecadado; filtros mês/ano e CSV/JSON de teste. | Reaproveitar o desenho; não declarar acervo real ou completo. Downloads estáticos não acompanham filtro ativo. |
| Estagiários | Oito registros fictícios com nome/admissão/término, filtro por ano de contratação e CSV/JSON de teste. | Reusar as três colunas e derivar o ano; downloads igualmente estáticos. |
| Atos próprios | 323 ementas: 2023: 87; 2024: 62; 2025: 74; 2026: 100. Caminho próprio e três filtros. Há PDFs em subpastas, mas a consulta principal não tem links PDF nem `atoNormativo`; os quatro HTMLs auxiliares também não os vinculam. | Conferir documento por registro, sem deduzir vínculo por número/nome de arquivo, especialmente duplicados. Presença de arquivos não demonstra cobertura. |
| Legislação/estrutura | Lei nº 9.553/2024 vinculada em Informações e Legislação Interna; nesta há `legislacao`. | Reusar uma origem documental; não declarar completo o conjunto 2.9. |
| Conteúdo institucional | Organograma, competências, quatro pares responsável/currículo, contatos/horário, canais e 17 pares FAQ com avisos. | Manter conteúdo editorial quando adequado; não impor XLSX a todos. |
| Demais conjuntos | As páginas principais não implementam consultas próprias para despesas, convênios, folha/padrão, terceirizados, diárias, licitações/sanções, contratos/fiscais/ordem, concursos, contas, SIC estatístico, Carta, política e pesquisas. | Ausência no protótipo não prova inexistência institucional ou inaplicabilidade. |
| Busca | Manifesto de oito páginas principais; texto de `main`. PDFs e quatro HTMLs auxiliares de portarias não estão no manifesto. | Busca geral não substitui consultas específicas; coordenar futuras páginas com mapa/navegação. |
| Importadores | `importar_dados.py` só implementa receitas/estagiários, aceita CSV/XLS/XLSX/JSON e lê a primeira aba XLSX por padrão. Conversor de portarias gera a região delimitada da página própria e verifica duplicidades/anos. | Multiabas/novos conjuntos exigirão evolução autorizada. O importador atual não atualiza automaticamente todos os links de exportação, opções de filtro e metadados. Não foram executados. |

## 5. Fichas por critério

M01–M10 são os modelos propostos na seção 7, não arquivos criados. Referência temporal e de arquivo deve vir da fonte real. O código da ficha é sempre da Cartilha; os códigos internos S apenas identificam a documentação técnica.


### Dimensão 2 — Institucional

#### 2.1 — Divulga a sua estrutura organizacional e a norma que a institui/altera?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A/B**. C, p. 26; S2, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Norma atualizada na íntegra; estrutura textual ou gráfica com hierarquia entre unidades; data de atualização.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar os requisitos de conteúdo e vigência descritos.
- **S — marcação e estrutura:** INST; S2 2.1.1–2.1.2: estruturaOrganizacional e normaEstruturaOrganizacional (Variável). Texto/imagem da estrutura e conteúdo ou acesso à norma, no escopo institucional. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Cadastro documental M01 para a norma; manter organograma e texto em HTML/imagem. Não exigir planilha da hierarquia.
- **Compartilhamento:** 2.2, 2.3 e 2.9, com uma única versão documental.
- **Documentos integrais/vínculos:** Norma que institui/altera a estrutura e complementos efetivamente vigentes.
- **Lacuna ou ambiguidade:** Organograma e vigência dependem de validação institucional; um PDF presente não comprova a estrutura vigente.

#### 2.2 — Divulga competências e/ou atribuições?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A/B — complementar**. C, p. 26; S2, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Descrição sintética das competências/atribuições ou acesso direto à legislação que as contenha, junto à estrutura, facilmente localizável.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar os requisitos de conteúdo e vigência descritos.
- **S — marcação e estrutura:** INST; S2 2.1.3: competencias (Texto); admite conteúdo e redirecionamento documentado. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Manter texto validado em HTML; se adotada norma vinculada, usar o catálogo M01. Nenhum XLSX próprio.
- **Compartilhamento:** 2.1 e 2.9: mesma legislação, sem duplicar o texto de origem.
- **Documentos integrais/vínculos:** Norma pertinente somente se essa for a forma de apresentação escolhida.
- **Lacuna ou ambiguidade:** Não transformar incisos em novas colunas obrigatórias. Redação consolidada ainda exige confirmação institucional.

#### 2.3 — Identifica o nome dos responsáveis pela gestão da Unidade, com currículo resumido?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A/B**. C, p. 27; S2, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Identificação nominal dos responsáveis pela gestão e currículo resumido; considerar os responsáveis pelas unidades representadas no organograma.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar os requisitos de conteúdo e vigência descritos.
- **S — marcação e estrutura:** INST; S2 2.1.4 responsavel (Texto) e 2.1.5 curriculoResumido (Texto/Arquivo/Link). Manter cada par associado no mesmo registro HTML. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Registros editoriais em HTML, como os quatro existentes; M01 apenas para currículos em arquivo, se utilizados. Não exigir XLSX próprio nem fotografia como campo PETP.
- **Compartilhamento:** 2.1: unidades; 6.1: nomes/cargos apenas se forem os mesmos vínculos confirmados.
- **Documentos integrais/vínculos:** Currículo resumido pode ser texto, arquivo ou link; não é necessário inventar PDF.
- **Lacuna ou ambiguidade:** S2 cita 2.3.1 para currículo, inexistente como critério autônomo C. Matriz II é ressalva técnica; planejar nome e currículo. Abrangência dos responsáveis permanece a esclarecer, sem presumir todas as gerências nem somente diretores.

#### 2.4 — Divulga os endereços e telefones atuais da Unidade e e-mails institucionais?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A — complementar**. C, p. 27; S2, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Endereços e telefones atuais e e-mails institucionais; a Cartilha aceita inclusive rodapé.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar os requisitos de conteúdo e vigência descritos.
- **S — marcação e estrutura:** INST; S2 2.1.6–2.1.8: enderecos, telefones, emails (Texto), cada categoria em elemento próprio sob o schema. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Manter cadastro editorial de contatos no HTML existente; não criar XLSX mínimo para essa informação estável.
- **Compartilhamento:** 2.5, 11.2 e 13.1 somente quando houver confirmação de que unidade e canais são os mesmos.
- **Documentos integrais/vínculos:** Nenhum documento integral exigido.
- **Lacuna ou ambiguidade:** Não presumir que atendimento geral seja SIC ou Ouvidoria; não adicionar CPF, ramais ou contatos inexistentes.

#### 2.5 — Divulga o horário de atendimento?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A — complementar**. C, p. 28; S2, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Horário de atendimento, no sítio ou no Portal.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar os requisitos de conteúdo e vigência descritos.
- **S — marcação e estrutura:** INST; S2 2.1.9: horariosAtendimento (Texto). Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Manutenção editorial no HTML, compartilhando o cadastro de atendimento; sem XLSX próprio.
- **Compartilhamento:** 2.4; 11.2/13.1 apenas se a equivalência institucional for confirmada.
- **Documentos integrais/vínculos:** Nenhum documento integral exigido.
- **Lacuna ou ambiguidade:** Validar horário real; não criar periodicidade de revisão não prevista no critério.

#### 2.6 — Divulga os atos normativos próprios?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A/B**. C, pp. 28–29; S2, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Publicação dos atos expedidos diretamente pela Unidade, conforme sua competência; relação de ementas não substitui o acesso aos atos.
- **C — itens e controles:** disponibilidade, atualidade, série histórica e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Filtro mínimo: tipo de ato, ano e palavra-chave. Gravação de relatórios não integra os itens deste critério.
- **S — marcação e estrutura:** INST; S2 2.2.1–2.2.4: atoNormativo (Link), filtroPesquisa, dataUltimaAtualizacao (Data), historicoExercicio. Destino documentado: Institucional/AtosNormativos. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M01, aba atos: tipo, número/ano, data e descrição já disponíveis; vínculo ao arquivo publicado após conferência. Entrada futura XLSX/CSV/JSON; os quatro HTMLs são a entrada atual do conversor.
- **Compartilhamento:** 2.9 apenas se a mesma norma for pertinente a ambos; catálogo documental compartilhado, critérios distintos.
- **Documentos integrais/vínculos:** Texto integral de cada ato próprio publicado.
- **Lacuna ou ambiguidade:** Há 323 ementas e PDFs nas subpastas de dist, mas zero links PDF na consulta principal inspecionada. Mapear documento por registro, especialmente números repetidos; não gerar caminhos por suposição. A importação não demonstra completude/atualidade.

#### 2.7 — Divulga as perguntas e respostas mais frequentes relacionadas às atividades desenvolvidas pela Unidade?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A — complementar**. C, pp. 29–30; S2, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Seção com perguntas e respostas sobre atividades e serviços da Unidade; FAQ vazia ou apenas sobre transparência não atende.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar os requisitos de conteúdo e vigência descritos.
- **S — marcação e estrutura:** INST; S2 2.1.10: perguntasRespostasFrequentes (Texto); conteúdo ou redirecionamento documentado. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Manter pares pergunta/resposta no HTML editorial existente, sem exigir tabela ou modelo XLSX adicional.
- **Compartilhamento:** 13.3 e 14.3: referências a serviços, preservando suas finalidades.
- **Documentos integrais/vínculos:** Nenhum PDF integral obrigatório.
- **Lacuna ou ambiguidade:** As 17 respostas do protótipo contêm prazos, regras e links sujeitos a validação. Não gerar novas respostas ou categorias obrigatórias.

#### 2.8 — Participa em redes sociais e apresenta, no seu sítio institucional, link de acesso ao seu perfil?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A — complementar**. C, pp. 30–31; S2, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Links de acesso aos perfis institucionais na página principal do sítio; WhatsApp é um dos exemplos da Cartilha.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar os requisitos de conteúdo e vigência descritos.
- **S — marcação e estrutura:** INST; S2 2.1.11: redeSocial (Link), uma ocorrência por canal confirmado. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Manter lista editorial de canais já existente; não há necessidade de XLSX próprio.
- **Compartilhamento:** Cadastro institucional de canais, sem substituir os contatos de 2.4.
- **Documentos integrais/vínculos:** Nenhum documento integral exigido.
- **Lacuna ou ambiguidade:** WhatsApp e Instagram existem no código; não foram testados externamente neste levantamento. Não inventar outros perfis.

#### 2.9 — Publica, de forma clara e nominal, a legislação interna como: Lei de Criação/Autorização, Estatuto/Regimento, Lei de Estrutura Administrativa, Carta Anual (inc. I,II, III, IV, VII e VIII art. 8º da Lei 13.303/2016 para empresas públicas e sociedades de economia mista)?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **B**. C, p. 31; S2, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Normas identificadas por tipo, número e ano, com inteiro teor. Para previdências: lei de criação/autorização, estatuto e regimento interno conforme legislação própria.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar os requisitos de conteúdo e vigência descritos.
- **S — marcação e estrutura:** INST; S2 2.3.1 (item técnico ligado a C 2.9): legislacao (Link/Anexo). Destino Institucional/LegislacaoInterna. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M01, aba legislação institucional: índice de documentos, não tabela de artigos da lei. Entrada XLSX/CSV para metadados e arquivos oficiais separados.
- **Compartilhamento:** 2.1/2.2 e 11.5 quando a mesma norma for pertinente, sem misturar os acervos públicos.
- **Documentos integrais/vínculos:** Lei de criação/autorização, estatuto e regimento, conforme existência jurídica; norma de estrutura disponível não substitui o conjunto.
- **Lacuna ou ambiguidade:** Matriz II em S2 não exclui a aplicabilidade expressa. Instrumento juridicamente inexistente requer fundamentação na seção, não declaração fictícia; vigência e completude ainda pendentes.


### Dimensão 3 — Receitas

#### 3.1 — Divulga as receitas da Unidade, evidenciando sua previsão e realização?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A**. C, pp. 32–35; S3, pp. 1–2, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Receita/duodécimos previstos e realizados, inclusive recursos extraordinários, em uma única página/arquivo para comparação.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação de conjunto selecionado em pelo menos um formato editável (E). Filtro mínimo: período (mês e ano).
- **S — marcação e estrutura:** REC; S3 itens 3.1–3.6: valorPrevistoReceita e valorArrecadadoReceita (Monetário), F/G/A/H. Exemplo usa tabela com as duas medidas por registro. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M02 receitas: ano, mês, valor previsto e valor arrecadado; XLSX/CSV/JSON, preservando a comparabilidade.
- **Compartilhamento:** 10.6 e dados abertos 14.4; manter a mesma origem contábil, sem confundir repasses legais com convênios.
- **Documentos integrais/vínculos:** Nenhum inteiro teor adicional exigido; LOA/RGF não substituem esses dados na mesma tela.
- **Lacuna ou ambiguidade:** Atualmente há 12 registros fictícios e exportações de teste. Repasses em datas fixas têm particularidade expressa na C p. 33; 30 dias PETP não dispensam regras contábeis de tempo real. As exportações atuais são estáticas e não refletem o filtro ativo.


### Dimensão 4 — Despesas

#### 4.1 — Divulga o total das despesas empenhadas, liquidadas e pagas?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A**. C, pp. 36–37; S4, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Totais empenhado, liquidado e pago no período, consolidados ou calculáveis pelo detalhamento, em uma única página/arquivo.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação de conjunto selecionado em pelo menos um formato editável (E). Filtro mínimo: exercício (ano), mês ou período.
- **S — marcação e estrutura:** DESP; S4 4.1.1–4.1.3: valorEmpenhado, valorLiquidado, valorPago (Monetário); controles 4.1.15–4.1.18 F/G/A/H, compartilhados com 4.2/4.3. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M03 despesas: registros de empenhos e movimentos contábeis para gerar os três totais sem duplicação; XLSX/CSV/JSON.
- **Compartilhamento:** 4.2, 4.3, pagamentos de 9.4 e balancetes 10.6; integrações por referências efetivas, não por semelhança de valor.
- **Documentos integrais/vínculos:** Não há documento integral específico adicional nesse critério.
- **Lacuna ou ambiguidade:** Definir a granularidade da origem contábil: somar saldos cumulativos de várias datas duplicaria despesas. Não atribuir o mesmo valor a empenho, liquidação e pagamento.

#### 4.2 — Divulga as despesas por classificação orçamentária?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A**. C, pp. 38–40; S4, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Unidade orçamentária, função, subfunção, natureza da despesa (categoria econômica, grupo e elemento) e fonte dos recursos; códigos e descrições por extenso. Detalhamento e exportação devem conservar todos esses elementos.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação de conjunto selecionado em pelo menos um formato editável (E). Filtro mínimo: exercício (ano), mês ou período e elemento de despesa.
- **S — marcação e estrutura:** DESP; S4 4.1.4–4.1.10: unidadeDespesa, funcaoDespesa, subFuncaoDespesa, categoriaDespesa, grupoDespesa, elementoDespesa, fonteRecursosDespesa; F/G/A/H. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M03: classificação nos registros correspondentes aos empenhos, com códigos e descrições da origem; sem planilha independente de totais divergentes.
- **Compartilhamento:** 4.1 e 4.3; fonte também é necessária à ordenação de 9.4.
- **Documentos integrais/vínculos:** Nenhum inteiro teor adicional exigido.
- **Lacuna ou ambiguidade:** Não criar classificação fictícia. Campo técnico numérico do Serigy não afasta a exigência C de código e descrição acessíveis.

#### 4.3 — Possibilita a consulta de empenhos com os detalhes do beneficiário do pagamento ou credor, o valor, o bem fornecido ou serviço prestado e a identificação do procedimento licitatório originário da despesa?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A**. C, pp. 40–41; S4, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Lista e detalhe individual de empenhos: credor, valor, objeto/bem/serviço, modalidade e número do procedimento (ou contratação direta/fundamentação pertinente). Vinculação ao procedimento para despesas licitáveis.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação de conjunto selecionado em pelo menos um formato editável (E). Filtro mínimo: número do empenho, nome e CPF ou CNPJ do credor, mês e exercício (ano).
- **S — marcação e estrutura:** DESP; S4 4.1.11–4.1.14 e 4.1.19: credorEmpenho, objetoEmpenho, modalidadeEmpenho, numeroProcedimento, valorEmpenhoIndividual; F/G/A/H. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M03: aba empenhos vinculada aos movimentos; manter identificador do empenho e procedimento real, credor, documento de identificação exigido para consulta e descrição.
- **Compartilhamento:** 4.1/4.2; 8.1/8.4 e 9.1 quando a despesa se originar desses processos.
- **Documentos integrais/vínculos:** Não há obrigação autônoma de anexar toda a nota fiscal no texto deste critério; identificar o procedimento na consulta da despesa.
- **Lacuna ou ambiguidade:** O número do empenho e o CPF/CNPJ são necessários ao filtro C, mas não têm item específico na tabela S4. Não inventar serigyItem para eles nem tornar a consulta exclusivamente individual.


### Dimensão 5 — Convênios e Transferências

#### 5.1 — Divulga as transferências recebidas a partir da celebração de convênios/acordos com indicação, no mínimo, do número/ano do convênio/termo ou ajuste, do valor total previsto dos recursos envolvidos, do valor recebido, do objeto, da vigência, da origem (órgão repassador/concedente) e o inteiro teor do instrumento de convênio/transferência?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A/B**. C, pp. 42–43; S5, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Órgão repassador, número/ano do instrumento, objeto, valor total previsto, valor recebido/já repassado, vigência e inteiro teor; resumo acessível sem abrir o documento.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação de conjunto selecionado em pelo menos um formato editável (E). Filtro mínimo: exercício (ano).
- **S — marcação e estrutura:** CONV; S5 5.1.1–5.1.11: identificaTransferencia, orgaoRepassador, vigenciaConvenio, objetoConvenio, valorTotalPrevisto, valorRepassado, anexoConvenio; F/G/A/H. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M05 convênios, aba recebidas, e M01 para arquivos. XLSX/CSV; repasses detalhados podem ser aba auxiliar para evitar contagem repetida do valor total.
- **Compartilhamento:** 5.2/5.3 compartilham estrutura documental, mas consultas de recebidas e realizadas devem permanecer separadas.
- **Documentos integrais/vínculos:** Inteiro teor do convênio/termo/ajuste.
- **Lacuna ou ambiguidade:** Não incluir transferências legais/constitucionais como se fossem voluntárias. S tipa vigenciaConvenio como Ano, mas exemplifica data: DÚVIDA — REVISÃO NECESSÁRIA; preservar o período real da fonte.

#### 5.2 — Divulga as transferências realizadas a partir da celebração de convênios/acordos/ajustes, com indicação, no mínimo, do número/ano do convênio/termo ou ajuste, do beneficiário, do objeto, da vigência, do valor total previsto para repasse, do valor concedido e inteiro teor do instrumento de convênio/termo ou ajuste?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A/B**. C, pp. 44–45; S5, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Beneficiário, número/ano do instrumento, objeto, vigência, valor total previsto e valores já repassados, com inteiro teor. Abrange repasses voluntários não contratuais.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação de conjunto selecionado em pelo menos um formato editável (E). Filtro mínimo: exercício (ano).
- **S — marcação e estrutura:** CONV; S5 5.2.1–5.2.11: identificaTransferencia, orgaoBeneficiario, vigenciaConvenio, objetoConvenio, valorTotalRepasse, valorRepassado, anexoConvenio; F/G/A/H. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M05, aba realizadas, e M01 para instrumentos; consultas autônomas das recebidas.
- **Compartilhamento:** 5.1/5.3: catálogo e participantes; dados de repasses podem ter vínculo com execução financeira sem misturar naturezas.
- **Documentos integrais/vínculos:** Inteiro teor do convênio/termo/ajuste.
- **Lacuna ou ambiguidade:** Não confundir contrato de fornecimento com repasse voluntário. Mesma ambiguidade técnica da vigência de 5.1; não supor que não existam transferências em previdência.

#### 5.3 — Divulga os acordos firmados que não envolvam transferência de recursos financeiros, identificando as partes, o número/ano do convênio/termo ou ajuste, o objeto, a vigência, as obrigações ajustadas e o inteiro teor do instrumento de convênio/termo ou ajuste?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A/B**. C, pp. 46–47; S5, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Partes, número/ano, objeto, vigência, obrigações ajustadas e inteiro teor dos acordos sem transferência financeira. Obrigações constam do título oficial mesmo não repetidas na lista do corpo.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação de conjunto selecionado em pelo menos um formato editável (E). Filtro mínimo: exercício (ano).
- **S — marcação e estrutura:** CONV; S5 5.3.1–5.3.10: identificaAcordo, participante, vigenciaConvenio, objetoConvenio, obrigacoes, anexoConvenio; F/G/A/H. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M05, aba sem_recursos; participantes e obrigações conforme a fonte. M01 para arquivos oficiais.
- **Compartilhamento:** Mesma estrutura de instrumentos de 5.1/5.2; sem campos financeiros fictícios nessa aba.
- **Documentos integrais/vínculos:** Inteiro teor do acordo/termo de cooperação ou equivalente.
- **Lacuna ou ambiguidade:** Não preencher valor zero para simular dados inexistentes. Vigência tem o mesmo conflito Ano/data. Não ocorrência deve cobrir e identificar os anos anteriores, quando verdadeira.


### Dimensão 6 — Recursos Humanos e concursos

#### 6.1 — Divulga a relação nominal dos servidores/autoridades/membros, seus cargos/funções, as respectivas lotações, as suas datas de admissão/exoneração/inativação e a carga horária do cargo/função ocupada/desempenhada?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A**. C, pp. 48–49; S6, pp. 1–4, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Nome completo, cargo/função, lotação, admissão, exoneração/inativação quando aplicável e carga horária. A C exige tabela estruturada em HTML; detalhe e exportação devem conter o mínimo completo.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação do conjunto selecionado em pelo menos um formato editável (E). Filtro mínimo: nome e cargo/função.
- **S — marcação e estrutura:** RH; S6 6.1.1–6.1.2, 6.1.4–6.1.11: nomeServidor, cargoServidor, lotacaoServidor, admissaoServidor, exoneracaoServidor, cargaHoraria; A/H/G/F. Resultado por vínculo, com detalhe associado se houver. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M04 pessoal, aba vínculos, XLSX/CSV/JSON; preservar movimentos reais ao longo do histórico, sem criar dados de exoneração de quem continua ativo.
- **Compartilhamento:** 6.2 compartilha identidade, cargo e período do vínculo; 6.3 é outro conjunto (faixas do cargo).
- **Documentos integrais/vínculos:** Nenhum documento integral adicional é exigido neste critério.
- **Lacuna ou ambiguidade:** Não presumir que inativos/beneficiários do RPPS sejam servidores da autarquia. Delimitar o universo funcional da Unidade, sem expor o cadastro de segurados.

#### 6.2 — Divulga a remuneração nominal de cada servidor/autoridade/Membro?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A**. C, pp. 50–51; S6, pp. 1–4, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Nome completo, cargo e remuneração nominal em relação aberta, sem exigir conhecimento prévio de CPF/nome completo/cargo/lotação, cadastro ou autenticação. Tabela é exigida; HTML é preferencial.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação do conjunto selecionado em pelo menos um formato editável (E). Filtro mínimo: nome, mês e ano.
- **S — marcação e estrutura:** RH; S6 6.1.1–6.1.3 e 6.1.8–6.1.11: nomeServidor, cargoServidor, salarioServidor (Monetário); A/H/G/F. Associar salário à pessoa e competência. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M04, aba folha: nome, cargo, remuneração e competência para filtro/histórico. Relação vinculada aos vínculos, sem exigir novas rubricas não previstas.
- **Compartilhamento:** 6.1: cadastro; 6.3: referência remuneratória, sem confundir tabela de cargos com pagamento nominal.
- **Documentos integrais/vínculos:** Nenhum PDF integral obrigatório.
- **Lacuna ou ambiguidade:** A Cartilha não fixa colunas de vencimento básico, descontos, líquido ou rubricas neste critério; não criá-las como mínimo normativo. Fonte real e delimitação de vínculos pendentes.

#### 6.3 — Divulga a tabela com o padrão remuneratório dos cargos e funções?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A/B**. C, pp. 51–53; S6, pp. 1–4, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Tabela com todas as faixas salariais dos cargos/funções previstos na estrutura, podendo ser extraída da legislação remuneratória atualizada.
- **C — itens e controles:** disponibilidade e atualidade. Atualidade: referência de até um ano; se não revisada nesse intervalo, informar expressamente que é a tabela vigente no exercício atual. Não exige H/F/G autônomos.
- **S — marcação e estrutura:** RH; S6 6.2.1–6.2.4: cargo (Texto), salario (Monetário), descricao (níveis/classes/padrões, Texto), A. Exemplo de tabela, sem controles H/F/G. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M04, aba padrões: cargo/função, nível/classe/padrão aplicável e valor conforme norma; vigência como referência real. M01 para legislação de suporte.
- **Compartilhamento:** 6.1/6.2 por cargo, mantendo separados valor de referência e remuneração paga.
- **Documentos integrais/vínculos:** Norma/tabela remuneratória se utilizada para apresentar o padrão; não basta link genérico sem a tabela localizável.
- **Lacuna ou ambiguidade:** Não inventar níveis/classes para cargos que não os possuam. Declaração de vigência exige confirmação, não mera alteração da data do site.

#### 6.4 — Divulga a lista de seus estagiários, contendo o nome dos estudantes; a data de contratação e a data de término do respectivo contrato?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A**. C, pp. 53–54; S6, pp. 1–4, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Nome completo do estudante, data de contratação e data de término do contrato.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: até 180 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação E ou PDF pesquisável expressamente aceito. Filtro mínimo: ano de contratação.
- **S — marcação e estrutura:** RH; S6 6.3.1–6.3.7: nomeEstagiario, admissaoEstagiario, terminoEstagiario; A/H/G/F. Exemplo de tabela com os três campos do estudante. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M04, aba estagiários, compatível com colunas atuais nome_completo/data_contratacao/data_termino; ano de contratação derivado da data. XLSX/CSV/JSON.
- **Compartilhamento:** Cadastro documental M01 só se necessário; não confundir estagiário com vínculo efetivo.
- **Documentos integrais/vínculos:** Não é exigido anexar o contrato individual de estágio.
- **Lacuna ou ambiguidade:** O protótipo tem oito registros fictícios, não acervo real. Não ocorrência deve identificar exercícios e atualização; ausência não autoriza inventar data de término. As exportações atuais também são estáticas, sem recorte automático do filtro.

#### 6.5 — Publica lista dos terceirizados que prestam serviços para a Unidade/entidades, contendo, em relação a cada um deles: nome completo, função ou atividade exercida e nome da empresa empregadora?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A**. C, pp. 55–56; S6, pp. 1–4, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Nome completo do terceirizado, função/atividade e nome/razão social da empregadora. Relação pode ser lista em PDF ou XLS, conforme a C.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: até 180 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação E ou PDF pesquisável. Filtro mínimo: ano.
- **S — marcação e estrutura:** RH; S6 6.4.1–6.4.7: nomeTerceirizado, funcaoTerceirizado, empresaTerceirizado (Texto); A/H/G/F. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M04, aba terceirizados: os três campos da relação e referência anual para o histórico; XLSX/CSV.
- **Compartilhamento:** 9.1: empresa e contrato somente se a vinculação efetiva for fornecida; não tornar número de contrato nova coluna mínima C 6.5.
- **Documentos integrais/vínculos:** Nenhum documento integral autônomo exigido; lista deve ser acessível.
- **Lacuna ou ambiguidade:** Ano de referência é necessário à consulta, mas não implica exigir CPF, salário do empregado, admissão ou dados pessoais extras.

#### 6.6 — Divulga a íntegra dos editais de concursos e seleções públicas realizados pela Unidade para provimento de cargos e empregos públicos?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **B**. C, pp. 56–58; S6, pp. 1–4, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Íntegra dos editais de concursos/seleções públicos realizados pela Unidade para provimento de cargos e empregos.
- **C — itens e controles:** disponibilidade, atualidade, série histórica e filtro de pesquisa. Atualidade: até um ano. Histórico: H3; a C ainda exemplifica X-1/X-2/X-3 quando o dado mais recente é do ano anterior. Filtro genérico, admitindo documentos identificáveis e acessíveis mesmo não pesquisáveis. Sem G.
- **S — marcação e estrutura:** RH; S6 6.5.1 editalConcurso (Link); 6.5.4–6.5.6 A/H/F. Caminho RecursosHumanos/Concurso. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M09 concursos, aba certames, e M01 para editais; índice documental por certame/exercício, não transcrição das cláusulas.
- **Compartilhamento:** 6.7 usa o mesmo certame, com documentos/resultados próprios.
- **Documentos integrais/vínculos:** Editais integrais de concursos e processos seletivos.
- **Lacuna ou ambiguidade:** A formulação do histórico usa duas referências de X; registrar a série sem reduzir cobertura por interpretação automática. Não ocorrência só se institucionalmente confirmada.

#### 6.7 — Divulga informações sobre os demais atos dos concursos públicos e processos seletivos da Unidade, contendo no mínimo a lista de aprovados com as classificações e as nomeações?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A/B**. C, pp. 58–60; S6, pp. 1–4, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Lista de aprovados com classificações e nomeações; acesso pode ser por planilha ou link direto ao executor do certame.
- **C — itens e controles:** disponibilidade, atualidade e filtro de pesquisa. Atualidade: até 30 dias quando houver concurso/processo seletivo em andamento. Filtro genérico com a mesma ressalva de identificação/acesso documental. Não lista H ou G.
- **S — marcação e estrutura:** RH; S6 6.5.2 aprovadosConcurso (Link/Numérico), 6.5.3 nomeadosConcurso (Link/Texto), 6.5.4 A e 6.5.6 F. Parear resultados e nomeações ao certame. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M09, abas aprovados e nomeações, ou índice M01 de listas oficiais quando suficientes; não impor planilha nominal se os documentos atendem.
- **Compartilhamento:** 6.6: referência única do concurso/processo seletivo.
- **Documentos integrais/vínculos:** Listas de aprovados/classificações e atos/listas de nomeações quando a apresentação for documental.
- **Lacuna ou ambiguidade:** Não transferir a série histórica de 6.6 para 6.7 como obrigação autônoma. Não inferir que todo aprovado foi nomeado; não divulgar inscrições/documentos pessoais não exigidos.


### Dimensão 7 — Diárias

#### 7.1 — Divulga o nome e o cargo/função do beneficiário, além do valor total recebido, número de diárias usufruídas por afastamento, período de afastamento, motivo do afastamento e local de destino?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A**. C, pp. 61–62; S7, pp. 1–2, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Nome e cargo/função do beneficiário, número de diárias, total recebido, datas de início/fim do afastamento, motivo e destino com nome da cidade. Seção própria; exportação deve incluir inclusive campos do detalhe.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação do conjunto selecionado em pelo menos um formato editável (E). Filtro mínimo: nome, mês e ano.
- **S — marcação e estrutura:** DIA; S7 7.1.1–7.1.12: nomeBeneficiario, cargoBeneficiario, numeroDiaria, dataInicioAfastamento, dataFimAfastamento, motivoAfastamento, localDestino, valorTotal; A/H/F/G. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M06 diárias, aba concessões: um afastamento/concessão por registro, preservando quantidade e total; XLSX/CSV/JSON.
- **Compartilhamento:** 6.1 para beneficiário/cargo quando houver vínculo confirmado; 4.3 para execução, sem substituir a seção de diárias.
- **Documentos integrais/vínculos:** Não é exigido anexar autorização ou comprovantes como mínimo deste critério.
- **Lacuna ou ambiguidade:** Não calcular total por multiplicação de uma tabela de referência se a fonte não confirmar o valor recebido. Definir a referência de mês da consulta sem inventar datas.

#### 7.2 — Divulga tabela ou relação que explicite os valores das diárias dentro do Estado, fora do Estado e fora do país, conforme legislação local?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A/B**. C, pp. 62–63; S7, pp. 1–2, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Valores dentro do Estado, fora do Estado e fora do país, segundo norma local. Tabela/relação da própria norma é aceita, na seção específica; informar expressamente eventual ausência legal de diárias internacionais.
- **C — itens e controles:** disponibilidade, atualidade, série histórica e filtro de pesquisa. Atualidade: até um ano ou indicação explícita de que a tabela mais antiga segue vigente. Histórico de pelo menos três anos anteriores à consulta (H3). Filtro genérico, sem parâmetros mínimos enumerados; sem G.
- **S — marcação e estrutura:** DIA; S7 7.2.1–7.2.6: valorEstadual, valorNacional, valorInternacional (Monetário); A/H/F. Exemplo de tabela dos valores, não de pagamentos. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M06, aba valores, apenas faixas/destinos efetivamente previstos na legislação; M01 para versões da norma/tabela.
- **Compartilhamento:** 7.1 pode consultar a referência, mas pagamento efetivo e valor de tabela são fatos distintos.
- **Documentos integrais/vínculos:** Norma ou tabela integrante dela, quando usada para apresentar os valores.
- **Lacuna ou ambiguidade:** Não preencher internacional com zero como se existisse previsão legal. Documentar validade das versões para a série histórica.


### Dimensão 8 — Licitações, planejamento de contratações e sanções

#### 8.1 — Divulga a relação das licitações em ordem sequencial, informando o número e modalidade licitatória, o objeto, a data, o valor estimado/homologado e a situação?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A**. C, pp. 64–65; S8, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Tabela estruturada em HTML de licitações em andamento e encerradas, em ordem numérica sequencial: número/modalidade, objeto, abertura, valor estimado/homologado e situação. Inclui dispensas e inexigibilidades, excetuadas compras diretas de pequeno valor.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação do conjunto selecionado em pelo menos um formato editável (E). Filtro mínimo: ano, mês, situação do certame e modalidade licitatória.
- **S — marcação e estrutura:** LIC; S8 8.1.1–8.1.6: modalidadeLicitacao, objetoLicitacao, dataLicitacao, valorLicitacao, faseLicitacao, sequencia; 8.1.11–8.1.14 F/G/A/H. Detalhes vinculados ao certame. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M07 licitações: dados mínimos por procedimento, preservando número e ano reais; abas/modalidades sem atos fictícios.
- **Compartilhamento:** 8.2–8.5: documentos do mesmo procedimento; 4.3 e 9.1: referências efetivas.
- **Documentos integrais/vínculos:** 8.1 é a relação; os integrais são tratados em 8.2–8.5, não substituídos pelo resumo.
- **Lacuna ou ambiguidade:** A tabela S8 não traz item próprio para número do certame; sequencia é exemplificada como ordinal. Não inventar numeroLicitacao nem dispensar o número exigido pela C.

#### 8.2 — Divulga a íntegra dos editais de licitação?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **B**. C, pp. 66–67; S8, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Editais completos dos certames em andamento e encerrados, acessíveis na seção de licitações.
- **C — itens e controles:** disponibilidade, atualidade, série histórica e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Filtro genérico, sem campos mínimos enumerados. Sem G.
- **S — marcação e estrutura:** LIC; S8 8.1.7 editalLicitacao (Anexo); 8.1.11 F, 8.1.13 A e 8.1.14 H. Itens de documento associados ao procedimento. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M01, vínculos ao certame de M07; índice e arquivos, sem modelo independente de editais.
- **Compartilhamento:** 8.1, 8.3 e catálogo documental.
- **Documentos integrais/vínculos:** Edital integral e seus anexos quando integrantes.
- **Lacuna ou ambiguidade:** Não substituir anexo por link à página inicial do PNCP ou de outro portal; o destino deve levar à informação do procedimento.

#### 8.3 — Divulga a íntegra dos demais documentos das fases interna e externa das licitações?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **B**. C, pp. 67–68; S8, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** TR/projeto básico/equivalente; justificativa; pareceres; orçamento/formação do preço; edital/anexos; atas de abertura/julgamento e outras; impugnações/recursos e análises quando houver; adjudicação e homologação.
- **C — itens e controles:** disponibilidade, atualidade, série histórica e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Filtro genérico. Documentos devem permitir pesquisa e seleção de texto, como DOC/DOCX ou PDF pesquisável; a regra do filtro admite a ressalva de documentos de terceiros identificáveis, sem eliminar a exigência de conteúdo. Sem G.
- **S — marcação e estrutura:** LIC; S8 8.1.8 docFasesLicitacao (Anexo); F/A/H compartilhados 8.1.11/13/14. Coleção de documentos em detalhe do certame. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M01, vários documentos por procedimento de M07, com identificação de fase/tipo já existentes na fonte.
- **Compartilhamento:** 8.1/8.2; reutilizar o mesmo edital, sem duplicar o arquivo.
- **Documentos integrais/vínculos:** Todos os documentos enumerados no mínimo C, condicionais conforme ocorrência.
- **Lacuna ou ambiguidade:** Não transformar a exceção de filtro textual em autorização geral para publicar digitalizações ilegíveis; não inventar parecer/ata ou declarar etapa inexistente sem confirmação.

#### 8.4 — Divulga a íntegra dos principais documentos dos processos de dispensa e inexigibilidade de licitação?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **B**. C, pp. 69–70; S8, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** TR/projeto básico/equivalente; justificativa de fornecedor/preço; caracterização de emergência/calamidade/risco quando for o caso; pareceres quando couber; homologação/ratificação da autoridade. A C ressalva dispensas de pequeno valor.
- **C — itens e controles:** disponibilidade, atualidade, série histórica e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Filtro genérico, com ressalva de identificação/acesso documental; documentos com pesquisa e seleção de texto/valor. Sem G.
- **S — marcação e estrutura:** LIC; S8 8.1.9 docDispensaLicitacao (Anexo); F/A/H de 8.1.11/13/14. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M01 ligado às contratações diretas de M07, preservando o regime e a identificação real do procedimento.
- **Compartilhamento:** 8.1, 4.3 e contratos decorrentes de 9.1.
- **Documentos integrais/vínculos:** Principais documentos de dispensa/inexigibilidade especificados na C; admite links externos diretos.
- **Lacuna ou ambiguidade:** Aplicar a ressalva de pequeno valor apenas aos fatos/regime pertinentes, não a toda contratação direta nem a todos os demais critérios.

#### 8.5 — Divulga a íntegra das Atas de Adesão – SRP?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **B**. C, p. 71; S8, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Íntegras das atas de adesão de registro de preços, em licitações e/ou contratos.
- **C — itens e controles:** disponibilidade, atualidade, série histórica e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Filtro genérico, sem campos mínimos enumerados; sem G.
- **S — marcação e estrutura:** LIC; S8 8.1.10 atasLicitacao (Anexo/Link), F/A/H compartilhados 8.1.11/13/14. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M01, documentos associados ao procedimento/contrato efetivo, sem planilha autônoma apenas para copiar o texto das atas.
- **Compartilhamento:** M07/8.1 e M08/9.1 se houver contratação decorrente.
- **Documentos integrais/vínculos:** Atas de adesão – SRP integrais.
- **Lacuna ou ambiguidade:** Não presumir que a simples ata geral de registro de preços comprove a adesão da Unidade. Associação documental exige conferência.

#### 8.6 — Divulga o plano de contratações anual?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **B**. C, pp. 71–72; S8, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Plano de Contratações Anual acessível na seção de licitações e/ou contratos. Declaração de não elaboração/inexistência não atende.
- **C — itens e controles:** disponibilidade e atualidade. Atualidade: PCA do exercício atual. Não lista H/F/G.
- **S — marcação e estrutura:** LIC; S8 8.2.1 contratacoesAnual (Anexo/Link), 8.2.2 A. Caminho Licitacoes/PlanoAnualContratacoes. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M01, categoria PCA por exercício; manter plano oficial em arquivo. Não criar planilha de itens do PCA sem fonte e escopo próprios.
- **Compartilhamento:** M07 utiliza o documento; 10.5 é plano estratégico distinto.
- **Documentos integrais/vínculos:** PCA do exercício atual.
- **Lacuna ou ambiguidade:** Não aplicar a regra geral de não ocorrência para declarar este critério atendido. Não inventar linhas de contratação ou metas do plano.

#### 8.7 — Divulga a relação dos licitantes e/ou contratados sancionados administrativamente pela Unidade?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A**. C, pp. 73–74; S8, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Nomes dos licitantes/contratados sancionados pela Unidade nas hipóteses dos incisos III e IV do art. 156 indicadas na C. Aplica-se expressamente às previdências.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação E ou PDF pesquisável expressamente aceito. Filtro genérico, sem parâmetros mínimos enumerados.
- **S — marcação e estrutura:** LIC; S8 8.3.1 nomeSancionado (Texto), 8.3.2 idSancionado (CNPJ/CPF, Texto), 8.3.3–8.3.6 F/G/A/H. Caminho Licitacoes/Sancoes. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M07, aba sanções: nomes e identificação requerida tecnicamente, com referência real para atualização/histórico. Não exigir novas colunas de dosimetria.
- **Compartilhamento:** Licitações/contratos apenas quando a relação efetiva estiver documentada; catálogo de não ocorrências comum.
- **Documentos integrais/vínculos:** A C não exige aqui o inteiro teor do ato sancionatório como campo mínimo; eventual vínculo é complementar.
- **Lacuna ou ambiguidade:** C mínimo nominal versus S com CNPJ/CPF: distinguir exigência técnica adicional e confirmar a forma de identificação/publicação. Não importar sanções de outras unidades como se fossem da autarquia.


### Dimensão 9 — Contratos, fiscais e ordem cronológica

#### 9.1 — Divulga a relação dos contratos celebrados em ordem sequencial, com o seu respectivo resumo, contendo, no mínimo, indicação do contratado(a), do valor, do objeto e da vigência, bem como dos aditivos deles decorrentes?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A/B**. C, p. 75; S9, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Contratos em ordem sequencial, com contratado, valor, objeto, vigência e aditivos quando houver, em seção própria.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação do conjunto selecionado em pelo menos um formato editável (E). Filtro mínimo: período.
- **S — marcação e estrutura:** CONT; S9 9.1.1–9.1.8: numeroContrato, contratado, valorContrato, objeto, inicioContrato, fimContrato, sequencia, termoAditivo; 9.1.10–9.1.13 F/G/A/H. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M08 contratos, abas contratos e aditivos; registros separados para relações um-para-muitos, mantendo resumo consultável.
- **Compartilhamento:** 9.2–9.4; 8.1/8.4 e 4.3 por referências documentadas.
- **Documentos integrais/vínculos:** Aditivos decorrentes vinculados; íntegra do contrato é obrigação de 9.2.
- **Lacuna ou ambiguidade:** Não somar o valor integral do contrato novamente para cada aditivo; distinguir valor original e efeitos reais conforme a fonte.

#### 9.2 — Divulga o inteiro teor dos contratos e dos respectivos termos aditivos?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **B**. C, pp. 76–77; S9, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Íntegras de contratos e respectivos aditivos, quando houver.
- **C — itens e controles:** disponibilidade, atualidade, série histórica e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Filtro genérico, sem mínimo específico; sem G.
- **S — marcação e estrutura:** CONT; S9 9.1.8 termoAditivo e 9.1.9 linkContrato (Link/Arquivo); F/A/H de 9.1.10/12/13. Detalhe documental ligado ao contrato. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M01 vinculado às abas contratos/aditivos de M08; sem cópias de arquivos para cada consulta.
- **Compartilhamento:** 9.1 e 9.3: mesmo identificador efetivo do contrato.
- **Documentos integrais/vínculos:** Contrato e todos os aditivos correspondentes.
- **Lacuna ou ambiguidade:** A relação resumida não substitui o inteiro teor. Não transformar ausência de anexo em declaração de que não houve aditivo.

#### 9.3 — Divulga a relação/lista dos fiscais de cada contrato vigente e encerrado?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A**. C, pp. 77–78; S9, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Relação nominal dos fiscais e contratos pelos quais respondem, incluindo contratos vigentes e encerrados. Não basta informação apenas no detalhe de cada contrato.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação E ou PDF pesquisável. Filtro genérico.
- **S — marcação e estrutura:** CONT; S9 9.2.1 fiscalGestor (Texto), 9.2.2 contratoFiscal (N/A), 9.2.3–9.2.6 F/G/A/H. Caminho Contratos/GestoresFiscais. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M08, aba fiscais: uma associação fiscal–contrato por registro, sem criar outro cadastro financeiro.
- **Compartilhamento:** 9.1/9.2; nomes funcionais podem ser referenciados em M04 se confirmados.
- **Documentos integrais/vínculos:** Portaria de designação não integra o mínimo expresso; se publicada, compartilhar M01/2.6.
- **Lacuna ou ambiguidade:** O Serigy diz fiscal/gestor; C exige fiscais. Não substituir fiscais por gestores nem presumir que sejam a mesma pessoa.

#### 9.4 — Divulga a ordem cronológica de seus pagamentos, bem como as justificativas que fundamentaram a eventual alteração dessa ordem?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A/B**. C, pp. 78–80; S9, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Lista dos créditos em ordem cronológica, por fonte e categorias contratuais (bens, locações, serviços, obras), com justificativas de eventuais alterações. C exemplifica vencimento, pagamento, credor e valor como identificação do crédito.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Publicação mensal e atualidade até 30 dias. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação do conjunto selecionado em pelo menos um formato editável (E). Filtro genérico. A exceção nominal ao Banese não se estende à Previdência Estadual.
- **S — marcação e estrutura:** CONT; S9 9.3.1–9.3.4: dataVencimento, dataPagamento, credor, valorPagamento; 9.3.5–9.3.8 F/G/A/H. Caminho Contratos/OrdemCronologica. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M08, aba ordem_pagamentos, usando pagamentos de M03 com fonte, categoria e justificativa real quando houver alteração. Não produzir a ordem apenas ordenando datas de pagamento.
- **Compartilhamento:** 4.1/4.3: valores/credores; 9.1: contrato; mesma transação financeira, com visão específica.
- **Documentos integrais/vínculos:** Justificativas integrais das alterações quando documentais; também podem ser apresentadas de forma explícita na seção.
- **Lacuna ou ambiguidade:** Fonte, categoria e justificativa são previstas em C, mas não têm propriedade específica na tabela S9. Não criar serigyItem para elas. Vencimento depende da regulamentação/fato, não é uma data dedutível arbitrariamente do nome do arquivo.


### Dimensão 10 — Planejamento e Prestação de Contas

#### 10.1 — Publica a Prestação de Contas do Ano Anterior (Balanço Geral)?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **B**. C, pp. 81–82; S10, pp. 1–2, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Balanço Geral: no mínimo balanços Orçamentário, Financeiro, Patrimonial e Demonstrações das Variações Patrimoniais. Se PDF, pesquisável.
- **C — itens e controles:** disponibilidade, atualidade, série histórica e filtro de pesquisa. Atualidade: último exercício exigível; prazo específico deve ser confirmado, e a menção geral a abril não fixa prazo local. Histórico especial: documento do exercício X e série X-1/X-2/X-3 descrita em C, não reduzir a H3 automaticamente. Filtro genérico; sem G.
- **S — marcação e estrutura:** PC; S10 10.1.1–10.1.4: balancoGeralAnoAnterior (Link), F/A/H. Coleção de links por exercício. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M01, documentos de prestação de contas classificados por exercício e demonstrativo; não exigir nova digitação de todas as contas em XLSX.
- **Compartilhamento:** 10.2/10.3 relacionam-se ao mesmo exercício, sem substituir os documentos; 3.1/4.1/10.6 podem compartilhar origem contábil.
- **Documentos integrais/vínculos:** Conjunto integral dos quatro demonstrativos mínimos da prestação de contas.
- **Lacuna ou ambiguidade:** A série descrita em C usa X e três exercícios precedentes: preservar a cobertura e registrar a referência validada. S10 diverge no schema de exemplos de filtro/atualização; ver ambiguidades gerais.

#### 10.2 — Divulga o Relatório de Gestão ou Atividades?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **B/C**. C, pp. 82–84; S10, pp. 1–2, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Relatório de gestão/atividades da Unidade relativo ao exercício anterior, com resultados finalísticos e/ou de gestão. Documento pesquisável, mesmo em formato não editável. Os tópicos que a C diz abordar em geral não são novas colunas obrigatórias.
- **C — itens e controles:** disponibilidade, atualidade, série histórica e filtro de pesquisa. Atualidade: último exercício encerrado. Histórico especial: X mais X-1/X-2/X-3 segundo a formulação C. Filtro genérico; sem G.
- **S — marcação e estrutura:** PC; S10 10.2.1–10.2.4: relatorioGestao (Anexo), F/A/H; exemplos usam links por exercício. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M01: índice anual e arquivo do relatório. Dados de resultados tabulares somente se já existentes em fonte validada, sem decomposição obrigatória do relatório.
- **Compartilhamento:** 10.1/10.3 por exercício; 10.5 planejamento e 14.5 avaliação de serviços podem ser referências, sem fundir os produtos.
- **Documentos integrais/vínculos:** Relatório de gestão ou atividades integral, pesquisável.
- **Lacuna ou ambiguidade:** Não substituir por planilha financeira ou por resumo criado automaticamente. Vigência, exercício e completude do arquivo precisam de confirmação.

#### 10.3 — Divulga a íntegra da decisão da apreciação ou julgamento das contas pelo Tribunal de Contas?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **B**. C, p. 84; S10, pp. 1–2, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Íntegra do Acórdão/Parecer do Tribunal sobre as contas, com indicação das contas ainda pendentes de apreciação; não basta divulgar a conclusão. Admite link direto ao documento no Tribunal.
- **C — itens e controles:** disponibilidade, atualidade e série histórica. Atualidade: última decisão/manifestação disponível, com a especificidade da Corte e pendências explícitas. Série C: decisões dos exercícios X-1/X-2/X-3 além da referência mais atual X. Não lista F/G.
- **S — marcação e estrutura:** PC; S10 10.3.1–10.3.3: integraJulgamentoTCE (Anexo), A/H; links/arquivos no mesmo contexto de exercício. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M01, decisões por exercício; situação pendente só conforme informação institucional, sem criar documento fictício para exercício não julgado.
- **Compartilhamento:** 10.1/10.2: exercício das contas; mesmo documento TCE não precisa ser copiado se existir link direto estável e válido.
- **Documentos integrais/vínculos:** Decisão integral de apreciação/julgamento, não apenas extrato da conclusão.
- **Lacuna ou ambiguidade:** A redação de disponibilidade em C é truncada e menciona última manifestação; manter a ressalva e não pressupor ausência de decisão. Não inventar prazo de julgamento.

#### 10.4 — Divulga o Relatório de Gestão Fiscal (RGF)?

- **Aplicabilidade / categoria / fontes:** SIM no quadro da Cartilha; forma concreta de atendimento sujeita à ressalva de emissores/consolidação da p. 85, sem dispensa presumida. **B**. C, p. 85; S10, pp. 1–2, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** RGF e todos os anexos obrigatórios do último período exigível, em seção própria. O quadro inclui Previdência Estadual, mas o parágrafo de aplicabilidade ressalva unidades sem RGF próprio.
- **C — itens e controles:** disponibilidade, atualidade, série histórica e filtro de pesquisa. Atualidade: último quadrimestre exigível, com prazo de até 30 dias após seu encerramento. Histórico de pelo menos três anos anteriores à consulta (H3). Filtro genérico; sem G.
- **S — marcação e estrutura:** PC; S10 10.4.1–10.4.4: RGF (Anexo, grafia maiúscula), F/A/H. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M01, índice de RGF por exercício/período, com documento próprio ou vínculo direto ao consolidado pertinente após decisão contábil.
- **Compartilhamento:** 10.1/10.6 compartilham origem contábil, mas não substituem o RGF.
- **Documentos integrais/vínculos:** RGF integral com anexos, próprio ou do Poder/órgão em que a Unidade esteja consolidada, conforme confirmação.
- **Lacuna ou ambiguidade:** DÚVIDA — REVISÃO NECESSÁRIA: confirmar se emite relatório próprio ou qual consolidado a abrange. C admite não se aplica fundamentado para não emissores ou link direto ao consolidado; não presumir dispensa nem criar RGF da autarquia.

#### 10.5 — Divulga o plano estratégico institucional?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **B/A**. C, p. 86; S10, pp. 1–2, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Plano estratégico com objetivos estratégicos, indicadores e metas; não se confunde com PPA.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar o conteúdo e a vigência descritos.
- **S — marcação e estrutura:** PC; S10 10.5.1 planoEstrategico (Anexo); exemplo de link para o plano, sem F/A/H/G próprios. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M01: plano integral e vigência real. Se existir base de objetivos/indicadores/metas validada, pode alimentar uma visão de acompanhamento, como melhoria técnica, sem XLSX mínimo adicional.
- **Compartilhamento:** 10.2 pode referenciar execução/resultados; 8.6 PCA é outro instrumento.
- **Documentos integrais/vínculos:** Plano estratégico institucional integral.
- **Lacuna ou ambiguidade:** Não criar indicadores, valores-alvo, prazo de vigência ou periodicidade de revisão que a fonte não forneça.

#### 10.6 — Publica os Balancetes Mensais?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **B/A**. C, p. 87; S10, pp. 1–2, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Balancetes mensais com, no mínimo, execução orçamentária e financeira do mês (receitas e despesas), identificados por mês/exercício; PDF pesquisável.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: último mês exigível; publicar em até 30 dias após o mês é recomendação expressa, não transformar em prazo absoluto. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação em pelo menos um formato editável (E). Versão oficial assinada acompanhada de editável sem assinaturas. Filtro: exercício e mês; C admite organização única facilmente localizável por Ctrl+F.
- **S — marcação e estrutura:** PC; S10 10.6.1–10.6.5: balanceteMensal (Anexo), F/G/A/H. Destino PlanejamentoPrestacaoContas/Balancetes. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M01 para arquivos oficiais e editáveis, ligados à competência; M02/M03 apenas se a origem contábil permitir gerar os dados corretos do balancete.
- **Compartilhamento:** 3.1, 4.1/4.2/4.3 e 10.1, sem confundir extração dos dados com demonstrativo oficial completo.
- **Documentos integrais/vínculos:** Balancete do mês e versões editáveis do conjunto, conforme a regra C.
- **Lacuna ou ambiguidade:** Matriz II em S10 é ressalva técnica; C inclui expressamente as previdências. Conferir o mês exigível com a contabilidade; não fabricar data de publicação.


### Dimensão 11 — SIC e estatísticas de acesso à informação

#### 11.1 — Existe o SIC no site ou no portal de transparência e indica a unidade/setor responsável?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A — complementar**. C, p. 88; S11, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Existência de SIC e identificação da unidade/setor responsável pelo atendimento físico.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar o conteúdo e a vigência descritos.
- **S — marcação e estrutura:** SIC; S11 11.1.1 setorResponsavel (Texto); contexto SIC/Detalhe. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Cadastro editorial específico do SIC em HTML; sem XLSX próprio.
- **Compartilhamento:** 11.2: mesmo setor; 2.4/13.1 apenas se a coincidência de unidade for comprovada.
- **Documentos integrais/vínculos:** Nenhum inteiro teor adicional exigido.
- **Lacuna ou ambiguidade:** Não usar automaticamente o nome da Ouvidoria ou o atendimento geral como setor SIC.

#### 11.2 — Indica o endereço físico, o telefone e o e-mail da unidade responsável pelo SIC, além do horário de funcionamento?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A — complementar**. C, pp. 89–90; S11, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Endereço físico e telefone do SIC, e-mail do responsável e horário da unidade.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar o conteúdo e a vigência descritos.
- **S — marcação e estrutura:** SIC; S11 11.1.2–11.1.5: enderecoSetor (Endereço), telefoneSetor (Numérico), emailSetor (E-mail), horarioFuncionamentoSetor (Hora). Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Manutenção editorial dos contatos específicos em HTML; sem planilha autônoma.
- **Compartilhamento:** 11.1; contatos gerais só mediante confirmação institucional de equivalência.
- **Documentos integrais/vínculos:** Nenhum documento integral exigido.
- **Lacuna ou ambiguidade:** Não inferir que contatos gerais da página Informações atendem ao SIC. Tipos técnicos não autorizam inventar ramais ou remover informação do telefone.

#### 11.5 — Divulga nesta seção, instrumento normativo local que regulamente a Lei nº 12.527/2011 – LAI?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **B**. C, pp. 93–94; S11, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Ato normativo local legal/infralegal que regulamenta a LAI; texto ou link visível, identificado e associado à Transparência/LAI.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar o conteúdo e a vigência descritos.
- **S — marcação e estrutura:** SIC; S11 11.3.1 lai (Texto/Link), contexto SIC/LAI. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M01 para norma e referência na página SIC; texto editorial ou arquivo oficial sem novo modelo.
- **Compartilhamento:** 2.6/2.9 somente se o mesmo ato for pertinente; uma origem documental, vários acessos contextualizados.
- **Documentos integrais/vínculos:** Instrumento normativo local integral, ou seu texto completo.
- **Lacuna ou ambiguidade:** Não criar regulamento a partir do modelo municipal ilustrativo nem pressupor que qualquer lei estadual de criação regule o SIC.

#### 11.6 — Divulga, na seção relativa ao e-SIC, os prazos de resposta ao cidadão, incluindo o recursal, e as autoridades competentes para o exame dos pedidos, além do procedimento referente à realização do pedido e de eventual recurso?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A — complementar**. C, pp. 94–95; S11, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Prazos de resposta e recursal, autoridades competentes e procedimento do pedido e eventual recurso, em destaque na seção e-SIC.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar o conteúdo e a vigência descritos.
- **S — marcação e estrutura:** SIC; S11 11.4.1–11.4.4: prazoResposta, recursal, autoridadeExame, procedimentoPedido (Texto). Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Texto orientativo estruturado em HTML, obtido da norma validada; sem XLSX mínimo.
- **Compartilhamento:** 11.5: norma de origem; cadastro do SIC em 11.1/11.2.
- **Documentos integrais/vínculos:** Norma de suporte compartilhada, se vinculada; o mínimo é a orientação visível na seção.
- **Lacuna ou ambiguidade:** Não copiar prazos ou autoridades do exemplo Serigy como dados da autarquia, nem criar coluna de instância recursal sem fonte.

#### 11.7 — Divulga relatório anual estatístico contendo a quantidade de pedidos de acesso recebidos, atendidos, indeferidos, bem como informações genéricas sobre os solicitantes?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A/C**. C, pp. 95–97; S11, pp. 1–3, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Relatório anual com quantidades de pedidos recebidos, atendidos, indeferidos e informações genéricas sobre solicitantes. Gráficos são aceitos se todos os dados estiverem claros e acessíveis.
- **C — itens e controles:** disponibilidade, atualidade, série histórica, gravação de relatórios e filtro de pesquisa. Atualidade: último exercício encerrado. Histórico de pelo menos três anos anteriores à consulta (H3). Exportação em pelo menos um formato editável (E). Filtro genérico, sem campos mínimos enumerados.
- **S — marcação e estrutura:** SIC; S11 11.5.1–11.5.8: pedidosRecebidos, pedidosAtendidos, pedidosIndeferidos (Numérico), infoGenericas (N/A); F/G/A/H. Exemplo apresenta tabela de totais e detalhe agregado. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M10 estatísticas, abas sic_anual e solicitantes_agregados; entrada com totais oficiais e categorias efetivamente existentes, sem pessoas identificáveis.
- **Compartilhamento:** Base operacional e-SIC alimenta agregados; não compartilhar/publicar cadastros individuais. M01 pode indexar o relatório oficial.
- **Documentos integrais/vínculos:** Relatório anual completo com as informações mínimas, em HTML/arquivo; se documental, vincular versão integral e exportação editável.
- **Lacuna ou ambiguidade:** Idade/sexo/categoria são exemplos C, não todas colunas obrigatórias. Não impor recebidos = atendidos + indeferidos sem conhecer os conceitos e saldos do sistema.


### Dimensão 12 — Mapa do site

#### 12.5 — Contém mapa do site institucional?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **B — complementar**. C, p. 101; S12, p. 1, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Mapa do sítio institucional, ao menos.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar o conteúdo e a vigência descritos.
- **S — marcação e estrutura:** ACESS; S12 item 12.5 acessibilidadeMapaSite (Link); não possui schema de dados financeiros. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Índice derivado das páginas efetivamente publicadas/manifesto de navegação; HTML/JSON técnico, sem XLSX próprio.
- **Compartilhamento:** Manifesto da busca geral de 1.4 e navegação, sem substituir o catálogo de documentos por critério.
- **Documentos integrais/vínculos:** Nenhum PDF integral obrigatório.
- **Lacuna ou ambiguidade:** Não prometer cobertura total dos documentos só porque existe mapa das oito páginas principais. Atualização da navegação é decisão de manutenção.


### Dimensão 13 — Ouvidoria e Carta de Serviços

#### 13.1 — Há informações sobre o atendimento presencial pela Ouvidoria (Indicação de endereço físico e telefone, além do horário de funcionamento)?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A — complementar**. C, pp. 103–104; S13, p. 1, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Endereço físico, telefone e horário de funcionamento da Ouvidoria.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar o conteúdo e a vigência descritos.
- **S — marcação e estrutura:** OUV; S13 itens 13.1–13.3 (todos ligados a C 13.1): enderecoSetor, telefoneSetor, horarioFuncionamentoSetor. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Cadastro editorial de atendimento da Ouvidoria; HTML, sem modelo XLSX mínimo.
- **Compartilhamento:** 2.4/2.5 e 11.2 somente se houver equivalência institucional confirmada; schemas permanecem distintos.
- **Documentos integrais/vínculos:** Nenhum documento integral exigido.
- **Lacuna ou ambiguidade:** Link genérico para a Ouvidoria não comprova a publicação dos três dados específicos da unidade.

#### 13.3 — Divulga Carta de Serviços ao Usuário?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A/B**. C, pp. 105–106; S13, p. 1, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Carta de Serviços atualizada: serviços; requisitos/documentos/formas/informações para acesso; etapas; prazo máximo; forma de prestação; locais/formas de manifestação sobre o serviço.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar o conteúdo e a vigência descritos.
- **S — marcação e estrutura:** OUV; S13 item técnico 13.5 servicoUsuario (Link), referente a C 13.3; não criar propriedades de cada coluna da carta. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Carta em HTML ou documento integral indexado em M01. Se mantido cadastro de serviços, usar os elementos da Carta já fornecidos, sem XLSX obrigatório.
- **Compartilhamento:** 14.3: mesmo catálogo pode apontar para serviços digitais confirmados; a Carta não comprova que o serviço já é digital.
- **Documentos integrais/vínculos:** Carta de Serviços integral quando apresentada em documento.
- **Lacuna ou ambiguidade:** Atualizada é requisito do conteúdo, mas C não fixa prazo numérico ou série neste critério. Não inventar serviços, prazos, documentos ou etapas.


### Dimensão 14 — LGPD, serviços digitais, dados abertos e satisfação

#### 14.1 — Identifica o encarregado/responsável pelo tratamento de dados pessoais e disponibiliza Canal de Comunicação com esse servidor (telefone e/ou e-mail)?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A — complementar**. C, p. 107; S14, pp. 1–2, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Nome do encarregado/responsável por dados pessoais e canal de comunicação (telefone e/ou e-mail).
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar o conteúdo e a vigência descritos.
- **S — marcação e estrutura:** LGPD; S14 14.1.1 nomeResponsavel (Nome), 14.1.2 contatoResponsavel (Telefone/E-mail). Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Cadastro editorial do encarregado confirmado, em HTML; sem XLSX adicional.
- **Compartilhamento:** Cadastros institucionais apenas se houver confirmação formal; papel LGPD não se deduz do responsável da Ouvidoria/SIC.
- **Documentos integrais/vínculos:** Nenhum ato de designação obrigatório como anexo neste critério.
- **Lacuna ou ambiguidade:** Não reutilizar nomes/contatos do exemplo S14 ou de cargos genéricos como se fossem o encarregado designado.

#### 14.2 — Publica a sua Política de Privacidade e Proteção de Dados?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **B**. C, pp. 108–109; S14, pp. 1–2, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Política de Privacidade e Proteção de Dados adotada pela Unidade.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar o conteúdo e a vigência descritos.
- **S — marcação e estrutura:** LGPD; S14 14.1.3 politicaPrivacidade (Link); exemplo é acesso ao conteúdo/arquivo. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Conteúdo institucional validado em HTML ou documento; M01 para o índice da versão, sem XLSX de cláusulas.
- **Compartilhamento:** 14.1 e páginas de serviços/formulários referenciam a política vigente.
- **Documentos integrais/vínculos:** Política integral, se publicada como documento.
- **Lacuna ou ambiguidade:** Não gerar política genérica ou declarar conformidade LGPD a partir da existência de um link.

#### 14.3 — Possibilita a demanda e o acesso a serviços públicos por meio digital, sem necessidade de solicitação presencial?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A — complementar**. C, pp. 109–110; S14, pp. 1–2, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Possibilidade efetiva de solicitar e acessar serviços públicos por meio digital, sem solicitação presencial; serviços digitais são distintos de pedidos LAI/e-SIC.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade na lista de itens: sem filtro, série histórica ou formato de exportação autônomos. Preservar o conteúdo e a vigência descritos.
- **S — marcação e estrutura:** LGPD; S14 14.2.1 servicoPublico (Link), contexto LGPDeGovernoDigital/Servicos. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Reutilizar o catálogo editorial da Carta de Serviços, com links reais para os serviços digitais; HTML/JSON técnico, sem XLSX próprio.
- **Compartilhamento:** 13.3: catálogo; não fundir a base de atendimento operacional com as estatísticas do SIC.
- **Documentos integrais/vínculos:** Nenhum PDF integral obrigatório.
- **Lacuna ou ambiguidade:** É critério funcional associado a um catálogo: a lista de links sozinha não comprova atendimento digital. Destinos exigem teste funcional após publicação.

#### 14.4 — Possibilita o acesso automatizado por sistemas externos em dados abertos (estruturados e legíveis por máquina), e a página contém as regras de utilização?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A/B**. C, pp. 111–112; S14, pp. 1–2, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Acesso automatizado externo em formato aberto e legível por máquina, com regras de utilização em seções detalhadas e exemplos; neste ciclo ao menos um caso legível por máquina atende ao mínimo.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade. Não fixa filtro, periodicidade ou série próprios, nem obriga servidor/API. Não confundir com G dos demais critérios.
- **S — marcação e estrutura:** LGPD; S14 14.3.1 dadosAbertos (Texto), no contexto LGPDeGovernoDigital/DadosAbertos. Exemplo envolve descrição das regras e acesso aos dados; não há propriedade apiEndpoint documentada. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** Gerar CSV/JSON público dos conjuntos aprovados e catálogo/regras em HTML; derivar dos M02–M10, sem um XLSX manual para duplicar dados abertos.
- **Compartilhamento:** Todos os conjuntos efetivamente publicáveis; identificadores e descrições podem reaproveitar M01 sem substituir dados por metadados.
- **Documentos integrais/vínculos:** Arquivos estruturados acessíveis e suas regras/exemplos de uso; não basta PDF ou planilha de origem privada.
- **Lacuna ou ambiguidade:** Os CSV/JSON atuais são de teste e não há página específica no recorte. Não afirmar dados reais ou API pronta. Não publicar planilha bruta com campos pessoais não autorizados.

#### 14.5 — Realiza e divulga resultados de pesquisas de satisfação?

- **Aplicabilidade / categoria / fontes:** SIM, conforme quadro da Cartilha. **A/C**. C, p. 113; S14, pp. 1–2, seções/itens indicados abaixo.
- **C — campos/conteúdo mínimo:** Resultados de pesquisas de satisfação efetivamente realizadas de forma regular; as frequências anual/semestral/pós-atendimento são exemplos, não um prazo único obrigatório.
- **C — itens e controles:** disponibilidade. Somente Disponibilidade; sem H/F/G/A autônomos ou escala de avaliação fixada.
- **S — marcação e estrutura:** LGPD; S14 14.1.4 pesquisaSatisfacao (Link/Forms), 14.1.5 resultadoSatisfacao (Link/Imagem/Texto). Pesquisa e resultados são itens distintos; gráfico ou tabela conforme a fonte. Aplicar a hierarquia e associação de registros da seção 3.2.
- **DT — conjunto e entrada propostos:** M10, abas pesquisas e resultados_agregados: perguntas, categorias/escala e resultados somente conforme os instrumentos realmente aplicados; sem inventar indicadores ou notas.
- **Compartilhamento:** 13.3/14.3: serviço avaliado quando identificado; metodologia e população distintas do relatório e-SIC 11.7.
- **Documentos integrais/vínculos:** Resultados completos da pesquisa; relatório/instrumento integral quando usados para sua apresentação, sem expor respondentes.
- **Lacuna ou ambiguidade:** Não basta link para responder à pesquisa. Não gerar NPS, percentuais ou escalas novas; categorias e denominadores dependem da fonte institucional.

## 6. Divergências e decisões pendentes

| Assunto | Evidência / decisão |
| --- | --- |
| Currículo e matriz | C tem só 2.3; S2 usa 2.3.1 como referência técnica do currículo e ressalva Matriz II. Planejar nome e currículo; esclarecer a abrangência dos responsáveis sem presumir todas as gerências ou somente diretores. |
| Aplicabilidade de 2.9/10.6 | Quadros C incluem Previdência; S2/S10 ressalvam Matriz II. Manter no escopo; falta de identificação nominal da matriz não autoriza excluir. |
| Emissão de RGF | C p. 85 admite solução fundamentada para não emissores ou link direto ao consolidado. Confirmar com a contabilidade, sem presumir dispensa, documento ou URL. |
| Schema de Planejamento | Cabeçalho S10 p. 1 e documentos p. 2 usam `planejamento-prestacao-contas.html`; filtro/atualização nos exemplos usam `gestao-fiscal-planejamento.html`. **DÚVIDA — REVISÃO NECESSÁRIA:** confirmar antes de implementar; alias PC registra o cabeçalho, sem resolver a divergência. |
| Grafia dos atributos | C pp. 15–16 nomeia `serigy...` e exemplifica `sc-camel-serigy-...`; SD e dimensões usam `serigy...`. Registrar a divergência, sem converter o protótipo nesta tarefa. |
| Vigência de convênios | S5 tipa `vigenciaConvenio` como Ano e exemplifica data; C exige vigência. Preservar o período real e confirmar representação técnica. |
| Séries históricas | Anos dos exemplos S não limitam a C. Em 10.1–10.3, preservar X e X-1/X-2/X-3 e confirmar a referência exigível. Não reduzir todo conjunto a três exercícios. |
| Campos sem item S | Número do empenho/identificação para filtro de 4.3, número do certame em 8.1 e fonte/categoria/justificativa de 9.4 não têm propriedade própria nas tabelas S citadas. Exibir o exigido sem criar atributos; validar a leitura posteriormente. |
| Sanções | C 8.7 fixa mínimo nominal; S8 acrescenta `idSancionado` (CNPJ/CPF). Identificação é requisito técnico adicional; confirmar fonte e publicação, sem inventar identificação ou colunas extras de penalidade. |
| Exportação | PDF nos exemplos S não substitui editável fora das exceções C. Entrada XLSX privada não é automaticamente o arquivo público; gerar derivados adequados e preservar versões oficiais. |
| Não ocorrência / PCA | Regra geral C p. 19 não supera a exceção 8.6. Não gerar declaração-padrão que marque todos os critérios como atendidos. |
| Estatísticas | Idade/sexo/categoria em 11.7 e frequências em 14.5 são exemplos. Não impor todas essas colunas, escala fixa, NPS ou equação de fechamento de pedidos sem fonte. |

## 7. Modelos XLSX mínimos propostos e ordem eficiente

**DT — organização proposta, não exigência da Cartilha para o formato de entrada.** Os dez modelos lógicos agrupam conjuntos com a mesma origem ou atualização relacionada, evitando um livro por critério. Cada aba reutiliza os mínimos das fichas; não cria novas colunas normativas. O número físico de arquivos poderá variar por responsável, sem obrigar concentração de bases ou mistura de consultas públicas.

Origens em `dados-entrada`, fora de `dist`. Caminho do arquivo, associação ao registro, exercício/competência, cobertura e atualização são controles técnicos de publicação, sempre com valores reais. O catálogo aponta para documentos oficiais separados: não incorpora PDFs em células nem substitui seus inteiros teores.

| Modelo proposto | Abas e conteúdo mínimo da origem | Critérios que atende/apoia | Ordem e dependências |
| --- | --- | --- | --- |
| **M01 — catalogo_documentos.xlsx** | Atos, legislação e documentos por assunto/exercício: tipo, número, ano, descrição/data quando presentes/exigidos e referência conferida ao arquivo. Vínculos ao procedimento/contrato/concurso; versões oficial/editável quando cabíveis. Controle de atualização e não ocorrência verdadeira. | 2.1, 2.2 (opção documental), 2.3 (currículo em arquivo), 2.6, 2.9; documentos de 5.1–5.3, 6.6–6.7, 7.2, 8.2–8.6, 9.1–9.2/9.4, 10.1–10.6, 11.5, 13.3, 14.2 e relatórios de 11.7/14.5. Não substitui dados numéricos. | **1:** infraestrutura comum e correspondência das portarias. Solicitar desde o início documentos contábeis essenciais e confirmação do RGF. Catálogo pode ter abas por área, sem duplicar arquivos. |
| **M02 — receitas.xlsx** | Ano, mês, previsto e realizado; mesma base para tabela e exportação. | 3.1; apoia 10.6/14.4. | **2:** reaproveitar tabela/importação existentes com dados reais. Critério essencial. |
| **M03 — despesas.xlsx** | Abas empenhos e movimentos/execução conforme origem contábil: identificação/período, credor, valor/estágios, objeto, procedimento e classificação com códigos/descrições. Evitar somar saldos cumulativos. | 4.1–4.3; referência para 9.4/10.6/14.4. | **3:** três essenciais numa base coerente. Definir granularidade com a contabilidade antes do layout definitivo. |
| **M04 — pessoal.xlsx** | Abas vínculos, folha, padrões, estagiários e terceirizados, cada qual com seus mínimos e referências para filtros/histórico. Pessoa, vínculo, pagamento e faixa salarial são conjuntos distintos. | 6.1–6.5; apoia 14.4. | **4:** estagiários reaproveita a importação atual; vínculos/folha compartilham cadastro. Pode haver entrega por área sem mudar o desenho lógico. |
| **M05 — convenios.xlsx** | Recebidas, realizadas e sem_recursos. Participantes/repasses como abas auxiliares somente quando houver relações múltiplas na fonte; instrumentos em M01. | 5.1–5.3. | **6:** reusar catálogo/controles, mantendo recebidas e realizadas em consultas autônomas, sem valores fictícios em acordos sem recursos. |
| **M06 — diarias.xlsx** | Concessões e valores de referência: beneficiário/cargo, quantidade/total, início/fim, motivo/cidade; faixas reais da norma e suas versões. | 7.1 e 7.2. | **7:** aproveitar filtros/atualização; separar pagamentos dos valores normativos. |
| **M07 — licitacoes.xlsx** | Procedimentos, incluindo contratações diretas pertinentes, com número/modalidade/objeto/abertura/valor/situação. Sanções em aba própria com identificação técnica confirmada. Fases, atas e PCA em M01. | 8.1–8.7; referência para 4.3/9.1. | **5a:** antes dos vínculos contratuais. Documentos não devem ser redigitados como se fossem dados do certame. |
| **M08 — contratos.xlsx** | Contratos, aditivos, fiscais e ordem_pagamentos. Associação fiscal–contrato; pagamentos com fonte/categoria/ordem e justificativas reais. Integrais em M01. | 9.1–9.4, com execução de M03. | **5b:** após identificação dos procedimentos de M07 e compatibilização com M03. Fiscais em relação autônoma. |
| **M09 — concursos.xlsx** | Certames, aprovados/classificações e nomeações conforme fonte oficial; editais/listas documentais em M01. Não impor base nominal se documentos completos bastarem ao caso. | 6.6 e 6.7. | **8:** reusar catálogo/controles, com prazos/série próprios. Não inferir nomeação pela aprovação. |
| **M10 — estatisticas.xlsx** | sic_anual, solicitantes_agregados, pesquisas e resultados_agregados conforme instrumentos reais. SIC: recebidos/atendidos/indeferidos e informações genéricas. Satisfação: escala/categorias/resultados somente da fonte. | 11.7 e 14.5; arquivos via M01. | **9:** depende dos conceitos e consolidação pelas áreas. Não publicar cadastros individuais nem forçar metodologia/população comum aos dois relatórios. |

A ordem é de reaproveitamento e dependências, não de dispensa ou pontuação normativa. Preparar fontes em paralelo e disponibilizar o que estiver completo/validado. **10.4 é essencial:** tratar documentos e confirmação de responsabilidade já em M01; os demais relatórios de contas também reutilizam M01, sem aguardar M10.

**Sem XLSX adicional obrigatório:** contatos, horário, competências, responsáveis/currículos textuais, FAQ, canais, orientações SIC, encarregado, Carta/serviços e política podem continuar editoriais em HTML ou documentos. Mapa/manifesto são índices técnicos; dados abertos podem ser derivados de CSV/JSON aprovados. Não criar livro vazio para cada página nem planilha de transcrição de leis/relatórios.

**Convenções DT a detalhar quando os modelos forem autorizados:** uma linha por fato/associação na granularidade da aba; datas XLSX ou ISO inequívoco na entrada; códigos/documentos como texto quando zeros/pontuação forem significativos; valores monetários numéricos conciliados com a fonte; sem células mescladas/totais intermediários confundidos com registros. Essas convenções não adicionam campos C. Conteúdos privados, credenciais e dados pessoais não autorizados não compõem os derivados públicos.

**Limitação atual:** aceitar XLSX não significa aceitar várias abas ou novos conjuntos. `importar_dados.py` usa a primeira aba e implementa somente receitas/estagiários; a evolução dependerá de tarefa específica. Nenhum importador ou modelo foi criado/alterado/executado neste levantamento.

## 8. Cobertura dos 66 critérios

“Fora deste recorte” significa critério aplicável de interface/fluxo, não dispensa. Formulários e-SIC contêm requerentes/pedidos: não se propõe XLSX público dessa base; os agregados de 11.7 estão incluídos. 14.3 foi mantido como complementar por compartilhar o catálogo de 13.3; seu atendimento depende da funcionalidade real, não de uma tabela.

| Código | Redação oficial | Aplicabilidade à Previdência Estadual | Tratamento no levantamento |
| --- | --- | --- | --- |
| 1.1 | Possui sítio oficial próprio na internet? | SIM (quadro C, p. 23). | Fora deste recorte: existência/disponibilidade do sítio. |
| 1.2 | Possui portal da transparência próprio ou compartilhado na internet? | SIM (quadro C, p. 23). | Fora deste recorte: existência do Portal. |
| 1.3 | O acesso ao portal transparência está visível na capa do site? | SIM (quadro C, p. 24). | Fora deste recorte: acesso visível/navegação. |
| 1.4 | O site e o portal de transparência contêm ferramenta de pesquisa de conteúdo que permita o acesso à informação? | SIM (quadro C, p. 24). | Fora deste recorte: busca geral, distinta dos filtros dos conjuntos. |
| 2.1 | Divulga a sua estrutura organizacional e a norma que a institui/altera? | SIM (quadro C, p. 26). | Ficha A/B |
| 2.2 | Divulga competências e/ou atribuições? | SIM (quadro C, p. 26). | Ficha A/B — complementar |
| 2.3 | Identifica o nome dos responsáveis pela gestão da Unidade, com currículo resumido? | SIM (quadro C, p. 27). | Ficha A/B |
| 2.4 | Divulga os endereços e telefones atuais da Unidade e e-mails institucionais? | SIM (quadro C, p. 27). | Ficha A — complementar |
| 2.5 | Divulga o horário de atendimento? | SIM (quadro C, p. 28). | Ficha A — complementar |
| 2.6 | Divulga os atos normativos próprios? | SIM (quadro C, p. 28). | Ficha A/B |
| 2.7 | Divulga as perguntas e respostas mais frequentes relacionadas às atividades desenvolvidas pela Unidade? | SIM (quadro C, p. 29). | Ficha A — complementar |
| 2.8 | Participa em redes sociais e apresenta, no seu sítio institucional, link de acesso ao seu perfil? | SIM (quadro C, p. 30). | Ficha A — complementar |
| 2.9 | Publica, de forma clara e nominal, a legislação interna como: Lei de Criação/Autorização, Estatuto/Regimento, Lei de Estrutura Administrativa, Carta Anual (inc. I,II, III, IV, VII e VIII art. 8º da Lei 13.303/2016 para empresas públicas e sociedades de economia mista)? | SIM (quadro C, p. 31). | Ficha B |
| 3.1 | Divulga as receitas da Unidade, evidenciando sua previsão e realização? | SIM (quadro C, p. 32). | Ficha A |
| 4.1 | Divulga o total das despesas empenhadas, liquidadas e pagas? | SIM (quadro C, p. 36). | Ficha A |
| 4.2 | Divulga as despesas por classificação orçamentária? | SIM (quadro C, p. 38). | Ficha A |
| 4.3 | Possibilita a consulta de empenhos com os detalhes do beneficiário do pagamento ou credor, o valor, o bem fornecido ou serviço prestado e a identificação do procedimento licitatório originário da despesa? | SIM (quadro C, p. 40). | Ficha A |
| 5.1 | Divulga as transferências recebidas a partir da celebração de convênios/acordos com indicação, no mínimo, do número/ano do convênio/termo ou ajuste, do valor total previsto dos recursos envolvidos, do valor recebido, do objeto, da vigência, da origem (órgão repassador/concedente) e o inteiro teor do instrumento de convênio/transferência? | SIM (quadro C, p. 42). | Ficha A/B |
| 5.2 | Divulga as transferências realizadas a partir da celebração de convênios/acordos/ajustes, com indicação, no mínimo, do número/ano do convênio/termo ou ajuste, do beneficiário, do objeto, da vigência, do valor total previsto para repasse, do valor concedido e inteiro teor do instrumento de convênio/termo ou ajuste? | SIM (quadro C, p. 44). | Ficha A/B |
| 5.3 | Divulga os acordos firmados que não envolvam transferência de recursos financeiros, identificando as partes, o número/ano do convênio/termo ou ajuste, o objeto, a vigência, as obrigações ajustadas e o inteiro teor do instrumento de convênio/termo ou ajuste? | SIM (quadro C, p. 46). | Ficha A/B |
| 6.1 | Divulga a relação nominal dos servidores/autoridades/membros, seus cargos/funções, as respectivas lotações, as suas datas de admissão/exoneração/inativação e a carga horária do cargo/função ocupada/desempenhada? | SIM (quadro C, p. 48). | Ficha A |
| 6.2 | Divulga a remuneração nominal de cada servidor/autoridade/Membro? | SIM (quadro C, p. 50). | Ficha A |
| 6.3 | Divulga a tabela com o padrão remuneratório dos cargos e funções? | SIM (quadro C, p. 51). | Ficha A/B |
| 6.4 | Divulga a lista de seus estagiários, contendo o nome dos estudantes; a data de contratação e a data de término do respectivo contrato? | SIM (quadro C, p. 53). | Ficha A |
| 6.5 | Publica lista dos terceirizados que prestam serviços para a Unidade/entidades, contendo, em relação a cada um deles: nome completo, função ou atividade exercida e nome da empresa empregadora? | SIM (quadro C, p. 55). | Ficha A |
| 6.6 | Divulga a íntegra dos editais de concursos e seleções públicas realizados pela Unidade para provimento de cargos e empregos públicos? | SIM (quadro C, p. 56). | Ficha B |
| 6.7 | Divulga informações sobre os demais atos dos concursos públicos e processos seletivos da Unidade, contendo no mínimo a lista de aprovados com as classificações e as nomeações? | SIM (quadro C, p. 58). | Ficha A/B |
| 7.1 | Divulga o nome e o cargo/função do beneficiário, além do valor total recebido, número de diárias usufruídas por afastamento, período de afastamento, motivo do afastamento e local de destino? | SIM (quadro C, p. 61). | Ficha A |
| 7.2 | Divulga tabela ou relação que explicite os valores das diárias dentro do Estado, fora do Estado e fora do país, conforme legislação local? | SIM (quadro C, p. 62). | Ficha A/B |
| 8.1 | Divulga a relação das licitações em ordem sequencial, informando o número e modalidade licitatória, o objeto, a data, o valor estimado/homologado e a situação? | SIM (quadro C, p. 64). | Ficha A |
| 8.2 | Divulga a íntegra dos editais de licitação? | SIM (quadro C, p. 66). | Ficha B |
| 8.3 | Divulga a íntegra dos demais documentos das fases interna e externa das licitações? | SIM (quadro C, p. 67). | Ficha B |
| 8.4 | Divulga a íntegra dos principais documentos dos processos de dispensa e inexigibilidade de licitação? | SIM (quadro C, p. 69). | Ficha B |
| 8.5 | Divulga a íntegra das Atas de Adesão – SRP? | SIM (quadro C, p. 71). | Ficha B |
| 8.6 | Divulga o plano de contratações anual? | SIM (quadro C, p. 71). | Ficha B |
| 8.7 | Divulga a relação dos licitantes e/ou contratados sancionados administrativamente pela Unidade? | SIM (quadro C, p. 73). | Ficha A |
| 9.1 | Divulga a relação dos contratos celebrados em ordem sequencial, com o seu respectivo resumo, contendo, no mínimo, indicação do contratado(a), do valor, do objeto e da vigência, bem como dos aditivos deles decorrentes? | SIM (quadro C, p. 75). | Ficha A/B |
| 9.2 | Divulga o inteiro teor dos contratos e dos respectivos termos aditivos? | SIM (quadro C, p. 76). | Ficha B |
| 9.3 | Divulga a relação/lista dos fiscais de cada contrato vigente e encerrado? | SIM (quadro C, p. 77). | Ficha A |
| 9.4 | Divulga a ordem cronológica de seus pagamentos, bem como as justificativas que fundamentaram a eventual alteração dessa ordem? | SIM (quadro C, p. 78). | Ficha A/B |
| 10.1 | Publica a Prestação de Contas do Ano Anterior (Balanço Geral)? | SIM (quadro C, p. 81). | Ficha B |
| 10.2 | Divulga o Relatório de Gestão ou Atividades? | SIM (quadro C, p. 82). | Ficha B/C |
| 10.3 | Divulga a íntegra da decisão da apreciação ou julgamento das contas pelo Tribunal de Contas? | SIM (quadro C, p. 84). | Ficha B |
| 10.4 | Divulga o Relatório de Gestão Fiscal (RGF)? | SIM (quadro C); ressalva de emissão/consolidação, p. 85. | Ficha B |
| 10.5 | Divulga o plano estratégico institucional? | SIM (quadro C, p. 86). | Ficha B/A |
| 10.6 | Publica os Balancetes Mensais? | SIM (quadro C, p. 87). | Ficha B/A |
| 11.1 | Existe o SIC no site ou no portal de transparência e indica a unidade/setor responsável? | SIM (quadro C, p. 88). | Ficha A — complementar |
| 11.2 | Indica o endereço físico, o telefone e o e-mail da unidade responsável pelo SIC, além do horário de funcionamento? | SIM (quadro C, p. 89). | Ficha A — complementar |
| 11.3 | Há possibilidade de envio de pedidos de informação de forma eletrônica (e -SIC)? | SIM (quadro C, p. 90). | Fora do recorte de bases públicas: canal/formulário e acompanhamento operacional do e-SIC; não publicar requerentes/pedidos. |
| 11.4 | A solicitação por meio de e-SIC é simples, ou seja, sem a exigência de itens de identificação do requerente que dificultem ou impossibilitem o acesso à informação, tais como: envio de documentos, assinatura reconhecida, declaração de responsabilidade, maioridade? | SIM (quadro C, p. 93). | Fora deste recorte: simplificação das exigências do requerimento. |
| 11.5 | Divulga nesta seção, instrumento normativo local que regulamente a Lei nº 12.527/2011 – LAI? | SIM (quadro C, p. 93). | Ficha B |
| 11.6 | Divulga, na seção relativa ao e-SIC, os prazos de resposta ao cidadão, incluindo o recursal, e as autoridades competentes para o exame dos pedidos, além do procedimento referente à realização do pedido e de eventual recurso? | SIM (quadro C, p. 94). | Ficha A — complementar |
| 11.7 | Divulga relatório anual estatístico contendo a quantidade de pedidos de acesso recebidos, atendidos, indeferidos, bem como informações genéricas sobre os solicitantes? | SIM (quadro C, p. 95). | Ficha A/C |
| 12.1 | O site oficial e o portal de transparência contêm símbolo de acessibilidade em destaque? | SIM (quadro C, p. 98). | Fora deste recorte: símbolo de acessibilidade. |
| 12.2 | O site e o portal de transparência contêm exibição do “caminho” de páginas percorridas pelo usuário? | SIM (quadro C, p. 98). | Fora deste recorte: caminho de navegação. |
| 12.3 | O site e o portal de transparência contêm opção de alto contraste? | SIM (quadro C, p. 99). | Fora deste recorte: alto contraste. |
| 12.4 | O site e o portal de transparência contêm ferramenta de redimensionamento de texto? | SIM (quadro C, p. 100). | Fora deste recorte: redimensionamento. |
| 12.5 | Contém mapa do site institucional? | SIM (quadro C, p. 101). | Ficha B — complementar |
| 13.1 | Há informações sobre o atendimento presencial pela Ouvidoria (Indicação de endereço físico e telefone, além do horário de funcionamento)? | SIM (quadro C, p. 103). | Ficha A — complementar |
| 13.2 | Há canal eletrônico de acesso/interação com a ouvidoria? | SIM (quadro C, p. 104). | Fora deste recorte: canal de manifestações da Ouvidoria, distinto da estatística LAI. |
| 13.3 | Divulga Carta de Serviços ao Usuário? | SIM (quadro C, p. 105). | Ficha A/B |
| 14.1 | Identifica o encarregado/responsável pelo tratamento de dados pessoais e disponibiliza Canal de Comunicação com esse servidor (telefone e/ou e-mail)? | SIM (quadro C, p. 107). | Ficha A — complementar |
| 14.2 | Publica a sua Política de Privacidade e Proteção de Dados? | SIM (quadro C, p. 108). | Ficha B |
| 14.3 | Possibilita a demanda e o acesso a serviços públicos por meio digital, sem necessidade de solicitação presencial? | SIM (quadro C, p. 109). | Ficha A — complementar |
| 14.4 | Possibilita o acesso automatizado por sistemas externos em dados abertos (estruturados e legíveis por máquina), e a página contém as regras de utilização? | SIM (quadro C, p. 111). | Ficha A/B |
| 14.5 | Realiza e divulga resultados de pesquisas de satisfação? | SIM (quadro C, p. 113). | Ficha A/C |

## 9. Limites e validação

Levantamento baseado nos documentos locais e na inspeção estática do código. Sem internet, homologação institucional, teste de links externos ou auditoria dos inteiros teores de cada futuro conjunto. Os modelos precisam ser confrontados com as fontes das áreas antes da criação; lacunas ficam registradas, sem dados ou URLs presumidos.

Foi criado somente `controle/inventario-tabelas.md`. A conferência final compara os arquivos preexistentes e executa `git diff --check`. Não houve alteração em `dist`, portanto o validador do protótipo não é uma validação necessária desta tarefa documental. Não foram criados XLSX, alteradas planilhas, páginas, importadores, referências ou configurações, nem realizado commit.
