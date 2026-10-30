// Okur formları (/iletisim/ ve eski bitki formları): /api/katki'ye gönderir.
document.querySelectorAll('.katki-form').forEach(f => {
  const ilt = f.classList.contains('iletisim-form');
  if (ilt) {
    const q = new URLSearchParams(location.search), sel = f.querySelector('[name=tur]');
    if (q.get('konu') && sel.querySelector('option[value="' + q.get('konu') + '"]')) sel.value = q.get('konu');
    if (q.get('bitki')) { f.dataset.bitki = q.get('bitki').replace(/[^a-z0-9]/g, ''); f.querySelector('[name=bitki_ad]').value = q.get('ad') || q.get('bitki'); }
    const yore = () => f.querySelectorAll('.yore-alan').forEach(x => { x.hidden = !['kullanim', 'ad'].includes(sel.value); });
    sel.addEventListener('change', yore); yore();
  }
  f.addEventListener('submit', async ev => {
    ev.preventDefault();
    const d = f.querySelector('.katki-durum'), b = f.querySelector('button'), v = Object.fromEntries(new FormData(f));
    v.bitki = f.dataset.bitki || ''; b.disabled = true; d.textContent = 'Gönderiliyor…';
    try {
      const r = await fetch('/api/katki', { method: 'POST', headers: { 'content-type': 'application/json', 'x-bt': '1' }, body: JSON.stringify(v) });
      const j = await r.json().catch(() => ({}));
      if (r.ok) { f.reset(); d.textContent = ilt ? 'Teşekkürler, mesajın ulaştı.' : 'Teşekkürler! Notun okunduktan sonra eklenecek.'; b.disabled = false; }
      else { d.textContent = j.error || 'Gönderilemedi, birazdan yeniden dene.'; b.disabled = false; }
    } catch (e) { d.textContent = 'Bağlantı kurulamadı, birazdan yeniden dene.'; b.disabled = false; }
  });
});
