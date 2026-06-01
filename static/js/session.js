// Session view – orchestrates unit playback, concept cards, questions
const Session = (() => {
  let _chapterId   = null;
  let _chapterData = null;
  let _unitList    = [];
  let _activeUnit  = null;
  let _items       = [];
  let _idx         = 0;
  let _sessionCorrect = 0;
  let _sessionTotal   = 0;
  let _unitCache   = {}; // unit_id -> items (for local review)

  // ── Open chapter ───────────────────────────────────────────────

  async function open(chapterId, startUnitId) {
    _chapterId = chapterId;
    _sessionCorrect = 0;
    _sessionTotal   = 0;
    _unitCache = {};

    const r = await fetch(`/api/chapter/${chapterId}`);
    if (!r.ok) { alert('Kapitel nicht gefunden oder gesperrt.'); return; }
    _chapterData = await r.json();
    _unitList = _chapterData.units || [];

    document.getElementById('session-chapter-title').textContent =
      _chapterData.chapter?.title || '';

    _renderUnitsNav();
    App.showView('session');

    const first = startUnitId
      ? _unitList.find(u => u.unit_id === startUnitId)
      : _unitList[0];
    if (first) await _loadUnit(first.unit_id);
  }

  // ── Units nav ──────────────────────────────────────────────────

  function _renderUnitsNav() {
    const nav = document.getElementById('session-units-nav');
    if (!nav) return;
    nav.innerHTML = _unitList.map(u => {
      const status = Store.getUnitStatus(u.unit_id, _chapterId);
      const done = status === 'completed' ? 'done' : '';
      const type = u.unit_type === 'concept_intro' || u.unit_type === 'concept' ? 'concept' : 'practice';
      return `<button class="unit-nav-btn ${done}" data-uid="${u.unit_id}" data-type="${type}">
        <span class="unit-nav-dot"></span>
        <span class="unit-nav-label">${_esc(u.title)}</span>
      </button>`;
    }).join('');

    nav.querySelectorAll('.unit-nav-btn').forEach(btn => {
      btn.addEventListener('click', async () => {
        await _loadUnit(btn.dataset.uid);
      });
    });
  }

  function _setActiveNavBtn(unitId) {
    document.querySelectorAll('.unit-nav-btn').forEach(b => {
      b.classList.toggle('active', b.dataset.uid === unitId);
    });
  }

  // ── Load unit ──────────────────────────────────────────────────

  async function _loadUnit(unitId) {
    const r = await fetch(`/api/unit/${unitId}`);
    if (!r.ok) return;
    const data = await r.json();
    _activeUnit = data;
    _items = data.items || [];
    _idx   = Store.getUnitProgress(unitId);
    if (_idx >= _items.length) _idx = 0;
    if (_items.length) _unitCache[unitId] = _items;

    document.getElementById('session-unit-label').textContent = data.title || '';
    _setActiveNavBtn(unitId);
    _renderProgressBar();
    _renderItem();
  }

  // ── Render current item ────────────────────────────────────────

  function _renderItem() {
    const content = document.getElementById('session-content');
    if (!content || !_items.length) return;

    if (_idx >= _items.length) {
      _completeUnit();
      return;
    }

    const item = _items[_idx];
    _renderProgressBar();
    _updateSidebarMeta(item);

    if (item.type === 'concept_card') {
      content.innerHTML = Concepts.render(item) + `
        <div class="concept-nav">
          <button class="btn-primary" id="btn-concept-next">
            ${_idx + 1 < _items.length ? 'Weiter →' : 'Zur Übung →'}
          </button>
        </div>`;
      document.getElementById('btn-concept-next')?.addEventListener('click', _advance);
      _hideHint();
      setTimeout(() => hljs && hljs.highlightAll && hljs.highlightAll(), 50);
    } else {
      content.innerHTML = Questions.render(item, _onAnswer);
      _setupHint(item);
      setTimeout(() => hljs && hljs.highlightAll && hljs.highlightAll(), 50);
    }

    // counter in sidebar
    const ctr = document.getElementById('question-counter');
    if (ctr) ctr.textContent = `${_idx + 1} / ${_items.length}`;
  }

  // ── Answer callback ────────────────────────────────────────────

  async function _onAnswer(correct, hintUsed) {
    if (_activeUnit) {
      const qid = _items[_idx]?.id;
      if (qid) {
        Store.recordAnswer({
          question_id: qid,
          correct,
          hint_used: hintUsed,
          unit_id: _activeUnit.unit_id,
          item_index: _idx,
        });
      }
    }

    if (_items[_idx]?.type !== 'concept_card') {
      _sessionTotal++;
      if (correct && !hintUsed) _sessionCorrect++;
    }

    _hideHint();
    _injectNextBtn(correct);
  }

  function _injectNextBtn(correct) {
    const content = document.getElementById('session-content');
    if (!content) return;
    const existing = content.querySelector('.btn-next-q');
    if (existing) return;
    const btn = document.createElement('button');
    btn.className = 'btn-primary btn-next-q';
    btn.textContent = _idx + 1 < _items.length ? 'Weiter →' : 'Abschließen ✓';
    btn.addEventListener('click', _advance);
    content.appendChild(btn);
  }

  function _advance() {
    _idx++;
    _renderItem();
  }

  // ── Unit complete ──────────────────────────────────────────────

  async function _completeUnit() {
    if (!_activeUnit) return;
    Store.completeUnit({ unit_id: _activeUnit.unit_id, chapter_id: _chapterId });

    // Mark nav btn done
    const navBtn = document.querySelector(`.unit-nav-btn[data-uid="${_activeUnit.unit_id}"]`);
    if (navBtn) navBtn.classList.add('done');

    // Find next unit that actually has items (skip empty summary units)
    const currIdx = _unitList.findIndex(u => u.unit_id === _activeUnit.unit_id);
    const next = _unitList.slice(currIdx + 1).find(u => (u.item_count || 0) > 0);

    if (next) {
      await _loadUnit(next.unit_id);
    } else {
      await _completeChapter();
    }
  }

  // ── Chapter complete ───────────────────────────────────────────

  async function _completeChapter() {
    const accuracy = _sessionTotal
      ? Math.round(_sessionCorrect / _sessionTotal * 100) : 100;

    Store.completeChapter({ chapter_id: _chapterId, accuracy });

    document.getElementById('complete-title').textContent =
      (_chapterData?.chapter?.title || 'Kapitel') + ' abgeschlossen!';
    document.getElementById('complete-accuracy').textContent =
      `${accuracy}% Richtig`;

    const reviewWrap = document.getElementById('complete-review-btn-wrap');
    if (reviewWrap) {
      if (_sessionTotal > 0 && accuracy < 100) {
        reviewWrap.innerHTML = `<button class="btn-secondary" id="btn-review">
          Fehler wiederholen</button>`;
        document.getElementById('btn-review')?.addEventListener('click', () => {
          _startReview();
        });
      } else {
        reviewWrap.innerHTML = '';
      }
    }

    App.showView('complete');
    Progress.refresh();
  }

  async function _startReview() {
    const wrongIds = new Set(Store.getWrongIds(_chapterId));
    if (!wrongIds.size) { alert('Keine Fehler!'); return; }

    const items = [];
    for (const cachedItems of Object.values(_unitCache)) {
      for (const item of cachedItems) {
        if (item.id && wrongIds.has(item.id)) items.push(item);
      }
    }

    if (!items.length) { alert('Keine Fehler!'); return; }

    _items = items;
    _idx   = 0;
    _sessionCorrect = 0;
    _sessionTotal   = 0;
    App.showView('session');
    _renderItem();
  }

  // ── Hint ───────────────────────────────────────────────────────

  function _setupHint(item) {
    const btn   = document.getElementById('hint-btn');
    const panel = document.getElementById('hint-panel');
    if (!btn || !panel) return;
    if (item.hint) {
      btn.style.display = 'block';
      panel.style.display = 'none';
      panel.textContent = item.hint;
      btn.onclick = () => {
        panel.style.display = 'block';
        btn.style.display   = 'none';
        Questions.useHint();
      };
    } else {
      _hideHint();
    }
  }

  function _hideHint() {
    const btn   = document.getElementById('hint-btn');
    const panel = document.getElementById('hint-panel');
    if (btn)   btn.style.display   = 'none';
    if (panel) panel.style.display = 'none';
  }

  // ── Sidebar meta ───────────────────────────────────────────────

  function _updateSidebarMeta(item) {
    const diffEl = document.getElementById('difficulty-display');
    const typeEl = document.getElementById('question-type-display');
    if (diffEl) {
      const labels = { 1:'Leicht', 2:'Mittel', 3:'Schwer' };
      diffEl.textContent = item.difficulty ? labels[item.difficulty] : '';
    }
    if (typeEl) {
      const labels = {
        multiple_choice: 'Multiple Choice',
        code_output: 'Code Output',
        code_completion: 'Code Vervollständigung',
        true_false: 'Wahr / Falsch',
        concept_matching: 'Zuordnung',
        mini_challenge: 'Mini-Challenge',
        interpret_conclude: 'Interpretieren',
        concept_card: 'Konzept',
      };
      typeEl.textContent = labels[item.type] || '';
    }
  }

  // ── Progress bar ───────────────────────────────────────────────

  function _renderProgressBar() {
    const fill = document.getElementById('session-progress-fill');
    if (!fill || !_items.length) return;
    const pct = Math.round(_idx / _items.length * 100);
    fill.style.width = pct + '%';
  }

  // ── Utils ──────────────────────────────────────────────────────

  function _esc(s) {
    return String(s || '').replace(/[&<>"']/g, c =>
      ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[c]));
  }

  return { open };
})();
