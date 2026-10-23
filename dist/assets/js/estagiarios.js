(function () {
  "use strict";
  const form = document.getElementById("filtro-estagiarios");
  if (!form) return;
  const rows = Array.from(document.querySelectorAll("#estagiarioTabela tbody tr"));
  const link = document.getElementById("exportar-estagiarios");
  const headers = ["Ano de Exercício", "Mês do Exercício", "Nome", "Setor/Local", "Data de Contratação", "Data de Término do Contrato (ou Desligamento)", "Houve Aditivo?"];
  const quote = value => '"' + String(value).replace(/"/g, '""') + '"';
  let url;
  function apply() {
    const values = new FormData(form);
    const selected = [];
    rows.forEach(row => {
      row.hidden = [["ano_contratacao", "anoContratacao"], ["ano_relacao", "anoRelacao"], ["mes_relacao", "mesRelacao"]]
        .some(([field, key]) => values.get(field) && values.get(field) !== row.dataset[key]);
      if (!row.hidden) selected.push(JSON.parse(row.dataset.exportValues));
    });
    document.querySelector('[data-count-for="estagiarioTabela"]').textContent = `${selected.length} registro(s) encontrado(s).`;
    document.getElementById("estagiarios-vazio").hidden = selected.length !== 0;
    const csv = [headers].concat(selected).map(row => row.map(quote).join(";")).join("\r\n") + "\r\n";
    if (url) URL.revokeObjectURL(url);
    url = URL.createObjectURL(new Blob(["\uFEFF" + csv], {type: "text/csv;charset=utf-8"}));
    link.href = url;
    link.download = "estagiarios-contratacao-" + (values.get("ano_contratacao") || "todos") + "-relacao-" + (values.get("ano_relacao") || "todos") + "-" + (values.get("mes_relacao") || "todos-meses") + ".csv";
  }
  form.addEventListener("submit", event => { event.preventDefault(); apply(); });
  form.addEventListener("change", apply);
  form.addEventListener("reset", () => window.setTimeout(apply, 0));
  link.addEventListener("click", apply);
  apply();
})();
