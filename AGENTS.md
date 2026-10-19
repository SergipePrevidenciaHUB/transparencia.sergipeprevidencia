# Regras permanentes do projeto

## Identidade e objetivo

- Este projeto corresponde ao site institucional e ao Portal da Transparência do SergipePrevidência.
- O objetivo prioritário é atender à Cartilha PETP 2026 do TCE/SE e à documentação oficial do robô Serigy.
- O escopo é exclusivamente a Previdência Estadual.
- A Cartilha PETP localizada em `referencias/petp` é a principal referência normativa e metodológica.
- A documentação localizada em `referencias/serigy` orienta as marcações e a leitura pelo robô.
- Os arquivos de `referencias/estrutura-cge` servem somente como referência visual e estrutural. Não copie automaticamente os JavaScripts, CSS ou arquivos gerados pelo site da CGE.

## Requisitos e decisões

- Não invente requisitos, campos, filtros, prazos, séries históricas ou marcações.
- Diferencie exigência formal, interpretação técnica e melhoria.
- Em caso de ambiguidade, registre a dúvida.

## Interface e estrutura

- Preserve o padrão visual atualmente implementado.
- Reutilize cabeçalho, rodapé, cores, tipografia, breadcrumb, componentes e controles de acessibilidade.
- `dist` contém exclusivamente o conteúdo publicável.
- `dados-entrada` contém arquivos de origem e não deve ser publicado.
- `referencias` contém documentos normativos e técnicos.
- `controle` contém instrumentos de acompanhamento.
- `tools` contém scripts de importação e validação.

## Segurança e alterações

- Não publique planilhas de origem, dados sigilosos, senhas, credenciais ou dados pessoais não autorizados.
- Não altere `.openai/hosting.json` sem solicitação expressa.
- Não insira o hash do Invoker sem autorização.
- Não exclua arquivos sem autorização.
- Não crie commits automaticamente.
- Antes de alterar uma página, identifique os arquivos necessários.
- Após qualquer alteração em `dist`, execute `python tools/validar_prototipo.py`.

## Fechamento de tarefas

- Ao finalizar uma tarefa, informe os arquivos criados, modificados e excluídos e o resultado das validações.
