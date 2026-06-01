// Frontend progress utilities – reads from /api/progress
const Progress = (() => {
  let _data = null;

  async function load() {
    _data = Store.getStats();
    return _data;
  }

  function get() { return _data; }

  function updateHeader() {
    if (!_data) return;
    const pct = _data.chapters_total
      ? Math.round(_data.chapters_completed / _data.chapters_total * 100)
      : 0;
    const el = document.getElementById('summary-pct');
    if (el) el.textContent = pct + '%';
  }

  function updateSidebar() {
    if (!_data) return;
    const chapEl  = document.getElementById('stat-chapters');
    const accEl   = document.getElementById('stat-accuracy');
    const answEl  = document.getElementById('stat-answered');
    if (chapEl) chapEl.textContent = `${_data.chapters_completed}/${_data.chapters_total}`;
    if (accEl)  accEl.textContent  = _data.answered ? _data.accuracy + '%' : '–';
    if (answEl) answEl.textContent = _data.answered;
  }

  async function refresh() {
    await load();
    updateHeader();
    updateSidebar();
  }

  return { load, get, refresh, updateHeader, updateSidebar };
})();
