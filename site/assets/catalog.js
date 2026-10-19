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

  var G = ['bolge','kat','kanit','guv','durum'];
  var state = { q:'', bolge:{}, kat:{}, kanit:{}, guv:{}, durum:{} };
  function any(o){ return Object.keys(o).some(function(k){ return o[k]; }); }
  function hit(o, vals){ return !any(o) || vals.some(function(v){ return o[v]; }); }
  function render(){
    var words = state.q ? norm(state.q).split(/\s+/) : [], n = 0;
    cards.forEach(function(c){
      var ok = words.every(function(w){ return c._s.indexOf(w) > -1; })
        && hit(state.bolge, c.dataset.bolge.split(' '))
        && hit(state.kat, c.dataset.kat.split(' '))
        && hit(state.kanit, [c.dataset.kanit])
        && hit(state.guv, [c.dataset.guv])
        && hit(state.durum, (c.dataset.durum || '').split(' '));
      c.hidden = !ok; if (ok) n++;
    });
    document.getElementById('count').textContent = n + ' / ' + cards.length + ' kayıt gösteriliyor';
    document.getElementById('empty').hidden = n > 0;
    document.getElementById('reset').hidden = !(state.q || G.some(function(g){ return any(state[g]); }));
    writeUrl();
  }
  // Filtreleri adres çubuğuna yaz, böylece filtrelenmiş görünüm paylaşılabilir
  function writeUrl(){
    try{
      var u = new URLSearchParams();
      if (state.q) u.set('q', state.q);
      G.forEach(function(g){ var v = Object.keys(state[g]).filter(function(k){ return state[g][k]; }); if (v.length) u.set(g, v.join(',')); });
      var s = u.toString();
      history.replaceState(null, '', location.pathname + (s ? '?' + s : ''));
    }catch(e){}
  }
  function readUrl(){
    try{
      var u = new URLSearchParams(location.search);
      if (u.get('q')) { state.q = u.get('q'); q.value = state.q; }
      G.forEach(function(g){ (u.get(g) || '').split(',').filter(Boolean).forEach(function(k){ state[g][k] = true; }); });
      document.querySelectorAll('.chip[data-g]').forEach(function(b){ b.setAttribute('aria-pressed', state[b.dataset.g][b.dataset.k] ? 'true' : 'false'); });
    }catch(e){}
  }
  document.querySelectorAll('.chip[data-g]').forEach(function(b){
    b.addEventListener('click', function(){
      var g = state[b.dataset.g], k = b.dataset.k; g[k] = !g[k];
      b.setAttribute('aria-pressed', g[k] ? 'true' : 'false'); render();
    });
  });
  var q = document.getElementById('q');
  readUrl();
  q.addEventListener('input', function(){ state.q = q.value.trim(); render(); });
  document.getElementById('reset').addEventListener('click', function(){
    state = { q:'', bolge:{}, kat:{}, kanit:{}, guv:{}, durum:{} }; q.value = '';
    document.querySelectorAll('.chip[data-g]').forEach(function(c){ c.setAttribute('aria-pressed','false'); });
    render();
  });

  // Bugünün bitkisi: tarihe göre sabit; yüksek riskli bitkiler rotasyona girmez
  var pool = cards.filter(function(c){ return c.dataset.guv !== 'yuksek'; });
  var d = new Date(), idx = Math.floor(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) / 864e5) % pool.length;
  var t = pool[idx], tl = document.getElementById('today');
  if (t && tl) {
    tl.href = t.getAttribute('href');
    document.getElementById('todayName').textContent = t.querySelector('h2').textContent;
    document.getElementById('todayLatin').textContent = t.querySelector('.latin').textContent;
  }
  render();
})();
