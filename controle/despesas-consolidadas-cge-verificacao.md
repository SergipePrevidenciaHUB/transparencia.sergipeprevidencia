# Despesas consolidadas - conferência interna

## Fontes e tratamento
- despesas-final.xlsx: 1.736 linhas de janeiro/2023 a outubro/2026, todas preservadas, com as 14 colunas de origem. Não se excluíram valores negativos (90 linhas com pelo menos uma medida negativa). Valores negativos não são automaticamente erros; podem representar movimentações/anulações.
- Despesas_Unificadas.xlsx: incluídas somente as 1.574 linhas da UO 37401 (FINANPREV) e 28 da UO 37403 (FUNPREV). Não se adicionaram linhas antigas das UOs 37201 e 37202.
- Total: 3.338 registros e 97 combinações exercício/mês/entidade. Não contém empenhos individuais nem valores sintéticos. O escopo continua restrito a 4.1 e 4.2.
- O dicionário Base_de_Conhecimento.xlsx foi utilizado para os códigos/descrições dos fundos e para enriquecimentos inequívocos do Instituto. Modalidade de aplicação é classificação orçamentária, não modalidade de licitação. Não inventar associação com procedimentos licitatórios.
- Cada registro possui ID, arquivo, aba e linha de origem. Os valores são mantidos em reais e também em centavos inteiros no JSON, para somas sem erros de ponto flutuante no portal.

## Cuidado obrigatório com unidade e duplicação
A exportação nova apresenta UG 372011-SERGIPE PREVID. e inclui ações do SPSM, não sendo equivalente somente à UO 37201. Não converter UG em UO por corte de dígitos. Na planilha, a coluna Código UG está preenchida para o Instituto e Código UO permanece vazia nessas linhas; os fundos preservam os códigos de UO da fonte anterior. O filtro Entidade tem SergipePrevidência, FINANPREV e FUNPREV. Não criar uma quarta parcela SPSM com as linhas antigas, pois duplicaria a cobertura já incluída na nova exportação.

## Cobertura
Instituto e FINANPREV: 12 meses de 2023/2024/2025 e janeiro a outubro/2026.
FUNPREV: abril e junho a setembro/2026, conforme a base anterior. Abril contém duas linhas zeradas. Maio e outubro não constam. Não completar ausências com zero ou presumir inexistência de despesas nesses meses.

## Conciliação e pendências
1. A nova exportação do Instituto e a soma antiga das UOs 37201/37202 não coincidem em todos os valores: empenhado diverge em 21 de 46 competências; liquidado em oito; pago em todas as 46. A aba Conferencia apresenta novo, anterior e diferença. A origem nova tem prioridade para o Instituto, como solicitado. Os valores antigos não foram misturados nem usados para corrigir a nova fonte.
2. No mês de outubro/2026, os valores pagos e liquidados da nova exportação são inferiores aos valores das fontes antigas em algumas referências. Confirmar data de corte, critérios e significado contábil de pagamento nas duas exportações. A estrutura está pronta, mas não há conciliação contábil entre os dois sistemas.
3. Existem 46 linhas do Instituto com código de elemento não recuperado por correspondência exata/única (descrição “Outros Benefícios Assitências do Servidor e do Militar”). A descrição original foi preservada; não inferir código com base em semelhança textual.
4. Uma linha apresenta fonte “Benefícios Previdenciários - Poder Executivo - Fundo em Repartição (Plano Financeiro)”, para a qual o dicionário oferece 1500002111 e 1801002111. Não escolher um código sem a origem. Descrição e valores preservados. Detalhamento de IDs na aba Conferencia.
5. Confirmar UO por linha na exportação do Instituto para o atendimento estrito de 4.2. A UG está identificada corretamente, mas isso não comprova a discriminação de UO.
6. Programa e ação dos fundos são enriquecidos pelo dicionário recebido; a atualidade histórica dessas denominações não foi certificada. Na nova exportação do Instituto, textos, prefixos e grafia são literais.
7. A classificação consolidada é mensal, no mesmo padrão dos valores apresentados nas fontes. A visualização “Todos os meses” soma somente os registros presentes no exercício. Não somar saldos anuais/acumulados por engano se a fonte mudar em futuras atualizações; validar essa semântica na origem.
8. Data de atualização no portal permanece 22/10/2026 conforme autorização vigente; data de extração/atualização contábil não foi comprovada. Não inventar fechamento ou alterar a data por causa do relógio do computador.

## Regras de layout e integração
- Capturas CGE fornecidas pelo responsável: filtros no topo, três totais destacados e tabela plana de classificação. Reproduzir a organização no visual do portal, sem copiar textos técnicos de teste da CGE.
- Uma seleção compartilhada alimenta os três totais, a tabela e a exportação. Somar registros de detalhe uma única vez. Totais mensais no JSON são referência de validação, nunca linhas adicionais.
- Exibir as 14 colunas da origem: Ano/Mês; Unidade orçamentária / gestora; Função; Sub-função; Categoria econômica (origem: Natureza da despesa); Grupo; Ação; Programa; Modalidade de aplicação; Elemento; Fonte; Empenhado; Liquidado; Pago. Códigos completos e descrições devem permanecer associados onde disponíveis.
- Filtros mínimos: exercício e mês/período (4.1); também elemento (4.2). Entidade facilita o recorte entre os três conjuntos solicitados. Não confundir modalidade de aplicação com contratação.
- Serigy: schema https://serigy.tce.se.gov.br/comum/despesas.html. Totais: valorEmpenhado, valorLiquidado, valorPago. Classificação: unidadeDespesa, funcaoDespesa, subFuncaoDespesa, categoriaDespesa, grupoDespesa, elementoDespesa, fonteRecursosDespesa. Controles: filtroPesquisa, historicoExercicio, salvarRelatorio, dataUltimaAtualizacao; ação/espera/carregamento devem apontar para seção real.
- Não marcar valores agregados de classificação como valorEmpenhoIndividual; essa marcação pertence a 4.3. Não adicionar atributos inventados a programa, ação ou modalidade de aplicação.
- Não gerar campo vazio como zero, nem usar “Não informado”. Sem dados no recorte: tabela sem linhas e mensagem breve de ausência de resultado, preservando distinção de total zero.

## Integração no Portal — 23/10/2026

Integrados os 3.338 registros desta preparação, com seleção compartilhada entre indicadores, tabela plana de 14 colunas e CSV. Padrão visual dos dois prints reaproveitado sem copiar componentes CGE. Inicialização em 2026/setembro/SergipePrevidência: 40 linhas, empenhado R$ 70.427.730,23, liquidado R$ 72.629.591,59 e pago R$ 46.645.716,08. Todos os registros permanecem no HTML inicial; somente o recorte selecionado fica visível. Ausência de registros apresenta traço nos indicadores, sem simular zero contábil.

`tools/integrar_despesas.py` agora delega à geração consolidada em `tools/despesas_consolidadas.py`; `--check` confere reprodução sem gravar. Fonte anterior não é misturada à preparação nova. JavaScript específico soma centavos inteiros com BigInt e exporta somente linhas de base selecionadas. Exercício obrigatório; limpar restaura o recorte inicial; todos os meses soma apenas competências existentes daquele exercício. Mantidas marcações de classificação, totais, filtro, histórico, CSV, espera/carregamento e atualização 22/10/2026, sem criar marcações para programa/ação/modalidade.

Conferidos os 97 totais mensais, contagens 1.736/1.574/28, os seis recortes proporcionais (inicial, FINANPREV, FUNPREV, elemento, sem dados e exercício sem mês), limpeza e CSV com todas as 14 colunas e valores. Chrome em desktop/celular, com rolagem restrita ao contêiner da tabela; evidências em `trabalho/despesas-cge-*/`. O bloco 4.3 foi comparado ao snapshot anterior; registros, avisos, marcações e JavaScript legado preservados, assim como o índice Git e os arquivos fora do escopo. Ensaios remanescentes continuam sujeitos ao bloqueio oficial global; não foi alterado o deploy nem executado o preparador sintético sobre os dados reais.

As pendências contábeis, de UG/UO, códigos, fonte ambígua, cobertura e denominações descritas acima permanecem abertas. Teste local não equivale a conciliação contábil, atualização comprovada das bases ou reconhecimento pelo Invoker. Não foram publicados avisos internos na interface.

## Verificação realizada na preparação
Contagens e valores conciliados aos arquivos; valores monetários com duas casas e sem estimação; planilha com seleção por exercício, mês, entidade e elemento. Conferidos os totais de setembro/2026 do Instituto e FINANPREV e soma das três entidades. Sem erros de fórmula na inspeção da ferramenta. A execução nativa no Excel e a leitura pelo Invoker não foram realizadas aqui.
Cartilha 4.1/4.2 exige disponibilidade, atualidade (30 dias), três exercícios anteriores, filtro e formato editável. Há série de 2023 a 2026 para Instituto/FINANPREV e dados disponíveis para FUNPREV; não declarar conformidade integral de UO/códigos, cobertura dos fundos, atualidade e conciliação contábil enquanto as pendências subsistirem.
