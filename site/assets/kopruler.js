/* Kültür köprüleri haritası: yay ile liste arasında karşılıklı vurgu */
(function(){
  var map = document.querySelector('.map'); if (!map) return;
  var arcs = map.querySelectorAll('.arc'), cards = document.querySelectorAll('.bridge[data-i]');
  var pinned = null;
  function show(i){
    map.classList.toggle('focus', !!i);
    arcs.forEach(function(a){ a.classList.toggle('on', a.dataset.i === i); });
    cards.forEach(function(c){ c.classList.toggle('on', c.dataset.i === i); });
  }
  function bind(el){
    el.addEventListener('mouseenter', function(){ show(el.dataset.i); });
    el.addEventListener('mouseleave', function(){ show(pinned); });
    el.addEventListener('focusin', function(){ show(el.dataset.i); });
  }
  arcs.forEach(bind); cards.forEach(bind);
  arcs.forEach(function(a){
    a.addEventListener('click', function(ev){
      ev.preventDefault(); pinned = a.dataset.i; show(pinned);
      var c = document.getElementById('kopru-' + pinned);
      if (c) { c.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'center' }); c.focus({ preventScroll: true }); }
    });
  });
  cards.forEach(function(c){ c.addEventListener('click', function(){ pinned = c.dataset.i; show(pinned); }); });
  var h = location.hash.match(/^#kopru-(\d+)$/); if (h) { pinned = h[1]; show(pinned); }
})();
