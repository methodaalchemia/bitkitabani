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
  return { sid, sub: s.sub };
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
async function igJson(r) { const j = await r.json().catch(() => ({})); if (!r.ok || j.error) throw new Error((j.error && j.error.message) || ('HTTP ' + r.status)); return j; }
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
  const day = trDay(), hour = trHour(), n = st.n || 0;
  const launching = n < LAUNCH;
  if (st.pauseUntil && Date.now() < st.pauseUntil) return { skipped: 'istek sınırı; bekleniyor' };
  if (launching) {
    if (hour < 9 || hour >= 23) return { skipped: 'gece' };
    if (st.lastAt && Date.now() - st.lastAt < 28 * 60e3) return { skipped: 'yarım saat dolmadı' };
  } else {
    if (hour < 19 || st.last === day) return { skipped: 'bugün sırası değil' };
  }
  try {
    const pr = await igAsset('p/' + n + '/post.json');
    if (!pr.ok) throw new Error(n + '. post bulunamadı; gece derlemesi bekleniyor');
    const post = await pr.json();
    const tok = await igToken(env, st);
    if (!st.uid) st.uid = (await igJson(await fetch(IG + '/me?fields=user_id,username&access_token=' + encodeURIComponent(tok)))).user_id;
    // Aynı post zaten çıkmış mı? (Önceki denemede paylaşım olup yanıt hata dönmüş olabilir.)
    const head = (post.caption || '').split('\n').find(x => x.trim()) || '';
    const recent = await igJson(await fetch(IG + '/me/media?fields=id,caption&limit=5&access_token=' + encodeURIComponent(tok)));
    const dup = (recent.data || []).find(m => (m.caption || '').split('\n').find(x => x.trim()) === head);
    if (dup) {
      st.n = n + 1; st.last = day; st.lastAt = Date.now(); st.lastId = dup.id; st.lastPlant = post.id; st.error = null; st.errorAt = null;
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
    // Günlük postlarda: hikâye (takipçilere duyuru) ve deneme Reels (önce takip etmeyenlere gösterilir)
    if (!launching && post.story) {
      try {
        const sid = (await igJson(await fetch(IG + '/' + st.uid + '/media', form({ media_type: 'STORIES', image_url: post.story })))).id;
        await igJson(await fetch(IG + '/' + st.uid + '/media_publish', form({ creation_id: sid }))); st.storyError = null;
      } catch (e) { st.storyError = String(e.message || e).slice(0, 200); }
    }
    if (!launching && post.reel) {
      try {
        const rid = (await igJson(await fetch(IG + '/' + st.uid + '/media', form({ media_type: 'REELS', video_url: post.reel, caption: post.caption, trial_params: JSON.stringify({ graduation_strategy: 'SS_PERFORMANCE' }) })))).id;
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
export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (url.pathname.startsWith('/ig/')) return igAsset(url.pathname.slice(4));
    if (!url.pathname.startsWith('/api/')) return env.ASSETS.fetch(req);
    if (url.pathname === '/api/ig-durum' && req.method === 'GET') {
      const st = (await call(env, 'ig:state', 'get')) || {};
      return json({ token: !!(env.IG_TOKEN || st.token), sayi: st.n || 0, reels: st.reels || 0, reelHata: st.reelError || null, hikayeHata: st.storyError || null, altMetin: !st.noAlt, sonPaylasim: st.last || null, bitki: st.lastPlant || null, hata: st.error || null, hataZamani: st.errorAt || null, tokenYenilendi: st.tokenAt ? new Date(st.tokenAt).toISOString() : null, bugun: trDay() });
    }
    if (req.method !== 'GET' && req.headers.get('x-bt') !== '1') return json({ error: 'csrf' }, 403);
    try {
      if (url.pathname === '/api/login' && req.method === 'POST') {
        if (!env.GOOGLE_CLIENT_ID) return json({ error: 'kapalı' }, 503);
        const { credential } = await req.json();
        const sub = await verifyGoogle(String(credential || ''), env.GOOGLE_CLIENT_ID);
        const sid = btoa(String.fromCharCode(...crypto.getRandomValues(new Uint8Array(32)))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=/g, '');
        await call(env, 'sess:' + sid, 'put', { sub, exp: Date.now() + SESSION_DAYS * 864e5 });
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
    if (env.IG_TOKEN) ctx.waitUntil(igPost(env));
  },
};
