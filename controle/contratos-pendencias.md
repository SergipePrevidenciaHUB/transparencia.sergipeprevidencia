# Contratos — pendências dos modelos

Escopo: C 9.1–9.4 / S 9.1–9.3. Mapeamento em `controle/contratos-modelos.md`. As pendências originais da consulta principal são preservadas; Fiscais e Ordem Cronológica são complementados abaixo.

## Consulta principal — C 9.1–9.2

As fontes devem vir das áreas responsáveis, sem dados de exemplo ou declaração de inexistência presumida.

| Seção / requisito | Informação ou arquivo necessário | Providência antes da publicação |
| --- | --- | --- |
| Relação e ordem — C 9.1 / S `numeroContrato`, `sequencia` | Cadastro oficial de contratos, identificação e ordenação sequencial | Conferir universo e números repetidos entre anos/séries. Preservar número como texto e definir ordenação sem transformar posição na identificação do contrato. |
| Resumo — C 9.1 / S `contratado`, `valorContrato`, `objeto`, `inicioContrato`, `fimContrato` | Contratado, valor, objeto e início/fim da vigência, provenientes da fonte | Validar conteúdo e significado dos valores. Não preencher nome, objeto, zero ou datas para completar campos; esclarecer informações faltantes ou eventuais vigências sem termo final. |
| Aditivos — C 9.1 / S `termoAditivo` | Relação dos aditivos efetivamente celebrados, contexto e efeitos documentados | Confirmar vínculo e apresentação do resumo; não presumir aditivo nem sua ausência por falta de arquivo. Definir como distinguir valor original e efeitos reais sem duplicar valores ou inventar colunas normativas. |
| Íntegra do contrato — C 9.2 / S `linkContrato` | Arquivo oficial integral ou URL direta conferida de cada contrato | Conferir identificação, versão e acesso sem login. Resumo/ementa não substitui o documento. Não deduzir URL pelo número do contrato. |
| Íntegra dos aditivos — C 9.2 / S `termoAditivo` | Cada instrumento integral, quando existente, associado ao mesmo contrato | Conferir correspondência e completude; não copiar caminhos de exemplo S ou associar apenas por semelhança de número/nome de arquivo. |
| Associação técnica — DT | Referência estável contrato–aditivo–documento e, se necessário, identificador interno | Evitar junções que gerem um contrato por documento. Não tornar identificador privado nova coluna pública obrigatória nem criar novos `serigyItem`. |
| Filtro de período — C 9.1 / S `filtroPesquisa` | Referência temporal que deve governar início/fim do recorte | Confirmar com a área se corresponde a celebração, vigência ou outro conceito. Não usar datas de upload ou supor igualdade com início/fim de vigência. Validar intervalos e combinação com exercício quando implementar. |
| Consulta documental — C 9.2 | Localização dos documentos pelos contratos do recorte | Implementar associação clara da linha ao detalhe e aos arquivos. C exige filtro genérico, sem parâmetros mínimos enumerados próprios; não copiar filtros de outra dimensão. |
| Histórico — C 9.1 e 9.2 / S `historicoExercicio` | Cadastro e documentos dos pelo menos três anos anteriores à consulta; referência dos exercícios | Conferir cobertura da relação e dos inteiros teores, sem limitar acervo aos exemplos S ou inventar registros para anos ausentes. |
| Gravação — C 9.1 / S `salvarRelatorio` | Pelo menos um formato editável do conjunto selecionado, com mínimos e associação aos aditivos | Implementar exportação coerente com os filtros, sem multiplicar o valor integral por termo/documento. Não confundir download de contrato com gravação editável da relação; C 9.2 não exige exportação autônoma. |
| Atualidade — C 9.1 e 9.2 / S `dataUltimaAtualizacao` | Datas reais, cobertura e responsável da relação e dos documentos | Confirmar o parâmetro de até 30 dias; não usar data de geração ou supor que uma referência do cadastro cubra todos os documentos. |
| Arquivos e dados pessoais | Versões oficiais adequadas à divulgação e derivados públicos necessários | Conferir conteúdo com a instituição; não publicar credenciais, dados privados ou planilha de origem indiscriminadamente. Não acrescentar CPF/CNPJ, contatos ou dados bancários como campos mínimos que estas fontes não enumeram. |

O HTML tem somente cabeçalhos de tabela, listas documentais vazias e controles desativados. Alimentar com dados reais e aplicar marcações após resolver as pendências; depois testar documentos, filtros, histórico, exportação e acessibilidade antes de mover para `dist`. O menu público e o deploy permanecem inalterados. Nenhuma comunicação externa foi enviada.


## GestoresFiscais — C 9.3 / S 9.2

| Requisito | Informação/arquivo faltante | Providência |
| --- | --- | --- |
| Relação autônoma | Nomes oficiais dos fiscais e identificação dos contratos vigentes e encerrados pelos quais respondem | Obter cadastro validado e cobertura, sem restringir aos contratos atuais ou ao detalhe de cada contrato. S diz fiscal/gestor, mas C exige fiscais: confirmar funções, não presumir equivalência. |
| Associação e temporalidade | Referência fiscal–contrato e mudanças/substituições efetivamente existentes | Definir granularidade DT e exercício de referência com a área; não deduzir por homônimos nem duplicar associações por cópias de arquivos. |
| Histórico e atualidade | Acervo de pelo menos três anos anteriores à consulta; data real, cobertura e responsável | Conferir parâmetro de até 30 dias e população incluindo contratos encerrados. Não usar data do HTML nem inventar exercícios sem fonte. |
| Filtro e gravação | Dados reais para seletor de exercício/busca e arquivo do recorte | Implementar o filtro DT e ao menos um editável ou PDF pesquisável aceito por C 9.3. Não anunciar exportação filtrada para arquivo estático que não segue a consulta. |
| Fonte documental e dados pessoais | Evidência funcional necessária para validar os vínculos e derivados publicáveis | Portaria de designação integral não é anexo mínimo deste critério. Não acrescentar CPF, salário ou contatos privados por cópia de cadastro bruto; não ocultar os nomes exigidos nem criar acesso restrito. |

## OrdemCronologica — C 9.4 / S 9.3

| Requisito | Informação/documento faltante | Providência |
| --- | --- | --- |
| Ordem oficial por grupos | Créditos e sua ordem real por fonte dos recursos e categorias de bens, locações, serviços e obras | Obter a fonte validada e a regra de ordenação. Não produzir a fila apenas ordenando pagamentos nem misturar fontes/categorias como uma ordem única. |
| Identificação dos créditos | Credor, valor, vencimento, pagamento e referência interna confiável para associação | Confirmar granularidade, pagamentos parciais/estornos ou créditos não pagos se existentes. Chave interna é DT, não nova coluna pública obrigatória. Não preencher valores ou datas ausentes por suposição. |
| Vencimento | Regulamentação/fato que define a exigibilidade e datas da origem | C menciona regra local e alternativas de liquidação/emissão de nota fiscal; confirmar qual se aplica. Não escolher automaticamente uma alternativa ou usar data do arquivo. |
| Fonte/categoria/justificativa sem item S | Identificações reais e fundamento de cada alteração da ordem | Exibir o conteúdo C em HTML, sem inventar `serigyItem`. A tabela S com quatro campos não dispensa essas informações. |
| Alterações e documentos | Justificativas reais da autoridade responsável, vinculadas ao crédito/grupo, com documentos se utilizados | Obter a explicação e evidências pertinentes; conferir acesso e correspondência. Não criar justificativa-padrão ou declarar ausência de alterações a partir de lacuna. Não usar `serigyLink` para PDF. |
| Publicação mensal e histórico | Listas dos meses reais de referência e acervo de pelo menos três anos anteriores à consulta | Definir cobertura e se listas da fonte são posições cumulativas ou movimentos; não somar novamente créditos repetidos em vários meses. Não inventar meses ausentes ou fechamento. |
| Filtro e exportação | Exercício/mês/fontes/categorias reais e derivado editável do conjunto | Implementar escolhas DT sem tratá-las como filtros mínimos enumerados C. Preservar ordem, grupos e fundamentos na exportação, sem duplicar por anexo ou repetição mensal; PDF sozinho não atende a gravação em 9.4. |
| Atualização | Referência real de atualização/cobertura e responsável | Conferir publicação mensal e parâmetro de até 30 dias, sem preencher com a data de geração. A ressalva nominal ao Banese não se aplica automaticamente à Previdência Estadual. |
| Arquivos de origem | Derivados públicos adequados e URLs oficiais conferidas, quando usados documentos | Não publicar planilhas privadas, dados bancários/credenciais ou campos pessoais adicionais por conveniência. Não inventar normas, links ou documentos para completar o modelo. |

Ambos os modelos continuam fora de `dist`, com dados vazios e controles desativados. Antes de publicar: receber e conferir fontes, resolver referências temporais e associações, alimentar dados/documentos e datas reais, implementar filtros/gravações aplicáveis e só então aplicar marcações e validar. O modelo principal, outras seções, menu e deploy permanecem inalterados; nenhuma comunicação externa foi enviada.
