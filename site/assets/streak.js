/* Seri sayacı: "Öğrendim" işaretlenen ya da bilmecesi çözülen günler (yalnızca bu tarayıcıda) */
(function(){
  var K = 'bt-days';
  function key(d){ return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }
  function days(){ try{ return JSON.parse(localStorage.getItem(K) || '[]'); }catch(e){ return []; } }
  function mark(){ var a = days(), t = key(new Date()); if (a.indexOf(t) < 0) { a.push(t); a = a.slice(-400); try{ localStorage.setItem(K, JSON.stringify(a)); }catch(e){} } return count(); }
  function count(){
    var a = days(), d = new Date(), n = 0;
    if (a.indexOf(key(d)) < 0) d.setDate(d.getDate() - 1);
    while (a.indexOf(key(d)) > -1) { n++; d.setDate(d.getDate() - 1); }
    return n;
  }
  function text(n){ return n >= 2 ? n + ' gündür üst üste öğreniyorsun' : n === 1 ? 'Seri başladı: 1 gün' : ''; }
  window.BTStreak = { key: key, mark: mark, count: count, text: text };
})();
