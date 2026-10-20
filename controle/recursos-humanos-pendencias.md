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
