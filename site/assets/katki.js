// Bitki sayfasındaki okur katkısı formu: /api/katki'ye gönderir.
document.querySelectorAll('.katki-form').forEach(f => f.addEventListener('submit', async ev => {
  ev.preventDefault();
  const d = f.querySelector('.katki-durum'), b = f.querySelector('button'), v = Object.fromEntries(new FormData(f));
  v.bitki = f.dataset.bitki; b.disabled = true; d.textContent = 'Gönderiliyor…';
  try {
    const r = await fetch('/api/katki', { method: 'POST', headers: { 'content-type': 'application/json', 'x-bt': '1' }, body: JSON.stringify(v) });
    const j = await r.json().catch(() => ({}));
    if (r.ok) { f.reset(); d.textContent = 'Teşekkürler! Notun okunduktan sonra eklenecek.'; }
    else { d.textContent = j.error || 'Gönderilemedi, birazdan yeniden dene.'; b.disabled = false; }
  } catch (e) { d.textContent = 'Bağlantı kurulamadı, birazdan yeniden dene.'; b.disabled = false; }
}));
