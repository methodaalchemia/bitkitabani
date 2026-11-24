/* Hesap sayfası: Google ile giriş, eşitleme durumu, çıkış ve silme (Türkçe ve İngilizce) */
(function(){
  var box = document.getElementById('acct'); if (!box) return;
  var cid = box.getAttribute('data-client');
  var en = box.getAttribute('data-lang') === 'en';
  var T = en ? {
    wait: 'Signing in…', ok: 'Signed in. Your progress has been merged with this device.', fail: 'Could not sign in. Please try again shortly.',
    out: 'Signed out. Your progress on this device is still here.', sure: 'Yes, delete my account data', del: 'All data in your account has been deleted. Your progress on this device is still here.', delfail: 'Could not delete; please try again.'
  } : {
    wait: 'Giriş yapılıyor…', ok: 'Giriş yapıldı. İlerlemen bu cihazla birleştirildi.', fail: 'Giriş yapılamadı. Biraz sonra yeniden dene.',
    out: 'Çıkış yapıldı. Bu cihazdaki ilerlemen yerinde duruyor.', sure: 'Eminim, hesabımdaki veriyi sil', del: 'Hesabındaki bütün veri silindi. Bu cihazdaki ilerlemen yerinde duruyor.', delfail: 'Silinemedi; yeniden dene.'
  };
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
    msg.textContent = T.wait;
    BTSync.login(resp.credential).then(function(){ msg.textContent = T.ok; show(); })
      .catch(function(){ msg.textContent = T.fail; });
  };
  document.getElementById('logout').addEventListener('click', function(){ BTSync.logout().then(function(){ msg.textContent = T.out; show(); }); });
  document.getElementById('del').addEventListener('click', function(){
    var b = this;
    if (b.getAttribute('data-sure') !== '1') { b.setAttribute('data-sure', '1'); b.textContent = T.sure; return; }
    BTSync.remove().then(function(){ msg.textContent = T.del; show(); })
      .catch(function(){ msg.textContent = T.delfail; });
  });
  if (BTSync.signedIn()) BTSync.sync().then(stats).catch(function(){});
  show();
  if (!cid) return;
  var s = document.createElement('script'); s.src = 'https://accounts.google.com/gsi/client'; s.async = true;
  s.onload = function(){
    google.accounts.id.initialize({ client_id: cid, callback: window.btOnGoogle, ux_mode: 'popup', itp_support: true });
    google.accounts.id.renderButton(document.getElementById('gbtn'), { theme: 'outline', size: 'large', text: 'signin_with', shape: 'rectangular', locale: en ? 'en' : 'tr' });
  };
  document.head.appendChild(s);
})();
