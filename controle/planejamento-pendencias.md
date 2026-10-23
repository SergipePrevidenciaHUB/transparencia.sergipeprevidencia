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


## Relatório de Gestão — conferências após alimentação de 10.2

A página de Relatório de Gestão foi alimentada com 2023, 2024 e 2025, exclusivamente a partir de `secoes.relatorioGestao` em `dados-entrada/planejamento/planejamento-prestacao-contas-consolidado.json`. Os três URLs permanecem literais. A atualização da relação no Portal é 21/10/2026, conforme referência fornecida; não comprova emissão ou atualização do conteúdo dos PDFs.

- **Conteúdo e integridade:** conferir cada PDF, sua correspondência ao exercício e à Unidade e a presença do relatório integral de gestão/atividades. Não se utilizou o título ou o nome do arquivo como prova de conteúdo finalístico.
- **Pesquisa de texto:** testar pesquisa, seleção e extração de texto nos três PDFs. Não foi feita auditoria dos seus inteiros teores ou pesquisabilidade nesta alimentação, nem se usou a expressão “PDF pesquisável” nos links públicos.
- **Disponibilidade externa:** conferir abertura pública de cada destino e estabilidade do endereço; a transcrição literal do índice não equivale a teste remoto de autenticidade/disponibilidade.
- **Histórico:** os três exercícios recebidos não homologam a série especial C 10.2 ou o conjunto completo. Confirmar eventual necessidade dos exercícios precedentes e obter os documentos pertinentes sem inventar links ou declarações de inexistência.
- **Schema:** esta página segue o contexto documental `planejamento-prestacao-contas.html` para os relatórios e os contextos `gestao-fiscal-planejamento.html` dos exemplos de pesquisa/atualização para esses controles. Conferir a extração no Serigy; não presumir equivalência global de schemas. A divergência original permanece registrada, sem alteração das outras páginas/modelos.

As reservas sem conteúdo desta página foram substituídas pelos três links reais e pela referência de atualização da relação. As pendências acima permanecem internas e não foram transformadas em declarações públicas de validação ou atendimento integral.


## Pendências após alimentação dos cinco índices de Planejamento

As páginas receberam os vínculos publicáveis do consolidado; não houve auditoria remota integral dos documentos. As pendências não foram apresentadas como avisos internos na interface e não equivalem a inexistência de documentos ou atendimento integral.

### Conteúdo, pesquisa e abrangência

- **10.1:** abrir as 16 prestações, confirmar exercício/unidade, inteiro teor e presença de Balanço Orçamentário, Financeiro, Patrimonial e Demonstrações das Variações Patrimoniais. Testar pesquisa/seleção de texto. Confirmar exigibilidade e série histórica; não há Balanço 2026 na fonte ou na página.
- **10.3:** conferir conteúdo, inteiro teor, correspondência ao exercício das contas e situação atual dos processos. Não inferir decisão pela pasta de upload, pelo título ou pela disponibilização de um resumo.
- **10.4:** conferir os 11 RGFs, emissor e consolidação que abrange a Unidade; confirmar todos os anexos obrigatórios efetivamente aplicáveis. A fonte oferece os quadrimestres 2023–2025 e 1º/2º de 2026; isso não homologa a completude, atualidade ou responsabilidade de emissão. C p. 85 prevê ressalva de não emissores/consolidação, sem dispensa presumida. Não criar novos demonstrativos obrigatórios a partir de exemplos.
- **10.5:** conferir no plano institucional objetivos estratégicos, indicadores, metas, versão e período. PPA/LDO/LOA e planos anuais são complementares; não substituem nem recebem `planoEstrategico`.
- **10.6:** abrir cada PDF e editável para confirmar competência, unidade, execução orçamentária/financeira e pesquisa de texto; conferir se a versão editável corresponde ao oficial e está sem assinaturas quando aplicável. Links individuais existentes permitem salvar os arquivos oferecidos; não se declara suprida a ausência de editáveis ou completa a gravação do acervo.

### Julgamentos de SergipePrevidência 2022 e 2023

O consolidado define `url: null` e fornece endereços somente para conferência. Esses endereços não foram vinculados às linhas 2022/2023. A tabela informa apenas “Documento ainda não disponibilizado nesta relação”, sem fabricar acórdão ou afirmar como confirmada a indicação de julgamento pendente da origem. Solicitar situação processual e decisão correta à área responsável. URLs que exigem conferência:
- 2023 — https://sergipeprevidencia.se.gov.br/wp-content/uploads/2024/04/2018-SERPREV-1-1.pdf
- 2022 — https://www.sergipeprevidencia.se.gov.br/wp-content/uploads/2021/11/governanca-acordao-prestacao-de-contas-sergipeprevidencia-2017.pdf

Caso um mesmo endereço seja fornecido para o exercício efetivo em outro registro do índice, sua utilização nesse contexto não o transforma em decisão de 2022/2023; conferir o conteúdo antes de homologar.

### Balancete de junho/2023 — SergipePrevidência

O PDF indicado no registro de junho aponta para arquivo identificado como agosto e repete o vínculo de agosto/2023:
https://sergipeprevidencia.se.gov.br/wp-content/uploads/2023/10/08-Balancete-Contabil-Consolidado-SERGIPE-Agosto-1.pdf

Esse PDF não é publicado como junho. O editável próprio de junho existente no JSON foi preservado, sem criar uma URL PDF a partir de seu nome:
https://sergipeprevidencia.se.gov.br/wp-content/uploads/2025/06/06-Balancete-Contabil-Consolidado-SERGIPE-Junho.docx

Solicitar o PDF correto de junho e conferir a correspondência com o editável. O PDF de agosto foi mantido apenas na linha agosto/2023 segundo a fonte, ainda sujeito à conferência de conteúdo. Nenhum período ou arquivo foi fabricado para preencher a lacuna.

### Editáveis ausentes na fonte — 20 períodos

Não foram criados links onde `editavel` é `null`. Obter os arquivos reais correspondentes às versões oficiais, sem assinaturas quando aplicável, e inserir os URLs na origem somente após conferência.

| Unidade | Exercício | Meses sem link editável |
| --- | --- | --- |
| FINANPREV | 2023 | 09, 10, 12 |
| FINANPREV | 2024 | 09, 10, 12 |
| FINANPREV | 2025 | 01, 08, 09 |
| SergipePrevidência | 2023 | 09, 10, 12 |
| SergipePrevidência | 2024 | 09, 10, 12 |
| SergipePrevidência | 2025 | 02, 08, 10, 11, 12 |

### URLs complementares e demais endereços suspeitos

- LDO: o parâmetro `RootFolder` aponta para LDO 2027; confirmar o destino pretendido.
- LOA: a página é `loa.aspx`, mas `RootFolder` também aponta para LDO 2027; confirmar/corrigir a origem após validação institucional.
- Os endereços completos de LDO e LOA estão preservados literalmente nos registros `planoEstrategico` do consolidado e nos links complementares da página. Não foram “corrigidos” por suposição nem marcados como plano institucional; não se atribuiu um exercício 2026 a esses materiais.
- Conferir disponibilidade remota, autenticidade, integridade e conteúdo de todos os outros URLs. Nomes de arquivo, uploads em exercício posterior e formatos aparentes não comprovam correspondência documental.

### Atualização, histórico e Serigy

21/10/2026 é a atualização das relações no Portal fornecida pelo responsável, não emissão dos PDFs nem comprovação de fechamento, completude ou homologação. Confirmar último período exigível e cobertura histórica de cada conjunto/unidade. Para 10.6, preservar aplicabilidade expressa à Previdência Estadual (C p. 87), sem exclusão baseada na ressalva Matriz II do S10. Conferir no Serigy os schemas documentais e os dos exemplos de filtro/atualização, bem como o caso do balancete com somente editável. RelatorioGestao foi preservado integralmente e suas pendências anteriores permanecem.

URLs complementares a conferir, transcritos do consolidado:

- Lei de Diretrizes Orçamentárias (LDO): `https://www.sefaz.se.gov.br/transparencia/SitePages/ldo.aspx?RootFolder=%2Ftransparencia%2FCiclo%20Oramentrio%2FLei%20de%20Diretrizes%20Or%C3%A7ament%C3%A1rias%20%E2%80%93%20LDO%2FLDO%202027&FolderCTID=0x012000FF756FE706E8044A912A97C105A91CDD&View=%7B21635CEF%2D6474%2D4790%2D951F%2DDA001AF7118F%7D`
- Lei Orçamentária Anual (LOA): `https://www.sefaz.se.gov.br/transparencia/SitePages/loa.aspx?RootFolder=%2Ftransparencia%2FCiclo%20Oramentrio%2FLei%20de%20Diretrizes%20Or%C3%A7ament%C3%A1rias%20%E2%80%93%20LDO%2FLDO%202027&FolderCTID=0x012000FF756FE706E8044A912A97C105A91CDD&View=%7BA4EBB1DE%2D05A5%2D442C%2DA1FE%2DFE890CA5EBF1%7D`


## Histórico — correções técnicas da avaliação 4172

Escopo desta rodada: somente Balanço Geral (S10 10.1.4), Relatório de Gestão (10.2.4) e Julgamento TCE (10.3.3). Não houve pesquisa institucional nem execução do Invoker. Documentos, URLs, linhas e datas existentes preservados integralmente.

O CSV 4172 atribuiu ponto=true a Balanço/Relatório, mas registrou INVALID_OPTION para 2026; TCE permaneceu ponto=false com WAITSECTION_NOT_FOUND. Os resultados originais foram mantidos nas três linhas da matriz.

Implementado: os três seletores historicoExercicio e seus botões apontam explicitamente, por serigyExecuteWaitSection, ao contêiner serigyLoadSection que engloba a tabela e a mensagem de recorte vazio. O formulário usa o schema do cabeçalho da dimensão, planejamento-prestacao-contas.html. A divergência dos exemplos (gestao-fiscal-planejamento.html) continua registrada; não foi usada para alterar as marcações/datas de atualização existentes. TCE não recebeu filtroPesquisa como nova exigência formal. Seleção, pesquisa, unidade quando existente e limpeza modificam efetivamente a consulta. Relatório passou a reutilizar planejamento.js; o controlador anterior não é mais associado ao formulário.

Balanço e Relatório agora permitem selecionar 2026 (value/serigyValue), apresentando “Documento ainda não disponível nesta relação para o exercício 2026.”, sem inserir linha, link, marca de documento ou declaração de inexistência institucional. Essa é uma opção técnica de consulta, não comprovação de acervo 2026. TCE mantém seus exercícios e as pendências anteriores de documentos, inclusive 2022/2023 do SergipePrevidência. Ausências em recortes por unidade também recebem mensagem explícita, sem documento artificial.

Pendências de conteúdo preservadas: recebimento/conferência de documentos ainda ausentes, inteiros teores, pesquisa de texto e cobertura; seleção 2026 não resolve essas pendências nem comprova exercício exigível ou atendimento integral. As alterações desta rodada são nos HTMLs e componente existente; geradores não foram alterados. Antes de uma regeneração, preservar/reincorporar esta estrutura para não perder as correções.

Testes em Chrome por HTTP local e cópia preparada com a base /transparencia.sergipeprevidencia: 252 verificações aprovadas, 260 referências HTTP, todas as opções, eventos change/submit, combinações com unidade, mensagens vazias, 2026 sem links e limpeza. Preservadas 16 linhas de Balanço, 3 de Relatório e 13 de TCE (estas incluem duas linhas de pendência, não 13 decisões). Índice Git preservado. Relatório em trabalho/planejamento-4172/resultado.json. Reavaliar os três itens no Invoker somente após publicação autorizada; testes locais não alteram a pontuação oficial.


## Histórico — opções de consulta da avaliação 4226

TCE / S10 10.3.3: INVALID_OPTION em 4226 porque o seletor começava em 2024 e não continha 2026 nem 2025. Acrescentadas somente opções value/serigyValue=2026/2025, sem linhas ou decisões novas. Schema planejamento-prestacao-contas.html, botão e seletor WaitSection=tabela-tce e resultado correspondente já estavam alinhados; planejamento.js já filtrava por change/submit e exibia mensagem por exercício nos recortes vazios. Preservadas 13 linhas (incluem duas pendências, não 13 decisões), URLs e data de atualização. Antes de regenerar a página, preservar as opções de consulta sem documento: elas não podem ser derivadas exclusivamente dos exercícios com arquivos.

Teste tools/testar_historicos_4226.py em Chrome/HTTP na cópia Pages: 22 verificações por página, exercícios 2026/2025/2024 aceitos, resultado observado alterado por exercício, confirmação estável na seleção repetida e submit, limpeza para todos, documentos e datas preservados. Não houve alteração dos scripts de filtro nem nova fonte institucional. Corrigido e testado localmente; reconhecimento pelo Invoker depende de publicação autorizada e nova avaliação.
