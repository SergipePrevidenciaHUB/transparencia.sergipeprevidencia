# Protótipo PETP 2026 — SergipePrevidência

Protótipo estático, sem CMS e sem banco de dados, destinado a testes visuais, funcionais e de marcação do robô Serigy.

## Escopo implementado

- Página inicial com acesso visível ao Portal da Transparência e pesquisa.
- Acessibilidade: símbolo, migalhas de pão, alto contraste, redimensionamento e mapa do site.
- Institucional > Informações: organograma e norma de estrutura.
- Receitas previstas e arrecadadas: mês, ano, valores previstos e realizados, filtros e downloads.
- Recursos Humanos > Estagiários: nome, contratação, término, filtro por ano e downloads.

## Atenções antes de publicar

1. Os dados de Receitas e Estagiários são fictícios.
2. O organograma fornecido deve ser validado contra a Lei nº 9.553/2024 e demais normas vigentes.
3. O HASH oficial do Invoker não foi inserido. Ele é exclusivo e deve ser incluído somente no ambiente autorizado.
4. A validação local confere arquivos e marcações, mas não substitui a avaliação oficial do Serigy.

## Executar no Windows

1. Instale o Python 3.
2. Dê duplo clique em `iniciar-servidor.bat`.
3. Acesse `http://localhost:8000/`.

Alternativamente, no terminal da pasta:

```powershell
py -m http.server 8000 --directory dist
```

## Validar a estrutura

```powershell
py tools/validar_prototipo.py
```

## Importar planilhas

Instale uma vez as bibliotecas:

```powershell
py -m pip install -r tools/requirements.txt
```

Importar Receitas:

```powershell
py tools/importar_dados.py receitas "C:\caminho\receitas.xlsx"
```

A planilha deve possuir: ano, mês, valor previsto e valor arrecadado.

Importar Estagiários:

```powershell
py tools/importar_dados.py estagiarios "C:\caminho\estagiarios.xlsx"
```

A planilha deve possuir: nome, data de contratação e data de término. O importador interrompe a geração se encontrar campo obrigatório vazio.

## Homologação no Serigy

Para a execução real do Invoker, o conteúdo da pasta `dist` deve estar publicado em URL acessível ao robô, sem login ou bloqueio. Depois, deve-se gerar o HASH da unidade no Portal de Homologação do TCE/SE e inserir na página principal do Portal da Transparência:

```html
<meta serigyItem="invoker" serigyValue="HASH-OFICIAL-DA-UNIDADE">
```

Somente então a URL pública poderá ser submetida ao Invoker.
