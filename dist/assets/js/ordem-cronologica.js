(function () {
  "use strict";
  const form = document.getElementById("filtro-ordem");
  const table = document.getElementById("tabela-ordem");
  if (!form || !table || !document.querySelector("[data-ordem-reais]")) return;
  const rows = Array.from(table.tBodies[0].rows);
  const button = document.getElementById("exportar-ordem");
  const status = document.getElementById("contagem-ordem");
  const norm = value => value.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase().trim();
  const money = cents => {
    const sign = cents < 0n ? "-" : "";
    const value = cents < 0n ? -cents : cents;
    return "R$ " + sign + (value / 100n).toLocaleString("pt-BR") + "," + String(value % 100n).padStart(2, "0");
  };
  let selected = rows;

  function apply() {
    const f = form.elements;
    const name = norm(f.credor.value);
    selected = rows.filter(row => {
      const visible = (!f.ano.value || row.dataset.ano === f.ano.value)
        && (!f.mes.value || row.dataset.mes === f.mes.value)
        && (!f.fonte.value || row.cells[5].textContent === f.fonte.value)
        && (!f.categoria.value || row.cells[6].textContent === f.categoria.value)
        && norm(row.cells[3].textContent).includes(name);
      row.hidden = !visible;
      return visible;
    });
    const labels = [f.ano, f.mes, f.fonte, f.categoria].filter(el => el.value)
      .map(el => el.selectedOptions[0].textContent);
    if (name) labels.push(f.credor.value.trim());
    status.textContent = (selected.length ? selected.length + " pagamento(s)." : "Nenhum pagamento neste recorte.")
      + (labels.length ? " Consulta: " + labels.join(" · ") + "." : "");
    for (const field of ["pago", "bruto", "retido"]) {
      const sum = selected.reduce((total, row) => total + BigInt(row.dataset[field]), 0n);
      document.getElementById("total-" + field + "-ordem").textContent = money(sum);
    }
    button.disabled = !selected.length;
  }

  form.addEventListener("submit", event => { event.preventDefault(); apply(); });
  form.addEventListener("change", apply);
  form.elements.credor.addEventListener("input", apply);
  form.addEventListener("reset", () => setTimeout(apply, 0));
  button.addEventListener("click", () => {
    // Exporta somente linhas de pagamentos; não exporta os totais como registros.
    const values = [Array.from(table.tHead.rows[0].cells, cell => cell.textContent.trim())]
      .concat(selected.map(row => Array.from(row.cells, cell => cell.textContent.trim())));
    const quote = value => '"' + value.replace(/"/g, '""') + '"';
    const csv = "\uFEFF" + values.map(row => row.map(quote).join(";")).join("\r\n") + "\r\n";
    const url = URL.createObjectURL(new Blob([csv], { type: "text/csv;charset=utf-8" }));
    const link = document.createElement("a");
    link.href = url;
    link.download = "ordem-cronologica.csv";
    document.body.appendChild(link);
    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  });
  apply();
})();
