// localStorage-based progress store — replaces all server-side progress calls
const Store = (() => {
  const KEY = 'statr_v1';
  let _chapterIds = [];
  let _chaptersTotal = 16;

  function _load() {
    try { return JSON.parse(localStorage.getItem(KEY) || '{}'); }
    catch { return {}; }
  }

  function _save(d) {
    try { localStorage.setItem(KEY, JSON.stringify(d)); }
    catch (e) { console.warn('Store.save failed', e); }
  }

  // Called once after /api/path loads
  function setMeta(chapterIds, total) {
    _chapterIds = chapterIds;
    _chaptersTotal = total;
  }

  // Overwrite server progress fields with local progress
  function enrichPath(chapters) {
    const p = _load();
    const chs = p.chapters || {};
    return chapters.map((ch, i) => {
      const cp = chs[ch.chapter_id] || {};
      const unlocked = i === 0 || !!cp.unlocked;
      const units_done = Object.values(cp.units || {}).filter(s => s === 'completed').length;
      const units_total = ch.unit_count || 0;
      const progress_pct = units_total ? Math.round(units_done / units_total * 100) : 0;
      return { ...ch, unlocked, completed: !!cp.completed, accuracy: cp.accuracy ?? null, progress_pct };
    });
  }

  function getCurrentChapter() {
    return _load().current_chapter || null;
  }

  function getUnitStatus(unit_id, chapter_id) {
    const p = _load();
    return ((p.chapters || {})[chapter_id]?.units || {})[unit_id] || 'not_started';
  }

  function getUnitProgress(unit_id) {
    const p = _load();
    return p.current_unit === unit_id ? (p.current_item || 0) : 0;
  }

  function recordAnswer({ question_id, correct, hint_used, unit_id, item_index }) {
    const p = _load();
    if (!p.questions) p.questions = {};
    const q = p.questions[question_id] || { times_seen: 0, times_correct: 0, hint_used: false };
    q.times_seen = (q.times_seen || 0) + 1;
    if (correct && !hint_used) q.times_correct = (q.times_correct || 0) + 1;
    q.last_result = correct ? 'correct' : 'wrong';
    if (hint_used) q.hint_used = true;
    p.questions[question_id] = q;
    p.current_unit = unit_id;
    p.current_item = (item_index || 0) + 1;
    _save(p);
  }

  function completeUnit({ unit_id, chapter_id }) {
    const p = _load();
    if (!p.chapters) p.chapters = {};
    if (!p.chapters[chapter_id]) p.chapters[chapter_id] = { unlocked: true };
    const cp = p.chapters[chapter_id];
    if (!cp.units) cp.units = {};
    cp.units[unit_id] = 'completed';
    p.current_unit = unit_id;
    p.current_item = 0;
    _save(p);
  }

  function completeChapter({ chapter_id, accuracy }) {
    const p = _load();
    if (!p.chapters) p.chapters = {};
    const cp = p.chapters[chapter_id] = p.chapters[chapter_id] || {};
    cp.completed = true;
    cp.accuracy = accuracy;

    let next_chapter = null;
    const idx = _chapterIds.indexOf(chapter_id);
    if (idx >= 0 && idx + 1 < _chapterIds.length) {
      const next_id = _chapterIds[idx + 1];
      if (!p.chapters[next_id]) p.chapters[next_id] = {};
      p.chapters[next_id].unlocked = true;
      p.current_chapter = next_id;
      next_chapter = next_id;
    }
    _save(p);
    return next_chapter;
  }

  function getWrongIds(chapter_id) {
    const p = _load();
    return Object.entries(p.questions || {})
      .filter(([qid, q]) => q.last_result === 'wrong' && qid.startsWith(chapter_id))
      .map(([qid]) => qid);
  }

  function getStats() {
    const p = _load();
    const answered = Object.keys(p.questions || {}).length;
    const correct = Object.values(p.questions || {}).filter(q => q.last_result === 'correct').length;
    const chapters_done = Object.values(p.chapters || {}).filter(cp => cp.completed).length;
    return {
      answered,
      correct,
      accuracy: answered ? Math.round(correct / answered * 100) : 0,
      chapters_completed: chapters_done,
      chapters_total: _chaptersTotal,
    };
  }

  return {
    setMeta, enrichPath, getCurrentChapter,
    getUnitStatus, getUnitProgress,
    recordAnswer, completeUnit, completeChapter,
    getWrongIds, getStats,
  };
})();
