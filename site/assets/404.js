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
  var en = /^\/en(\/|$)/.test(path), base = en ? '/en/' : '/';
  if (en) {
    document.documentElement.lang = 'en';
    document.title = 'Page not found | Bitki Tabanı';
    var h1 = document.querySelector('.page-head h1'); if (h1) h1.textContent = 'Page not found';
    var hp = document.querySelector('.page-head p'); if (hp) hp.textContent = 'The page may have moved, or the address may be mistyped.';
    var h2 = document.querySelector('#nfs h2'); if (h2) h2.textContent = 'Were you looking for this?';
    var nv = document.querySelector('.site-nav nav');
    if (nv) nv.innerHTML = '<a href="/en/catalog/">Catalog</a><a href="/en/bridges/">Culture bridges</a><a href="/en/about/">About</a><a href="/" lang="tr">Türkçe</a>';
    var lg = document.querySelector('.site-nav .logo'); if (lg) lg.href = '/en/';
    var ft = document.querySelector('footer.site'); if (ft) ft.innerHTML = '<div><h3>About this site</h3><p>A compilation made for knowledge and curiosity; it is not medical advice.</p><p><a href="/en/about/">About and method</a> · <a href="/en/privacy/">Privacy</a> · <a href="/">Türkçe</a></p></div>';
    var sl = document.getElementById('nfSearch'); if (sl) { sl.href = '/en/catalog/'; sl.textContent = 'Search the catalog →'; }
  }
  var q = norm(path.split('/').filter(Boolean).pop() || '');
  if (!q || q === 'en') return;
  var scored = data.map(function(x){
    var keys = [norm(x[0]).replace(/^kopruler /, ''), norm(x[1]), norm(x[2])].filter(Boolean);
    var best = Math.min.apply(null, keys.map(function(k){
      if (k.indexOf(q) > -1 || q.indexOf(k) > -1) return 0;
      return lev(q, k) / Math.max(q.length, k.length);
    }));
    return [best, x];
  }).filter(function(s){ return s[0] < 0.5; }).sort(function(a, b){ return a[0] - b[0]; }).slice(0, 6);
  document.getElementById('nfSearch').href = (en ? '/en/catalog/' : '/katalog/') + '?q=' + encodeURIComponent(q);
  document.getElementById('nfSearch').textContent = en ? 'Search the catalog for “' + q + '” →' : '“' + q + '” için katalogda ara →';
  if (!scored.length) return;
  var ul = document.getElementById('nfList');
  scored.forEach(function(s){
    var li = document.createElement('li'), a = document.createElement('a');
    a.href = (en && s[1][0].indexOf('kopruler/') !== 0 ? '/en/' : '/') + s[1][0] + '/'; a.textContent = s[1][1]; li.appendChild(a);
    if (s[1][2]) { var i = document.createElement('i'); i.className = 'latin'; i.textContent = ' ' + s[1][2]; li.appendChild(i); }
    ul.appendChild(li);
  });
  document.getElementById('nfs').hidden = false;
})();
