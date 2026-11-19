(function () {
  var s = document.getElementById('etksel'), q = document.getElementById('etkq'), m = document.getElementById('etkmsg');
  if (!s) return;
  var low = function (t) { return t.replace(/I/g, 'ı').replace(/İ/g, 'i').toLowerCase(); };

  // --- süzme: ilaç grubu, ilaç adı (ticari ya da etken madde) ya da bitki adı ---
  function run() {
    var c = s.value, t = low(q.value.trim()), n = 0, ilacEslesen = 0;
    document.querySelectorAll('.etkgrp').forEach(function (g) {
      var on = !c || g.dataset.c === c, k = 0;
      // Yazılan şey bu grubun ilaç adlarından biriyse bütün grup eşleşsin
      var ilac = !!t && (g.dataset.ara || '').indexOf(t) >= 0;
      if (ilac) ilacEslesen++;
      g.querySelectorAll('tbody tr').forEach(function (r) {
        var v = on && (!t || ilac || low(r.textContent).indexOf(t) >= 0);
        r.hidden = !v; if (v) k++;
      });
      g.hidden = !k; n += k;
    });
    m.textContent = n
      ? (ilacEslesen ? 'Bu ilaçla etkileşimi bildirilen ' + n + ' bitki.' : n + ' etkileşim kaydı gösteriliyor.')
      : 'Bu seçimde katalogda bildirilmiş bir etkileşim yok. Bu, güvenli olduğu anlamına gelmez; eczacına sor.';
    try { history.replaceState(null, '', c ? '#' + c : location.pathname); } catch (e) {}
  }
  s.addEventListener('change', run);
  q.addEventListener('input', run);

  // --- "doktoruna götür" listesi: işaretlenen bitkiler burada birikir ---
  var kutu = document.getElementById('gotur'), liste = document.getElementById('goturList'), secili = [];
  function yenile() {
    if (!kutu) return;
    kutu.hidden = !secili.length;
    liste.innerHTML = secili.map(function (x) {
      return '<li><b>' + x.ad + '</b>' + (x.grup ? ' — ' + x.grup : '') + '</li>';
    }).join('');
  }
  function metin() {
    return 'Kullandığım bitkiler ve bildirilen ilaç etkileşimleri\n\n'
      + secili.map(function (x) { return '• ' + x.ad + (x.grup ? ' — ' + x.grup : ''); }).join('\n')
      + '\n\nKaynak: bitkitabani.com/rehber/ilac-etkilesimi/ · Tıbbi tavsiye değildir.';
  }
  document.addEventListener('change', function (ev) {
    var c = ev.target;
    if (!c.classList || !c.classList.contains('etkchk')) return;
    var sat = c.closest('tr'), grp = c.closest('.etkgrp');
    var ad = sat.querySelector('a') ? sat.querySelector('a').textContent : c.value;
    var gad = grp && grp.querySelector('h2') ? grp.querySelector('h2').textContent : '';
    if (c.checked) { if (!secili.some(function (x) { return x.id === c.value && x.grup === gad; })) secili.push({ id: c.value, ad: ad, grup: gad }); }
    else secili = secili.filter(function (x) { return !(x.id === c.value && x.grup === gad); });
    yenile();
  });
  var yaz = document.getElementById('goturYaz'), kop = document.getElementById('goturKopya'), sil = document.getElementById('goturSil');
  if (yaz) yaz.addEventListener('click', function () { document.body.classList.add('yazdir-gotur'); window.print(); setTimeout(function () { document.body.classList.remove('yazdir-gotur'); }, 500); });
  if (kop) kop.addEventListener('click', function () {
    var t = metin();
    if (navigator.clipboard) navigator.clipboard.writeText(t).then(function () { kop.textContent = 'Kopyalandı'; setTimeout(function () { kop.textContent = 'Kopyala'; }, 1500); });
  });
  if (sil) sil.addEventListener('click', function () {
    secili = []; document.querySelectorAll('.etkchk').forEach(function (c) { c.checked = false; }); yenile();
  });

  try { var u = new URLSearchParams(location.search).get('q'); if (u) { q.value = u; run(); } } catch (e) {}
  var h = location.hash.slice(1); if (h && s.querySelector('option[value="' + h + '"]')) { s.value = h; run(); }
})();
