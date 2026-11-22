/* Uzun sayfa düzeni: sağ sütundaki "Bu sayfada" listesinde okunan bölüm işaretlenir */
(function(){
  var yan = document.querySelector('.yan-toc'); if (!yan || !('IntersectionObserver' in window)) return;
  var links = {}, aktif = null;
  yan.querySelectorAll('a[href^="#"]').forEach(function(a){ links[decodeURIComponent(a.getAttribute('href').slice(1))] = a; });
  function isaretle(id){
    if (aktif === id) return; aktif = id;
    Object.keys(links).forEach(function(k){ links[k].classList.toggle('on', k === id); });
  }
  var gorunen = {};
  var io = new IntersectionObserver(function(es){
    es.forEach(function(en){ gorunen[en.target.id] = en.isIntersecting ? en.boundingClientRect.top : undefined; });
    var ilk = Object.keys(links).filter(function(k){ return gorunen[k] !== undefined; })[0];
    if (ilk) isaretle(ilk);
  }, { rootMargin: '-80px 0px -55% 0px' });
  Object.keys(links).forEach(function(id){ var h = document.getElementById(id); if (h) io.observe(h); });
})();
