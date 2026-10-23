(function () {
  const form = document.getElementById('ep-filtro');
  if (!form) return;
  const table = document.getElementById('ep-tabela'), rows = Array.from(table.tBodies[0].rows);
  const button = document.getElementById('ep-csv'), documentInput = form.elements.documento;
  let matching = [];
  function apply() {
    const doc = documentInput.value.trim();
    documentInput.setCustomValidity('');
    if (/^[\d.\-\s]+$/.test(doc) && doc.replace(/\D/g, '').length === 11 || doc.includes('*')) {
      documentInput.setCustomValidity('Informe um CNPJ ou identificador público, exceto CPF.');
      documentInput.reportValidity(); return;
    }
    const text = value => value.toLocaleLowerCase('pt-BR');
    matching = rows.filter(row => row.dataset.ano === form.elements.ano.value &&
      (!form.elements.mes.value || row.dataset.mes === form.elements.mes.value) &&
      (!form.elements.entidade.value || row.dataset.entidade === form.elements.entidade.value) &&
      text(row.cells[0].textContent).includes(text(form.elements.numero.value.trim())) &&
      text(row.cells[3].textContent).includes(text(form.elements.nome.value.trim())) &&
      (!doc || row.dataset.tipo !== 'CPF' && row.cells[2].textContent.replace(/[.\/\-\s]/g, '').toLowerCase().includes(doc.replace(/[.\/\-\s]/g, '').toLowerCase())));
    const selected = new Set(matching);
    rows.forEach(row => { row.hidden = !selected.has(row); });
    document.getElementById('ep-status').textContent = matching.length + ' registros no recorte.';
    table.dataset.consulta = String(Number(table.dataset.consulta || 0) + 1);
    button.disabled = !matching.length;
  }
  documentInput.addEventListener('input', () => documentInput.setCustomValidity(''));
  form.addEventListener('submit', event => { event.preventDefault(); apply(); });
  form.querySelectorAll('select').forEach(select => select.addEventListener('change', apply));
  form.addEventListener('reset', () => { documentInput.setCustomValidity(''); setTimeout(apply, 0); });
  button.addEventListener('click', () => {
    if (!matching.length) return;
    const records = [Array.from(table.tHead.rows[0].cells).slice(0,19)].concat(matching.map(row => Array.from(row.cells).slice(0,19)));
    const csv = '\uFEFF' + records.map(record => record.map(cell => '"'+cell.textContent.trim().replace(/"/g,'""')+'"').join(';')).join('\r\n')+'\r\n';
    const url = URL.createObjectURL(new Blob([csv], {type:'text/csv;charset=utf-8'}));
    const a = document.createElement('a'); a.href = url; a.download = 'empenhos-publicos-'+form.elements.ano.value+'.csv';a.click();setTimeout(() => URL.revokeObjectURL(url),0);
  });
  apply();
})();
