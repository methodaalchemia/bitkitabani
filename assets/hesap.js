/* Hesap sayfası: Google ile giriş, eşitleme durumu, çıkış ve silme */
(function(){
  var box = document.getElementById('acct'); if (!box) return;
  var cid = box.getAttribute('data-client');
  var out = document.getElementById('acctOut'), inn = document.getElementById('acctIn'), msg = document.getElementById('acctMsg');
  function arr(k){ try{ return JSON.parse(localStorage.getItem(k) || '[]'); }catch(e){ return []; } }
  function stats(){
    var games = 0; try{ for (var i = 0; i < localStorage.length; i++) if (/^bt-oyun-/.test(localStorage.key(i))) games++; }catch(e){}
    document.getElementById('stLearned').textContent = arr('bt-learned').length;
    document.getElementById('stStreak').textContent = window.BTStreak ? BTStreak.count() : 0;
    document.getElementById('stGames').textContent = games;
  }
  function show(){ var s = BTSync.signedIn(); out.hidden = s; inn.hidden = !s; stats(); }
  window.btOnGoogle = function(resp){
    msg.textContent = 'Giriş yapılıyor…';
    BTSync.login(resp.credential).then(function(){ msg.textContent = 'Giriş yapıldı. İlerlemen bu cihazla birleştirildi.'; show(); })
      .catch(function(){ msg.textContent = 'Giriş yapılamadı. Biraz sonra yeniden dene.'; });
  };
  document.getElementById('logout').addEventListener('click', function(){ BTSync.logout().then(function(){ msg.textContent = 'Çıkış yapıldı. Bu cihazdaki ilerlemen yerinde duruyor.'; show(); }); });
  document.getElementById('del').addEventListener('click', function(){
    var b = this;
    if (b.getAttribute('data-sure') !== '1') { b.setAttribute('data-sure', '1'); b.textContent = 'Eminim, hesabımdaki veriyi sil'; return; }
    BTSync.remove().then(function(){ msg.textContent = 'Hesabındaki bütün veri silindi. Bu cihazdaki ilerlemen yerinde duruyor.'; show(); })
      .catch(function(){ msg.textContent = 'Silinemedi; yeniden dene.'; });
  });
  if (BTSync.signedIn()) BTSync.sync().then(stats).catch(function(){});
  show();
  if (!cid) return;
  var s = document.createElement('script'); s.src = 'https://accounts.google.com/gsi/client'; s.async = true;
  s.onload = function(){
    google.accounts.id.initialize({ client_id: cid, callback: window.btOnGoogle, ux_mode: 'popup', itp_support: true });
    google.accounts.id.renderButton(document.getElementById('gbtn'), { theme: 'outline', size: 'large', text: 'signin_with', shape: 'rectangular', locale: 'tr' });
  };
  document.head.appendChild(s);
})();
