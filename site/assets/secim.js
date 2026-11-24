/* Fotoğraf seçim sayfası: her bitki için 6 aday; seçimler bu tarayıcıda saklanır ve liste olarak kopyalanır. */
(function(){
  var KEY = 'bt-secim';
  var picks = {};
  try{ picks = JSON.parse(localStorage.getItem(KEY) || '{}'); }catch(e){}
  function save(){ try{ localStorage.setItem(KEY, JSON.stringify(picks)); }catch(e){} out(); }
  var rows = Array.prototype.slice.call(document.querySelectorAll('.pick-row'));
  function out(){
    var lines = rows.map(function(r){ var id = r.dataset.id; return picks[id] ? id + ' | ' + picks[id] : null; }).filter(Boolean);
    document.getElementById('result').value = lines.join('\n');
    document.getElementById('done').textContent = lines.length + ' / ' + rows.length + ' bitki seçildi';
  }
  function fill(row){
    var grid = row.querySelector('.cands'), id = row.dataset.id;
    BTPhoto.candidates(row.dataset.taxon, 500, 6).then(function(list){
      list = list.slice(0, 6);
      grid.innerHTML = '';
      if (!list.length) { grid.innerHTML = '<p class="muted">Uygun fotoğraf bulunamadı. Bu bitki için bana bir fotoğraf bağlantısı gönderebilirsin.</p>'; return; }
      list.forEach(function(info){
        var b = document.createElement('button');
        b.type = 'button'; b.className = 'cand'; b.setAttribute('aria-pressed', picks[id] === info.file ? 'true' : 'false');
        b.title = info.file;
        var ph = document.createElement('div'); ph.className = 'ph'; b.appendChild(ph);
        BTPhoto.show(ph, info);
        b.addEventListener('click', function(){
          picks[id] = info.file; save();
          grid.querySelectorAll('.cand').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        });
        grid.appendChild(b);
      });
    });
  }
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting) { io.unobserve(e.target); fill(e.target); } }); }, { rootMargin: '600px' });
    rows.forEach(function(r){ io.observe(r); });
  } else rows.forEach(fill);
  document.getElementById('copy').addEventListener('click', function(){
    var t = document.getElementById('result');
    var msg = document.getElementById('copied');
    if (navigator.clipboard) navigator.clipboard.writeText(t.value).then(function(){ msg.textContent = 'Kopyalandı'; }, function(){ t.select(); msg.textContent = 'Metni seçtim, kopyalayabilirsin'; });
    else { t.select(); msg.textContent = 'Metni seçtim, kopyalayabilirsin'; }
  });
  out();
})();
