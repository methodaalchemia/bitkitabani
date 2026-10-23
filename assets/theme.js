/* Tema düğmesi: otomatik → açık → koyu. Seçim bu tarayıcıda saklanır. */
(function(){
  var K = 'bt-theme', root = document.documentElement;
  var L = { tr: { auto: 'Tema: sistem', light: 'Tema: açık', dark: 'Tema: koyu' }, en: { auto: 'Theme: system', light: 'Theme: light', dark: 'Theme: dark' } };
  function get(){ try{ return localStorage.getItem(K) || 'auto'; }catch(e){ return 'auto'; } }
  function set(v){ try{ if (v === 'auto') localStorage.removeItem(K); else localStorage.setItem(K, v); }catch(e){} }
  function apply(v){ if (v === 'auto') root.removeAttribute('data-theme'); else root.setAttribute('data-theme', v); }
  document.querySelectorAll('.themebtn').forEach(function(b){
    var lang = b.getAttribute('data-l') === 'en' ? 'en' : 'tr';
    function paint(){ var v = get(); b.setAttribute('title', L[lang][v]); b.setAttribute('aria-label', L[lang][v]); b.textContent = v === 'light' ? '☀' : v === 'dark' ? '☾' : '◐'; }
    b.addEventListener('click', function(){ var v = get(), n = v === 'auto' ? 'light' : v === 'light' ? 'dark' : 'auto'; set(n); apply(n); paint(); });
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
