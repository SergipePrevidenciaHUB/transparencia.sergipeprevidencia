# Convênios — revisão documental e técnica

## Resultado
- Planilha nova: oito acordos reais, e não sete. Acrescenta Faculdade de Direito 8 de Julho, 002/2026, processo 522/2026.
- Oito instrumentos individuais lidos: Estácio, UFS, FANESE, Pio Décimo, UNINASSAU, UNIT, IFS e Faculdade de Direito 8 de Julho. Resumos distinguem Instituto, parceiro e compromissos conjuntos; não são mera repetição do objeto.
- Estácio: PDF anexado lido visualmente, páginas 1–3; resumo concluído. O link original file:// é inadequado para publicação; destino WordPress planejado no JSON.
- Faculdade de Direito 8 de Julho: PDF anexado lido, cláusulas 1ª–8ª e protocolo de assinaturas; resumo concluído. PDF preparado para publicação no destino WordPress planejado.
- Resumos são documentais; aprovação institucional posterior não foi presumida.

## Cartilha PETP 2026
5.1/5.2, páginas 42–45: declaração expressa de inexistência no período, acompanhada de atualização, é solução prevista. Histórico mínimo de três anos anteriores, consulta por exercício e relatório editável estão previstos no critério. Manter consulta da declaração por exercício e exportação do seu texto; não criar transações.
5.3, páginas 46–47: partes, identificação, objeto, vigência, obrigações e íntegra; histórico de três anos anteriores, pesquisa por exercício, atualização e exportação editável. O relatório deve incluir as obrigações.

## Serigy
Documentação: https://serigy.tce.se.gov.br/petp/comum/convenios-transferencias.html
Definições: https://serigy.tce.se.gov.br/definicoes.html
Schema: https://serigy.tce.se.gov.br/comum/convenios-transferencias.html
A seção “sem informações” exemplifica um valorRepassado ausente em uma transferência existente, NÃO demonstra aprovação integral quando nenhuma transferência existe. A regra geral permite serigyEmpty com motivo único por campo. Aplicar esta técnica à linha explicitamente declaratória de ausência é uma adaptação fundamentada, cujo reconhecimento depende do Invoker; não alegar 100% comprovado.
Não basta tabela com tbody vazio ou atributos nos cabeçalhos. Manter declaração verdadeira e células de ausência justificadas, sem número/beneficiário/valor/anexo inventado e sem link vazio. Valores monetários ausentes não devem ser convertidos em R$ 0,00 como se fossem operações reais. A linha declaratória não conta como transferência.

Campos 5.1: identificaTransferencia, orgaoRepassador, vigenciaConvenio, objetoConvenio, valorTotalPrevisto, valorRepassado, anexoConvenio.
Campos 5.2: identificaTransferencia, orgaoBeneficiario, vigenciaConvenio, objetoConvenio, valorTotalRepasse, valorRepassado, anexoConvenio.
Campos 5.3: identificaAcordo, participante, vigenciaConvenio, objetoConvenio, obrigacoes, anexoConvenio.
Controles: filtroPesquisa, salvarRelatorio, historicoExercicio, dataUltimaAtualizacao; serigyExecuteWaitSection apontando exatamente ao serigyLoadSection da tabela correspondente. Options com value e serigyValue para os exercícios reais do período declarado. Ao filtrar ano, consultar abrangência da declaração, sem simular ocorrência de transferências.

## Pendências documentais
- UNIT: planilha informa 12/12/2024–11/12/2029; cláusula V do PDF informa prazo indeterminado. Preservar a informação atual até conferência, sem calcular prazo substituto.
- IFS: número 006/2024 veio da planilha, não foi encontrado no título do PDF.
- Estácio e Faculdade de Direito 8 de Julho: PDFs recebidos e resumos concluídos. Publicar nos destinos WordPress planejados do JSON/CSV. Não usar URLs de rede interna. Integrar estas duas providências ao controle geral de PDFs do portal, sem criar outro controle permanente.
- UFS: PDF registra data no corpo e assinatura digital posterior; não redefinir vigência pela assinatura sem confirmação.
- Histórico de acordos deve considerar vigência no exercício quando a interface se propuser a listar acordos vigentes; ano do número e ano inicial de vigência não são equivalentes. UNINASSAU/IFS têm número 2024 e vigência iniciada em 2025.
- Ausência de transferências: declaração institucional anteriormente confirmada de 01/2018 até 21/10/2026. Atualização da página 22/10/2026 não estende automaticamente o período confirmado. Não inventar dia inicial em janeiro/2018.

## Integração limitada
Remover registros, documentos vinculados, avisos e CSVs sintéticos de 5.1/5.2/5.3 da página e seus geradores. Manter declarações, marcações e controles funcionais. Os ensaios de Despesas/SIC/Sanções/Contratos não fazem parte desta remoção; preservar bloqueio oficial global enquanto existirem outros dados sintéticos.
Não excluir arquivo compartilhado nem desativar bloqueio global apenas para limpar estes três módulos. Documentos de teste não podem continuar acessíveis na publicação como se fossem instrumentos reais; excluir somente os artefatos exclusivos confirmados, verificando referências.
Em 5.3 os oito resumos estão disponíveis. Substituir eventuais células de obrigações ausentes pelos textos reais com obrigacoes. Não usar serigyEmpty nesses resumos. O reconhecimento técnico pelo robô e a publicação das duas íntegras planejadas continuam pendentes.

## Conferências realizadas
Oito linhas preservadas; seis PDFs acessados por URLs da planilha e lidos; FANESE anexado também lido; dois PDFs adicionais recebidos e lidos. Os seis resumos anteriores permaneceram idênticos. Fontes e referências individuais constam do JSON e da planilha de trabalho. Nenhuma página do portal alterada, nenhum Invoker executado. Não há pontuação nova comprovada.

## Complemento dos dois anexos
- Estácio: a numeração interna da cláusula Quinta repete 4.1–4.5; as referências no resumo respeitam o impresso. Obrigações e assinatura de 12/05/2022 legíveis nas imagens.
- Faculdade 8 de Julho: selecionar estagiários de forma objetiva/impessoal, relatório semestral e reserva de 10% para pessoas com deficiência são disposições deste instrumento, não generalizadas para os outros acordos. Última assinatura em 30/09/2026, conforme protocolo.
- dataUltimaAtualizacao do portal preservada em 22/10/2026; não confundir com datas de assinatura.


## Integração dos três módulos — 23/10/2026

Recebidas e Realizadas agora contêm somente a declaração institucional de ausência de transferências voluntárias de 01/2018 até 21/10/2026. A atualização da relação é 22/10/2026, sem ampliar o período confirmado nem inventar dia inicial em janeiro/2018. Uma linha declaratória, não contabilizada como transferência, apresenta sete células com serigyItem e motivos serigyEmpty específicos e distintos. É aplicação fundamentada das Definições e do exemplo de ausência de informação; o exemplo isolado não comprova aceitação integral de ausência de operações. Reconhecimento depende de nova avaliação pelo Invoker/TCE-SE.

Consulta por exercício inclui 2026, 2025, 2024 e 2023; seleção e pesquisa observam a mesma seção/tabela, alterando a referência da declaração. Limpeza retorna à abrangência confirmada. CSV exporta exercício consultado, período confirmado, texto da declaração e atualização da página, sem simular transações ou valores monetários.

SemTransferencia apresenta oito acordos reais do JSON revisado e oito obrigacoes_texto, com responsabilidades do Instituto, parceiro e compromissos conjuntos. Identificação, ambas as partes, vigência literal, objeto, obrigações e acesso à íntegra receberam os itens documentados. CSV inclui todos esses campos. O filtro passou a considerar sobreposição da vigência com o exercício consultado, não o ano do número ou apenas o início; a coluna de início continua identificada como tal. UNIT mantém literalmente 12/12/2024–11/12/2029 da fonte; a divergência com a cláusula de prazo indeterminado fica exclusivamente no controle documental.

Estácio e Faculdade de Direito 8 de Julho utilizam documento_url_planejada somente porque documento_url é nulo. Os demais seis URLs públicos da fonte foram preservados. As duas providências de publicação foram incorporadas ao controle geral existente em controle/atos-normativos-verificacao.md; o CSV de origem foi preservado como insumo, sem criar outro controle permanente. Os PDFs não foram copiados para dist. Upload e disponibilidade pública dos dois destinos continuam pendentes, assim como as ressalvas documentais anteriores sobre UNIT, IFS e UFS e a aprovação institucional posterior dos resumos.

Gerador atual: tools/integrar_convenios.py (ou --check para conferir sem gravar). O antigo preparar_teste_acordo.py passou a recusar --ativar; as opções de conferência/desativação usam o gerador real. As entradas antigas de testes encaminham para tools/testar_convenios_reais.py, sem recriar ensaios. Somente três documentos HTML de ensaio e o JS exclusivo de teste foram retirados de dist, depois da conferência de referências. CSVs de ensaio eram gerados no navegador; seus botões/ramificações foram removidos. Não havia CSV estático exclusivo em dist/dados.

Os ensaios das demais áreas e o bloqueio global de publicação oficial permanecem. Esta implementação local e seus testes não alteram resultados das avaliações 4172/4226 nem comprovam pontuação nova ou conformidade integral no robô.
