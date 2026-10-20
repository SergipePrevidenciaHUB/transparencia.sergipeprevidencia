# Filtro por Unidade Orçamentária — ativação futura

## Situação

`dist/assets/js/filtro-uo.js` fornece o predicado reutilizável; `tabelas.js` o combina, opcionalmente, com ano, mês, tipo e palavra-chave. O componente não foi ativado nas páginas: os exemplos de Receitas não têm UO confirmada, e Despesas ainda não tem registros nem tabela. Nenhuma UO foi atribuída aos exemplos existentes. As páginas, os layouts de controle e os importadores permanecem intactos.

O filtro somente seleciona linhas e atualiza a contagem de registros. Não soma valores, consolida, deduplica, altera células, cria registros ou remove linhas do HTML/DOM. Sem `data-uo-filter`, mantém o comportamento anterior das tabelas, sem depender do novo módulo.

## Contrato

- Cada linha oficial precisa de `data-codigo-uo` com o `codigo_uo` confirmado e de `data-uo-confirmada="true"`. São atributos técnicos, não marcações Serigy nem novas colunas dos layouts.
- A confirmação é feita na origem antes da publicação. O JavaScript não valida a verdade contábil: apenas exige confirmação explícita, código textual de cinco dígitos e presença na lista de UOs permitidas da consulta.
- “Todas as unidades” usa valor vazio no seletor e inclui apenas linhas confirmadas das UOs permitidas. Não é código de UO, registro financeiro ou total adicional.
- Linhas sem confirmação, com código ausente, malformado ou fora do escopo não entram no recorte por UO, inclusive em “Todas”. Não inferir a unidade por nome, valor ou posição da linha nem assumir 37201 como padrão.
- As linhas continuam no HTML original para leitura automatizada. A seleção apenas combina o atributo `hidden` com os demais filtros existentes. Com JavaScript desabilitado, o HTML permanece disponível sem filtragem interativa.

## Ativação após a importação dos registros oficiais

1. Validar a UO de cada registro na fonte e resolver as pendências de cobertura antes de apresentar a listagem como completa. Não ativar sobre os dados fictícios atuais. Os atributos de confirmação não substituem essa revisão.
2. Manter no HTML todas as linhas oficiais, seus atributos de ano/mês usados por `tabelas.js` e suas marcações Serigy. Acrescentar os dois atributos de UO às linhas confirmadas e uma célula visível com código e nome da unidade. Não colocar exemplos fictícios em `dist` para habilitar o componente.
3. Carregar os scripts abaixo, nessa ordem, com `defer`. Nas páginas sem tabela, só adicionar `tabelas.js` quando houver tabela real e formulário associado. Os caminhos seguem o padrão atual de recursos do Portal; nenhum ajuste de deploy foi feito.

```html
<script defer src="/assets/js/filtro-uo.js"></script>
<script defer src="/assets/js/tabelas.js"></script>
```

4. No mesmo formulário já identificado por `data-table-filter` e `data-target`, acrescentar `data-uo-codes="37201 37401 37403"` para Receitas ou `data-uo-codes="37201 37202 37401 37403"` para Despesas. Não criar outro controlador independente da mesma tabela.
5. Acrescentar ao formulário um campo com a classe existente `field`, rótulo associado e um `select` com `name="codigo_uo"` e `data-uo-filter`. A opção inicial e padrão “Todas as unidades” deve ter `value=""`; as opções específicas usam os códigos e nomes da tabela abaixo. Não criar `serigyItem` próprio para o seletor: ele é decisão técnica adicional aos filtros documentados.
6. Manter os botões de pesquisa/limpeza e a contagem com `data-count-for`. Mudar a UO aplica todos os campos conjuntamente; pesquisar continua funcionando, e limpar retorna aos padrões do formulário, incluindo “Todas”. Não há um segundo filtro que reexiba uma linha excluída por ano, mês, tipo ou palavra-chave.
7. Informar junto da consulta: “A consulta lista registros por unidade. Não apresenta total consolidado.” Havendo linhas sem UO confirmada, explicar que elas não entram nessa consulta e resolver a pendência institucional; não ocultar a limitação atrás do rótulo “Todas”.
8. Tratar a exportação em tarefa própria. O componente não modifica os downloads estáticos existentes. A futura exportação deve corresponder ao recorte e preservar a UO por registro, sem misturar consolidados e componentes.

| Código | Nome da opção | Receitas | Despesas |
| --- | --- | --- | --- |
| 37201 | SergipePrevidência | Sim | Sim |
| 37202 | SPSM | Não | Sim |
| 37401 | FINANPREV | Sim | Sim |
| 37403 | FUNPREV | Sim | Sim |

Em Receitas, SPSM permanece registrado em 37201 conforme a orientação institucional; não criar opção 37202 nem copiar esses valores para uma linha adicional. Em Despesas, SPSM é opção própria. A lista permitida é configuração da consulta, não inferência feita pelo componente.

Com o campo ativado, a ausência de `filtro-uo.js` gera erro explícito de configuração. Uma lista de códigos permitidos vazia não admite linhas. Por isso, conferir scripts, opções e atributos antes de publicar a ativação.

## Teste e limites

Os registros de exemplo ficam somente em `tools/testar_filtro_uo.js`, fora de `dist`. Executar da raiz com `cscript.exe //nologo tools\testar_filtro_uo.js` no Windows ou `node tools/testar_filtro_uo.js` onde Node já estiver disponível. O teste usa o predicado real, com listas distintas de UOs, seleção específica/conjunta, confirmação ausente, códigos inválidos e combinação com ano/mês. Não instala dependências nem cria dados publicáveis.

A ativação depende dos dados oficiais e da futura adaptação das páginas/exportações. As dúvidas contábeis dos layouts continuam abertas. Este componente não resolve movimentos, saldos, competência, ajustes ou consolidação e não atribui UOs aos registros.
