/* Wikimedia Commons fotoğraflarını yükler; yazar ve lisansı gösterir. */
(function(){
  function getCache(k){ try{ var v = sessionStorage.getItem(k); return v ? JSON.parse(v) : null; }catch(e){ return null; } }
  function setCache(k,v){ try{ sessionStorage.setItem(k, JSON.stringify(v)); }catch(e){} }
  function strip(html){ var d = document.createElement('div'); d.innerHTML = html || ''; return (d.textContent || '').replace(/\s+/g,' ').trim(); }

  function summary(title){
    var key = 'wk:' + title, c = getCache(key);
    if (c) return Promise.resolve(c);
    return fetch('https://en.wikipedia.org/api/rest_v1/page/summary/' + encodeURIComponent(title))
      .then(function(r){ if(!r.ok) throw 0; return r.json(); })
      .then(function(j){
        var src = (j.originalimage && j.originalimage.source) || '';
        var th = (j.thumbnail && j.thumbnail.source) || '';
        var out = { thumb: th, orig: src, file: src && src.indexOf('/wikipedia/commons/') > -1 ? decodeURIComponent(src.split('/').pop()) : '' };
        setCache(key, out); return out;
      });
  }
  function sized(info, w){
    if (info.thumb && info.thumb.indexOf('/thumb/') > -1) return info.thumb.replace(/\/\d+px-/, '/' + w + 'px-');
    return info.thumb || info.orig;
  }
  function credit(file){
    var key = 'cm:' + file, c = getCache(key);
    if (c) return Promise.resolve(c);
    var url = 'https://commons.wikimedia.org/w/api.php?action=query&format=json&origin=*&prop=imageinfo&iiprop=extmetadata&titles=' + encodeURIComponent('File:' + file);
    return fetch(url).then(function(r){ return r.json(); }).then(function(j){
      var pages = j.query && j.query.pages, p = pages && pages[Object.keys(pages)[0]];
      var m = p && p.imageinfo && p.imageinfo[0] && p.imageinfo[0].extmetadata || {};
      var out = { artist: strip(m.Artist && m.Artist.value), lic: strip(m.LicenseShortName && m.LicenseShortName.value) };
      setCache(key, out); return out;
    });
  }
  function load(el){
    var title = el.getAttribute('data-wiki'); if (!title) return;
    var w = el.getAttribute('data-size') || '500';
    summary(title).then(function(info){
      if (!info.file) return; // yalnızca Commons'taki özgür lisanslı görseller
      var img = document.createElement('img');
      img.alt = el.getAttribute('data-alt') || '';
      img.decoding = 'async';
      img.onload = function(){ img.classList.add('on'); el.classList.add('loaded'); };
      img.onerror = function(){ if (img.src !== info.thumb && info.thumb) img.src = info.thumb; };
      img.src = sized(info, w);
      el.appendChild(img);
      var capId = el.getAttribute('data-caption');
      var cap = capId && document.getElementById(capId);
      if (cap) {
        var page = 'https://commons.wikimedia.org/wiki/File:' + encodeURIComponent(info.file.replace(/ /g,'_'));
        cap.innerHTML = 'Fotoğraf: <a href="' + page + '" target="_blank" rel="noopener">Wikimedia Commons</a>';
        credit(info.file).then(function(c){
          var parts = [];
          if (c.artist) parts.push(c.artist.replace(/[<>]/g,''));
          if (c.lic) parts.push(c.lic.replace(/[<>]/g,''));
          cap.innerHTML = 'Fotoğraf: ' + (parts.length ? parts.join(' · ') + ' · ' : '') + '<a href="' + page + '" target="_blank" rel="noopener">Wikimedia Commons</a>';
        }).catch(function(){});
      }
    }).catch(function(){});
  }
  var els = Array.prototype.slice.call(document.querySelectorAll('.ph[data-wiki]'));
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if (e.isIntersecting) { io.unobserve(e.target); load(e.target); } });
    }, { rootMargin: '300px' });
    els.forEach(function(el){ io.observe(el); });
  } else { els.forEach(load); }
})();
