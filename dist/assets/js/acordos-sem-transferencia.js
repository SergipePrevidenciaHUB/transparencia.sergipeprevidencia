/* Consulta dos registros de cooperação disponíveis, sem inferência financeira. */
(function () {
  "use strict";
  const form = document.getElementById("filtro-acordos");
  if (!form) return;
  const table = document.getElementById("tabela-acordos");
  const rows = Array.from(table.tBodies[0].rows);
  const button = document.getElementById("csv-acordos");
  const testTable = document.getElementById("tabela-ensaio-acordo");
  const testRows = testTable ? Array.from(testTable.tBodies[0].rows) : [];
  const testButton = document.getElementById("csv-ensaio-acordo");
  let matching = rows;
  function apply() {
    const year = form.elements.ano.value;
    matching = rows.filter(row => !year || row.dataset.year === year);
    rows.forEach(row => { row.hidden = !matching.includes(row); });
    document.getElementById("contagem-acordos").textContent = matching.length + " registros no recorte" + (year ? " — início da vigência em " + year : " — todos os exercícios disponíveis") + ".";
    button.disabled = !matching.length;
    testRows.forEach(row => { row.hidden = !!year && row.dataset.year !== year; });
    if (testButton) {
      const count = testRows.filter(row => !row.hidden).length;
      testButton.disabled = !count;
      document.getElementById("contagem-ensaio-acordo").textContent = count + " registro sintético no recorte" + (year ? " — " + year : "") + ".";
    }
  }
  form.addEventListener("submit", event => { event.preventDefault(); apply(); });
  form.addEventListener("change", apply);
  form.addEventListener("reset", () => window.setTimeout(apply, 0));
  button.addEventListener("click", () => {
    if (!matching.length) return;
    exportRows(table, matching, "acordos-sem-transferencia-");
  });
  if (testButton) testButton.addEventListener("click", () => {
    const visible = testRows.filter(row => !row.hidden);
    if (visible.length) exportRows(testTable, visible, "DADO-SINTETICO-TESTE-SERIGY-acordo-");
  });
  function exportRows(sourceTable, sourceRows, filename) {
    const records = [Array.from(sourceTable.tHead.rows[0].cells).map(cell => cell.textContent.trim())].concat(sourceRows.map(row => Array.from(row.cells).map(cell => {
      const a = cell.querySelector("a"); return a ? a.textContent.trim() + " — " + a.href : cell.innerText.trim();
    })));
    const quote = value => '"' + value.replace(/"/g, '""') + '"';
    const text = "\uFEFF" + records.map(row => row.map(quote).join(";")).join("\r\n") + "\r\n";
    const url = URL.createObjectURL(new Blob([text], {type: "text/csv;charset=utf-8"}));
    const a = document.createElement("a"); a.href = url; a.download = filename + (form.elements.ano.value || "todos-exercicios") + ".csv"; a.click(); window.setTimeout(() => URL.revokeObjectURL(url), 0);
  }
  apply();
})();
