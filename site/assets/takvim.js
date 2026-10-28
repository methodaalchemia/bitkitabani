// Takvimler: ritüeller için "yılın çarkı" + kartlar, doğa için yıllık toplama çizelgesi.
// Her öğeye dokununca ayrıntı; Google Takvim, Apple/Outlook (.ics) ve paylaş.
(function () {
  var root = document.querySelector('.tk'); if (!root) return;
  var D; try { D = JSON.parse(document.getElementById('tkData').textContent); } catch (e) { return; }
  var AY = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];
  var AYK = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
  var TUR = { halk: 'Halk bayramı', gok: 'Gökyüzü', and: 'And’lar' };
  var BASE = location.origin, now = new Date(), bugun = new Date(now.getFullYear(), now.getMonth(), now.getDate()), cm = now.getMonth() + 1;
  var esc = function (s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var pad = function (n) { return (n < 10 ? '0' : '') + n; };
  var ymd = function (d) { return d.getFullYear() + pad(d.getMonth() + 1) + pad(d.getDate()); };
  function aralik(o, yil) {
    if (o.t.length === 2) { var mm = +o.t - 1; return [new Date(yil, mm, 1), new Date(yil, mm + 1, 0)]; }
    var p = o.t.split('-'); var g = new Date(yil, +p[0] - 1, +p[1]); return [g, g];
  }
  function siradaki(o) { var r = aralik(o, bugun.getFullYear()); if (r[1] < bugun) r = aralik(o, bugun.getFullYear() + 1); return r; }
  function olayEv(o) {
    var r = siradaki(o), d2 = new Date(r[1]); d2.setDate(d2.getDate() + 1); var url = BASE + '/takvim/#' + o.s;
    return { baslik: o.ad, d1: r[0], d2: d2, aciklama: o.kisa + (o.not ? ' ' + o.not : '') + ' ' + url, url: url, metin: o.kisa };
  }
  function bitkiEv(x) {
    var ay = x.ay.indexOf(cm) >= 0 ? cm : (x.ay.filter(function (a) { return a > cm; })[0] || x.ay[0]);
    var yil = ay < cm ? bugun.getFullYear() + 1 : bugun.getFullYear(), url = BASE + '/' + x.id + '/';
    return { baslik: '🌿 ' + x.ad + ' toplama mevsimi', d1: new Date(yil, ay - 1, 1), d2: new Date(yil, ay - 1, 2), aciklama: x.m + ' ' + url, url: url, metin: x.ad + ': ' + x.m };
  }
  function gcal(e) {
    return 'https://calendar.google.com/calendar/render?action=TEMPLATE&text=' + encodeURIComponent(e.baslik) + '&dates=' + ymd(e.d1) + '/' + ymd(e.d2) + '&details=' + encodeURIComponent(e.aciklama) + '&recur=' + encodeURIComponent('RRULE:FREQ=YEARLY');
  }
  function icsEsc(t) { return String(t).replace(/\\/g, '\\\\').replace(/;/g, '\\;').replace(/,/g, '\\,').replace(/\n/g, '\\n'); }
  function ics(list, ad) {
    var L = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Bitki Tabani//TR', 'CALSCALE:GREGORIAN'];
    list.forEach(function (e, i) {
      L.push('BEGIN:VEVENT', 'UID:' + Date.now() + '-' + i + '@bitkitabani.com', 'DTSTAMP:' + new Date().toISOString().replace(/[-:]/g, '').slice(0, 15) + 'Z',
        'DTSTART;VALUE=DATE:' + ymd(e.d1), 'DTEND;VALUE=DATE:' + ymd(e.d2), 'RRULE:FREQ=YEARLY', 'SUMMARY:' + icsEsc(e.baslik), 'DESCRIPTION:' + icsEsc(e.aciklama), 'URL:' + e.url,
        'BEGIN:VALARM', 'TRIGGER:-P1D', 'ACTION:DISPLAY', 'DESCRIPTION:' + icsEsc(e.baslik), 'END:VALARM', 'END:VEVENT');
    });
    L.push('END:VCALENDAR');
    var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([L.join('\r\n') + '\r\n'], { type: 'text/calendar;charset=utf-8' })); a.download = ad + '.ics';
    document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }
  function paylas(e, btn) {
    if (navigator.share) { navigator.share({ title: e.baslik, text: e.metin, url: e.url }).catch(function () {}); return; }
    (navigator.clipboard ? navigator.clipboard.writeText(e.baslik + ' · ' + e.url) : Promise.reject()).then(function () { btn.textContent = 'Bağlantı kopyalandı ✓'; }, function () { prompt('Bağlantıyı kopyala:', e.url); });
  }
  function dugmeler(key) {
    return '<div class="tk-btns" data-ev="' + key + '"><a class="tk-b tk-b1" target="_blank" rel="noopener" data-act="g">Google Takvim’e ekle</a><button class="tk-b" data-act="ics">Apple / Outlook</button><button class="tk-b" data-act="pay">Paylaş</button></div>';
  }
  function evOf(key) { var k = key.split(':'); if (k[0] === 'o') return olayEv(D.o.find(function (o) { return o.s === k[1]; })); return bitkiEv(D.p.find(function (x) { return x.id === k[1]; })); }
  function tarihMetni(o) { var r = siradaki(o); return o.t.length === 2 ? AY[r[0].getMonth()] + ' boyunca' : r[0].getDate() + ' ' + AY[r[0].getMonth()] + ' ' + r[0].getFullYear(); }
  function kalan(o) { var r = siradaki(o); if (r[0] <= bugun) return 'Şu anda'; var g = Math.round((r[0] - bugun) / 864e5); return g === 1 ? 'Yarın' : g + ' gün sonra'; }
  function olayHtml(o, kart) {
    return (kart ? '' : '<span class="tk-etiket tk-o-' + o.tur + '">' + TUR[o.tur] + '</span>') + '<h3>' + esc(o.ad) + '</h3><p class="tk-tarih">' + tarihMetni(o) + ' · ' + kalan(o) + '</p><p>' + esc(o.kisa) + '</p>' +
      (o.not ? '<p class="tk-not"><b>Hazırlık:</b> ' + esc(o.not) + '</p>' : '') +
      (o.b.length ? '<p class="tk-bit"><b>Bitkileri:</b> ' + o.b.map(function (b) { return '<a href="/' + b[0] + '/">' + esc(b[1]) + '</a>'; }).join(', ') + '</p>' : '') +
      dugmeler('o:' + o.s) + '<p class="muted-s tk-lnk"><a href="/takvim/#' + o.s + '">Ayrıntı ve kaynaklar</a> · <a href="' + o.l[0] + '">' + esc(o.l[1]) + '</a></p>';
  }
  function bitkiHtml(x) {
    return '<span class="tk-etiket tk-k-' + x.k + '">' + esc(D.k[x.k]) + '</span><h3>' + esc(x.ad) + '</h3><p class="tk-tarih">Toplama ayları: ' + x.ay.map(function (a) { return AY[a - 1]; }).join(', ') + '</p><p>' + esc(x.m) + '</p>' +
      '<p class="tk-not"><b>Doğada bulamazsan:</b> ' + (x.a ? 'kurutulmuş hâli aktarlarda satılır. Almadan önce bitkinin sayfasındaki “kurutulmuş hâli” fotoğrafıyla karşılaştır, Latince adını sor.' : 'aktarda ararken Latince adını sor ve bitkinin sayfasındaki karıştırma notuna bak.') + '</p>' +
      dugmeler('p:' + x.id) + '<p class="muted-s tk-lnk"><a href="/' + x.id + '/">' + esc(x.ad) + ' sayfası →</a></p>';
  }
  var dlg = root.querySelector('.tk-dlg'), ic = root.querySelector('.tk-ic');
  function ac(html) { ic.innerHTML = html; hazirla(ic); if (dlg.showModal) dlg.showModal(); else dlg.setAttribute('open', ''); }
  function hazirla(el) { el.querySelectorAll('.tk-btns').forEach(function (b) { var a = b.querySelector('[data-act="g"]'); if (a) a.href = gcal(evOf(b.dataset.ev)); }); }

  // ---------- Ritüeller: yılın çarkı + kartlar ----------
  function cark() {
    var S = 360, C = S / 2, R1 = 150, R0 = 112, yil = bugun.getFullYear();
    var ac2 = function (d) { var b = new Date(d.getFullYear(), 0, 1); var g = (d - b) / 864e5; return g / 365.25 * 360 - 90; };
    var pt = function (a, r) { var t = a * Math.PI / 180; return [C + r * Math.cos(t), C + r * Math.sin(t)]; };
    var yay = function (a1, a2, r0, r1) {
      var p1 = pt(a1, r1), p2 = pt(a2, r1), p3 = pt(a2, r0), p4 = pt(a1, r0), b = (a2 - a1) > 180 ? 1 : 0;
      return 'M' + p1 + 'A' + r1 + ',' + r1 + ' 0 ' + b + ' 1 ' + p2 + 'L' + p3 + 'A' + r0 + ',' + r0 + ' 0 ' + b + ' 0 ' + p4 + 'Z';
    };
    var mevsim = [['kis', -90, ac2(new Date(yil, 2, 20))], ['ilk', ac2(new Date(yil, 2, 20)), ac2(new Date(yil, 5, 21))], ['yaz', ac2(new Date(yil, 5, 21)), ac2(new Date(yil, 8, 22))], ['son', ac2(new Date(yil, 8, 22)), ac2(new Date(yil, 11, 21))], ['kis', ac2(new Date(yil, 11, 21)), 270]];
    var g = '<svg class="tk-cark" viewBox="0 0 ' + S + ' ' + S + '" role="img" aria-label="Yılın çarkı: ritüel ve mevsim takvimi">';
    mevsim.forEach(function (m) { g += '<path class="tk-mv tk-mv-' + m[0] + '" d="' + yay(m[1], m[2], R0, R1) + '"/>'; });
    for (var i = 0; i < 12; i++) {
      var a = ac2(new Date(yil, i, 1)), p0 = pt(a, R0), p1 = pt(a, R1 + 6);
      g += '<line class="tk-ayc" x1="' + p0[0] + '" y1="' + p0[1] + '" x2="' + p1[0] + '" y2="' + p1[1] + '"/>';
      var am = ac2(new Date(yil, i, 15)), pl = pt(am, R1 + 16);
      g += '<text class="tk-ayl' + (i === bugun.getMonth() ? ' tk-ayl-bu' : '') + '" x="' + pl[0] + '" y="' + pl[1] + '" text-anchor="middle" dominant-baseline="middle">' + AYK[i] + '</text>';
    }
    D.o.forEach(function (o) {
      var r = aralik(o, yil);
      if (o.t.length === 2) { g += '<path class="tk-oy tk-o-' + o.tur + '" data-o="' + o.s + '" tabindex="0" role="button" aria-label="' + esc(o.ad) + '" d="' + yay(ac2(r[0]), ac2(r[1]) + 1, R0 - 16, R0 - 4) + '"><title>' + esc(o.ad) + '</title></path>'; return; }
      var p = pt(ac2(r[0]), (R0 + R1) / 2);
      g += '<circle class="tk-od tk-o-' + o.tur + '" data-o="' + o.s + '" tabindex="0" role="button" aria-label="' + esc(o.ad) + '" cx="' + p[0] + '" cy="' + p[1] + '" r="9"><title>' + esc(o.ad) + '</title></circle>';
    });
    var pn = pt(ac2(bugun), R1 + 2), pc = pt(ac2(bugun), 30);
    g += '<line class="tk-ibre" x1="' + pc[0] + '" y1="' + pc[1] + '" x2="' + pn[0] + '" y2="' + pn[1] + '"/><circle class="tk-ibre-u" cx="' + pn[0] + '" cy="' + pn[1] + '" r="4"/>';
    var sr = D.o.slice().sort(function (a, b) { return siradaki(a)[0] - siradaki(b)[0]; })[0];
    g += '<text class="tk-mrk1" x="' + C + '" y="' + (C - 18) + '" text-anchor="middle">Bugün</text><text class="tk-mrk2" x="' + C + '" y="' + (C + 4) + '" text-anchor="middle">' + bugun.getDate() + ' ' + AY[bugun.getMonth()] + '</text>';
    g += '<text class="tk-mrk1" x="' + C + '" y="' + (C + 26) + '" text-anchor="middle">Sıradaki: ' + esc(sr.ad) + '</text>';
    return g + '</svg>';
  }
  function ritueller() {
    var L = D.o.slice().sort(function (a, b) { return siradaki(a)[0] - siradaki(b)[0]; });
    var kart = L.map(function (o) { return '<article class="tk-kart tk-o-' + o.tur + '" id="k-' + o.s + '"><span class="tk-etiket tk-o-' + o.tur + '">' + TUR[o.tur] + '</span>' + olayHtml(o, true) + '</article>'; }).join('');
    root.querySelector('.tk-govde').innerHTML = '<div class="tk-cark-w">' + cark() + '<div class="tk-lgs">' +
      Object.keys(TUR).map(function (k) { return '<span class="tk-lg tk-o-' + k + '">' + TUR[k] + '</span>'; }).join('') + '</div></div><div class="tk-kartlar">' + kart + '</div>';
    hazirla(root.querySelector('.tk-kartlar'));
  }

  // ---------- Doğa: yıllık toplama çizelgesi ----------
  var kisimF = 'hepsi', sadeceSimdi = false;
  function cizelge() {
    var L = D.p.filter(function (x) { return (kisimF === 'hepsi' || x.k === kisimF) && (!sadeceSimdi || x.ay.indexOf(cm) >= 0); });
    L.sort(function (a, b) { var A = a.ay.indexOf(cm) >= 0, B = b.ay.indexOf(cm) >= 0; return A === B ? 0 : A ? -1 : 1; });
    var h = '<div class="tk-cz" role="table" aria-label="Yıllık toplama çizelgesi"><div class="tk-cz-r tk-cz-h" role="row"><div class="tk-cz-ad" role="columnheader">Bitki</div>' +
      AYK.map(function (a, i) { return '<div role="columnheader" class="' + (i + 1 === cm ? 'tk-cz-bu' : '') + '">' + a + '</div>'; }).join('') + '</div>';
    var rit = '<div class="tk-cz-r tk-cz-rit" role="row"><div class="tk-cz-ad" role="rowheader">Ritüeller</div>';
    for (var m = 1; m <= 12; m++) {
      var bu = D.o.filter(function (o) { return +o.t.split('-')[0] === m; });
      rit += '<div class="' + (m === cm ? 'tk-cz-bu' : '') + '">' + bu.map(function (o) { return '<button class="tk-rd tk-o-' + o.tur + '" data-o="' + o.s + '" title="' + esc(o.ad) + '" aria-label="' + esc(o.ad) + '"></button>'; }).join('') + '</div>';
    }
    h += rit + '</div>';
    h += L.map(function (x) {
      var s = '<div class="tk-cz-r" role="row"><button class="tk-cz-ad tk-k-' + x.k + '" data-p="' + x.id + '" role="rowheader">' + esc(x.ad) + '</button>';
      for (var m = 1; m <= 12; m++) {
        var on = x.ay.indexOf(m) >= 0, sol = on && x.ay.indexOf(m === 1 ? 12 : m - 1) < 0, sag = on && x.ay.indexOf(m === 12 ? 1 : m + 1) < 0;
        s += '<div role="cell" class="' + (m === cm ? 'tk-cz-bu' : '') + '">' + (on ? '<button class="tk-bar tk-k-' + x.k + (sol ? ' tk-bar-s' : '') + (sag ? ' tk-bar-e' : '') + '" data-p="' + x.id + '" aria-label="' + esc(x.ad) + ', ' + AY[m - 1] + '"></button>' : '') + '</div>';
      }
      return s + '</div>';
    }).join('');
    h += '</div>';
    var n = D.p.filter(function (x) { return x.ay.indexOf(cm) >= 0; }).length;
    root.querySelector('.tk-govde').innerHTML = '<div class="tk-ozet"><b>' + AY[cm - 1] + ':</b> ' + n + ' bitkinin toplama mevsimi. <button class="linkbtn tk-ayekle">Bu ayın listesini takvime ekle</button></div>' +
      '<div class="tk-filtre" role="group" aria-label="Kullanılan kısım"><button class="tk-f' + (kisimF === 'hepsi' ? ' on' : '') + '" data-k="hepsi">Hepsi</button>' +
      Object.keys(D.k).filter(function (k) { return D.p.some(function (x) { return x.k === k; }); }).map(function (k) { return '<button class="tk-f tk-k-' + k + (kisimF === k ? ' on' : '') + '" data-k="' + k + '">' + D.k[k] + '</button>'; }).join('') +
      '<label class="tk-simdi-f"><input type="checkbox"' + (sadeceSimdi ? ' checked' : '') + '> Yalnızca bu ay</label></div>' +
      '<div class="tk-cz-w">' + h + '</div>';
    var w = root.querySelector('.tk-cz-w'), bu = w.querySelector('.tk-cz-h .tk-cz-bu'), ad = w.querySelector('.tk-cz-h .tk-cz-ad');
    if (bu && w.scrollWidth > w.clientWidth) w.scrollLeft = Math.max(0, bu.offsetLeft - ad.offsetWidth - bu.offsetWidth * 2);
  }

  root.addEventListener('click', function (e) {
    var b = e.target.closest('[data-act]');
    if (b) { var ev = evOf(b.closest('.tk-btns').dataset.ev); if (b.dataset.act === 'ics') ics([ev], ev.baslik.replace(/[^\wçğıöşüÇĞİÖŞÜ]+/g, '-')); if (b.dataset.act === 'pay') paylas(ev, b); return; }
    var t = e.target.closest('[data-o],[data-p],.tk-f,.tk-ayekle'); if (!t || dlg.contains(t) && !t.dataset.o && !t.dataset.p) return;
    if (t.dataset.o) {
      var k = root.querySelector('#k-' + t.dataset.o);
      if (k && !dlg.contains(t)) { k.scrollIntoView({ behavior: 'smooth', block: 'center' }); k.classList.add('tk-vurgu'); setTimeout(function () { k.classList.remove('tk-vurgu'); }, 1600); }
      else ac(olayHtml(D.o.find(function (o) { return o.s === t.dataset.o; })));
    } else if (t.dataset.p) ac(bitkiHtml(D.p.find(function (x) { return x.id === t.dataset.p; })));
    else if (t.classList.contains('tk-f')) { kisimF = t.dataset.k; cizelge(); }
    else if (t.classList.contains('tk-ayekle')) ics(D.p.filter(function (x) { return x.ay.indexOf(cm) >= 0; }).map(bitkiEv), 'toplama-' + AY[cm - 1].toLowerCase());
  });
  root.addEventListener('keydown', function (e) { if ((e.key === 'Enter' || e.key === ' ') && e.target.matches('[data-o][tabindex]')) { e.preventDefault(); e.target.dispatchEvent(new MouseEvent('click', { bubbles: true })); } });
  root.addEventListener('change', function (e) { if (e.target.closest('.tk-simdi-f')) { sadeceSimdi = e.target.checked; cizelge(); } });
  dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
  if (root.dataset.odak === 'o') ritueller(); else cizelge();
  function detayAc() { var id = decodeURIComponent(location.hash.slice(1)), a = id && document.getElementById(id), d = a && a.closest('details'); if (d) { d.open = true; setTimeout(function () { a.scrollIntoView({ block: 'start' }); }, 50); } }
  window.addEventListener('hashchange', detayAc); detayAc();
  var h = decodeURIComponent(location.hash.slice(1)), k0 = h && root.querySelector('#k-' + CSS.escape(h));
  if (k0) setTimeout(function () { k0.scrollIntoView({ block: 'center' }); k0.classList.add('tk-vurgu'); }, 200);
})();
