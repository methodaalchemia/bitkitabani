/* Bitki fotoğrafları: Wikidata + Wikimedia Commons.
   Yalnızca gerçek fotoğraflar seçilir (JPEG/WebP); çizim, botanik levha, herbaryum örneği, harita ve diyagramlar elenir.
   Fotoğrafçı ve lisans her bitki sayfasında gösterilir. */
(function(){
  var V = 'img3:';
  var BAD = /illustrat|drawing|k[öo]e?hler|medizinal-pflanzen|botanical (art|plate|print)|\bplate\b|tafel|lithograph|engraving|woodcut|painting|watercolou?r|herbari|exsiccat|\bmaps?\b|distribution|diagram|molecule|chemical structure|stamp|coin|logo|bottle|drink|beverage|cup of|powder|capsule|svg/i;
  function g(k){ try{ var v = localStorage.getItem(V + k); return v ? JSON.parse(v) : null; }catch(e){ return null; } }
  function s(k,v){ try{ localStorage.setItem(V + k, JSON.stringify(v)); }catch(e){} }
  function strip(h){ var d = document.createElement('div'); d.innerHTML = h || ''; return (d.textContent || '').replace(/\s+/g,' ').trim(); }
  function j(url){ return fetch(url).then(function(r){ if(!r.ok) throw 0; return r.json(); }); }
  var WD = 'https://www.wikidata.org/w/api.php?format=json&origin=*&';
  var CM = 'https://commons.wikimedia.org/w/api.php?format=json&origin=*&';
  var II = 'prop=imageinfo&iiprop=url|mime|extmetadata&iiextmetadatafilter=Categories|ImageDescription|ObjectName|Artist|LicenseShortName&iiurlwidth=';

  function ok(page){
    var ii = page && page.imageinfo && page.imageinfo[0]; if (!ii) return false;
    if (!/^image\/(jpeg|webp)$/.test(ii.mime || '')) return false;
    var m = ii.extmetadata || {};
    var text = [page.title, m.Categories && m.Categories.value, m.ObjectName && m.ObjectName.value, strip(m.ImageDescription && m.ImageDescription.value)].join(' ');
    return !BAD.test(text);
  }
  function pack(page){
    var ii = page.imageinfo[0], m = ii.extmetadata || {};
    return { src: ii.thumburl || ii.url, file: page.title.replace(/^File:/,''),
      artist: strip(m.Artist && m.Artist.value).slice(0, 120), lic: strip(m.LicenseShortName && m.LicenseShortName.value) };
  }
  function fromWikidata(taxon, w){
    return j(WD + 'action=query&list=search&srlimit=1&srsearch=' + encodeURIComponent('haswbstatement:"P225=' + taxon + '"'))
      .then(function(r){
        var q = r.query && r.query.search && r.query.search[0] && r.query.search[0].title; if (!q) return null;
        return j(WD + 'action=wbgetclaims&property=P18&entity=' + q).then(function(c){
          var files = ((c.claims && c.claims.P18) || []).map(function(x){ return x.mainsnak && x.mainsnak.datavalue && x.mainsnak.datavalue.value; }).filter(Boolean);
          if (!files.length) return null;
          return j(CM + 'action=query&' + II + w + '&titles=' + encodeURIComponent(files.map(function(f){ return 'File:' + f; }).join('|'))).then(function(r2){
            var pages = r2.query && r2.query.pages || {};
            var list = Object.keys(pages).map(function(k){ return pages[k]; });
            for (var i = 0; i < list.length; i++) if (ok(list[i])) return pack(list[i]);
            return null;
          });
        });
      });
  }
  function fromCommons(taxon, w){
    var q = '"' + taxon + '" filetype:bitmap -illustration -drawing -herbarium -plate -map';
    return j(CM + 'action=query&generator=search&gsrnamespace=6&gsrlimit=15&gsrsearch=' + encodeURIComponent(q) + '&' + II + w)
      .then(function(r){
        var pages = r.query && r.query.pages || {};
        var list = Object.keys(pages).map(function(k){ return pages[k]; }).sort(function(a,b){ return (a.index||0) - (b.index||0); });
        for (var i = 0; i < list.length; i++) if (ok(list[i])) return pack(list[i]);
        return null;
      });
  }
  function find(taxon, w){
    var key = taxon + '@' + w, c = g(key);
    if (c !== null) return Promise.resolve(c);
    return fromWikidata(taxon, w).catch(function(){ return null; })
      .then(function(r){ return r || fromCommons(taxon, w).catch(function(){ return null; }); })
      .then(function(r){ s(key, r || false); return r; });
  }
  function esc(t){ return String(t).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }

  function load(el){
    var taxon = el.getAttribute('data-taxon'); if (!taxon) return;
    var w = el.getAttribute('data-size') || '500';
    find(taxon, w).then(function(info){
      if (!info) return;
      var img = document.createElement('img');
      img.alt = el.getAttribute('data-alt') || taxon;
      img.decoding = 'async';
      img.onload = function(){ img.classList.add('on'); el.classList.add('loaded'); };
      img.src = info.src;
      el.appendChild(img);
      var cap = document.getElementById(el.getAttribute('data-caption') || '');
      if (cap) {
        var page = 'https://commons.wikimedia.org/wiki/File:' + encodeURIComponent(info.file.replace(/ /g,'_'));
        var parts = [info.artist, info.lic].filter(Boolean).map(esc);
        cap.innerHTML = 'Fotoğraf: ' + (parts.length ? parts.join(' · ') + ' · ' : '') + '<a href="' + page + '" target="_blank" rel="noopener">Wikimedia Commons</a>';
      }
    });
  }
  var els = Array.prototype.slice.call(document.querySelectorAll('.ph[data-taxon]'));
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting) { io.unobserve(e.target); load(e.target); } }); }, { rootMargin: '300px' });
    els.forEach(function(el){ io.observe(el); });
  } else { els.forEach(load); }
})();
