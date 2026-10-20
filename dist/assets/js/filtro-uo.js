(function (root) {
  "use strict";

  // A confirmação vem da revisão da fonte; o código não a deduz do nome ou valor.
  function matches(code, confirmed, selected, allowedCodes) {
    if (confirmed !== true || typeof code !== "string" || !/^\d{5}$/.test(code)) return false;
    if (typeof selected !== "string" || !allowedCodes) return false;
    var allowed = false;
    for (var i = 0; i < allowedCodes.length; i += 1) {
      if (allowedCodes[i] === code) allowed = true;
    }
    return allowed && (selected === "" || selected === code);
  }

  var api = { matches: matches };
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.PortalUoFilter = api;
})(this);
