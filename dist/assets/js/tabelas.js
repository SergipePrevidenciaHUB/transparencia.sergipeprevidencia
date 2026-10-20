(function () {
  function normalize(value) {
    return String(value).normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLocaleLowerCase("pt-BR");
  }

  function setupFilter(form) {
    const target = document.getElementById(form.dataset.target);
    if (!target) return;
    const rows = Array.from(target.querySelectorAll("tbody tr"));
    const count = document.querySelector(`[data-count-for="${form.dataset.target}"]`);
    const uoSelect = form.querySelector("[data-uo-filter]");
    const uoFilter = uoSelect && window.PortalUoFilter;
    const uoCodes = (form.dataset.uoCodes || "").split(/\s+/).filter(Boolean);
    if (uoSelect && !uoFilter) throw new Error("Carregue filtro-uo.js antes de tabelas.js para ativar o filtro por UO.");
    // Somente número e descrição dos atos; não inclui datas ou notas de revisão.
    const searchTexts = new Map(rows.map(function (row) {
      return [row, normalize(Array.from(row.querySelectorAll("[data-search-text]")).map(function (cell) {
        return cell.textContent;
      }).join(" "))];
    }));

    function apply() {
      const values = Object.fromEntries(new FormData(form).entries());
      const terms = normalize(values.palavra || "").trim().split(/\s+/).filter(Boolean);
      let visible = 0;
      rows.forEach(function (row) {
        const matchesYear = !values.ano || row.dataset.year === values.ano;
        const matchesMonth = !values.mes || row.dataset.month === values.mes;
        const matchesType = !values.tipo || row.dataset.type === values.tipo;
        const matchesText = terms.every(function (term) { return searchTexts.get(row).includes(term); });
        const matchesUo = !uoSelect || uoFilter.matches(
          row.dataset.codigoUo, row.dataset.uoConfirmada === "true", uoSelect.value, uoCodes
        );
        const matches = matchesYear && matchesMonth && matchesType && matchesText && matchesUo;
        row.hidden = !matches;
        if (matches) visible += 1;
      });
      if (count) count.textContent = `${visible} registro(s) encontrado(s).`;
    }

    form.addEventListener("submit", function (event) { event.preventDefault(); apply(); });
    form.addEventListener("reset", function () { window.setTimeout(apply, 0); });
    if (uoSelect) uoSelect.addEventListener("change", apply);
    apply();
  }

  document.querySelectorAll("[data-table-filter]").forEach(setupFilter);
})();
