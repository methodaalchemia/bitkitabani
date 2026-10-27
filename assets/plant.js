(function(){
  var b = document.getElementById('learnBtn'); if (!b) return;
  var id = b.getAttribute('data-id'), list = [];
  try{ list = JSON.parse(localStorage.getItem('bt-learned') || '[]'); }catch(e){}
  function paint(){ var on = list.indexOf(id) > -1; b.setAttribute('aria-pressed', on ? 'true' : 'false'); b.textContent = on ? '✓ Öğrendim' : 'Öğrendim olarak işaretle'; }
  b.addEventListener('click', function(){
    var i = list.indexOf(id); if (i > -1) list.splice(i,1); else { list.push(id); if (window.BTStreak) { var n = BTStreak.mark(), st = document.getElementById('streakNote'); if (st) st.textContent = BTStreak.text(n); } }
    try{ localStorage.setItem('bt-learned', JSON.stringify(list)); }catch(e){}
    paint();
  });
  paint();
  var st = document.getElementById('streakNote'); if (st && window.BTStreak) st.textContent = BTStreak.text(BTStreak.count());
})();
/* üst galeri: noktalar kaydırmayı izler, noktaya basınca o görsele gider */
(function(){
  document.querySelectorAll('.galeri').forEach(function(g){
    var tr = g.querySelector('.g-track'), ds = g.querySelectorAll('.g-dots button');
    if (!tr || !ds.length) return;
    function set(){ var i = Math.round(tr.scrollLeft / tr.clientWidth); ds.forEach(function(d, k){ if (k === i) d.setAttribute('aria-current', 'true'); else d.removeAttribute('aria-current'); }); }
    tr.addEventListener('scroll', function(){ window.requestAnimationFrame(set); }, { passive: true }); set();
    ds.forEach(function(d, k){ d.addEventListener('click', function(){ tr.scrollTo({ left: k * tr.clientWidth, behavior: 'smooth' }); }); });
  });
})();
