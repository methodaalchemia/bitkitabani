(function(){var s=document.getElementById('etksel'),q=document.getElementById('etkq'),m=document.getElementById('etkmsg');if(!s)return;try{var u=new URLSearchParams(location.search).get('q');if(u){q.value=u;setTimeout(run,0)}}catch(e){}
var low=function(t){return t.replace(/I/g,'ı').replace(/İ/g,'i').toLowerCase()};
function run(){var c=s.value,t=low(q.value.trim()),n=0;document.querySelectorAll('.etkgrp').forEach(function(g){var on=!c||g.dataset.c===c,k=0;g.querySelectorAll('tbody tr').forEach(function(r){var v=on&&(!t||low(r.textContent).indexOf(t)>=0);r.hidden=!v;if(v)k++});g.hidden=!k;n+=k});
m.textContent=n?n+' etkileşim kaydı gösteriliyor.':'Bu seçimde katalogda bildirilmiş bir etkileşim yok. Bu, güvenli olduğu anlamına gelmez; eczacına sor.';
try{history.replaceState(null,'',c?'#'+c:location.pathname)}catch(e){}}
s.addEventListener('change',run);q.addEventListener('input',run);
var h=location.hash.slice(1);if(h&&s.querySelector('option[value="'+h+'"]')){s.value=h;run()}})();
