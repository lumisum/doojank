(() => {
  // Keep local previews out of the public site's statistics.
  if (location.hostname !== 'lumisum.github.io') return;
  const status = document.getElementById('visitor-status');
  const script = document.createElement('script');
  script.src = 'https://cdn.busuanzi.cc/busuanzi/3.6.9/busuanzi.min.js';
  script.defer = true;
  const showUnavailable = () => {
    if (status) status.textContent = document.documentElement.lang === 'en' ? 'Statistics are temporarily unavailable.' : '统计暂未连接，稍后再来看看。';
  };
  script.addEventListener('error', showUnavailable);
  document.head.appendChild(script);
  if (!status) return;
  const count = document.getElementById('busuanzi_site_uv');
  const observer = new MutationObserver(() => {
    if (/^\d[\d,]*$/.test(count.textContent.trim())) {
      status.textContent = document.documentElement.lang === 'en' ? 'Thank you for visiting.' : '感谢每一位来访的朋友。';
      observer.disconnect();
      clearTimeout(timeout);
    }
  });
  observer.observe(count, { childList: true, characterData: true, subtree: true });
  const timeout = setTimeout(showUnavailable, 12000);
})();
