/* Ensaio sintético identificado; dados permanecem no HTML inicial. */
(function () {
  "use strict";
  const form = document.getElementById("filtro-relatorio-sic");
  if (!form) return;
  const table = document.getElementById("tabela-relatorio-sic");
  const rows = Array.from(table.tBodies[0].rows);
  const button = document.getElementById("csv-relatorio-sic");
  const status = document.getElementById("contagem-relatorio-sic");
  const warning = document.getElementById("aviso-sic-sintetico").textContent.trim();
  let matching = rows;
  function apply() {
    const year = form.elements.exercicio.value;
    matching = rows.filter(row => !year || row.dataset.year === year);
    rows.forEach(row => { row.hidden = !matching.includes(row); });
    status.textContent = matching.length + " registros sintéticos no recorte" + (year ? " — exercício " + year : " — todos os exercícios de teste") + ".";
    button.disabled = matching.length === 0;
  }
  form.addEventListener("submit", event => { event.preventDefault(); apply(); });
  form.addEventListener("change", apply);
  form.addEventListener("reset", () => window.setTimeout(apply, 0));
  button.addEventListener("click", () => {
    if (!matching.length) return;
    const records = [Array.from(table.tHead.rows[0].cells).map(cell => cell.textContent.trim()).concat("Natureza dos dados")]
      .concat(matching.map(row => Array.from(row.cells).map(cell => cell.textContent.trim()).concat(warning)));
    const quote = value => '"' + value.replace(/"/g, '""') + '"';
    const csv = "\uFEFF" + records.map(row => row.map(quote).join(";")).join("\r\n") + "\r\n";
    const url = URL.createObjectURL(new Blob([csv], {type: "text/csv;charset=utf-8"}));
    const link = document.createElement("a"); link.href = url;
    link.download = "sic-SINTETICOS-TESTE-SERIGY-" + (form.elements.exercicio.value || "todos-exercicios") + ".csv";
    link.click(); window.setTimeout(() => URL.revokeObjectURL(url), 0);
  });
  apply();
})();
