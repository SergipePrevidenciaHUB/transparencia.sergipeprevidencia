# Recursos Humanos — pendências dos modelos não publicados

Escopo: C 6.1–6.3 e 6.5–6.7; S 6.1–6.2 e 6.4–6.5. Estagiários não é alterado. Correspondência completa em `controle/recursos-humanos-modelos.md`. Ausência de dados não comprova ausência de vínculos, pagamentos ou padrões. Os modelos não incluem declarações de atendimento ou de não ocorrência.

## RecursosHumanos/FolhaPagamento — vínculos funcionais, C 6.1

| Seção / requisito | Informação ou arquivo necessário | Providência antes da publicação |
| --- | --- | --- |
| Abrangência nominal | Relação oficial de servidores, autoridades e membros da Unidade, com fonte/responsável e cobertura | Delimitar com RH os vínculos abrangidos, inclusive cessões e múltiplos vínculos quando existentes. Não presumir que aposentados/pensionistas segurados sejam servidores da autarquia. |
| Campos C 6.1 / S 6.1.1–2 e 6.1.4–7 | Nome, cargo/função, lotação, admissão, exoneração/inativação quando aplicável e carga horária | Receber cadastro estruturado com todos os mínimos; confirmar conceito de admissão, unidade da carga horária e distinção entre vínculo ativo e desligamento não informado. Não criar datas ausentes. |
| Histórico | Arquivos dos pelo menos três anos anteriores ao da consulta e referência do cadastro atual | Definir com a fonte se há movimentos, posições ou outra granularidade. Confirmar como reconstruir o recorte anual sem inventar snapshots mensais ou perder movimentações. |
| Identidade e associação | Chave interna estável do vínculo, se necessária | Definir DT para evitar homônimos e multiplicação por pagamentos; não expor CPF/matrícula automaticamente nem deduzir identidade apenas pelo nome. |
| Filtros e gravação | Dados efetivos para nome/cargo e exercícios; exportação editável do conjunto | Implementar consulta aberta e independente da folha, com todos os campos na exportação. Não disponibilizar apenas busca que exija conhecer o servidor. |
| Atualidade | Data real de atualização, cobertura e área responsável | Preencher somente após confirmação; manter referência de até 30 dias conforme C. Data de geração do HTML não serve como atualização do cadastro. |

## RecursosHumanos/FolhaPagamento — remuneração nominal, C 6.2

| Seção / requisito | Informação ou arquivo necessário | Providência antes da publicação |
| --- | --- | --- |
| Relação nominal por competência | Arquivo oficial contendo nome completo, cargo, remuneração e mês/ano de referência | Receber fonte estruturada, incluindo cobertura histórica. Não usar os exemplos S nem importar contracheques completos como cadastro público. |
| Conceito de remuneração | Definição do valor fornecido e tratamento de folhas complementares, ajustes, estornos ou pagamentos retroativos, se existentes | Confirmar com RH/folha como compor uma linha por vínculo/competência sem duplicar valores; não supor bruto/líquido ou novas rubricas obrigatórias. Não corrigir ou somar automaticamente fontes de conceitos distintos. |
| Correspondência com o cadastro funcional | Referências confiáveis de vínculo, cargo e competência | Resolver homônimos e múltiplos vínculos; confirmar qual cargo corresponde a cada pagamento. Evitar junção que repita folha para cada movimento do cadastro. |
| Histórico, mês e ano | Competências efetivamente disponíveis, incluindo os três anos anteriores ao da consulta | Popular opções reais e conferir lacunas. Não criar pagamentos zero para períodos ausentes nem declarar acervo completo sem confirmação. |
| Acesso e exportação | Relação aberta e exportação editável do recorte nome/mês/ano | Implementar sem cadastro/login, CPF obrigatório ou conhecimento prévio de nome completo. Exportar os mínimos, incluindo a referência da competência, sem levar campos pessoais privados da fonte. |
| Atualidade | Data real da folha publicada, cobertura e responsável | Confirmar separadamente do cadastro funcional e alimentar a reserva de atualização; observar o parâmetro C de até 30 dias. |

## RecursosHumanos/PadraoRemuneratorio — C 6.3

| Seção / requisito | Informação ou arquivo necessário | Providência antes da publicação |
| --- | --- | --- |
| Cobertura da estrutura | Relação validada dos cargos/funções previstos e de todas as faixas correspondentes | Conferir completude com RH e estrutura vigente; não limitar aos cargos atualmente ocupados ou confundir salários pagos com padrão legal. |
| Valores e descrição S | Tabela oficial com cargo/função, valor e níveis/classes/padrões efetivamente existentes | Confirmar descrição, unidade/referência do valor e tratamento de cargos sem escalonamento. Não inventar padrões, classes ou valores para preencher células. |
| Legislação de origem | Normas e anexos remuneratórios vigentes ou referência direta conferida, caso utilizados | Associar cada faixa à fonte pertinente e validar vigência; não construir URLs por suposição nem usar link genérico em lugar de tabela localizável. Não há obrigação autônoma de criar PDF novo. |
| Atualização e vigência | Data real da referência e confirmação de validade no exercício atual | Se não revisada no intervalo de um ano, obter confirmação para informar expressamente que segue vigente. Não substituir a data antiga pela data do site. |
| Controles | Nenhuma exigência própria de filtro/histórico/exportação nas fontes deste critério | Preservar o escopo: não copiar os controles da folha como obrigação normativa nem marcar ação de pesquisa inexistente. |

## Tratamento de dados pessoais e arquivos de entrada

- Solicitar às áreas apenas os campos necessários às consultas e ao relacionamento técnico. O formato de entrada pode ser estruturado (DT), mas não foi criada planilha nem definido importador nesta tarefa.
- Manter arquivos de origem e chaves privadas fora de `dist`. Conferir conteúdo e autorização dos derivados públicos de HTML e exportação; não publicar planilha integral por conveniência.
- Nomes, cargos, lotação e remuneração nominal são conteúdo exigido para o universo funcional pertinente. Confirmar esse universo e as exceções concretas com a instituição, sem usar dúvidas genéricas para criar restrição de acesso à relação.
- CPF, dados bancários, endereço residencial, dependentes, saúde e outros dados adicionais eventualmente presentes na origem não foram propostos como campos públicos. Não transportar o cadastro de segurados do RPPS para estes modelos.
- As dúvidas de conteúdo, competência, abrangência e vigência precisam de resposta das áreas responsáveis. Até a alimentação e validação, manter os modelos fora da área publicada e sem links no menu público.


## RecursosHumanos/Terceirizados — C 6.5 / S 6.4

| Seção / requisito | Informação ou arquivo faltante | Providência antes da publicação |
| --- | --- | --- |
| Relação nominal C p. 55 / S 6.4.1–3 | Nome completo, função/atividade e empresa empregadora de cada trabalhador que presta serviços à Unidade | Obter relação oficial validada pela área responsável. Não usar exemplos S nem nomes de servidores como terceirizados por dedução. |
| Identificação temporal | Exercício/cobertura real da relação; mudanças de atividade/empresa quando existentes | Definir a granularidade com a fonte, preservando associações trabalhador–atividade–empregadora no período, sem duplicar registros por cópias de listas ou inventar admissão/desligamento. |
| Histórico C p. 56 / S 6.4.5 | Pelo menos os três anos anteriores ao da consulta | Conferir acervo e preencher opções reais. Se não houve contratação, obter confirmação dos exercícios e declaração verdadeira; ausência de arquivo não comprova não ocorrência. |
| Filtro e gravação C p. 56 / S 6.4.6–7 | Consulta por ano e arquivo correspondente ao conjunto selecionado | Implementar filtro e ao menos um editável ou PDF pesquisável, alternativa expressa C. Não anunciar exportação filtrada para arquivo estático sem esse recorte. |
| Atualidade / S 6.4.4 | Data real da atualização e cobertura, responsável | Obter referência verificável para o parâmetro de até 180 dias, sem usar data de geração. |
| Documentos e dados pessoais | Lista oficial caso adotada apresentação documental e campos autorizados dos derivados | Conferir legibilidade/acesso e os três mínimos; não acrescentar CPF, salário, dados bancários ou contratos de trabalho como obrigação deste critério. Não publicar arquivo bruto com dados pessoais adicionais. |

## RecursosHumanos/Concurso — editais, C 6.6 / S 6.5.1

| Seção / requisito | Informação ou arquivo faltante | Providência antes da publicação |
| --- | --- | --- |
| Catálogo de certames | Identificação oficial dos concursos e seleções da Unidade para cargos/empregos públicos | Obter referência estável por certame (DT), sem inventar concursos nem associar documentos por número isolado. |
| Íntegra dos editais | Documentos integrais oficiais e retificações pertinentes, se existentes, ou URLs diretas conferidas | Validar correspondência com o certame e acesso sem login. Não gerar URLs por padrão nem copiar links ilustrativos S. Não substituir íntegra por ementa ou link à capa do executor. |
| Histórico C p. 58 / S 6.5.5 | Acervo dos anos exigíveis e referência do dado mais recente | Confirmar aplicação da redação X/X-1/X-2/X-3 quando o último dado é do ano anterior. Não truncar a cobertura para três exercícios por regra automática. |
| Atualidade C p. 57 / S 6.5.4 | Data real da informação e cobertura | Conferir referência de até um ano. Se não ocorreram concursos, obter período e referência institucional para declaração expressa, sem usar a falta de documentos como prova. |
| Filtro / S 6.5.6 | Metadados efetivos para identificar certames e exercícios | Implementar os controles DT e testar localização. C não enumera filtros mínimos e admite arquivos identificáveis/acessíveis nas condições da p. 58. |

## RecursosHumanos/Concurso — demais atos, C 6.7 / S 6.5.2–3

| Seção / requisito | Informação ou arquivo faltante | Providência antes da publicação |
| --- | --- | --- |
| Aprovados e classificações | Listas oficiais ranqueadas, planilha ou acesso direto aos dados do executor | Conferir certame, completude e classificação; o tipo Numérico do item S não torna suficiente publicar somente a quantidade de aprovados. |
| Nomeações | Atos/listas oficiais de nomeação, vinculados ao certame | Conferir candidatos/atos e correspondência; não presumir nomeação por aprovação nem criar documentos ausentes. Se a situação for não ocorrência de nomeações, solicitar esclarecimento específico, sem declarar que não houve concurso. |
| Associação documental | Chave/referência comum dos certames entre editais e demais atos | Preservar o contexto entre as duas seções sem inventar propriedades Serigy. Um mesmo certame pode ter vários documentos; não exigir transcrição nominal se documentos completos atenderem. |
| Atualidade C p. 59 / S 6.5.4 | Situação real de andamento dos certames, data de atualização e cobertura dos atos | Aplicar até 30 dias quando houver concurso/processo seletivo em andamento; não generalizar para acervo encerrado. Confirmar eventual ausência de concursos antes de declaração expressa. |
| Filtro / S 6.5.6 | Identificação dos documentos/certames e acesso público | Implementar busca DT por certame, sem exigir CPF/nome de candidato. Conferir a ressalva documental C p. 59; não criar série histórica ou exportação autônoma como requisitos de 6.7. |
| Dados pessoais | Versões oficiais apropriadas à divulgação de resultados e nomeações | Conferir conteúdo de arquivos e páginas externas; não levar inscrições, documentos de identificação, contatos ou outros dados adicionais da base operacional ao modelo/exportações por conveniência. Não ocultar o conteúdo nominal exigido nem criar login de consulta. |

## Condição de liberação dos novos modelos

Confirmar fontes, abrangência, documentos e datas; responder as dúvidas temporais e de associação; alimentar dados reais e então aplicar as marcações; implementar/testar filtros e a gravação somente de Terceirizados. Concurso não recebeu botão de exportação porque C 6.6–6.7 não o exigem e S 6.5 não o documenta. Após validação e autorização de publicação, mover os conteúdos completos para as rotas correspondentes de `dist` e só então ajustar navegação pública. Nenhum aviso interno ou declaração fictícia foi inserido nos HTMLs.


## Estagiários — origem dos oito registros e aviso público

Nesta revisão, o HTML atual, `dist/dados/recursos-humanos/estagiarios-teste.csv/json` e a ficha 6.4 de `controle/inventario-tabelas.md` foram confrontados: o conjunto de oito nomes/datas coincide com a demonstração identificada como fictícia. Não foi localizada uma fonte institucional de estágio que substitua ou confirme esse conjunto como oficial. A confirmação de origem real dada nesta solicitação refere-se exclusivamente a Receitas.

Manter os oito registros identificados como **dados fictícios**, inclusive no aviso principal, legenda e acesso aos downloads. A data 18/10/2026 associada ao conjunto de teste não representa atualização de cadastro oficial; retirar essa data da interface sem inventar outra. A relação real, sua cobertura e a data de atualização devem ser fornecidas pelo RH antes de substituir a demonstração. Não remover a identificação de ficção pela simples retirada dos avisos gerais de protótipo.


Conferência complementar de origem: CSV e JSON têm oito registros e todos trazem `observacao = DADO FICTICIO`. O CSV contém “Carla Vitoria Lima”, enquanto JSON e HTML usam “Carla Vitória Lima”. Registrar a diferença de acentuação para eventual sincronização; nenhum arquivo de dados será corrigido nesta rodada. Os registros correspondem após normalização de acentos e datas.


## Padrão Remuneratório — pendências após alimentação de C 6.3

Fonte: `dados-entrada/rh/Padrao_Remuneratorio.xlsx`, aba Padrão Remuneratório, 17 registros reais. A apresentação distingue remuneração base/vencimento, CC sem vínculo 100% e CC com vínculo 60%, sem cálculos ou junção de modalidades.

- **Vigência e atualização:** obter a referência institucional da tabela e confirmar se permanece vigente no exercício atual. A origem não fornece data explícita de atualização, período de validade ou legislação. Não usar metadados do XLSX ou data da edição do HTML como atualização, nem declarar atualidade/vigência por dedução.
- **Completude:** confirmar com RH que as 17 linhas abrangem todos os cargos/funções e faixas/símbolos aplicáveis à estrutura, incluindo eventuais padrões não presentes na fonte. Não inferir acervo completo da simples carga da planilha.
- **Significado dos sinais:** a planilha tem 26 sinais “-” nas remunerações e dois nos símbolos. Mantê-los literalmente; confirmar com RH seu significado, sem presumir remuneração zero, inexistência jurídica ou ausência de direito.
- **Modalidades e percentuais:** confirmar a composição e as condições das três modalidades, caso seja necessária explicação adicional. Manter os rótulos 100% e 60% da fonte, sem recalcular ou corrigir seus valores.
- **Normas de suporte:** se forem fornecidas para contextualizar o padrão, conferir sua correspondência e vigência antes de criar links. A tarefa não inventa uma lei nem transforma documento inexistente na origem em novo anexo obrigatório.
- **Leitura Serigy:** os campos usam apenas `cargo`, `descricao` e `salario`, distinguindo as três colunas por seus cabeçalhos e pelo registro. Conferir posteriormente a extração das modalidades no Invoker, sem atribuir conformidade integral à carga do HTML.

A estrutura vazia de 6.3 foi substituída pelos registros; os demais modelos e seções não foram alterados. As pendências são internas, sem faixa pública de validação ou falsa data de atualização.


## Estagiários — pendências após carga da relação real

A orientação histórica acima sobre manter os oito nomes de demonstração na página foi superada pela fonte real agora fornecida: `dados-entrada/rh/estagiarios.xlsx`, Plan1, 714 registros. Os arquivos antigos `estagiarios-teste.csv/json` não foram alterados ou excluídos, mas deixaram de ser oferecidos na página.

- **Atualização e cobertura:** obter do RH a data real de atualização e confirmar cobertura por período. A presença de anos 2023–2026 e a carga do arquivo não comprovam completude ou atualidade. Não criar meses ausentes.
- **Término/desligamento:** 605 células vazias e 109 preenchidas. Confirmar situação e significado dos vazios com RH; não inferir vigência, atividade ou renovação. O campo fonte reúne término ou desligamento, sem permitir separar esses eventos.
- **Aditivo:** 605 células vazias; ausência não equivale a “Não”. Preservar as respostas existentes sem deduzir duração contratual.
- **Período e repetições:** Ano/Mês são da relação; preservar todos os registros inclusive repetições. Qualquer revisão da correspondência entre pessoa, contrato e períodos depende da origem, sem deduplicação automática.
- **Regeneração:** usar `tools/integrar_estagiarios.py` para esta fonte. O importador genérico de demonstração não contempla seus períodos e campos complementares; não utilizá-lo para regenerar esta página sem adaptação específica.
- **Leitura Serigy:** conferir posteriormente a extração dos três campos de estágio e dos controles no robô; nenhum hash ou declaração de atendimento integral foi inserido.


## Terceirizados — pendências após carga de C 6.5

Fonte: `dados-entrada/rh/terceirizados.xlsx`, aba Plan1. Mantidos 3.078 registros, com cinco colunas públicas. As orientações anteriores para obter uma relação real foram atendidas quanto à disponibilização desta fonte, permanecendo as conferências abaixo.

| Linha física XLSX | Período da relação | Campo faltante | Empresa | Providência |
| --- | --- | --- | --- | --- |
| 970 | maio/2024 | CARGO — Função ou atividade exercida | NILTEK | Solicitar à área responsável a função correta e corrigir na origem após conferência. |
| 1931 | agosto/2025 | NOME — Nome completo | NILTEK | Solicitar identificação nominal correta; não deduzir de meses adjacentes. |
| 2008 | setembro/2025 | NOME — Nome completo | NILTEK | Solicitar identificação nominal correta; não deduzir de outros registros. |

Essas três linhas foram preservadas integralmente entre as colunas autorizadas. “Não informado” não recebe `nomeTerceirizado`/`funcaoTerceirizado` e o CSV mantém a célula vazia. Não houve exclusão silenciosa ou preenchimento por suposição.

- Obter a data real de atualização da relação antes de marcar `dataUltimaAtualizacao`. Não utilizar data de importação, metadados do XLSX ou último período como prova.
- Confirmar completude e cobertura dos períodos 2023–2026; não criar meses ou declarar ausência de fatos nos períodos não fornecidos.
- Repetições por período são próprias da relação mensal: não deduplicar por nome. Todas as empresas da origem permanecem, sem exclusão por interpretação contratual.
- LOTAÇÃO, DATA DE ADMISSÃO e DATA DE DEMISSÃO permanecem fora desta publicação; eventual inclusão depende de tarefa e avaliação próprias. O XLSX não foi copiado para `dist`.
- Conferir posteriormente a leitura dos campos/controles no Serigy. A implementação usa S 6.4.1–6.4.7 apenas nos contextos confirmados, sem afirmar validação oficial.


## Servidores — pendências após alimentação da relação nominal C 6.1

Fonte: `dados-entrada/rh/relacao-servidores.xlsx`, Plan1, 1.598 registros de relações periódicas (430/449/416/303 em 2023/2024/2025/2026). O fornecimento desta relação supera a pendência anterior de obter uma fonte nominal, sem resolver os pontos abaixo. Não houve carga de remuneração.

- **Carga horária:** confirmar a unidade de tempo, base e significado dos valores 40, 180 e 200 por registro/cargo. A coluna informa o número da fonte, sem afirmar horas semanais/mensais, converter ou harmonizar valores. Confirmar sua correspondência com a carga do cargo/função exigida por C 6.1.
- **Função e Cargo Efetivo:** manter as duas informações quando presentes, identificadas na célula/CSV. O literal VAZIO é um marcador de ausência: não publicar como cargo válido nem substituí-lo por cargo presumido. A origem tem 357 ocorrências desse marcador/ausência em Função e 1.108 em Cargo Efetivo; confirmar eventual necessidade de correção da origem com RH.
- **Exoneração/inativação:** 27 registros preenchidos e 1.571 vazios; não deduzir atividade/vigência a partir de ausência. Confirmar cobertura dos eventos e distinção de vínculos se necessária, sem criar campos ou datas por suposição.
- **Atualização e cobertura:** obter data real de atualização e confirmar completude dos períodos e do universo funcional. Importação, último mês ou data de modificação do XLSX não comprovam atualidade. Não presumir segurados/inativos do RPPS como servidores da Unidade.
- **Identificação por período:** preservar repetições nas relações mensais e não criar competências ausentes. Qualquer correção de vínculos ou registros depende de fonte institucional.
- **Marcação e publicação:** conferir posteriormente a extração Serigy. Os campos semanticamente incertos continuam documentados sem marcação indevida. A existência da consulta não declara atendimento integral ao PETP; a alimentação de C 6.2 passa a ser descrita na seção específica abaixo.


## Remuneração nominal — pendências após alimentação de C 6.2

O bloco 6.2 agora possui 1.596 registros conciliados de `remuneracao.xlsx`, sem alterar o bloco 6.1. A pendência anterior de obter dados de remuneração foi superada quanto ao fornecimento desta fonte. A carga não declara cobertura histórica integral, validação contábil ou atendimento integral do critério.

- **714 estágios universitários:** excluídos da remuneração de servidores por classificação expressa no Cargo Efetivo. Índices físicos, períodos e classificações registrados em `controle/remuneracao-conciliacao.json`; totais anuais 147/170/209/188 (2023/2024/2025/2026). Não atribuir seus rendimentos a servidores por coincidência de nome ou período. Não alterar os dados de Estagiários nesta tarefa.
- **Associação ambígua, dezembro/2024:** José Roberto de Lima Andrade tem duas linhas na relação (859, 860) e duas na remuneração (1170, 1171). Os cargos efetivos diferem (`SERV EXTERNO` / `SERV EXTERNO-PROFESSOR`), embora o rendimento de cada linha seja R$ 27.450,00. Solicitar ao RH chave de vínculo/explicação da duplicidade e orientação documental antes de atribuir, somar ou deduplicar os valores. Nenhum desses dois rendimentos foi publicado; os dois registros da relação 6.1 não foram excluídos.
- **Significado do rendimento:** confirmar abrangência e composição de `Valor de Rendimento Contra-Cheque`, tratamento de verbas eventuais/indenizatórias e folhas complementares. Não chamar o valor de salário-base, não deduzir descontos ou usar líquido como remuneração. O rótulo público permanece “Valor de rendimentos do contracheque”; `salarioServidor` é a propriedade técnica confirmada, não uma conclusão sobre rubricas.
- **Precisão monetária:** parte dos números tem resíduos binários muito inferiores a um centavo. A apresentação segue as duas casas do formato da própria planilha; valores armazenados e exibidos estão no JSON de conciliação. Qualquer mudança de formato ou precisão efetiva superior à tolerância fica pendente, sem correção automática de valores.
- **Atualização e períodos:** obter data real de atualização e confirmar cobertura por competência, incluindo eventuais ajustes posteriores. A competência mais recente e a importação não comprovam atualidade, fechamento ou completude. Não preencher `dataUltimaAtualizacao` sem evidência real.
- **Leitura Serigy:** conferir posteriormente a associação de nome, cargo e rendimento por linha e os controles no robô. Não inserir hash nem declarar homologação a partir da validação local.

Permanecem as demais pendências do 6.1, especialmente a unidade da carga horária e a cobertura. A equivalência de início de exercício à admissão já foi confirmada e sua marcação foi preservada.


### Atualização das páginas de RH — 21/10/2026

Data de atualização da página informada pela instituição: 21/10/2026, publicada sob o schema de Recursos Humanos em FolhaPagamento (uma única marcação compartilhada pelos blocos 6.1 e 6.2), Padrão Remuneratório, Estagiários e Terceirizados. Correspondências Serigy: 6.1.8, 6.2.4, 6.3.4 e 6.4.4. Resolvida somente a ausência dessa data na interface; não constitui confirmação de vigência, completude, unidade da carga horária ou situação individual. Preservadas as demais pendências.

Os geradores de Estagiários e Terceirizados reproduzem a data fixa confirmada, sem usar a data da execução. FolhaPagamento mantém o bloco comum fora das duas regiões regeneradas. Não foi identificado gerador específico de Padrão Remuneratório; o HTML é mantido diretamente. Futuras alterações da data exigem nova informação institucional. O campo interno `atualizacao` do relatório de conciliação remuneratória não é a atualização da página e permaneceu inalterado.

## Consulta unificada de servidores e remuneração — 22/10/2026

Uma tabela com 1.598 cadastros e 1.596 rendimentos, usando as associações físicas já conciliadas e preservadas em `remuneracao-conciliacao.json`. Sem novo cruzamento, soma ou deduplicação. Os dois cadastros de dezembro/2024 (linhas 859 e 860) permanecem sem rendimento atribuído, não zero. Campos ausentes usam justificativas de ausência, sem presumir vínculo ativo. Permanecem a ambiguidade desses rendimentos, a unidade da carga horária, a composição dos rendimentos e a completude dos períodos. Data comum da página atualizada para 22/10/2026 conforme solicitação; competências e datas individuais preservadas. Explicações de processamento ficam neste controle. CSV do recorte contém os nove campos da tabela; o antigo CSV separado de remuneração foi preservado como arquivo legado, sem ligação na consulta.

## Ajustes de apresentação RH — 22/10/2026

Removidas explicações de processamento da interface de Padrão Remuneratório, Estagiários e Terceirizados; mantidas neste controle. A data da página é 22/10/2026, sem comprovar vigência ou cobertura. Padrão: sinais “-” são da origem, não zero; modalidades separadas, sem recalcular percentuais. Estagiários: “Ano de Exercício” e “Mês do Exercício” são apenas rótulos do período da relação, distintos do ano de contratação; 605 términos ausentes não permitem concluir vigência. Cobertura de 2023 limitada aos meses presentes [2, 10, 11, 12], sem criação de períodos. Terceirizados: lacunas de informação, não falha técnica: [{"linha": 954, "nome_ausente": false, "funcao_ausente": true}, {"linha": 1888, "nome_ausente": true, "funcao_ausente": false}, {"linha": 1963, "nome_ausente": true, "funcao_ausente": false}]. Preservados campos ausentes, repetições e unidades da fonte. Referências aria-describedby dos parágrafos retirados também removidas.


### Amostras legadas retiradas da publicação

Os CSV/JSON antigos receitas-teste (12 registros fictícios sem UO) e estagiarios-teste (oito registros fictícios), identificados no inventário original, continuavam em dist sem links ativos. Foram retirados do pacote e preservados em trabalho/revisao-final/amostras-legadas. Não se confundem com a planilha receitas-teste.xlsx de 425 registros reais, nem com os 714 estagiários reais. O texto legado de teste nos metadados de Receitas foi substituído por descrição factual, sem declaração de homologação ou completude.


## 4252 — ausências individualizadas em FolhaPagamento

6.1.6: mantidos os 1.598 cadastros, 27 datas reais de exoneração/inativação e 1.571 células visualmente vazias. Cada ausência agora inclui campo, Plan1:linha de origem e ano/mês, identificadores já usados na conciliação; não contém CPF nem afirma vínculo ativo. A mesma rotina individualiza as duas ausências remuneratórias ambíguas, sem atribuir valores. Datas presentes não recebem serigyEmpty. Definições Serigy, p. 2: motivo explicativo único e distinto por atributo. CSV e conteúdo público preservados; gerador e Chrome conferidos. A informação faltante e as ambiguidades do RH permanecem; correção técnica não equivale à aprovação de 6.1.6 pelo robô. Evidências: trabalho/conferencia-4252-campos/testes.json.
