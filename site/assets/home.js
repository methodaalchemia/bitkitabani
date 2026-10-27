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
