/* Consultas de Despesas: linhas no HTML; ensaio sintético exige aviso explícito.
   Sem interpretação de movimentos/saldos ou cálculo de totais/consolidação. */
(function () {
  // Apenas apresentação da natureza: categorias e grupos não são registros financeiros.
  function hierarchy(table, rows) {
    const roots = new Map();
    let sequence = 0;
    let selected = new Set(rows);
    function group(label, depth, level) {
      const row = document.createElement("tr");
      row.dataset.classificacaoNivel = level;
      const cell = row.insertCell();
      cell.colSpan = table.tHead.rows[0].cells.length;
      cell.style.paddingInlineStart = (depth * 1.25 + 0.5) + "rem";
      const button = document.createElement("button");
      button.type = "button";
      button.className = "secondary";
      button.textContent = "− " + label;
      button.setAttribute("aria-expanded", "true");
      cell.append(button);
      row.id = table.id + "-grupo-" + (++sequence);
      const node = {row: row, button: button, label: label, open: true, children: new Map(), rows: []};
      button.addEventListener("click", function () { node.open = !node.open; render(selected); });
      return node;
    }
    rows.forEach(function (row) {
      const cells = Array.from(row.cells).map(function (cell) { return cell.textContent.trim(); });
      // Isolar UO, período, função, subfunção e fonte; fonte não é filho do elemento.
      const key = JSON.stringify([row.dataset.codigoUo, row.dataset.exercicio, row.dataset.mes, cells[0], cells[3], cells[4], cells[5], cells[8]]);
      if (!roots.has(key)) roots.set(key, group("Categoria Econômica: " + cells[5] + " — " + cells[0] + " — " + cells[1] + "/" + cells[2] + " — " + cells[3] + " / " + cells[4] + " — Fonte: " + cells[8], 0, "categoria"));
      const root = roots.get(key);
      if (!root.children.has(cells[6])) root.children.set(cells[6], group("Grupo: " + cells[6], 1, "grupo"));
      const child = root.children.get(cells[6]);
      if (!row.id) row.id = table.id + "-registro-" + (++sequence);
      child.rows.push(row);
    });
    const fragment = document.createDocumentFragment();
    roots.forEach(function (root) {
      fragment.append(root.row);
      root.button.setAttribute("aria-controls", Array.from(root.children.values()).map(function (child) { return child.row.id; }).join(" "));
      root.children.forEach(function (child) {
        fragment.append(child.row);
        child.button.setAttribute("aria-controls", child.rows.map(function (row) { return row.id; }).join(" "));
        child.rows.forEach(function (row) { fragment.append(row); });
      });
    });
    table.tBodies[0].replaceChildren(fragment);
    function render(matches) {
      selected = matches;
      roots.forEach(function (root) {
        root.row.hidden = !Array.from(root.children.values()).some(function (child) { return child.rows.some(function (row) { return selected.has(row); }); });
        [root].concat(Array.from(root.children.values())).forEach(function (node) {
          node.button.setAttribute("aria-expanded", String(node.open));
          node.button.textContent = (node.open ? "− " : "+ ") + node.label;
        });
        root.children.forEach(function (child) {
          child.row.hidden = root.row.hidden || !root.open || !child.rows.some(function (row) { return selected.has(row); });
          child.rows.forEach(function (row) { row.hidden = !selected.has(row) || !root.open || !child.open; });
        });
      });
    }
    return render;
  }
  function setup(config) {
    const prefix = config.prefix;
    const form = document.getElementById(prefix + "-filtro");
    if (!form) return;
    const table = document.getElementById(prefix + "-tabela");
    const result = document.getElementById(prefix + "-resultados");
    const status = document.getElementById(prefix + "-status");
    const download = document.getElementById(prefix + "-csv");
    const synthetic = form.closest('[data-despesas-sinteticas="true"]');
    const warning = synthetic ? synthetic.dataset.avisoSintetico : "";
    const year = form.elements.ano, month = form.elements.mes, unit = form.elements.codigo_uo;
    const element = form.elements.elemento;
    const codes = new Set(["37201", "37202", "37401", "37403"]);
    const rows = Array.from(table.querySelectorAll("tbody tr"));
    function content(row, item) {
      const cell = row.querySelector('[serigyItem="' + item + '"]');
      return cell ? cell.textContent.trim() : "";
    }
    const ready = rows.length > 0 && rows.every(function (row) {
      return /^\d{4}$/.test(row.dataset.exercicio || "") && /^(?:[1-9]|1[0-2])$/.test(row.dataset.mes || "") &&
        codes.has(row.dataset.codigoUo) && row.dataset.uoConfirmada === "true" && row.cells.length === config.columns &&
        config.items.every(function (item) {
          const value = content(row, item);
          return config.money || (config.moneyItems || []).includes(item) ? /^-?(?:R\$\s*)?\d[\d.]*,\d{2}$/.test(value) : value.length > 0;
        });
    });
    if (!ready) { status.textContent = "Consulta indisponível enquanto os dados oficiais não forem disponibilizados."; return; }
    year.replaceChildren(new Option("Todos os exercícios disponíveis", ""));
    Array.from(new Set(rows.map(function (row) { return row.dataset.exercicio; }))).sort().reverse().forEach(function (value) {
      const option = new Option(value, value); option.setAttribute("serigyValue", value); year.add(option);
    });
    if (element) {
      element.replaceChildren(new Option("Todos os elementos disponíveis", ""));
      Array.from(new Set(rows.map(function (row) { return content(row, "elementoDespesa"); }))).sort().forEach(function (value) { element.add(new Option(value, value)); });
    }
    form.querySelectorAll("select, input, button").forEach(function (control) { control.disabled = false; });
    form.setAttribute("serigyItem", "filtroPesquisa"); year.setAttribute("serigyItem", "historicoExercicio"); result.hidden = false;
    const render = config.hierarchy ? hierarchy(table, rows) : function (matches) { rows.forEach(function (row) { row.hidden = !matches.has(row); }); };
    let matching = rows;
    function apply() {
      matching = rows.filter(function (row) {
        return (!year.value || row.dataset.exercicio === year.value) && (!month.value || row.dataset.mes === month.value) &&
          (!unit.value || row.dataset.codigoUo === unit.value) && (!element || !element.value || content(row, "elementoDespesa") === element.value) &&
          (config.textFilters || []).every(function (filter) {
            const value = form.elements[filter.name].value.trim().toLocaleLowerCase("pt-BR");
            return !value || row.cells[filter.column].textContent.toLocaleLowerCase("pt-BR").includes(value);
          });
      });
      render(new Set(matching));
      status.textContent = matching.length + (warning ? " registro(s) sintético(s)" : " registro(s)") + " no recorte. Valores por UO e período; sem total conjunto.";
      download.disabled = matching.length === 0;
      download.textContent = matching.length ? "Baixar recorte em CSV" : "Baixar recorte em CSV — sem registros";
      if (matching.length) { download.setAttribute("serigyItem", "salvarRelatorio"); download.setAttribute("serigyValue", "csv"); }
      else { download.removeAttribute("serigyItem"); download.removeAttribute("serigyValue"); }
    }
    function escapeCsv(value) { return '"' + value.replace(/"/g, '""') + '"'; }
    download.addEventListener("click", function () {
      if (!matching.length) return;
      const records = [Array.from(table.querySelectorAll("thead th")).map(function (cell) { return cell.textContent.trim(); })]
        .concat(matching.map(function (row) { return Array.from(row.cells).map(function (cell) { return cell.textContent.trim(); }); }));
      if (warning) {
        records[0].push("Natureza dos dados");
        records.slice(1).forEach(function (record) { record.push(warning); });
      }
      const csv = "\uFEFF" + records.map(function (record) { return record.map(escapeCsv).join(";"); }).join("\r\n") + "\r\n";
      const url = URL.createObjectURL(new Blob([csv], {type: "text/csv;charset=utf-8"}));
      const anchor = document.createElement("a"); anchor.href = url;
      anchor.download = prefix + (warning ? "-SINTETICOS-TESTE-SERIGY" : "") + "-" + (year.value || "exercicios-disponiveis") + "-" + (month.value || "meses-disponiveis") + "-" + (unit.value || "todas-uo") + ".csv";
      anchor.click(); window.setTimeout(function () { URL.revokeObjectURL(url); }, 0);
    });
    form.addEventListener("submit", function (event) { event.preventDefault(); apply(); });
    form.addEventListener("reset", function () { window.setTimeout(apply, 0); }); apply();
  }
  setup({prefix: "despesas-totais", columns: 6, money: true, items: ["valorEmpenhado", "valorLiquidado", "valorPago"]});
  setup({prefix: "despesas-classificacao", columns: 9, hierarchy: true, items: ["unidadeDespesa", "funcaoDespesa", "subFuncaoDespesa", "categoriaDespesa", "grupoDespesa", "elementoDespesa", "fonteRecursosDespesa"]});
  setup({prefix: "despesas-empenhos", columns: 10, moneyItems: ["valorEmpenhoIndividual"], items: ["credorEmpenho", "valorEmpenhoIndividual", "objetoEmpenho", "modalidadeEmpenho", "numeroProcedimento"], textFilters: [{name: "numero_empenho", column: 3}, {name: "credor", column: 4}, {name: "documento", column: 5}]});
})();
