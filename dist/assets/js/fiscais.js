/* Consulta de associações; ano do instrumento não é período de designação. */
(function () {
  "use strict";
  const form = document.getElementById("filtro-fiscais");
  if (!form) return;
  const table = document.getElementById("tabela-fiscais");
  const rows = Array.from(table.tBodies[0].rows);
  const button = document.getElementById("csv-fiscais");
  let matching = rows;
  function apply() {
    const year = form.elements.ano.value;
    matching = rows.filter(row => (!year || row.dataset.year === year) && (!form.elements.funcao.value || row.dataset.role === form.elements.funcao.value) && row.cells[4].textContent.toLocaleLowerCase("pt-BR").includes(form.elements.nome.value.trim().toLocaleLowerCase("pt-BR")));
    rows.forEach(row => { row.hidden = !matching.includes(row); });
    document.getElementById("contagem-fiscais").textContent = matching.length + " registros no recorte" + (year ? " — ano do instrumento " + year : " — todos os exercícios disponíveis") + ".";
    button.disabled = !matching.length;
  }
  form.addEventListener("submit", event => { event.preventDefault(); apply(); });
  form.addEventListener("change", apply);
  form.addEventListener("input", apply);
  form.addEventListener("reset", () => window.setTimeout(apply, 0));
  button.addEventListener("click", () => {
    if (!matching.length) return;
    const records = [Array.from(table.tHead.rows[0].cells).map(cell => cell.textContent.trim())].concat(matching.map(row => Array.from(row.cells).map(cell => {
      const a = cell.querySelector("a"); return a ? a.textContent.trim() + " — " + a.href : cell.innerText.trim();
    })));
    const quote = value => '"' + value.replace(/"/g, '""') + '"';
    const text = "\uFEFF" + records.map(row => row.map(quote).join(";")).join("\r\n") + "\r\n";
    const url = URL.createObjectURL(new Blob([text], {type: "text/csv;charset=utf-8"}));
    const a = document.createElement("a"); a.href = url; a.download = "fiscais-" + (form.elements.ano.value || "todos-exercicios") + ".csv"; a.click(); window.setTimeout(() => URL.revokeObjectURL(url), 0);
  });
  apply();
})();
