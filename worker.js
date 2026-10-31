// Bitki Tabanı: Google ile giriş ve ilerleme saklama.
// Statik sayfalar ./site'tan sunulur; bu Worker yalnızca /api/* isteklerini karşılar.
// Saklanan veri: Google hesap kimliği numarası (sub) ve ilerleme (öğrenilen bitkiler, seri günleri, bilmece tahminleri).
// E-posta, ad ya da fotoğraf saklanmaz.
import { DurableObject } from 'cloudflare:workers';

const COOKIE = 'bt_s';
const SESSION_DAYS = 180;
let JWKS = null, JWKS_AT = 0;

export class UserStore extends DurableObject {
  async fetch(req) {
    const { op, value } = await req.json();
    if (op === 'get') return Response.json((await this.ctx.storage.get('v')) ?? null);
    if (op === 'put') { await this.ctx.storage.put('v', value); return Response.json(true); }
    if (op === 'del') { await this.ctx.storage.deleteAll(); return Response.json(true); }
    return new Response('bad op', { status: 400 });
  }
}

function store(env, name) { return env.USERS.get(env.USERS.idFromName(name)); }
async function call(env, name, op, value) {
  const r = await store(env, name).fetch('https://do/', { method: 'POST', body: JSON.stringify({ op, value }) });
  return r.json();
}
function b64url(s) { s = s.replace(/-/g, '+').replace(/_/g, '/'); while (s.length % 4) s += '='; return Uint8Array.from(atob(s), c => c.charCodeAt(0)); }
function json(data, status = 200, headers = {}) {
  return new Response(JSON.stringify(data), { status, headers: { 'content-type': 'application/json', 'cache-control': 'no-store', ...headers } });
}
function cookieOf(req) {
  const m = (req.headers.get('cookie') || '').match(new RegExp('(?:^|; )' + COOKIE + '=([A-Za-z0-9_-]{20,})'));
  return m ? m[1] : null;
}
function setCookie(v, maxAge) {
  return `${COOKIE}=${v}; Path=/api/; HttpOnly; Secure; SameSite=Lax; Max-Age=${maxAge}`;
}

async function verifyGoogle(token, clientId) {
  const [h, p, s] = token.split('.');
  if (!s) throw new Error('token');
  const header = JSON.parse(new TextDecoder().decode(b64url(h)));
  const claims = JSON.parse(new TextDecoder().decode(b64url(p)));
  if (!JWKS || Date.now() - JWKS_AT > 3600e3) {
    JWKS = (await (await fetch('https://www.googleapis.com/oauth2/v3/certs')).json()).keys; JWKS_AT = Date.now();
  }
  const jwk = JWKS.find(k => k.kid === header.kid);
  if (!jwk || header.alg !== 'RS256') throw new Error('key');
  const key = await crypto.subtle.importKey('jwk', jwk, { name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' }, false, ['verify']);
  const ok = await crypto.subtle.verify('RSASSA-PKCS1-v1_5', key, b64url(s), new TextEncoder().encode(h + '.' + p));
  if (!ok) throw new Error('sig');
  if (!['accounts.google.com', 'https://accounts.google.com'].includes(claims.iss)) throw new Error('iss');
  if (claims.aud !== clientId) throw new Error('aud');
  if (claims.exp * 1000 < Date.now()) throw new Error('exp');
  return claims.sub;
}
const ADMIN_SHA = '52036425c1c067cf803b39af2caee68b2c97fe22d49901893bb126943b4d6813';   // site sahibinin e-postasının SHA-256 özeti (adres kodda açık yazılmaz)
async function sha256hex(s) { return [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s)))].map(b => b.toString(16).padStart(2, '0')).join(''); }
function googleClaims(token) { try { return JSON.parse(new TextDecoder().decode(b64url(token.split('.')[1]))); } catch (e) { return {}; } }

// İki cihazdaki ilerlemeyi birleştir: listeler birleşir, bilmecede daha uzun tahmin listesi kalır.
function merge(a, b) {
  a = a || {}; b = b || {};
  const uni = (x, y) => [...new Set([...(x || []), ...(y || [])])].slice(-1000);
  const games = { ...(a.games || {}) };
  for (const [d, g] of Object.entries(b.games || {})) if (!games[d] || (g || []).length > games[d].length) games[d] = g;
  const keys = Object.keys(games).sort().slice(-400);
  return { learned: uni(a.learned, b.learned), days: uni(a.days, b.days).sort(), games: Object.fromEntries(keys.map(k => [k, games[k]])) };
}
function clean(v) {
  const ids = x => (Array.isArray(x) ? x : []).filter(s => typeof s === 'string' && /^[a-z0-9-]{1,40}$/.test(s));
  const dates = x => (Array.isArray(x) ? x : []).filter(s => typeof s === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(s));
  const games = {};
  for (const [d, g] of Object.entries((v && v.games) || {})) if (/^\d{4}-\d{2}-\d{2}$/.test(d)) games[d] = ids(g).slice(0, 6);
  return { learned: ids(v && v.learned), days: dates(v && v.days), games };
}

async function session(req, env) {
  const sid = cookieOf(req); if (!sid) return null;
  const s = await call(env, 'sess:' + sid, 'get');
  if (!s || s.exp < Date.now()) return null;
  return { sid, sub: s.sub, admin: !!s.admin, ep: s.ep };
}


// ---------- Instagram: her akşam günün kaydırmalı postunu paylaş ----------
// Görseller ve açıklama derlemede site/ig/<tarih>/ altına yazılır (tools/ig.py).
// Gerekli gizli değişken: IG_TOKEN (Instagram API with Instagram Login, uzun ömürlü token).
// Token 60 gün geçerlidir; 20 günde bir kendiliğinden yenilenir ve Durable Object'te saklanır.
const IG = 'https://graph.instagram.com/v23.0';
// Instagram görselleri ve videoları sitede değil, geçmişi tutulmayan igmedia dalında durur (depo şişmesin diye).
const IGRAW = 'https://raw.githubusercontent.com/methodaalchemia/bitkitabani/igmedia/';
async function igAsset(path) {
  if (!path || path.endsWith('/')) path += 'index.html';
  if (path.includes('..')) return new Response('yok', { status: 404 });
  const r = await fetch(IGRAW + path, { cf: { cacheTtl: 300, cacheEverything: true } });
  if (!r.ok) return new Response('yok', { status: 404 });
  const ext = path.split('.').pop();
  const ct = { jpg: 'image/jpeg', mp4: 'video/mp4', json: 'application/json; charset=utf-8', html: 'text/html; charset=utf-8' }[ext] || 'application/octet-stream';
  return new Response(r.body, { headers: { 'content-type': ct, 'cache-control': 'public, max-age=300', 'x-robots-tag': 'noindex' } });
}
function trDay(d = new Date()) { return new Date(d.getTime() + 3 * 3600e3).toISOString().slice(0, 10); }
async function igJson(r) { const j = await r.json().catch(() => ({})); if (!r.ok || j.error) { const x = j.error || {}; throw new Error([x.message || ('HTTP ' + r.status), x.error_user_msg, x.code && ('kod ' + x.code + (x.error_subcode ? '/' + x.error_subcode : ''))].filter(Boolean).join(' · ')); } return j; }
async function igToken(env, st) {
  let tok = st.token, at = st.tokenAt || 0;
  if (env.IG_TOKEN && env.IG_TOKEN !== st.seed) { tok = env.IG_TOKEN; at = Date.now(); st.seed = env.IG_TOKEN; } // yeni token girildiyse onu kullan
  if (!tok) throw new Error('IG_TOKEN tanımlı değil');
  if (Date.now() - at > 20 * 864e5) {
    const j = await igJson(await fetch('https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token=' + encodeURIComponent(tok)));
    tok = j.access_token; at = Date.now();
  }
  st.token = tok; st.tokenAt = at;
  return tok;
}
// Açılış: ilk 12 post (profilde 4 sıra) aynı gün yarım saat arayla; sonra her akşam 19:00'dan itibaren günde bir post.
const LAUNCH = 14; // 12 post + yeni stille yeniden paylaşılan ilk 2
function trHour(d = new Date()) { return new Date(d.getTime() + 3 * 3600e3).getUTCHours(); }
function trH(d = new Date()) { const x = new Date(d.getTime() + 3 * 3600e3); return x.getUTCHours() + x.getUTCMinutes() / 60; }   // ondalıklı saat (20.5 = 20:30)
// Paylaşım saatleri (Türkiye): akşam 20:30 günlük bitki; öğlen 12:30 ek postlar; Threads 08:30 kavram, 12:30 'Biliyor muydunuz?', 15:00 yöresel ad sorusu, 17:30 rehber/tarif/sembol, 21:30 soru.
async function igPost(env) {
  const st = (await call(env, 'ig:state', 'get')) || {};
  if (st.reelPending && st.token) {   // video işlenince yayımla
    try {
      const s = await igJson(await fetch(IG + '/' + st.reelPending + '?fields=status_code&access_token=' + encodeURIComponent(st.token)));
      if (s.status_code === 'FINISHED') { await igJson(await fetch(IG + '/' + st.uid + '/media_publish', { method: 'POST', body: new URLSearchParams({ creation_id: st.reelPending, access_token: st.token }) })); st.reelPending = null; st.reels = (st.reels || 0) + 1; }
      else if (s.status_code === 'ERROR' || Date.now() - st.reelAt > 6 * 3600e3) { st.reelError = 'video işlenemedi'; st.reelPending = null; }
    } catch (e) { st.reelError = String(e.message || e).slice(0, 200); st.reelPending = null; }
    await call(env, 'ig:state', 'put', st);
  }
  if (!st.fix1) { st.fix1 = true; if (st.n === 15 && st.lastPlant === 'atkestanesi') { st.n = 14; st.lastDaily = null; st.catchup = true; } }   // 22 Ekim: yanlışlıkla 'zaten paylaşılmış' sayıldı
  const day = trDay(), hour = trHour(), n = st.n || 0;
  const launching = n < LAUNCH;
  if (st.pauseUntil && Date.now() < st.pauseUntil) return { skipped: 'istek sınırı; bekleniyor' };
  if (launching) {
    if (hour < 9 || hour >= 23) return { skipped: 'gece' };
    if (st.lastAt && Date.now() - st.lastAt < 28 * 60e3) return { skipped: 'yarım saat dolmadı' };
  } else {
    if (st.catchup) { if (hour < 9) return { skipped: 'gece' }; }   // kaçırılan postu sabah telafi et
    else if (trH() < 20.4 || st.lastDaily === day) return { skipped: 'bugün sırası değil' };   // açılış postu olan gün de akşam günlük post çıkar
  }
  try {
    const pr = await igAsset('p/' + n + '/post.json');
    if (!pr.ok) throw new Error(n + '. post bulunamadı; gece derlemesi bekleniyor');
    const post = await pr.json();
    const tok = await igToken(env, st);
    if (!st.uid) st.uid = (await igJson(await fetch(IG + '/me?fields=user_id,username&access_token=' + encodeURIComponent(tok)))).user_id;
    // Aynı post zaten çıkmış mı? (Önceki denemede paylaşım olup yanıt hata dönmüş olabilir.)
    const key = c => (c || '').split('\n').map(x => x.trim()).filter(x => x && !x.startsWith('🆕')).slice(0, 2).join('|');   // ortak '🆕' satırı karşılaştırılmaz
    const head = key(post.caption);
    const recent = await igJson(await fetch(IG + '/me/media?fields=id,caption&limit=5&access_token=' + encodeURIComponent(tok)));
    const dup = (recent.data || []).find(m => key(m.caption) === head);
    if (dup) {
      st.n = n + 1; st.last = day; st.lastAt = Date.now(); st.lastId = dup.id; st.lastPlant = post.id; st.error = null; st.errorAt = null;
      if (!launching && !st.catchup) st.lastDaily = day;
      st.catchup = false;
      await call(env, 'ig:state', 'put', st);
      return { n: st.n, skipped: 'zaten paylaşılmış' };
    }
    const form = o => { const f = new URLSearchParams(o); f.set('access_token', tok); return { method: 'POST', body: f }; };
    const kids = [];
    for (let i = 0; i < post.images.length; i++) {
      const base = { image_url: post.images[i], is_carousel_item: 'true' };
      let r;
      try { r = await igJson(await fetch(IG + '/' + st.uid + '/media', form(post.alts && post.alts[i] && !st.noAlt ? { ...base, alt_text: post.alts[i].slice(0, 1000) } : base))); }
      catch (e) { if (!/alt_text/i.test(String(e.message))) throw e; st.noAlt = true; r = await igJson(await fetch(IG + '/' + st.uid + '/media', form(base))); }
      kids.push(r.id);
    }
    const box = (await igJson(await fetch(IG + '/' + st.uid + '/media', form({ media_type: 'CAROUSEL', children: kids.join(','), caption: post.caption })))).id;
    for (let i = 0; i < 4; i++) {
      await new Promise(r => setTimeout(r, 5000));
      const s = await igJson(await fetch(IG + '/' + box + '?fields=status_code&access_token=' + encodeURIComponent(tok)));
      if (s.status_code === 'FINISHED') break;
      if (s.status_code === 'ERROR') throw new Error('Instagram görselleri işleyemedi');
    }
    const pub = await igJson(await fetch(IG + '/' + st.uid + '/media_publish', form({ creation_id: box })));
    st.n = n + 1; st.last = day; st.lastAt = Date.now(); st.lastId = pub.id; st.lastPlant = post.id; st.error = null; st.errorAt = null;
    if (!launching && !st.catchup) st.lastDaily = day;
    st.catchup = false;
    // Günlük postlarda: hikâye (takipçilere duyuru) ve Reels (profilde ve akışta görünür)
    if (!launching && post.story) {
      try {
        const sid = (await igJson(await fetch(IG + '/' + st.uid + '/media', form({ media_type: 'STORIES', image_url: post.story })))).id;
        await igJson(await fetch(IG + '/' + st.uid + '/media_publish', form({ creation_id: sid }))); st.storyError = null;
      } catch (e) { st.storyError = String(e.message || e).slice(0, 200); }
    }
    if (!launching && post.reel) {
      try {
        const rid = (await igJson(await fetch(IG + '/' + st.uid + '/media', form({ media_type: 'REELS', video_url: post.reel, caption: post.caption, share_to_feed: 'true' })))).id;
        st.reelPending = rid; st.reelAt = Date.now(); st.reelError = null;
      } catch (e) { st.reelError = String(e.message || e).slice(0, 200); }
    }
  } catch (e) {
    st.error = String(e.message || e).slice(0, 300); st.errorAt = new Date().toISOString();
    if (/limit/i.test(st.error)) st.pauseUntil = Date.now() + 2 * 3600e3;   // istek sınırına takılınca 2 saat bekle
  }
  await call(env, 'ig:state', 'put', st);
  return { n: st.n || 0, error: st.error };
}
// ---------- Threads: Instagram'daki günlük postun kısa metni ve aynı görselleri ----------
// Gerekli gizli değişken: TH_TOKEN (Threads API, uzun ömürlü token). 20 günde bir kendiliğinden yenilenir.
const TH = 'https://graph.threads.net/v1.0';
async function thPublish(tok, o) {   // tek görselli ya da yalnızca metin Threads postu
  if (!/#\S/.test(o.text)) o = { ...o, text: (o.text + '\n\n#şifalıbitkiler').slice(0, 500) };   // Threads'te tek konu etiketi
  const form = x => { const f = new URLSearchParams(x); f.set('access_token', tok); return { method: 'POST', body: f }; };
  const box = (await igJson(await fetch(TH + '/me/threads', form(o.image ? { media_type: 'IMAGE', image_url: o.image, text: o.text } : { media_type: 'TEXT', text: o.text })))).id;
  for (let i = 0; i < 6; i++) {
    await new Promise(r => setTimeout(r, 5000));
    const s = await igJson(await fetch(TH + '/' + box + '?fields=status&access_token=' + encodeURIComponent(tok)));
    if (s.status === 'FINISHED') break;
    if (s.status === 'ERROR') throw new Error('Threads görseli işleyemedi');
  }
  return igJson(await fetch(TH + '/me/threads_publish', form({ creation_id: box })));
}
// Bağlantıyı ana metinden alıp gönderinin altına ilk yorum olarak yazar (Threads ana metindeki bağlantıları daha az gösteriyor).
function thAyir(text, yedek) {
  const m = text.match(/(?:https?:\/\/)?bitkitabani\.com\/[^\s)]*/);
  const url = m ? m[0].replace(/^https?:\/\//, '') : yedek;
  if (!url) return { text, link: null };
  const kalan = m ? text.split('\n').filter(l => !l.includes(m[0])).join('\n').replace(/\n{3,}/g, '\n\n').trim() : text;
  return { text: kalan.length > 40 ? kalan : text, link: kalan.length > 40 ? url : null };
}
async function thYorum(tok, parentId, link) {
  if (!parentId || !link) return;
  const form = x => { const f = new URLSearchParams(x); f.set('access_token', tok); return { method: 'POST', body: f }; };
  const box = (await igJson(await fetch(TH + '/me/threads', form({ media_type: 'TEXT', text: 'Kaynaklar ve devamı 👉 ' + link, reply_to_id: parentId })))).id;
  await new Promise(r => setTimeout(r, 4000));
  await igJson(await fetch(TH + '/me/threads_publish', form({ creation_id: box })));
}
async function thPost(env) {
  env = { ...env, TH_TOKEN: env.TH_TOKEN || env.TH_Token };   // panelde 'TH_Token' olarak da eklenebilir
  const ig = (await call(env, 'ig:state', 'get')) || {};
  const st = (await call(env, 'th:state', 'get')) || {};
  const day = trDay(), hour = trHour();
  st.slot = st.slot || {};
  if (st.pauseUntil && Date.now() < st.pauseUntil) return { skipped: 'bekleniyor' };
  // Hangi post sırada? Günlük bitki (Instagram'dan sonra), sabah 10'da 'Biliyor muydunuz?', öğleden sonra 14'te rehber/tarif.
  let job = null;
  if ((ig.n || 0) >= LAUNCH && ig.last === day && ig.lastPlant && ig.lastPlant !== st.plant && st.last !== day + ':' + ig.lastPlant) job = 'gunluk';
  else if (trH() >= 8.4 && st.slot.kavram !== day) job = 'kavram';
  else if (trH() >= 12.4 && st.slot.sabah !== day) job = 'sabah';
  else if (trH() >= 14.9 && st.slot.ad !== day) job = 'ad';
  else if (trH() >= 17.4 && st.slot.ogle !== day) job = 'ogle';
  else if (trH() >= 21.4 && trH() < 23.5 && st.slot.soru !== day) job = 'soru';
  if (!job) return { skipped: 'sırası değil' };
  st.step = null;
  try {
    let tok = st.token, at = st.tokenAt || 0;
    if (env.TH_TOKEN && env.TH_TOKEN !== st.seed) { tok = env.TH_TOKEN; at = Date.now(); st.seed = env.TH_TOKEN; }
    if (Date.now() - at > 20 * 864e5) { tok = (await igJson(await fetch('https://graph.threads.net/refresh_access_token?grant_type=th_refresh_token&access_token=' + encodeURIComponent(tok)))).access_token; at = Date.now(); }
    st.token = tok; st.tokenAt = at;
    if (job === 'gunluk') {
      const pr = await igAsset('p/' + (ig.n - 1) + '/post.json');
      if (!pr.ok) throw new Error('post bulunamadı');
      const post = await pr.json();
      const paras = (post.caption || '').split(/\n\s*\n/).map(x => x.trim()).filter(Boolean);
      const body = paras.filter(x => !x.startsWith('🆕') && !x.startsWith('#') && !x.startsWith('Kaydırarak') && !x.startsWith('Kaynaklarıyla') && !x.startsWith('Bilgilendirme'));
      let text = '';
      for (const x of body.slice(0, 3)) if ((text + '\n\n' + x).length < 440) text += (text ? '\n\n' : '') + x;
      if (!text) text = body[0].slice(0, 440);
      text += '\n\n#şifalıbitkiler';
      const form = o => { const f = new URLSearchParams(o); f.set('access_token', tok); return { method: 'POST', body: f }; };
      const kids = [];
      st.step = 'görsel';
      for (const u of post.images.slice(0, 10)) kids.push((await igJson(await fetch(TH + '/me/threads', form({ media_type: 'IMAGE', image_url: u, is_carousel_item: 'true' })))).id);
      await new Promise(r => setTimeout(r, 12000));
      st.step = 'albüm';
      const box = (await igJson(await fetch(TH + '/me/threads', form({ media_type: 'CAROUSEL', children: kids.join(','), text })))).id;
      st.step = 'yayın';
      for (let i = 0; i < 6; i++) {
        await new Promise(r => setTimeout(r, 5000));
        const s = await igJson(await fetch(TH + '/' + box + '?fields=status&access_token=' + encodeURIComponent(tok)));
        if (s.status === 'FINISHED') break;
        if (s.status === 'ERROR') throw new Error('Threads görselleri işleyemedi');
      }
      const yay = await igJson(await fetch(TH + '/me/threads_publish', form({ creation_id: box })));
      st.last = day + ':' + post.id; st.plant = post.id;
      try { await thYorum(tok, yay && yay.id, 'bitkitabani.com/' + post.id + '/'); st.yorumHata = null; } catch (e) { st.yorumHata = String(e.message || e).slice(0, 160); }
    } else {
      const pr = await igAsset('threads.json');
      if (!pr.ok) throw new Error('threads.json bulunamadı');
      const plan = (await pr.json())[day];
      if (!plan || !plan[job]) { st.slot[job] = day; throw new Error('bugün için ' + job + ' metni yok'); }
      const ay = thAyir(plan[job].text, plan[job].bitki ? 'bitkitabani.com/' + plan[job].bitki + '/' : null);
      const pub = await thPublish(tok, { ...plan[job], text: ay.text });
      try { await thYorum(tok, pub && pub.id, ay.link); st.yorumHata = null; } catch (e) { st.yorumHata = String(e.message || e).slice(0, 160); }
      if (job === 'ad' && pub && pub.id) { st.adIds = st.adIds || {}; st.adIds[pub.id] = { bitki: plan[job].bitki || null, gun: day }; const ks = Object.keys(st.adIds); if (ks.length > 14) delete st.adIds[ks[0]]; }
      st.slot[job] = day;
    }
    st.n = (st.n || 0) + 1; st.error = null;
  } catch (e) {
    st.error = job + (st.step ? '/' + st.step : '') + ': ' + String(e.message || e).slice(0, 280); st.errorAt = new Date().toISOString();
    if (/limit/i.test(st.error)) st.pauseUntil = Date.now() + 2 * 3600e3;
    const fk = 'fails_' + job;
    st[fk] = (st.lastFailDay === day ? (st[fk] || 0) : 0) + 1; st.lastFailDay = day;
    if (st[fk] >= 3) { if (job === 'gunluk') st.plant = ig.lastPlant; else st.slot[job] = day; }   // aynı iş için günde en fazla 3 deneme
  }
  await call(env, 'th:state', 'put', st);
  return { n: st.n || 0, error: st.error };
}
// ---------- Facebook sayfası: Instagram'daki günlük bitki postu, aynı görseller ve sitenin bağlantısıyla ----------
// Gerekli gizli değişken: FB_TOKEN (sayfa token'ı; kullanıcı token'ı verilirse sayfanınki otomatik bulunur).
const FB = 'https://graph.facebook.com/v23.0';
async function fbAuth(env, st) {
  if (st.page && st.seed === env.FB_TOKEN) return st;
  let tok = env.FB_TOKEN, me = await igJson(await fetch(FB + '/me?fields=id,name&access_token=' + encodeURIComponent(tok)));
  try {   // kullanıcı token'ıysa yönettiği sayfalardan Bitki Tabanı'nı seç
    const acc = await igJson(await fetch(FB + '/me/accounts?fields=id,name,access_token&access_token=' + encodeURIComponent(tok)));
    const p = (acc.data || []).find(x => /bitki/i.test(x.name)) || (acc.data || [])[0];
    if (p) { tok = p.access_token; me = { id: p.id, name: p.name }; }
  } catch (e) { /* sayfa token'ı: /me/accounts desteklenmez */ }
  st.page = me.id; st.pageName = me.name; st.token = tok; st.seed = env.FB_TOKEN; st.error = null;
  return st;
}
async function fbPost(env) {   // günde en fazla 3 post: 12:30 günün kavramı (ritüel günlerinde takvim), 17:30 rehber/tarif/sembol, ~21:00 günlük bitki
  const ig = (await call(env, 'ig:state', 'get')) || {};
  const st = (await call(env, 'fb:state', 'get')) || {};
  const day = trDay();
  st.slot = st.slot || {};
  if (st.pauseUntil && Date.now() < st.pauseUntil) return { skipped: 'bekleniyor' };
  let job = null;
  try {
    await fbAuth(env, st);
    if ((ig.n || 0) >= LAUNCH && ig.last === day && ig.lastPlant && ig.lastPlant !== st.plant && Date.now() - (ig.lastAt || 0) > 25 * 60e3 && trH() >= 20.4 && trH() < 23.9) job = 'gunluk';
    else if (trH() >= 12.4 && trH() < 16 && st.slot.oglen !== day) job = 'oglen';
    else if (trH() >= 17.4 && trH() < 20 && st.slot.aksam !== day) job = 'aksam';
    if (!job) { await call(env, 'fb:state', 'put', st); return { skipped: 'sırası değil' }; }
    const form = o => { const f = new URLSearchParams(o); f.set('access_token', st.token); return { method: 'POST', body: f }; };
    const linkify = t => t.replace(/(^|[\s(])bitkitabani\.com\//g, '$1https://bitkitabani.com/');
    if (job === 'gunluk') {
      const pr = await igAsset('p/' + (ig.n - 1) + '/post.json');
      if (!pr.ok) throw new Error('post bulunamadı');
      const post = await pr.json();
      const paras = (post.caption || '').split(/\n\s*\n/).map(x => x.trim()).filter(Boolean);
      const body = paras.filter(x => !x.startsWith('#') && !x.startsWith('Kaydırarak') && !x.startsWith('Kaynaklarıyla') && !/profil/i.test(x));
      const message = body.join('\n\n') + '\n\nDevamı ve kaynaklar: https://bitkitabani.com/' + post.id + '/\n\n#şifalıbitkiler #bitkitabanı';
      const ids = [];
      for (const u of post.images.slice(0, 10)) ids.push((await igJson(await fetch(FB + '/' + st.page + '/photos', form({ url: u, published: 'false' })))).id);
      const o = { message };
      ids.forEach((id, i) => { o['attached_media[' + i + ']'] = JSON.stringify({ media_fbid: id }); });
      st.lastId = (await igJson(await fetch(FB + '/' + st.page + '/feed', form(o)))).id;
      st.plant = post.id;
    } else {
      st.slot[job] = day;   // hata olsa da aynı slotu gün içinde tekrar deneme (spam olmasın)
      const pr = await igAsset('threads.json');
      if (!pr.ok) throw new Error('threads.json bulunamadı');
      const plan = (await pr.json())[day] || {};
      const ritual = plan.sabah && /^Bugün /.test(plan.sabah.text);
      const p = job === 'oglen' ? (ritual ? plan.sabah : (plan.kavram || plan.sabah)) : plan.ogle;
      if (!p) throw new Error('bugün için ' + job + ' metni yok');
      const text = linkify(p.text);
      st.lastId = p.image ? (await igJson(await fetch(FB + '/' + st.page + '/photos', form({ url: p.image, caption: text })))).id
                          : (await igJson(await fetch(FB + '/' + st.page + '/feed', form({ message: text })))).id;
    }
    st.last = day; st.n = (st.n || 0) + 1; st.error = null; st.fails = 0;
  } catch (e) {
    st.error = (job ? job + ': ' : '') + String(e.message || e).slice(0, 300); st.errorAt = new Date().toISOString();
    if (/limit/i.test(st.error)) st.pauseUntil = Date.now() + 2 * 3600e3;
    if (job === 'gunluk') { st.fails = (st.failDay === day ? (st.fails || 0) : 0) + 1; st.failDay = day; if (st.fails >= 3) st.plant = ig.lastPlant; }
  }
  await call(env, 'fb:state', 'put', st);
  return { n: st.n || 0, error: st.error };
}
// ---------- Ayın ilk günü: 'Bu ay doğada' postu (Instagram tek görsel + Threads) ----------
async function aylikPost(env) {
  const day = trDay(), hour = trHour();
  if (day.slice(8) !== '01' || trH() < 12.4) return;
  const key = day.slice(0, 7);
  const ig = (await call(env, 'ig:state', 'get')) || {};
  const th = (await call(env, 'th:state', 'get')) || {};
  if (ig.aylik === key && (!(env.TH_TOKEN || env.TH_Token) || (th.slot || {}).aylik === key)) return;
  const pr = await igAsset('aylik.json');
  if (!pr.ok) return;
  const a = await pr.json();
  if (a.ay !== key) return;
  if (ig.aylik !== key && ig.token && ig.uid && !(ig.pauseUntil && Date.now() < ig.pauseUntil)) {
    try {
      const form = o => { const f = new URLSearchParams(o); f.set('access_token', ig.token); return { method: 'POST', body: f }; };
      const box = (await igJson(await fetch(IG + '/' + ig.uid + '/media', form({ image_url: a.image, caption: a.caption, alt_text: a.alt })))).id;
      await new Promise(r => setTimeout(r, 8000));
      await igJson(await fetch(IG + '/' + ig.uid + '/media_publish', form({ creation_id: box })));
      ig.aylik = key; ig.aylikError = null;
    } catch (e) { ig.aylikError = String(e.message || e).slice(0, 200); ig.aylikFails = (ig.aylikFails || 0) + 1; if (ig.aylikFails >= 3) { ig.aylik = key; ig.aylikFails = 0; } }
    await call(env, 'ig:state', 'put', ig);
  }
  if ((env.TH_TOKEN || env.TH_Token) && th.token && (th.slot || {}).aylik !== key) {
    th.slot = th.slot || {};
    try { await thPublish(th.token, { text: a.threads, image: a.image }); th.slot.aylik = key; }
    catch (e) { th.error = 'aylik: ' + String(e.message || e).slice(0, 200); th.errorAt = new Date().toISOString(); th.aylikFails = (th.aylikFails || 0) + 1; if (th.aylikFails >= 3) { th.slot.aylik = key; th.aylikFails = 0; } }
    await call(env, 'th:state', 'put', th);
  }
}
// ---------- Haftalık ek postlar (Pzt/Çar/Cum öğlen): Instagram + Threads albüm ----------
async function ekPost(env) {
  const day = trDay(), hour = trHour();
  if (trH() < 12.4 || hour >= 22) return;
  const ig = (await call(env, 'ig:state', 'get')) || {};
  const th = (await call(env, 'th:state', 'get')) || {};
  const thOn = !!(env.TH_TOKEN || env.TH_Token) && th.token;
  if ((ig.ek === day || day < '2026-11-16') && (!thOn || (th.slot || {}).ek === day)) return;
  const pr = await igAsset('ek.json');
  if (!pr.ok) return;
  const a = (await pr.json())[day];
  if (!a) return;
  // Yeni hesap: Instagram çok sık paylaşımı kısıtlıyor; ek postlar Instagram'da 16 Kasım'dan sonra başlar (Threads'te hemen).
  if (day >= '2026-11-16' && ig.ek !== day && ig.token && ig.uid && !(ig.pauseUntil && Date.now() < ig.pauseUntil)) {
    try {
      const form = o => { const f = new URLSearchParams(o); f.set('access_token', ig.token); return { method: 'POST', body: f }; };
      const kids = [];
      for (let i = 0; i < a.images.length; i++) kids.push((await igJson(await fetch(IG + '/' + ig.uid + '/media', form({ image_url: a.images[i], is_carousel_item: 'true', ...(a.alts && a.alts[i] && !ig.noAlt ? { alt_text: a.alts[i] } : {}) })))).id);
      const box = (await igJson(await fetch(IG + '/' + ig.uid + '/media', form({ media_type: 'CAROUSEL', children: kids.join(','), caption: a.caption })))).id;
      await new Promise(r => setTimeout(r, 8000));
      await igJson(await fetch(IG + '/' + ig.uid + '/media_publish', form({ creation_id: box })));
      ig.ek = day; ig.ekError = null; ig.ekSayi = (ig.ekSayi || 0) + 1;
    } catch (e) {
      ig.ekError = String(e.message || e).slice(0, 200);
      if (/limit/i.test(ig.ekError)) ig.pauseUntil = Date.now() + 2 * 3600e3;
      ig.ekFails = (ig.ekFailDay === day ? (ig.ekFails || 0) : 0) + 1; ig.ekFailDay = day; if (ig.ekFails >= 3) ig.ek = day;
    }
    await call(env, 'ig:state', 'put', ig);
  }
  if (thOn && (th.slot || {}).ek !== day) {
    th.slot = th.slot || {};
    try {
      const form = o => { const f = new URLSearchParams(o); f.set('access_token', th.token); return { method: 'POST', body: f }; };
      const kids = [];
      for (const u of a.images) kids.push((await igJson(await fetch(TH + '/me/threads', form({ media_type: 'IMAGE', image_url: u, is_carousel_item: 'true' })))).id);
      await new Promise(r => setTimeout(r, 12000));   // görseller işlenmeden albüm kurulamıyor
      const box = (await igJson(await fetch(TH + '/me/threads', form({ media_type: 'CAROUSEL', children: kids.join(','), text: (a.threads + (/#\S/.test(a.threads) ? '' : '\n\n#şifalıbitkiler')).slice(0, 500) })))).id;
      await new Promise(r => setTimeout(r, 10000));
      await igJson(await fetch(TH + '/me/threads_publish', form({ creation_id: box })));
      th.slot.ek = day; th.n = (th.n || 0) + 1;
    } catch (e) {
      th.error = 'ek: ' + String(e.message || e).slice(0, 200); th.errorAt = new Date().toISOString();
      th.ekFails = (th.ekFailDay === day ? (th.ekFails || 0) : 0) + 1; th.ekFailDay = day; if (th.ekFails >= 3) th.slot.ek = day;
    }
    await call(env, 'th:state', 'put', th);
  }
}
// ---------- E-posta bülteni: çift onaylı kayıt, haftalık otomatik gönderim (Resend) ----------
// Gerekli gizli değişken: RESEND_KEY. Saklanan: e-posta adresi, rıza tarihi, duyuru tercihi, kaynak sayfa. Başka bir şey saklanmaz.
const MAIL_FROM = 'Bitki Tabanı <bulten@bitkitabani.com>';
const SITE = 'https://bitkitabani.com';
async function sendMail(env, to, subject, html, text) {
  const key = env.RESEND_KEY || env.RESEND_Key;
  if (!key) throw new Error('RESEND_KEY tanımlı değil');
  const r = await fetch('https://api.resend.com/emails', { method: 'POST', headers: { authorization: 'Bearer ' + key, 'content-type': 'application/json' },
    body: JSON.stringify({ from: MAIL_FROM, to: [to], reply_to: 'iletisim@bitkitabani.com', subject, html, text, headers: { 'List-Unsubscribe': '<' + SITE + '/api/abone/cik?t=' + (html.match(/cik\?t=([a-f0-9]+)/) || [])[1] + '>' } }) });
  if (!r.ok) throw new Error('Resend ' + r.status + ' ' + (await r.text()).slice(0, 200));
}
const hex = n => [...crypto.getRandomValues(new Uint8Array(n))].map(b => b.toString(16).padStart(2, '0')).join('');
const esc = s => String(s || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
function mailWrap(inner, t) {
  return `<!doctype html><html lang="tr"><body style="margin:0;background:#F1EADD;font-family:Georgia,serif;color:#1C2140"><div style="max-width:560px;margin:0 auto;padding:28px 22px">
<p style="font-size:22px;font-weight:bold;margin:0 0 18px">Bitki <i style="color:#A3271B">Tabanı</i></p>${inner}
<hr style="border:0;border-top:1px solid #DCCFBA;margin:28px 0 14px"><p style="font-family:Arial,sans-serif;font-size:12px;color:#5D5866;line-height:1.5">Bu e-postayı bitkitabani.com’da bültene kaydolduğunuz için alıyorsunuz. Bilgilendirme amaçlıdır; tıbbi tavsiye yerine geçmez.<br><a href="${SITE}/api/abone/cik?t=${t}" style="color:#5D5866">Bültenden çık</a> · <a href="${SITE}/gizlilik/" style="color:#5D5866">Gizlilik</a></p></div></body></html>`;
}
async function confirmMail(env, email, t) {
  const link = `${SITE}/api/abone/onay?t=${t}`;
  const inner = `<p style="font-size:17px;line-height:1.55">Merhaba,</p><p style="font-size:17px;line-height:1.55">Bitki Tabanı bültenine kaydolmak için aşağıdaki düğmeye tıklayın. Tıklamazsanız adresiniz listeye eklenmez ve 7 gün sonra silinir.</p>
<p style="margin:26px 0"><a href="${link}" style="background:#A3271B;color:#fff;text-decoration:none;padding:13px 22px;border-radius:999px;font-family:Arial,sans-serif;font-size:15px">Kaydımı onayla</a></p>
<p style="font-family:Arial,sans-serif;font-size:13px;color:#5D5866">Düğme çalışmazsa bu adresi tarayıcınıza yapıştırın:<br>${link}</p>`;
  await sendMail(env, email, 'Bitki Tabanı bülteni: kaydınızı onaylayın', mailWrap(inner, t), `Bitki Tabanı bültenine kaydolmak için bu bağlantıyı açın: ${link}`);
}
async function aboneApi(req, env, url) {
  const L = (await call(env, 'abone:list', 'get')) || {};
  if (url.pathname === '/api/abone' && req.method === 'POST') {
    const b = await req.json().catch(() => ({}));
    if (b.hp) return json({ ok: true });   // bot tuzağı
    const email = String(b.email || '').trim().toLowerCase();
    if (!/^[^\s@<>]{1,64}@[^\s@<>]{1,190}\.[a-z]{2,}$/.test(email)) return json({ error: 'Geçerli bir e-posta adresi yazın.' }, 400);
    if (!b.riza) return json({ error: 'Kayıt için onay kutusunu işaretleyin.' }, 400);
    const now = new Date().toISOString(); const old = L[email];
    if (old && old.on) { old.d = !!b.duyuru || old.d; if (b.kurs && typeof old.kurs !== 'number') { old.kurs = 0; old.kursAt = 0; } await call(env, 'abone:list', 'put', L); return json({ ok: true, zaten: true }); }
    if (old && old.sent && Date.now() - Date.parse(old.sent) < 10 * 60e3) return json({ ok: true });   // art arda gönderme yok
    const t = (old && old.t) || hex(16);
    L[email] = { t, on: false, d: !!b.duyuru, at: now, src: String(b.kaynak || '').slice(0, 80), sent: null, ...(b.kurs ? { kurs: 0 } : {}) };
    try { await confirmMail(env, email, t); L[email].sent = now; } catch (e) { L[email].err = String(e.message || e).slice(0, 120); }
    await call(env, 'abone:list', 'put', L);
    return json({ ok: true });
  }
  const t = url.searchParams.get('t') || '';
  const email = Object.keys(L).find(k => L[k].t === t && /^[a-f0-9]{32}$/.test(t));
  if (url.pathname === '/api/abone/onay') {
    if (email) { L[email].on = true; L[email].onay = L[email].onay || new Date().toISOString(); if (L[email].kurs === 0) await kursGonder(env, email, L[email]).catch(() => null); await call(env, 'abone:list', 'put', L); }
    return Response.redirect(SITE + (email ? '/bulten/onaylandi/' : '/bulten/'), 302);
  }
  if (url.pathname === '/api/abone/cik') {
    if (email) { delete L[email]; await call(env, 'abone:list', 'put', L); }   // çıkınca adres tamamen silinir
    if (req.method === 'POST') return new Response('ok');   // e-posta istemcilerinin tek tık çıkışı
    return Response.redirect(SITE + '/bulten/ayrildiniz/', 302);
  }
  return json({ error: 'yok' }, 404);
}
async function kursGonder(env, email, a) {   // sıradaki kurs dersini gönder
  const pr = await igAsset('kurs.json'); if (!pr.ok) throw new Error('kurs.json yok');
  const K = await pr.json(); const d = K[a.kurs]; if (!d) return;
  await sendMail(env, email, 'Bitki Tabanı · ' + d.konu, mailWrap(d.html, a.t), d.text + `\n\nKurstan ve bültenden çıkmak için: ${SITE}/api/abone/cik?t=${a.t}`);
  a.kurs += 1; a.kursAt = Date.now();
}
// Pazar 10:00'dan sonra haftalık bülten; bekleyen onay e-postaları ve 7 günü geçen onaysız kayıtlar da burada işlenir.
async function bultenCron(env) {
  if (!(env.RESEND_KEY || env.RESEND_Key)) return;
  const L = (await call(env, 'abone:list', 'get')) || {}; let changed = false;
  for (const [e, a] of Object.entries(L)) {
    if (!a.on && Date.now() - Date.parse(a.at) > 7 * 864e5) { delete L[e]; changed = true; continue; }
    if (!a.on && !a.sent) { try { await confirmMail(env, e, a.t); a.sent = new Date().toISOString(); a.err = null; } catch (x) { a.err = String(x.message || x).slice(0, 120); } changed = true; }
  }
  const day = trDay(), hour = trHour(), dow = new Date(Date.now() + 3 * 3600e3).getUTCDay();
  if (hour >= 8 && hour < 21) {   // kurs: onaydan sonra her gün bir ders (en az 20 saat arayla)
    let k = 0;
    for (const [e, a] of Object.entries(L)) {
      if (k >= 40) break;
      if (a.on && typeof a.kurs === 'number' && a.kurs < 7 && Date.now() - (a.kursAt || 0) > 20 * 3600e3) {
        try { await kursGonder(env, e, a); k++; changed = true; } catch (x) { a.err = String(x.message || x).slice(0, 120); changed = true; break; }
      }
    }
  }
  const st = (await call(env, 'bulten:state', 'get')) || {};
  if (dow === 0 && hour >= 10 && st.last !== day) {
    const pr = await igAsset('bulten.json');
    if (pr.ok) {
      const B = await pr.json(); let n = 0;
      const todo = Object.entries(L).filter(([e, a]) => a.on && a.lastWeek !== B.hafta && !(typeof a.kurs === 'number' && a.kurs < 7)).slice(0, 90);   // günlük gönderim sınırının altında kal
      for (const [e, a] of todo) {
        try { await sendMail(env, e, B.konu, mailWrap(B.html, a.t), B.text + `\n\nBültenden çıkmak için: ${SITE}/api/abone/cik?t=${a.t}`); a.lastWeek = B.hafta; n++; changed = true; }
        catch (x) { st.err = String(x.message || x).slice(0, 160); break; }
      }
      if (Object.values(L).every(a => !a.on || a.lastWeek === B.hafta || (typeof a.kurs === 'number' && a.kurs < 7))) st.last = day;   // kalanlar bir sonraki çalışmada
      st.sayi = (st.sayi || 0) + n;
      await call(env, 'bulten:state', 'put', st);
    }
  }
  if (changed) await call(env, 'abone:list', 'put', L);
}

// ---------- Okur katkıları: site formu ve Threads 'yörende ne denir?' yanıtları; site sahibi onaylar ----------
const KATKI_TUR = { ad: 'Yöresel ad', kullanim: 'Yöresel kullanım', duzeltme: 'Düzeltme', iletisim: 'İletişim', isbirligi: 'İş birliği', basin: 'Basın' };
async function katkiEkle(env, k) {
  const L = (await call(env, 'katki:list', 'get')) || [];
  if (k.ext && L.some(x => x.ext === k.ext)) return false;
  L.push({ id: crypto.randomUUID().slice(0, 12), at: new Date().toISOString(), durum: 'bekliyor', ...k });
  while (L.length > 2000) L.shift();
  await call(env, 'katki:list', 'put', L); return true;
}
// Yorum bildirimi: Instagram ve Threads'e gelen yeni yorumlar Telegram botundan site sahibine özel mesajla gelir.
// Kurulum: sahibi bota "/start 520364" yazar; bot o sohbeti kaydeder. İlk taramada mevcut yorumlar bildirilmeden işaretlenir.
async function bildirim(env) {
  const tk = String(env.TG_TOKEN || '').trim().replace(/^bot/i, '').replace(/\s+/g, ''); if (!tk) return;
  const TG = 'https://api.telegram.org/bot' + tk;
  const st = (await call(env, 'tg:bildir', 'get')) || { seen: [] };
  const gonder = (text) => fetch(TG + '/sendMessage', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ chat_id: st.chat, text, parse_mode: 'HTML', link_preview_options: { is_disabled: true } }) });
  if (!st.chat) {
    const u = await (await fetch(TG + '/getUpdates?timeout=0&offset=' + (st.offset || 0))).json();
    for (const x of u.result || []) {
      st.offset = x.update_id + 1; const m = x.message;
      if (m && m.chat && m.chat.type === 'private' && /^\/start\s+520364\b/.test(m.text || '')) { st.chat = m.chat.id; await gonder('Tamam 🌿 Instagram ve Threads’e gelen yeni yorumları buradan sana bildireceğim.'); break; }
    }
    await call(env, 'tg:bildir', 'put', st);
    if (!st.chat) return;
  }
  if (st.son && Date.now() - st.son < 25 * 60e3) return;
  st.son = Date.now();
  const seen = new Set(st.seen || []), yeni = [], esc = x => String(x || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  try {
    const ig = (await call(env, 'ig:state', 'get')) || {};
    if (ig.token && ig.uid) {
      const q = '&access_token=' + encodeURIComponent(ig.token);
      if (!st.igUser) st.igUser = ((await igJson(await fetch(IG + '/' + ig.uid + '?fields=username' + q))) || {}).username || '';
      const L = (await igJson(await fetch(IG + '/' + ig.uid + '/media?fields=id,caption,permalink,comments_count&limit=12' + q))).data || [];
      for (const md of L) if (md.comments_count) {
        const C = (await igJson(await fetch(IG + '/' + md.id + '/comments?fields=id,text,username,timestamp&limit=50' + q))).data || [];
        for (const c of C) if (!seen.has('ig:' + c.id)) { seen.add('ig:' + c.id); if (c.username !== st.igUser) yeni.push(['Instagram', c.username, c.text, md.permalink, (md.caption || '').split('\n')[0]]); }
      }
    }
  } catch (e) { st.hata = 'ig: ' + String(e.message || e).slice(0, 120); }
  try {
    const th = (await call(env, 'th:state', 'get')) || {};
    if (th.token) {
      const q = '&access_token=' + encodeURIComponent(th.token);
      if (!st.thUser) st.thUser = ((await igJson(await fetch(TH + '/me?fields=username' + q))) || {}).username || '';
      const L = (await igJson(await fetch(TH + '/me/threads?fields=id,text,permalink&limit=12' + q))).data || [];
      for (const md of L) {
        const C = (await igJson(await fetch(TH + '/' + md.id + '/replies?fields=id,text,username,timestamp' + q))).data || [];
        for (const c of C) if (!seen.has('th:' + c.id)) { seen.add('th:' + c.id); if (c.username !== st.thUser) yeni.push(['Threads', c.username, c.text, md.permalink, (md.text || '').split('\n')[0]]); }
      }
    }
  } catch (e) { st.hata = 'th: ' + String(e.message || e).slice(0, 120); }
  st.seen = [...seen].slice(-800);
  if (!st.ilk) { st.ilk = true; await call(env, 'tg:bildir', 'put', st); return; }   // ilk tarama: eski yorumlar bildirilmez
  if (yeni.length) {
    const t = '💬 <b>' + yeni.length + ' yeni yorum</b>\n\n' + yeni.slice(0, 15).map(([k, u, x, l, b]) => `<b>${k}</b> · @${esc(u)}\n“${esc(String(x).slice(0, 300))}”\n<a href="${esc(l)}">${esc(b.slice(0, 60)) || 'gönderi'} →</a>`).join('\n\n');
    await gonder(t);
  }
  await call(env, 'tg:bildir', 'put', st);
}
async function thYanitlar(env) {   // günde bir: son 'ad' postlarına gelen yanıtlar katkı listesine
  const st = (await call(env, 'th:state', 'get')) || {};
  if (!st.token || !st.adIds || st.yanitGun === trDay()) return;
  st.yanitGun = trDay();
  for (const [mid, m] of Object.entries(st.adIds)) {
    try {
      const r = await igJson(await fetch(TH + '/' + mid + '/replies?fields=id,text,username,timestamp&access_token=' + encodeURIComponent(st.token)));
      for (const y of r.data || []) if (y.text) await katkiEkle(env, { src: 'threads', ext: 'th:' + y.id, bitki: m.bitki, tur: 'ad', metin: String(y.text).slice(0, 600), ad: y.username ? '@' + y.username : '', yore: '' });
    } catch (e) { st.yanitHata = String(e.message || e).slice(0, 160); }
  }
  await call(env, 'th:state', 'put', st);
}
async function katkiApi(req, env, url) {
  if (url.pathname === '/api/katki' && req.method === 'POST') {
    const b = await req.json().catch(() => ({}));
    if (b.hp) return json({ ok: true });   // bot tuzağı
    const bitki = String(b.bitki || '').replace(/[^a-z0-9]/g, '').slice(0, 40) || 'genel', tur = KATKI_TUR[b.tur] ? b.tur : 'kullanim';
    const metin = String(b.metin || '').trim().slice(0, 2000);
    if (metin.length < 3) return json({ error: 'Lütfen kısa da olsa bir not yazın.' }, 400);
    const ip = req.headers.get('cf-connecting-ip') || 'x', key = trDay() + ':' + ip;
    const RL = (await call(env, 'katki:rl', 'get')) || {};
    for (const k of Object.keys(RL)) if (!k.startsWith(trDay())) delete RL[k];
    if ((RL[key] = (RL[key] || 0) + 1) > 8) return json({ error: 'Bugün için yeterince not gönderdiniz, teşekkürler.' }, 429);
    await call(env, 'katki:rl', 'put', RL);
    await katkiEkle(env, { src: 'form', bitki, tur, metin, yore: String(b.yore || '').slice(0, 80), ad: String(b.ad || '').slice(0, 60), kaynak: String(b.kaynak || '').slice(0, 200), bitkiAd: String(b.bitki_ad || '').slice(0, 60), eposta: String(b.eposta || '').trim().slice(0, 120) });
    return json({ ok: true });
  }
  if (url.pathname === '/api/katki-onayli' && req.method === 'GET') {   // derleme bunu okur
    const L = (await call(env, 'katki:list', 'get')) || [];
    return json(L.filter(x => x.durum === 'onay').map(({ bitki, tur, metin, yore, ad, src, at }) => ({ bitki, tur, metin, yore, ad, src, at })));
  }
  const s = await session(req, env);
  if (!s) return json({ error: 'giriş yok', not: 'bitkitabani.com/hesap/ sayfasından Google ile giriş yap' }, 401);
  if (!s.admin) return json({ error: 'yetki', hesap: s.ep || 'eski oturum: çıkış yapıp yeniden gir' }, 403);
  if (url.pathname === '/api/katki-sosyal-dene' && req.method === 'GET') {   // yönetici: ?k=tg|bsky
    const k = url.searchParams.get('k');
    if (k === 'tg' && env.TG_TOKEN) return json(await tgPost(env, true));
    if (k === 'bsky' && env.BSKY_HANDLE) return json(await bskyPost(env, true));
    return json({ error: 'anahtar yok', tg: !!env.TG_TOKEN, bsky: !!env.BSKY_HANDLE });
  }
  if (url.pathname === '/api/katki-liste' && req.method === 'GET') return json((await call(env, 'katki:list', 'get')) || []);
  if (url.pathname === '/api/katki-karar' && req.method === 'POST') {
    const b = await req.json().catch(() => ({})); const L = (await call(env, 'katki:list', 'get')) || [];
    const k = L.find(x => x.id === b.id); if (!k) return json({ error: 'yok' }, 404);
    if (['onay', 'red', 'bekliyor'].includes(b.karar)) k.durum = b.karar;
    if (typeof b.metin === 'string') k.metin = b.metin.slice(0, 600);
    if (typeof b.bitki === 'string') k.bitki = b.bitki.replace(/[^a-z0-9]/g, '').slice(0, 40);
    await call(env, 'katki:list', 'put', L); return json({ ok: true });
  }
  return json({ error: 'yok' }, 404);
}

// ---------- Akıllı arama: soru cümlesini bitki metinleriyle anlam olarak karşılaştırır (Workers AI, bge-m3) ----------
const ARA_MODEL = '@cf/baai/bge-m3';   // gömmeler yalnızca 't' alanından; 'c' cümleleri sonuç açıklaması içindir
function f32b64(a) { const u = new Uint8Array(new Float32Array(a).buffer); let s = ''; for (let i = 0; i < u.length; i += 8192) s += String.fromCharCode(...u.subarray(i, i + 8192)); return btoa(s); }
function b64f32(s) { const b = Uint8Array.from(atob(s), c => c.charCodeAt(0)); return new Float32Array(b.buffer); }
async function araVek(env, req, data) {
  const ver = data.ver; const meta = await call(env, 'ara:meta', 'get');
  if (meta && meta.ver === ver) { const out = []; for (let k = 0; k < meta.n; k++) out.push(...(await call(env, 'ara:vec:' + k, 'get')).map(b64f32)); return out; }
  const out = []; let k = 0;
  for (let i = 0; i < data.p.length; i += 25, k++) {
    const r = await env.AI.run(ARA_MODEL, { text: data.p.slice(i, i + 25).map(x => x.t) });
    const vs = r.data.map(v => { const n = Math.hypot(...v); return v.map(x => x / n); });
    out.push(...vs.map(v => new Float32Array(v))); await call(env, 'ara:vec:' + k, 'put', vs.map(f32b64));
  }
  await call(env, 'ara:meta', 'put', { ver, n: k }); return out;
}
async function araApi(req, env, url) {
  const q = String(url.searchParams.get('q') || '').trim().slice(0, 200);
  if (q.length < 3) return json({ error: 'Biraz daha uzun yaz.' }, 400);
  if (!env.AI) return json({ error: 'Arama şu an kapalı.' }, 503);
  const ip = req.headers.get('cf-connecting-ip') || 'x', key = trDay() + ':' + ip;
  const RL = (await call(env, 'ara:rl', 'get')) || {}; for (const k of Object.keys(RL)) if (!k.startsWith(trDay())) delete RL[k];
  if ((RL[key] = (RL[key] || 0) + 1) > 80) return json({ error: 'Bugünlük arama sınırına ulaştın, yarın yeniden dene.' }, 429);
  await call(env, 'ara:rl', 'put', RL);
  const data = await (await env.ASSETS.fetch(new Request(url.origin + '/ara.json'))).json();
  const V = await araVek(env, req, data);
  const qv = (await env.AI.run(ARA_MODEL, { text: [q] })).data[0]; const n = Math.hypot(...qv);
  const sem = V.map(v => { let s = 0; for (let j = 0; j < v.length; j++) s += v[j] * qv[j] / n; return s; });
  // anlam araması + kelime eşleşmesi: aranan kelimelerin hepsini içeren cümlesi olan bitki öne çıkar
  const norm = t => t.toLocaleLowerCase('tr').normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/ı/g, 'i');
  const kok = t => norm(t).split(/[^a-z0-9]+/).filter(x => x.length >= 3).map(x => x.slice(0, 5));
  const qk = [...new Set(kok(q))];
  const cumle = p => {
    let best = null, bs = 0;
    for (const [lab, an, c] of p.c || []) { const ck = kok(c); const s = qk.filter(k => ck.some(x => x.startsWith(k) || (x.length >= 4 && k.startsWith(x)))).length; if (s > bs) { bs = s; best = { etiket: lab, bolum: an, cumle: c }; } }
    return { best, kw: qk.length ? bs / qk.length : 0 };
  };
  const L = data.p.map((p, i) => { const c = cumle(p); return { i, c, s: sem[i] + 0.4 * c.kw + (c.kw === 1 ? 0.2 : 0), sem: sem[i] }; });
  const tam = L.some(x => x.c.kw === 1);
  const sonuc = L.filter(x => tam ? x.c.kw === 1 || (x.sem > 0.5 && x.c.kw >= 0.5) : x.sem > 0.42 || x.c.kw >= 0.5)
    .sort((a, b) => b.s - a.s).slice(0, 10)
    .map(x => { const p = data.p[x.i]; return { id: p.id, tr: p.tr, la: p.la, guv: p.guv, ...(x.c.best || { etiket: 'Sayfa', bolum: '', cumle: p.kisa }), skor: Math.round(x.s * 100) / 100 }; });
  return json({ q, sonuc }, 200, { 'cache-control': 'no-store' });
}

// ---------- Telegram kanalı ve Bluesky: günlük bitki postu (Instagram'dan sonra, akşam) ----------
// Gizli değişkenler: TG_TOKEN, TG_CHAT (@kanal) · BSKY_HANDLE, BSKY_PASSWORD (uygulama şifresi)
async function gunlukPost(env, zorla) {   // Instagram'da bugün paylaşılan bitkinin metni ve ilk görseli
  const ig = (await call(env, 'ig:state', 'get')) || {};
  if (!ig.lastPlant || !ig.n || (!zorla && ig.last !== trDay())) return null;   // deneme: son paylaşılanı kullan
  const pr = await igAsset('p/' + (ig.n - 1) + '/post.json'); if (!pr.ok) return null;
  const post = await pr.json();
  const paras = (post.caption || '').split(/\n\s*\n/).map(x => x.trim()).filter(x => x && !/^(🆕|#|Kaydırarak|Kaynaklarıyla|Bilgilendirme)/.test(x) && !/profil/i.test(x));
  return { id: post.id, paras, image: (post.images || [])[0], url: 'https://bitkitabani.com/' + post.id + '/', alt: (post.alts || [])[0] || '' };
}
async function tgPost(env, zorla) {
  const st = (await call(env, 'tg:state', 'get')) || {}; const day = trDay();
  if (!zorla && (st.last === day || trH() < 20.6)) return { skipped: 'sırası değil' };
  try {
    const g = await gunlukPost(env, zorla); if (!g) return { skipped: 'bugün post yok' };
    let cap = ''; for (const x of g.paras) if ((cap + '\n\n' + x).length < 860) cap += (cap ? '\n\n' : '') + x;
    const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    const body = { chat_id: env.TG_CHAT, caption: esc(cap) + `\n\n<a href="${g.url}">Devamı ve kaynaklar: bitkitabani.com</a>`, parse_mode: 'HTML' };
    const tk = String(env.TG_TOKEN).trim().replace(/^bot/i, '').replace(/\s+/g, '');   // kopyalarken gelen boşluk/satır sonu temizlenir
    const r = await fetch('https://api.telegram.org/bot' + tk + (g.image ? '/sendPhoto' : '/sendMessage'), { method: 'POST', headers: { 'content-type': 'application/json' },
      body: JSON.stringify(g.image ? { ...body, photo: g.image } : { chat_id: env.TG_CHAT, text: body.caption, parse_mode: 'HTML' }) });
    const j = await r.json(); if (!j.ok) throw new Error((j.description || 'telegram') + (j.error_code === 404 ? ' (TG_TOKEN hatalı: BotFather’daki satırın tamamı, 123456:ABC… biçiminde olmalı)' : ''));
    st.kanal = j.result && j.result.chat ? (j.result.chat.title || '') + ' · ' + (j.result.chat.username ? '@' + j.result.chat.username : 'özel kanal') + ' · mesaj ' + j.result.message_id : null;
    if (!zorla) st.last = day; st.plant = g.id; st.n = (st.n || 0) + 1; st.error = null;
  } catch (e) { st.error = String(e.message || e).slice(0, 200); st.errorAt = new Date().toISOString(); if (!zorla) st.last = day; }
  await call(env, 'tg:state', 'put', st); return st;
}
// Telegram arşiv: kanal yeni olduğu için Instagram'daki eski bitki postları gün içinde sırayla (10:00, 11:30, 14:00, 15:30, 19:00, 23:00) gönderilir; arşiv bitince durur.
async function tgArsiv(env) {
  const day = trDay(), h = trH(), SL = [10, 11.5, 14, 15.5, 19, 23];
  const st = (await call(env, 'tg:arsiv', 'get')) || { i: 0, done: {} };
  const ig = (await call(env, 'ig:state', 'get')) || {};
  if (!ig.n || st.i >= ig.n - 1) return { skipped: 'arşiv bitti' };
  const k = SL.find(t => h >= t && h < t + 1.5 && st.done[t] !== day);
  if (k === undefined) return { skipped: 'sırası değil' };
  st.done[k] = day;
  try {
    const pr = await igAsset('p/' + st.i + '/post.json'); st.i++;
    if (!pr.ok) throw new Error('post yok');
    const post = await pr.json();
    const paras = (post.caption || '').split(/\n\s*\n/).map(x => x.trim()).filter(x => x && !/^(🆕|#|Kaydırarak|Kaynaklarıyla|Bilgilendirme)/.test(x) && !/profil/i.test(x));
    let cap = ''; for (const x of paras) if ((cap + '\n\n' + x).length < 860) cap += (cap ? '\n\n' : '') + x;
    const esc = x => x.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    const c = '📚 Arşivden\n\n' + esc(cap) + `\n\n<a href="https://bitkitabani.com/${post.id}/">Devamı ve kaynaklar: bitkitabani.com</a>`;
    const tk = String(env.TG_TOKEN).trim().replace(/^bot/i, '').replace(/\s+/g, '');
    const img = (post.images || [])[0];
    const r = await fetch('https://api.telegram.org/bot' + tk + (img ? '/sendPhoto' : '/sendMessage'), { method: 'POST', headers: { 'content-type': 'application/json' },
      body: JSON.stringify(img ? { chat_id: env.TG_CHAT, photo: img, caption: c, parse_mode: 'HTML' } : { chat_id: env.TG_CHAT, text: c, parse_mode: 'HTML' }) });
    const j = await r.json(); if (!j.ok) throw new Error(j.description || 'telegram');
    st.n = (st.n || 0) + 1; st.error = null;
  } catch (e) { st.error = String(e.message || e).slice(0, 200); st.errorAt = new Date().toISOString(); }
  await call(env, 'tg:arsiv', 'put', st); return st;
}
// Telegram ek paylaşımlar: Threads planındaki gün içi metinler (kavram 08:30, bilgi 12:30, rehber/tarif 17:30, halk bilgisi 21:40).
async function tgEk(env) {
  const day = trDay(), h = trH();
  const SL = [['kavram', 8.5], ['sabah', 12.5], ['ogle', 17.5], ['soru', 21.7]];
  const st = (await call(env, 'tg:ek', 'get')) || {};
  const job = SL.find(([k, t]) => h >= t && h < t + 2.5 && st[k] !== day);
  if (!job) return { skipped: 'sırası değil' };
  st[job[0]] = day;
  try {
    const pr = await igAsset('threads.json'); if (!pr.ok) throw new Error('threads.json yok');
    const plan = ((await pr.json())[day] || {})[job[0]]; if (!plan || !plan.text) throw new Error('metin yok');
    const esc = x => x.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    let t = esc(plan.text.replace(/\n*(#\S+\s*)+$/u, '').trim()).replace(/(bitkitabani\.com\/[\w\-\/]*)/g, '<a href="https://$1">$1</a>');
    const tk = String(env.TG_TOKEN).trim().replace(/^bot/i, '').replace(/\s+/g, '');
    const foto = plan.image && t.length < 1000;
    const r = await fetch('https://api.telegram.org/bot' + tk + (foto ? '/sendPhoto' : '/sendMessage'), { method: 'POST', headers: { 'content-type': 'application/json' },
      body: JSON.stringify(foto ? { chat_id: env.TG_CHAT, photo: plan.image, caption: t, parse_mode: 'HTML' } : { chat_id: env.TG_CHAT, text: t, parse_mode: 'HTML', link_preview_options: { is_disabled: false } }) });
    const j = await r.json(); if (!j.ok) throw new Error(j.description || 'telegram');
    st.n = (st.n || 0) + 1; st.error = null;
  } catch (e) { st.error = job[0] + ': ' + String(e.message || e).slice(0, 200); st.errorAt = new Date().toISOString(); }
  await call(env, 'tg:ek', 'put', st); return st;
}
async function bskyPost(env, zorla) {
  const st = (await call(env, 'bsky:state', 'get')) || {}; const day = trDay();
  if (!zorla && (st.last === day || trH() < 20.7)) return { skipped: 'sırası değil' };
  const X = 'https://bsky.social/xrpc/';
  try {
    const g = await gunlukPost(env, zorla); if (!g) return { skipped: 'bugün post yok' };
    const ses = await (await fetch(X + 'com.atproto.server.createSession', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ identifier: env.BSKY_HANDLE, password: env.BSKY_PASSWORD }) })).json();
    if (!ses.accessJwt) throw new Error('giriş: ' + (ses.message || 'başarısız'));
    const H = { authorization: 'Bearer ' + ses.accessJwt };
    const link = 'bitkitabani.com/' + g.id + '/';
    let t = g.paras[0] || ''; const room = 290 - link.length - 2;
    if ([...t].length > room) t = [...t].slice(0, room - 1).join('').replace(/\s+\S*$/, '') + '…';
    const text = t + '\n\n' + link, enc = new TextEncoder(), start = enc.encode(t + '\n\n').length;
    const rec = { $type: 'app.bsky.feed.post', text, createdAt: new Date().toISOString(), langs: ['tr'],
      facets: [{ index: { byteStart: start, byteEnd: start + enc.encode(link).length }, features: [{ $type: 'app.bsky.richtext.facet#link', uri: g.url }] }] };
    if (g.image) {
      const img = await fetch(g.image); const buf = await img.arrayBuffer();
      if (buf.byteLength < 950000) {
        const up = await (await fetch(X + 'com.atproto.repo.uploadBlob', { method: 'POST', headers: { ...H, 'content-type': img.headers.get('content-type') || 'image/jpeg' }, body: buf })).json();
        if (up.blob) rec.embed = { $type: 'app.bsky.embed.images', images: [{ image: up.blob, alt: g.alt.slice(0, 900) }] };
      }
    }
    const r = await (await fetch(X + 'com.atproto.repo.createRecord', { method: 'POST', headers: { ...H, 'content-type': 'application/json' }, body: JSON.stringify({ repo: ses.did, collection: 'app.bsky.feed.post', record: rec }) })).json();
    if (!r.uri) throw new Error(r.message || 'bluesky');
    if (!zorla) st.last = day; st.plant = g.id; st.n = (st.n || 0) + 1; st.error = null;
  } catch (e) { st.error = String(e.message || e).slice(0, 200); st.errorAt = new Date().toISOString(); if (!zorla) st.last = day; }
  await call(env, 'bsky:state', 'put', st); return st;
}
// ---------- İstatistik: Instagram ve Threads gönderilerinin erişim/kaydetme/paylaşım sayıları ----------
// Günde bir kez: 10:00'da Instagram, 11:00'de Threads (istek sınırına takılmamak için ayrı saatlerde). Sonuç /api/istatistik sayfasında.
async function istCron(env) {
  const day = trDay(), h = trH();
  const ist = (await call(env, 'ist:state', 'get')) || { ig: {}, th: {} };
  const ilk = s => String(s || '').split('\n').map(x => x.trim()).find(Boolean) || '';
  if (h >= 10 && ist.igGun !== day) {
    ist.igGun = day;
    try {
      const ig = (await call(env, 'ig:state', 'get')) || {}; const tok = ig.token; if (!tok || !ig.uid) throw new Error('Instagram anahtarı yok');
      const q = '&access_token=' + encodeURIComponent(tok);
      const prof = await igJson(await fetch(IG + '/' + ig.uid + '?fields=followers_count,media_count' + q));
      const L = (await igJson(await fetch(IG + '/' + ig.uid + '/media?fields=id,caption,media_type,media_product_type,timestamp,permalink,like_count,comments_count&limit=20' + q))).data || [];
      const posts = [];
      for (const m of L) {
        const met = m.media_product_type === 'REELS' ? 'reach,saved,shares,views,total_interactions' : 'reach,saved,shares,views,total_interactions';
        let v = {};
        try { for (const x of (await igJson(await fetch(IG + '/' + m.id + '/insights?metric=' + met + q))).data || []) v[x.name] = (x.values && x.values[0] && x.values[0].value) ?? x.total_value?.value ?? 0; }
        catch (e) { v.hata = String(e.message || e).slice(0, 120); }
        posts.push({ id: m.id, t: m.timestamp, tur: m.media_product_type === 'REELS' ? 'Reel' : m.media_type === 'CAROUSEL_ALBUM' ? 'Kaydırmalı' : 'Görsel', baslik: ilk(m.caption).slice(0, 90), link: m.permalink, begeni: m.like_count || 0, yorum: m.comments_count || 0, ...v });
      }
      ist.ig = { takipci: prof.followers_count, gonderi: prof.media_count, posts, hata: null };
      ist.igTakip = (ist.igTakip || []).filter(x => x[0] !== day).concat([[day, prof.followers_count]]).slice(-90);
    } catch (e) { ist.ig = { ...(ist.ig || {}), hata: String(e.message || e).slice(0, 200) }; }
    await call(env, 'ist:state', 'put', ist); return;
  }
  if (h >= 11 && ist.thGun !== day) {
    ist.thGun = day;
    try {
      const th = (await call(env, 'th:state', 'get')) || {}; const tok = th.token; if (!tok) throw new Error('Threads anahtarı yok');
      const q = '&access_token=' + encodeURIComponent(tok);
      let takipci = null;
      try { const u = await igJson(await fetch(TH + '/me/threads_insights?metric=followers_count' + q)); takipci = ((u.data || [])[0] || {}).total_value?.value ?? null; } catch (e) {}
      const L = (await igJson(await fetch(TH + '/me/threads?fields=id,text,timestamp,permalink,media_type&limit=25' + q))).data || [];
      const posts = [];
      for (const m of L) {
        let v = {};
        try { for (const x of (await igJson(await fetch(TH + '/' + m.id + '/insights?metric=views,likes,replies,reposts,quotes,shares' + q))).data || []) v[x.name] = (x.values && x.values[0] && x.values[0].value) ?? x.total_value?.value ?? 0; }
        catch (e) { v.hata = String(e.message || e).slice(0, 120); }
        posts.push({ id: m.id, t: m.timestamp, baslik: ilk(m.text).slice(0, 90), link: m.permalink, ...v });
      }
      ist.th = { takipci, posts, hata: null };
      if (takipci != null) ist.thTakip = (ist.thTakip || []).filter(x => x[0] !== day).concat([[day, takipci]]).slice(-90);
    } catch (e) { ist.th = { ...(ist.th || {}), hata: String(e.message || e).slice(0, 200) }; }
    await call(env, 'ist:state', 'put', ist);
  }
}
function istSayfa(ist) {
  const e = s => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  const n = x => (x == null || x === '' ? '–' : Number(x).toLocaleString('tr-TR'));
  const tarih = t => t ? new Date(new Date(t).getTime() + 3 * 3600e3).toISOString().slice(5, 16).replace('T', ' ') : '';
  const degisim = L => { if (!L || L.length < 2) return ''; const a = L[Math.max(0, L.length - 8)][1], b = L[L.length - 1][1]; const d = b - a; return ` <small>(${d >= 0 ? '+' : ''}${d} son 7 gün)</small>`; };
  const ig = ist.ig || {}, th = ist.th || {};
  const igP = (ig.posts || []).slice(), thP = (th.posts || []).slice();
  const igSkor = p => (p.saved || 0) * 3 + (p.shares || 0) * 3 + (p.yorum || 0) * 2 + (p.begeni || 0);
  const enIyi = igP.slice().sort((a, b) => igSkor(b) - igSkor(a))[0];
  const thEn = thP.slice().sort((a, b) => (b.views || 0) - (a.views || 0))[0];
  const ort = (L, k) => L.length ? Math.round(L.reduce((s, p) => s + (p[k] || 0), 0) / L.length) : 0;
  const turOrt = {}; for (const p of igP) { (turOrt[p.tur] = turOrt[p.tur] || []).push(p); }
  const igSat = igP.map(p => `<tr><td>${tarih(p.t)}</td><td>${e(p.tur)}</td><td><a href="${e(p.link)}" target="_blank" rel="noopener">${e(p.baslik) || '(başlıksız)'}</a>${p.hata ? `<br><small class=h>${e(p.hata)}</small>` : ''}</td><td>${n(p.reach)}</td><td>${n(p.views)}</td><td>${n(p.begeni)}</td><td>${n(p.yorum)}</td><td><b>${n(p.saved)}</b></td><td><b>${n(p.shares)}</b></td></tr>`).join('');
  const thSat = thP.map(p => `<tr><td>${tarih(p.t)}</td><td><a href="${e(p.link)}" target="_blank" rel="noopener">${e(p.baslik) || '(görsel)'}</a>${p.hata ? `<br><small class=h>${e(p.hata)}</small>` : ''}</td><td><b>${n(p.views)}</b></td><td>${n(p.likes)}</td><td>${n(p.replies)}</td><td>${n(p.reposts)}</td><td>${n(p.shares)}</td></tr>`).join('');
  return `<!doctype html><html lang=tr><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><meta name=robots content=noindex><title>İstatistik · Bitki Tabanı</title>
<style>:root{--bg:#faf7f2;--fg:#2b2a26;--mut:#776f63;--ac:#a5543a;--ln:#e6dfd4;--card:#fff}@media(prefers-color-scheme:dark){:root{--bg:#1c1b19;--fg:#ece6dc;--mut:#a59d90;--ac:#e08a6a;--ln:#38352f;--card:#252320}}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,-apple-system,sans-serif;padding:16px;max-width:1000px;margin:auto}h1{font-size:22px;margin:4px 0 2px}h2{font-size:18px;margin:28px 0 8px}.mut{color:var(--mut)}a{color:var(--ac)}
.k{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:14px 0}.k div{background:var(--card);border:1px solid var(--ln);border-radius:10px;padding:10px 12px}.k b{display:block;font-size:22px}
.tw{overflow-x:auto;border:1px solid var(--ln);border-radius:10px;background:var(--card)}table{border-collapse:collapse;width:100%;font-size:13.5px}td,th{padding:7px 9px;border-bottom:1px solid var(--ln);text-align:left;vertical-align:top}th{position:sticky;top:0;background:var(--card);font-weight:600;white-space:nowrap}td:nth-child(n+4){text-align:right;white-space:nowrap}.h{color:#c0392b}.not{background:var(--card);border-left:3px solid var(--ac);padding:8px 12px;border-radius:6px;margin:10px 0}</style></head><body>
<h1>İstatistik</h1><div class=mut>Her gün 10:00 (Instagram) ve 11:00 (Threads) güncellenir. Son 20 Instagram, 25 Threads gönderisi. Kaydetme ve paylaşım en değerli sinyallerdir.</div>
<div class=k><div>Instagram takipçi<b>${n(ig.takipci)}</b>${degisim(ist.igTakip)}</div><div>Threads takipçi<b>${n(th.takipci)}</b>${degisim(ist.thTakip)}</div>
${Object.entries(turOrt).map(([t, L]) => `<div>${e(t)} ort. erişim<b>${n(ort(L, 'reach'))}</b><small class=mut>${L.length} gönderi</small></div>`).join('')}<div>Threads ort. görüntülenme<b>${n(ort(thP, 'views'))}</b></div></div>
${enIyi ? `<div class=not>Instagram'da en çok etkileşim alan: <a href="${e(enIyi.link)}" target=_blank>${e(enIyi.baslik)}</a> · ${n(enIyi.saved)} kaydetme, ${n(enIyi.shares)} paylaşım</div>` : ''}
${thEn ? `<div class=not>Threads'te en çok görülen: <a href="${e(thEn.link)}" target=_blank>${e(thEn.baslik)}</a> · ${n(thEn.views)} görüntülenme</div>` : ''}
<h2>Instagram</h2>${ig.hata ? `<p class=h>Hata: ${e(ig.hata)}</p>` : ''}<div class=tw><table><tr><th>Tarih</th><th>Tür</th><th>Gönderi</th><th>Erişim</th><th>İzlenme</th><th>Beğeni</th><th>Yorum</th><th>Kaydetme</th><th>Paylaşım</th></tr>${igSat || '<tr><td colspan=9 class=mut>Henüz veri yok.</td></tr>'}</table></div>
<h2>Threads</h2>${th.hata ? `<p class=h>Hata: ${e(th.hata)}</p>` : ''}<div class=tw><table><tr><th>Tarih</th><th>Gönderi</th><th>Görüntülenme</th><th>Beğeni</th><th>Yanıt</th><th>Yeniden paylaşım</th><th>Paylaşım</th></tr>${thSat || '<tr><td colspan=7 class=mut>Henüz veri yok.</td></tr>'}</table></div>
<p class=mut><small>Son güncelleme: Instagram ${e(ist.igGun || '–')}, Threads ${e(ist.thGun || '–')}</small></p></body></html>`;
}

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (url.pathname.startsWith('/ig/')) return igAsset(url.pathname.slice(4));
    if (!url.pathname.startsWith('/api/')) return env.ASSETS.fetch(req);
    if (url.pathname === '/api/ig-durum' && req.method === 'GET') {
      const st = (await call(env, 'ig:state', 'get')) || {};
      const th = (await call(env, 'th:state', 'get')) || {};
      const fb = (await call(env, 'fb:state', 'get')) || {};
      const AL = (await call(env, 'abone:list', 'get')) || {}; const bs = (await call(env, 'bulten:state', 'get')) || {};
      return json({ facebook: { token: !!env.FB_TOKEN, sayfa: fb.pageName || null, oglen: (fb.slot || {}).oglen || null, aksam: (fb.slot || {}).aksam || null, sayi: fb.n || 0, son: fb.last || null, bitki: fb.plant || null, hata: fb.error || null, hataZamani: fb.errorAt || null }, bulten: { anahtar: !!(env.RESEND_KEY || env.RESEND_Key), onayli: Object.values(AL).filter(a => a.on).length, kursta: Object.values(AL).filter(a => a.on && typeof a.kurs === 'number' && a.kurs < 7).length, bekleyen: Object.values(AL).filter(a => !a.on).length, duyuru: Object.values(AL).filter(a => a.on && a.d).length, gonderilen: bs.sayi || 0, hata: bs.err || Object.values(AL).map(a => a.err).find(Boolean) || null }, threads: { token: !!(env.TH_TOKEN || env.TH_Token || th.token), sayi: th.n || 0, son: th.last || null, kavram: (th.slot || {}).kavram || null, sabah: (th.slot || {}).sabah || null, ogle: (th.slot || {}).ogle || null, bitki: th.plant || null, hata: th.error || null, hataZamani: th.errorAt || null }, token: !!(env.IG_TOKEN || st.token), sayi: st.n || 0, reels: st.reels || 0, reelHata: st.reelError || null, hikayeHata: st.storyError || null, altMetin: !st.noAlt, aylik: st.aylik || null, ek: st.ek || null, ekSayi: st.ekSayi || 0, ekHata: st.ekError || null, aylikHata: st.aylikError || null, sonPaylasim: st.last || null, bitki: st.lastPlant || null, hata: st.error || null, hataZamani: st.errorAt || null, tokenYenilendi: st.tokenAt ? new Date(st.tokenAt).toISOString() : null, bugun: trDay() });
    }
    if (url.pathname === '/api/ara' && req.method === 'GET') return araApi(req, env, url);
    if (url.pathname.startsWith('/api/q/') && req.method === 'GET') {   // QR kart okutması: say ve bitki sayfasına yönlendir
      const id = url.pathname.slice(7).replace(/[^a-z0-9]/g, '').slice(0, 40);
      const k = (url.searchParams.get('k') || '').replace(/[^a-z0-9-]/g, '').slice(0, 40);
      try { const q = (await call(env, 'qr:sayac', 'get')) || {}; q[id] = (q[id] || 0) + 1; q._toplam = (q._toplam || 0) + 1; if (k) q['k:' + k] = (q['k:' + k] || 0) + 1; await call(env, 'qr:sayac', 'put', q); } catch (e) {}
      return Response.redirect(url.origin + '/' + id + '/?utm_source=qr' + (k ? '&utm_campaign=' + k : ''), 302);
    }
    if (url.pathname === '/api/qr-durum' && req.method === 'GET') return json((await call(env, 'qr:sayac', 'get')) || {});
    if (url.pathname.startsWith('/api/abone/') && (req.method === 'GET' || url.pathname === '/api/abone/cik')) return aboneApi(req, env, url);
    if (req.method !== 'GET' && req.headers.get('x-bt') !== '1') return json({ error: 'csrf' }, 403);
    if (url.pathname === '/api/abone') return aboneApi(req, env, url);
    if (url.pathname.startsWith('/api/katki')) return katkiApi(req, env, url);
    if (url.pathname === '/api/istatistik' || url.pathname === '/api/istatistik-yenile') {
      const s = await session(req, env);
      if (!s || !s.admin) return json({ error: s ? 'yetki' : 'giriş yok', not: 'bitkitabani.com/hesap/ sayfasından giriş yap' }, s ? 403 : 401);
      if (url.pathname === '/api/istatistik-yenile') { const ist = (await call(env, 'ist:state', 'get')) || {}; const k = url.searchParams.get('k') === 'th' ? 'thGun' : 'igGun'; ist[k] = null; if (k === 'thGun') ist.igGun = trDay(); await call(env, 'ist:state', 'put', ist); await istCron(env); return Response.redirect(url.origin + '/api/istatistik', 302); }
      return new Response(istSayfa((await call(env, 'ist:state', 'get')) || {}), { headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store', 'x-robots-tag': 'noindex' } });
    }
    try {
      if (url.pathname === '/api/login' && req.method === 'POST') {
        if (!env.GOOGLE_CLIENT_ID) return json({ error: 'kapalı' }, 503);
        const { credential } = await req.json();
        const sub = await verifyGoogle(String(credential || ''), env.GOOGLE_CLIENT_ID);
        const sid = btoa(String.fromCharCode(...crypto.getRandomValues(new Uint8Array(32)))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=/g, '');
        const gc = googleClaims(String(credential || ''));
        const admin = !!(gc.email_verified && (await sha256hex(String(gc.email || '').toLowerCase())) === ADMIN_SHA);
        const em = String(gc.email || ''), ep = em.slice(0, 2) + '…@' + em.split('@')[1];
        await call(env, 'sess:' + sid, 'put', { sub, admin, ep, exp: Date.now() + SESSION_DAYS * 864e5 });
        const data = (await call(env, 'user:' + sub, 'get')) || merge();
        return json({ ok: true, data }, 200, { 'set-cookie': setCookie(sid, SESSION_DAYS * 86400) });
      }
      const s = await session(req, env);
      if (!s) return json({ error: 'giriş yok' }, 401);
      const uname = 'user:' + s.sub;
      if (url.pathname === '/api/me' && req.method === 'GET') return json({ ok: true, data: (await call(env, uname, 'get')) || merge() });
      if (url.pathname === '/api/me' && req.method === 'PUT') {
        const body = await req.text(); if (body.length > 200000) return json({ error: 'büyük' }, 413);
        const incoming = clean(JSON.parse(body));
        const merged = url.searchParams.get('merge') ? merge(await call(env, uname, 'get'), incoming)
          : { ...merge(await call(env, uname, 'get'), incoming), learned: incoming.learned }; // öğrenilenlerden çıkarma da eşitlensin
        await call(env, uname, 'put', merged);
        return json({ ok: true, data: merged });
      }
      if (url.pathname === '/api/logout' && req.method === 'POST') {
        await call(env, 'sess:' + s.sid, 'del');
        return json({ ok: true }, 200, { 'set-cookie': setCookie('x'.repeat(20), 0) });
      }
      if (url.pathname === '/api/me' && req.method === 'DELETE') {
        await call(env, uname, 'del'); await call(env, 'sess:' + s.sid, 'del');
        return json({ ok: true }, 200, { 'set-cookie': setCookie('x'.repeat(20), 0) });
      }
      return json({ error: 'yok' }, 404);
    } catch (e) {
      return json({ error: 'hata' }, 400);
    }
  },
  async scheduled(event, env, ctx) {
    if (env.IG_TOKEN) ctx.waitUntil(igPost(env).then(() => (env.TH_TOKEN || env.TH_Token) ? thPost(env) : null).then(() => aylikPost(env)).then(() => ekPost(env)));
    ctx.waitUntil(bultenCron(env).catch(() => null));
    ctx.waitUntil(thYanitlar(env).catch(() => null));
    if (env.TG_TOKEN) ctx.waitUntil(bildirim(env).catch(() => null));
    ctx.waitUntil(istCron(env).catch(() => null));
    if (env.FB_TOKEN) ctx.waitUntil(fbPost(env).catch(() => null));
    if (env.TG_TOKEN && env.TG_CHAT) ctx.waitUntil(tgPost(env).catch(() => null).then(() => tgEk(env)).catch(() => null).then(() => tgArsiv(env)).catch(() => null));
    if (env.BSKY_HANDLE && env.BSKY_PASSWORD) ctx.waitUntil(bskyPost(env).catch(() => null));
  },
};
