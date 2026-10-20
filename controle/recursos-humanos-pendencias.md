# Recursos Humanos — pendências dos modelos não publicados

Escopo: C 6.1–6.3 e S 6.1–6.2. Correspondência completa em `controle/recursos-humanos-modelos.md`. Ausência de dados não comprova ausência de vínculos, pagamentos ou padrões. Os modelos não incluem declarações de atendimento ou de não ocorrência.

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
- As dúvidas de conteúdo, competência, abrangência e vigência precisam de resposta das áreas responsáveis. Até a alimentação e validação, manter ambos os modelos fora da área publicada e sem links no menu público.
