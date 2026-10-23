/* Consulta de declaração institucional; a linha de ausência não é uma operação. */
(function () {
  "use strict";
  const form=document.getElementById("filtro-convenios");
  if(!form)return;
  const table=document.getElementById("tabela-convenios"),declaration=document.getElementById("texto-declaracao").textContent;
  const period="01/2018 até 21/10/2026";
  function apply(){
    const year=form.elements.ano.value,scope=year?"Exercício consultado: "+year:"Todos os exercícios do período confirmado";
    table.caption.textContent="Declaração de ausência de transferências — "+scope;
    table.tBodies[0].rows[0].dataset.exercicioConsultado=year;
    table.querySelectorAll("[serigyEmpty]").forEach(cell=>cell.setAttribute("serigyEmpty",cell.dataset.motivoAusencia+" "+scope+"."));
    document.getElementById("contagem-convenios").textContent="0 transferências. "+scope+". Período confirmado: "+period+".";
  }
  form.addEventListener("submit",e=>{e.preventDefault();apply();});
  form.addEventListener("change",apply);form.addEventListener("reset",()=>window.setTimeout(apply,0));
  document.getElementById("csv-convenios").addEventListener("click",()=>{
    const records=[["Exercício consultado","Período confirmado","Declaração institucional","Atualização da página"],[form.elements.ano.value||"Todos",period,declaration,"22/10/2026"]];
    const quote=s=>'"'+s.replace(/"/g,'""')+'"';
    const csv="\uFEFF"+records.map(r=>r.map(quote).join(';')).join('\r\n')+'\r\n';
    const url=URL.createObjectURL(new Blob([csv],{type:"text/csv;charset=utf-8"}));
    const a=document.createElement("a");a.href=url;a.download="declaracao-transferencias-"+document.querySelector("h1").textContent.trim().replace(/\s+/g,'-')+'-'+(form.elements.ano.value||'todos')+'.csv';a.click();window.setTimeout(()=>URL.revokeObjectURL(url),0);
  });
  apply();
})();
