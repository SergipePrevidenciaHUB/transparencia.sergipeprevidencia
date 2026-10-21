(function () {
  const root = document.documentElement;
  const body = document.body;
  const storageKey = "sergipeprev-acessibilidade";
  let state = { scale: 1, contrast: false };
  try {
    state = JSON.parse(localStorage.getItem(storageKey) || '{"scale":1,"contrast":false}');
  } catch (error) {
    // Sem armazenamento, manter as preferencias apenas nesta sessao.
  }

  function applyState() {
    root.style.setProperty("--escala-texto", String(state.scale));
    body.classList.toggle("high-contrast", state.contrast);
    const contrastButton = document.querySelector("[data-action='contrast']");
    if (contrastButton) contrastButton.setAttribute("aria-pressed", String(state.contrast));
    try {
      localStorage.setItem(storageKey, JSON.stringify(state));
    } catch (error) {
      // A persistencia e opcional; os controles ja foram atualizados.
    }
  }

  document.addEventListener("click", function (event) {
    const control = event.target.closest("[data-action]");
    if (!control) return;
    const action = control.dataset.action;
    if (action === "increase") state.scale = Math.min(1.35, +(state.scale + 0.1).toFixed(2));
    if (action === "decrease") state.scale = Math.max(0.9, +(state.scale - 0.1).toFixed(2));
    if (action === "reset-font") state.scale = 1;
    if (action === "contrast") state.contrast = !state.contrast;
    applyState();
  });

  // Acrescentar aqui o caminho de cada nova página publicada do protótipo.
  const searchPages = [
    "/Portal-da-Transparencia/",
    "/Portal-da-Transparencia/Institucional/AtosNormativos/",
    "/Portal-da-Transparencia/Institucional/Informacoes/",
    "/Portal-da-Transparencia/Institucional/LegislacaoInterna/",
    "/Portal-da-Transparencia/Receitas/PrevistaArrecada/",
    "/Portal-da-Transparencia/Despesas/",
    "/Portal-da-Transparencia/Convenios/Realizadas/",
    "/Portal-da-Transparencia/Convenios/Recebidas/",
    "/Portal-da-Transparencia/Convenios/SemTransferencia/",
    "/Portal-da-Transparencia/RecursosHumanos/Concurso/",
    "/Portal-da-Transparencia/RecursosHumanos/Estagiarios/",
    "/Portal-da-Transparencia/RecursosHumanos/FolhaPagamento/",
    "/Portal-da-Transparencia/RecursosHumanos/PadraoRemuneratorio/",
    "/Portal-da-Transparencia/RecursosHumanos/Terceirizados/",
    "/Portal-da-Transparencia/Diarias/Relacao/",
    "/Portal-da-Transparencia/Diarias/TabelaValores/",
    "/Portal-da-Transparencia/Licitacoes/",
    "/Portal-da-Transparencia/Licitacoes/PlanoAnualContratacoes/",
    "/Portal-da-Transparencia/Licitacoes/Sancoes/",
    "/Portal-da-Transparencia/Contratos/GestoresFiscais/",
    "/Portal-da-Transparencia/Contratos/",
    "/Portal-da-Transparencia/Contratos/OrdemCronologica/",
    "/Portal-da-Transparencia/PlanejamentoPrestacaoContas/Balancetes/",
    "/Portal-da-Transparencia/PlanejamentoPrestacaoContas/BalancoGeral/",
    "/Portal-da-Transparencia/PlanejamentoPrestacaoContas/PlanoEstrategico/",
    "/Portal-da-Transparencia/PlanejamentoPrestacaoContas/RelatorioGestao/",
    "/Portal-da-Transparencia/PlanejamentoPrestacaoContas/RGF/",
    "/Portal-da-Transparencia/PlanejamentoPrestacaoContas/TCE/",
    "/Portal-da-Transparencia/SIC/Detalhe/",
    "/Portal-da-Transparencia/SIC/eSIC/",
    "/Portal-da-Transparencia/SIC/LAI/",
    "/Portal-da-Transparencia/SIC/RelatorioAnualEstatistico/",
    "/Portal-da-Transparencia/Ouvidoria/",
    "/Portal-da-Transparencia/LGPDeGovernoDigital/DadosAbertos/",
    "/Portal-da-Transparencia/LGPDeGovernoDigital/",
    "/Portal-da-Transparencia/LGPDeGovernoDigital/Servicos/",
    "/mapa-do-site/"
  ];
  // Apenas pares conhecidos: não cortar sufixos indiscriminadamente (ex.: "lápis").
  // Não é uma análise morfológica completa; novos plurais exigem pares revisados.
  const searchPlurals = new Map(Object.entries({
    normas: "norma", receitas: "receita", previstas: "prevista", arrecadadas: "arrecadada",
    informacoes: "informacao", competencias: "competencia", estagiarios: "estagiario",
    beneficios: "beneficio", servidores: "servidor", responsaveis: "responsavel",
    curriculos: "curriculo", diretores: "diretor", documentos: "documento",
    pensoes: "pensao", contribuicoes: "contribuicao", servicos: "servico",
    recursos: "recurso", paginas: "pagina", organogramas: "organograma"
  }));
  const searchStopWords = new Set("a as o os de da das do dos e em no nos na nas para por com um uma".split(" "));
  let searchIndexPromise;

  function searchWords(text) {
    const normalized = text.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    return (normalized.match(/[a-z0-9]+/g) || [])
      .filter(function (word) { return !searchStopWords.has(word); })
      .map(function (word) { return searchPlurals.get(word) || word; });
  }

  function mainSearchText(parsed) {
    const main = parsed.querySelector("main");
    if (!main) throw new Error("Página sem conteúdo principal.");
    main.querySelectorAll("script, style, template, noscript, nav, header, footer, [hidden], [aria-hidden='true'], .visually-hidden")
      .forEach(function (element) { element.remove(); });
    main.querySelectorAll("[style]").forEach(function (element) {
      if (element.style.display === "none" || /^(hidden|collapse)$/.test(element.style.visibility)) element.remove();
    });
    const walker = parsed.createTreeWalker(main, NodeFilter.SHOW_TEXT);
    const text = [];
    while (walker.nextNode()) text.push(walker.currentNode.nodeValue);
    return text.join(" ");
  }

  async function loadSearchPage(url, order) {
    const controller = new AbortController();
    const timeout = setTimeout(function () { controller.abort(); }, 15000);
    try {
      const response = await fetch(url, { mode: "same-origin", redirect: "error", signal: controller.signal });
      if (!response.ok) throw new Error("Página indisponível.");
      // Documento inerte: seus scripts não são executados nem seus nós inseridos na página atual.
      const parsed = new DOMParser().parseFromString(await response.text(), "text/html");
      const title = parsed.title.trim() || url;
      const titleWords = new Set(searchWords(title));
      return {
        url: url, title: title, order: order, titleWords: titleWords,
        words: new Set([...titleWords, ...searchWords(mainSearchText(parsed))])
      };
    } finally {
      clearTimeout(timeout);
    }
  }

  function loadSearchIndex() {
    if (!/^https?:$/.test(window.location.protocol)) return Promise.reject(new Error("A busca requer HTTP."));
    if (!searchIndexPromise) {
      // Cache em memória; falhas não ficam armazenadas e permitem tentar novamente.
      // Se qualquer página falhar, não apresentar uma busca incompleta como resultado definitivo.
      searchIndexPromise = Promise.all(searchPages.map(loadSearchPage)).catch(function (error) {
        searchIndexPromise = null;
        throw error;
      });
    }
    return searchIndexPromise;
  }

  document.querySelectorAll("[data-site-search]").forEach(function (form, index) {
    const input = form.querySelector("input");
    const results = document.createElement("div");
    results.className = "site-search-results";
    results.id = "site-search-results-" + index;
    const status = document.createElement("p");
    status.setAttribute("role", "status");
    status.setAttribute("aria-live", "polite");
    status.setAttribute("aria-atomic", "true");
    const list = document.createElement("ul");
    list.setAttribute("aria-label", "Resultados da pesquisa");
    list.hidden = true;
    results.append(status, list);
    form.append(results);
    input.setAttribute("aria-controls", results.id);
    let requestId = 0;

    input.addEventListener("input", function () {
      requestId += 1;
      status.textContent = "";
      list.replaceChildren();
      list.hidden = true;
      list.removeAttribute("aria-busy");
    });

    form.addEventListener("submit", async function (event) {
      event.preventDefault();
      const currentRequest = ++requestId;
      const queryWords = [...new Set(searchWords(input.value))];
      list.replaceChildren();
      list.hidden = true;
      list.removeAttribute("aria-busy");
      if (!queryWords.length) {
        status.textContent = "Digite uma palavra para pesquisar.";
        return;
      }
      status.textContent = "Pesquisando…";
      list.setAttribute("aria-busy", "true");
      try {
        const pages = await loadSearchIndex();
        if (currentRequest !== requestId) return;
        const matches = pages.filter(function (page) {
          return queryWords.every(function (word) { return page.words.has(word); });
        }).map(function (page) {
          return { page: page, score: queryWords.filter(function (word) { return page.titleWords.has(word); }).length };
        });
        // Mais termos no título primeiro; empates seguem a ordem do manifesto.
        matches.sort(function (a, b) { return b.score - a.score || a.page.order - b.page.order; });
        matches.forEach(function (match) {
          const item = document.createElement("li");
          const link = document.createElement("a");
          link.href = match.page.url;
          link.textContent = match.page.title;
          item.append(link);
          list.append(item);
        });
        list.hidden = !matches.length;
        status.textContent = matches.length
          ? matches.length + (matches.length === 1 ? " página encontrada." : " páginas encontradas.")
          : "Nenhuma página foi encontrada para essa pesquisa.";
      } catch (error) {
        if (currentRequest !== requestId) return;
        status.textContent = "Não foi possível carregar as páginas para pesquisa. Tente novamente.";
      } finally {
        if (currentRequest === requestId) list.removeAttribute("aria-busy");
      }
      // Não deslocar o foco: os links permanecem acessíveis pela navegação normal por Tab.
    });
  });

  applyState();
})();
