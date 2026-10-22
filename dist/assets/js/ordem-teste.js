(function () {
  "use strict";
  const f=document.getElementById("filtro-ordem"), t=document.getElementById("tabela-ordem");
  if (!f || !t || !t.querySelector("[data-dado-sintetico]")) return;
  const rows=Array.from(t.tBodies[0].rows), b=document.getElementById("exportar-ordem");
  let selected=rows;
  function apply() {
    selected=rows.filter(r=>(!f.elements.ano.value || r.dataset.year===f.elements.ano.value) && (!f.elements.mes.value || r.dataset.mes===f.elements.mes.value) && r.cells[3].textContent.toLocaleLowerCase("pt-BR").includes(f.elements.credor.value.trim().toLocaleLowerCase("pt-BR")));
    const set=new Set(selected); rows.forEach(r=>{r.hidden=!set.has(r);});
    document.getElementById("contagem-ordem").textContent=selected.length+" pagamentos sintéticos no recorte."; b.disabled=!selected.length;
  }
  f.addEventListener("change",apply);f.addEventListener("input",apply);f.addEventListener("submit",e=>{e.preventDefault();apply();});f.addEventListener("reset",()=>setTimeout(apply,0));
  b.addEventListener("click",()=>{
    if (!selected.length) return;
    const data=[Array.from(t.tHead.rows[0].cells).map(c=>c.textContent.trim())].concat(selected.map(r=>Array.from(r.cells).map(c=>c.textContent.trim())));
    const quote=v=>'"'+v.replace(/"/g,'""')+'"';
    const text="\uFEFF"+data.map(r=>r.map(quote).join(";")).join("\r\n")+"\r\n";
    const url=URL.createObjectURL(new Blob([text],{type:"text/csv;charset=utf-8"}));const a=document.createElement("a");a.href=url;a.download="ordem-SINTETICOS-TESTE-SERIGY-"+(f.elements.ano.value||"todos")+".csv";a.click();setTimeout(()=>URL.revokeObjectURL(url),0);
  });apply();
})();
