// Takvim: aylık ızgara, ritüeller ve toplama mevsimleri; tıklayınca ayrıntı, takvime ekle ve paylaş.
(function () {
  var root = document.querySelector('.tk'); if (!root) return;
  var D; try { D = JSON.parse(document.getElementById('tkData').textContent); } catch (e) { return; }
  var AY = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];
  var GUN = ['Pzt', 'Sal', 'Çar', 'Per', 'Cum', 'Cmt', 'Paz'];
  var TUR = { halk: 'Halk bayramı', gok: 'Gökyüzü', and: 'And’lar' };
  var BASE = location.origin;
  var now = new Date(), y = now.getFullYear(), m = now.getMonth();
  var q = new URLSearchParams(location.search); if (q.get('ay')) { var a = +q.get('ay'); if (a >= 1 && a <= 12) m = a - 1; }
  var goster = { o: true, p: true };
  try { var f = JSON.parse(localStorage.getItem('tkFiltre') || 'null'); if (f) goster = f; } catch (e) {}
  root.querySelectorAll('[data-f]').forEach(function (c) {
    c.checked = goster[c.dataset.f] !== false;
    c.addEventListener('change', function () { goster[c.dataset.f] = c.checked; try { localStorage.setItem('tkFiltre', JSON.stringify(goster)); } catch (e) {} ciz(); });
  });
  var esc = function (s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var pad = function (n) { return (n < 10 ? '0' : '') + n; };
  var ymd = function (d) { return d.getFullYear() + pad(d.getMonth() + 1) + pad(d.getDate()); };
  function olayAraligi(o, yil) {
    if (o.t.length === 2) { var mm = +o.t - 1; return [new Date(yil, mm, 1), new Date(yil, mm + 1, 0)]; }
    var p = o.t.split('-'); var g = new Date(yil, +p[0] - 1, +p[1]); return [g, g];
  }
  function ciz() {
    root.querySelector('.tk-baslik').textContent = AY[m] + ' ' + y;
    // bu ay doğada
    var ayEl = root.querySelector('.tk-ay');
    var bitk = D.p.filter(function (x) { return x.ay.indexOf(m + 1) >= 0; });
    var aylik = D.o.filter(function (o) { return o.t.length === 2 && +o.t === m + 1; });
    var h = '';
    if (goster.o && aylik.length) h += '<div class="tk-ay-s"><b>Bu ay boyunca</b> ' + aylik.map(function (o) { return '<button class="tk-e tk-o-' + o.tur + '" data-o="' + o.s + '">' + esc(o.ad) + '</button>'; }).join('') + '</div>';
    if (goster.p) h += '<div class="tk-ay-s"><b>' + AY[m] + ' ayında doğada toplananlar</b> ' + (bitk.length ? bitk.map(function (x) { return '<button class="tk-e tk-k-' + x.k + '" data-p="' + x.id + '">' + esc(x.ad) + '</button>'; }).join('') : '<span class="muted-s">Bu ay katalogda toplama mevsimi olan bir bitki yok.</span>') +
      (bitk.length ? ' <button class="linkbtn tk-ayekle" data-ay="' + (m + 1) + '">Bu ayın listesini takvime ekle</button>' : '') + '</div>';
    ayEl.innerHTML = h;
    // ızgara
    var ilk = new Date(y, m, 1), bas = (ilk.getDay() + 6) % 7, son = new Date(y, m + 1, 0).getDate();
    var gunluk = {};
    if (goster.o) D.o.forEach(function (o) {
      if (o.t.length === 2) return;
      var r = olayAraligi(o, y); if (r[0].getMonth() === m) (gunluk[r[0].getDate()] = gunluk[r[0].getDate()] || []).push(o);
    });
    var g = '<div class="tk-row tk-hd">' + GUN.map(function (x) { return '<div>' + x + '</div>'; }).join('') + '</div><div class="tk-row">';
    var bugun = new Date(); var hucre = 0;
    for (var i = 0; i < bas; i++) { g += '<div class="tk-c tk-bos"></div>'; hucre++; }
    for (var d = 1; d <= son; d++) {
      var bu = bugun.getFullYear() === y && bugun.getMonth() === m && bugun.getDate() === d;
      g += '<div class="tk-c' + (bu ? ' tk-bu' : '') + (gunluk[d] ? ' tk-dolu' : '') + '"><span class="tk-n">' + d + '</span>' +
        (gunluk[d] || []).map(function (o) { return '<button class="tk-e tk-o-' + o.tur + '" data-o="' + o.s + '">' + esc(o.ad) + '</button>'; }).join('') + '</div>';
      hucre++; if (hucre % 7 === 0 && d < son) g += '</div><div class="tk-row">';
    }
    while (hucre % 7) { g += '<div class="tk-c tk-bos"></div>'; hucre++; }
    root.querySelector('.tk-grid').innerHTML = g + '</div>';
  }
  function gcal(baslik, d1, d2, aciklama, yillik) {
    return 'https://calendar.google.com/calendar/render?action=TEMPLATE&text=' + encodeURIComponent(baslik) + '&dates=' + ymd(d1) + '/' + ymd(d2) + '&details=' + encodeURIComponent(aciklama) + (yillik ? '&recur=' + encodeURIComponent('RRULE:FREQ=YEARLY') : '');
  }
  function icsEsc(t) { return String(t).replace(/\\/g, '\\\\').replace(/;/g, '\\;').replace(/,/g, '\\,').replace(/\n/g, '\\n'); }
  function ics(olaylar, ad) {
    var L = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Bitki Tabani//TR', 'CALSCALE:GREGORIAN'];
    olaylar.forEach(function (e, i) {
      L.push('BEGIN:VEVENT', 'UID:' + Date.now() + '-' + i + '@bitkitabani.com', 'DTSTAMP:' + new Date().toISOString().replace(/[-:]/g, '').slice(0, 15) + 'Z',
        'DTSTART;VALUE=DATE:' + ymd(e.d1), 'DTEND;VALUE=DATE:' + ymd(e.d2), 'SUMMARY:' + icsEsc(e.baslik), 'DESCRIPTION:' + icsEsc(e.aciklama), 'URL:' + e.url);
      if (e.yillik) L.push('RRULE:FREQ=YEARLY');
      L.push('BEGIN:VALARM', 'TRIGGER:-P1D', 'ACTION:DISPLAY', 'DESCRIPTION:' + icsEsc(e.baslik), 'END:VALARM', 'END:VEVENT');
    });
    L.push('END:VCALENDAR');
    var blob = new Blob([L.join('\r\n') + '\r\n'], { type: 'text/calendar;charset=utf-8' });
    var a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = ad + '.ics'; document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }
  function paylas(baslik, metin, url, btn) {
    if (navigator.share) { navigator.share({ title: baslik, text: metin, url: url }).catch(function () {}); return; }
    var t = baslik + ' · ' + url;
    (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(function () { btn.textContent = 'Bağlantı kopyalandı'; }, function () { prompt('Bağlantıyı kopyala:', url); });
  }
  var dlg = root.querySelector('.tk-dlg'), ic = root.querySelector('.tk-ic'), aktif = null;
  function ac(html, ev) {
    aktif = ev; ic.innerHTML = html + '<div class="tk-btns"><a class="cta small" target="_blank" rel="noopener" href="' + gcal(ev.baslik, ev.d1, ev.d2, ev.aciklama, ev.yillik) + '">Google Takvim’e ekle</a><button class="cta small ghost" data-act="ics">Apple / Outlook (.ics)</button><button class="cta small ghost" data-act="pay">Paylaş</button></div>';
    if (dlg.showModal) dlg.showModal(); else dlg.setAttribute('open', '');
  }
  function sonraki(o) { var r = olayAraligi(o, y); var sonY = new Date(); if (r[1] < new Date(sonY.getFullYear(), sonY.getMonth(), sonY.getDate()) && y <= sonY.getFullYear()) r = olayAraligi(o, y + 1); return r; }
  function olayAc(slug) {
    var o = D.o.find(function (x) { return x.s === slug; }); if (!o) return;
    var r = sonraki(o), d2 = new Date(r[1]); d2.setDate(d2.getDate() + 1);
    var tarih = o.t.length === 2 ? AY[r[0].getMonth()] + ' boyunca' : r[0].getDate() + ' ' + AY[r[0].getMonth()] + ' ' + r[0].getFullYear();
    var url = BASE + '/takvim/#' + o.s;
    var html = '<span class="tk-etiket tk-o-' + o.tur + '">' + TUR[o.tur] + '</span><h3>' + esc(o.ad) + '</h3><p class="tk-tarih">' + tarih + '</p><p>' + esc(o.kisa) + '</p>' +
      (o.not ? '<p class="tk-not"><b>Hazırlık:</b> ' + esc(o.not) + '</p>' : '') +
      (o.b.length ? '<p class="tk-bit"><b>Bitkileri:</b> ' + o.b.map(function (b) { return '<a href="/' + b[0] + '/">' + esc(b[1]) + '</a>'; }).join(', ') + '</p>' : '') +
      '<p class="muted-s"><a href="/takvim/#' + o.s + '">Ayrıntı ve kaynaklar</a> · <a href="' + o.l[0] + '">' + esc(o.l[1]) + '</a></p>';
    ac(html, { baslik: o.ad, d1: r[0], d2: d2, aciklama: o.kisa + (o.not ? ' ' + o.not : '') + ' ' + url, url: url, yillik: true, metin: o.kisa });
  }
  function bitkiAc(id) {
    var x = D.p.find(function (p) { return p.id === id; }); if (!x) return;
    var ay = x.ay.indexOf(m + 1) >= 0 ? m + 1 : x.ay[0], yil = y;
    var d1 = new Date(yil, ay - 1, 1), d2 = new Date(yil, ay - 1, 2);
    var url = BASE + '/' + x.id + '/';
    var html = '<span class="tk-etiket tk-k-' + x.k + '">' + esc(D.k[x.k]) + '</span><h3>' + esc(x.ad) + '</h3><p class="tk-tarih">Toplama ayları: ' + x.ay.map(function (a) { return AY[a - 1]; }).join(', ') + '</p><p>' + esc(x.m) + '</p>' +
      '<p class="tk-not"><b>Doğada bulamazsan:</b> ' + (x.a ? 'kurutulmuş hâli aktarlarda satılır. Almadan önce bitkinin sayfasındaki “kurutulmuş hâli” fotoğrafıyla karşılaştır, Latince adını sor.' : 'aktarda ararken Latince adını sor ve bitkinin sayfasındaki karıştırma notuna bak.') + '</p>' +
      '<p class="muted-s"><a href="/' + x.id + '/">' + esc(x.ad) + ' sayfası →</a></p>';
    ac(html, { baslik: '🌿 ' + x.ad + ' toplama mevsimi', d1: d1, d2: d2, aciklama: x.m + ' ' + url, url: url, yillik: true, metin: x.ad + ': ' + x.m });
  }
  ic.addEventListener('click', function (e) {
    var b = e.target.closest('[data-act]'); if (!b || !aktif) return;
    if (b.dataset.act === 'ics') ics([aktif], aktif.baslik.replace(/[^\wçğıöşüÇĞİÖŞÜ]+/g, '-'));
    if (b.dataset.act === 'pay') paylas(aktif.baslik, aktif.metin, aktif.url, b);
  });
  root.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b || dlg.contains(b)) return;
    if (b.dataset.o) olayAc(b.dataset.o);
    else if (b.dataset.p) bitkiAc(b.dataset.p);
    else if (b.classList.contains('tk-nav')) { m += +b.dataset.d; if (m < 0) { m = 11; y--; } if (m > 11) { m = 0; y++; } ciz(); }
    else if (b.classList.contains('tk-bugun')) { y = now.getFullYear(); m = now.getMonth(); ciz(); }
    else if (b.classList.contains('tk-ayekle')) {
      var ay = +b.dataset.ay;
      ics(D.p.filter(function (x) { return x.ay.indexOf(ay) >= 0; }).map(function (x) {
        return { baslik: '🌿 ' + x.ad + ' toplama mevsimi', d1: new Date(y, ay - 1, 1), d2: new Date(y, ay - 1, 2), aciklama: x.m + ' ' + BASE + '/' + x.id + '/', url: BASE + '/' + x.id + '/', yillik: false };
      }), 'toplama-' + AY[ay - 1].toLowerCase());
    }
  });
  dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
  ciz();
  var h = decodeURIComponent(location.hash.slice(1));
  if (h && D.o.some(function (o) { return o.s === h; }) && root.dataset.odak === 'o') {
    var o = D.o.find(function (x) { return x.s === h; }); var r = sonraki(o); y = r[0].getFullYear(); m = r[0].getMonth(); ciz();
  }
})();
