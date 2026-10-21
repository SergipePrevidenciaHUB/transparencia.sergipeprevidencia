# Licitações — pendências dos modelos

Escopo dos controles: C 8.1–8.7 / S 8.1–8.3. Mapeamento em `controle/licitacoes-modelos.md`. Não há dados ou documentos institucionais homologados nos modelos. As pendências originais de C 8.1–8.5 são preservadas abaixo; o HTML principal permanece inalterado.

## Modelo principal — C 8.1–8.5 / S 8.1

| Seção / requisito | Dado ou documento faltante | Providência |
| --- | --- | --- |
| Relação — C 8.1 | Catálogo real de licitações em andamento e encerradas, dispensas e inexigibilidades pertinentes; número/ano, modalidade, objeto, abertura, valor e situação | Receber fonte oficial e confirmar universo e exceção das compras diretas de pequeno valor, sem assumir que a autarquia não licita. |
| Ordem e identidade — C 8.1 / S `sequencia` | Regra de ordenação numérica e chave inequívoca entre procedimentos, anos/modalidades e documentos | Confirmar números repetidos e ordenação; não usar ordinal como número do certame nem colapsar registros por número isolado. Chave interna é DT, não novo item S. |
| Data e filtro — C 8.1 | Data real de abertura e referência de mês/ano para diretas sem sessão | Esclarecer com a área a apresentação desses casos; não inventar abertura, usar data de arquivo como fato ou marcar data desconhecida como disponível. |
| Valor e situação — C 8.1 | Valor estimado ou homologado devidamente identificado, situação real e referência | Confirmar conceitos e atualizações; não deduzir homologação da presença de arquivo nem substituir ausência por zero. S tipa data como Texto e valor como Número: não criar tipos/propriedades extras. |
| Editais — C 8.2 / S `editalLicitacao` | Íntegras e anexos integrantes dos certames em andamento e encerrados | Conferir documento por procedimento e acesso público direto. Ementa ou link à capa do PNCP não basta. |
| Fases — C 8.3 / S `docFasesLicitacao` | TR/projeto/equivalente, justificativa, pareceres, orçamento/preço, edital/anexos, atas, recursos/impugnações e análises quando houver, adjudicação/homologação | Inventariar por fase/documento e apontar quais existem ou estão em outro documento; conferir íntegra e pesquisa/seleção de texto. Não inventar etapas nem declarar inexistência por arquivo ausente. |
| Diretas — C 8.4 / S `docDispensaLicitacao` | TR/projeto/equivalente, justificativa de fornecedor/preço, caracterização da emergência/calamidade/risco e pareceres quando cabíveis, homologação/ratificação | Confirmar regime e alcance da ressalva de pequeno valor; não aplicá-la a toda contratação direta. Conferir pesquisa/seleção de texto ou valor e vínculos externos admitidos. |
| Adesões — C 8.5 / S `atasLicitacao` | Atas integrais das adesões realmente realizadas e referência ao procedimento | Confirmar que o documento é de adesão da Unidade, não apenas ata geral SRP. Não presumir adesão por contrato semelhante. |
| Histórico — C 8.1–8.5 | Acervo de pelo menos três anos anteriores ao da consulta, inclusive os documentos de cada grupo | Conferir cobertura por critério; publicar documentos reais sem preencher anos com fatos fictícios. Esclarecer lacunas e eventual não ocorrência com a instituição. |
| Filtros — C 8.1–8.5 / S `filtroPesquisa` | Opções reais de ano, mês, situação e modalidade e identificação dos documentos associados | Implementar recortes combináveis da relação e localização dos documentos; não transformar filtros mínimos de 8.1 em parâmetros normativos novos para 8.2–8.5. |
| Exportação — somente C 8.1 / S `salvarRelatorio` | Arquivo editável do recorte com todos os mínimos | Implementar ao menos um formato; evitar multiplicar procedimentos/valores pelo número de anexos. Downloads dos documentos continuam próprios, não substituídos pela exportação do resumo. |
| Atualização — C 8.1–8.5 / S `dataUltimaAtualizacao` | Datas reais, coberturas e responsáveis da relação e de cada grupo documental | Conferir o parâmetro de até 30 dias separadamente; não usar geração/importação nem uma data do resumo para todo o acervo. |
| Associação, documentos e dados pessoais | Chave procedimento–documento; versões oficiais adequadas e URLs conferidas | Validar correspondência, íntegra, legibilidade e acesso sem login. Não publicar arquivos privados/credenciais ou dados pessoais adicionais por cópia bruta. Não construir URLs ou usar `serigyLink` para PDF. |

Antes de mover para `dist`: resolver as pendências pertinentes, receber e conferir dados/documentos, implementar controles e vínculo por registro, preencher datas e só então marcar conteúdo real. A tabela e as listas vazias atuais não comprovam não ocorrência nem atendimento. O modelo não foi adicionado ao menu público; nenhuma comunicação externa foi enviada.


## PlanoAnualContratacoes — C 8.6 / S 8.2

| Requisito | Dado/documento necessário | Providência antes da publicação |
| --- | --- | --- |
| Plano consultável | PCA oficial do exercício atual, completo e com eventuais anexos integrantes confirmados | Obter o arquivo ou URL direta conferida; validar Unidade, exercício e versão com a área responsável. Não criar plano ou itens de contratação sem fonte. |
| Atualidade C / S `dataUltimaAtualizacao` | Exercício do plano e data real de atualização/cobertura | Conferir que é o PCA do exercício exigido. Data de geração/upload não substitui a referência real nem torna um plano antigo atual. |
| Documento / S `contratacoesAnual` | Arquivo/URL pública correspondente, sem login | Conferir destino e íntegra; não construir URL ou usar `serigyLink` para PDF. Identificar versões/anexos sem inventá-los. |
| Ausência de PCA | Esclarecimento institucional se o plano não for disponibilizado | Registrar a lacuna: C p. 72 rejeita declaração de inexistência/não elaboração como atendimento. Não publicar declaração fictícia nem marcar o critério como atendido por ausência. |
| Controles | Nenhuma exigência própria de filtro, histórico ou exportação em C 8.6 / S 8.2 | Preservar a apresentação documental; não copiar controles de Sanções/listagem como obrigações do PCA. |

## Sancoes — C 8.7 / S 8.3

| Requisito | Dado/arquivo necessário | Providência antes da publicação |
| --- | --- | --- |
| Universo de sanções / S `nomeSancionado` | Relação oficial dos licitantes/contratados sancionados pela Unidade nas hipóteses indicadas em C p. 73 | Confirmar autoria e enquadramento com a área responsável. Não importar indiscriminadamente registros de outros órgãos nem copiar nomes S. |
| Identificação adicional S `idSancionado` | CNPJ/CPF confiável e versão publicável, associada ao mesmo sancionado | **DÚVIDA — REVISÃO NECESSÁRIA:** confirmar origem e tratamento com a instituição; não inventar identificação ou máscara. C exige mínimo nominal; S acrescenta a identificação. Não publicar cadastro bruto com informações pessoais adicionais. |
| Histórico / S `historicoExercicio` | Acervo de pelo menos três anos anteriores ao da consulta e referência temporal das ocorrências | Definir com a fonte como representar sanções, alterações e recortes anuais sem repetir dados por cópias de arquivos ou deduzir vigência. Popular somente exercícios reais. |
| Filtro / S `filtroPesquisa` | Registros reais e parâmetros DT de nome/exercício | Implementar consulta do conjunto; C não enumera filtros mínimos específicos neste critério. Não exigir CPF conhecido pelo visitante nem copiar filtros de modalidade/situação da listagem. |
| Gravação / S `salvarRelatorio` | Editável ou PDF pesquisável correspondente ao conjunto selecionado | Implementar pelo menos uma alternativa aceita em C p. 74, incluindo os campos publicáveis confirmados. Não anunciar recorte para download estático sem correspondência. |
| Atualidade / S `dataUltimaAtualizacao` | Data real da relação, cobertura e responsável | Confirmar o parâmetro de até 30 dias; não usar a data de importação/geração. |
| Documentos de origem | Evidência oficial para conferência dos registros quando necessária | Obter apoio da área sem transformar ato sancionatório integral em anexo mínimo não enumerado em C 8.7. Não criar documento/URL fictício para preencher a relação. |
| Eventual não ocorrência | Confirmação institucional do período sem sanções, se verdadeira | Não inferir inexistência a partir da tabela/arquivo ausente nem publicar nomes substitutos. Nenhuma declaração foi inserida no modelo. |

PCA e Sanções permanecem fora de `dist`, sem links novos no menu público. Liberar cada página somente após receber e conferir suas fontes, preencher referências reais e implementar os controles aplicáveis, sem atribuir marcações de dados a posições vazias. O modelo principal, Diárias e o deploy não são alterados por este complemento.
