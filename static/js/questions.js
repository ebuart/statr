// Question renderer + answer handling for all 7 question types
const Questions = (() => {
  let _current = null;
  let _hintUsed = false;
  let _answered = false;
  let _onAnswer = null; // fn(correct, hintUsed)

  // ── Public API ─────────────────────────────────────────────────

  function render(item, onAnswer) {
    _current   = item;
    _hintUsed  = false;
    _answered  = false;
    _onAnswer  = onAnswer;

    const type = item.type || 'multiple_choice';
    switch (type) {
      case 'multiple_choice':   return _renderMC(item);
      case 'code_output':       return _renderCodeOutput(item);
      case 'code_completion':   return _renderCodeCompletion(item);
      case 'true_false':        return _renderTF(item);
      case 'concept_matching':  return _renderMatching(item);
      case 'mini_challenge':    return _renderMiniChallenge(item);
      case 'interpret_conclude': return _renderInterpret(item);
      default:                  return _renderMC(item);
    }
  }

  function useHint() {
    _hintUsed = true;
  }

  // Returns the 0-based index of the correct option.
  // item.correct may be an integer index already, or a string matching one of item.options.
  function _correctIdx(item) {
    const c = item.correct;
    if (typeof c === 'number') return c;
    const opts = item.options || [];
    const idx = opts.findIndex(o => String(o) === String(c));
    return idx >= 0 ? idx : 0;
  }

  // Shuffle options and return { shuffled, correctIdx }.
  function _shuffleOptions(item) {
    const opts = (item.options || []).slice();
    const origCorrectIdx = _correctIdx(item);
    const correctVal = opts[origCorrectIdx];
    // Fisher-Yates
    for (let i = opts.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [opts[i], opts[j]] = [opts[j], opts[i]];
    }
    const newCorrectIdx = opts.findIndex(o => o === correctVal);
    return { shuffled: opts, correctIdx: newCorrectIdx };
  }

  // ── Shared helpers ─────────────────────────────────────────────

  function _esc(s) {
    return String(s || '').replace(/[&<>"']/g, c =>
      ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[c]));
  }

  function _codeBlock(code) {
    if (!code) return '';
    return `<pre class="code-block"><code class="language-r">${_esc(code)}</code></pre>`;
  }

  function _diffBadge(d) {
    const labels = { 1: 'Leicht', 2: 'Mittel', 3: 'Schwer' };
    const cls    = { 1: 'diff-low', 2: 'diff-mid', 3: 'diff-high' };
    return `<span class="diff-badge ${cls[d] || 'diff-mid'}">${labels[d] || 'Mittel'}</span>`;
  }

  function _questionShell(item, bodyHtml) {
    const code  = item.code_snippet ? _codeBlock(item.code_snippet) : '';
    const ctx   = item.context
      ? `<p class="q-context">${_esc(item.context)}</p>` : '';
    const diff  = _diffBadge(item.difficulty);
    return `
      <div class="question-card" id="q-card">
        <div class="q-meta">${diff}</div>
        ${ctx}
        <p class="q-text">${_esc(item.question)}</p>
        ${code}
        ${bodyHtml}
        <div class="explain-panel" id="explain-panel" style="display:none"></div>
      </div>`;
  }

  function _showExplain(correct) {
    const panel = document.getElementById('explain-panel');
    const card  = document.getElementById('q-card');
    if (!panel || !_current) return;
    panel.style.display = 'block';
    panel.innerHTML = `
      <span class="explain-result ${correct ? 'correct' : 'wrong'}">
        ${correct ? '✓ Richtig' : '✗ Falsch'}
      </span>
      <p class="explain-text">${_esc(_current.explanation || '')}</p>`;
    if (card) card.classList.add(correct ? 'correct' : 'wrong');
    setTimeout(() => hljs && hljs.highlightAll && hljs.highlightAll(), 50);
  }

  function _lockOptions() {
    document.querySelectorAll('.option-btn').forEach(b => b.disabled = true);
  }

  function _fireAnswer(correct) {
    if (_answered) return;
    _answered = true;
    _showExplain(correct);
    if (_onAnswer) _onAnswer(correct, _hintUsed);
  }

  // ── Multiple Choice ────────────────────────────────────────────

  function _renderMC(item) {
    const { shuffled, correctIdx } = _shuffleOptions(item);
    const opts = shuffled.map((o, i) => `
      <button class="option-btn" data-idx="${i}">${_esc(o)}</button>`).join('');
    const html = `<div class="options-list">${opts}</div>`;
    const shell = _questionShell(item, html);

    setTimeout(() => {
      document.querySelectorAll('.option-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          if (_answered) return;
          const idx = parseInt(btn.dataset.idx);
          const correct = idx === correctIdx;
          _lockOptions();
          btn.classList.add(correct ? 'selected-correct' : 'selected-wrong');
          if (!correct) {
            const rightBtn = document.querySelector(`.option-btn[data-idx="${correctIdx}"]`);
            if (rightBtn) rightBtn.classList.add('correct-reveal');
          }
          _fireAnswer(correct);
        });
      });
      hljs && hljs.highlightAll && hljs.highlightAll();
    }, 0);

    return shell;
  }

  // ── Code Output ───────────────────────────────────────────────

  function _renderCodeOutput(item) {
    return _renderMC(item); // same mechanics, code shown in shell
  }

  // ── Code Completion ───────────────────────────────────────────

  function _renderCodeCompletion(item) {
    const { shuffled, correctIdx } = _shuffleOptions(item);
    const opts = shuffled.map((o, i) => `
      <button class="option-btn code-opt" data-idx="${i}"><code>${_esc(o)}</code></button>`).join('');
    const html = `<div class="options-list">${opts}</div>`;
    const shell = _questionShell(item, html);

    setTimeout(() => {
      document.querySelectorAll('.option-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          if (_answered) return;
          const idx = parseInt(btn.dataset.idx);
          const correct = idx === correctIdx;
          _lockOptions();
          btn.classList.add(correct ? 'selected-correct' : 'selected-wrong');
          if (!correct) {
            const rightBtn = document.querySelector(`.option-btn[data-idx="${correctIdx}"]`);
            if (rightBtn) rightBtn.classList.add('correct-reveal');
          }
          _fireAnswer(correct);
        });
      });
      hljs && hljs.highlightAll && hljs.highlightAll();
    }, 0);

    return shell;
  }

  // ── True / False ──────────────────────────────────────────────

  function _renderTF(item) {
    const tfItem = (item.options && item.options.length) ? item : { ...item, options: ['TRUE', 'FALSE'] };
    const { shuffled, correctIdx } = _shuffleOptions(tfItem);
    const html = `
      <div class="tf-row">
        ${shuffled.map((o, i) => `<button class="option-btn tf-btn" data-idx="${i}">${_esc(o)}</button>`).join('')}
      </div>`;
    const shell = _questionShell(item, html);

    setTimeout(() => {
      document.querySelectorAll('.tf-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          if (_answered) return;
          const idx = parseInt(btn.dataset.idx);
          const correct = idx === correctIdx;
          _lockOptions();
          btn.classList.add(correct ? 'selected-correct' : 'selected-wrong');
          if (!correct) {
            const rightBtn = document.querySelector(`.tf-btn[data-idx="${correctIdx}"]`);
            if (rightBtn) rightBtn.classList.add('correct-reveal');
          }
          _fireAnswer(correct);
        });
      });
      hljs && hljs.highlightAll && hljs.highlightAll();
    }, 0);

    return shell;
  }

  // ── Concept Matching ──────────────────────────────────────────

  function _renderMatching(item) {
    const body = `<div id="matching-area"></div>
      <button class="btn-primary btn-submit-match" id="btn-submit-match" style="display:none">
        Fertig
      </button>`;
    const shell = _questionShell(item, body);

    setTimeout(() => {
      const area = document.getElementById('matching-area');
      if (!area || !item.pairs) return;
      Matching.init(area, item.pairs, allCorrect => {
        if (allCorrect) _fireAnswer(true);
      });
      hljs && hljs.highlightAll && hljs.highlightAll();
    }, 0);

    return shell;
  }

  // ── Mini Challenge ────────────────────────────────────────────

  function _renderMiniChallenge(item) {
    const html = `
      <textarea class="code-input" id="code-input" rows="6"
        placeholder="# Dein R-Code hier…" spellcheck="false"></textarea>
      <div class="mini-challenge-actions">
        <button class="btn-primary" id="btn-check-code">Prüfen</button>
      </div>`;
    const shell = _questionShell(item, html);

    setTimeout(() => {
      const btn = document.getElementById('btn-check-code');
      if (!btn) return;
      btn.addEventListener('click', () => {
        if (_answered) return;
        const inp = document.getElementById('code-input');
        const val = (inp ? inp.value : '').trim().toLowerCase();
        const expected = String(item.correct_pattern || item.correct || '').toLowerCase();
        const correct = expected ? val.includes(expected) : val.length > 5;
        if (inp) inp.disabled = true;
        btn.disabled = true;
        _fireAnswer(correct);
      });
    }, 0);

    return shell;
  }

  // ── Interpret & Conclude ──────────────────────────────────────

  function _renderInterpret(item) {
    // Shows R console output + asks for statistical interpretation
    const consoleOut = item.console_output || item.code_snippet;
    const consoleSim = consoleOut
      ? `<div class="console-sim"><pre>${_esc(consoleOut)}</pre></div>`
      : '';

    const { shuffled, correctIdx } = _shuffleOptions(item);
    const opts = shuffled.map((o, i) => `
      <button class="option-btn" data-idx="${i}">${_esc(o)}</button>`).join('');

    const inner = `
      ${consoleSim}
      <div class="options-list">${opts}</div>`;
    const shell = _questionShell(item, inner);

    setTimeout(() => {
      document.querySelectorAll('.option-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          if (_answered) return;
          const idx = parseInt(btn.dataset.idx);
          const correct = idx === correctIdx;
          _lockOptions();
          btn.classList.add(correct ? 'selected-correct' : 'selected-wrong');
          if (!correct) {
            const rightBtn = document.querySelector(`.option-btn[data-idx="${correctIdx}"]`);
            if (rightBtn) rightBtn.classList.add('correct-reveal');
          }
          _fireAnswer(correct);
        });
      });
      hljs && hljs.highlightAll && hljs.highlightAll();
    }, 0);

    return shell;
  }

  return { render, useHint };
})();
