/* Günün bilmecesi: ipuçlarından bitkiyi bul. Her yanlış tahminde yeni bir ipucu açılır; 6 hak. */
(function(){
  var root = document.getElementById('game'); if (!root) return;
  var D = JSON.parse(document.getElementById('gameData').textContent);
  var P = D.p, MAX = 6;
  function norm(s){ return (s || '').toLocaleLowerCase('tr').replace(/[çğıöşüâî]/g, function(c){ return {'ç':'c','ğ':'g','ı':'i','ö':'o','ş':'s','ü':'u','â':'a','î':'i'}[c]; }).replace(/[^a-z0-9]+/g, ' ').trim(); }
  var now = new Date(), today = BTStreak.key(now);
  var dayNum = Math.floor(Date.UTC(now.getFullYear(), now.getMonth(), now.getDate()) / 864e5);
  var ans = P[(dayNum * 37 + 11) % P.length];
  var SK = 'bt-oyun-' + today, guesses = [];
  try{ guesses = JSON.parse(localStorage.getItem(SK) || '[]'); }catch(e){}
  function save(){ try{ localStorage.setItem(SK, JSON.stringify(guesses)); }catch(e){} }
  var byNorm = {}; P.forEach(function(p){ byNorm[norm(p.tr)] = p; });
  function byId(id){ for (var i = 0; i < P.length; i++) if (P[i].id === id) return P[i]; }
  function shared(a, b){ return a.bolge.some(function(r){ return b.bolge.indexOf(r) > -1; }); }

  var cluesEl = document.getElementById('clues'), listEl = document.getElementById('guesses'),
      form = document.getElementById('guessForm'), input = document.getElementById('guessInput'),
      msg = document.getElementById('gameMsg'), endEl = document.getElementById('gameEnd');

  function esc(t){ var d = document.createElement('div'); d.textContent = t; return d.innerHTML; }
  function clue(i){
    var c = ans.c[i];
    if (c[0] === 'img') return '<li class="clue img"><span class="eyebrow">İpucu ' + (i + 1) + ' · Fotoğraf</span><img src="' + c[1] + '" alt="Bilmece bitkisinin fotoğrafı" width="500" height="667"></li>';
    return '<li class="clue"><span class="eyebrow">İpucu ' + (i + 1) + ' · ' + esc(c[0]) + '</span><p>' + esc(c[1]) + '</p></li>';
  }
  function won(){ return guesses.length && guesses[guesses.length - 1] === ans.id; }
  function over(){ return won() || guesses.length >= MAX; }
  function squares(){ return guesses.map(function(id){ var g = byId(id); return id === ans.id ? '🟩' : (g.fam === ans.fam || shared(g, ans)) ? '🟨' : '⬜'; }).join(''); }
  function render(){
    var open = Math.min(over() ? MAX : guesses.length + 1, ans.c.length), h = '';
    for (var i = 0; i < open; i++) h += clue(i);
    cluesEl.innerHTML = h;
    listEl.innerHTML = guesses.map(function(id){
      var g = byId(id), ok = id === ans.id;
      var hints = ok ? '<span class="hit">Doğru</span>' :
        '<span class="' + (shared(g, ans) ? 'near' : 'miss') + '">Bölge ' + (shared(g, ans) ? 'ortak' : 'farklı') + '</span>' +
        '<span class="' + (g.fam === ans.fam ? 'near' : 'miss') + '">Familya ' + (g.fam === ans.fam ? 'aynı' : 'farklı') + '</span>';
      return '<li><b>' + esc(g.tr) + '</b>' + hints + '</li>';
    }).join('');
    document.getElementById('left').textContent = over() ? '' : (MAX - guesses.length) + ' hakkın kaldı';
    form.hidden = over();
    if (over()) {
      var w = won();
      if (w) { BTStreak.mark(); }
      var n = BTStreak.count();
      endEl.innerHTML = '<p class="verdict">' + (w ? guesses.length + '. tahminde buldun!' : 'Bugünün bitkisi buydu:') + '</p>' +
        '<a class="today" href="/' + ans.id + '/"><b>' + esc(ans.tr) + '</b><i>' + esc(ans.la) + '</i></a>' +
        '<p class="sq" aria-label="Sonuç">' + squares() + '</p>' +
        (n ? '<p class="muted-s">' + BTStreak.text(n) + '</p>' : '') +
        '<p><button type="button" class="learn" id="shareBtn">Sonucu paylaş</button> <span id="shareMsg" class="muted-s"></span></p>' +
        '<p class="muted-s">Yarın yeni bir bitki gelecek.</p>';
      endEl.hidden = false;
      document.getElementById('shareBtn').addEventListener('click', share);
    }
  }
  function share(){
    var t = 'Bitki Tabanı bilmecesi · ' + now.getDate() + ' ' + D.ay[now.getMonth()] + '\n' + squares() + ' ' + (won() ? guesses.length : 'X') + '/' + MAX + '\nhttps://bitkitabani.com/oyun/';
    var m = document.getElementById('shareMsg');
    if (navigator.share) { navigator.share({ text: t }).catch(function(){}); return; }
    if (navigator.clipboard) navigator.clipboard.writeText(t).then(function(){ m.textContent = 'Kopyalandı'; }, function(){ m.textContent = t; });
    else m.textContent = t;
  }
  form.addEventListener('submit', function(ev){
    ev.preventDefault();
    var g = byNorm[norm(input.value)];
    if (!g) { msg.textContent = 'Bu adı katalogda bulamadım; listeden seç.'; return; }
    if (guesses.indexOf(g.id) > -1) { msg.textContent = 'Bunu zaten denedin.'; return; }
    msg.textContent = ''; guesses.push(g.id); save(); input.value = ''; render();
    if (!over()) input.focus();
  });
  render();
})();
