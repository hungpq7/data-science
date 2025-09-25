// _static/open-all-content-links.js
window.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('main a[href]:not([href^="#"])').forEach(a => {
    a.setAttribute('target', '_blank');
    a.setAttribute('rel', 'noopener noreferrer');
  });
});