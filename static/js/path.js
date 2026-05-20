// Path view – renders the chapter path from /api/path
const Path = (() => {

  async function load() {
    const r = await fetch('/api/path');
    const data = await r.json();
    _render(data.chapters, data.current_chapter);
    Progress.refresh();
  }

  function _render(chapters, currentId) {
    const el = document.getElementById('chapter-path');
    if (!el) return;
    el.innerHTML = chapters.map((ch, i) => _card(ch, i, currentId)).join('');

    el.querySelectorAll('.chapter-card[data-cid]').forEach(card => {
      card.addEventListener('click', () => {
        const cid = card.dataset.cid;
        const ch  = chapters.find(c => c.chapter_id === cid);
        if (!ch || ch.coming_soon) return;
        if (!ch.unlocked && !ch.completed) return;
        Session.open(cid);
      });
    });
  }

  function _card(ch, idx, currentId) {
    const priorityDot = {
      high:   '<span class="dot dot-high"></span>',
      medium: '<span class="dot dot-medium"></span>',
      low:    '<span class="dot dot-low"></span>',
    }[ch.priority] || '';

    let stateClass = '';
    let badge = '';
    let locked = false;

    if (ch.coming_soon) {
      stateClass = 'coming-soon';
      badge = '<span class="ch-badge">Bald verfügbar</span>';
      locked = true;
    } else if (ch.completed) {
      stateClass = 'completed';
      badge = `<span class="ch-badge ch-badge-done">✓ ${ch.accuracy != null ? ch.accuracy + '%' : ''}</span>`;
    } else if (!ch.unlocked) {
      stateClass = 'locked';
      badge = '<span class="ch-badge ch-badge-lock">🔒</span>';
      locked = true;
    } else if (ch.chapter_id === currentId) {
      stateClass = 'active';
    }

    const pct = ch.progress_pct || 0;
    const bar = !ch.coming_soon && !locked
      ? `<div class="ch-progress-track"><div class="ch-progress-fill" style="width:${pct}%"></div></div>`
      : '';

    return `
      <div class="chapter-card ${stateClass}" data-cid="${ch.chapter_id}"
           role="button" tabindex="${locked ? -1 : 0}"
           aria-label="${_esc(ch.title)}">
        <div class="ch-header">
          <div class="ch-num-wrap">
            <span class="ch-num">${idx + 1}</span>
            ${priorityDot}
          </div>
          ${badge}
        </div>
        <h3 class="ch-title">${_esc(ch.title)}</h3>
        <p class="ch-desc">${_esc(ch.description)}</p>
        ${bar}
      </div>`;
  }

  function _esc(s) {
    return String(s || '').replace(/[&<>"']/g, c =>
      ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[c]));
  }

  return { load };
})();
