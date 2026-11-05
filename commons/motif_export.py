# -*- coding: utf-8 -*-
import importlib.util, math, random as _rnd, html, json, os, re
spec = importlib.util.spec_from_file_location('motifler', '/home/claude/bitkitabani/motifler.py')
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)

def e(s): return html.escape(str(s), quote=True)

def motif_paths(mo):
    r = _rnd.Random(mo['slug'])
    def wob(pts, amp):
        out = []
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            n = max(2, int(math.hypot(x1 - x0, y1 - y0) / 3))
            for k in range(n):
                t = k / n
                out.append((x0 + (x1 - x0) * t + r.uniform(-amp, amp), y0 + (y1 - y0) * t + r.uniform(-amp, amp)))
        out.append((pts[-1][0] + r.uniform(-amp, amp), pts[-1][1] + r.uniform(-amp, amp)))
        return out
    def path(pts):
        if len(pts) < 2: return ''
        d = f'M{pts[0][0]:.1f} {pts[0][1]:.1f}'
        for (ax, ay), (bx, by) in zip(pts[1:], pts[2:] + [pts[-1]]):
            d += f' Q{ax:.1f} {ay:.1f} {(ax + bx) / 2:.1f} {(ay + by) / 2:.1f}'
        return d
    INK = '#1b1b1b'
    body = ''.join(f'<path d="{path(wob(p, .45))}" fill="{INK}" stroke="none" opacity=".9"/>' for p in mo.get('dolu', []))
    body += ''.join(f'<path d="{path(wob(p, .55))}"/>' for p in mo['cizim'])
    body += ''.join(f'<path d="{path(wob(p, .9))}" stroke-width="1.1" opacity=".55"/>' for p in mo['cizim'])
    return body, INK

def svg_for(mo):
    body, INK = motif_paths(mo)
    ad = mo['ad']
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 -4 108 108" width="512" height="512" '
            f'fill="none" stroke="{INK}" stroke-width="3.3" stroke-linecap="round" stroke-linejoin="round" '
            f'role="img" aria-labelledby="t d">'
            f'<title id="t">{e(ad)} motifi</title>'
            f'<desc id="d">{e(mo["kisa"])} Çizim: Edanaz Tınmazlar, Bitki Tabanı (bitkitabani.com). CC BY-SA 4.0.</desc>'
            f'{body}</svg>\n')

def dosya_adi(mo):
    ad = mo['ad'].replace('/', '-').strip()
    return f'{ad} motifi - Bitki Tabani cizimi.svg'

rows = []
for mo in M.MOTIFLER:
    fn = dosya_adi(mo)
    open(os.path.join('/home/claude/commons/svg', fn), 'w', encoding='utf-8').write(svg_for(mo))
    rows.append({'slug': mo['slug'], 'ad': mo['ad'], 'dosya': fn, 'bolge': mo['bolge'],
                 'tema': M.TEMALAR.get(mo['tema'], mo['tema']), 'kisa': mo['kisa'],
                 'kaynaklar': [k[0] for k in mo.get('kaynaklar', [])]})
json.dump(rows, open('/home/claude/commons/motifler.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('üretilen SVG:', len(rows))
