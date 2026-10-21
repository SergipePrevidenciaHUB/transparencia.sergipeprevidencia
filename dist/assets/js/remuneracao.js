(function () {
  "use strict";
  const form = document.getElementById("filtro-remuneracao");
  if (!form) return;
  const records = Array.from(document.querySelectorAll("#registros-remuneracao tr"))
    .map(row => ({row, values: JSON.parse(row.dataset.exportValues)}));
  const link = document.getElementById("exportar-remuneracao");
  const headers = ["Ano da competência", "Mês da competência", "Nome completo", "Cargo/função", "Valor de rendimentos do contracheque"];
  const normalize = value => String(value).normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLocaleLowerCase("pt-BR");
  const quote = value => '"' + String(value).replace(/"/g, '""') + '"';
  let url;
  function apply() {
    const values = new FormData(form);
    const terms = normalize(values.get("nome") || "").trim().split(/\s+/).filter(Boolean);
    const selected = [];
    records.forEach(record => {
      const data = record.values;
      record.row.hidden = Boolean((values.get("ano") && values.get("ano") !== data[0]) ||
        (values.get("mes") && values.get("mes") !== data[1]) || !terms.every(term => normalize(data[2]).includes(term)));
      if (!record.row.hidden) selected.push(data);
    });
    document.querySelector('[data-count-for="tabela-remuneracao"]').textContent = `${selected.length} registro(s) encontrado(s).`;
    document.getElementById("remuneracao-vazio").hidden = selected.length !== 0;
    const csv = [headers].concat(selected).map(row => row.map(quote).join(";")).join("\r\n") + "\r\n";
    if (url) URL.revokeObjectURL(url);
    url = URL.createObjectURL(new Blob(["\uFEFF" + csv], {type: "text/csv;charset=utf-8"}));
    link.href = url;
    link.download = "remuneracao-" + (values.get("ano") || "todos-anos") + "-" + (values.get("mes") || "todos-meses") + ".csv";
  }
  form.addEventListener("submit", event => { event.preventDefault(); apply(); });
  form.addEventListener("change", apply);
  form.addEventListener("input", apply);
  form.addEventListener("reset", () => window.setTimeout(apply, 0));
  link.addEventListener("click", apply);
  apply();
})();
