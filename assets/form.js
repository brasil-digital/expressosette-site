// Envia o formulario de pedido pro endpoint do clean-scout (VPS) e manda pra /thanks/.
(function () {
  var params = new URLSearchParams(location.search);
  document.querySelectorAll("form.lead").forEach(function (f) {
    f.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var msg = f.querySelector(".msg");
      var d = Object.fromEntries(new FormData(f).entries());
      msg.className = "msg err";
      if (!d.service || !d.town || !d.name) { msg.textContent = "Please fill in service, town and name."; return; }
      if (!d.phone && !d.email) { msg.textContent = "Please add a phone number or an email so we can reply."; return; }
      if (!d.consent) { msg.textContent = "Please check the consent box so we can contact you."; return; }
      d.page = location.pathname;
      ["utm_source", "utm_medium", "utm_campaign", "gclid"].forEach(function (k) { if (params.get(k)) d[k] = params.get(k); });
      var btn = f.querySelector("button");
      btn.disabled = true; msg.className = "msg"; msg.textContent = "Sending...";
      fetch(f.dataset.endpoint, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(d) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); location.href = "/thanks/"; })
        .catch(function () {
          btn.disabled = false; msg.className = "msg err";
          msg.textContent = "Sorry, something went wrong. Please try again in a minute.";
        });
    });
  });
})();
