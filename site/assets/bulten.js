/* Bülten kayıt kutusu: e-posta adresini /api/abone'ye gönderir (çift onaylı kayıt). */
(function(){document.querySelectorAll('.abone-form').forEach(function(f){var m=f.querySelector('.abone-msg'),b=f.querySelector('button');
f.addEventListener('submit',function(ev){ev.preventDefault();var em=f.email.value.trim();
if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(em)){m.textContent='Geçerli bir e-posta adresi yazın.';f.email.focus();return}
if(!f.riza.checked){m.textContent='Kayıt için onay kutusunu işaretleyin.';return}
b.disabled=true;m.textContent='Gönderiliyor…';
fetch('/api/abone',{method:'POST',headers:{'content-type':'application/json','x-bt':'1'},body:JSON.stringify({email:em,riza:true,duyuru:f.duyuru.checked,hp:f.hp.value,kaynak:f.getAttribute('data-kaynak')})})
.then(function(r){return r.json().then(function(j){return[r.ok,j]})}).then(function(x){var ok=x[0],j=x[1];
if(!ok){m.textContent=j.error||'Bir sorun oldu, biraz sonra yeniden deneyin.';b.disabled=false;return}
m.textContent=j.zaten?'Bu adres zaten kayıtlı, teşekkürler!':'Neredeyse tamam: e-postanıza gelen bağlantıya tıklayarak kaydınızı onaylayın. Gelmezse spam klasörüne bakın.';f.email.value=''})
.catch(function(){m.textContent='Bağlantı kurulamadı, biraz sonra yeniden deneyin.';b.disabled=false})})})})();
