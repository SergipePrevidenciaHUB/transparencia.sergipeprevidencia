/* Consulta somente totais por UO/período previamente conciliados e presentes no HTML.
   Não interpreta movimentos, saldos, consolidação ou referência de atualização. */
(function () {
  const form = document.getElementById("despesas-totais-filtro");
  if (!form) return;
  const table = document.getElementById("despesas-totais-tabela");
  const result = document.getElementById("despesas-totais-resultados");
  const status = document.getElementById("despesas-totais-status");
  const download = document.getElementById("despesas-totais-csv");
  const year = form.elements.ano;
  const month = form.elements.mes;
  const unit = form.elements.codigo_uo;
  const codes = new Set(["37201", "37202", "37401", "37403"]);
  const rows = Array.from(table.querySelectorAll("tbody tr"));
  const items = ["valorEmpenhado", "valorLiquidado", "valorPago"];
  const ready = rows.length > 0 && rows.every(function (row) {
    return /^\d{4}$/.test(row.dataset.exercicio || "") &&
      /^(?:[1-9]|1[0-2])$/.test(row.dataset.mes || "") &&
      codes.has(row.dataset.codigoUo) && row.dataset.uoConfirmada === "true" &&
      row.cells.length === 6 && items.every(function (item) {
        const cell = row.querySelector('[serigyItem="' + item + '"]');
        return cell && /^-?(?:R\$\s*)?\d[\d.]*,\d{2}$/.test(cell.textContent.trim());
      });
  });
  if (!ready) {
    // Sem opções históricas presumidas, exportação vazia ou marca de controle inativo.
    status.textContent = "Consulta indisponível enquanto os dados oficiais não forem disponibilizados.";
    return;
  }
  year.replaceChildren(new Option("Todos os exercícios disponíveis", ""));
  Array.from(new Set(rows.map(function (row) { return row.dataset.exercicio; })))
    .sort().reverse().forEach(function (value) {
      const option = new Option(value, value);
      option.setAttribute("serigyValue", value);
      year.add(option);
    });
  form.querySelectorAll("select, button").forEach(function (control) { control.disabled = false; });
  form.setAttribute("serigyItem", "filtroPesquisa");
  year.setAttribute("serigyItem", "historicoExercicio");
  result.hidden = false;
  function visibleRows() { return rows.filter(function (row) { return !row.hidden; }); }
  function apply() {
    rows.forEach(function (row) {
      row.hidden = !!((year.value && row.dataset.exercicio !== year.value) ||
        (month.value && row.dataset.mes !== month.value) ||
        (unit.value && row.dataset.codigoUo !== unit.value));
    });
    const count = visibleRows().length;
    status.textContent = count + " registro(s) no recorte. Valores por UO e período; sem total conjunto.";
    download.disabled = count === 0;
    download.textContent = count ? "Baixar recorte em CSV" : "Baixar recorte em CSV — sem registros";
    if (count) {
      download.setAttribute("serigyItem", "salvarRelatorio");
      download.setAttribute("serigyValue", "csv");
    } else {
      download.removeAttribute("serigyItem");
      download.removeAttribute("serigyValue");
    }
  }
  function escapeCsv(value) { return '"' + value.replace(/"/g, '""') + '"'; }
  download.addEventListener("click", function () {
    const selected = visibleRows();
    if (!selected.length) return;
    const records = [Array.from(table.querySelectorAll("thead th")).map(function (cell) { return cell.textContent.trim(); })]
      .concat(selected.map(function (row) { return Array.from(row.cells).map(function (cell) { return cell.textContent.trim(); }); }));
    const csv = "\uFEFF" + records.map(function (record) { return record.map(escapeCsv).join(";"); }).join("\r\n") + "\r\n";
    const url = URL.createObjectURL(new Blob([csv], {type: "text/csv;charset=utf-8"}));
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.download = "despesas-totais-" + (year.value || "exercicios-disponiveis") + "-" + (month.value || "meses-disponiveis") + "-" + (unit.value || "todas-uo") + ".csv";
    anchor.click();
    window.setTimeout(function () { URL.revokeObjectURL(url); }, 0);
  });
  form.addEventListener("submit", function (event) { event.preventDefault(); apply(); });
  form.addEventListener("reset", function () { window.setTimeout(apply, 0); });
  apply();
})();
