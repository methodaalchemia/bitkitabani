"""English edition of Bitki Tabanı (/en/). Called at the end of build.py with build.py's globals."""
import json, os, re, importlib

def run(G):
    e, short_la, IMG, BASE, OUT, write = G['e'], G['short_la'], G['IMG'], G['BASE'], G['OUT'], G['write']
    P, BR, REG, EK, ETK, DERIN, EXTRA = G['P'], G['BR'], G['REG'], G['EK'], G['ETK'], G['DERIN'], G['D'].get('EXTRA', {})
    YASAL, KORUMA = G['YASAL'], G['KORUMA']
    EMA, NCCIH, OTHER, POWO, BAYTOP = G['EMA'], G['NCCIH'], G['OTHER'], G['POWO'], G['BAYTOP']
    slug_of, bridge_map, pips, acc, dot = G['slug_of'], G['bridge_map'], G['pips'], G['acc'], G['dot']
    FAV, FONTS, CONTENT_DATE, AUTHOR = G['FAV'], G['FONTS'], G['CONTENT_DATE'], G['AUTHOR']
    import sys; sys.path.insert(0, os.path.join(G['HERE'], 'en'))
    EN = {}
    for n in range(1, 9):
        EN.update(importlib.import_module(f'p{n}').EN)
    from etk_en import ETK_EN
    from derin_en import D_EN
    from misc_en import ALT_EN, KORUMA_EN, YASAL_EN, YASAL_AD_EN, BR_EN, REG_EN, KAT_EN, KANIT_EN, GUV_EN, KAN_AD_EN, BIO_EN
    missing = [p['id'] for p in P if p['id'] not in EN]
    assert not missing, ('missing English entries', missing)
    byId = {p['id']: p for p in P}
    name = lambda p: EN[p['id']]['name']
    PAIRS = {}   # en path -> tr path

    def head(title, desc, path, tr_path, extra='', image=None):
        url = BASE + path; image = image or BASE + '/img/kantaron-960.jpg'
        PAIRS[path] = tr_path
        return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{url}">
<link rel="alternate" hreflang="tr" href="{BASE}{tr_path}">
<link rel="alternate" hreflang="x-default" href="{BASE}{tr_path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Bitki Tabanı">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="en_GB">
<meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{image}">
<meta name="theme-color" content="#A3271B">
{FAV}
{FONTS}
<link rel="stylesheet" href="/assets/style.css">
{extra}
</head>
<body>
<div class="wrap{{narrow}}">
'''
    def nav(cur, tr_path):
        a = lambda href, label, key: f'<a href="{href}"{" aria-current=\"page\"" if cur == key else ""}>{label}</a>'
        return f'''<div class="motif" aria-hidden="true"></div><div class="site-nav"><a class="logo" href="/en/">Bitki <em>Tabanı</em></a><nav>{a("/en/catalog/", "Catalog", "kat")}{a("/en/bridges/", "Culture bridges", "br")}{a("/en/about/", "About", "about")}<a href="{tr_path}" lang="tr" hreflang="tr">Türkçe</a></nav></div>'''
    FOOT = '''<div class="motif indigo" aria-hidden="true"></div>
<footer class="site">
  <div>
    <h3>About this site</h3>
    <p>A compilation made for knowledge and curiosity; it is not medical advice. Before using any plant, especially if you take medicines, are pregnant or breastfeeding, talk to a doctor or pharmacist.</p>
    <p>Photos are from Wikimedia Commons under free licences; the author and licence are given on each plant’s page.</p>
    <p><a href="/en/about/">About and method</a> · <a href="/">Türkçe</a> · <a href="mailto:iletisim@bitkitabani.com">Contact</a></p>
  </div>
  <div class="legend">
    <h3>Evidence level</h3>
    <div><span class="pips"><i class="on"></i><i class="on"></i><i class="on"></i></span> Clinical: controlled trials or an approved medicine</div>
    <div><span class="pips"><i class="on"></i><i class="on"></i><i></i></span> Limited: small or few human studies</div>
    <div><span class="pips"><i class="on"></i><i></i><i></i></span> Traditional: no or very few human studies</div>
  </div>
  <div class="legend">
    <h3>Safety</h3>
    <div><span class="sf dusuk">Generally safe</span> in moderate use</div>
    <div><span class="sf orta">Caution</span> interaction or dose risks</div>
    <div><span class="sf yuksek">High risk</span> poisonous or serious side effects</div>
    <div><span class="lg yasak">Illegal in Türkiye</span> shown with a separate label</div>
  </div>
</footer>
</div>
'''
    def page(title, desc, path, tr_path, body, cur, scripts='', narrow=False, extra='', image=None):
        h = head(title, desc, path, tr_path, extra, image).replace('{narrow}', ' narrow' if narrow else '')
        return h + nav(cur, tr_path) + body + FOOT + scripts + '\n</body>\n</html>\n'

    def ph(p, size, eager=False):
        m = IMG.get(p['id'])
        if not m: return f'<div class="ph"><span class="ph-mark">{e(short_la(p))}</span></div>'
        w, h = (m['w'], m['h']) if size == 960 else (m.get('w500', 500), m.get('h500', 667))
        load = 'fetchpriority="high"' if eager else 'loading="lazy"'
        src = f'<source type="image/webp" srcset="/img/{p["id"]}-{size}.webp">' if os.path.exists(os.path.join(G['HERE'], 'img', f'{p["id"]}-{size}.webp')) else ''
        return f'<div class="ph loaded"><picture>{src}<img src="/img/{p["id"]}-{size}.jpg" width="{w}" height="{h}" alt="{e(name(p))} ({e(short_la(p))}): {e(ALT_EN.get(p["id"], "plant"))}" {load} decoding="async"></picture></div>'
    def credit(p):
        m = IMG.get(p['id'])
        if not m: return ''
        lic = f'<a href="{e(m["licenseUrl"])}" target="_blank" rel="noopener">{e(m["license"])}</a>' if m.get('licenseUrl') else e(m.get('license', ''))
        parts = [x for x in [e(m.get('artist', '')), lic] if x]
        return 'Photo: ' + ' · '.join(parts) + f' · <a href="{e(m["page"])}" target="_blank" rel="noopener">Wikimedia Commons</a>'
    def tags(p):
        out = []
        y = YASAL_EN.get(p['id'])
        if y: out.append(f'<span class="lg {y[0]}">{YASAL_AD_EN[y[0]]}</span>')
        k = KORUMA_EN.get(p['id'])
        if k and k.get('rozet'): out.append(f'<span class="lg koruma">{e(k["rozet"])}</span>')
        return f'<div class="tags">{"".join(out)}</div>' if out else ''
    def card(p):
        x = EN[p['id']]
        s = ' '.join([x['name'], p['la'], x['other'], p['fam'], x['part'], x['prep'], x['science'], x['fact']] + [t for u in x['uses'] for t in u] + [KAT_EN[k] for k in p['kat']])
        durum = ([YASAL[p["id"]][0] if YASAL[p["id"]][0] == "yasak" else "kisitli"] if p["id"] in YASAL else []) + (["koruma"] if KORUMA.get(p["id"], {}).get("rozet") else [])
        return f'''<a class="card" href="/en/{p["id"]}/" data-id="{p["id"]}" data-bolge="{" ".join(p["bolge"])}" data-kat="{" ".join(p["kat"])}" data-kanit="{p["kanit"]}" data-guv="{p["guv"]}" data-durum="{" ".join(durum)}" data-s="{e(s)}">
  {ph(p, 500)}
  <div class="body">
    <div class="row"><span class="acc">{acc(p["no"])}</span><span class="regs">{"".join(dot(r) for r in p["bolge"])}</span></div>
    <h2>{e(x["name"])}</h2>
    <div class="latin">{e(p["la"])}</div>
    <div class="fam" lang="la">{e(p["fam"])}</div>
    {tags(p)}
    <div class="foot"><span class="ev" aria-label="Evidence level: {KANIT_EN[p["kanit"]]}">{pips(p["kanit"])} Evidence: {KANIT_EN[p["kanit"]]}</span><span class="sf {p["guv"]}">{GUV_EN[p["guv"]]}</span></div>
  </div>
</a>'''
    def refs(p):
        pid = p['id']; items = []
        for label, url in EMA.get(pid, []):
            items.append(('EMA monograph', f'{label}: European Medicines Agency herbal assessment', url))
        if pid in NCCIH:
            items.append(('NCCIH', 'US National Center for Complementary and Integrative Health: use and safety summary', f'https://www.nccih.nih.gov/health/{NCCIH[pid]}'))
        for label, url in OTHER.get(pid, []):
            kind = 'Official source' if ('fda.gov' in url or 'unodc.org' in url or 'nobelprize.org' in url) else 'Research'
            items.append((kind, label, url))
        if 'anadolu' in p['bolge'] and any('Anadolu' in w for w, _ in p['kul']):
            items.append(('Book', BAYTOP, ''))
        nm = POWO.get(pid, short_la(p))
        if nm:
            import urllib.parse
            items.append(('Botanical record', f'Kew Plants of the World Online: {nm}', 'https://powo.science.kew.org/results?q=' + urllib.parse.quote(nm)))
        return '<ol class="refs">' + ''.join((f'<li><span class="kind">{e(k)}</span><a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a></li>' if u else f'<li><span class="kind">{e(k)}</span><cite>{e(t)}</cite></li>') for k, t, u in items) + '<li class="muted-s">Titles of research sources are summarised in Turkish on the Turkish page; links open the original English publications.</li></ol>'

    def toc(html):
        items = []
        def sub(m):
            t = m.group(1); sid = re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')
            items.append((sid, t)); return f'<section class="sec" id="{sid}"><h2>{t}</h2>'
        html = re.sub(r'<section class="sec"><h2>([^<]+)</h2>', sub, html)
        nav_ = '<nav class="toc" aria-label="On this page"><span class="eyebrow">On this page</span><ol>' + ''.join(f'<li><a href="#{s}">{t}</a></li>' for s, t in items) + '</ol></nav>'
        return html.replace('<!--TOC-->', nav_)

    def map_en(only=None):
        s = bridge_map(only)
        s = s.replace('Kültür köprüleri haritası: Anadolu, Asya, And Dağları, Amazon ve Kuzey Amerika arasındaki bitki bağlantıları', 'Culture bridges map: plant links between Anatolia, Asia, the Andes, the Amazon and North America')
        for i, b in enumerate(BR, 1):
            s = s.replace(f'href="/kopruler/{slug_of(b)}/" class="num" aria-label="Köprü {i}: {e(b["t"])}"', f'href="/en/bridges/{slug_of(b)}/" class="num" aria-label="Bridge {i}: {e(BR_EN[i-1][0])}"')
        LBL = {'Anadolu: üzerlik':'Anatolia: Syrian rue','Amazon: ayahuasca':'Amazon: ayahuasca','Anadolu: sedef otu':'Anatolia: rue','And: ruda':'Andes: ruda','Köyceğiz: sığla':'Köyceğiz: sweetgum',
               'Ekvador kıyısı: palo santo':'Ecuador coast: palo santo','Anadolu: ısırgan':'Anatolia: nettle','And: ortiga':'Andes: ortiga','Kahramanmaraş: salep':'Kahramanmaraş: salep','Junín platosu: maca':'Junín plateau: maca',
               'Anadolu: banotu':'Anatolia: henbane','Amazon: toé':'Amazon: toé','Toroslar: ardıç':'Taurus: juniper','Kırgızistan: arça':'Kyrgyzstan: arça','Kaliforniya: ak adaçayı':'California: white sage',
               'Kahramanmaraş: Maraş otu':'Kahramanmaraş: Maraş otu','Amazon: mapacho':'Amazon: mapacho','Asya: pelin, artemisinin':'Asia: wormwood, artemisinin','And: kınakına':'Andes: cinchona',
               'Anadolu: kına':'Anatolia: henna','Amazon: huito':'Amazon: huito','Uşak: kök boya':'Uşak: madder','Ekvador: achiote':'Ecuador: achiote','Gümüşhane: kuşburnu':'Gümüşhane: rose hip',
               'Amazon: camu camu':'Amazon: camu camu','Asya: efedra':'Asia: ephedra','And: koka':'Andes: coca','Anadolu: kudret narı':'Anatolia: bitter melon','Amazon: sorosi':'Amazon: sorosi',
               'Kore: ginseng':'Korea: ginseng','Akdeniz: adamotu':'Mediterranean: mandrake','Meksika: peyote':'Mexico: peyote','And: San Pedro':'Andes: San Pedro'}
        for k, v in LBL.items():
            s = s.replace(f'>{e(k)}</text>', f'>{e(v)}</text>')
        return s

    DISC = '<aside class="disclaimer" role="note"><b>Not medical advice.</b> This page describes traditional uses as a cultural record and summarises the science; it is not a diagnosis or treatment recommendation. Before using {n} or any other plant, especially if you take medicines, are pregnant or breastfeeding, or have a health condition, talk to your doctor or pharmacist. If you suspect poisoning, call your local poison centre (in Türkiye, UZEM: <b>114</b>).</aside>'
    DATE_TXT = CONTENT_DATE

    # ---------- plant pages ----------
    bridges_of = {}
    for i, b in enumerate(BR, 1):
        for k in (b['a'], b.get('b')):
            if k: bridges_of.setdefault(k, []).append(i)
    for idx, p in enumerate(P):
        pid = p['id']; x = EN[pid]; ek = EK.get(pid, {})
        prev, nxt = P[idx - 1], P[(idx + 1) % len(P)]
        regs_txt = ', '.join(REG_EN[r] for r in p['bolge'])
        first = lambda t: t.split('. ')[0].rstrip('.') + '.'
        y = YASAL_EN.get(pid)
        qa = [(f'What is {x["name"]}?', f'{x["name"]} ({short_la(p)}) is a plant of the {p["fam"]} family. Traditions that use it: {regs_txt}. Part used: {x["part"].lower()}.'),
              (f'What is {x["name"]} used for?', f'Traditional use: {first(x["uses"][0][1])} Scientific evidence: {KANIT_EN[p["kanit"]].lower()}. {first(x["science"])}'),
              (f'Is {x["name"]} safe?', f'Safety label: {GUV_EN[p["guv"]].lower()}. {x["safety"]}' + (f' Legal status: {YASAL_AD_EN[y[0]]}.' if y else ''))]
        kisa = '<section class="kisaca" aria-label="In short"><span class="eyebrow">In short</span>' + ''.join(f'<div class="qa"><h2 class="q">{e(q)}</h2><p>{e(a)}</p></div>' for q, a in qa) + '</section>'
        uses = ''.join(f'<div class="use"><div class="who">{e(w)}</div><p>{e(t)}</p></div>' for w, t in x['uses'])
        sec = lambda h, inner: f'<section class="sec"><h2>{h}</h2>{inner}</section>'
        body_s = sec('Traditional use', f'<div class="uses">{uses}</div>')
        if ek:
            body_s += sec('In nature', f'<dl class="meta wide"><div><dt>Where it grows</dt><dd>{e(x["habitat"])}</dd></div><div><dt>Harvest season</dt><dd>{e(x["season"])}</dd></div><div><dt>Local names</dt><dd>{e(x["local"])}</dd></div></dl>')
            body_s += sec('Mix-up risk', f'<div class="callout orta"><p>{e(x["confusion"])}</p></div>')
        body_s += sec('Preparation', f'<p>{e(x["prep"])}</p>') + sec('What science says', f'<p>{e(x["science"])}</p>')
        faq = []
        if pid in D_EN:
            dd = D_EN[pid]
            rows = ''.join(f'<tr><th scope="row">{e(i)}</th><td><span class="kv {k}">{KAN_AD_EN[k]}</span></td><td>{e(n)}</td></tr>' for i, k, n in dd['iddia'])
            body_s += sec('How strong is the evidence?', f'<p class="muted-s">Claims often repeated online about {e(x["name"])}, and what science says today.</p><div class="tablewrap"><table class="cmp etk kanit"><thead><tr><th scope="col">Claim</th><th scope="col">Evidence</th><th scope="col">Note</th></tr></thead><tbody>{rows}</tbody></table></div>')
            body_s += sec('Common mistakes', '<ul class="hatalar">' + ''.join(f'<li>{e(h)}</li>' for h in dd['hata']) + '</ul>')
            body_s += sec('Frequently asked', '<div class="faq">' + ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in dd['sss']) + '</div>')
            faq = dd['sss']
        body_s += sec('Safety', f'<div class="callout {p["guv"]}"><div class="lvl">{GUV_EN[p["guv"]]}</div><p>{e(x["safety"])}</p></div>')
        if pid in ETK_EN:
            rows = ''.join(f'<tr><th scope="row">{e(g)}</th><td>{e(w)}</td></tr>' for g, w in ETK_EN[pid])
            body_s += sec('Drug interactions', f'<div class="tablewrap"><table class="cmp etk"><thead><tr><th scope="col">Medicine or substance</th><th scope="col">Why it matters</th></tr></thead><tbody>{rows}</tbody></table></div><p class="muted-s">This list is not complete. If you take regular medication, ask your pharmacist or doctor before trying {e(x["name"])}.</p>')
        if y:
            body_s += sec('Legal status', f'<div class="callout {"yuksek" if y[0] == "yasak" else "orta"}"><div class="lvl">{YASAL_AD_EN[y[0]]}</div><p>{e(y[1])}</p><p class="muted-s">Laws differ by country; check local rules before travelling with or buying any plant product.</p></div>')
        k = KORUMA_EN.get(pid)
        if k:
            rows = ''.join(f'<div><dt>{lab}</dt><dd>{e(v)}</dd></div>' for lab, v in [('IUCN', k.get('iucn')), ('CITES', k.get('cites')), ('Note', k.get('not_')), ('Alternative', k.get('alternatif'))] if v)
            body_s += sec('Conservation', f'<dl class="meta wide">{rows}</dl>')
        if pid in bridges_of:
            body_s += sec('Culture bridge', ''.join(f'<p><b>{e(BR_EN[i-1][0])}.</b> {e(BR_EN[i-1][1])} <a class="cta" href="/en/bridges/{slug_of(BR[i-1])}/">Read the comparison →</a></p>' for i in bridges_of[pid]))
        rel = [byId[r] for r in EXTRA.get(pid, []) if r in byId]
        def sim(q): return 2 * len(set(q['bolge']) & set(p['bolge'])) + len(set(q['kat']) & set(p['kat'])) + (2 if q['fam'] == p['fam'] else 0)
        similar = rel[:1] + sorted((q for q in P if q['id'] != pid and q not in rel), key=lambda q: (-sim(q), q['no']))[:3 - len(rel[:1])]
        body_s += f'<section class="sec"><h2>Similar plants</h2><div class="grid sim">{"".join(card(q) for q in similar)}</div></section>'
        body_s += sec('Sources', refs(p))
        meta = f'''<dl class="meta"><div><dt>Other names</dt><dd>{e(x["other"])}</dd></div><div><dt>Part used</dt><dd>{e(x["part"])}</dd></div><div><dt>Region</dt><dd>{"<br>".join(dot(r) + " " + e(REG_EN[r]) for r in p["bolge"])}</dd></div><div><dt>Use</dt><dd>{", ".join(KAT_EN[c] for c in p["kat"])}</dd></div></dl>'''
        body = f'''
<nav class="crumbs" aria-label="Breadcrumb"><a href="/en/">Home</a><span>/</span><a href="/en/catalog/">Catalog</a><span>/</span><span>{e(x["name"])}</span></nav>
<article class="sheet">
  <header class="sheet-head">
    <div class="titles">
      <span class="eyebrow">{acc(p["no"])} · <span lang="la">{e(p["fam"])}</span></span>
      <h1>{e(x["name"])}</h1>
      <span class="latin">{e(p["la"])}</span>
      <div class="badges"><span class="ev">{pips(p["kanit"])} Evidence: {KANIT_EN[p["kanit"]]}</span><span class="sf {p["guv"]}">{GUV_EN[p["guv"]]}</span>{tags(p).replace('<div class="tags">','').replace('</div>','')}</div>
      <p class="intro">{e(x["fact"])}</p>
      {meta}
    </div>
    <figure class="photo">{ph(p, 960, eager=True)}<figcaption>{credit(p)}</figcaption></figure>
  </header>
  {kisa}
  <!--TOC-->
  {body_s}
  {DISC.format(n=e(x["name"]))}
  <p class="updated">Written by <a href="/en/about/#author">Edanaz Tınmazlar</a> · Last reviewed: <time datetime="{CONTENT_DATE}">{DATE_TXT}</time> · <a href="/{pid}/" lang="tr">Türkçe</a></p>
  <div class="sheet-foot"><div class="pager"><a href="/en/{prev["id"]}/">← {e(EN[prev["id"]]["name"])}</a><a href="/en/{nxt["id"]}/">{e(EN[nxt["id"]]["name"])} →</a></div></div>
</article>
'''
        body = toc(body)
        title = (f'{x["name"]}: what it is, effects and toxicity' if p['guv'] == 'yuksek' else f'{x["name"]}: uses, benefits and side effects')
        if len(title) < 46: title += ' | Bitki Tabanı'
        desc = f'{x["name"]} ({short_la(p)}): {first(x["uses"][0][1])} Evidence: {KANIT_EN[p["kanit"]].lower()}. Safety notes and sources.'
        desc = desc if len(desc) <= 160 else desc[:157].rsplit(' ', 1)[0] + '…'
        ld = [{"@context":"https://schema.org","@type":"Article","headline":f'{x["name"]} ({short_la(p)})',"inLanguage":"en","author":{**AUTHOR, 'url': BASE + '/en/about/#author', 'jobTitle': 'Artist and herbalist'},
               "about":{"@type":"Taxon","name":short_la(p),"alternateName":[x['name'], p['tr']]},"description":desc,"dateModified":CONTENT_DATE,"url":f'{BASE}/en/{pid}/',
               "image":(f'{BASE}/img/{pid}-960.jpg' if pid in IMG else None),"publisher":{"@type":"Organization","name":"Bitki Tabanı","url":BASE+"/"}},
              {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":BASE+"/en/"},{"@type":"ListItem","position":2,"name":"Catalog","item":BASE+"/en/catalog/"},{"@type":"ListItem","position":3,"name":x['name'],"item":f'{BASE}/en/{pid}/'}]},
              {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in qa + list(faq)]}]
        write(f'/en/{pid}/', page(title, desc, f'/en/{pid}/', f'/{pid}/', body, 'plant', narrow=True,
              extra=''.join(f'<script type="application/ld+json">{json.dumps(z, ensure_ascii=False)}</script>' for z in ld), image=(f'{BASE}/img/{pid}-960.jpg' if pid in IMG else None)))

    # ---------- catalog ----------
    cnt = lambda fn: sum(1 for p in P if fn(p))
    regs = [k for k in REG if cnt(lambda p, k=k: k in p['bolge']) >= 3]
    durum = [('yasak', 'Illegal in Türkiye', lambda p: YASAL.get(p['id'], ('',))[0] == 'yasak'),
             ('kisitli', 'Restricted or licensed in Türkiye', lambda p: YASAL.get(p['id'], ('',))[0] in ('kisitli', 'lisansli')),
             ('koruma', 'Needs protection', lambda p: bool(KORUMA.get(p['id'], {}).get('rozet')))]
    groups = [('bolge','Region',[(k,REG_EN[k],dot(k),cnt(lambda p,k=k: k in p['bolge'])) for k in regs]),
              ('kat','Use',[(k,v,'',cnt(lambda p,k=k: k in p['kat'])) for k,v in KAT_EN.items()]),
              ('kanit','Evidence',[(k,v,pips(k),cnt(lambda p,k=k: p['kanit']==k)) for k,v in KANIT_EN.items()]),
              ('guv','Safety',[(k,v,f'<span class="dot" style="background:var(--s-{k})"></span>',cnt(lambda p,k=k: p['guv']==k)) for k,v in GUV_EN.items()]),
              ('durum','Legal and conservation',[(k,v,'',cnt(fn)) for k,v,fn in durum])]
    filters = ''.join(f'<div class="fgroup"><span>{lab}</span><div class="chips">' + ''.join(f'<button type="button" class="chip" data-g="{g}" data-k="{k}" aria-pressed="false">{ic}{e(v)} <span class="n">{n}</span></button>' for k,v,ic,n in opts) + '</div></div>' for g,lab,opts in groups)
    srt = sorted(P, key=lambda p: EN[p['id']]['name'].lower())
    kat = f'''
<nav class="crumbs" aria-label="Breadcrumb"><a href="/en/">Home</a><span>/</span><span>Catalog</span></nav>
<header class="page-head"><span class="eyebrow">{len(P)} entries</span><h1>Plant catalog</h1><p>Filter every plant by region, use, evidence level, safety and legal status. Your filters are written to the address bar, so you can share the link.</p></header>
<section style="display:flex;flex-direction:column;gap:18px" aria-label="Catalog">
  <div class="controls">
    <label class="search" for="q"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" stroke="currentColor" stroke-width="2" fill="none"/><path d="M15.5 15.5L21 21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      <input id="q" type="search" placeholder="Search plants, Latin names, uses… (e.g. evil eye, cough, incense)" autocomplete="off" aria-label="Search plants"></label>
    <div class="fgroups">{filters}</div>
  </div>
  <div class="resultbar"><span id="count" aria-live="polite" data-tpl="Showing {{n}} of {{t}} entries">Showing {len(P)} of {len(P)} entries</span><button class="linkbtn" id="reset" type="button" hidden>Clear filters</button></div>
  <div class="grid">{"".join(card(p) for p in srt)}</div>
  <div class="empty" id="empty" hidden>No plants match these filters. Try removing a filter or a different word.</div>
</section>'''
    ldk = {"@context":"https://schema.org","@type":"CollectionPage","name":"Plant catalog","url":BASE+"/en/catalog/","inLanguage":"en","mainEntity":{"@type":"ItemList","numberOfItems":len(P),"itemListElement":[{"@type":"ListItem","position":i+1,"url":f'{BASE}/en/{p["id"]}/',"name":EN[p['id']]['name']} for i,p in enumerate(srt)]}}
    write('/en/catalog/', page(f'Plant catalog: {len(P)} medicinal and ritual plants | Bitki Tabanı', f'Filter {len(P)} medicinal and ritual plants from Anatolia, Asia, the Andes, the Amazon and North America by region, use, evidence and safety.', '/en/catalog/', '/katalog/', kat, 'kat', '<script src="/assets/catalog.js" defer></script>', extra=f'<script type="application/ld+json">{json.dumps(ldk, ensure_ascii=False)}</script>'))

    # ---------- bridges ----------
    def mini(p):
        return f'<a class="mini" href="/en/{p["id"]}/"><span class="where">{"".join(dot(r) for r in p["bolge"])} {e(" · ".join(REG_EN[r] for r in p["bolge"]))}</span><b>{e(name(p))}</b><span class="latin">{e(p["la"])}</span></a>'
    items = []
    for i, b in enumerate(BR, 1):
        a = byId[b['a']]; c = byId.get(b.get('b')) if b.get('b') else None
        t, d = BR_EN[i-1]
        txt = f'<div class="txt"><h2><span class="bn">{i}</span><a href="/en/bridges/{slug_of(b)}/">{e(t)}</a></h2><p>{e(d)}</p><p><a class="cta" href="/en/bridges/{slug_of(b)}/">Read the comparison →</a></p></div>'
        items.append(f'<article class="bridge" id="kopru-{i}" data-i="{i}" tabindex="-1">{mini(a)}<span class="arrow" aria-hidden="true">↔</span>{mini(c)}{txt}</article>' if c else f'<article class="bridge single" id="kopru-{i}" data-i="{i}" tabindex="-1">{mini(a)}<span class="note">One plant, several cultures</span>{txt}</article>')
    brp = f'''<header class="page-head"><span class="eyebrow">{len(BR)} comparisons</span><h1>Culture bridges</h1><p>Cultures thousands of kilometres apart have often used the same molecules, or the same plant, for similar troubles. Each arc on the map is a bridge; hover over it or pick one from the list below.</p></header>
<figure class="mapwrap">{map_en()}<figcaption>Map: Natural Earth (public domain), Natural Earth projection. Dots show the region, not an exact collection site.</figcaption></figure>
<div class="bridges">{"".join(items)}</div>'''
    write('/en/bridges/', page(f'Culture bridges map: {len(BR)} plant comparisons | Bitki Tabanı', f'{len(BR)} culture bridges between Anatolia, Asia, the Andes, the Amazon and North America: Syrian rue and ayahuasca, ephedra and coca, salep and maca, side by side.', '/en/bridges/', '/kopruler/', brp, 'br', '<script src="/assets/kopruler.js" defer></script>'))
    for i, b in enumerate(BR, 1):
        slug = slug_of(b); a = byId[b['a']]; c = byId.get(b.get('b')) if b.get('b') else None
        ps = [a] + ([c] if c else []); t, d = BR_EN[i-1]
        tn = f'{name(a)} and {name(c)}' if c else name(a)
        yas = lambda q: YASAL_AD_EN[YASAL_EN[q['id']][0]] if q['id'] in YASAL_EN else 'No specific restriction'
        rows = [('Latin name', lambda q: f'<i>{e(q["la"])}</i>'), ('Family', lambda q: e(q['fam'])), ('Region', lambda q: ', '.join(e(REG_EN[r]) for r in q['bolge'])),
                ('Part used', lambda q: e(EN[q['id']]['part'])), ('Use', lambda q: ', '.join(KAT_EN[k] for k in q['kat'])), ('Scientific evidence', lambda q: KANIT_EN[q['kanit']]),
                ('Safety', lambda q: f'<span class="sf {q["guv"]}">{GUV_EN[q["guv"]]}</span>'), ('Legal status in Türkiye', yas)]
        th = '<tr><th scope="col"></th>' + ''.join(f'<th scope="col"><a href="/en/{q["id"]}/">{e(name(q))}</a></th>' for q in ps) + '</tr>'
        tb = ''.join('<tr><th scope="row">' + lab + '</th>' + ''.join(f'<td>{fn(q)}</td>' for q in ps) + '</tr>' for lab, fn in rows)
        blocks = ''.join(f'<section class="sec"><h2>{e(name(q))}</h2><div class="uses">' + ''.join(f'<div class="use"><div class="who">{e(w)}</div><p>{e(tx)}</p></div>' for w, tx in EN[q['id']]['uses']) + f'</div><p><b>Science:</b> {e(EN[q["id"]]["science"])}</p><p><b>Safety:</b> {e(EN[q["id"]]["safety"])}</p><p><a class="cta" href="/en/{q["id"]}/">Full {e(name(q))} page →</a></p></section>' for q in ps)
        others = ''.join(f'<li><a href="/en/bridges/{slug_of(z)}/">{e(BR_EN[j][0])}</a></li>' for j, z in enumerate(BR) if z is not b)
        pv, nx = BR[i-2], BR[i % len(BR)]
        body = f'''
<nav class="crumbs" aria-label="Breadcrumb"><a href="/en/">Home</a><span>/</span><a href="/en/bridges/">Culture bridges</a><span>/</span><span>{e(t)}</span></nav>
<article class="sheet">
<header class="page-head"><span class="eyebrow">Culture bridge {i} · {e(tn)}</span><h1>{e(t)}</h1><p>{e(d)}</p></header>
<figure class="mapwrap">{map_en(only=i)}<figcaption>Map: Natural Earth (public domain). Dots show the region, not an exact collection site.</figcaption></figure>
<section class="sec"><h2>Side by side</h2><div class="tablewrap"><table class="cmp"><thead>{th}</thead><tbody>{tb}</tbody></table></div></section>
{blocks}
{DISC.format(n="these plants")}
<p class="updated">Last reviewed: <time datetime="{CONTENT_DATE}">{DATE_TXT}</time> · <a href="/kopruler/{slug}/" lang="tr">Türkçe</a></p>
<section class="sec"><h2>Other bridges</h2><ul class="otherlist">{others}</ul></section>
<div class="sheet-foot"><a class="cta" href="/en/bridges/">All bridges and the map →</a><div class="pager"><a href="/en/bridges/{slug_of(pv)}/">← {e(BR_EN[BR.index(pv)][0])}</a><a href="/en/bridges/{slug_of(nx)}/">{e(BR_EN[BR.index(nx)][0])} →</a></div></div>
</article>'''
        write(f'/en/bridges/{slug}/', page(f'{t}: {tn} | Bitki Tabanı', (f'{tn}: ' + d)[:157], f'/en/bridges/{slug}/', f'/kopruler/{slug}/', body, 'br', narrow=True, image=(f'{BASE}/img/{a["id"]}-960.jpg' if a['id'] in IMG else None)))

    # ---------- about ----------
    about = f'''<header class="page-head"><span class="eyebrow">About</span><h1>What is Bitki Tabanı?</h1><p>Bitki Tabanı (“plant base” in Turkish) is an independent, non-commercial ethnobotanical record of plants used for healing and ritual across cultures. It aims to spark curiosity and to set traditional knowledge side by side with today’s science. The main edition is in Turkish; this is the English edition.</p></header>
<section class="sec" id="author"><h2>Who writes it</h2><p>{BIO_EN}</p><p><a href="https://www.instagram.com/teda.naz/" rel="me noopener">Instagram</a></p></section>
<section class="sec"><h2>Sources we use</h2><ol class="srclist"><li><b>Official herbal assessments:</b> monographs of the European Medicines Agency’s Committee on Herbal Medicinal Products (EMA/HMPC) and summaries of the US National Center for Complementary and Integrative Health (NCCIH).</li><li><b>Systematic reviews and clinical trials:</b> Cochrane reviews and peer-reviewed journals indexed in PubMed.</li><li><b>Names and classification:</b> Kew’s Plants of the World Online (POWO).</li><li><b>Conservation and trade:</b> the IUCN Red List and CITES.</li><li><b>Legal status:</b> official legislation and UNODC publications.</li><li><b>Traditional use:</b> ethnobotanical field studies and academic books; for Anatolia, Turhan Baytop’s <i>Türkiye’de Bitkiler ile Tedavi</i>.</li></ol><p>Wikipedia, news sites, and pages of herb shops and supplement sellers are not used as sources.</p></section>
<section class="sec"><h2>Evidence levels</h2><dl class="meta wide"><div><dt>Clinical</dt><dd>Controlled human trials or an officially approved medicinal use.</dd></div><div><dt>Limited</dt><dd>Small or few human studies; promising but not conclusive.</dd></div><div><dt>Traditional</dt><dd>Use is culturally documented, but there are no or very few human studies. This does not mean the plant does not work; it means science does not yet know.</dd></div></dl></section>
<section class="sec"><h2>Safety labels</h2><dl class="meta wide"><div><dt>Generally safe</dt><dd>No serious side effects reported with moderate, traditional use.</dd></div><div><dt>Caution</dt><dd>Risk of drug interactions, dosing problems or harm to certain groups (pregnancy, children, chronic illness).</dd></div><div><dt>High risk</dt><dd>Poisonous plants or plants with serious side effects. They are here for their cultural and historical importance, not as a recommendation.</dd></div></dl><p>Legal status is shown separately from safety: a plant can be poisonous without being illegal, and illegal without being poisonous.</p></section>
<section class="sec"><h2>Respect for traditional knowledge</h2><p>Traditional uses are described with the names and context of the communities that keep them alive, using specific names such as Shipibo or Huichol rather than generalisations. Sacred and ceremonial uses are recorded as culture, not as advice.</p></section>
<section class="sec"><h2>Independence</h2><p>Bitki Tabanı sells nothing, carries no ads, uses no affiliate links and takes no money from any company. Corrections are welcome at <a href="mailto:iletisim@bitkitabani.com">iletisim@bitkitabani.com</a>.</p></section>'''
    write('/en/about/', page('About and method | Bitki Tabanı', 'Who writes Bitki Tabanı, which sources it uses, and how evidence levels and safety labels are set.', '/en/about/', '/yontem/', about, 'about', narrow=True))

    # ---------- home ----------
    REG_TXT = {'anadolu': 'Smoke against the evil eye, Anatolian folk healing and plants of the Mediterranean.', 'asya': 'Shamanic smoke of the steppe, Chinese medicine and the roots of Siberia.',
               'and': 'Coca leaf, the San Pedro cactus and cleansing herbs of the high Andes.', 'amazon': 'Ayahuasca, huito body paint and the forest’s teacher plants.', 'kamerika': 'White sage, peyote and the healing plants of the prairies.'}
    regcards = ''.join(f'<a class="regcard" href="/en/catalog/?bolge={k}"><span class="eyebrow">{dot(k)} {e(REG_EN[k])}</span><b>{cnt(lambda p,k=k: k in p["bolge"])} plants</b><span>{REG_TXT[k]}</span></a>' for k in regs)
    FEAT = ['uzerlik','ayahuasca','salep','maca','kantaron','koka','kina','huito','safran','guarana','sigla','peyote']
    home = f'''
<header class="top">
  <div class="brand">
    <span class="eyebrow">Ethnobotanical record</span>
    <h1 class="wordmark">Bitki <em>Tabanı</em></h1>
    <p class="lede">{len(P)} healing and ritual plants from Anatolia, Asia, the Andes, the Amazon and North America. Each entry brings together traditional use, what science says, safety notes and sources.</p>
    <p><a class="cta" href="/en/catalog/">Open the catalog →</a></p>
  </div>
</header>
<section class="sec"><h2>By region</h2><div class="regs-grid">{regcards}</div></section>
<section class="sec"><h2>Featured</h2><div class="grid">{"".join(card(byId[i]) for i in FEAT if i in byId)}</div><p><a class="cta" href="/en/catalog/">See all {len(P)} plants →</a></p></section>
<section class="sec"><h2>Culture bridges</h2><p>Cultures thousands of kilometres apart have often used the same molecules, or the same plant, for similar troubles. See {len(BR)} bridges on the map.</p><div class="mapwrap">{map_en()}</div><p><a class="cta" href="/en/bridges/">See all bridges and comparisons →</a></p></section>'''
    ldw = {"@context":"https://schema.org","@type":"WebSite","name":"Bitki Tabanı","url":BASE+"/en/","inLanguage":"en","description":"A sourced, non-commercial ethnobotanical database of healing and ritual plants across cultures."}
    write('/en/', page('Bitki Tabanı: medicinal and ritual plants across cultures', f'{len(P)} healing and ritual plants from Anatolia, Asia, the Andes, the Amazon and North America: traditional use, scientific evidence, safety and sources.', '/en/', '/', home, 'home', extra=f'<script type="application/ld+json">{json.dumps(ldw, ensure_ascii=False)}</script>'))

    # ---------- hreflang on Turkish pages ----------
    for en_path, tr_path in PAIRS.items():
        f = os.path.join(OUT, tr_path.strip('/'), 'index.html') if tr_path != '/' else os.path.join(OUT, 'index.html')
        if not os.path.exists(f): continue
        h = open(f, encoding='utf-8').read()
        if 'hreflang="en"' in h: continue
        tag = f'<link rel="alternate" hreflang="tr" href="{BASE}{tr_path}">\n<link rel="alternate" hreflang="en" href="{BASE}{en_path}">\n<link rel="alternate" hreflang="x-default" href="{BASE}{tr_path}">\n'
        h = h.replace('<link rel="canonical"', tag + '<link rel="canonical"', 1)
        h = h.replace('{a("/hesap/"', '{a("/hesap/"')
        h = h.replace('<a href="/hesap/">Hesap</a></nav>', f'<a href="/hesap/">Hesap</a><a href="{en_path}" lang="en" hreflang="en">English</a></nav>', 1)
        open(f, 'w', encoding='utf-8').write(h)
    return sorted(PAIRS)
