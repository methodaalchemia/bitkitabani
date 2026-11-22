/* Ana sayfa köprü haritası: yayın ya da numaranın üzerine gelince o köprünün kartı.
   Dokunmatik ekranda numaraya dokunmak doğrudan köprü sayfasını açar. */
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
  if (!matchMedia('(hover: hover)').matches) return;
  map.querySelectorAll('.arc').forEach(function(a){
    a.addEventListener('mouseenter', function(ev){ goster(a, ev); });
    a.addEventListener('mousemove', konum);
    a.addEventListener('mouseleave', gizle);
    a.addEventListener('focusin', function(){ var c = a.querySelector('.num circle'); if (!c) return;
      var b = c.getBoundingClientRect(); goster(a, {clientX: b.right, clientY: b.bottom}); });
    a.addEventListener('focusout', gizle);
  });
})();
