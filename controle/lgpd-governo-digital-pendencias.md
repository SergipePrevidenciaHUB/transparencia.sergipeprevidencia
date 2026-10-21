# LGPD e Governo Digital — pendências para alimentação e publicação

Escopo desta etapa: **C 14.1 e 14.2 ↔ S 14.1.1–14.1.3**. Ambos aplicáveis expressamente à Previdência Estadual; Disponibilidade é o único item exigido. Fontes: Cartilha pp. 107–109 nos trechos LGPD e Serigy Docs 14, seção 14.1 e exemplos correspondentes. Mapeamento detalhado em `controle/lgpd-governo-digital-modelos.md`.

Modelo não publicado: `modelos/Portal-da-Transparencia/LGPDeGovernoDigital/index.html`. Rota S `/Portal-da-Transparencia/LGPDeGovernoDigital/`, sem sufixo LGPD. Não foi adicionada ao menu.

| Requisito / bloco | Dado, documento ou dúvida pendente | Providência antes da publicação |
| --- | --- | --- |
| C 14.1 / identidade | Nome institucionalmente confirmado do encarregado/responsável | Receber confirmação da função e preencher `#nome-encarregado-lgpd`; não deduzir pelo cargo de gestor ou responsável de SIC/Ouvidoria. S 14.1.1 `nomeResponsavel` — Nome. |
| C 14.1 / comunicação | Telefone e/ou e-mail real de comunicação com o encarregado | Confirmar vínculo à função, autorização de divulgação e destino. Um dos meios atende à redação; não exigir ambos nem reaproveitar contato geral sem equivalência. S 14.1.2 `contatoResponsavel` — Telefone ou E-mail. |
| Conferência da designação | Fonte que confirme a identidade e a responsabilidade | Obter referência institucional para validação. Não transformar ato de designação, CPF, fotografia ou currículo em anexo/campo obrigatório; não são mínimos deste recorte. |
| C 14.2 / política adotada | Política de Privacidade e Proteção de Dados efetivamente adotada pela Unidade | Receber conteúdo integral e confirmar versão, abrangência e adoção. Não gerar política genérica, copiar exemplo S ou declarar conformidade pela simples identificação. S 14.1.3 `politicaPrivacidade` — Link. |
| C 14.2 / URL e acesso | Destino oficial conferido para HTML/documento integral | Confirmar acesso público, integridade e correspondência à política; não criar URL por suposição ou presumir destino definitivo de PDF. Não usar serigyLink para PDF. |
| Normas e documentos distintos | Relação entre suporte legal, eventual ato de designação e política institucional | Manter finalidades separadas. Leis federais e ato de designação não substituem a política adotada. Se a instituição fornecer instrumentos distintos, registrar a função de cada um antes de apresentar; não presumir dois arquivos de política nem biblioteca normativa obrigatória. |
| Atualização e controles | Sem periodicidade, filtro, histórico, exportação ou data autônomos enumerados em C 14.1/14.2 ou S 14.1.1–14.1.3 | Confirmar que a identidade, contato e versão são os efetivamente adotados. Não preencher data do dia ou criar propriedade de atualização; metadado editorial futuro deve ter fonte real. |
| Rota e limites da seção | S 14.1 inclui também itens 14.1.4/14.1.5 para C 14.5 | Satisfação está fora desta rodada. Em etapa futura, preservar os blocos LGPD na mesma rota ao preparar os demais conteúdos; não sobrescrever nem inventar subrota por dedução. Serviços/Dados Abertos não foram modelados. |
| Publicação e marcações | Dados e documentos reais ainda não recebidos/conferidos | Alimentar os blocos e aplicar nomeResponsavel, contatoResponsavel e politicaPrivacidade somente em conteúdo existente; validar rótulos, comunicação, acesso e integridade antes de mover para dist em tarefa autorizada. Não enviar mensagens externas nem publicar dados privados para teste. |

Contatos gerais do rodapé não são canal homologado do encarregado. Não há conteúdo fictício, declarações de inexistência ou marcações de dados vazios. Dist, menus, deploy, Ouvidoria, SIC e modelos anteriores foram preservados. Não houve consulta externa ou confirmação institucional nesta tarefa.


## Complemento — Serviços Públicos: C 14.3 / S 14.2.1

Fontes: Cartilha pp. 109–110, critério **14.3**; Serigy Docs 14, seção **14.2**, item **14.2.1 `servicoPublico` (Link)**, p. 1 e exemplo nas pp. 1–2. Critério obrigatório, aplicável expressamente à Previdência Estadual, com somente Disponibilidade.

**Rota própria:** `/Portal-da-Transparencia/LGPDeGovernoDigital/Servicos/`. Modelo `modelos/Portal-da-Transparencia/LGPDeGovernoDigital/Servicos/index.html`. Não compartilha o caminho exato do modelo de LGPD; não há variante ou montagem conjunta necessária. O HTML pai permaneceu intacto; o breadcrumb do novo modelo referencia sua rota futura, sem inclusão em menu público.

| Requisito / tema | Conteúdo ou dúvida pendente | Providência |
| --- | --- | --- |
| Serviços reais | Identificação dos serviços administrativos/operacionais efetivamente oferecidos digitalmente pela Unidade | Receber catálogo e confirmação da área. Não copiar exemplos C/S, presumir serviço por nome de plataforma ou usar e-SIC como substituto. |
| URLs e formas de acesso | Destino oficial pertinente a cada serviço e vínculo ao SergipePrevidência | Conferir cada URL e o acesso digital; não construir caminho ou inserir link genérico como comprovação de serviço funcional. |
| Funcionamento | Possibilidade real de demandar/acessar o serviço sem solicitação presencial | Verificar o fluxo previsto e suas condições com a fonte institucional; não declarar atendimento pela presença de link. Testar somente sem envio de demanda real não autorizado. |
| Informação ao usuário | Nome, eventual descrição e orientação de acesso real de cada serviço | Obter conteúdo validado e associar ao acesso correspondente. Organização editorial é DT; não criar prazos, requisitos, autenticação, etapas ou canais por analogia. |
| Documentos eventuais | Instruções/documentos efetivamente necessários e fornecidos para o serviço | Conferir pertinência e destino. C/S deste critério não impõem anexo adicional nem os campos completos da Carta; documento descritivo não substitui acesso digital. |
| Marcação e controles | Acessos reais ainda não recebidos | Aplicar apenas `servicoPublico` aos links confirmados sob schema lgpd-governo-digital; sem itens de nome/descrição inventados, marcação em lista vazia ou filtro/histórico/exportação/data autônomos não previstos. |
| Relação com outras páginas | Eventual catálogo compartilhado com Carta de Serviços | Reaproveitar somente origem validada, sem confundir divulgação da Carta, e-SIC e prestação digital. Não alterar os modelos existentes nem presumir fluxo comum. |
| Publicação | Catálogo e funcionalidade ainda sem validação | Resolver pendências, alimentar e testar links, teclado, rótulos e fluxo digital antes de mover para dist em tarefa autorizada. Sem atualização de menus ou deploy nesta rodada. |

Nenhuma informação sobre serviço, prazo, canal, URL ou documento foi inventada. Permanecem preservados os modelos de LGPD e das demais seções e as alterações preexistentes. A busca comum não substitui a verificação da prestação digital e o modelo vazio não comprova atendimento.


## Complemento — Dados Abertos: C 14.4 / S 14.3.1

Fontes: Cartilha PETP 2026, critério **14.4**, pp. 111–112; Serigy Docs 14, seção **14.3**, item **14.3.1 `dadosAbertos` (Texto)** e exemplo na p. 1. Critério obrigatório, aplicável à Previdência Estadual, com somente Disponibilidade. Rota própria `/Portal-da-Transparencia/LGPDeGovernoDigital/DadosAbertos/`; modelo no mesmo sufixo sob `modelos/`.

| Tema / requisito | Informação ou arquivo pendente | Providência |
| --- | --- | --- |
| Conjuntos reais | Identificação do(s) conjunto(s) autorizado(s), conteúdo e origem | Receber e conferir dados publicáveis. C prevê pelo menos um caso legível por máquina neste ciclo; não declarar mínimo satisfeito por modelo vazio ou arquivo de teste não validado. |
| Formatos | Arquivo(s) em formato aberto e legível por máquina | Confirmar o formato realmente oferecido, sem impor uma lista de extensões ou oferecer versões inexistentes. Testar leitura automatizada e integridade. |
| URL/acesso | Destino oficial e acesso automatizado efetivo para cada conjunto | Conferir a correspondência e o funcionamento; não presumir API nem montar caminhos por nome/ano. Exemplo GET S não é endpoint da Unidade. |
| Regras de utilização | Conteúdo institucional com seções detalhadas | Receber regras adotadas, associadas ao acesso real. Não inventar licença nominal, condições ou texto-padrão de reutilização; identificar a fonte de eventuais instrumentos existentes. |
| Exemplos | Exemplos coerentes com os dados e acessos efetivamente aprovados | Preparar e testar somente após receber arquivos/URLs e regras. Não copiar API fictícia ou usar comando com destino presumido. |
| Metadados e período | Descrições, referência temporal e cobertura reais, quando utilizadas como DT | Não preencher data atual automaticamente nem afirmar completude. C 14.4 não fixa periodicidade/histórico próprios; manter exigências aplicáveis ao conjunto de origem. |
| Conteúdo público | Derivados aprovados, sem fontes privadas, dados pessoais indevidos ou credenciais | Validar a publicação; não copiar XLSX de origem ou cadastros operacionais. Arquivos de teste de outras páginas não foram homologados por esta tarefa. |
| Marcação | Texto real de dados abertos, regras e acesso | Aplicar apenas dadosAbertos no schema correto após alimentação. Não inventar propriedades de formato/API/licença, filtro, exportação ou atualização; não marcar contêiner vazio. |
| Publicação | Dados, regras, exemplos e acessos ainda sem alimentação | Resolver pendências, testar acesso automatizado, exemplos, links e acessibilidade antes de mover para dist em tarefa autorizada. Não incluir modelo vazio no menu. |

### Cobertura e pendências restantes da dimensão 14

- **14.1 / S 14.1.1–14.1.2:** modelo raiz preparado; faltam identidade e contato do encarregado confirmados.
- **14.2 / S 14.1.3:** modelo raiz preparado; faltam política adotada, versão e acesso integral.
- **14.3 / S 14.2.1:** Serviços preparado; faltam catálogo real, destinos, orientações e comprovação de demanda/acesso digital.
- **14.4 / S 14.3.1:** Dados Abertos preparado nesta etapa; faltam conjuntos, formatos reais, URLs/acesso automatizado, regras e exemplos.
- **14.5 / S 14.1.4–14.1.5:** fragmento não publicado preparado conforme complemento abaixo, para integração à rota raiz; faltam instrumento/acesso real, regularidade e resultados confirmados. Modelo LGPD preservado, sem nova rota pública.

A cobertura descrita é de preparação, não de atendimento aos critérios. Nenhuma pendência anterior foi encerrada pela criação do catálogo vazio. Modelos LGPD/Serviços e demais seções, dist, menus e deploy permaneceram preservados; nenhuma publicação ou consulta externa foi realizada.


## Complemento — Satisfação: C 14.5 / S 14.1.4–14.1.5

**Texto C exato:** “14.5 Realiza e divulga resultados de pesquisas de satisfação?” (Cartilha, p. 113). Critério obrigatório, aplicável expressamente à Previdência Estadual, com somente **Disponibilidade**. Devem ser divulgados resultados de pesquisas regularmente aplicadas; as frequências citadas são exemplos, não prazo único.

**S:** 14.1.4 `pesquisaSatisfacao` (Link ou Forms) e 14.1.5 `resultadoSatisfacao` (Link, Imagem ou Texto), na seção 14.1, rota **`/Portal-da-Transparencia/LGPDeGovernoDigital/`**. Fontes conferidas: C p. 113 e S pp. 1–2, tabela e exemplo correspondentes.

**Preparação sem nova página:** `modelos/variantes/pesquisas-satisfacao/bloco-satisfacao.html`, fragmento de seção para integrar futuramente ao main da raiz LGPD, após a política. Não publicar o fragmento como página própria, não sobrescrever o index existente nem criar subrota por suposição. O main, cabeçalho e rodapé da página raiz serão reutilizados; nenhum deles foi alterado.

| Requisito / tema | Informação ou evidência faltante | Providência |
| --- | --- | --- |
| Realização da pesquisa | Instrumento, serviço/público avaliado e forma real de aplicação | Receber confirmação da área. Não criar perguntas, categorias, escala, serviço ou formulário próprio por suposição. |
| Regularidade | Aplicações efetivas e regularidade adotada, com referências reais | Confirmar com a fonte, sem impor anual/semestral ou prazo fixo. Um relatório isolado não comprova regularidade. C não define série mínima ou histórico de três anos neste critério. |
| Acesso / S 14.1.4 | Link ou instrumento real compatível com a forma de aplicação | Conferir destino/conteúdo antes de inserir pesquisaSatisfacao. Não copiar URL de exemplo ou supor pesquisa ativa. Esclarecer a apresentação se a aplicação for presencial ou não houver formulário online; não criar um só para preencher a reserva. |
| Divulgação / S 14.1.5 | Resultados efetivamente produzidos e sua associação à pesquisa/aplicação | Receber conteúdo completo pertinente, em apresentação compatível com a fonte e as alternativas S. Não basta link para responder; não reutilizar estatísticas SIC como satisfação sem fonte metodológica. |
| Referências e conceitos | Período/aplicação, categorias, metodologia e bases que permitam entender os resultados reais | Confirmar os elementos existentes. Não inventar NPS, percentuais, totais, notas ou denominadores nem impor indicadores fixos como mínimo C. |
| Proteção de dados | Resultados públicos adequados e sem respostas individuais identificáveis | Conferir agregados/derivados com a área; não publicar cadastro privado, contato ou respondente. |
| URLs / documentos / imagens | Acessos e arquivos reais, se utilizados na apresentação | Conferir correspondência e acesso. S permite Link/Imagem/Texto para resultados, sem exigir todos ou formato específico. Não gerar URL por data/nome nem criar relatório ou formato inexistente. |
| Integração e marcações | Conteúdo e apresentação ainda não alimentados | Inserir a seção no main da raiz em tarefa autorizada, mantendo LGPD. Aplicar pesquisaSatisfacao e resultadoSatisfacao só no conteúdo real; sem marcação em div vazio ou novo item de data/filtro/exportação. |
| Publicação | Regularidade, instrumentos, resultados e eventuais destinos ainda pendentes | Resolver fontes, alimentar e testar acesso e acessibilidade, sem enviar respostas reais não autorizadas. Não declarar atendimento ou publicar fragmento vazio. |

### Situação consolidada da dimensão

14.1 e 14.2 têm estrutura no modelo raiz; 14.3 em Servicos; 14.4 em DadosAbertos; 14.5 tem agora fragmento para a mesma rota raiz de 14.1/14.2. **Todos os cinco estão contemplados na preparação estrutural, sem comprovação de alimentação ou atendimento.** Permanecem pendentes identidade/contato, política, serviços digitais, conjuntos/regras/exemplos e pesquisas/resultados reais. O status anterior “14.5 ainda sem modelo” foi atualizado; nenhuma pendência institucional foi encerrada pela criação do fragmento.

Não foram exigidos controles autônomos de filtro, histórico, gravação ou atualização que C/S 14.5 não enumeram. Não foram alterados dist, menus, deploy, modelos existentes ou outras seções. Sem dados, documentos, links, datas ou formatos inventados.
