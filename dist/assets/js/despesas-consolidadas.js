/* 4.1/4.2: detalhes mensais reais; cada linha participa uma única vez. */
(function () {
  const form = document.getElementById('dc-filtro');
  if (!form) return;
  const table = document.getElementById('dc-tabela');
  const rows = Array.from(table.tBodies[0].rows);
  const download = document.getElementById('dc-csv');
  const measures = ['empenhado', 'liquidado', 'pago'];
  const items = ['valorEmpenhado', 'valorLiquidado', 'valorPago'];
  let matching = [];
  function money(n) {
    const negative = n < 0n;
    if (negative) n = -n;
    return (negative ? '-' : '') + (n / 100n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.') + ',' + (n % 100n).toString().padStart(2, '0');
  }
  function apply() {
    matching = rows.filter(row => row.dataset.ano === form.elements.ano.value &&
      (!form.elements.mes.value || row.dataset.mes === form.elements.mes.value) &&
      (!form.elements.entidade.value || row.dataset.entidade === form.elements.entidade.value) &&
      (!form.elements.elemento.value || row.dataset.elemento === form.elements.elemento.value));
    const selected = new Set(matching);
    rows.forEach(row => { row.hidden = !selected.has(row); });
    measures.forEach((measure, i) => {
      const cell = document.getElementById('dc-' + measure);
      cell.textContent = matching.length ? 'R$ ' + money(matching.reduce((sum, row) => sum + BigInt(row.dataset[measure]), 0n)) : '—';
      if (matching.length) cell.setAttribute('serigyItem', items[i]);
      else cell.removeAttribute('serigyItem');
    });
    document.getElementById('dc-status').textContent = matching.length ? matching.length + ' registros no recorte.' : 'Nenhum registro encontrado para o recorte.';
    table.dataset.consulta = String(Number(table.dataset.consulta || 0) + 1);
    download.disabled = !matching.length;
  }
  form.addEventListener('submit', event => { event.preventDefault(); apply(); });
  form.addEventListener('change', apply);
  form.addEventListener('reset', () => setTimeout(apply, 0));
  download.addEventListener('click', () => {
    if (!matching.length) return;
    const records = [Array.from(table.tHead.rows[0].cells)].concat(matching.map(row => Array.from(row.cells)));
    const csv = '\uFEFF' + records.map(record => record.map(cell => '"' + cell.textContent.trim().replace(/"/g, '""') + '"').join(';')).join('\r\n') + '\r\n';
    const url = URL.createObjectURL(new Blob([csv], {type: 'text/csv;charset=utf-8'}));
    const a = document.createElement('a'); a.href = url;
    a.download = 'despesas-' + form.elements.ano.value + '-' + (form.elements.mes.value || 'meses-disponiveis') + '-' + (form.elements.entidade.value || 'todas-entidades') + '.csv';
    a.click(); setTimeout(() => URL.revokeObjectURL(url), 0);
  });
  apply();
})();
