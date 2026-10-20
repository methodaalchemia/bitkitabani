/* 404: adrese en çok benzeyen bitki ve köprüleri öner */
(function(){
  var el = document.getElementById('nfData'); if (!el) return;
  var data = JSON.parse(el.textContent);
  function norm(s){ return (s || '').toLowerCase().replace(/[çğıöşüâî]/g, function(c){ return {'ç':'c','ğ':'g','ı':'i','ö':'o','ş':'s','ü':'u','â':'a','î':'i'}[c]; }).replace(/[^a-z0-9]+/g, ' ').trim(); }
  function lev(a, b){
    var m = a.length, n = b.length, d = [], i, j;
    for (i = 0; i <= m; i++) { d[i] = [i]; }
    for (j = 1; j <= n; j++) d[0][j] = j;
    for (i = 1; i <= m; i++) for (j = 1; j <= n; j++) d[i][j] = Math.min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + (a[i-1] === b[j-1] ? 0 : 1));
    return d[m][n];
  }
  var path = decodeURIComponent(location.pathname).replace(/\.html$/, '');
  var q = norm(path.split('/').filter(Boolean).pop() || '');
  if (!q) return;
  var scored = data.map(function(x){
    var keys = [norm(x[0]).replace(/^kopruler /, ''), norm(x[1]), norm(x[2])].filter(Boolean);
    var best = Math.min.apply(null, keys.map(function(k){
      if (k.indexOf(q) > -1 || q.indexOf(k) > -1) return 0;
      return lev(q, k) / Math.max(q.length, k.length);
    }));
    return [best, x];
  }).filter(function(s){ return s[0] < 0.5; }).sort(function(a, b){ return a[0] - b[0]; }).slice(0, 6);
  document.getElementById('nfSearch').href = '/katalog/?q=' + encodeURIComponent(q);
  document.getElementById('nfSearch').textContent = '“' + q + '” için katalogda ara →';
  if (!scored.length) return;
  var ul = document.getElementById('nfList');
  scored.forEach(function(s){
    var li = document.createElement('li'), a = document.createElement('a');
    a.href = '/' + s[1][0] + '/'; a.textContent = s[1][1]; li.appendChild(a);
    if (s[1][2]) { var i = document.createElement('i'); i.className = 'latin'; i.textContent = ' ' + s[1][2]; li.appendChild(i); }
    ul.appendChild(li);
  });
  document.getElementById('nfs').hidden = false;
})();
