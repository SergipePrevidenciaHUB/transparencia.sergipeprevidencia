/* Consulta dos registros de cooperação disponíveis, sem inferência financeira. */
(function () {
  "use strict";
  const form = document.getElementById("filtro-acordos");
  if (!form) return;
  const table = document.getElementById("tabela-acordos");
  const rows = Array.from(table.tBodies[0].rows);
  const button = document.getElementById("csv-acordos");
  let matching = rows;
  function apply() {
    const year = form.elements.ano.value;
    matching = rows.filter(row => !year || row.dataset.year === year);
    rows.forEach(row => { row.hidden = !matching.includes(row); });
    document.getElementById("contagem-acordos").textContent = matching.length + " registros no recorte" + (year ? " — início da vigência em " + year : " — todos os exercícios disponíveis") + ".";
    button.disabled = !matching.length;
  }
  form.addEventListener("submit", event => { event.preventDefault(); apply(); });
  form.addEventListener("change", apply);
  form.addEventListener("reset", () => window.setTimeout(apply, 0));
  button.addEventListener("click", () => {
    if (!matching.length) return;
    const records = [Array.from(table.tHead.rows[0].cells).map(cell => cell.textContent.trim())].concat(matching.map(row => Array.from(row.cells).map(cell => {
      const a = cell.querySelector("a"); return a ? a.textContent.trim() + " — " + a.href : cell.innerText.trim();
    })));
    const quote = value => '"' + value.replace(/"/g, '""') + '"';
    const text = "\uFEFF" + records.map(row => row.map(quote).join(";")).join("\r\n") + "\r\n";
    const url = URL.createObjectURL(new Blob([text], {type: "text/csv;charset=utf-8"}));
    const a = document.createElement("a"); a.href = url; a.download = "acordos-sem-transferencia-" + (form.elements.ano.value || "todos-exercicios") + ".csv"; a.click(); window.setTimeout(() => URL.revokeObjectURL(url), 0);
  });
  apply();
})();
