/* Long articles retain their full text and offer a compact chapter index. */
(() => {
  const index = document.querySelector('.article-toc');
  const chapters = document.querySelectorAll('.article-content h2');
  if (!index || !chapters.length) return;
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
  index.hidden = false;
})();
