/* Ensaio identificado; a declaração institucional permanece independente. */
(function () {
  "use strict";
  const form = document.getElementById("filtro-sancoes");
  if (!form) return;
  const table = document.getElementById("tabela-sancoes");
  const rows = Array.from(table.tBodies[0].rows);
  const button = document.getElementById("csv-sancoes");
  let matching = rows;
  function apply() {
    const year = form.elements.exercicio.value;
    matching = rows.filter(row => !year || row.dataset.year === year);
    rows.forEach(row => { row.hidden = !matching.includes(row); });
    document.getElementById("contagem-sancoes").textContent = matching.length + " registros sintéticos no recorte" + (year ? " — " + year : " — todos os exercícios de teste") + ".";
    button.disabled = !matching.length;
  }
  form.addEventListener("submit", event => { event.preventDefault(); apply(); });
  form.addEventListener("change", apply);
  form.addEventListener("reset", () => window.setTimeout(apply, 0));
  button.addEventListener("click", () => {
    if (!matching.length) return;
    const data = [Array.from(table.tHead.rows[0].cells).map(cell => cell.textContent.trim())].concat(matching.map(row => Array.from(row.cells).map(cell => cell.textContent.trim())));
    const quote = value => '"' + value.replace(/"/g, '""') + '"';
    const csv = "\uFEFF" + data.map(row => row.map(quote).join(";")).join("\r\n") + "\r\n";
    const url = URL.createObjectURL(new Blob([csv], {type: "text/csv;charset=utf-8"}));
    const a = document.createElement("a"); a.href = url; a.download = "sancoes-SINTETICOS-TESTE-SERIGY-" + (form.elements.exercicio.value || "todos") + ".csv"; a.click(); window.setTimeout(() => URL.revokeObjectURL(url), 0);
  });
  apply();
})();
