# Planejamento e Prestação de Contas — pendências dos modelos

Escopo dos controles: C 10.1–10.4 / S 10.1–10.4. As pendências originais de 10.1–10.2 são preservadas; 10.3–10.4 são complementados abaixo. Mapeamento em `controle/planejamento-modelos.md`. Nenhum documento ou data foi inventado; os modelos não foram publicados.

## BalancoGeral — C 10.1

| Requisito | Informação ou arquivo necessário | Providência |
| --- | --- | --- |
| Conteúdo mínimo | Balanço Geral oficial da Unidade, abrangendo Balanços Orçamentário, Financeiro e Patrimonial e Demonstrações das Variações Patrimoniais | Receber os arquivos e conferir o conjunto por exercício; um documento integral pode reunir os quatro. Não gerar demonstrativos a partir de Receitas/Despesas nem afirmar presença sem ler o documento. |
| Exercício exigível e prazo | Confirmação da contabilidade sobre exercício exigível e regra/prazo local de publicação | C menciona abril apenas de forma geral e reconhece prazos variáveis; não criar prazo local ou atrasos por suposição. Não confundir ano do documento com upload. |
| Série histórica especial | Documento de referência X e prestações X-1/X-2/X-3, conforme a redação C p. 82 | Confirmar a referência exigível frente ao último encerrado e conferir acervo. Não reduzir a três arquivos totais nem preencher lacunas com documento de outro exercício. |
| Formato e acesso | Arquivos oficiais completos, PDF pesquisável quando essa for a forma adotada, ou URLs diretas conferidas | Testar pesquisa, Unidade, correspondência e acesso sem login. Não copiar links exemplificativos S nem construir URLs por ano. |
| Atualização | Data real do conjunto, cobertura e responsável | Preencher somente depois da alimentação e da confirmação do schema. Data nova na página não torna balanço antigo o último exigível. |

## RelatorioGestao — C 10.2

| Requisito | Informação ou arquivo necessário | Providência |
| --- | --- | --- |
| Relatório oficial | Relatório de gestão ou atividades elaborado pelo chefe da Unidade, com resultados finalísticos e/ou de gestão do exercício anterior | Obter e conferir o documento integral; não substituir por balanço, texto criado pelo site ou resumo automático. Temas gerais listados na C não criam colunas obrigatórias no índice. |
| Atualidade e histórico | Relatório do último exercício encerrado e série X-1/X-2/X-3 além da referência X | Confirmar exercícios e cobertura conforme C p. 83, sem limitar ao ano corrente/últimos três arquivos ou aos exemplos S. |
| Pesquisabilidade | Documento pesquisável, mesmo se não editável (por exemplo, PDF) | Conferir pesquisa/consulta do conteúdo e integridade, sem exigir editável ou formatos adicionais não previstos no critério. |
| Metadados e acesso | Exercício efetivo de gestão, identificação real do relatório, arquivo/URL oficial e responsável | Associar documento ao exercício certo e à Unidade, não ao nome do arquivo por dedução. Conferir destino e acesso direto. |
| Atualização | Referência real de atualização/cobertura do conjunto | Não preencher com data da geração/upload nem transportar prazo de balanços, finanças ou outras seções. Aplicar marcação só depois de resolver o schema e haver conteúdo. |

## Comuns aos modelos 10.1–10.2

| Assunto | Pendência / providência |
| --- | --- |
| Schema — **DÚVIDA — REVISÃO NECESSÁRIA** | S identifica `planejamento-prestacao-contas.html` no cabeçalho/documentos e `gestao-fiscal-planejamento.html` no exemplo de atualização. Confirmar antes de ativar os itens. O modelo usa somente o contexto do cabeçalho, sem presumir equivalência nem marcar campos vazios. |
| Filtro / histórico | Implementar o seletor de exercício proposto como DT, preenchido só com opções reais, respeitando a série C. Não apresentar esse parâmetro como mínimo nominal enumerado pela Cartilha. |
| Gravação / formatos | C e as seções S consultadas não exigem exportação editável autônoma. Não copiar botões CSV/PDF de outras dimensões; o download deve ser o documento oficial conferido, nos formatos admitidos em cada critério. |
| Publicação e dados privados | Conferir derivados/documentos oficiais e acesso público; não copiar arquivos de trabalho, credenciais ou fontes privadas para `dist`. Não inventar declaração de inexistência por arquivo ausente. |

Antes de publicar: resolver fontes, documentos, cobertura histórica, prazos/referências e schema; alimentar arquivos/metadados/datas reais; implementar filtros e marcações; validar por HTTP os documentos e recortes, extração e acessibilidade. Os controles atuais estão desativados, sem dados fictícios ou promessa de atendimento ao PETP. Nenhuma comunicação externa foi enviada.


## TCE — C 10.3 / S 10.3

| Requisito | Informação/documento necessário | Providência |
| --- | --- | --- |
| Íntegra da apreciação/julgamento | Último Acórdão/Parecer ou manifestação pertinente da Corte, com arquivo/URL direta oficial | Obter e conferir documento integral e contas a que se refere; conclusão/extrato não basta. Não criar decisões ou deduzir teor por número de arquivo. |
| Situação das contas | Identificação institucional das contas ainda pendentes de apreciação | Confirmar exercício das contas e situação; falta de PDF não prova pendência, inexistência ou julgamento. Não confundir ano da decisão com exercício das contas. |
| Atualidade e ressalva C | Última manifestação opinativa quando cabível conforme C p. 84; cobertura e data real da informação | Confirmar como se aplica a especificidade da Corte quando os últimos julgamentos não cobrem os exercícios citados. Não criar prazo de julgamento ou transportar máximo de 30 dias de RGF. |
| Histórico | Decisão de referência X e série X-1/X-2/X-3, com indicação das contas pendentes conforme a fonte | Conferir a redação C frente ao acervo e à ressalva da última manifestação. Não reduzir a três arquivos totais nem inventar documentos para preencher anos. |
| Controles | Exercícios reais e navegação histórica funcional | Implementar o seletor DT; não criar `filtroPesquisa`/exportação porque não são itens de C/S 10.3. Aplicar `integraJulgamentoTCE` e atualização só a conteúdo real, após confirmar o schema. |

## RGF — C 10.4 / S 10.4

| Requisito | Informação/documento necessário | Providência |
| --- | --- | --- |
| Aplicabilidade / emissor | Confirmação jurídico-contábil se a Unidade emite RGF próprio ou em qual Poder/órgão está consolidada | **DÚVIDA — REVISÃO NECESSÁRIA:** quadro C inclui Previdência, mas há ressalva para não emissores. Obter fundamentação e cobertura reais; não presumir dispensa nem publicar declaração inventada de não aplicação. |
| Periodicidade exigida | RGF do último quadrimestre exigível; referência e prazo de até 30 dias após encerramento | Conferido em C p. 85. Confirmar o período concreto com a contabilidade e a correspondência do arquivo; não usar trimestre/semestre/mês por analogia nem deduzir fechamento pela data do upload. |
| Demonstrativos e anexos | RGF integral com todos os anexos obrigatórios aplicáveis ao emissor, próprio ou consolidado pertinente | C/S não enumeram a lista nominal/quantidade de anexos nestes trechos. **DÚVIDA — REVISÃO NECESSÁRIA:** receber composição validada pela contabilidade e identificar o conjunto completo, sem criar lista universal ou estruturas financeiras não previstas. |
| Documentos / cobertura | Arquivos oficiais ou URLs diretas, com exercício, quadrimestre, emissor e abrangência | Conferir identidade, integridade e consolidação da Unidade. Um arquivo pode reunir todos os anexos; vários arquivos devem manter o mesmo contexto. Não marcar um documento parcial como relatório completo. |
| Histórico | Pelo menos três anos anteriores à consulta e quadrimestres reais disponíveis | Conferir acervo por período e cobertura; não limitar aos anos de exemplos nem aplicar automaticamente X/X-1/X-2/X-3 de 10.3. Não gerar períodos sem documento. |
| Consulta | Exercícios e quadrimestres reais para os seletores DT | Implementar filtro genérico C com organização proposta, sem declarar os parâmetros como mínimos enumerados. Não copiar busca/exportação de outros conjuntos. |
| Atualização | Data real do conjunto, cobertura e responsável | Preencher somente após haver conteúdo e confirmação do schema; não usar a data de geração. Atualidade depende também do quadrimestre exigível e do prazo, não apenas de uma data recente na página. |
| Formatos / gravação | Documentos oficiais do conjunto; nenhuma exportação autônoma enumerada em C/S 10.4 | Não exigir CSV/editável ou formatos adicionais por copiar os modelos anteriores. O acesso ao RGF e anexos deve ser direto e funcional quando alimentado. |

## Pendências comuns a 10.3–10.4

Manter a divergência entre `planejamento-prestacao-contas.html` (cabeçalho/documentos) e `gestao-fiscal-planejamento.html` (exemplo de atualização) como **DÚVIDA — REVISÃO NECESSÁRIA**, sem presumir equivalência. Aplicar os itens e datas reais somente após esclarecimento e alimentação. URLs precisam de conferência; não usar `serigyLink` para PDF nem publicar arquivos privados por cópia bruta. Dados/declarações dependem de fonte institucional, não da falta de registros no modelo.

Antes da publicação autorizada: resolver emissão/cobertura/anexos do RGF e situação/acervo das contas, receber e conferir documentos, preencher referências reais, implementar os controles aplicáveis, aplicar marcações no contexto correto e validar documentos, recortes, histórico, extração e acessibilidade. Nenhum arquivo dos modelos anteriores, `dist`, menu, Receitas ou deploy foi alterado neste complemento; nenhuma comunicação externa foi enviada.


## PlanoEstrategico — C 10.5 / S 10.5

| Requisito | Informação/documento faltante | Providência |
| --- | --- | --- |
| Plano integral | Plano estratégico institucional adotado, com objetivos estratégicos, indicadores e metas | Receber e conferir o documento; não substituir por PPA ou inventar conteúdo. |
| Identificação e vigência | Versão, horizonte e identificação conforme documento real; arquivo/URL oficial | Conferir versão e acesso público. Não impor periodicidade, histórico, filtro, exportação ou data de atualização autônomos que C/S 10.5 não enumeram. |
| Marcação | Conteúdo documental real e schema esclarecido | Aplicar somente `planoEstrategico` (Anexo, 10.5.1) ao acesso/conteúdo existente. |

## Balancetes — C 10.6 / S 10.6

**Aplicabilidade confirmada:** a Cartilha p. 87 inclui expressamente a Previdência Estadual. A ressalva técnica S “apenas à Matriz II” não autoriza excluir 10.6. Esclarecer a correspondência da matriz sem suspender o levantamento do acervo.

| Requisito | Informação/documento faltante | Providência |
| --- | --- | --- |
| Conteúdo mensal | Balancetes oficiais com execução orçamentária e financeira mensal de receitas e despesas, por exercício/mês | Receber os documentos e conferir completude e período; não gerar balancetes a partir das tabelas de Receitas ou Despesas. |
| Atualidade | Último mês exigível, data real de publicação/atualização e cobertura | Confirmar com a contabilidade. Até 30 dias é recomendação C, sem prazo absoluto inventado. Não usar data de geração do modelo. |
| Histórico | Acervo mensal de pelo menos três anos anteriores à consulta | Conferir exercício e mês; não limitar aos exemplos S nem criar registros para períodos ausentes. |
| Formatos e assinaturas | PDF pesquisável quando adotado; versão oficial assinada preservada e editável correspondente sem assinaturas | Receber derivados adequados e conferir equivalência; não copiar a fonte privada nem presumir que PDF satisfaça a gravação editável. |
| Consulta e gravação | Dados dos períodos reais e conjunto exportável em pelo menos um formato editável | Ativar filtros por exercício/mês e exportação coerente com seleção. C também admite página única localizável por Ctrl+F. Não definir extensão ou empacotamento sem a fonte; não duplicar documentos no conjunto. |
| Marcações S | `balanceteMensal`, `filtroPesquisa`, `salvarRelatorio`, `dataUltimaAtualizacao`, `historicoExercicio` (10.6.1–10.6.5) | Aplicar somente em dados/ações reais; formato real em `serigyValue` da exportação. Confirmar o schema antes de ativar. |
| Divergências técnicas | Matriz II; descrições S 10.6.4/10.6.5 mencionam contratos; schemas diferentes nos exemplos | **DÚVIDA — REVISÃO NECESSÁRIA:** esclarecer representação com fonte técnica, sem alterar a aplicabilidade C nem importar regras de Contratos. |

Antes de publicar os dois novos modelos: obter arquivos/metadados, conferir conteúdo e acesso, resolver dúvidas técnicas, alimentar e marcar somente dados existentes; implementar os controles aplicáveis de Balancetes; testar documentos, formatos, recortes, histórico, HTML e acessibilidade. Não há declaração de inexistência ou atendimento. Os quatro HTMLs anteriores, `dist`, menus e deploy foram preservados.
