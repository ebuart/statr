"""
klausur_bank.py – Klausursimulation-Kapitel: K1..K6, je 10 Varianten mit
zufaelligen Werten/Kontexten. Alle Antworten werden hier in Python BERECHNET,
damit sie garantiert korrekt sind. app.py injiziert das Kapitel beim Laden;
die Zufallsauswahl (1 aus 10 pro Aufgabe) macht api_unit via `pick`.
"""
import random

LETTERS = list("ABCDEFGHIJKLMN")
STATES = ["Bay", "Nds", "Sac", "BW", "Hes", "NRW", "Thü", "Bra"]
CITY_CTX = [
    ("Stadt", "Einw", "Einwohner (Tsd.)"),
    ("Filiale", "Ums", "Umsatz (Tsd. €)"),
    ("Produkt", "Preis", "Preis (€)"),
    ("Schule", "Schueler", "Schülerzahl"),
    ("Verein", "Mitgl", "Mitglieder"),
]

# ── Overfull shared dropdown pools (nicht per Ausschluss loesbar) ──
POOL_TEST = [
    "Chi-Quadrat-Unabhängigkeitstest", "Einstichproben-t-Test",
    "Zweistichproben-t-Test (gepaart)", "Zweistichproben-t-Test (ungepaart, Welch)",
    "Korrelationstest", "Binomialtest", "ANOVA (Varianzanalyse)",
    "Durbin-Watson-Test", "Levene-Test", "Shapiro-Wilk-Test",
    "Wilcoxon-Test", "F-Test auf Varianzgleichheit",
]
POOL_REL = ["≤", "<", ">", "≥", "=", "≠", "≈"]
POOL_DECIS = ["H₀ ablehnen", "H₀ nicht ablehnen", "H₁ ablehnen",
              "H₀ beweisen", "H₁ nicht ablehnen", "keine Entscheidung möglich"]
POOL_SIG = ["signifikant", "nicht signifikant", "hoch signifikant",
            "nicht interpretierbar", "zufällig", "kausal"]
POOL_FUNC = ["die Summe", "das Maximum", "das Minimum", "der Mittelwert",
             "das Produkt", "die Anzahl", "die Varianz", "der Median"]
POOL_DIST = ["auf [a,b] gleichverteilten", "normalverteilten", "poissonverteilten",
             "exponentialverteilten", "binomialverteilten", "diskret gleichverteilten"]
POOL_APPROX = ["die Wahrscheinlichkeit P(…)", "den Erwartungswert E(…)",
               "die Varianz V(…)", "den Median", "die Dichte", "die Verteilungsfunktion",
               "den Standardfehler", "die Korrelation"]


def _seed(k, i):
    return random.Random(k * 1000 + i * 7 + 13)


def _df_text(cols, rows):
    """Formatiert einen DataFrame wie R ihn druckt."""
    header = "  " + "  ".join(f"{c:>4}" if len(c) <= 4 else c for c in cols)
    lines = [header]
    for idx, r in enumerate(rows, 1):
        cells = "  ".join(f"{str(v):>4}" for v in r)
        lines.append(f"{idx}  {cells}")
    return "\n".join(lines)


def _mk(cid, i, typ, **kw):
    it = {"id": f"{cid}_{typ[:3]}{i}", "priority": "high", "type": typ,
          "difficulty": kw.pop("difficulty", 2)}
    it.update(kw)
    return it


# ─────────────────────────── K1 – DataFrame ───────────────────────────

def _k1(i):
    r = _seed(1, i)
    name, vcol, vlabel = r.choice(CITY_CTX)
    n = 7
    letters = LETTERS[:n]
    bls = [r.choice(STATES) for _ in range(n)]
    while len(set(bls)) < 3:
        bls = [r.choice(STATES) for _ in range(n)]
    vals = [r.choice(range(40, 141, r.choice([1, 5, 10]))) for _ in range(n)]
    cols = [name, "BL", vcol]
    rows = list(zip(letters, bls, vals))
    df = _df_text(cols, rows)
    ctx = f"DataFrame X ({name}, BL, {vcol})"
    kind = i % 7

    if kind == 0:  # sum mit Bedingung
        c = r.choice([80, 90, 100])
        sel = [v for v in vals if v > c]
        ans = sum(sel)
        snip = f"> X\n{df}\n> sum(X[X${vcol}>{c},3])"
        return _mk("k1", i, "numeric", context=ctx, code_snippet=snip,
                   question=f"Was gibt sum(X[X${vcol}>{c},3]) aus?",
                   blanks=[{"label": "Summe", "answer": ans, "tol": 0.5}],
                   explanation=f"Zeilen mit {vcol}>{c}: {sel} → Summe {ans}.",
                   hint=f"Erst Zeilen filtern ({vcol}>{c}), dann Spalte 3 summieren.")

    if kind == 1:  # order() -> Sequenz der Namen
        order = [letters[k] for k in sorted(range(n), key=lambda z: vals[z])]
        distract = [x for x in LETTERS[n:n + 3]]
        blocks = letters + distract
        snip = f"> X\n{df}\n> X[order(X${vcol}),]${name}"
        return _mk("k1", i, "block_order", context=ctx, code_snippet=snip,
                   question=f"Setze die Ausgabe von X[order(X${vcol}),]${name} zusammen.",
                   assemble_hint="Namen aufsteigend nach dem Zahlenwert anordnen (überzählige Blöcke bleiben übrig):",
                   blocks=blocks, answer=order,
                   explanation=f"Aufsteigend nach {vcol} sortiert: {' '.join(order)}.",
                   hint="order() gibt Positionen; kleinster Wert zuerst.")

    if kind == 2:  # X[i,] Zeile als cloze
        row = r.randrange(n)
        einw_pool = sorted(set(vals + [r.choice(range(40, 141)) for _ in range(5)]))
        snip = f"> X\n{df}\n> X[{row + 1},]"
        return _mk("k1", i, "dropdown_cloze", context=ctx, code_snippet=snip,
                   question=f"Stelle die Ausgabe von X[{row + 1},] zusammen:",
                   template=f"{name} = [[0]] · BL = [[1]] · {vcol} = [[2]]",
                   pools={"NAME": LETTERS[:n + 3], "BL": STATES, "VAL": [str(x) for x in einw_pool]},
                   blanks=[{"pool": "NAME", "answer": letters[row]},
                           {"pool": "BL", "answer": bls[row]},
                           {"pool": "VAL", "answer": str(vals[row])}],
                   explanation=f"Zeile {row + 1}: {letters[row]} {bls[row]} {vals[row]}.",
                   hint="X[i,] = ganze Zeile i, alle Spalten.")

    if kind == 3:  # apply length -> n
        snip = f"> X\n{df}\n> apply(X,2,length)"
        return _mk("k1", i, "numeric", difficulty=1, context=ctx, code_snippet=snip,
                   question="apply(X,2,length) liefert für jede Spalte denselben Wert. Welchen?",
                   blanks=[{"label": "Wert je Spalte", "answer": n, "tol": 0}],
                   explanation=f"Jede Spalte hat n={n} Einträge.",
                   hint="MARGIN=2 = Spalten; length = Anzahl Einträge.")

    if kind == 4:  # aggregate max/min je BL -> cloze
        fun = r.choice(["min", "max"])
        agg = {}
        for (l, b, v) in rows:
            agg[b] = (min if fun == "min" else max)(agg.get(b, v), v)
        states_sorted = sorted(agg)
        pv = sorted(set(vals + [r.choice(range(40, 141)) for _ in range(5)]))
        tmpl = " · ".join(f"{s} = [[{k}]]" for k, s in enumerate(states_sorted))
        blanks = [{"pool": "VAL", "answer": str(agg[s])} for s in states_sorted]
        snip = f"> X\n{df}\n> aggregate(X${vcol}~X$BL, FUN={fun})"
        return _mk("k1", i, "dropdown_cloze", difficulty=3, context=ctx, code_snippet=snip,
                   question=f"aggregate(...FUN={fun}) – ordne je Bundesland (alphabetisch) den Wert zu:",
                   template=tmpl, pools={"VAL": [str(x) for x in pv]}, blanks=blanks,
                   explanation="Je BL das " + ("Minimum" if fun == "min" else "Maximum") +
                               ": " + ", ".join(f"{s}={agg[s]}" for s in states_sorted) + ".",
                   hint="Gruppen alphabetisch, je Gruppe die Funktion anwenden.")

    if kind == 5:  # seq index -> block_order
        step = r.choice([2, 3])
        idxs = list(range(1, n, step))  # 0-based seq(2,n,step)-ish
        picked = [letters[k] for k in idxs]
        blocks = letters + LETTERS[n:n + 2]
        snip = f"> X\n{df}\n> X[seq(2,nrow(X),{step}),1]"
        return _mk("k1", i, "block_order", context=ctx, code_snippet=snip,
                   question=f"Setze die Ausgabe von X[seq(2,nrow(X),{step}),1] zusammen:",
                   assemble_hint=f"seq(2,{n},{step}) liefert Positionen – zugehörige Namen der Reihe nach:",
                   blocks=blocks, answer=picked,
                   explanation=f"seq(2,{n},{step}) = {[k+1 for k in idxs]} → {' '.join(picked)}.",
                   hint="seq(von,bis,schritt): Start 2, Schritt "+str(step)+", nie über n.")

    # kind == 6: einzelnes Element
    ri, ci = n - 1, 3
    snip = f"> X\n{df}\n> X[nrow(X),ncol(X)]"
    return _mk("k1", i, "numeric", difficulty=1, context=ctx, code_snippet=snip,
               question="Was gibt X[nrow(X),ncol(X)] aus?",
               blanks=[{"label": "Wert", "answer": vals[-1], "tol": 0}],
               explanation=f"Letzte Zeile ({n}), letzte Spalte (3): {vals[-1]}.",
               hint="nrow=letzte Zeile, ncol=letzte Spalte.")


# ─────────────────────────── K2 – Monte-Carlo ─────────────────────────

def _k2(i):
    r = _seed(2, i)
    m = r.choice([5, 8, 10, 12, 15, 20])
    a, b = 10, 20
    reps = r.choice([1000, 2000, 5000])
    kind = i % 3

    if kind == 0:  # sum runif, mean(x>c)
        ev = m * (a + b) / 2
        c = int(round(ev / 10) * 10)
        snip = (f"f <- function(n) {{\n  x <- runif(n, {a}, {b})\n  return(sum(x))\n}}\n"
                f"x <- replicate({reps}, f({m}))\nmean(x > {c})")
        return _mk("k2", i, "dropdown_cloze", context="Monte-Carlo-Simulation", code_snippet=snip,
                   question="Beschreibe, was der Code berechnet:",
                   template=(f"f({m}) simuliert [[0]] von {m} [[1]] Zufallszahlen. "
                             f"replicate wiederholt das {reps}-mal. mean(x > {c}) ist eine Näherung für [[2]]."),
                   pools={"FUNC": POOL_FUNC, "DIST": POOL_DIST, "APX": POOL_APPROX},
                   blanks=[{"pool": "FUNC", "answer": "die Summe"},
                           {"pool": "DIST", "answer": "auf [a,b] gleichverteilten"},
                           {"pool": "APX", "answer": "die Wahrscheinlichkeit P(…)"}],
                   explanation=f"Summe von {m} U({a},{b})-Zahlen; E(Summe)={ev:.0f}. "
                               f"mean(x>{c}) ≈ P(Summe > {c}).",
                   hint="mean(Bedingung) = Anteil = Näherung für eine Wahrscheinlichkeit.")

    if kind == 1:  # plausibility numeric
        ev = m * (a + b) / 2
        snip = (f"f <- function(n) sum(runif(n, {a}, {b}))\n"
                f"x <- replicate({reps}, f({m}))\nmean(x)")
        return _mk("k2", i, "numeric", context="Monte-Carlo-Simulation", code_snippet=snip,
                   question=f"mean(x) nähert E(Summe von {m} U({a},{b})-Zahlen). Welchen Wert erwartest du?",
                   blanks=[{"label": "≈ E(Summe)", "answer": ev, "tol": ev * 0.03 + 1}],
                   explanation=f"E einer U({a},{b})-Zahl = {(a+b)/2}; × {m} = {ev:.0f}.",
                   hint="E(U(a,b)) = (a+b)/2, mal Anzahl.")

    # kind == 2: max rnorm
    mu, sd = r.choice([100, 50, 80]), r.choice([10, 15, 20])
    snip = (f"f <- function(k) max(rnorm(k, {mu}, {sd}))\n"
            f"y <- replicate({reps}, f({m}))\nmean(y <= {mu + sd})")
    return _mk("k2", i, "dropdown_cloze", context="Monte-Carlo-Simulation", code_snippet=snip,
               question="Beschreibe, was der Code berechnet:",
               template=(f"f({m}) simuliert [[0]] von {m} [[1]] Zufallszahlen. "
                         f"mean(y <= {mu + sd}) ist eine Näherung für [[2]]."),
               pools={"FUNC": POOL_FUNC, "DIST": POOL_DIST, "APX": POOL_APPROX},
               blanks=[{"pool": "FUNC", "answer": "das Maximum"},
                       {"pool": "DIST", "answer": "normalverteilten"},
                       {"pool": "APX", "answer": "die Wahrscheinlichkeit P(…)"}],
               explanation=f"Maximum von {m} N({mu},{sd})-Zahlen; mean(y≤{mu+sd}) ≈ P(max ≤ {mu+sd}).",
               hint="max() über die Stichprobe; mean(≤) ≈ Wahrscheinlichkeit.")


# ───────────────────────── K3 – Chi² & ANOVA ──────────────────────────

def _k3(i):
    r = _seed(3, i)
    kind = i % 3

    if kind == 0:  # chi2 cloze
        x2 = round(r.uniform(2, 12), 3)
        df = r.choice([1, 2, 3])
        p = round(r.uniform(0.01, 0.09) if x2 > 6 else r.uniform(0.12, 0.6), 3)
        v1, v2 = r.choice([("Studiengruppe", "Geschlecht"), ("Region", "Kaufabschluss"),
                           ("Klasse", "Bestanden"), ("Abteilung", "Krankheit")])
        rel = "≤" if p <= 0.05 else ">"
        dec = "H₀ ablehnen" if p <= 0.05 else "H₀ nicht ablehnen"
        sig = "einen Zusammenhang" if p <= 0.05 else "keinen Zusammenhang"
        snip = (f"Pearson's Chi-squared test\ndata: {v1} and {v2}\n"
                f"X-squared = {x2}, df = {df}, p-value = {p}")
        return _mk("k3", i, "dropdown_cloze", context="Aufgabe K3(a) – Testoutput", code_snippet=snip,
                   question="Interpretiere den Test:",
                   template=(f"Der [[0]] prüft, ob {v1} und {v2} unabhängig sind. "
                             f"p = {p} [[1]] 0.05 → [[2]]. Die Daten zeigen [[3]]."),
                   pools={"TEST": POOL_TEST, "REL": POOL_REL, "DEC": POOL_DECIS,
                          "CON": ["einen Zusammenhang", "keinen Zusammenhang",
                                  "einen Mittelwertunterschied", "eine Korrelation",
                                  "gleiche Varianzen", "Normalverteilung"]},
                   blanks=[{"pool": "TEST", "answer": "Chi-Quadrat-Unabhängigkeitstest"},
                           {"pool": "REL", "answer": rel},
                           {"pool": "DEC", "answer": dec},
                           {"pool": "CON", "answer": sig}],
                   explanation=f"χ²-Unabhängigkeitstest; p={p} {rel} 0.05 → {dec}; {sig}.",
                   hint="χ² prüft Unabhängigkeit zweier abgezählter Merkmale.")

    if kind == 1:  # anova cloze
        k = r.choice([3, 4])
        n = r.choice([120, 150, 176, 200])
        fval = round(r.uniform(0.5, 5), 3)
        p = round(r.uniform(0.001, 0.04) if fval > 3 else r.uniform(0.1, 0.6), 3)
        rel = "≤" if p <= 0.05 else ">"
        dec = "H₀ ablehnen" if p <= 0.05 else "H₀ nicht ablehnen"
        con = ("mindestens zwei Gruppen unterscheiden sich" if p <= 0.05
               else "kein Gruppenunterschied nachweisbar")
        snip = (f"            Df Sum Sq Mean Sq F value Pr(>F)\n"
                f"Gruppe    {k-1:>4}   ...     ...  {fval}  {p}\n"
                f"Residuals {n-k:>4}   ...     ...")
        return _mk("k3", i, "dropdown_cloze", context="Aufgabe K3(b) – ANOVA", code_snippet=snip,
                   question="Interpretiere die ANOVA:",
                   template=(f"Die [[0]] prüft, ob sich die Erwartungswerte der Gruppen unterscheiden. "
                             f"p = {p} [[1]] 0.05 → [[2]], d.h. [[3]]."),
                   pools={"TEST": POOL_TEST, "REL": POOL_REL, "DEC": POOL_DECIS,
                          "CON": ["mindestens zwei Gruppen unterscheiden sich",
                                  "kein Gruppenunterschied nachweisbar",
                                  "alle Gruppen sind identisch", "die Varianzen sind gleich",
                                  "ein linearer Zusammenhang besteht", "die Daten sind normalverteilt"]},
                   blanks=[{"pool": "TEST", "answer": "ANOVA (Varianzanalyse)"},
                           {"pool": "REL", "answer": rel},
                           {"pool": "DEC", "answer": dec},
                           {"pool": "CON", "answer": con}],
                   explanation=f"ANOVA; F={fval}, p={p} {rel} 0.05 → {dec}; {con}.",
                   hint="Df der Gruppe = k−1, der Residuen = n−k.")

    # kind == 2: n und k aus Df berechnen
    k = r.choice([3, 4, 5])
    n = r.choice([100, 120, 150, 176])
    snip = (f"            Df Sum Sq Mean Sq F value Pr(>F)\n"
            f"SG        {k-1:>4}   2548    1274   1.635  0.198\n"
            f"Residuals {n-k:>4} 134773     779")
    return _mk("k3", i, "numeric", difficulty=2, context="Aufgabe K3(b) – ANOVA-Df",
               code_snippet=snip,
               question="Bestimme aus den Freiheitsgraden: Anzahl Gruppen k und Stichprobenumfang n.",
               blanks=[{"label": "Gruppen k", "answer": k, "tol": 0},
                       {"label": "Stichprobenumfang n", "answer": n, "tol": 0}],
               explanation=f"Df(Gruppe)=k−1={k-1} → k={k}; Df(Res)=n−k={n-k} → n={n}.",
               hint="k−1 = erste Df-Zeile; n−k = Residuals-Df.")


# ─────────────────────── K4 – Multiple Regression ŷ ───────────────────

def _k4(i):
    r = _seed(4, i)
    b0 = round(r.uniform(-5, 8), 3)
    bG = round(r.uniform(-3, 3), 3)
    b1 = round(r.uniform(-12, 12), 3)
    b2 = round(r.uniform(-8, 8), 3)
    b3 = round(r.uniform(-2, 2), 3)
    G = r.choice([0, 1, 2, 10])
    x1 = r.choice([0, 1, -1, 2])
    x2 = r.choice([-5, 0, 3, -2])
    x3 = r.choice([0, 1, -1])
    yhat = b0 + bG * G + b1 * x1 + b2 * x2 + b3 * x3
    snip = (f"Coefficients:\n(Intercept)      G       x1      x2      x3\n"
            f"{b0:>10} {bG:>7} {b1:>7} {b2:>7} {b3:>7}\n\n"
            f"Neuer Fall:  G={G}, x1={x1}, x2={x2}, x3={x3}")
    if i % 4 == 3:  # eine Variante: Vorzeichen-Interpretation als cloze
        sign = "positiv" if b1 > 0 else "negativ"
        return _mk("k4", i, "dropdown_cloze", context="Aufgabe K4 – Koeffizienten",
                   code_snippet=snip.split("\n\n")[0],
                   question="Interpretiere den Koeffizienten von x1:",
                   template=("Steigt x1 um 1 (übrige Variablen konstant), so ändert sich ŷ um [[0]]. "
                             "Der Zusammenhang zwischen x1 und y ist damit [[1]]."),
                   pools={"NUM": [str(b1), str(-b1), str(round(b1*2, 3)), str(b0), str(b2),
                                  str(round(b1+1, 3)), "1", "0"],
                          "SGN": ["positiv", "negativ", "unkorreliert", "quadratisch",
                                  "kausal", "nicht interpretierbar"]},
                   blanks=[{"pool": "NUM", "answer": str(b1)},
                           {"pool": "SGN", "answer": sign}],
                   explanation=f"Koeffizient b1={b1}: ŷ ändert sich um {b1} je Einheit x1 → {sign}.",
                   hint="bᵢ = Änderung von ŷ pro Einheit xᵢ bei konstanten übrigen.")
    return _mk("k4", i, "numeric", difficulty=2, context="Aufgabe K4 – ŷ berechnen",
               code_snippet=snip,
               question="Berechne die ŷ-Schätzung für den neuen Fall.",
               blanks=[{"label": "ŷ", "answer": round(yhat, 3), "tol": 0.05}],
               explanation=(f"ŷ = {b0} + {bG}·{G} + {b1}·{x1} + {b2}·{x2} + {b3}·{x3} "
                            f"= {yhat:.3f}."),
               hint="Alle Werte in die geschätzte Gleichung einsetzen und aufsummieren.")


# ─────────────────── K5 – Regression: summary-Diagnose ────────────────

def _k5(i):
    r = _seed(5, i)
    kind = i % 3

    if kind == 0:  # R^2 als Prozent
        r2 = round(r.uniform(0.2, 0.85), 3)
        snip = (f"lm(aus ~ ., data=X)\n...\nMultiple R-squared: {r2}, "
                f"Adjusted R-squared: {round(r2-0.02,3)}")
        return _mk("k5", i, "numeric", difficulty=1, context="Aufgabe K5 – Bestimmtheitsmaß",
                   code_snippet=snip,
                   question=f"Multiple R-squared: {r2}. Wie viel % der Streuung von y erklärt das Modell?",
                   blanks=[{"label": "erklärte Streuung in %", "answer": round(r2 * 100, 1), "tol": 0.2}],
                   explanation=f"R²={r2} → {r2*100:.1f} % der Streuung erklärt, Rest unerklärt.",
                   hint="R² · 100 = erklärter Streuungsanteil in Prozent.")

    if kind == 1:  # Durbin-Watson cloze
        dw = round(r.uniform(1.7, 2.3), 2)
        p = round(r.uniform(0.2, 0.7), 2)
        rel = "≤" if p <= 0.05 else ">"
        con = "Autokorrelation vorliegt" if p <= 0.05 else "keine Autokorrelation vorliegt"
        ok = "verletzt" if p <= 0.05 else "erfüllt"
        snip = (f"Durbin-Watson test\ndata: model\nDW = {dw}, p-value = {p}\n"
                f"alternative hypothesis: true autocorrelation is greater than 0")
        return _mk("k5", i, "dropdown_cloze", context="Aufgabe K5 – Residuendiagnose",
                   code_snippet=snip,
                   question="Interpretiere den Test:",
                   template=("Der [[0]] prüft die Residuen auf [[1]]. "
                             f"p = {p} [[2]] 0.05 → es zeigt sich, dass [[3]]; die Modellannahme ist damit [[4]]."),
                   pools={"TEST": POOL_TEST, "REL": POOL_REL,
                          "WHAT": ["Autokorrelation", "Heteroskedastizität", "Multikollinearität",
                                   "Normalverteilung", "Linearität", "Varianzgleichheit"],
                          "CON": ["Autokorrelation vorliegt", "keine Autokorrelation vorliegt",
                                  "Heteroskedastizität vorliegt", "die Fehler normalverteilt sind"],
                          "OK": ["erfüllt", "verletzt", "nicht prüfbar", "irrelevant"]},
                   blanks=[{"pool": "TEST", "answer": "Durbin-Watson-Test"},
                           {"pool": "WHAT", "answer": "Autokorrelation"},
                           {"pool": "REL", "answer": rel},
                           {"pool": "CON", "answer": con},
                           {"pool": "OK", "answer": ok}],
                   explanation=f"Durbin-Watson: DW={dw}, p={p} {rel} 0.05 → {con} (Annahme A {ok}).",
                   hint="H₀: keine Autokorrelation; DW ≈ 2 = gut.")

    # kind == 2: Multikollinearitaet / VIF cloze
    vif = round(r.uniform(6, 18), 1)
    lvl = "starke" if vif > 10 else "moderate bis hohe"
    snip = (f"Coefficients:\n              Estimate  Pr(>|t|)\n"
            f"gaus           1.0434  2.1e-06 ***\n"
            f"e              0.0002    0.988\n"
            f"m              1.3288    0.824\n\n> vif(model)\ngaus e m → z.B. {vif}")
    return _mk("k5", i, "dropdown_cloze", context="Aufgabe K5 – Multikollinearität",
               code_snippet=snip,
               question="Nur gaus ist signifikant, e und m nicht. Erkläre die Ursache:",
               template=("Mögliche Ursache ist [[0]]: die Information von e und m steckt schon in gaus. "
                         f"Der VIF von {vif} deutet auf [[1]] Multikollinearität. "
                         "Das bläht die [[2]] auf. Prüfen kann man es mit [[3]]."),
               pools={"CAUSE": ["Multikollinearität", "Heteroskedastizität", "Autokorrelation",
                                "Overfitting", "Nichtlinearität", "ein saturiertes Modell"],
                      "LVL": ["starke", "moderate bis hohe", "geringe", "keine"],
                      "WHAT": ["Standardfehler", "Bestimmtheitsmaße", "Residuen", "Freiheitsgrade"],
                      "HOW": ["den VIF (vif())", "den Durbin-Watson-Test", "einen Q-Q-Plot",
                              "den Levene-Test", "einen t-Test"]},
               blanks=[{"pool": "CAUSE", "answer": "Multikollinearität"},
                       {"pool": "LVL", "answer": lvl},
                       {"pool": "WHAT", "answer": "Standardfehler"},
                       {"pool": "HOW", "answer": "den VIF (vif())"}],
               explanation=f"Multikollinearität (VIF={vif}, {lvl}) bläht die Standardfehler auf → VIF/Streudiagramme prüfen.",
               hint="Korrelierte Prädiktoren → große Standardfehler; Diagnose per VIF.")


# ───────────────── K6 – gepaarter vs. ungepaarter t-Test ──────────────

def _k6(i):
    r = _seed(6, i)
    ctxp = r.choice([("Diät", "vor", "nach", "Gewicht"),
                     ("Training", "vorher", "nachher", "Reaktionszeit"),
                     ("Medikament", "Tag1", "Tag30", "Blutdruck")])
    label, a, b, meas = ctxp
    tp = round(r.uniform(2.0, 3.5), 2)
    pp = round(r.uniform(0.005, 0.045), 3)
    pu = round(r.uniform(0.1, 0.4), 2)
    md = round(r.uniform(1.5, 5.0), 2)
    kind = i % 3

    if kind == 0:  # welcher Test besser + Schluss
        snip = (f"> t.test({a}, {b}, paired=TRUE)\nPaired t-test\n"
                f"t = {tp}, df = 69, p-value = {pp}\nmean difference: {md}\n\n"
                f"> t.test({a}, {b}, paired=FALSE)\nWelch Two Sample t-test\n"
                f"t = 1.4, df = 115, p-value = {pu}")
        return _mk("k6", i, "dropdown_cloze", context=f"Aufgabe K6 – {label} ({meas} {a}/{b})",
                   code_snippet=snip,
                   question="Interpretiere und wähle den passenden Test:",
                   template=(f"Da {a} und {b} an denselben Einheiten gemessen wurden, ist der [[0]] geeignet. "
                             f"Sein p = {pp} [[1]] 0.05 → [[2]]; der Effekt ist [[3]]. "
                             f"Der ungepaarte Test übersieht ihn, weil er die [[4]] verschenkt."),
                   pools={"TEST": POOL_TEST, "REL": POOL_REL, "DEC": POOL_DECIS, "SIG": POOL_SIG,
                          "INFO": ["Paarung / Korrelation der Messungen", "Normalverteilung",
                                   "Stichprobengröße", "Varianzgleichheit", "Effektstärke"]},
                   blanks=[{"pool": "TEST", "answer": "Zweistichproben-t-Test (gepaart)"},
                           {"pool": "REL", "answer": "≤"},
                           {"pool": "DEC", "answer": "H₀ ablehnen"},
                           {"pool": "SIG", "answer": "signifikant"},
                           {"pool": "INFO", "answer": "Paarung / Korrelation der Messungen"}],
                   explanation=(f"Gepaart (p={pp}≤0.05) → signifikanter Effekt; ungepaart (p={pu}) übersieht ihn, "
                                "weil die Streuung zwischen den Einheiten nicht eliminiert wird."),
                   hint="Dieselben Einheiten zweimal gemessen → gepaart, trennschärfer.")

    if kind == 1:  # Korrelationstest Zweck cloze
        rr = round(r.uniform(0.5, 0.8), 3)
        snip = (f"Pearson's product-moment correlation\ndata: {a} and {b}\n"
                f"t = 7.8, df = 68, p-value = 6e-11\ncor = {rr}")
        return _mk("k6", i, "dropdown_cloze", context=f"Aufgabe K6 – {label}",
                   code_snippet=snip,
                   question="Wozu dient dieser Test vor dem eigentlichen Diät-/Effekt-Test?",
                   template=(f"Der [[0]] prüft, ob {a} und {b} [[1]] sind. "
                             f"r = {rr}, p = 6e-11 [[2]] 0.05 → die Messungen sind [[3]], "
                             "also sollte der Effekt-Test [[4]] durchgeführt werden."),
                   pools={"TEST": POOL_TEST, "REL": POOL_REL,
                          "KORR": ["korreliert", "unabhängig", "normalverteilt", "gleich groß"],
                          "PAIR": ["gepaart/abhängig", "unabhängig", "homoskedastisch", "identisch"],
                          "HOW": ["gepaart", "ungepaart", "einseitig", "mit ANOVA"]},
                   blanks=[{"pool": "TEST", "answer": "Korrelationstest"},
                           {"pool": "KORR", "answer": "korreliert"},
                           {"pool": "REL", "answer": "≤"},
                           {"pool": "PAIR", "answer": "gepaart/abhängig"},
                           {"pool": "HOW", "answer": "gepaart"}],
                   explanation=f"Korrelationstest zeigt r={rr} (p≤0.05) → Messungen abhängig → gepaarter t-Test.",
                   hint="Signifikante Korrelation der Messreihen ⇒ Paarung ⇒ gepaart testen.")

    # kind == 2: self_check – offene Begründung
    snip = (f"> t.test({a}-{b})\n95 percent confidence interval:\n {round(md-2,3)}  {round(md+2,3)}")
    return _mk("k6", i, "self_check", difficulty=2, context=f"Aufgabe K6 – {label}",
               code_snippet=snip,
               question=(f"Erläutere die Bedeutung des 95%-Konfidenzintervalls für die mittlere "
                         f"Differenz ({a}−{b}) und was folgt, wenn 0 nicht enthalten ist."),
               sample_solution=(f"Das Intervall [{round(md-2,3)}, {round(md+2,3)}] ist so konstruiert, dass bei "
                                "wiederholten Stichproben 95 % solcher Intervalle die wahre mittlere Differenz "
                                "überdecken. Da 0 NICHT enthalten ist (nur positive Werte), ist eine echte "
                                "mittlere Änderung plausibel – der Effekt ist auf 5%-Niveau signifikant."),
               explanation="Kernpunkte: 95 % Überdeckung bei Wiederholung; 0 nicht enthalten ⇒ signifikant.",
               hint="KI ohne 0 ⇒ signifikanter Unterschied.")


# ───────────────────────────── Aufbau ─────────────────────────────────

_GEN = {"K1": _k1, "K2": _k2, "K3": _k3, "K4": _k4, "K5": _k5, "K6": _k6}
_TITLES = {
    "K1": "K1 – DataFrame & Indexierung",
    "K2": "K2 – Monte-Carlo-Simulation",
    "K3": "K3 – Chi² & ANOVA",
    "K4": "K4 – Multiple Regression: ŷ",
    "K5": "K5 – Regressions-Diagnose",
    "K6": "K6 – t-Tests (gepaart/ungepaart)",
}


def build_chapter():
    units = [{
        "unit_id": "ch_klausursim_intro",
        "unit_type": "concept",
        "title": "So läuft die Simulation",
        "estimated_minutes": 1,
        "items": [{
            "type": "concept_card",
            "title": "Klausursimulation K1–K6",
            "content_html": (
                "<p>Diese Simulation zieht <b>pro Aufgabe K1–K6 zufällig eine von 10 Varianten</b> "
                "mit anderen Werten und Kontexten. Nichts ist am Kontext erratbar.</p>"
                "<ul><li><b>Berechnung:</b> Zahl eintippen (Toleranz erlaubt).</li>"
                "<li><b>Lückentext:</b> Dropdowns mit vielen Optionen – exakt richtig wählen.</li>"
                "<li><b>Blöcke ordnen:</b> Antwort der Reihe nach zusammenklicken; überzählige Blöcke bleiben übrig.</li>"
                "<li><b>Freitext:</b> selbst formulieren, dann mit Musterlösung vergleichen.</li></ul>"
                "<p>Am Ende siehst du deine <b>Trefferquote in %</b>. Mehrfach spielen = Intuition.</p>"),
            "key_takeaway": "Ein Durchgang = je 1 zufällige Variante von K1..K6. Trefferquote am Ende.",
        }],
    }]
    for key in ["K1", "K2", "K3", "K4", "K5", "K6"]:
        gen = _GEN[key]
        items = [gen(i) for i in range(10)]
        units.append({
            "unit_id": f"ch_klausursim_{key.lower()}",
            "unit_type": "practice",
            "title": _TITLES[key],
            "estimated_minutes": 3,
            "pick": 1,               # api_unit zieht 1 zufällige Variante
            "items": items,
        })
    return {
        "chapter_id": "ch_klausursim",
        "title": "🎯 Klausursimulation",
        "description": "Zufällige klausurnahe Aufgaben K1–K6 – nichts erratbar, Trefferquote am Ende.",
        "priority": "high",
        "unlocked": True,
        "units": units,
    }


if __name__ == "__main__":
    import json
    ch = build_chapter()
    tot = sum(len(u["items"]) for u in ch["units"] if u.get("unit_type") == "practice")
    print(f"Klausursimulation: {len(ch['units'])-1} Aufgaben, {tot} Varianten gesamt.")
    print(json.dumps(ch["units"][1]["items"][0], ensure_ascii=False, indent=1)[:600])
