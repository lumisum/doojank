/* A quiet chapter index follows the headings already present in each essay. */
(() => {
  const index = document.querySelector('.article-toc');
  const chapters = document.querySelectorAll('.article-content h2');
  if (!index || chapters.length < 3) return;
  const list = index.querySelector('ol');
  chapters.forEach((chapter, position) => {
    if (!chapter.id) chapter.id = `chapter-${position + 1}`;
    const item = document.createElement('li');
    const link = document.createElement('a');
    link.href = `#${encodeURIComponent(chapter.id)}`;
    link.textContent = chapter.textContent;
    item.append(link);
    list.append(item);
  });
  const count = index.querySelector('.toc-count');
  if (count) count.textContent = `${chapters.length} ${document.documentElement.lang === 'en' ? 'sections' : '节'}`;
  index.hidden = false;
})();
