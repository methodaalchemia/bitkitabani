(function(){
  var b = document.getElementById('learnBtn'); if (!b) return;
  var id = b.getAttribute('data-id'), list = [];
  try{ list = JSON.parse(localStorage.getItem('bt-learned') || '[]'); }catch(e){}
  function paint(){ var on = list.indexOf(id) > -1; b.setAttribute('aria-pressed', on ? 'true' : 'false'); b.textContent = on ? '✓ Öğrendim' : 'Öğrendim olarak işaretle'; }
  b.addEventListener('click', function(){
    var i = list.indexOf(id); if (i > -1) list.splice(i,1); else list.push(id);
    try{ localStorage.setItem('bt-learned', JSON.stringify(list)); }catch(e){}
    paint();
  });
  paint();
})();
