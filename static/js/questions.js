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
      case 'numeric':           return _renderNumeric(item);
      case 'dropdown_cloze':    return _renderCloze(item);
      case 'block_order':       return _renderBlockOrder(item);
      case 'self_check':        return _renderSelfCheck(item);
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

  // ── Numeric input (tolerance-checked, no options shown) ────────

  function _renderNumeric(item) {
    const blanks = item.blanks || [];
    const rows = blanks.map((b, i) => `
      <div class="num-row">
        <label class="num-label">${_esc(b.label || ('Wert ' + (i + 1)))}</label>
        <input type="text" inputmode="decimal" class="num-input" data-idx="${i}"
               autocomplete="off" spellcheck="false" placeholder="?">
      </div>`).join('');
    const body = `
      <div class="num-grid">${rows}</div>
      <button class="btn-primary" id="btn-check-num">Prüfen</button>`;
    const shell = _questionShell(item, body);

    setTimeout(() => {
      const btn = document.getElementById('btn-check-num');
      if (!btn) return;
      btn.addEventListener('click', () => {
        if (_answered) return;
        let allOk = true;
        document.querySelectorAll('.num-input').forEach(inp => {
          const i = parseInt(inp.dataset.idx);
          const b = blanks[i];
          const raw = (inp.value || '').replace(',', '.').trim();
          const val = parseFloat(raw);
          const tol = (b.tol != null) ? b.tol : 0.01;
          const ok = raw !== '' && Math.abs(val - b.answer) <= tol;
          inp.disabled = true;
          inp.classList.add(ok ? 'num-ok' : 'num-bad');
          if (!ok) { allOk = false; inp.value = raw + '  → ' + b.answer; }
        });
        btn.disabled = true;
        _fireAnswer(allOk);
      });
      hljs && hljs.highlightAll && hljs.highlightAll();
    }, 0);
    return shell;
  }

  // ── Dropdown cloze (overfull shared pools → not eliminable) ────

  function _renderCloze(item) {
    const pools = item.pools || {};
    const blanks = item.blanks || [];
    const tmpl = item.template || '';
    // Build select html for a blank
    const selHtml = (b, i) => {
      const pool = (b.pool && pools[b.pool]) ? pools[b.pool] : (b.options || []);
      const opts = pool.slice();
      for (let k = opts.length - 1; k > 0; k--) {
        const j = Math.floor(Math.random() * (k + 1));
        [opts[k], opts[j]] = [opts[j], opts[k]];
      }
      const optHtml = ['<option value="">– wählen –</option>']
        .concat(opts.map(o => `<option value="${_esc(o)}">${_esc(o)}</option>`)).join('');
      return `<select class="cloze-sel" data-idx="${i}">${optHtml}</select>`;
    };
    // Replace [[N]] placeholders
    let html = _esc(tmpl).replace(/\[\[(\d+)\]\]/g, (m, n) => {
      const i = parseInt(n);
      return blanks[i] ? selHtml(blanks[i], i) : m;
    }).replace(/\n/g, '<br>');
    const body = `
      <div class="cloze-body">${html}</div>
      <button class="btn-primary" id="btn-check-cloze">Prüfen</button>`;
    const shell = _questionShell(item, body);

    setTimeout(() => {
      const btn = document.getElementById('btn-check-cloze');
      if (!btn) return;
      btn.addEventListener('click', () => {
        if (_answered) return;
        let allOk = true;
        document.querySelectorAll('.cloze-sel').forEach(sel => {
          const i = parseInt(sel.dataset.idx);
          const ok = sel.value === String(blanks[i].answer);
          sel.disabled = true;
          sel.classList.add(ok ? 'cloze-ok' : 'cloze-bad');
          if (!ok) allOk = false;
        });
        btn.disabled = true;
        _fireAnswer(allOk);
      });
      hljs && hljs.highlightAll && hljs.highlightAll();
    }, 0);
    return shell;
  }

  // ── Block order (assemble/sort answer; distractors present) ────

  function _renderBlockOrder(item) {
    const blocks = (item.blocks || []).slice();
    for (let k = blocks.length - 1; k > 0; k--) {
      const j = Math.floor(Math.random() * (k + 1));
      [blocks[k], blocks[j]] = [blocks[j], blocks[k]];
    }
    const pool = blocks.map((b, i) =>
      `<button class="blk-chip" data-val="${_esc(b)}">${_esc(b)}</button>`).join('');
    const body = `
      <p class="blk-hint">${_esc(item.assemble_hint || 'Antwort der Reihe nach zusammenklicken (überzählige Blöcke bleiben übrig):')}</p>
      <div class="blk-answer" id="blk-answer"><span class="blk-placeholder">…</span></div>
      <div class="blk-pool" id="blk-pool">${pool}</div>
      <button class="btn-primary" id="btn-check-blk">Prüfen</button>`;
    const shell = _questionShell(item, body);

    const chosen = [];
    setTimeout(() => {
      const ansEl = document.getElementById('blk-answer');
      const redraw = () => {
        ansEl.innerHTML = chosen.length
          ? chosen.map((c, i) => `<button class="blk-chip in-ans" data-pos="${i}">${_esc(c)}</button>`).join('')
          : '<span class="blk-placeholder">…</span>';
        ansEl.querySelectorAll('.blk-chip').forEach(ch => {
          ch.addEventListener('click', () => {
            if (_answered) return;
            chosen.splice(parseInt(ch.dataset.pos), 1);
            redraw();
          });
        });
      };
      document.querySelectorAll('#blk-pool .blk-chip').forEach(ch => {
        ch.addEventListener('click', () => {
          if (_answered) return;
          chosen.push(ch.dataset.val);
          redraw();
        });
      });
      const btn = document.getElementById('btn-check-blk');
      btn.addEventListener('click', () => {
        if (_answered) return;
        const ans = item.answer || [];
        const ok = chosen.length === ans.length &&
                   chosen.every((c, i) => String(c) === String(ans[i]));
        btn.disabled = true;
        document.querySelectorAll('.blk-chip').forEach(c => c.disabled = true);
        ansEl.classList.add(ok ? 'blk-ok' : 'blk-bad');
        _fireAnswer(ok);
      });
      hljs && hljs.highlightAll && hljs.highlightAll();
    }, 0);
    return shell;
  }

  // ── Self-check (open free text + reveal Musterlösung) ──────────

  function _renderSelfCheck(item) {
    const body = `
      <textarea class="code-input" id="sc-input" rows="5"
        placeholder="Deine Antwort in Stichworten…" spellcheck="false"></textarea>
      <button class="btn-primary" id="btn-reveal-sc">Musterlösung zeigen</button>
      <div id="sc-solution" style="display:none">
        <div class="sc-model"><b>Musterlösung:</b><br>${_esc(item.sample_solution || '')}</div>
        <p class="sc-ask">Hattest du das Wesentliche?</p>
        <div class="sc-grade">
          <button class="btn-primary sc-yes">Ja, hatte ich ✓</button>
          <button class="btn-secondary sc-no">Nicht ganz ✗</button>
        </div>
      </div>`;
    const shell = _questionShell(item, body);
    setTimeout(() => {
      const reveal = document.getElementById('btn-reveal-sc');
      reveal.addEventListener('click', () => {
        document.getElementById('sc-solution').style.display = 'block';
        reveal.style.display = 'none';
        const inp = document.getElementById('sc-input');
        if (inp) inp.disabled = true;
      });
      document.querySelector('.sc-yes')?.addEventListener('click', () => { if (!_answered) _fireAnswer(true); });
      document.querySelector('.sc-no')?.addEventListener('click', () => { if (!_answered) _fireAnswer(false); });
    }, 0);
    return shell;
  }

  return { render, useHint };
})();
