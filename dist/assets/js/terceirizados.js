(function () {
  "use strict";
  const form = document.getElementById("filtro-terceirizados");
  if (!form) return;
  const rows = Array.from(document.querySelectorAll("#registros-terceirizados tr"));
  const link = document.getElementById("exportar-terceirizados");
  const headers = ["Ano", "Mês", "Nome completo", "Função ou atividade exercida", "Empresa empregadora"];
  const quote = value => '"' + String(value).replace(/"/g, '""') + '"';
  let url;
  function apply() {
    const values = new FormData(form);
    const selected = [];
    rows.forEach(row => {
      row.hidden = Boolean((values.get("ano") && values.get("ano") !== row.dataset.year) ||
        (values.get("mes") && values.get("mes") !== row.dataset.month));
      if (!row.hidden) selected.push(JSON.parse(row.dataset.exportValues));
    });
    document.querySelector('[data-count-for="tabela-terceirizados"]').textContent = `${selected.length} registro(s) encontrado(s).`;
    document.getElementById("terceirizados-vazio").hidden = selected.length !== 0;
    const csv = [headers].concat(selected).map(row => row.map(quote).join(";")).join("\r\n") + "\r\n";
    if (url) URL.revokeObjectURL(url);
    url = URL.createObjectURL(new Blob(["\uFEFF" + csv], {type: "text/csv;charset=utf-8"}));
    link.href = url;
    link.download = "terceirizados-" + (values.get("ano") || "todos-anos") + "-" + (values.get("mes") || "todos-meses") + ".csv";
  }
  form.addEventListener("submit", event => { event.preventDefault(); apply(); });
  form.addEventListener("change", apply);
  form.addEventListener("reset", () => window.setTimeout(apply, 0));
  link.addEventListener("click", apply);
  apply();
})();
