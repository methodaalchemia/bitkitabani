/* Bitki bulucu: derde göre, hamilelik ve ilaç durumuna göre katalogdan süzer. Sunucuya hiçbir şey gönderilmez. */
(function () {
  var root = document.getElementById('bb'), el = document.getElementById('bbdata');
  if (!root || !el) return;
  var D = JSON.parse(el.textContent), st = { k: null, h: null, g: {} };
  var $ = function (s) { return root.querySelector(s); }, $$ = function (s) { return root.querySelectorAll(s); };
  var esc = function (t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  function show(n) {
    $$('.bbstep').forEach(function (s) { s.hidden = +s.dataset.s > n; });
    var t = $('.bbstep[data-s="' + n + '"]'); if (t && n > 1) t.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  // 1. dert
  $('.bbk').innerHTML = D.k.map(function (k) { return '<a href="#' + k.s + '" data-k="' + k.s + '">' + k.i + '<span>' + esc(k.a) + '</span></a>'; }).join('');
  $('.bbk').addEventListener('click', function (e) {
    var a = e.target.closest('a[data-k]'); if (!a) return; e.preventDefault();
    st.k = a.dataset.k; $$('.bbk a').forEach(function (x) { x.classList.toggle('on', x === a); x.setAttribute('aria-pressed', x === a); });
    show(2);
  });
  // 2. hamilelik
  $$('[data-h]').forEach(function (b) { b.addEventListener('click', function () {
    st.h = b.dataset.h === '1'; $$('[data-h]').forEach(function (x) { x.setAttribute('aria-pressed', x === b); }); show(3);
  }); });
  // 3. ilaçlar
  $('.bbg').insertAdjacentHTML('beforeend', D.g.map(function (g) { return '<button type="button" class="chip" data-g="' + g[0] + '">' + esc(g[1]) + '</button>'; }).join(''));
  $('.bbg').addEventListener('click', function (e) {
    var b = e.target.closest('[data-g]'); if (!b) return; var g = b.dataset.g;
    if (g === 'yok') st.g = {}; else { delete st.g.yok; st.g[g] = !st.g[g]; }
    if (g === 'yok') st.g.yok = true;
    $$('.bbg [data-g]').forEach(function (x) { x.setAttribute('aria-pressed', !!st.g[x.dataset.g]); });
  });
  $('.bbgo').addEventListener('click', function () { result(); show(4); });
  $('.bbagain').addEventListener('click', function () {
    st = { k: null, h: null, g: {} }; $$('[aria-pressed]').forEach(function (x) { x.setAttribute('aria-pressed', 'false'); x.classList.remove('on'); });
    show(1); root.scrollIntoView({ behavior: 'smooth' });
  });
  function result() {
    var k = D.k.filter(function (x) { return x.s === st.k; })[0]; if (!k) return;
    var ok = [], out = [];
    k.b.forEach(function (id) {
      var p = D.p[id], why = [];
      if (p.g === 'yuksek') why.push('yüksek riskli');
      if (p.y) why.push('yasal kısıtlı');
      if (st.h && p.h) why.push('hamilelik/emzirme uyarısı var');
      for (var g in st.g) if (g !== 'yok' && st.g[g] && (D.e[g] || []).indexOf(id) > -1) why.push((D.g.filter(function (x) { return x[0] === g; })[0] || [, ''])[1].split(' (')[0] + ' ile etkileşebilir');
      (why.length ? out : ok).push({ id: id, p: p, why: why });
    });
    var pip = function (n) { var s = '<span class="pips" aria-hidden="true">'; for (var i = 1; i <= 3; i++) s += '<i class="' + (i <= n ? 'on' : '') + '"></i>'; return s + '</span>'; };
    var h = '', low = function (t) { return t.replace(/I/g, 'ı').replace(/İ/g, 'i').toLowerCase(); }, U = low(k.u || '');
    var hit = Object.keys(st.g).filter(function (g) { return g !== 'yok' && st.g[g] && (D.gk[g] || []).some(function (w) { return U.indexOf(w) > -1; }); });
    if (st.h) h += '<p class="warnbox"><b>Hamilelik ve emzirme:</b> Aşağıdaki bitkilerin çoğunun hamilelikte ve emzirirken güvenli olduğunu gösteren yeterli veri yok; Avrupa İlaç Ajansı bu dönemde çoğu bitkisel ürünü önermiyor. Katalogda açık uyarısı olanları eledik, ama kalanlardan birini de denemeden önce mutlaka hekimine ya da eczacına danış.</p>';
    if (hit.length) h += '<p class="warnbox"><b>Kullandığın ilaç için dikkat:</b> ' + esc(k.u) + '</p>';
    if (ok.length) {
      h += '<ol class="bblist">' + ok.map(function (o) {
        var p = o.p, kn = D.K[p.k] || [0, ''];
        return '<li class="bbitem">' + (p.m ? '<a class="bbimg" href="/' + o.id + '/"><img src="/img/' + o.id + '-500.jpg" alt="" loading="lazy" width="96" height="128"></a>' : '') +
          '<div><h3><a href="/' + o.id + '/">' + esc(p.t) + '</a> <i lang="la">' + esc(p.l) + '</i></h3>' +
          '<p class="bbmeta">' + pip(kn[0]) + ' ' + esc(kn[1]) + ' kanıt <span class="sf ' + p.g + '">' + esc(D.G[p.g] || '') + '</span></p>' +
          '<p>' + esc(k.n[o.id] || '') + '</p>' +
          '<p class="bblinks"><a href="/' + o.id + '/">Bitki sayfası →</a>' + (p.r ? ' <a href="/tarif/' + p.r + '/">Tarifi →</a>' : '') + '</p></div></li>';
      }).join('') + '</ol>';
    } else h += '<p class="warnbox">Seçimlerine göre bu dert için katalogda güvenle önerebileceğimiz bir bitki kalmadı. Bir hekime ya da eczacıya danışmanı öneririz.</p>';
    if (out.length) h += '<details class="bbout"><summary>Senin için elenenler (' + out.length + ')</summary><ul>' + out.map(function (o) { return '<li><a href="/' + o.id + '/">' + esc(o.p.t) + '</a>: ' + esc(o.why.join(', ')) + '</li>'; }).join('') + '</ul></details>';
    if (k.u && !hit.length) h += '<p class="warnbox"><b>Dikkat:</b> ' + esc(k.u) + '</p>';
    if (st.h || Object.keys(st.g).some(function (g) { return g !== 'yok' && st.g[g]; })) h += '<p class="muted-s">Hamileysen ya da düzenli ilaç kullanıyorsan, listedeki bir bitkiye başlamadan önce de hekimine ya da eczacına sor. Bu liste yalnızca katalogda bildirilen uyarılara göre süzüldü.</p>';
    h += '<p><a href="/rehber/' + k.s + '/">' + esc(k.a) + ' rehberinin tamamı →</a></p>';
    $('.bbres').innerHTML = h;
  }
})();
