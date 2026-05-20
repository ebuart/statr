// SPA router + view switching
const App = (() => {
  const VIEWS = ['view-path', 'view-session', 'view-complete'];

  function showView(name) {
    VIEWS.forEach(id => {
      const el = document.getElementById(id);
      if (!el) return;
      if (id === `view-${name}`) {
        el.classList.add('active');
      } else {
        el.classList.remove('active');
      }
    });
  }

  function _init() {
    // Back button
    document.getElementById('btn-back-path')?.addEventListener('click', () => {
      showView('path');
      Path.load();
    });

    // Next chapter button on complete screen
    document.getElementById('btn-next-chapter')?.addEventListener('click', async () => {
      const r = await fetch('/api/path');
      const data = await r.json();
      showView('path');
      Path.load();
    });

    // Keyboard: Escape → back to path
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') {
        const session = document.getElementById('view-session');
        if (session && session.classList.contains('active')) {
          showView('path');
          Path.load();
        }
      }
    });

    // Load initial path
    Path.load();
  }

  // Boot on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', _init);
  } else {
    _init();
  }

  return { showView };
})();
