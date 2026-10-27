// Site sahibinin katkı onay sayfası. Yalnızca yönetici oturumunda veri döner.
(() => {
  const box = document.getElementById('kListe'), only = document.getElementById('kSadece');
  const TUR = { ad: 'Yöresel ad', kullanim: 'Yöresel kullanım', duzeltme: 'Düzeltme' };
  const esc = s => String(s || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  let L = [];
  async function karar(id, k, extra = {}) {
    await fetch('/api/katki-karar', { method: 'POST', headers: { 'content-type': 'application/json', 'x-bt': '1' }, body: JSON.stringify({ id, karar: k, ...extra }) });
    const x = L.find(y => y.id === id); if (x) { x.durum = k; Object.assign(x, extra); } draw();
  }
  function draw() {
    const rows = L.filter(x => !only.checked || x.durum === 'bekliyor').reverse();
    if (!rows.length) { box.innerHTML = '<p>Bekleyen katkı yok.</p>'; return; }
    box.innerHTML = rows.map(x => `<section class="sec kk" data-id="${x.id}"><p class="muted-s">${esc(x.at.slice(0, 10))} · ${x.src === 'threads' ? 'Threads' : 'Site formu'} · ${TUR[x.tur] || ''} · <b>${esc(x.durum)}</b></p>
      <p>Bitki: <input class="kb" value="${esc(x.bitki || '')}" size="14"> ${x.bitki ? `<a href="/${esc(x.bitki)}/">sayfa</a>` : ''}</p>
      <textarea class="km" rows="3" style="width:100%">${esc(x.metin)}</textarea>
      <p class="muted-s">Yöre: ${esc(x.yore) || '-'} · Kaynak: ${esc(x.kaynak) || '-'} · Ad: ${esc(x.ad) || '-'}</p>
      <p><button data-k="onay">Onayla</button> <button data-k="red">Reddet</button></p></section>`).join('');
  }
  box.addEventListener('click', e => {
    const b = e.target.closest('button[data-k]'); if (!b) return;
    const s = b.closest('.kk'); karar(s.dataset.id, b.dataset.k, { metin: s.querySelector('.km').value, bitki: s.querySelector('.kb').value });
  });
  only.addEventListener('change', draw);
  fetch('/api/katki-liste', { credentials: 'same-origin' }).then(r => r.ok ? r.json() : Promise.reject(r.status))
    .then(j => { L = j; draw(); })
    .catch(() => { box.innerHTML = '<p>Bu sayfayı görmek için site sahibinin Google hesabıyla <a href="/hesap/">giriş yapmalısın</a>. Daha önce giriş yaptıysan bir kez çıkıp yeniden gir.</p>'; });
})();
