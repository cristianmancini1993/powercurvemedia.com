(function () {
  const end = Date.now() + 15 * 60 * 1000;
  function tick() {
    const diff = Math.max(0, end - Date.now());
    const h = Math.floor(diff / 3600000);
    const m = Math.floor((diff % 3600000) / 60000);
    const s = Math.floor((diff % 60000) / 1000);
    const hEl = document.getElementById('cd-h');
    const mEl = document.getElementById('cd-m');
    const sEl = document.getElementById('cd-s');
    if (hEl) hEl.textContent = String(h).padStart(2, '0');
    if (mEl) mEl.textContent = String(m).padStart(2, '0');
    if (sEl) sEl.textContent = String(s).padStart(2, '0');
    if (diff > 0) setTimeout(tick, 1000);
  }
  tick();
})();

(function () {
  let count = 41;
  const el = document.getElementById('liveCount');
  if (!el) return;
  const tpl = '<strong>{n} ľudí</strong> si práve prezerá Breezon';
  setInterval(function () {
    count += (Math.random() > 0.5 ? 1 : -1) * Math.ceil(Math.random() * 2);
    count = Math.min(52, Math.max(34, count));
    el.innerHTML = tpl.replace('{n}', String(count));
  }, 2000);
})();

document.querySelectorAll('.faq-item').forEach(function (item) {
  var btn = item.querySelector('.faq-q');
  if (!btn) return;
  btn.addEventListener('click', function () {
    var isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item.open').forEach(function (i) {
      i.classList.remove('open');
    });
    if (!isOpen) item.classList.add('open');
  });
});
