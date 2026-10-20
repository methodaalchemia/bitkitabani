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

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (!url.pathname.startsWith('/api/')) return env.ASSETS.fetch(req);
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
};
