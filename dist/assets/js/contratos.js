/* Consulta da relação de contratos; registros permanecem no HTML inicial. */
(function () {
  "use strict";
  function init(suffix) {
  const form = document.getElementById("filtro-contratos" + suffix);
  if (!form) return;
  const table = document.getElementById("tabela-contratos" + suffix);
  const rows = Array.from(table.tBodies[0].rows);
  const button = document.getElementById("exportar-contratos" + suffix);
  let matching = rows;
  function apply() {
    const query = form.elements.texto.value.trim().toLocaleLowerCase("pt-BR");
    matching = rows.filter(row => (!form.elements.ano.value || row.dataset.year === form.elements.ano.value) && [2, 3, 5].some(i => row.cells[i].textContent.toLocaleLowerCase("pt-BR").includes(query)));
    const selected = new Set(matching);
    rows.forEach(row => { row.hidden = !selected.has(row); });
    document.getElementById("contagem-contratos" + suffix).textContent = matching.length + " contratos no recorte.";
    button.disabled = !matching.length;
  }
  form.addEventListener("submit", event => { event.preventDefault(); apply(); });
  form.addEventListener("change", apply);
  form.addEventListener("input", apply);
  form.addEventListener("reset", () => window.setTimeout(apply, 0));
  button.addEventListener("click", () => {
    if (!matching.length) return;
    const records = [Array.from(table.tHead.rows[0].cells).map(cell => cell.textContent.trim())].concat(matching.map(row => Array.from(row.cells).map(cell => {
      const links = Array.from(cell.querySelectorAll("a"));
      return links.length ? links.map(a => a.textContent.trim() + " — " + a.href).join(" | ") : cell.textContent.trim();
    })));
    const quote = value => '"' + value.replace(/"/g, '""') + '"';
    const text = "\uFEFF" + records.map(row => row.map(quote).join(";")).join("\r\n") + "\r\n";
    const url = URL.createObjectURL(new Blob([text], {type: "text/csv;charset=utf-8"}));
    const a = document.createElement("a"); a.href = url; a.download = "contratos-" + (form.elements.ano.value || "todos-exercicios") + ".csv"; a.click(); window.setTimeout(() => URL.revokeObjectURL(url), 0);
  });
  apply();
  }
  init("");
})();
