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
