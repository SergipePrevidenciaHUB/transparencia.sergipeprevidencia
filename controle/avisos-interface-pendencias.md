# Avisos públicos — revisão e pendências internas

Registro anterior à revisão dos HTMLs de `dist`, por solicitação do projeto. A retirada de avisos editoriais de protótipo ou revisão não confirma vigência, completude, homologação, fechamento contábil ou atendimento ao PETP/Serigy. Não há datas institucionais novas nesta revisão.

## Pendências preservadas fora da interface

| Página ou conteúdo | Pendência e providência | Referência interna |
| --- | --- | --- |
| Informações Institucionais — organograma | Conferir a estrutura vigente e os atos complementares. O inventário já registra diferenças entre a imagem e a Lei nº 9.553/2024: Conselho Fiscal, diretorias, vinculação de Ouvidoria/GERPLANEA e denominações de unidades. Obter organograma e data real aprovados pela instituição. A data 18/10/2026 apresentada como atualização do protótipo não comprova atualização institucional e será retirada da interface. | `controle/inventario-bloco-1.md`, critério 2.1; `controle/inventario-tabelas.md`, 2.1. |
| Informações Institucionais — competências | Conferir redação consolidada da Lei nº 5.852/2006 e alterações, correspondência com as competências reproduzidas do HTML de referência e vigência. | Inventários, critério 2.2. |
| Informações Institucionais — responsáveis e currículos | Confirmar atualidade de nomes, cargos e currículos e abrangência dos responsáveis. A remoção do aviso não valida os quatro pares existentes. | Inventários, critério 2.3. |
| Contatos, horário, WhatsApp e Instagram | Confirmar a atualidade dos contatos e a titularidade/destino dos canais reproduzidos das referências. Não foi realizado teste dos sistemas externos nesta revisão. Abrange os rodapés e a entrada do Portal. | Inventário do bloco 1, critérios 2.4, 2.5 e 2.8. |
| Perguntas frequentes | Revisar as 17 respostas e as 11 ocorrências de links: legislação, regras previdenciárias, procedimentos, contatos e referências a 2021, 2022 e calendário de 2026. Não presumir atualização por remoção da faixa de revisão. | Inventário do bloco 1, critério 2.7, e HTML institucional. |
| Atos Normativos | Concluir as correspondências documentais pendentes e confirmar completude, abrangência histórica e atualização do acervo. Preservar registros e vínculos existentes. A interface continuará informando que o acervo é parcial, sem instruções internas de validação. | Controles de vínculos por ano e inventário, critério 2.6. |
| Legislação Interna | Reunir os demais instrumentos aplicáveis, confirmar vigência e associação com a legislação própria. A Lei nº 9.553/2024 disponível não comprova acervo completo nem inexistência de estatuto ou regimento. | Inventários, critério 2.9. |
| Despesas e demais seções ainda sem conteúdo | Obter dados/documentos, cobertura e atualização reais e implementar as consultas e exportações pertinentes antes de ativá-las. Manter indicação factual de informação ainda a disponibilizar e controles indisponíveis. | Controles de pendências de cada dimensão, especialmente `controle/despesas-pendencias.md`. |
| Receitas | A instituição esclareceu que os 425 registros são reais; “receitas-teste.xlsx” nomeava o teste inicial de importação. Permanecem as conferências contábeis, sem impedimento ao prosseguimento. | `controle/receitas-pendencias.md`. |
| Estagiários | Os oito registros atuais continuam identificados nas fontes locais como fictícios. Manter aviso, legenda e identificação das exportações; obter relação oficial antes de apresentá-los como dados institucionais. A data de demonstração não é atualização do cadastro oficial. | `controle/recursos-humanos-pendencias.md`, complemento desta revisão. |

## Limites da correção de Receitas

Os números, registros, arquivos CSV/JSON, filtros, cálculos e scripts não serão alterados. O JSON externo e o JSON incorporado no HTML contêm o metadado antigo `aviso` de planilha de teste, também reproduzido nas exportações JSON dinâmicas. Ele será preservado nesta tarefa para não alterar dados/exportações ou sua conciliação. O importador ainda gera textos de teste; uma regeneração poderá reintroduzi-los. Corrigir esses metadados e textos do gerador em tarefa específica, sem modificar valores nem assumir homologação contábil. Os arquivos antigos `receitas-teste.csv/json` de demonstração não se confundem com a integração atual e não serão modificados nem excluídos nesta rodada.

## Tratamento dos avisos

Retirar faixas genéricas de protótipo/teste, instruções internas de revisão, referências a critérios não homologados e datas meramente técnicas. Substituir o rótulo de rodapé por “Portal da Transparência”. Preservar explicações técnicas dos dados (previsão anual, acumulado, meses disponíveis, soma bruta com intraorçamentárias), identificação inequívoca dos dados fictícios de Estagiários e mensagens factuais de conteúdo pendente. A interface não receberá declarações de inexistência, conformidade ou fechamento de período.


## Organograma — substituição pela versão SVG atualizada

A página Informacoes utiliza a versão atualizada fornecida em dados-entrada/institucional/organograma-sergipeprevidencia-lei-5852.svg, copiada sem alterações para dist. O bloco público mantém somente a estrutura e a referência breve à Lei nº 5.852/2006; o endereço do texto compilado foi preservado sem menção visível à ALESE. O PDF modificador da Lei nº 9.553/2024 continua na seção própria. Permanecem internas a confirmação institucional da estrutura e de sua data real, a conferência dos atos complementares e a situação dos regimentos. Nenhuma data de geração do SVG comprova aprovação institucional. As divergências descritas anteriormente neste controle referem-se à imagem PNG antiga e não devem ser automaticamente atribuídas à nova versão.
