/* Ana sayfa: eski filtre adreslerini kataloğa yönlendir, bugünün bitkisini seç */
(function(){
  if (/[?&](q|bolge|kat|kanit|guv|durum)=/.test(location.search)) { location.replace('/katalog/' + location.search); return; }
  var sk = document.getElementById('streak'); if (sk && window.BTStreak) { var n = BTStreak.count(); if (n) { sk.textContent = BTStreak.text(n); sk.hidden = false; } }
  var t = document.getElementById('today'); if (!t) return;
  var pool = []; try { pool = JSON.parse(t.getAttribute('data-pool') || '[]'); } catch(e) {}
  if (!pool.length) return;
  var d = new Date(), p = pool[Math.floor(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) / 864e5) % pool.length];
  t.href = '/' + p[0] + '/';
  document.getElementById('todayName').textContent = p[1];
  document.getElementById('todayLatin').textContent = p[2];
})();
/* Ana sayfa arama: bitki adlarında anlık öneri; cümle yazılırsa akıllı aramaya gider */
(function(){
  var f = document.querySelector('.hsearch'), q = document.getElementById('hq'), L = document.getElementById('hqList'), D = [];
  if (!f || !q) return;
  try { D = JSON.parse(document.getElementById('hqData').textContent); } catch(e) {}
  var norm = function(s){ return (s || '').toLocaleLowerCase('tr').normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/ı/g, 'i'); };
  var esc = function(s){ return String(s).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); };
  function matches(v){
    var n = norm(v); if (n.length < 2) return [];
    var a = [], b = [];
    D.forEach(function(x){ var tr = norm(x[1]), la = norm(x[2]), dg = norm(x[3]);
      if (tr.indexOf(n) === 0 || la.indexOf(n) === 0) a.push(x); else if (tr.indexOf(n) > 0 || la.indexOf(n) > 0 || dg.indexOf(n) >= 0) b.push(x); });
    return a.concat(b).slice(0, 7);
  }
  q.addEventListener('input', function(){
    var m = matches(q.value);
    L.innerHTML = m.map(function(x){ return '<li role="option"><a href="/' + x[0] + '/"><b>' + esc(x[1]) + '</b> <i>' + esc(x[2]) + '</i></a></li>'; }).join('');
    L.hidden = !m.length;
  });
  f.addEventListener('submit', function(ev){
    var v = q.value.trim(); if (!v) { ev.preventDefault(); return; }
    var m = matches(v);
    if (m.length === 1 || (m.length && norm(m[0][1]) === norm(v))) { ev.preventDefault(); location.href = '/' + m[0][0] + '/'; return; }
    if (v.split(/\s+/).length >= 3 || !m.length) { ev.preventDefault(); location.href = '/rehber/?q=' + encodeURIComponent(v) + '#ara'; }
  });
  document.addEventListener('click', function(e){ if (!f.contains(e.target)) L.hidden = true; });
})();
