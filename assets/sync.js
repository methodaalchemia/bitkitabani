/* Google ile giriş yapıldıysa ilerlemeyi (öğrenilenler, seri, bilmece) hesapla eşitler. Giriş yoksa hiçbir şey yapmaz. */
(function(){
  var A = 'bt-auth', applying = false, timer = null;
  function g(k){ try{ return localStorage.getItem(k); }catch(e){ return null; } }
  function arr(k){ try{ return JSON.parse(g(k) || '[]'); }catch(e){ return []; } }
  var setItem = Storage.prototype.setItem;
  function put(k, v){ applying = true; try{ setItem.call(localStorage, k, v); }catch(e){} applying = false; }
  function local(){
    var games = {};
    try{ for (var i = 0; i < localStorage.length; i++) { var k = localStorage.key(i); if (/^bt-oyun-\d{4}-\d{2}-\d{2}$/.test(k)) games[k.slice(8)] = arr(k); } }catch(e){}
    return { learned: arr('bt-learned'), days: arr('bt-days'), games: games };
  }
  function uni(a, b){ var o = []; (a || []).concat(b || []).forEach(function(x){ if (o.indexOf(x) < 0) o.push(x); }); return o; }
  function merge(a, b){
    var games = {}, k;
    for (k in a.games || {}) games[k] = a.games[k];
    for (k in b.games || {}) if (!games[k] || b.games[k].length > games[k].length) games[k] = b.games[k];
    return { learned: uni(a.learned, b.learned), days: uni(a.days, b.days).sort(), games: games };
  }
  function apply(d){
    put('bt-learned', JSON.stringify(d.learned || []));
    put('bt-days', JSON.stringify(d.days || []));
    for (var k in d.games || {}) put('bt-oyun-' + k, JSON.stringify(d.games[k]));
  }
  function same(a, b){ return JSON.stringify(merge(a, {})) === JSON.stringify(merge(b, {})); }
  function api(method, path, body){
    return fetch('/api/' + path, { method: method, credentials: 'same-origin', headers: { 'x-bt': '1', 'content-type': 'application/json' }, body: body });
  }
  function signedOut(){ try{ localStorage.removeItem(A); }catch(e){} document.documentElement.classList.remove('bt-in'); }
  function push(){
    if (g(A) !== '1') return;
    clearTimeout(timer);
    timer = setTimeout(function(){ api('PUT', 'me', JSON.stringify(local())).then(function(r){ if (r.status === 401) signedOut(); }).catch(function(){}); }, 700);
  }
  Storage.prototype.setItem = function(k, v){
    setItem.call(this, k, v);
    if (!applying && this === localStorage && /^bt-(learned|days|oyun-)/.test(k)) push();
  };
  function syncNow(){
    var before = local();
    return api('PUT', 'me?merge=1', JSON.stringify(before)).then(function(r){
      if (r.status === 401) { signedOut(); return false; }
      return r.json().then(function(j){
        if (!j.ok) return false;
        apply(j.data);
        return !same(before, j.data);
      });
    });
  }
  window.BTSync = {
    signedIn: function(){ return g(A) === '1'; },
    login: function(credential){
      return api('POST', 'login', JSON.stringify({ credential: credential })).then(function(r){
        if (!r.ok) throw new Error('giriş');
        put(A, '1'); document.documentElement.classList.add('bt-in');
        return syncNow();
      });
    },
    logout: function(){ return api('POST', 'logout').finally(signedOut); },
    remove: function(){ return api('DELETE', 'me').then(function(r){ if (!r.ok) throw new Error('silme'); signedOut(); }); },
    sync: syncNow
  };
  if (g(A) === '1') {
    document.documentElement.classList.add('bt-in');
    var once = 'bt-synced';
    syncNow().then(function(changed){
      var done = false; try{ done = sessionStorage.getItem(once) === '1'; sessionStorage.setItem(once, '1'); }catch(e){}
      if (changed && !done && !/\/hesap\/$/.test(location.pathname)) location.reload();
    }).catch(function(){});
  }
})();
