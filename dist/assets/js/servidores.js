(function () {
  "use strict";
  const form = document.getElementById("filtro-vinculos");
  if (!form) return;
  const rows = Array.from(document.querySelectorAll("#registros-vinculos tr"));
  const records = rows.map(row => ({row, values: JSON.parse(row.dataset.exportValues)}));
  const link = document.getElementById("exportar-vinculos");
  const headers = ["Ano da relação", "Mês da relação", "Nome completo", "Cargo/função", "Lotação", "Data de início de exercício", "Data de exoneração ou inativação", "Carga horária informada", "Valor de rendimentos do contracheque"];
  const quote = value => '"' + String(value).replace(/"/g, '""') + '"';
  const normalize = value => String(value).normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLocaleLowerCase("pt-BR");
  const matches = (value, query) => normalize(query).trim().split(/\s+/).filter(Boolean).every(term => normalize(value).includes(term));
  let url;
  function apply() {
    const filters = new FormData(form);
    const selected = [];
    records.forEach(({row, values}) => {
      row.hidden = Boolean((filters.get("ano") && filters.get("ano") !== values[0]) ||
        (filters.get("mes") && filters.get("mes") !== values[1]) ||
        !matches(values[2], filters.get("nome") || "") || !matches(values[3], filters.get("cargo") || ""));
      if (!row.hidden) selected.push(values);
    });
    document.querySelector('[data-count-for="tabela-vinculos"]').textContent = `${selected.length} registro(s) encontrado(s).`;
    document.getElementById("vinculos-vazio").hidden = selected.length !== 0;
    const csv = [headers].concat(selected).map(row => row.map(quote).join(";")).join("\r\n") + "\r\n";
    if (url) URL.revokeObjectURL(url);
    url = URL.createObjectURL(new Blob(["\uFEFF" + csv], {type: "text/csv;charset=utf-8"}));
    link.href = url;
    link.download = "servidores-" + (filters.get("ano") || "todos-anos") + "-" + (filters.get("mes") || "todos-meses") + ".csv";
  }
  form.addEventListener("submit", event => { event.preventDefault(); apply(); });
  form.addEventListener("change", apply);
  form.addEventListener("input", apply);
  form.addEventListener("reset", () => window.setTimeout(apply, 0));
  link.addEventListener("click", apply);
  apply();
})();
