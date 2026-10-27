// Akıllı arama sayfası: /api/ara
(() => {
  const f = document.getElementById('araForm'), q = document.getElementById('araQ'), o = document.getElementById('araSonuc');
  const esc = s => String(s || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  async function ara(t) {
    o.innerHTML = '<p>Aranıyor…</p>';
    try {
      const r = await fetch('/api/ara?q=' + encodeURIComponent(t)); const j = await r.json();
      if (!r.ok) { o.innerHTML = '<p>' + esc(j.error || 'Arama yapılamadı.') + '</p>'; return; }
      o.innerHTML = j.sonuc.length ? '<ul class="guidelist">' + j.sonuc.map(x => `<li><a href="/${x.id}/"><b>${esc(x.tr)}</b> <i>${esc(x.la)}</i></a><br><span class="muted-s">${esc(x.guv)} · ${esc(x.kisa)}</span></li>`).join('') + '</ul>'
        : '<p>Yakın bir sonuç bulunamadı. Başka kelimelerle dene ya da <a href="/katalog/">kataloğa</a> göz at.</p>';
    } catch (e) { o.innerHTML = '<p>Bağlantı kurulamadı.</p>'; }
  }
  f.addEventListener('submit', e => { e.preventDefault(); history.replaceState(null, '', '?q=' + encodeURIComponent(q.value)); ara(q.value); });
  const p = new URLSearchParams(location.search).get('q'); if (p) { q.value = p; ara(p); }
})();
