(() => {
  const dialog = document.getElementById('qr-dialog');
  if (!dialog) return;
  const image = document.getElementById('qr-dialog-image');
  const title = document.getElementById('qr-dialog-title');
  document.querySelectorAll('[data-qr-src]').forEach(button => {
    button.addEventListener('click', () => {
      image.src = button.dataset.qrSrc;
      image.alt = button.dataset.qrTitle + (document.documentElement.lang === 'en' ? ' QR code' : '二维码');
      title.textContent = button.dataset.qrTitle;
      if (typeof dialog.showModal === 'function') dialog.showModal();
      else window.open(image.src, '_blank', 'noopener');
    });
  });
  dialog.querySelector('.qr-dialog-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const box = dialog.getBoundingClientRect();
    if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) dialog.close();
  });
})();
