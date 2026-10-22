(function () {
  "use strict";
  const form = document.getElementById("filtro-licitacoes");
  if (!form) return;
  const table = document.getElementById("tabela-licitacoes");
  const rows = Array.from(table.tBodies[0].rows);
  const button = document.getElementById("exportar-licitacoes");
  const testTable = document.getElementById("tabela-ensaio-licitacao");
  const testRows = testTable ? Array.from(testTable.tBodies[0].rows) : [];
  const testButton = document.getElementById("exportar-ensaio-licitacao");
  let matching = rows;
  function apply() {
    const query = form.elements.texto.value.trim().toLocaleLowerCase("pt-BR");
    const matches = row => ["ano", "modalidade", "situacao", "mes"].every(key => !form.elements[key].value || row.dataset[key === "ano" ? "year" : key] === form.elements[key].value) && row.textContent.toLocaleLowerCase("pt-BR").includes(query);
    matching = rows.filter(matches);
    const selected = new Set(matching);
    rows.forEach(row => { row.hidden = !selected.has(row); });
    document.getElementById("contagem-licitacoes").textContent = matching.length + " procedimentos no recorte.";
    button.disabled = !matching.length;
    testRows.forEach(row => { row.hidden = !matches(row); });
    if (testButton) {
      const count = testRows.filter(row => !row.hidden).length;
      testButton.disabled = !count;
      document.getElementById("contagem-ensaio-licitacao").textContent = count + " procedimento sintético no recorte.";
    }
  }
  form.addEventListener("submit", event => { event.preventDefault(); apply(); });
  form.addEventListener("change", apply);
  form.addEventListener("input", apply);
  form.addEventListener("reset", () => window.setTimeout(apply, 0));
  button.addEventListener("click", () => {
    if (!matching.length) return;
    exportRows(table, matching, "licitacoes-");
  });
  if (testButton) testButton.addEventListener("click", () => {
    const visible = testRows.filter(row => !row.hidden);
    if (visible.length) exportRows(testTable, visible, "DADO-SINTETICO-TESTE-SERIGY-licitacao-");
  });
  function exportRows(sourceTable, sourceRows, filename) {
    const records = [Array.from(sourceTable.tHead.rows[0].cells).map(c => c.textContent.trim())].concat(sourceRows.map(row => Array.from(row.cells).map(c => {
      const links = Array.from(c.querySelectorAll("a"));
      return links.length ? links.map(a => a.textContent.trim() + " — " + a.href).join(" | ") : c.textContent.trim();
    })));
    const quote = v => '"' + v.replace(/"/g, '""') + '"';
    const text = "\uFEFF" + records.map(row => row.map(quote).join(";")).join("\r\n") + "\r\n";
    const url = URL.createObjectURL(new Blob([text], {type:"text/csv;charset=utf-8"}));
    const a = document.createElement("a"); a.href = url; a.download = filename + (form.elements.ano.value || "todos") + ".csv"; a.click(); window.setTimeout(() => URL.revokeObjectURL(url), 0);
  }
  apply();
})();
