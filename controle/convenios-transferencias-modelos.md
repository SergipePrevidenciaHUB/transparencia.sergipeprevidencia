# Convênios e Transferências — correspondência dos modelos

## 1. Escopo, fontes e área não publicada

Somente critérios 5.1, 5.2 e 5.3, aplicáveis à Previdência Estadual. **C** indica exigência da Cartilha; **S** indica marcação/estrutura documentada no Serigy; **DT** indica escolha de implementação. Não há dados homologados nem declaração de atendimento.

Fontes lidas nesta tarefa: `AGENTS.md`; Cartilha PETP 2026 local, somente pp. 42–47 (5.1: 42–43; 5.2: 44–45; 5.3: 46–47); `referencias/serigy/5. Convênios e Transferências _ Serigy Docs.pdf`, pp. 1–3; somente fichas 5.1–5.3 de `controle/inventario-tabelas.md`. Foram inspecionados os componentes existentes do Portal e de Despesas, o preparador e o `.gitignore` para definir reaproveitamento e isolamento. Não houve pesquisa externa ou leitura de inteiros teores institucionais.

**DT:** modelos completos de página em `modelos/`, fora de `dist`, com o mesmo caminho relativo do destino futuro. A pasta é versionável e não está ignorada pelo Git. `tools/preparar_deploy.py` define `DIST = ROOT / "dist"` e copia somente essa origem para `_site`; `modelos/` e `controle/` não integram essa cópia. O preparador não foi alterado nem executado. Nenhum link foi acrescentado ao menu, mapa ou manifesto públicos.

## 2. Caminhos confirmados

O prefixo `[Portal da Transparencia]` de S corresponde, neste projeto, a `/Portal-da-Transparencia/`. Preservar caixa e grafia dos segmentos de S; não criar `ConveniosTransferencias` como substituto.

| Critério / fonte | Seção S | Caminho S literal após o prefixo | Modelo versionável | Destino futuro, ainda não criado |
| --- | --- | --- | --- | --- |
| 5.1 / C pp. 42–43; S p. 1 | 5.1. Transferências Recebidas | `Convenios/Recebidas` | `modelos/Portal-da-Transparencia/Convenios/Recebidas/index.html` | `dist/Portal-da-Transparencia/Convenios/Recebidas/index.html` |
| 5.2 / C pp. 44–45; S p. 1 | 5.2. Transferências Realizadas | `Convenios/Realizadas` | `modelos/Portal-da-Transparencia/Convenios/Realizadas/index.html` | `dist/Portal-da-Transparencia/Convenios/Realizadas/index.html` |
| 5.3 / C pp. 46–47; S p. 1 | 5.3. Acordos Sem Transferência | `Convenios/SemTransferencia` | `modelos/Portal-da-Transparencia/Convenios/SemTransferencia/index.html` | `dist/Portal-da-Transparencia/Convenios/SemTransferencia/index.html` |

Schema comum, confirmado em S p. 1: `https://serigy.tce.se.gov.br/comum/convenios-transferencias.html`. Está no `main` dos três modelos como contexto, sem itens de dados em campos vazios.

## 3. Estrutura e campos por página

**DT:** tabela de instrumentos com resumo completo e acesso ao inteiro teor na mesma linha. A Cartilha admite consulta detalhada na mesma seção; não impõe tabela HTML universal. Os exemplos S usam linhas associadas por instrumento (p. 2), o que fundamenta esta escolha. Não criar tabela de valores para acordos sem recursos, nem substituir resumos por lista genérica de PDFs.

Cada `tbody` está vazio, sem linhas ou células fictícias. As posições abaixo são reservas para futuras células reais; **nenhum desses `serigyItem` foi aplicado a cabeçalhos, células vazias, controles desativados ou contêineres vazios**. A navegação, busca geral e acessibilidade preservam suas marcações existentes porque são componentes reais.

### 3.1. Transferências Recebidas — 5.1

Somente transferências voluntárias recebidas por convênios/termos/ajustes e instrumentos equivalentes. Não incluir transferências legais/constitucionais como se fossem convênios. C exige o resumo legível sem abrir o instrumento (pp. 42–43).

| Coluna futura de `#tabela-recebidas` | Conteúdo C | Item S / `serigyItem` futuro | Tipo S |
| --- | --- | --- | --- |
| 1 | Número/ano do instrumento | 5.1.1 `identificaTransferencia` | Número/Ano |
| 2 | Órgão/Poder repassador ou concedente | 5.1.2 `orgaoRepassador` | Texto |
| 3 | Objeto | 5.1.4 `objetoConvenio` | Texto |
| 4 | Vigência real do instrumento | 5.1.3 `vigenciaConvenio` | Ano; divergência no exemplo |
| 5 | Valor total previsto do instrumento | 5.1.5 `valorTotalPrevisto` | Monetário |
| 6 | Valor recebido / valores já repassados à Unidade | 5.1.6 `valorRepassado` | Monetário |
| 7 | Inteiro teor do convênio/termo/ajuste | 5.1.7 `anexoConvenio` | Anexo |

**Documento:** link direto conferido para cada instrumento integral, associado ao mesmo registro. Valores previstos e recebidos são medidas distintas. Vários recebimentos de um instrumento não autorizam repetir o valor total para cada movimento e somar tudo como novos convênios.

### 3.2. Transferências Realizadas — 5.2

Consulta separada e autônoma das recebidas, conforme C p. 45. Abrange repasses voluntários sem natureza contratual, inclusive os tipos pertinentes enumerados em C p. 44; não importar contratos de fornecimento como convênios.

| Coluna futura de `#tabela-realizadas` | Conteúdo C | Item S / `serigyItem` futuro | Tipo S |
| --- | --- | --- | --- |
| 1 | Número/ano do instrumento | 5.2.1 `identificaTransferencia` | Número/Ano |
| 2 | Nome do beneficiário | 5.2.2 `orgaoBeneficiario` | Texto |
| 3 | Objeto do convênio/repasse | 5.2.4 `objetoConvenio` | Texto |
| 4 | Vigência real | 5.2.3 `vigenciaConvenio` | Ano; divergência no exemplo |
| 5 | Valor total previsto para repasse | 5.2.5 `valorTotalRepasse` | Monetário |
| 6 | Valor concedido / já repassado conforme a fonte | 5.2.6 `valorRepassado` | Monetário |
| 7 | Inteiro teor do instrumento | 5.2.7 `anexoConvenio` | Anexo |

**Documento:** convênio/termo/ajuste integral. Confirmar o significado dos valores e a referência de apuração com a instituição. O nome S `orgaoBeneficiario` não restringe os beneficiários a órgãos: C menciona Unidade/pessoa física ou jurídica. Não adicionar CPF/CNPJ como mínimo obrigatório inexistente nestas fontes.

### 3.3. Acordos Sem Transferência — 5.3

Acordos em que não haja recebimento nem transferência de recursos financeiros (C p. 46). Resumo das partes e obrigações associado ao instrumento. Não preencher colunas financeiras com zero para simular acordo sem recursos.

| Coluna futura de `#tabela-sem-transferencia` | Conteúdo C | Item S / `serigyItem` futuro | Tipo S |
| --- | --- | --- | --- |
| 1 | Número/ano do acordo/termo/ajuste | 5.3.1 `identificaAcordo` | Número/Ano |
| 2 | Todas as partes participantes | 5.3.2 `participante` | Texto |
| 3 | Objeto | 5.3.4 `objetoConvenio` | Texto |
| 4 | Vigência real | 5.3.3 `vigenciaConvenio` | Ano; divergência no exemplo |
| 5 | Obrigações ajustadas | 5.3.5 `obrigacoes` | Texto |
| 6 | Inteiro teor do instrumento | 5.3.6 `anexoConvenio` | Anexo |

**Documento:** acordo/termo/ajuste integral. As obrigações estão no título oficial de C p. 46 e em S; sua ausência na enumeração do corpo de C não autoriza omiti-las. **DT:** resumo textual das obrigações na coluna; informações adicionais podem ficar em detalhe associado, sem transcrever documentos inteiros obrigatoriamente. S p. 2 exemplifica acesso documental às obrigações, mas tipa a propriedade como Texto: validar a apresentação efetiva sem omitir o resumo exigido.

## 4. Correspondência dos controles e aplicação futura das marcações

As regras C abaixo se aplicam a **cada uma** das páginas. As fontes são C pp. 43, 45 e 47 e S pp. 1–3. Controles só receberão marcação funcional quando operarem sobre dados oficiais: hoje estão desativados e não há JS de consulta/exportação específico. `site.js` mantém apenas os recursos gerais do Portal.

| Requisito | Recebidas / S | Realizadas / S | Sem Transferência / S | Aplicação futura, somente com conteúdo funcional |
| --- | --- | --- | --- | --- |
| Filtro mínimo C: exercício/ano | 5.1.8 `filtroPesquisa`; `#filtro-recebidas` | 5.2.8 `filtroPesquisa`; `#filtro-realizadas` | 5.3.7 `filtroPesquisa`; `#filtro-sem-transferencia` | Marcar o formulário com `serigyItem="filtroPesquisa"` após implementar a consulta autônoma. Não exigir outros filtros como obrigação C. |
| Histórico: ao menos os três anos que antecedem ao da consulta | 5.1.11 `historicoExercicio`; `#exercicio-recebidas` | 5.2.11 `historicoExercicio`; `#exercicio-realizadas` | 5.3.10 `historicoExercicio`; `#exercicio-sem-transferencia` | Marcar o seletor com `serigyItem="historicoExercicio"` e cada opção real com `serigyValue` do exercício correspondente. Os anos exemplificados em S não limitam a cobertura C. Não criar opções de anos sem fonte. |
| Exportar o conjunto selecionado em pelo menos um formato editável | 5.1.9 `salvarRelatorio`; `#exportar-recebidas` | 5.2.9 `salvarRelatorio`; `#exportar-realizadas` | 5.3.8 `salvarRelatorio`; `#exportar-sem-transferencia` | `serigyItem="salvarRelatorio"` e `serigyValue` do formato realmente gerado. **DT a implementar:** CSV ou outro editável aprovado. O PDF do exemplo S não substitui o editável C. Exportar todos os mínimos, inclusive os que futuramente ficarem em detalhe. |
| Atualidade: informações mais recentes de até 30 dias anteriores à consulta | 5.1.10 `dataUltimaAtualizacao`; `#atualizacao-recebidas` | 5.2.10 `dataUltimaAtualizacao`; `#atualizacao-realizadas` | 5.3.9 `dataUltimaAtualizacao`; `#atualizacao-sem-transferencia` | Preencher o contêiner com a data real do conjunto e só então aplicar `serigyItem="dataUltimaAtualizacao"`. S p. 3 distingue atualização e cobertura (“dados até”); confirmar ambas, sem criar novo item ou preencher com a data de geração. |

**Associação de carregamento (S pp. 1–2):** na ação de pesquisar, `serigyExecuteWaitSection` deve ter o mesmo valor do `serigyLoadSection` no contêiner dos resultados. Reservas por página: `#pesquisar-recebidas` → `#resultados-recebidas`, valor `resultados-recebidas`; `#pesquisar-realizadas` → `#resultados-realizadas`, valor `resultados-realizadas`; `#pesquisar-sem-transferencia` → `#resultados-sem-transferencia`, valor `resultados-sem-transferencia`. Esses IDs são DT do componente real; não são novos itens. A estrutura atual possui os IDs, mas não anuncia carregamento inexistente.

**Documentos (S p. 2):** reservar a célula do instrumento para `serigyItem="anexoConvenio"`, com links reais identificados dentro dela, como no exemplo S. Se houver vários arquivos integrantes, mantê-los em lista na mesma célula ou detalhe associado. O WordPress oficial pode continuar sendo o repositório; qualquer URL absoluta precisa ser fornecida/descoberta e conferida por documento. Não construir URLs pelo número do instrumento, não colocar `href="#"`, não usar `serigyLink` para PDF e não copiar exemplos de S como dados institucionais.

**Disponibilidade:** todos os elementos mínimos devem ser visíveis no resumo ou em detalhe da mesma seção. Exportação deve preservar o conjunto selecionado, sem repetir o valor total por movimento. Os tipos `N/A` dos controles S não indicam inaplicabilidade da Previdência.

## 5. Divergências e limites preservados

1. **Vigência — DÚVIDA — REVISÃO NECESSÁRIA:** S p. 1 tipa `vigenciaConvenio` como Ano e S p. 2 exemplifica uma data; C exige vigência. Preservar o período real informado pelo instrumento. Confirmar representação técnica antes de marcar; não reduzir a vigência ao ano nem inventar data final.
2. **Exemplos incompletos:** o exemplo de Realizadas não exibe vigência/anexo, e o exemplo de Sem Transferência não exibe vigência. As tabelas normativas de S e a Cartilha os exigem. Os modelos incluem esses campos.
3. **Obrigações:** mantidas em 5.3 por estarem no título C e na propriedade S, mesmo não repetidas na lista do corpo de C.
4. **Ausência de fatos:** não confundir falta de dados com inexistência de instrumentos. C pp. 43/45/47 admite declaração expressa verdadeira por período, com atualização. Em 5.3, C p. 47 exige também informação de não ocorrência nos anos anteriores. Não foi produzida nenhuma declaração, nem atribuído `serigyEmpty` a ausência desconhecida.

## 6. Condições para mover os modelos para dist

Os modelos **não estão prontos para publicação**. As pendências específicas estão em `controle/convenios-transferencias-pendencias.md`.

Para cada página: receber e conferir registros e inteiros teores; delimitar os exercícios reais e a cobertura histórica; esclarecer vigência; obter referências reais de atualização/cobertura; inserir linhas associadas e marcações somente nos dados existentes; implementar e testar filtro, histórico e exportação do mesmo recorte. Se houver não ocorrência, somente a instituição pode confirmar o período e a declaração pertinente, conforme C. Nada pode ser presumido de tabela vazia.

Depois, em tarefa de publicação autorizada, copiar somente a página e seus arquivos públicos necessários para o destino correspondente de `dist`, sem levar controles internos ou fontes privadas. Atualizar navegação/mapa/manifesto apenas quando as páginas tiverem conteúdo publicável. Executar o validador do protótipo e testar por HTTP local a navegação, os documentos, filtros e exportação. Não declarar o critério integralmente atendido pela simples movimentação do arquivo.

## 7. Validação deste recorte

Verificação estrutural dos três HTMLs: idioma, cabeçalho/rodapé, IDs e rótulos, integridade de tags e tabelas, ausência de registros fictícios, controles desativados, ausência de itens S de dados em campos vazios, links/recursos existentes no `dist` para o destino futuro. Caminhos e propriedades confrontados com S5 e C 5.1–5.3. Conferidos isolamento fora de `dist`, exclusão pelo preparador e ausência de ignore dos cinco arquivos novos. A conferência inclui `git diff --check` e preservação por hash dos arquivos preexistentes de Receitas, navegação, CSS/JS compartilhados e preparador. O preparador não foi executado; nenhuma página pública foi alterada.
