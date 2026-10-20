// Fixture isolada, fora de dist. Executar com node ou cscript.exe //nologo.
(function () {
  var api;
  if (typeof require === "function") {
    api = require("../dist/assets/js/filtro-uo.js");
  } else {
    var fso = new ActiveXObject("Scripting.FileSystemObject");
    var root = fso.GetParentFolderName(fso.GetParentFolderName(WScript.ScriptFullName));
    var file = fso.OpenTextFile(fso.BuildPath(root, "dist\\assets\\js\\filtro-uo.js"), 1);
    var source = file.ReadAll();
    file.Close();
    var module = { exports: {} };
    eval(source);
    api = module.exports;
  }

  var checks = 0;
  function assert(value, message) {
    if (!value) throw new Error(message);
    checks += 1;
  }
  var receitas = ["37201", "37401", "37403"];
  var despesas = ["37201", "37202", "37401", "37403"];
  var records = [
    { id: "a", code: "37201", confirmed: true, year: "2026", month: "01", value: 10 },
    { id: "b", code: "37401", confirmed: true, year: "2026", month: "02", value: 10 },
    { id: "c", code: "37403", confirmed: true, year: "2025", month: "01", value: 10 },
    { id: "d", code: "37202", confirmed: true, year: "2026", month: "01", value: 10 },
    { id: "e", confirmed: false, year: "2026", month: "01", value: 10 },
    { id: "f", code: "37201", confirmed: false, year: "2026", month: "01", value: 10 }
  ];
  function select(code, allowed, year, month) {
    var result = [];
    for (var i = 0; i < records.length; i += 1) {
      var row = records[i];
      if (api.matches(row.code, row.confirmed, code, allowed) &&
          (!year || row.year === year) && (!month || row.month === month)) result.push(row);
    }
    return result;
  }

  assert(select("", receitas).length === 3, "Todas/receitas deve listar apenas as tres UOs confirmadas");
  assert(select("", despesas).length === 4, "Todas/despesas deve admitir SPSM");
  assert(select("37201", receitas).length === 1, "Uma UO nao inclui linha sem confirmacao");
  assert(select("37401", receitas)[0] === records[1], "Selecao deve preservar o registro original");
  assert(select("37202", receitas).length === 0, "SPSM nao e opcao propria de receitas");
  assert(select("37202", despesas).length === 1, "SPSM e UO de despesas");
  assert(select("99999", despesas).length === 0, "Selecao fora do escopo deve retornar zero registros");
  assert(select("Todas", despesas).length === 0, "Todas usa valor vazio, nao codigo ficticio");
  assert(!api.matches(undefined, true, "", receitas), "Codigo ausente nao pode ser atribuido");
  assert(!api.matches("37201", "true", "", receitas), "API exige confirmacao booleana explicita");
  assert(!api.matches(37201, true, "", receitas), "Codigo numerico nao deve ser convertido implicitamente");
  assert(!api.matches(" 37201", true, "", receitas), "Codigo malformado nao deve ser corrigido por suposicao");
  assert(!api.matches("37201", true, "", []), "Lista de UOs vazia nao deve liberar linhas");
  assert(select("", receitas, "2026", "01").length === 1, "UO deve combinar com ano e mes");
  assert(select("37401", receitas, "2026", "01").length === 0, "UO nao pode reexibir linha fora do mes");
  assert(select("", receitas, "2025", "01")[0] === records[2], "Todas deve respeitar o exercicio");
  assert(select("", receitas)[0] === records[0], "Limpar UO deve restaurar a listagem confirmada");
  assert(records.length === 6 && records[4].code === undefined && records[0].value === 10,
    "Filtro nao deve remover linhas, atribuir UO ou alterar valores");
  assert(select("", receitas)[0] !== select("", receitas)[1], "Valores iguais em UOs distintas nao sao deduplicados");
  assert(typeof api.total === "undefined", "Componente nao deve calcular consolidacao");

  var message = "PASS: " + checks + " verificacoes isoladas; fixture fora de dist.";
  if (typeof WScript !== "undefined") WScript.Echo(message);
  else console.log(message);
})();
