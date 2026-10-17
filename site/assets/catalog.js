(function(){
  var learned = [];
  try{ learned = JSON.parse(localStorage.getItem('bt-learned') || '[]'); }catch(e){}
  var cards = Array.prototype.slice.call(document.querySelectorAll('.card[data-id]'));
  var norm = function(s){ return s.toLocaleLowerCase('tr').replace(/ı/g,'i').normalize('NFD').replace(/[̀-ͯ]/g,''); };
  cards.forEach(function(c){
    c._s = norm(c.getAttribute('data-s') || '');
    if (learned.indexOf(c.dataset.id) > -1) {
      var m = document.createElement('span'); m.className = 'learned-mark'; m.textContent = 'ÖĞRENDİM'; c.appendChild(m);
    }
  });
  var el = document.getElementById('learnedCount'); if (el) el.textContent = learned.length;

  var state = { q:'', bolge:{}, kat:{}, kanit:{}, guv:{} };
  function any(o){ return Object.keys(o).some(function(k){ return o[k]; }); }
  function hit(o, vals){ return !any(o) || vals.some(function(v){ return o[v]; }); }
  function render(){
    var words = state.q ? norm(state.q).split(/\s+/) : [], n = 0;
    cards.forEach(function(c){
      var ok = words.every(function(w){ return c._s.indexOf(w) > -1; })
        && hit(state.bolge, c.dataset.bolge.split(' '))
        && hit(state.kat, c.dataset.kat.split(' '))
        && hit(state.kanit, [c.dataset.kanit])
        && hit(state.guv, [c.dataset.guv]);
      c.hidden = !ok; if (ok) n++;
    });
    document.getElementById('count').textContent = n + ' / ' + cards.length + ' kayıt gösteriliyor';
    document.getElementById('empty').hidden = n > 0;
    document.getElementById('reset').hidden = !(state.q || any(state.bolge) || any(state.kat) || any(state.kanit) || any(state.guv));
  }
  document.querySelectorAll('.chip[data-g]').forEach(function(b){
    b.addEventListener('click', function(){
      var g = state[b.dataset.g], k = b.dataset.k; g[k] = !g[k];
      b.setAttribute('aria-pressed', g[k] ? 'true' : 'false'); render();
    });
  });
  var q = document.getElementById('q');
  q.addEventListener('input', function(){ state.q = q.value.trim(); render(); });
  document.getElementById('reset').addEventListener('click', function(){
    state = { q:'', bolge:{}, kat:{}, kanit:{}, guv:{} }; q.value = '';
    document.querySelectorAll('.chip[data-g]').forEach(function(c){ c.setAttribute('aria-pressed','false'); });
    render();
  });

  // Bugünün bitkisi: tarihe göre sabit
  var d = new Date(), idx = Math.floor(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) / 864e5) % cards.length;
  var t = cards[idx], tl = document.getElementById('today');
  if (t && tl) {
    tl.href = t.getAttribute('href');
    document.getElementById('todayName').textContent = t.querySelector('h2').textContent;
    document.getElementById('todayLatin').textContent = t.querySelector('.latin').textContent;
  }
  render();
})();
