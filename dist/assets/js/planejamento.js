(function () {
  "use strict";
  document.querySelectorAll("[data-planejamento-filter]").forEach(form => {
    const table = document.getElementById(form.dataset.target);
    if (!table) return;
    const rows = Array.from(table.querySelectorAll("tbody tr"));
    const count = document.querySelector(`[data-count-for="${table.id}"]`);
    function apply() {
      const values = new FormData(form);
      let visible = 0;
      rows.forEach(row => {
        row.hidden = Boolean((values.get("ano") && values.get("ano") !== row.dataset.year) ||
          (values.get("unidade") && values.get("unidade") !== row.dataset.unit) ||
          (values.get("mes") && values.get("mes") !== row.dataset.month));
        if (!row.hidden) visible += 1;
      });
      if (count) count.textContent = `${visible} registro(s) encontrado(s).`;
    }
    form.addEventListener("submit", event => { event.preventDefault(); apply(); });
    form.addEventListener("change", apply);
    form.addEventListener("reset", () => window.setTimeout(apply, 0));
    apply();
  });
})();
