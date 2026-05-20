// Concept card renderer
const Concepts = (() => {
  function render(item) {
    const visual = item.visual_type && item.visual_type !== 'none'
      ? `<div class="concept-visual"><img src="/api/visual/${item.visual_type}" alt="${_esc(item.title)}" loading="lazy"></div>`
      : '';
    const takeaway = item.key_takeaway
      ? `<div class="concept-takeaway"><span class="takeaway-label">Kernaussage</span>${_esc(item.key_takeaway)}</div>`
      : '';

    return `
      <div class="concept-card">
        <div class="concept-header">
          <span class="concept-badge">Konzept</span>
          <h2 class="concept-title">${_esc(item.title)}</h2>
        </div>
        ${visual}
        <div class="concept-body">${item.content_html || ''}</div>
        ${takeaway}
      </div>`;
  }

  function _esc(str) {
    return String(str || '').replace(/[&<>"']/g, c =>
      ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[c]));
  }

  return { render };
})();
