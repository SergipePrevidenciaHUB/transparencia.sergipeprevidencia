# Pesquisa por CPF completo - contrato técnico e implantação pendente

## Limitação atual
GitHub Pages entrega conteúdo estático e não executa backend. Uma pesquisa baseada somente em JS do navegador exige que o índice pesquisável esteja público, incompatível com o requisito do responsável. É possível manter o portal no Pages e consultar uma API HTTPS separada, preferencialmente na infraestrutura institucional gerida pela TI/CGE.
Não há implantação ou teste de backend neste pacote. O código local não está acessível ao ChatGPT Work. O Codex deve verificar o repositório real e qualquer serviço existente.

## Fluxo permitido
1. Cidadão informa CPF completo no campo específico, com execução explícita em “Pesquisar”. Sem autocomplete de CPF nem consulta a cada tecla. O CPF digitado necessariamente existe na memória do navegador que o usuário utiliza; a exigência é não devolver ou distribuir CPFs da base.
2. Enviar somente esse CPF e os filtros necessários no corpo de POST HTTPS para /api/empenhos/consulta-cpf. Nunca em URL, query string, analytics, logs, telemetria, localStorage ou sessionStorage. Não refletir CPF em mensagens de sucesso/erro e limpar o campo ao terminar, sem armazená-lo.
3. Serviço valida CPF completo, tamanho, dígitos verificadores, esquema e limites. Pesquisa exata com parâmetros preparados, sem prefixos, curingas, listagem de CPFs ou enumeração sequencial.
4. Resposta: dados públicos já mascarados ou IDs opacos estáveis EMP-... presentes na projeção pública; nenhum CPF completo, token derivado de CPF, índice privado ou segredo. Não devolver base irrestrita.
5. Preservar o recorte e aplicar paginação/limite máximo. Exportações devem passar pela mesma projeção mascarada; nada de exportar a tabela privada.

## Base e acesso
- Inputs originais completos em armazenamento privado com permissões de serviço mínimas, criptografia de disco/banco e backups, acesso administrativo autenticado e auditado. Diretório fora da árvore publicada e do repositório público.
- Preferir índice privado HMAC-SHA-256 do CPF normalizado, com chave secreta de servidor guardada em gestor de segredos e rotação documentada. O índice continua dado pessoal e não pode ser publicado. Se for necessário conservar CPF recuperável, criptografia autenticada e chaves separadas do banco. Nunca SHA-256 simples, salt conhecido no cliente ou chave embarcada no JS.
- O ID público da nota deriva de UG/UO/NE/exercício, não do CPF. É preciso que o importador privado gere exatamente os IDs do JSON preparado. Não é possível recuperar CPF completo a partir da projeção mascarada; a base privada deve ser construída das fontes originais autorizadas, somente no ambiente restrito.
- Não incluir segredo, token administrativo, credencial ou dado bruto em arquivos versionados, sourcemaps, bundles, artefatos ou mensagens de teste.

## Proteção contra automação
- Limitação real de requisições no servidor/gateway e compartilhada entre instâncias, por IP confiável, sessão/identidade autorizada e limite global. Persistência apropriada, não apenas contador em JS ou memória efêmera. Retornar 429 e Retry-After quando necessário.
- Limites para corpo, tempo de consulta, tamanho de página, concorrência e exportação; impedir consultas em lote e chamadas sem CPF completo.
- Autenticação/autorização compatível com a política definida para essa consulta. Se o acesso individual puder ser anônimo, usar desafio antiabuso validado no servidor e controles de risco, reconhecendo risco residual de enumeração. CAPTCHA isolado não impede extração em massa.
- CORS com origens permitidas é defesa complementar, não autenticação; não bloquear toda a transparência atrás de login. Informações públicas mascaradas continuam acessíveis e exportáveis.
- TLS, headers de segurança, Cache-Control: no-store nas respostas da consulta, erros genéricos e logs sem CPF/corpo. Auditoria pode registrar quantidade, rota, status e identificador técnico mínimo, sem conservar documento digitado.

## Critérios de aceitação
- CPF exato localiza as notas corretas sem expor documento em resposta, cache, erro, log ou download.
- CPF inválido/parcial, consultas em lote e origens/credenciais indevidas são recusadas.
- Limites são testados com carga controlada; após ultrapassar, 429 efetivo. Com serviço indisponível, falhar fechado sem fallback para base completa no cliente.
- Inspecionar HTML, JS, JSON, source maps e XLSX/CSV/PDF públicos. Asserções com CPFs originais devem rodar em ambiente privado, mostrando só contagens/IDs, nunca imprimindo os CPFs.
- Auditoria de arquivos rastreados, staging e pacote Pages para impedir publicação de fontes restritas. .gitignore não remove histórico anterior. Se for encontrado CPF real em histórico público, registrar exposição e providência específica; não reescrever histórico ou forçar push automaticamente.
- Proteções reduzem risco, não garantem impossibilidade de extração. O pacote não é certificação LGPD nem teste de penetração.

## Referências técnicas
- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html
- https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html
- https://cheatsheetseries.owasp.org/cheatsheets/Bot_Management_and_Anti-Automation_Cheat_Sheet.html
