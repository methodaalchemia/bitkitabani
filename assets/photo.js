/* Bitki fotoğrafları: Wikimedia Commons.
   Sıra: 1) elle seçilmiş dosya (data-file), 2) Commons "Quality images" yakın çekimleri,
   3) Wikidata'daki tür fotoğrafı, 4) genel Commons araması.
   Yalnızca gerçek fotoğraflar (JPEG/WebP); çizim, levha, herbaryum, harita vb. elenir. */
(function(){
  var V = 'img4:';
  var BAD = /illustrat|drawing|k[öo]e?hler|medizinal-pflanzen|botanical (art|plate|print)|\bplate\b|tafel|lithograph|engraving|woodcut|painting|watercolou?r|herbari|exsiccat|\bmaps?\b|distribution|diagram|molecule|chemical structure|stamp|coin|logo|bottle|drink|beverage|cup of|powder|capsule|svg|landscape|panorama|habitat|forest|market/i;
  function g(k){ try{ var v = localStorage.getItem(V + k); return v ? JSON.parse(v) : null; }catch(e){ return null; } }
  function s(k,v){ try{ localStorage.setItem(V + k, JSON.stringify(v)); }catch(e){} }
  function strip(h){ var d = document.createElement('div'); d.innerHTML = h || ''; return (d.textContent || '').replace(/\s+/g,' ').trim(); }
  function j(url){ return fetch(url).then(function(r){ if(!r.ok) throw 0; return r.json(); }); }
  var WD = 'https://www.wikidata.org/w/api.php?format=json&origin=*&';
  var CM = 'https://commons.wikimedia.org/w/api.php?format=json&origin=*&';
  function II(w){ return 'prop=imageinfo&iiprop=url|mime|size|extmetadata&iiextmetadatafilter=Categories|ImageDescription|ObjectName|Artist|LicenseShortName&iiurlwidth=' + w; }

  function ok(page){
    var ii = page && page.imageinfo && page.imageinfo[0]; if (!ii) return false;
    if (!/^image\/(jpeg|webp)$/.test(ii.mime || '')) return false;
    if (ii.width && ii.width < 800) return false;
    var m = ii.extmetadata || {};
    var text = [page.title, m.Categories && m.Categories.value, m.ObjectName && m.ObjectName.value, strip(m.ImageDescription && m.ImageDescription.value)].join(' ');
    return !BAD.test(text);
  }
  function pack(page){
    var ii = page.imageinfo[0], m = ii.extmetadata || {};
    return { src: ii.thumburl || ii.url, file: page.title.replace(/^File:/,''),
      artist: strip(m.Artist && m.Artist.value).slice(0, 120), lic: strip(m.LicenseShortName && m.LicenseShortName.value) };
  }
  function pagesOf(r){
    var p = r.query && r.query.pages || {};
    return Object.keys(p).map(function(k){ return p[k]; }).sort(function(a,b){ return (a.index||0) - (b.index||0); });
  }
  function search(q, w, n){
    return j(CM + 'action=query&generator=search&gsrnamespace=6&gsrlimit=' + (n || 20) + '&gsrsearch=' + encodeURIComponent(q) + '&' + II(w))
      .then(function(r){ return pagesOf(r).filter(ok).map(pack); }).catch(function(){ return []; });
  }
  function byFiles(files, w){
    return j(CM + 'action=query&' + II(w) + '&titles=' + encodeURIComponent(files.map(function(f){ return 'File:' + f; }).join('|')))
      .then(function(r){ return pagesOf(r).filter(function(p){ return p.imageinfo; }).map(pack); }).catch(function(){ return []; });
  }
  function wikidata(taxon, w){
    return j(WD + 'action=query&list=search&srlimit=1&srsearch=' + encodeURIComponent('haswbstatement:"P225=' + taxon + '"'))
      .then(function(r){
        var q = r.query && r.query.search && r.query.search[0] && r.query.search[0].title; if (!q) return [];
        return j(WD + 'action=wbgetclaims&property=P18&entity=' + q).then(function(c){
          var files = ((c.claims && c.claims.P18) || []).map(function(x){ return x.mainsnak && x.mainsnak.datavalue && x.mainsnak.datavalue.value; }).filter(Boolean);
          if (!files.length) return [];
          return j(CM + 'action=query&' + II(w) + '&titles=' + encodeURIComponent(files.map(function(f){ return 'File:' + f; }).join('|')))
            .then(function(r2){ return pagesOf(r2).filter(ok).map(pack); });
        });
      }).catch(function(){ return []; });
  }
  /* Aday listesi: önce kaliteli yakın çekimler */
  function candidates(taxon, w, n){
    var q = '"' + taxon + '"';
    return search(q + ' incategory:Quality_images', w, 20).then(function(a){
      if (a.length >= n) return a;
      return wikidata(taxon, w).then(function(b){
        return search(q + ' filetype:bitmap -illustration -drawing -herbarium', w, 25).then(function(c){
          var seen = {}, out = [];
          a.concat(b, c).forEach(function(x){ if (!seen[x.file]) { seen[x.file] = 1; out.push(x); } });
          return out;
        });
      });
    });
  }
  function best(taxon, file, w){
    var key = (file || taxon) + '@' + w, c = g(key);
    if (c !== null) return Promise.resolve(c);
    var p = file ? byFiles([file], w).then(function(a){ return a[0] || null; })
                 : candidates(taxon, w, 1).then(function(a){ return a[0] || null; });
    return p.then(function(r){ s(key, r || false); return r; });
  }
  function esc(t){ return String(t).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
  function commonsPage(file){ return 'https://commons.wikimedia.org/wiki/File:' + encodeURIComponent(file.replace(/ /g,'_')); }
  function credit(info){
    var parts = [info.artist, info.lic].filter(Boolean).map(esc);
    return 'Fotoğraf: ' + (parts.length ? parts.join(' · ') + ' · ' : '') + '<a href="' + commonsPage(info.file) + '" target="_blank" rel="noopener">Wikimedia Commons</a>';
  }
  function show(el, info){
    var img = document.createElement('img');
    img.alt = el.getAttribute('data-alt') || '';
    img.decoding = 'async';
    img.onload = function(){ img.classList.add('on'); el.classList.add('loaded'); };
    img.src = info.src;
    el.appendChild(img);
  }
  function load(el){
    var taxon = el.getAttribute('data-taxon'); if (!taxon) return;
    best(taxon, el.getAttribute('data-file'), el.getAttribute('data-size') || '500').then(function(info){
      if (!info) return;
      show(el, info);
      var cap = document.getElementById(el.getAttribute('data-caption') || '');
      if (cap) cap.innerHTML = credit(info);
    });
  }
  window.BTPhoto = { candidates: candidates, show: show, credit: credit };
  var els = Array.prototype.slice.call(document.querySelectorAll('.ph[data-taxon]'));
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting) { io.unobserve(e.target); load(e.target); } }); }, { rootMargin: '300px' });
    els.forEach(function(el){ io.observe(el); });
  } else { els.forEach(load); }
})();
