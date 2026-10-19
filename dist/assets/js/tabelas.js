(function () {
  function setupFilter(form) {
    const target = document.getElementById(form.dataset.target);
    if (!target) return;
    const rows = Array.from(target.querySelectorAll("tbody tr"));
    const count = document.querySelector(`[data-count-for="${form.dataset.target}"]`);

    function apply() {
      const values = Object.fromEntries(new FormData(form).entries());
      let visible = 0;
      rows.forEach(function (row) {
        const matchesYear = !values.ano || row.dataset.year === values.ano;
        const matchesMonth = !values.mes || row.dataset.month === values.mes;
        const matches = matchesYear && matchesMonth;
        row.hidden = !matches;
        if (matches) visible += 1;
      });
      if (count) count.textContent = `${visible} registro(s) encontrado(s).`;
    }

    form.addEventListener("submit", function (event) { event.preventDefault(); apply(); });
    form.addEventListener("reset", function () { window.setTimeout(apply, 0); });
    apply();
  }

  document.querySelectorAll("[data-table-filter]").forEach(setupFilter);
})();
