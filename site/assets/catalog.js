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
        && G.every(function(g){ return hit(state[g], vals(c, g)); });
      c.hidden = !ok; if (ok) n++;
    });
    updateCounts(words);
    var ce = document.getElementById('count'), tpl = ce.getAttribute('data-tpl'); ce.textContent = tpl ? tpl.replace('{n}', n).replace('{t}', cards.length) : n + ' / ' + cards.length + ' kayıt gösteriliyor';
    document.getElementById('empty').hidden = n > 0;
    document.getElementById('reset').hidden = !(state.q || G.some(function(g){ return any(state[g]); }));
    writeUrl();
  }
  function vals(c, g){ return g === 'kanit' || g === 'guv' ? [c.dataset[g]] : (c.dataset[g] || '').split(' '); }
  function updateCounts(words){
    var base = cards.filter(function(c){ return words.every(function(w){ return c._s.indexOf(w) > -1; }); });
    document.querySelectorAll('.chip[data-g]').forEach(function(b){
      var g = b.dataset.g, k = b.dataset.k;
      var n = base.filter(function(c){
        return G.every(function(o){ return o === g || hit(state[o], vals(c, o)); }) && vals(c, g).indexOf(k) > -1;
      }).length;
      var el = b.querySelector('.n'); if (el) el.textContent = n;
      b.classList.toggle('zero', n === 0 && b.getAttribute('aria-pressed') !== 'true');
    });
  }
  // Filtreleri adres çubuğuna yaz, böylece filtrelenmiş görünüm paylaşılabilir
  function writeUrl(){
    try{
      var u = new URLSearchParams();
      if (state.q) u.set('q', state.q);
      G.forEach(function(g){ var v = Object.keys(state[g]).filter(function(k){ return state[g][k]; }); if (v.length) u.set(g, v.join(',')); });
      var s = u.toString();
      history.replaceState(null, '', location.pathname + (s ? '?' + s : ''));
      markNoindex();
    }catch(e){}
  }
  function markNoindex(){
    var m = document.querySelector('meta[name="robots"]');
    if (location.search) { if (!m) { m = document.createElement('meta'); m.name = 'robots'; document.head.appendChild(m); } m.content = 'noindex, follow'; }
    else if (m) m.parentNode.removeChild(m);
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
  var pool = cards.filter(function(c){ return c.dataset.guv !== 'yuksek'; }); if (!pool.length) pool = cards;
  var d = new Date(), idx = Math.floor(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) / 864e5) % pool.length;
  var t = pool[idx], tl = document.getElementById('today');
  if (t && tl) {
    tl.href = t.getAttribute('href');
    document.getElementById('todayName').textContent = t.querySelector('h2').textContent;
    document.getElementById('todayLatin').textContent = t.querySelector('.latin').textContent;
  }
  render();
})();
