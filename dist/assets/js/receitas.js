(function(root){
  "use strict";
  const months=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"];
  const fields=["codigo_uo","unidade","ano","mes","categoria","codigo_categoria","origem","codigo_origem","especie","codigo_especie","previsto","arrecadado"];
  function matches(row,values,api,allowed,confirmed=true){
    return api.matches(String(row.codigo_uo),confirmed,values.codigo_uo||"",allowed)&&String(row.ano)===values.ano;
  }
  // Inteiros com escala da origem: somar antes de arredondar, sem ponto flutuante.
  function units(value, scale) {
    const m = /^([+-]?)(\d+)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/.exec(String(value));
    if (!m) throw new Error("Valor decimal inválido na entrada de Receitas.");
    const power = scale + Number(m[4] || 0) - (m[3] || "").length;
    if (power < 0) throw new Error("Escala decimal insuficiente.");
    return (m[1] === "-" ? -1n : 1n) * BigInt(m[2] + (m[3] || "")) * (10n ** BigInt(power));
  }
  function decimal(value, scale) {
    const negative = value < 0n;
    const text = (negative ? -value : value).toString().padStart(scale + 1, "0");
    return (negative ? "-" : "") + text.slice(0, -scale) + "." + text.slice(-scale);
  }
  function money(value, scale) {
    if (value === null) return "—";
    const factor = 10n ** BigInt(scale - 2);
    const cents = ((value < 0n ? -value : value) + factor / 2n) / factor;
    const text = cents.toString().padStart(3, "0");
    return "R$ " + (value < 0n && cents !== 0n ? "-" : "") + text.slice(0, -2).replace(/\B(?=(\d{3})+(?!\d))/g, ".") + "," + text.slice(-2);
  }
  function select(data,values,api,allowed){
    const scope=data.classificacoes.filter(r=>matches(r,values,api,allowed));
    const reference=values.mes?Number(values.mes):(scope.length?Math.max(...scope.map(r=>Number(r.mes))):null);
    const base=scope.filter(r=>Number(r.mes)<=reference);
    const annual=data.previsao_anual.filter(r=>matches(r,values,api,allowed));
    const sum=(rows,field)=>rows.reduce((v,r)=>v+units(r[field],data.escala_decimal),0n);
    const forecast=annual.length?sum(annual,"previsao_anual"):null;
    const receipt=base.length?sum(base,"arrecadado"):null;
    const coverage={};
    base.forEach(r=>{if(!coverage[r.codigo_uo])coverage[r.codigo_uo]=new Set();coverage[r.codigo_uo].add(Number(r.mes));});
    Object.keys(coverage).forEach(u=>{coverage[u]=Array.from(coverage[u]).sort((a,b)=>a-b);});
    return {aviso:data.aviso,filtros:values,recorte:{tipo:"acumulado",ano:values.ano,mes_referencia:reference,meses_disponiveis_por_uo:coverage,fechamento_confirmado:false},previsao_anual:annual,classificacoes:base,
      totais:{previsto_anual:forecast===null?null:decimal(forecast,data.escala_decimal),arrecadado:receipt===null?null:decimal(receipt,data.escala_decimal),soma_bruta_inclui_intraorcamentarias:!values.codigo_uo}};
  }
  function csv(data){
    const quote=v=>'"'+String(v===null||v===undefined?"":v).replace(/"/g,'""')+'"';
    const headers=["tipo_recorte","ano_referencia","mes_referencia_acumulado"].concat(fields.map(k=>k==="mes"?"mes_registro":k==="previsto"?"previsto_na_origem":k==="arrecadado"?"arrecadado_no_mes":k));
    const reference=data.recorte.mes_referencia===null?"":String(data.recorte.mes_referencia).padStart(2,"0");
    const rows=data.classificacoes.map(r=>["acumulado",data.recorte.ano,reference].concat(fields.map(k=>r[k])).map(quote).join(";"));
    return "\uFEFF"+headers.join(";")+"\r\n"+rows.join("\r\n")+(rows.length?"\r\n":"");
  }
  if(typeof module==="object"&&module.exports)module.exports={select,csv,units,money};
  if(typeof document==="undefined")return;
  const form=document.getElementById("receitasFiltro");
  if(!form)return;
  if(!root.PortalUoFilter)throw new Error("Carregue filtro-uo.js antes de receitas.js.");
  const data=JSON.parse(document.getElementById("receitasDados").textContent),allowed=form.dataset.uoCodes.split(/\s+/);
  const table=document.getElementById("receitaTabela"),rows=Array.from(table.querySelectorAll("tbody tr"));
  const byId=new Map(rows.map(r=>[r.id,r])),sources=new Map(rows.map(r=>[r,r.dataset.baseIndices.split(" ").map(i=>data.classificacoes[Number(i)])]));
  const expanded=new Set(),eligible=new Set(),urls={};
  function displayRows(){
    rows.forEach(row=>{
      let visible=eligible.has(row),parent=row.dataset.parentId;
      while(visible&&parent){visible=expanded.has(parent);parent=byId.get(parent).dataset.parentId;}
      row.hidden=!visible;
      const button=row.querySelector("[data-receita-toggle]");
      if(button){
        const open=expanded.has(row.id);button.setAttribute("aria-expanded",String(open));row.dataset.expanded=String(open);
        button.querySelector(".receita-acao").textContent=open?"Recolher":"Abrir";
      }
    });
  }
  function apply(){
    const values=Object.fromEntries(new FormData(form).entries()),selected=select(data,values,root.PortalUoFilter,allowed),scale=data.escala_decimal;
    const reference=selected.recorte.mes_referencia,label=reference===null?null:months[reference-1]+"/"+values.ano;
    expanded.clear();eligible.clear();
    rows.forEach(row=>{
      if(!matches({codigo_uo:row.dataset.codigoUo,ano:row.dataset.year},values,root.PortalUoFilter,allowed,row.dataset.uoConfirmada==="true"))return;
      const base=sources.get(row).filter(r=>Number(r.mes)<=reference);
      if(!base.length)return;
      eligible.add(row);
      row.querySelector("[data-accum-value]").textContent=money(base.reduce((v,r)=>v+units(r.arrecadado,scale),0n),scale);
      row.querySelector("[data-reference-label]").textContent=label;
    });
    displayRows();
    document.getElementById("receitasTotalPrevisto").textContent=selected.totais.previsto_anual===null?"—":money(units(selected.totais.previsto_anual,scale),scale);
    document.getElementById("receitasTotalArrecadado").textContent=selected.totais.arrecadado===null?"—":money(units(selected.totais.arrecadado,scale),scale);
    document.getElementById("receitasTituloArrecadado").textContent=label?"Arrecadação acumulada até "+label:"Arrecadação acumulada — sem registros no arquivo";
    document.getElementById("receitasReferenciaAnual").textContent="Exercício "+values.ano+" · "+form.elements.codigo_uo.selectedOptions[0].textContent+". A previsão é anual e não muda com o mês de referência."+(selected.previsao_anual.length?"":" Sem previsão anual informada.");
    document.getElementById("receitasReferenciaMes").textContent="Soma dos registros mensais disponíveis desde o início do exercício"+(label?" até "+label:"")+"; não presume fechamento.";
    const coverage=Object.entries(selected.recorte.meses_disponiveis_por_uo).map(([uo,list])=>"UO "+uo+": "+list.map(m=>months[m-1].toLocaleLowerCase("pt-BR")).join(", ")+"/"+values.ano);
    document.getElementById("receitasCobertura").textContent=coverage.length?"Meses presentes no acumulado — "+coverage.join("; ")+". A cobertura não comprova fechamento contábil.":"Nenhum registro mensal disponível no recorte selecionado.";
    document.getElementById("receitasSomaBruta").textContent=values.codigo_uo?"Soma dos registros da unidade, incluindo receitas intraorçamentárias presentes na fonte.":"Soma bruta dos registros, incluindo receitas intraorçamentárias. Não representa consolidação contábil.";
    document.getElementById("receitasContagem").textContent=selected.classificacoes.length+" registro(s) mensais de base no acumulado. Abra Categoria Econômica → Origem → Espécie para consultar as classificações.";
    document.getElementById("receitasVazio").hidden=selected.classificacoes.length!==0;
    document.querySelectorAll("[data-receitas-export]").forEach(link=>{
      const format=link.dataset.receitasExport;if(urls[format])URL.revokeObjectURL(urls[format]);
      urls[format]=URL.createObjectURL(new Blob([format==="csv"?csv(selected):JSON.stringify(selected,null,2)+"\n"],{type:format==="csv"?"text/csv;charset=utf-8":"application/json;charset=utf-8"}));
      link.href=urls[format];link.download="receitas-acumuladas-"+values.ano+"-"+(reference===null?"sem-registros":String(reference).padStart(2,"0"))+"."+format;
    });
  }
  table.addEventListener("click",event=>{
    const row=event.target.closest("tr"),button=row&&row.querySelector("[data-receita-toggle]");
    if(!button||event.target.closest("a,input,select,textarea"))return;
    if(!event.target.closest("button")){
      if(root.getSelection()&&!root.getSelection().isCollapsed)return;
      button.focus({preventScroll:true});
    }
    if(expanded.has(row.id))expanded.delete(row.id);else expanded.add(row.id);
    displayRows();
  });
  form.addEventListener("submit",event=>{event.preventDefault();apply();});form.addEventListener("change",apply);form.addEventListener("reset",()=>root.setTimeout(apply,0));apply();
})(this);
