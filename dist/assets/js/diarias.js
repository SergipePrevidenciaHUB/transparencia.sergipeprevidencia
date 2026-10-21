(function () {
  "use strict";
  const form = document.getElementById("filtro-relacao-diarias");
  if (!form) return;
  const table = document.getElementById("tabela-relacao-diarias");
  const rows = Array.from(table.querySelectorAll("tbody tr"));
  const link = document.getElementById("exportar-relacao-diarias");
  const headers = ["ANO", "MÊS", "NOME DO SERVIDOR", "CARGO", "DESTINO", "DESCRIÇÃO DO EVENTO", "DATA DE SAÍDA", "DATA DE RETORNO", "Nº DE DIÁRIAS", "TOTAL RECEBIDO", "SITUAÇÃO"];
  const quote = value => '"' + String(value).replace(/"/g, '""') + '"';
  let url;
  function updateExport() {
    const visible = rows.filter(row => !row.hidden);
    const content = [headers].concat(visible.map(row => JSON.parse(row.dataset.exportValues)))
      .map(values => values.map(quote).join(";")).join("\r\n");
    if (url) URL.revokeObjectURL(url);
    url = URL.createObjectURL(new Blob(["\uFEFF" + content + "\r\n"], { type: "text/csv;charset=utf-8" }));
    link.href = url;
    const values = new FormData(form);
    link.download = "relacao-diarias-" + (values.get("ano") || "todos-anos") + "-" + (values.get("mes") || "todos-meses") + ".csv";
    document.getElementById("diarias-vazio").hidden = visible.length !== 0;
  }
  // tabelas.js aplica os filtros antes deste handler; exportar somente a base visível.
  form.addEventListener("submit", updateExport);
  form.addEventListener("reset", () => window.setTimeout(updateExport, 0));
  form.addEventListener("change", () => form.requestSubmit());
  document.getElementById("nome-relacao-diarias").addEventListener("input", () => form.requestSubmit());
  link.addEventListener("click", () => form.requestSubmit());
  updateExport();
})();
