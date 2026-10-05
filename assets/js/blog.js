(() => {
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
})();
