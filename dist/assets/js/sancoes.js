(function () {
  "use strict";
  const form = document.getElementById("filtro-sancoes");
  if (!form) return;
  const declaration = document.getElementById("declaracao-sancoes").textContent.trim();
  const table = document.getElementById("tabela-sancoes");
  function apply() {
    const year = form.elements.exercicio.value;
    const scope = year ? "exercício consultado: " + year : "todo o período declarado";
    table.caption.textContent = "Declaração institucional — " + scope + ", até 21/10/2026";
    document.getElementById("contagem-sancoes").textContent = "Nenhuma pessoa sancionada na declaração institucional. Consulta: " + scope + ". Limite da declaração: 21/10/2026.";
    table.querySelector('[serigyItem="nomeSancionado"]').textContent = "Não houve licitantes ou contratados sancionados pela unidade até 21/10/2026, conforme declaração institucional — " + scope + ".";
  }
  form.addEventListener("submit", event => { event.preventDefault(); apply(); });
  form.addEventListener("change", apply);
  form.addEventListener("reset", () => window.setTimeout(apply, 0));
  document.getElementById("csv-sancoes").addEventListener("click", () => {
    apply();
    const data = [["Declaração", "Exercício consultado", "Período confirmado", "Atualização da página"], [declaration, form.elements.exercicio.value || "Todo o período declarado", "Até 21/10/2026; início do período não confirmado.", "22/10/2026"]];
    const quote = v => '"' + v.replace(/"/g, '""') + '"';
    const csv = "\uFEFF" + data.map(row => row.map(quote).join(";")).join("\r\n") + "\r\n";
    const url = URL.createObjectURL(new Blob([csv], {type: "text/csv;charset=utf-8"}));
    const a = document.createElement("a"); a.href = url; a.download = "declaracao-sancoes-" + (form.elements.exercicio.value || "periodo-declarado") + ".csv"; a.click(); window.setTimeout(() => URL.revokeObjectURL(url), 0);
  });
  apply();
})();
