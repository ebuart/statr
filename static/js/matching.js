// Drag-and-drop engine for concept_matching question type
const Matching = (() => {
  let _container = null;
  let _pairs = [];
  let _matched = {};
  let _onComplete = null;

  function init(container, pairs, onComplete) {
    _container = container;
    _pairs = pairs;
    _matched = {};
    _onComplete = onComplete;
    _render();
  }

  function _render() {
    const terms = _pairs.map(p => ({ id: p.id, text: p.term }));
    const defs = _shuffle(_pairs.map(p => ({ id: p.id, text: p.definition })));

    _container.innerHTML = `
      <div class="matching-container">
        <div class="matching-col matching-terms">
          ${terms.map(t => `
            <div class="drag-item" draggable="true" data-id="${t.id}" data-type="term">
              ${_escape(t.text)}
            </div>`).join('')}
        </div>
        <div class="matching-col matching-defs">
          ${defs.map(d => `
            <div class="drop-zone" data-id="${d.id}">
              <span class="drop-zone-text">${_escape(d.text)}</span>
              <span class="drop-zone-badge"></span>
            </div>`).join('')}
        </div>
      </div>`;

    _bindDrag();
    _bindTouch();
  }

  function _bindDrag() {
    let dragId = null;

    _container.querySelectorAll('.drag-item').forEach(el => {
      el.addEventListener('dragstart', e => {
        dragId = el.dataset.id;
        el.classList.add('dragging');
        e.dataTransfer.effectAllowed = 'move';
      });
      el.addEventListener('dragend', () => el.classList.remove('dragging'));
    });

    _container.querySelectorAll('.drop-zone').forEach(zone => {
      zone.addEventListener('dragover', e => { e.preventDefault(); zone.classList.add('drag-over'); });
      zone.addEventListener('dragleave', () => zone.classList.remove('drag-over'));
      zone.addEventListener('drop', e => {
        e.preventDefault();
        zone.classList.remove('drag-over');
        if (dragId) _attempt(dragId, zone.dataset.id);
        dragId = null;
      });
    });
  }

  function _bindTouch() {
    let active = null, ghost = null;

    _container.querySelectorAll('.drag-item').forEach(el => {
      el.addEventListener('touchstart', e => {
        active = el;
        const t = e.touches[0];
        ghost = el.cloneNode(true);
        ghost.style.cssText = `position:fixed;opacity:0.8;pointer-events:none;z-index:9999;left:${t.clientX - 40}px;top:${t.clientY - 20}px;`;
        document.body.appendChild(ghost);
        el.classList.add('dragging');
      }, { passive: true });

      el.addEventListener('touchmove', e => {
        if (!ghost) return;
        const t = e.touches[0];
        ghost.style.left = `${t.clientX - 40}px`;
        ghost.style.top  = `${t.clientY - 20}px`;
        e.preventDefault();
      }, { passive: false });

      el.addEventListener('touchend', e => {
        if (ghost) { ghost.remove(); ghost = null; }
        if (!active) return;
        active.classList.remove('dragging');
        const t = e.changedTouches[0];
        const target = document.elementFromPoint(t.clientX, t.clientY);
        const zone = target && target.closest('.drop-zone');
        if (zone) _attempt(active.dataset.id, zone.dataset.id);
        active = null;
      });
    });
  }

  function _attempt(termId, defId) {
    const correct = termId === defId;
    _matched[termId] = correct;

    const termEl = _container.querySelector(`.drag-item[data-id="${termId}"]`);
    const zoneEl = _container.querySelector(`.drop-zone[data-id="${defId}"]`);

    if (termEl) {
      termEl.classList.toggle('match-correct', correct);
      termEl.classList.toggle('match-wrong', !correct);
      if (correct) termEl.setAttribute('draggable', 'false');
    }
    if (zoneEl) {
      zoneEl.classList.toggle('match-correct', correct);
      zoneEl.classList.toggle('match-wrong', !correct);
      const badge = zoneEl.querySelector('.drop-zone-badge');
      if (badge) badge.textContent = correct ? '✓' : '✗';
      if (!correct) {
        setTimeout(() => {
          zoneEl.classList.remove('match-wrong');
          if (badge) badge.textContent = '';
          if (termEl) { termEl.classList.remove('match-wrong'); }
        }, 800);
      }
    }

    if (correct && _onComplete) {
      const allDone = _pairs.every(p => _matched[p.id] === true);
      if (allDone) _onComplete(true);
    }
  }

  function isComplete() {
    return _pairs.every(p => _matched[p.id] === true);
  }

  function _shuffle(arr) {
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function _escape(str) {
    return String(str).replace(/[&<>"']/g, c =>
      ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[c]));
  }

  return { init, isComplete };
})();
