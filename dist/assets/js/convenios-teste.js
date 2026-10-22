/* Consulta de ensaio identificada: não transforma exemplos em registros oficiais. */
(function () {
  "use strict";
  const form = document.getElementById("filtro-convenios");
  if (!form) return;
  const table = document.getElementById("tabela-convenios");
  const rows = Array.from(table.tBodies[0].rows);
  const button = document.getElementById("csv-convenios");
  let matching = rows;
  function apply() {
    const year = form.elements.ano.value;
    matching = rows.filter(row => !year || row.dataset.year === year);
    rows.forEach(row => { row.hidden = !matching.includes(row); });
    document.getElementById("contagem-convenios").textContent = matching.length + " registros sintéticos no recorte" + (year ? " — " + year : " — todos os exercícios de teste") + ".";
    button.disabled = !matching.length;
  }
  form.addEventListener("submit", event => { event.preventDefault(); apply(); });
  form.addEventListener("change", apply);
  form.addEventListener("reset", () => window.setTimeout(apply, 0));
  button.addEventListener("click", () => {
    if (!matching.length) return;
    const data = [Array.from(table.tHead.rows[0].cells).map(cell => cell.textContent.trim())].concat(matching.map(row => Array.from(row.cells).map(cell => {
      const link = cell.querySelector("a"); return link ? cell.textContent.trim() + " — " + link.href : cell.textContent.trim();
    })));
    const quote = value => '"' + value.replace(/"/g, '""') + '"';
    const csv = "\uFEFF" + data.map(row => row.map(quote).join(";")).join("\r\n") + "\r\n";
    const url = URL.createObjectURL(new Blob([csv], {type: "text/csv;charset=utf-8"}));
    const link = document.createElement("a"); link.href = url;
    link.download = "convenios-" + document.querySelector("h1").textContent.trim().replace(/\s+/g, "-") + "-SINTETICOS-TESTE-SERIGY-" + (form.elements.ano.value || "todos") + ".csv";
    link.click(); window.setTimeout(() => URL.revokeObjectURL(url), 0);
  });
  apply();
})();
