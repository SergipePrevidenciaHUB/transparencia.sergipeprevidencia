(function () {
  const root = document.documentElement;
  const body = document.body;
  const storageKey = "sergipeprev-acessibilidade";
  const state = JSON.parse(localStorage.getItem(storageKey) || '{"scale":1,"contrast":false}');

  function applyState() {
    root.style.setProperty("--escala-texto", String(state.scale));
    body.classList.toggle("high-contrast", state.contrast);
    const contrastButton = document.querySelector("[data-action='contrast']");
    if (contrastButton) contrastButton.setAttribute("aria-pressed", String(state.contrast));
    localStorage.setItem(storageKey, JSON.stringify(state));
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

  document.querySelectorAll("[data-site-search]").forEach(function (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      const query = form.querySelector("input").value.trim().toLowerCase();
      const pages = [
        { terms: "transparencia portal", url: "/Portal-da-Transparencia/" },
        { terms: "institucional informacoes estrutura organizacional organograma norma", url: "/Portal-da-Transparencia/Institucional/Informacoes/" },
        { terms: "receita receitas prevista arrecadada realização", url: "/Portal-da-Transparencia/Receitas/PrevistaArrecada/" },
        { terms: "recursos humanos estagiarios estágio", url: "/Portal-da-Transparencia/RecursosHumanos/Estagiarios/" },
        { terms: "mapa do site acessibilidade", url: "/mapa-do-site/" }
      ];
      const result = pages.find(function (page) { return page.terms.includes(query); });
      if (result) window.location.href = result.url;
      else alert("Nenhuma página do protótipo foi encontrada para essa pesquisa.");
    });
  });

  applyState();
})();
