/* Ana sayfa köprü haritası: yayın ya da numaranın üzerine gelince o köprünün kartı.
   Dokunmatik ekranda yaya dokununca kart haritanın altında açılır; sayfaya gitmek için karttaki bağlantı. */
(function(){
  var fig = document.getElementById('kopru-harita'); if (!fig) return;
  var map = fig.querySelector('svg.map'), kut = fig.querySelector('.hk-ipucu'), veri;
  try { veri = JSON.parse(document.getElementById('kopru-veri').textContent); } catch (e) { return; }
  var byI = {}; veri.forEach(function(v){ byI[v.i] = v; });
  function esc(s){ return String(s).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
  function goster(arc, ev){
    var v = byI[arc.dataset.i]; if (!v) return;
    map.classList.add('focus');
    map.querySelectorAll('.arc').forEach(function(a){ a.classList.toggle('on', a === arc); });
    kut.innerHTML = (v.f.length ? '<div class="hi-f">' + v.f.map(function(f){ return '<img src="' + esc(f) + '" alt="">'; }).join('') + '</div>' : '')
      + '<div class="hi-t"><b>' + esc(v.t) + '</b><span class="hi-d">' + esc(v.d) + '</span><span class="hi-b">' + esc(v.b) + '</span></div>';
    kut.hidden = false;
    konum(ev);
  }
  function konum(ev){
    if (kut.hidden || !ev) return;
    var r = fig.getBoundingClientRect(), w = kut.offsetWidth, h = kut.offsetHeight;
    var x = ev.clientX - r.left + 18, y = ev.clientY - r.top + 18;
    if (x + w > r.width - 8) x = ev.clientX - r.left - w - 18;
    if (y + h > r.height - 8) y = Math.max(8, ev.clientY - r.top - h - 18);
    kut.style.left = Math.max(8, x) + 'px'; kut.style.top = y + 'px';
  }
  function gizle(){
    kut.hidden = true; map.classList.remove('focus');
    map.querySelectorAll('.arc').forEach(function(a){ a.classList.remove('on'); });
  }
  if (!matchMedia('(hover: hover)').matches) {
    fig.classList.add('dokun');
    map.querySelectorAll('.arc').forEach(function(a){
      a.addEventListener('click', function(ev){
        ev.preventDefault(); ev.stopPropagation();
        if (a.classList.contains('on') && !kut.hidden) { gizle(); return; }
        goster(a, null);
        var v = byI[a.dataset.i], u = v && v.u ? v.u : a.getAttribute('href');
        kut.querySelector('.hi-t').insertAdjacentHTML('beforeend', '<a class="hi-git" href="' + esc(u) + '">Köprüyü aç →</a>');
        kut.insertAdjacentHTML('afterbegin', '<button type="button" class="hi-kapat" aria-label="Kapat">×</button>');
        kut.querySelector('.hi-kapat').addEventListener('click', function(e){ e.stopPropagation(); gizle(); });
      });
    });
    document.addEventListener('click', function(ev){ if (!kut.hidden && !kut.contains(ev.target)) gizle(); });
    return;
  }
  map.querySelectorAll('.arc').forEach(function(a){
    a.addEventListener('mouseenter', function(ev){ goster(a, ev); });
    a.addEventListener('mousemove', konum);
    a.addEventListener('mouseleave', gizle);
    a.addEventListener('focusin', function(){ var c = a.querySelector('.num circle'); if (!c) return;
      var b = c.getBoundingClientRect(); goster(a, {clientX: b.right, clientY: b.bottom}); });
    a.addEventListener('focusout', gizle);
  });
})();
