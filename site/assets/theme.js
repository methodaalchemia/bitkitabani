/* Tema düğmesi: yalnızca iki mod — açık ve koyu. İlk açılışta sistem tercihiyle başlar, seçim bu tarayıcıda saklanır. */
(function(){
  var K = 'bt-theme', root = document.documentElement;
  var L = { tr: { light: 'Tema: açık', dark: 'Tema: koyu' }, en: { light: 'Theme: light', dark: 'Theme: dark' } };
  function sistem(){ try{ return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'; }catch(e){ return 'light'; } }
  function get(){ var v; try{ v = localStorage.getItem(K); }catch(e){}
    return v === 'light' || v === 'dark' ? v : sistem(); }
  function set(v){ try{ localStorage.setItem(K, v); }catch(e){} }
  function apply(v){ root.setAttribute('data-theme', v); }
  document.querySelectorAll('.themebtn').forEach(function(b){
    var lang = b.getAttribute('data-l') === 'en' ? 'en' : 'tr';
    function paint(){ var v = get(); b.setAttribute('title', L[lang][v]); b.setAttribute('aria-label', L[lang][v]); b.textContent = v === 'light' ? '☀' : '☾'; }
    b.addEventListener('click', function(){ var n = get() === 'dark' ? 'light' : 'dark'; set(n); apply(n); paint(); });
    paint();
  });
  /* Dar ekranda katalog filtreleri kapalı başlar */
  var fb = document.querySelector('details.fbox');
  if (fb && window.matchMedia && window.matchMedia('(max-width: 720px)').matches && !/[?&](bolge|kat|kanit|guv|durum)=/.test(location.search)) fb.open = false;
})();
/* Menü: dışarı tıklayınca ya da Esc ile kapanır */
(function(){var m=document.querySelector('details.menu');if(!m)return;
document.addEventListener('click',function(e){if(m.open&&!m.contains(e.target))m.open=false});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&m.open){m.open=false;m.querySelector('summary').focus()}});})();
/* Paylaş / kopyala / yazdır */
(function(){document.querySelectorAll('.sharebar').forEach(function(b){var u=b.dataset.url,t=b.dataset.title,m=b.querySelector('.sb-msg');
var sh=b.querySelector('.sb-share');if(!navigator.share)sh.hidden=true;
sh.addEventListener('click',function(){navigator.share({title:t,url:u}).catch(function(){})});
b.querySelector('.sb-copy').addEventListener('click',function(){(navigator.clipboard?navigator.clipboard.writeText(u):Promise.reject()).then(function(){m.textContent='Bağlantı kopyalandı.'},function(){m.textContent=u})});
b.querySelector('.sb-print').addEventListener('click',function(){window.print()});});})();

/* Kaydırınca üst menüye gölge; menü dışına tıklayınca ya da Esc ile kapanır */
(function(){
  var n=document.querySelector('.site-nav');if(!n)return;
  var f=function(){n.classList.toggle('scrolled',window.scrollY>8)};
  window.addEventListener('scroll',f,{passive:true});f();
  document.addEventListener('click',function(ev){var m=document.querySelector('details.menu[open]');if(m&&!m.contains(ev.target))m.removeAttribute('open')});
  document.addEventListener('keydown',function(ev){if(ev.key==='Escape'){var m=document.querySelector('details.menu[open]');if(m)m.removeAttribute('open')}});
  // CSP: satır içi olay işleyicileri yerine (onclick/onsubmit) veri öznitelikleri
  document.addEventListener('click',function(ev){var b=ev.target.closest&&ev.target.closest('[data-yazdir]');if(b){ev.preventDefault();window.print()}});
  document.addEventListener('submit',function(ev){if(ev.target.hasAttribute&&ev.target.hasAttribute('data-gonderme'))ev.preventDefault()},true);
})();
