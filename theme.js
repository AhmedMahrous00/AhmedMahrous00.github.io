(() => {
  'use strict';
  const key = 'amahrous-theme';
  const media = window.matchMedia('(prefers-color-scheme: dark)');
  const valid = value => ['light', 'dark', 'system'].includes(value);
  let preference = 'system';
  try {
    const stored = localStorage.getItem(key);
    if (valid(stored)) preference = stored;
  } catch (_) { /* Theme selection also works when storage is unavailable. */ }
  const apply = () => {
    document.documentElement.dataset.theme = preference === 'system'
      ? (media.matches ? 'dark' : 'light') : preference;
    const control = document.getElementById('theme-choice');
    if (control) control.value = preference;
  };
  apply();
  if (media.addEventListener) media.addEventListener('change', apply);
  else if (media.addListener) media.addListener(apply);
  window.addEventListener('storage', event => {
    if (event.key === key || event.key === null) {
      preference = valid(event.newValue) ? event.newValue : 'system';
      apply();
    }
  });
  document.addEventListener('DOMContentLoaded', () => {
    const control = document.getElementById('theme-choice');
    if (!control) return;
    control.value = preference;
    control.addEventListener('change', () => {
      preference = valid(control.value) ? control.value : 'system';
      try { localStorage.setItem(key, preference); } catch (_) {}
      apply();
    });
    document.querySelector('.theme-toolbar').hidden = false;
  });
})();
