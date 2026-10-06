(() => {
  const themeButton = document.querySelector('.blog-theme-toggle');
  const applyTheme = theme => {
    const dark = theme === 'dark';
    document.documentElement.dataset.blogTheme = dark ? 'dark' : 'light';
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.content = dark ? '#09111f' : '#f5f5f7';
    if (themeButton) {
      const en = document.documentElement.lang === 'en';
      const label = en ? (dark ? 'Switch to light theme' : 'Switch to dark theme')
        : (dark ? '切换为亮色主题' : '切换为暗色主题');
      themeButton.setAttribute('aria-pressed', String(dark));
      themeButton.setAttribute('aria-label', label);
      themeButton.title = label;
    }
  };
  if (themeButton) {
    applyTheme(document.documentElement.dataset.blogTheme);
    themeButton.hidden = false;
    themeButton.addEventListener('click', () => {
      const theme = document.documentElement.dataset.blogTheme === 'dark' ? 'light' : 'dark';
      applyTheme(theme);
      try { localStorage.setItem('wulai-blog-theme-apple-v1', theme); } catch (_) {}
    });
    addEventListener('storage', event => {
      if (event.key === 'wulai-blog-theme-apple-v1') applyTheme(event.newValue);
    });
  }
  const tools = document.querySelector('.archive-tools');
  if (tools) {
    tools.hidden = false;
    const input = document.getElementById('essay-search');
    const cards = Array.from(document.querySelectorAll('.exhibit-card'));
    const counter = document.getElementById('search-count');
    const empty = document.querySelector('.search-empty');
    const en = document.documentElement.lang === 'en';
    input.addEventListener('input', () => {
      const terms = input.value.normalize('NFKC').toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
      let count = 0;
      cards.forEach(card => {
        const text = card.dataset.search.normalize('NFKC').toLocaleLowerCase();
        card.hidden = !terms.every(term => text.includes(term));
        if (!card.hidden) count++;
      });
      counter.textContent = terms.length ? `${count} ${en ? 'essays' : '篇文章'}` : '';
      empty.hidden = count !== 0;
    });
  }
  const bar = document.querySelector('.reading-progress span');
  const article = document.querySelector('.article-content');
  if (bar && article) {
    let pending = false;
    const update = () => {
      const rect = article.getBoundingClientRect();
      const distance = Math.max(1, rect.height - innerHeight * .4);
      const progress = Math.max(0, Math.min(1, (innerHeight * .25 - rect.top) / distance));
      bar.style.transform = `scaleX(${progress})`;
      pending = false;
    };
    const queue = () => { if (!pending) { pending = true; requestAnimationFrame(update); } };
    addEventListener('scroll', queue, {passive:true});
    addEventListener('resize', queue);
    addEventListener('load', queue);
    update();
  }
  // Small pointer-driven depth; touch and reduced-motion users keep a static surface.
  if (matchMedia('(hover: hover) and (pointer: fine)').matches && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('.exhibit-card, .orbit-book').forEach(card => {
      let frame = 0;
      let x = .5, y = .5;
      const paint = () => {
        card.style.setProperty('--rx', `${(0.5 - y) * 3}deg`);
        card.style.setProperty('--ry', `${(x - 0.5) * 4}deg`);
        card.style.setProperty('--px', `${x * 100}%`);
        card.style.setProperty('--py', `${y * 100}%`);
        frame = 0;
      };
      card.addEventListener('pointermove', event => {
        const rect = card.getBoundingClientRect();
        x = (event.clientX - rect.left) / rect.width;
        y = (event.clientY - rect.top) / rect.height;
        if (!frame) frame = requestAnimationFrame(paint);
      });
      card.addEventListener('pointerleave', () => {
        if (frame) cancelAnimationFrame(frame);
        frame = 0;
        card.style.setProperty('--rx', '0deg');
        card.style.setProperty('--ry', '0deg');
        card.style.setProperty('--px', '50%');
        card.style.setProperty('--py', '50%');
      });
    });
  }
})();
