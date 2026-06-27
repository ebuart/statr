import json

with open('/Users/maxim/Documents/Studium/COMSTATISTIK/statr/data/content.json', encoding='utf-8') as f:
    data = json.load(f)

# ═══════════════════════════════════════════════════════════════
# V12 – Multiple lineare Regression
# ═══════════════════════════════════════════════════════════════
ch_v12 = {
    "chapter_id": "ch_v12",
    "title": "Multiple Regression",
    "description": "Mehrere Prädiktoren, summary() lesen, predict()",
    "lecture": "V12",
    "priority": "high",
    "unlocked": False,
    "completed": False,
    "units": [
        {
            "unit_id": "ch_v12_concept_0",
            "unit_type": "concept",
            "title": "Das multiple Regressionsmodell",
            "estimated_minutes": 5,
            "items": [{
                "type": "concept_card",
                "title": "Von einfach zu multipel",
                "content_html": "<p>Einfache Regression: <code>y = β₀ + β₁·x + ε</code> — ein Prädiktor.</p><p>Multiple Regression: <code>y = β₀ + β₁·x₁ + β₂·x₂ + … + βₚ·xₚ + ε</code> — mehrere Prädiktoren gleichzeitig.</p><div class='console-sim'><span class='prompt'>&gt;</span> model &lt;- lm(Preis ~ Alter + Km, data=autos)<br><span class='prompt'>&gt;</span> coef(model)<br><span class='output'>(Intercept)       Alter          Km<br>  25000.00     -800.00       -0.05</span></div><p>Jedes βⱼ ist ein <strong>partieller Effekt</strong>: Einfluss von xⱼ bei konstantem Wert aller anderen Prädiktoren.</p>",
                "visual_type": "console",
                "key_takeaway": "lm(y ~ x1 + x2 + x3) passt multiple Regression an. Jeder Koeffizient misst den Effekt bei konstanten anderen Variablen."
            }]
        },
        {
            "unit_id": "ch_v12_concept_1",
            "unit_type": "concept",
            "title": "summary() bei multipler Regression lesen",
            "estimated_minutes": 7,
            "items": [{
                "type": "concept_card",
                "title": "Die wichtigsten Ausgaben von summary(lm())",
                "content_html": "<table class='concept-table'><thead><tr><th>Ausgabe</th><th>Bedeutung</th></tr></thead><tbody><tr><td><code>Estimate</code></td><td>Geschätzter Koeffizient β̂ⱼ</td></tr><tr><td><code>Std. Error</code></td><td>Standardfehler des Schätzers</td></tr><tr><td><code>t value</code></td><td>t = Estimate / Std.Error</td></tr><tr><td><code>Pr(&gt;|t|)</code></td><td>p-Wert: signifikant wenn &lt; 0.05</td></tr><tr><td><code>R-squared</code></td><td>Anteil erklärter Varianz (0–1)</td></tr><tr><td><code>Adj. R-squared</code></td><td>R² korrigiert für Prädiktorzahl</td></tr><tr><td><code>F-statistic</code></td><td>Test ob Gesamtmodell signifikant</td></tr></tbody></table>",
                "visual_type": "table",
                "key_takeaway": "Adj. R² statt R² für Modellvergleich nutzen – R² steigt immer wenn man Prädiktoren hinzufügt, auch unnötige."
            }]
        },
        {
            "unit_id": "ch_v12_concept_2",
            "unit_type": "concept",
            "title": "Interaktionen & predict()",
            "estimated_minutes": 5,
            "items": [{
                "type": "concept_card",
                "title": "Interaktionsterme und Vorhersage",
                "content_html": "<p><strong>Interaktion</strong>: Effekt von x₁ hängt von x₂ ab — <code>y ~ x1*x2</code> ist Kurzform für <code>y ~ x1 + x2 + x1:x2</code>.</p><p><strong>Quadratischer Term</strong>: <code>y ~ x + I(x^2)</code> — <code>I()</code> schützt vor R-Interpretation des <code>^</code>.</p><div class='console-sim'><span class='prompt'>&gt;</span> predict(model, data.frame(Alter=3, Km=50000))<br><span class='output'>[1] 19500</span><br><span class='prompt'>&gt;</span> predict(model, data.frame(Alter=3, Km=50000), interval=\"prediction\")<br><span class='output'>     fit   lwr   upr<br>[1,] 19500 14200 24800</span></div>",
                "visual_type": "console",
                "key_takeaway": "predict(model, newdata) sagt vorher. interval='prediction' gibt Prognoseintervall für neue Einzelwerte, interval='confidence' für den Erwartungswert."
            }]
        },
        {
            "unit_id": "ch_v12_practice_1",
            "unit_type": "practice",
            "title": "Multiple Regression – Praxistraining",
            "estimated_minutes": 20,
            "items": [
                {
                    "id": "ch_v12_q01",
                    "difficulty": 1, "priority": "high",
                    "type": "multiple_choice",
                    "context": "Du möchtest den Mietpreis aus Quadratmeter und Zimmeranzahl vorhersagen.",
                    "question": "Welcher Befehl passt das multiple Regressionsmodell an?",
                    "code_snippet": None,
                    "options": ["lm(Preis ~ Qm + Zimmer, data=df)", "lm(Preis ~ Qm, Zimmer, data=df)", "lm(y = Preis, x = Qm + Zimmer)", "glm(Preis ~ Qm + Zimmer)"],
                    "correct": "lm(Preis ~ Qm + Zimmer, data=df)",
                    "explanation": "In R trennt ~ die Zielvariable von den Prädiktoren. Mehrere Prädiktoren werden mit + verbunden: lm(y ~ x1 + x2, data=df).",
                    "hint": "Die Formelnotation: y ~ x1 + x2. Prädiktoren mit + trennen.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v12_q02",
                    "difficulty": 1, "priority": "high",
                    "type": "code_output",
                    "context": "summary(model) zeigt für den Prädiktor 'Alter': Estimate = -800, p-Wert = 0.002.",
                    "question": "Was bedeutet das (Signifikanzniveau α=0.05)?",
                    "code_snippet": None,
                    "options": [
                        "Alter ist signifikant; jedes zusätzliche Jahr senkt y um 800 (bei konstantem anderen Prädiktoren)",
                        "Alter ist nicht signifikant; der Effekt ist zu klein",
                        "Der p-Wert zeigt, dass Alter positiv mit y korreliert",
                        "Alter erklärt 80% der Varianz"
                    ],
                    "correct": "Alter ist signifikant; jedes zusätzliche Jahr senkt y um 800 (bei konstantem anderen Prädiktoren)",
                    "explanation": "p = 0.002 < 0.05 → signifikant, H₀ (β=0) wird abgelehnt. Estimate = -800: ein Jahr mehr Alter reduziert y um 800 Einheiten, bei konstantem Wert der anderen Prädiktoren.",
                    "hint": "p < α → signifikant. Das Vorzeichen des Estimate gibt die Richtung an.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v12_q03",
                    "difficulty": 2, "priority": "high",
                    "type": "multiple_choice",
                    "context": "Modell M1 hat R² = 0.85, Modell M2 (mit einem Extra-Prädiktor) hat R² = 0.86.",
                    "question": "Welches Gütekriterium ist für den Vergleich der Modelle besser geeignet?",
                    "code_snippet": None,
                    "options": ["Adjusted R²", "R²", "Residual standard error", "t-Wert der Koeffizienten"],
                    "correct": "Adjusted R²",
                    "explanation": "R² steigt immer wenn man einen Prädiktor hinzufügt, selbst wenn er nutzlos ist. Adjusted R² bestraft für jeden zusätzlichen Parameter und sinkt, wenn ein Prädiktor keinen echten Beitrag leistet.",
                    "hint": "Welches Maß korrigiert für die Anzahl der Prädiktoren?",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v12_q04",
                    "difficulty": 1, "priority": "medium",
                    "type": "code_output",
                    "context": "Du hast ein Regressionsmodell auf einem Autopreis-Datensatz trainiert.",
                    "question": "Was gibt dieser Befehl zurück?",
                    "code_snippet": "predict(model, data.frame(Alter=5, Km=80000))",
                    "options": [
                        "Den vorhergesagten Preis für ein 5 Jahre altes Auto mit 80.000 km",
                        "Den Korrelationskoeffizienten zwischen Alter und Km",
                        "Die Residuen für diese Beobachtung",
                        "Einen Fehler, da newdata fehlt"
                    ],
                    "correct": "Den vorhergesagten Preis für ein 5 Jahre altes Auto mit 80.000 km",
                    "explanation": "predict(model, newdata) berechnet ŷ = β̂₀ + β̂₁·Alter + β̂₂·Km für die angegebenen neuen Werte. data.frame() verpackt die neuen Werte in das erwartete Format.",
                    "hint": "predict() mit newdata macht eine Vorhersage für neue (nicht im Training gesehene) Werte.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v12_q05",
                    "difficulty": 2, "priority": "medium",
                    "type": "multiple_choice",
                    "context": "Du willst ein Modell anpassen, bei dem der Effekt von x1 je nach Wert von x2 verschieden ist.",
                    "question": "Welche Formel ist korrekt?",
                    "code_snippet": None,
                    "options": ["lm(y ~ x1 * x2)", "lm(y ~ x1 + x2, interaction=TRUE)", "lm(y ~ x1 & x2)", "lm(y ~ x1^x2)"],
                    "correct": "lm(y ~ x1 * x2)",
                    "explanation": "y ~ x1*x2 ist Kurzform für y ~ x1 + x2 + x1:x2. Der Interaktionsterm x1:x2 modelliert, dass der Effekt von x1 von x2 abhängt (und umgekehrt).",
                    "hint": "In R steht * für Haupteffekte + Interaktion, : nur für die Interaktion.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v12_q06",
                    "difficulty": 2, "priority": "high",
                    "type": "multiple_choice",
                    "context": "summary(model) zeigt F-statistic: 45.3 mit p-value < 2.2e-16.",
                    "question": "Was testet der F-Test in summary(lm())?",
                    "code_snippet": None,
                    "options": [
                        "Ob das Gesamtmodell besser ist als ein Modell nur mit Intercept (H₀: alle β = 0)",
                        "Ob die Residuen normalverteilt sind",
                        "Ob alle Prädiktoren signifikant sind",
                        "Ob die Varianzen der Gruppen gleich sind"
                    ],
                    "correct": "Ob das Gesamtmodell besser ist als ein Modell nur mit Intercept (H₀: alle β = 0)",
                    "explanation": "Der F-Test testet H₀: β₁ = β₂ = … = βₚ = 0, also ob keiner der Prädiktoren einen Effekt hat. Ein kleiner p-Wert → Gesamtmodell ist signifikant besser als das Nullmodell.",
                    "hint": "F-Test testet das Gesamtmodell, t-Tests testen einzelne Koeffizienten.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v12_q07",
                    "difficulty": 2, "priority": "medium",
                    "type": "multiple_choice",
                    "context": "Du willst einen quadratischen Zusammenhang modellieren.",
                    "question": "Welche Formel ist korrekt für y = β₀ + β₁x + β₂x²?",
                    "code_snippet": None,
                    "options": ["lm(y ~ x + I(x^2))", "lm(y ~ x + x^2)", "lm(y ~ x^2 + x)", "lm(y ~ poly(x,2), raw=TRUE)"],
                    "correct": "lm(y ~ x + I(x^2))",
                    "explanation": "Innerhalb von Formeln hat ^ eine spezielle Bedeutung (Interaktionstiefe). I() schützt davor: I(x^2) bedeutet 'rechne x^2 arithmetisch'. Alternative: poly(x,2,raw=TRUE).",
                    "hint": "Warum nicht einfach x^2? Weil ^ in Formeln anders interpretiert wird als in Ausdrücken.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v12_q08",
                    "difficulty": 1, "priority": "medium",
                    "type": "code_output",
                    "context": "Du willst die Residuen deines Modells inspizieren.",
                    "question": "Welcher Befehl liefert die Residuen?",
                    "code_snippet": "model <- lm(y ~ x1 + x2, data=df)",
                    "options": ["residuals(model)", "model$fitted", "predict(model)", "coef(model)"],
                    "correct": "residuals(model)",
                    "explanation": "residuals(model) bzw. model$residuals gibt die Differenzen eᵢ = yᵢ - ŷᵢ zurück. model$fitted liefert die angepassten Werte ŷᵢ, nicht die Residuen.",
                    "hint": "Residuum = tatsächlicher Wert minus vorhergesagter Wert.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v12_q09",
                    "difficulty": 3, "priority": "medium",
                    "type": "interpret_conclude",
                    "context": "Ein Modell mit 3 Prädiktoren auf n=50 Beobachtungen hat Residual standard error: 4.2 on 46 degrees of freedom.",
                    "question": "Wie kommen die 46 Freiheitsgrade zustande?",
                    "code_snippet": None,
                    "options": [
                        "n - (p+1) = 50 - 4 = 46 (n Beobachtungen minus Intercept und 3 Prädiktoren)",
                        "n - p = 50 - 4 = 46",
                        "p · (n-1) = 3 · 49 = 147, dann reduziert",
                        "Freiheitsgrade = n - 1 = 49, dann korrigiert"
                    ],
                    "correct": "n - (p+1) = 50 - 4 = 46 (n Beobachtungen minus Intercept und 3 Prädiktoren)",
                    "explanation": "Bei multipler Regression mit p Prädiktoren und Intercept hat man p+1 = 4 Parameter. Freiheitsgrade der Residuen: df = n - (p+1) = 50 - 4 = 46.",
                    "hint": "Freiheitsgrade = Beobachtungen - Anzahl geschätzter Parameter (Intercept + p Prädiktoren).",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                }
            ]
        },
        {
            "unit_id": "ch_v12_summary",
            "unit_type": "summary",
            "title": "Kapitel V12 abgeschlossen",
            "estimated_minutes": 1,
            "items": []
        }
    ]
}

# ═══════════════════════════════════════════════════════════════
# V13 – Regressionsdiagnose & Modellwahl
# ═══════════════════════════════════════════════════════════════
ch_v13 = {
    "chapter_id": "ch_v13",
    "title": "Regressionsdiagnose & Modellwahl",
    "description": "Residualanalyse, Cook's Distanz, AIC, step()",
    "lecture": "V13",
    "priority": "high",
    "unlocked": False,
    "completed": False,
    "units": [
        {
            "unit_id": "ch_v13_concept_0",
            "unit_type": "concept",
            "title": "Residualanalyse & Diagnoseplots",
            "estimated_minutes": 6,
            "items": [{
                "type": "concept_card",
                "title": "Die 4 Standard-Diagnoseplots: plot(model)",
                "content_html": "<p><code>plot(model)</code> erzeugt 4 Diagnoseplots:</p><table class='concept-table'><thead><tr><th>Plot</th><th>Prüft</th></tr></thead><tbody><tr><td>Residuals vs Fitted</td><td>Linearität & Homoskedastizität</td></tr><tr><td>Normal Q-Q</td><td>Normalverteilung der Residuen</td></tr><tr><td>Scale-Location</td><td>Konstante Varianz (Homoskedastizität)</td></tr><tr><td>Residuals vs Leverage</td><td>Einflussreiche Beobachtungen</td></tr></tbody></table><p>Ideal: Residuals vs Fitted zeigt keine Muster (zufällige Streuung um 0).</p>",
                "visual_type": "table",
                "key_takeaway": "plot(model) zeigt 4 Plots. Trichterform in Residuals vs Fitted → Heteroskedastizität. Abweichungen im Q-Q-Plot → Nicht-Normalität."
            }]
        },
        {
            "unit_id": "ch_v13_concept_1",
            "unit_type": "concept",
            "title": "Einflussreiche Beobachtungen",
            "estimated_minutes": 5,
            "items": [{
                "type": "concept_card",
                "title": "Hebelwerte & Cook's Distanz",
                "content_html": "<p><strong>Hebelwert (leverage)</strong>: Beobachtung mit extremem x-Wert — hat großen Einfluss auf die Regressionsgerade.</p><p><strong>Cook's Distanz D</strong>: Misst Einfluss einer Beobachtung auf <em>alle</em> Koeffizientenschätzungen. D > 1 gilt als problematisch.</p><div class='console-sim'><span class='prompt'>&gt;</span> hatvalues(model)   <span class='comment'># Hebelwerte</span><br><span class='prompt'>&gt;</span> cooks.distance(model)  <span class='comment'># Cook's D</span><br><span class='prompt'>&gt;</span> plot(model, which=4)  <span class='comment'># Cook's D als Plot</span></div>",
                "visual_type": "console",
                "key_takeaway": "Cook's Distanz > 1 → Beobachtung prüfen. Hoher Hebelwert allein ist noch kein Problem – erst wenn auch Residuum groß ist."
            }]
        },
        {
            "unit_id": "ch_v13_concept_2",
            "unit_type": "concept",
            "title": "AIC, BIC & Schrittweise Regression",
            "estimated_minutes": 6,
            "items": [{
                "type": "concept_card",
                "title": "Modellvergleich mit AIC und step()",
                "content_html": "<p><strong>AIC</strong> (Akaike Information Criterion): AIC = −2·logL + 2k — kleiner ist besser.</p><p><strong>BIC</strong>: BIC = −2·logL + k·ln(n) — bestraft stärker für viele Parameter.</p><div class='console-sim'><span class='prompt'>&gt;</span> AIC(model1, model2)<br><span class='output'>       df      AIC<br>model1  4  234.5<br>model2  6  231.2</span><br><span class='prompt'>&gt;</span> step(full_model, direction=\"backward\")<br><span class='comment'># Entfernt schrittweise Prädiktoren mit schlechtestem AIC</span></div>",
                "visual_type": "console",
                "key_takeaway": "Kleinerer AIC/BIC = besseres Modell. step() automatisiert Vorwärts-, Rückwärts- oder beidseitige Variablenselektion."
            }]
        },
        {
            "unit_id": "ch_v13_practice_1",
            "unit_type": "practice",
            "title": "Diagnose & Modellwahl – Praxistraining",
            "estimated_minutes": 20,
            "items": [
                {
                    "id": "ch_v13_q01",
                    "difficulty": 1, "priority": "high",
                    "type": "multiple_choice",
                    "context": "Du hast ein lineares Regressionsmodell angepasst.",
                    "question": "Welcher R-Befehl erzeugt die 4 Standard-Diagnoseplots?",
                    "code_snippet": None,
                    "options": ["plot(model)", "diagnostics(model)", "qqplot(residuals(model))", "plot(residuals(model))"],
                    "correct": "plot(model)",
                    "explanation": "plot() auf ein lm-Objekt erzeugt automatisch 4 Diagnoseplots: Residuals vs Fitted, Normal Q-Q, Scale-Location und Residuals vs Leverage.",
                    "hint": "R's plot() ist überladen: auf lm-Objekten erzeugt es speziell die 4 Diagnoseplots.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v13_q02",
                    "difficulty": 2, "priority": "high",
                    "type": "interpret_conclude",
                    "context": "Residuals vs Fitted Plot zeigt eine trichterförmig auseinanderlaufende Punktewolke.",
                    "question": "Was ist das Problem und wie nennt man es?",
                    "code_snippet": None,
                    "options": [
                        "Heteroskedastizität – die Varianz der Fehler nimmt mit den Fitted Values zu",
                        "Autokorrelation – die Residuen hängen voneinander ab",
                        "Multikollinearität – Prädiktoren korrelieren miteinander",
                        "Overfitting – das Modell ist zu komplex"
                    ],
                    "correct": "Heteroskedastizität – die Varianz der Fehler nimmt mit den Fitted Values zu",
                    "explanation": "Trichterform im Residuals vs Fitted Plot ist das klassische Zeichen für Heteroskedastizität: Die Streuung der Residuen ist nicht konstant, sondern wächst mit den vorhergesagten Werten. Lösungen: Log-Transformation der Zielvariable oder gewichtete Regression.",
                    "hint": "Konstante Varianz = Homoskedastizität. Nicht konstant = Hetero-skedastizität.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v13_q03",
                    "difficulty": 1, "priority": "high",
                    "type": "multiple_choice",
                    "context": "Du möchtest prüfen, ob eine Beobachtung einen unverhältnismäßig großen Einfluss auf die Schätzung hat.",
                    "question": "Welches Maß verwendest du?",
                    "code_snippet": None,
                    "options": ["Cook's Distanz", "R²", "VIF (Variance Inflation Factor)", "Standardfehler der Residuen"],
                    "correct": "Cook's Distanz",
                    "explanation": "Cook's Distanz misst, wie stark sich alle Koeffizientenschätzungen verändern würden, wenn man eine bestimmte Beobachtung weglässt. D > 1 gilt als Warnsignal.",
                    "hint": "Cook's Distanz heißt nach R.D. Cook und ist DAS Maß für Einflusspunkte.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v13_q04",
                    "difficulty": 2, "priority": "high",
                    "type": "code_output",
                    "context": "Du vergleichst zwei Modelle mit AIC.",
                    "question": "Welches Modell bevorzugst du?",
                    "code_snippet": "AIC(m1, m2)\n#        df      AIC\n# m1      4   312.8\n# m2      7   298.4",
                    "options": [
                        "m2 – kleinerer AIC trotz mehr Parametern",
                        "m1 – weniger Parameter sind immer besser",
                        "m2 – mehr Freiheitsgrade = mehr Information",
                        "Keines – AIC-Unterschied unter 20 ist bedeutungslos"
                    ],
                    "correct": "m2 – kleinerer AIC trotz mehr Parametern",
                    "explanation": "AIC: kleiner = besser. m2 hat AIC = 298.4 < 312.8, also ist m2 zu bevorzugen. Der AIC berücksichtigt bereits die Komplexität (Strafterm 2k). Eine Differenz von 14.4 ist substanziell.",
                    "hint": "AIC-Regel: kleiner = besser. Der Strafterm für Parameter ist schon eingerechnet.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v13_q05",
                    "difficulty": 2, "priority": "high",
                    "type": "multiple_choice",
                    "context": "Du verwendest step() zur automatischen Variablenselektion.",
                    "question": "Was macht step(full_model, direction='backward')?",
                    "code_snippet": None,
                    "options": [
                        "Startet mit vollem Modell, entfernt in jedem Schritt den Prädiktor mit schlechtestem AIC",
                        "Startet mit leerem Modell und fügt schrittweise Prädiktoren hinzu",
                        "Testet alle möglichen Modellkombinationen und wählt das beste",
                        "Skaliert die Prädiktoren rückwärts von groß nach klein"
                    ],
                    "correct": "Startet mit vollem Modell, entfernt in jedem Schritt den Prädiktor mit schlechtestem AIC",
                    "explanation": "Rückwärtsselektion (backward): Startet mit dem vollen Modell (alle Prädiktoren), entfernt in jedem Schritt den Prädiktor, dessen Wegfall den AIC am stärksten verbessert (oder am wenigsten verschlechtert). Endet wenn kein Entfernen mehr hilft.",
                    "hint": "backward = von groß nach klein. forward = von klein nach groß. both = beidseitig.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v13_q06",
                    "difficulty": 2, "priority": "medium",
                    "type": "multiple_choice",
                    "context": "Welches Kriterium bestraft stärker für viele Parameter?",
                    "question": "Vergleiche AIC und BIC.",
                    "code_snippet": None,
                    "options": [
                        "BIC – Strafterm ist k·ln(n) statt 2k, also größer wenn n > e² ≈ 7.4",
                        "AIC – Strafterm 2k wächst schneller als ln(n)",
                        "Beide bestrafen gleich stark",
                        "Das hängt nur von der Stichprobengröße n ab, ohne klares Muster"
                    ],
                    "correct": "BIC – Strafterm ist k·ln(n) statt 2k, also größer wenn n > e² ≈ 7.4",
                    "explanation": "AIC-Strafterm: 2k. BIC-Strafterm: k·ln(n). Für n > e² ≈ 7.4 (also praktisch immer) ist ln(n) > 2, sodass BIC stärker bestraft → wählt sparsamere Modelle.",
                    "hint": "ln(10) ≈ 2.3, ln(100) ≈ 4.6 – BIC bestraft mit wachsendem n immer stärker.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v13_q07",
                    "difficulty": 2, "priority": "medium",
                    "type": "interpret_conclude",
                    "context": "Normal Q-Q Plot der Residuen zeigt an den Rändern (Quantile < -2 und > 2) starke Abweichungen von der Diagonalen.",
                    "question": "Was schließt du daraus?",
                    "code_snippet": None,
                    "options": [
                        "Die Residuen sind nicht normalverteilt – die Verteilung hat schwere Ränder (heavy tails)",
                        "Das Modell hat Heteroskedastizität",
                        "Die Residuen sind perfekt normalverteilt",
                        "Das Modell hat Multikollinearität"
                    ],
                    "correct": "Die Residuen sind nicht normalverteilt – die Verteilung hat schwere Ränder (heavy tails)",
                    "explanation": "Im Q-Q-Plot liegen perfekt normalverteilte Residuen auf der Diagonalen. Abweichungen an den Rändern → Heavy Tails (oder Ausreißer). Das verletzt die Normalverteilungsannahme für t- und F-Tests.",
                    "hint": "Q-Q-Plot: Punkte auf Diagonale = Normalverteilung. Abweichungen an Rändern = Heavy Tails.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v13_q08",
                    "difficulty": 3, "priority": "medium",
                    "type": "multiple_choice",
                    "context": "VIF-Werte deines Modells:",
                    "question": "Was deutet auf ein Problem hin?",
                    "code_snippet": "vif(model)\n# x1   x2   x3\n# 1.3  1.8  12.4",
                    "options": [
                        "x3 – VIF > 10 deutet auf starke Multikollinearität hin",
                        "x1 – kleinster VIF = größtes Problem",
                        "Alle Prädiktoren – VIF > 1 ist immer problematisch",
                        "Keiner – VIF unter 15 ist akzeptabel"
                    ],
                    "correct": "x3 – VIF > 10 deutet auf starke Multikollinearität hin",
                    "explanation": "VIF (Variance Inflation Factor): VIF = 1 (keine Kollinearität), VIF > 5 (moderat), VIF > 10 (problematisch). x3 mit VIF = 12.4 korreliert stark mit anderen Prädiktoren → Schätzungen für x3 sind instabil.",
                    "hint": "Faustregel: VIF > 10 = starke Multikollinearität. car::vif(model) berechnet die Werte.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                }
            ]
        },
        {
            "unit_id": "ch_v13_summary",
            "unit_type": "summary",
            "title": "Kapitel V13 abgeschlossen",
            "estimated_minutes": 1,
            "items": []
        }
    ]
}

# ═══════════════════════════════════════════════════════════════
# V14 – Logistische Regression
# ═══════════════════════════════════════════════════════════════
ch_v14 = {
    "chapter_id": "ch_v14",
    "title": "Logistische Regression",
    "description": "Binäre Zielvariable, glm(), Odds Ratio, Konfusionsmatrix",
    "lecture": "V14",
    "priority": "high",
    "unlocked": False,
    "completed": False,
    "units": [
        {
            "unit_id": "ch_v14_concept_0",
            "unit_type": "concept",
            "title": "Wann logistische Regression?",
            "estimated_minutes": 5,
            "items": [{
                "type": "concept_card",
                "title": "Binäre Zielvariable – Problem mit linearer Regression",
                "content_html": "<p>Binäre Zielvariable: y ∈ {0, 1} (z.B. krank/gesund, Spam/Kein Spam, bestanden/nicht bestanden).</p><p>Lineare Regression ungeeignet: Vorhersagen können &gt; 1 oder &lt; 0 sein – keine Wahrscheinlichkeiten.</p><p><strong>Logistisches Modell</strong>: modelliert P(y=1|x) direkt als Wahrscheinlichkeit:</p><p style='text-align:center'><code>P(y=1|x) = 1 / (1 + e<sup>−η</sup>)</code> mit <code>η = β₀ + β₁x₁ + …</code></p><p>Die Logit-Transformation: <code>log(p / (1−p)) = η</code> ist linear in x.</p>",
                "visual_type": "text",
                "key_takeaway": "Logistische Regression für 0/1-Zielvariablen. Sie modelliert P(y=1|x) ∈ [0,1] – immer zwischen 0 und 1."
            }]
        },
        {
            "unit_id": "ch_v14_concept_1",
            "unit_type": "concept",
            "title": "glm() in R – Anpassung und summary()",
            "estimated_minutes": 6,
            "items": [{
                "type": "concept_card",
                "title": "glm() mit family=binomial",
                "content_html": "<div class='console-sim'><span class='prompt'>&gt;</span> model &lt;- glm(bestanden ~ Lernstunden + Vorerfahrung,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;family = binomial, data = df)<br><span class='prompt'>&gt;</span> summary(model)</div><p>Die Koeffizienten sind <strong>Log-Odds</strong>:</p><table class='concept-table'><thead><tr><th>Koeffizient</th><th>Bedeutung</th></tr></thead><tbody><tr><td>β̂₁ = 0.8</td><td>1 Std. mehr → Log-Odds steigen um 0.8</td></tr><tr><td>exp(0.8) ≈ 2.23</td><td>Odds Ratio: Odds verdoppeln sich mehr als</td></tr></tbody></table><p>Signifikanz: z-Wert und p-Wert statt t-Wert (asymptotisch).</p>",
                "visual_type": "console",
                "key_takeaway": "glm(y ~ x, family=binomial) für logistische Regression. Koeffizienten = Log-Odds, exp(β) = Odds Ratio."
            }]
        },
        {
            "unit_id": "ch_v14_concept_2",
            "unit_type": "concept",
            "title": "Vorhersage & Konfusionsmatrix",
            "estimated_minutes": 5,
            "items": [{
                "type": "concept_card",
                "title": "predict() und Klassifikationsgüte",
                "content_html": "<div class='console-sim'><span class='prompt'>&gt;</span> <span class='comment'># Wahrscheinlichkeiten</span><br><span class='prompt'>&gt;</span> p_hat &lt;- predict(model, type=\"response\")<br><span class='output'>[1] 0.23 0.81 0.67 0.12 …</span><br><span class='prompt'>&gt;</span> <span class='comment'># Klassifikation mit Schwellenwert 0.5</span><br><span class='prompt'>&gt;</span> y_pred &lt;- ifelse(p_hat &gt; 0.5, 1, 0)<br><span class='prompt'>&gt;</span> <span class='comment'># Konfusionsmatrix</span><br><span class='prompt'>&gt;</span> table(y_pred, df$bestanden)<br><span class='output'>       0   1<br>y=0   45   5<br>y=1    3  47</span></div><p>Accuracy = (45+47) / 100 = 0.92</p>",
                "visual_type": "console",
                "key_takeaway": "predict(model, type='response') gibt P(y=1|x). type='link' gibt den linearen Prädiktor η. Konfusionsmatrix mit table(pred, actual)."
            }]
        },
        {
            "unit_id": "ch_v14_practice_1",
            "unit_type": "practice",
            "title": "Logistische Regression – Praxistraining",
            "estimated_minutes": 20,
            "items": [
                {
                    "id": "ch_v14_q01",
                    "difficulty": 1, "priority": "high",
                    "type": "multiple_choice",
                    "context": "Du willst vorhersagen, ob eine Email Spam (1) oder kein Spam (0) ist.",
                    "question": "Welches Modell ist geeignet?",
                    "code_snippet": None,
                    "options": [
                        "glm(Spam ~ Woerter + Links, family=binomial, data=df)",
                        "lm(Spam ~ Woerter + Links, data=df)",
                        "aov(Spam ~ Woerter, data=df)",
                        "t.test(Spam ~ Links, data=df)"
                    ],
                    "correct": "glm(Spam ~ Woerter + Links, family=binomial, data=df)",
                    "explanation": "Für eine binäre Zielvariable (0/1) wird logistische Regression verwendet: glm() mit family=binomial. lm() ist für stetige Zielvariablen und könnte Werte außerhalb [0,1] liefern.",
                    "hint": "Binäre Zielvariable → logistische Regression → glm(..., family=binomial).",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v14_q02",
                    "difficulty": 1, "priority": "high",
                    "type": "code_output",
                    "context": "Du willst die Vorhersage-Wahrscheinlichkeiten aus einem logistischen Regressionsmodell erhalten.",
                    "question": "Welcher Befehl liefert P(y=1|x) für alle Beobachtungen?",
                    "code_snippet": "model <- glm(y ~ x, family=binomial, data=df)",
                    "options": [
                        "predict(model, type=\"response\")",
                        "predict(model, type=\"link\")",
                        "predict(model)",
                        "fitted(model, type=\"probability\")"
                    ],
                    "correct": "predict(model, type=\"response\")",
                    "explanation": "type='response' transformiert den linearen Prädiktor η durch die Sigmoid-Funktion zu P(y=1|x) ∈ [0,1]. type='link' gibt η direkt zurück (Log-Odds-Skala). fitted(model) ist äquivalent zu predict(..., type='response') ohne newdata.",
                    "hint": "response = Antwortskala = Wahrscheinlichkeit. link = Linkfunktionsskala = Log-Odds.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v14_q03",
                    "difficulty": 2, "priority": "high",
                    "type": "interpret_conclude",
                    "context": "summary(glm(...)) zeigt: Lernstunden Estimate = 0.65, exp(0.65) ≈ 1.92.",
                    "question": "Wie interpretierst du den Koeffizienten?",
                    "code_snippet": None,
                    "options": [
                        "Eine Stunde mehr Lernen erhöht die Odds zu bestehen um Faktor 1.92 (also +92%)",
                        "Eine Stunde mehr Lernen erhöht die Wahrscheinlichkeit zu bestehen um 65%",
                        "Eine Stunde mehr Lernen erhöht die Wahrscheinlichkeit zu bestehen um 1.92",
                        "Lernstunden sind nicht signifikant (p > 0.05)"
                    ],
                    "correct": "Eine Stunde mehr Lernen erhöht die Odds zu bestehen um Faktor 1.92 (also +92%)",
                    "explanation": "Koeffizienten in logistischer Regression sind Log-Odds. exp(β) = Odds Ratio. exp(0.65) ≈ 1.92: Odds steigen um 92% pro zusätzliche Lernstunde. Die Wahrscheinlichkeit selbst steigt nichtlinear – abhängig vom Ausgangswert.",
                    "hint": "Exp(Koeffizient) = Odds Ratio. Odds Ratio = 1.92 → Odds steigen um 92%.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v14_q04",
                    "difficulty": 2, "priority": "high",
                    "type": "multiple_choice",
                    "context": "Du klassifizierst mit Schwellenwert 0.5.",
                    "question": "Welcher Befehl erstellt die Konfusionsmatrix?",
                    "code_snippet": "p_hat <- predict(model, type=\"response\")",
                    "options": [
                        "table(ifelse(p_hat > 0.5, 1, 0), df$y)",
                        "confusionMatrix(p_hat, df$y)",
                        "matrix(p_hat > 0.5, df$y)",
                        "apply(p_hat, 1, function(p) p > 0.5)"
                    ],
                    "correct": "table(ifelse(p_hat > 0.5, 1, 0), df$y)",
                    "explanation": "ifelse(p_hat > 0.5, 1, 0) konvertiert Wahrscheinlichkeiten in Klassen (0 oder 1). table(vorhergesagt, tatsächlich) erzeugt die Konfusionsmatrix. confusionMatrix() ist im Paket 'caret', nicht in Basis-R.",
                    "hint": "Erst Wahrscheinlichkeit → Klasse (ifelse), dann Kreuz-Tabelle (table).",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v14_q05",
                    "difficulty": 1, "priority": "medium",
                    "type": "multiple_choice",
                    "context": None,
                    "question": "Was ist der Unterschied zwischen glm() und lm() in R?",
                    "code_snippet": None,
                    "options": [
                        "glm() unterstützt verschiedene Fehlerverteilungen (family); lm() nur Normalverteilung",
                        "glm() ist schneller als lm() für große Datensätze",
                        "lm() kann auch für logistische Regression genutzt werden",
                        "glm() verwendet immer den logit-Link, auch bei family=gaussian"
                    ],
                    "correct": "glm() unterstützt verschiedene Fehlerverteilungen (family); lm() nur Normalverteilung",
                    "explanation": "lm() ist der Spezialfall von glm() mit family=gaussian und identity-Link. glm() generalisiert auf beliebige Exponentialfamilien: binomial (Logistik), poisson (Zähldaten), gamma usw.",
                    "hint": "glm() = Generalized Linear Model. Das 'Generalized' bezieht sich auf die verschiedenen family-Optionen.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v14_q06",
                    "difficulty": 3, "priority": "high",
                    "type": "interpret_conclude",
                    "context": "Datensatz: 90% der Beobachtungen sind Klasse 0, 10% Klasse 1. Dein Modell hat Accuracy 0.91.",
                    "question": "Ist das Modell wirklich gut? Was ist das Problem?",
                    "code_snippet": None,
                    "options": [
                        "Nein – ein triviales Modell das immer 0 vorhersagt hätte bereits 90% Accuracy (Imbalanced Classes)",
                        "Ja – 91% Accuracy ist ausgezeichnet, das Modell funktioniert",
                        "Nein – bei logistischer Regression sollte Accuracy > 95% sein",
                        "Ja – 1% besser als Zufall ist statistisch signifikant"
                    ],
                    "correct": "Nein – ein triviales Modell das immer 0 vorhersagt hätte bereits 90% Accuracy (Imbalanced Classes)",
                    "explanation": "Bei stark unausgeglichenen Klassen (Imbalanced Data) ist Accuracy irreführend. Ein Modell das immer 0 vorhersagt hat schon 90% Accuracy. Besser: Sensitivität, Spezifität, F1-Score oder AUC/ROC.",
                    "hint": "Frage dich: Welche Accuracy hätte ein Modell, das immer die Mehrheitsklasse vorhersagt?",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v14_q07",
                    "difficulty": 2, "priority": "medium",
                    "type": "multiple_choice",
                    "context": "Du willst für ein logistisches Regressionsmodell zwei Varianten vergleichen.",
                    "question": "Welches Kriterium verwendest du für den Modellvergleich?",
                    "code_snippet": None,
                    "options": [
                        "AIC(model1, model2) – auch für glm()-Modelle verfügbar",
                        "R² – auch bei logistischer Regression das Hauptgütekriterium",
                        "F-Test – wie bei linearer Regression",
                        "RMSE – Root Mean Squared Error"
                    ],
                    "correct": "AIC(model1, model2) – auch für glm()-Modelle verfügbar",
                    "explanation": "AIC funktioniert für alle mit Maximum Likelihood geschätzten Modelle, also auch glm(). R² ist bei logistischer Regression nicht definiert (es gibt Pseudo-R²-Varianten). Der F-Test gilt nur für lineare Regression.",
                    "hint": "AIC basiert auf der Log-Likelihood – die gibt es auch bei logistischer Regression.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v14_q08",
                    "difficulty": 2, "priority": "medium",
                    "type": "code_output",
                    "context": "Logistisches Modell angepasst. Vorhersage für neuen Datenpunkt:",
                    "question": "Was gibt predict(model, newdata=data.frame(x=5), type='link') zurück?",
                    "code_snippet": None,
                    "options": [
                        "Den linearen Prädiktor η = β₀ + β₁·5 (Log-Odds, nicht Wahrscheinlichkeit)",
                        "Die Wahrscheinlichkeit P(y=1|x=5) ∈ [0,1]",
                        "Die vorhergesagte Klasse (0 oder 1)",
                        "Den Standardfehler der Vorhersage"
                    ],
                    "correct": "Den linearen Prädiktor η = β₀ + β₁·5 (Log-Odds, nicht Wahrscheinlichkeit)",
                    "explanation": "type='link' gibt den linearen Prädiktor η zurück – also den Wert vor der Sigmoid-Transformation. Um die Wahrscheinlichkeit zu erhalten: 1/(1+exp(-η)) oder predict(..., type='response').",
                    "hint": "link = Linkfunktion-Skala = Log-Odds. response = Antwortskala = Wahrscheinlichkeit.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "ch_v14_q09",
                    "difficulty": 3, "priority": "medium",
                    "type": "multiple_choice",
                    "context": "Konfusionsmatrix deines Modells:",
                    "question": "Wie hoch ist die Accuracy?",
                    "code_snippet": "#          tatsächlich\n# vorhergesagt  0   1\n#            0  40   8\n#            1   5  47",
                    "options": [
                        "(40+47) / (40+8+5+47) = 87/100 = 0.87",
                        "(40+47) / (40+47) = 1.0",
                        "47 / (47+8) = 0.855",
                        "40 / (40+5) = 0.889"
                    ],
                    "correct": "(40+47) / (40+8+5+47) = 87/100 = 0.87",
                    "explanation": "Accuracy = (TP + TN) / n_gesamt. TP = 47 (korrekt als 1 klassifiziert), TN = 40 (korrekt als 0). FP = 5, FN = 8. n = 40+8+5+47 = 100. Accuracy = 87/100 = 0.87.",
                    "hint": "Accuracy = richtig klassifiziert / gesamt. Richtig = Diagonale der Konfusionsmatrix.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                }
            ]
        },
        {
            "unit_id": "ch_v14_summary",
            "unit_type": "summary",
            "title": "Kapitel V14 abgeschlossen",
            "estimated_minutes": 1,
            "items": []
        }
    ]
}

# ═══════════════════════════════════════════════════════════════
# Klausur-Simulation 1 – Original (exakt K1 aus Klausurübungsaufgaben)
# ═══════════════════════════════════════════════════════════════
DF_X_SNIPPET = """> X
  Stadt  BL Einw
1     A Nds   70
2     B Bay   50
3     C Bay  120
4     D Sac   90
5     E Nds  110
6     F Sac   90
7     G Bay   60"""

K1_CONTEXT = "Klausur-Simulation K1 – DataFrame X (Stadt, BL, Einw)"

klausur1_units = [
    {
        "unit_id": "ch_klausur1_concept",
        "unit_type": "concept",
        "title": "Aufgabe K1 – Hinweise und DataFrame",
        "estimated_minutes": 3,
        "items": [{
            "type": "concept_card",
            "title": "Klausur K1 – DataFrame X",
            "content_html": "<p>Gegeben ist der folgende DataFrame X mit Städten, Bundesländern und Einwohnerzahl (in Tausend):</p><div class='console-sim'>&gt; X<br>&nbsp; Stadt&nbsp;&nbsp;BL Einw<br>1&nbsp;&nbsp;&nbsp;&nbsp; A Nds&nbsp;&nbsp; 70<br>2&nbsp;&nbsp;&nbsp;&nbsp; B Bay&nbsp;&nbsp; 50<br>3&nbsp;&nbsp;&nbsp;&nbsp; C Bay&nbsp;&nbsp;120<br>4&nbsp;&nbsp;&nbsp;&nbsp; D Sac&nbsp;&nbsp; 90<br>5&nbsp;&nbsp;&nbsp;&nbsp; E Nds&nbsp;&nbsp;110<br>6&nbsp;&nbsp;&nbsp;&nbsp; F Sac&nbsp;&nbsp; 90<br>7&nbsp;&nbsp;&nbsp;&nbsp; G Bay&nbsp;&nbsp; 60</div><p>Für jede der folgenden Teilaufgaben: Berechne im Kopf, was R ausgeben würde.</p>",
            "visual_type": "console",
            "key_takeaway": "Strategien: DF[i,j] → Zeile i, Spalte j. Negativer Index schließt aus. order() sortiert aufsteigend."
        }]
    },
    {
        "unit_id": "ch_klausur1_practice",
        "unit_type": "practice",
        "title": "K1 – Alle Teilaufgaben",
        "estimated_minutes": 25,
        "items": [
            {
                "id": "klausur1_qa",
                "difficulty": 1, "priority": "high",
                "type": "interpret_conclude",
                "context": K1_CONTEXT,
                "question": "a) Was gibt X[3,] aus?",
                "code_snippet": None,
                "console_output": DF_X_SNIPPET + "\n> X[3,]",
                "options": [
                    "  Stadt  BL Einw\n3     C Bay  120",
                    "  Stadt  BL Einw\n3     B Bay   50",
                    "[1] \"C\" \"Bay\" 120",
                    "  Stadt  BL Einw\n3     D Sac   90"
                ],
                "correct": "  Stadt  BL Einw\n3     C Bay  120",
                "explanation": "X[3,] selektiert die gesamte 3. Zeile. Zeile 3: Stadt=C, BL=Bay, Einw=120. R behält die Zeilennummer (3) als Zeilenname.",
                "hint": "X[i,] = gesamte Zeile i mit allen Spalten.",
                "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "klausur1_qb",
                "difficulty": 2, "priority": "high",
                "type": "interpret_conclude",
                "context": K1_CONTEXT,
                "question": "b) Was gibt X[seq(2, nrow(X), 3), 1] aus?",
                "code_snippet": None,
                "console_output": DF_X_SNIPPET + "\n> X[seq(2,nrow(X),3),1]",
                "options": [
                    "[1] \"B\" \"E\"",
                    "[1] \"B\" \"C\" \"D\" \"E\"",
                    "[1] 2 5",
                    "[1] \"A\" \"D\" \"G\""
                ],
                "correct": "[1] \"B\" \"E\"",
                "explanation": "seq(2, 7, 3) = c(2, 5). X[c(2,5), 1] selektiert Spalte 1 (Stadt) der Zeilen 2 und 5 → \"B\" und \"E\".",
                "hint": "seq(from, to, by): seq(2,7,3) ergibt c(2,5). Dann Spalte 1 (Stadt) dieser Zeilen.",
                "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "klausur1_qc",
                "difficulty": 1, "priority": "high",
                "type": "interpret_conclude",
                "context": K1_CONTEXT,
                "question": "c) Was gibt X[nrow(X), ncol(X)] aus?",
                "code_snippet": None,
                "console_output": DF_X_SNIPPET + "\n> X[nrow(X),ncol(X)]",
                "options": ["[1] 60", "[1] 90", "[1] \"G\"", "[1] 7"],
                "correct": "[1] 60",
                "explanation": "nrow(X)=7, ncol(X)=3. X[7,3] = Zeile 7, Spalte 3 (Einw) = 60.",
                "hint": "nrow(X) = 7 (letzte Zeile), ncol(X) = 3 (letzte Spalte = Einw).",
                "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "klausur1_qd",
                "difficulty": 2, "priority": "high",
                "type": "interpret_conclude",
                "context": K1_CONTEXT,
                "question": "d) Was gibt X[-c(1,2,4,5), 2:3] aus?",
                "code_snippet": None,
                "console_output": DF_X_SNIPPET + "\n> X[-c(1,2,4,5),2:3]",
                "options": [
                    "   BL Einw\n3 Bay  120\n6 Sac   90\n7 Bay   60",
                    "   BL Einw\n1 Nds   70\n3 Bay  120",
                    "   BL Einw\n3 Bay  120\n4 Sac   90",
                    "  Stadt  BL\n3     C Bay\n6     F Sac"
                ],
                "correct": "   BL Einw\n3 Bay  120\n6 Sac   90\n7 Bay   60",
                "explanation": "-c(1,2,4,5) schließt Zeilen 1,2,4,5 aus → verbleiben Zeilen 3,6,7. 2:3 = Spalten BL und Einw.",
                "hint": "Negativer Index schließt aus. 7 Zeilen minus 4 = 3 übrig: Zeilen 3, 6, 7.",
                "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "klausur1_qe",
                "difficulty": 1, "priority": "medium",
                "type": "interpret_conclude",
                "context": K1_CONTEXT,
                "question": "e) Was gibt apply(X, 2, length) aus?",
                "code_snippet": None,
                "console_output": DF_X_SNIPPET + "\n> apply(X,2,length)",
                "options": [
                    "Stadt    BL  Einw \n    7     7     7",
                    "[1] 3",
                    "[1] 7",
                    "Stadt    BL  Einw \n    1     1     1"
                ],
                "correct": "Stadt    BL  Einw \n    7     7     7",
                "explanation": "MARGIN=2 → über Spalten iterieren. length() jeder Spalte = Anzahl Zeilen = 7. Ergebnis: benannter Vektor mit 7 für jede der 3 Spalten.",
                "hint": "apply(X, 2, f) wendet f auf jede Spalte an. length() einer Spalte = nrow(X) = 7.",
                "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "klausur1_qf",
                "difficulty": 2, "priority": "high",
                "type": "interpret_conclude",
                "context": K1_CONTEXT,
                "question": "f) Was gibt X[order(X$Einw),]$Stadt aus?",
                "code_snippet": None,
                "console_output": DF_X_SNIPPET + "\n> X[order(X$Einw),]$Stadt",
                "options": [
                    "[1] \"B\" \"G\" \"A\" \"D\" \"F\" \"E\" \"C\"",
                    "[1] \"C\" \"E\" \"D\" \"F\" \"A\" \"G\" \"B\"",
                    "[1] \"A\" \"B\" \"C\" \"D\" \"E\" \"F\" \"G\"",
                    "[1] \"B\" \"G\" \"A\" \"F\" \"D\" \"E\" \"C\""
                ],
                "correct": "[1] \"B\" \"G\" \"A\" \"D\" \"F\" \"E\" \"C\"",
                "explanation": "order() sortiert aufsteigend nach Einw: 50(B), 60(G), 70(A), 90(D), 90(F), 110(E), 120(C). Bei Gleichstand (D und F: beide 90) bleibt die ursprüngliche Reihenfolge erhalten.",
                "hint": "order(X$Einw) gibt Indizes in aufsteigender Reihenfolge. Dann $Stadt extrahiert den Stadtnamen.",
                "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "klausur1_qg",
                "difficulty": 2, "priority": "high",
                "type": "interpret_conclude",
                "context": K1_CONTEXT,
                "question": "g) Was gibt sum(X[X$Einw > 100, 3]) aus?",
                "code_snippet": None,
                "console_output": DF_X_SNIPPET + "\n> sum(X[X$Einw>100,3])",
                "options": ["[1] 230", "[1] 2", "[1] 120", "[1] 110"],
                "correct": "[1] 230",
                "explanation": "X$Einw > 100 → Zeilen mit Einw > 100: C(120) und E(110). Spalte 3 (Einw): c(120, 110). sum = 230.",
                "hint": "Erst Boolesche Indizierung: Einw > 100. Dann Spalte 3. Dann sum().",
                "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "klausur1_qh",
                "difficulty": 3, "priority": "high",
                "type": "interpret_conclude",
                "context": K1_CONTEXT,
                "question": "h) Was gibt aggregate(X$Einw ~ X$BL, FUN=min) aus?",
                "code_snippet": None,
                "console_output": DF_X_SNIPPET + "\n> aggregate(X$Einw~X$BL, FUN=min)",
                "options": [
                    "  X$BL X$Einw\n1  Bay     50\n2  Nds     70\n3  Sac     90",
                    "  X$BL X$Einw\n1  Bay    120\n2  Nds    110\n3  Sac     90",
                    "  X$BL X$Einw\n1  Bay     77\n2  Nds     90\n3  Sac     90",
                    "  X$BL X$Einw\n1  Bay      3\n2  Nds      2\n3  Sac      2"
                ],
                "correct": "  X$BL X$Einw\n1  Bay     50\n2  Nds     70\n3  Sac     90",
                "explanation": "aggregate gruppiert X$Einw nach X$BL und wendet min() an. Bay: min(50,120,60)=50. Nds: min(70,110)=70. Sac: min(90,90)=90. Gruppen alphabetisch sortiert.",
                "hint": "aggregate(y ~ gruppe, FUN=f) wendet f auf y für jede Gruppe an. Alphabetische Sortierung der Gruppen.",
                "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "klausur1_qfunc",
                "difficulty": 2, "priority": "high",
                "type": "interpret_conclude",
                "context": "Klausur K1g – Funktion auf DataFrame",
                "question": "Was macht f(X, c(3,1,2))?",
                "code_snippet": "f <- function(Y, rf) return(Y[, rf])",
                "console_output": None,
                "options": [
                    "Gibt X mit Spalten in Reihenfolge Einw, Stadt, BL zurück (Spalten 3,1,2 neu geordnet)",
                    "Gibt die Zeilen 3, 1, 2 von X zurück",
                    "Gibt einen Fehler zurück",
                    "Gibt nur die 3. Spalte (Einw) zurück"
                ],
                "correct": "Gibt X mit Spalten in Reihenfolge Einw, Stadt, BL zurück (Spalten 3,1,2 neu geordnet)",
                "explanation": "Y[, rf] selektiert Spalten per Indexvektor rf=c(3,1,2): erst Spalte 3 (Einw), dann 1 (Stadt), dann 2 (BL). Ergebnis: DataFrame mit umgeordneten Spalten.",
                "hint": "Y[, rf] mit Vektor rf selektiert Spalten in angegebener Reihenfolge.",
                "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "klausur1_quniq",
                "difficulty": 3, "priority": "high",
                "type": "mini_challenge",
                "context": "Klausur K1h – Funktion schreiben",
                "question": "Schreibe uniq(x): gibt die sortierte Wertemenge von x zurück (jeder Wert nur einmal). Nur Basis-R.",
                "code_snippet": "# Ziel:\n# uniq(c(6,4,3,6,1,4,4,3,6))  →  [1] 1 3 4 6\n\n# Variante 1 (elegant):\nuniq <- function(x) {\n  _____( unique(x) )\n}\n\n# Variante 2 (mit Schleife):\nuniq <- function(x) {\n  result <- c()\n  for (val in sort(x)) {\n    if (!(val %in% result)) {\n      result <- c(result, val)\n    }\n  }\n  return(result)\n}",
                "options": [],
                "correct": "sort",
                "correct_pattern": "sort",
                "explanation": "Variante 1: sort(unique(x)) — unique() entfernt Duplikate, sort() sortiert aufsteigend. Variante 2: Schleife über sort(x), nur hinzufügen wenn val noch nicht in result ist.",
                "hint": "Zwei Schritte: (1) Duplikate entfernen mit unique(), (2) sortieren mit sort().",
                "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
            }
        ]
    },
    {
        "unit_id": "ch_klausur1_summary",
        "unit_type": "summary",
        "title": "Klausur-Simulation 1 abgeschlossen",
        "estimated_minutes": 1,
        "items": []
    }
]

# ═══════════════════════════════════════════════════════════════
# Klausur-Simulation 2 – Variante mit anderem DataFrame Z
# ═══════════════════════════════════════════════════════════════
DF_Z_SNIPPET = """> Z
  Artikel   Kat Preis
1       A  Elek   299
2       B  Mode   149
3       C  Elek   499
4       D Sport   199
5       E  Mode   129
6       F Sport   249
7       G  Elek   179"""

K2_CONTEXT = "Klausur-Simulation K2 – DataFrame Z (Artikel, Kat, Preis)"

ch_klausur2 = {
    "chapter_id": "ch_klausur2",
    "title": "Klausur-Simulation 2 – Variante",
    "description": "Gleiche Aufgabentypen wie K1, andere Werte zum Üben",
    "lecture": "–",
    "priority": "high",
    "unlocked": False,
    "completed": False,
    "units": [
        {
            "unit_id": "ch_klausur2_concept",
            "unit_type": "concept",
            "title": "Aufgabe K2 – Hinweise und DataFrame Z",
            "estimated_minutes": 3,
            "items": [{
                "type": "concept_card",
                "title": "Klausur K2 – DataFrame Z (Variante mit anderen Werten)",
                "content_html": "<p>Gleiche Aufgabenstruktur wie K1, aber ein anderer DataFrame. Übe mit frischen Zahlen!</p><div class='console-sim'>&gt; Z<br>&nbsp; Artikel&nbsp;&nbsp;&nbsp;Kat Preis<br>1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;&nbsp;Elek&nbsp;&nbsp; 299<br>2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B&nbsp;&nbsp;Mode&nbsp;&nbsp; 149<br>3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C&nbsp;&nbsp;Elek&nbsp;&nbsp; 499<br>4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D&nbsp;Sport&nbsp;&nbsp; 199<br>5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E&nbsp;&nbsp;Mode&nbsp;&nbsp; 129<br>6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F&nbsp;Sport&nbsp;&nbsp; 249<br>7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G&nbsp;&nbsp;Elek&nbsp;&nbsp; 179</div><p>Spalten: Artikel (chr), Kat (chr: Elek/Mode/Sport), Preis (int, in Euro)</p>",
                "visual_type": "console",
                "key_takeaway": "Gleiche R-Befehle, neue Daten. Wenn du K1 beherrschst, schaffst du auch K2."
            }]
        },
        {
            "unit_id": "ch_klausur2_practice",
            "unit_type": "practice",
            "title": "K2 – Alle Teilaufgaben",
            "estimated_minutes": 25,
            "items": [
                {
                    "id": "klausur2_qa",
                    "difficulty": 1, "priority": "high",
                    "type": "interpret_conclude",
                    "context": K2_CONTEXT,
                    "question": "a) Was gibt Z[4,] aus?",
                    "code_snippet": None,
                    "console_output": DF_Z_SNIPPET + "\n> Z[4,]",
                    "options": [
                        "  Artikel   Kat Preis\n4       D Sport   199",
                        "  Artikel   Kat Preis\n4       C  Elek   499",
                        "[1] \"D\" \"Sport\" 199",
                        "  Artikel   Kat Preis\n4       E  Mode   129"
                    ],
                    "correct": "  Artikel   Kat Preis\n4       D Sport   199",
                    "explanation": "Z[4,] selektiert die gesamte 4. Zeile. Zeile 4: Artikel=D, Kat=Sport, Preis=199.",
                    "hint": "Z[i,] = gesamte Zeile i mit allen Spalten.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "klausur2_qb",
                    "difficulty": 2, "priority": "high",
                    "type": "interpret_conclude",
                    "context": K2_CONTEXT,
                    "question": "b) Was gibt Z[seq(2, nrow(Z), 2), 1] aus?",
                    "code_snippet": None,
                    "console_output": DF_Z_SNIPPET + "\n> Z[seq(2,nrow(Z),2),1]",
                    "options": [
                        "[1] \"B\" \"D\" \"F\"",
                        "[1] \"A\" \"C\" \"E\" \"G\"",
                        "[1] 2 4 6",
                        "[1] \"B\" \"C\" \"D\""
                    ],
                    "correct": "[1] \"B\" \"D\" \"F\"",
                    "explanation": "seq(2, 7, 2) = c(2, 4, 6). Z[c(2,4,6), 1] selektiert Spalte 1 (Artikel) der Zeilen 2, 4, 6 → \"B\", \"D\", \"F\".",
                    "hint": "seq(from=2, to=7, by=2) = c(2,4,6). Dann Spalte 1 (Artikel).",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "klausur2_qc",
                    "difficulty": 1, "priority": "high",
                    "type": "interpret_conclude",
                    "context": K2_CONTEXT,
                    "question": "c) Was gibt Z[1, ncol(Z)] aus?",
                    "code_snippet": None,
                    "console_output": DF_Z_SNIPPET + "\n> Z[1,ncol(Z)]",
                    "options": ["[1] 299", "[1] 499", "[1] \"A\"", "[1] 7"],
                    "correct": "[1] 299",
                    "explanation": "ncol(Z)=3. Z[1,3] = Zeile 1, Spalte 3 (Preis) = 299 (Artikel A, Kategorie Elek).",
                    "hint": "ncol(Z) = 3 (Spalte 3 = Preis). Zeile 1 hat Preis = 299.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "klausur2_qd",
                    "difficulty": 2, "priority": "high",
                    "type": "interpret_conclude",
                    "context": K2_CONTEXT,
                    "question": "d) Was gibt Z[-c(1, 3, 5, 7), 2:3] aus?",
                    "code_snippet": None,
                    "console_output": DF_Z_SNIPPET + "\n> Z[-c(1,3,5,7),2:3]",
                    "options": [
                        "     Kat Preis\n2   Mode   149\n4  Sport   199\n6  Sport   249",
                        "     Kat Preis\n1   Elek   299\n3   Elek   499",
                        "  Artikel   Kat\n2       B  Mode\n4       D Sport",
                        "     Kat Preis\n2   Mode   149\n4  Sport   199"
                    ],
                    "correct": "     Kat Preis\n2   Mode   149\n4  Sport   199\n6  Sport   249",
                    "explanation": "-c(1,3,5,7) schließt Zeilen 1,3,5,7 aus → verbleiben Zeilen 2,4,6. 2:3 = Spalten Kat und Preis.",
                    "hint": "Ausgeschlossen: ungerade Zeilen 1,3,5,7. Übrig: Zeilen 2,4,6. Spalten 2:3 = Kat und Preis.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "klausur2_qe",
                    "difficulty": 1, "priority": "medium",
                    "type": "interpret_conclude",
                    "context": K2_CONTEXT,
                    "question": "e) Was gibt apply(Z, 2, length) aus?",
                    "code_snippet": None,
                    "console_output": DF_Z_SNIPPET + "\n> apply(Z,2,length)",
                    "options": [
                        "Artikel     Kat   Preis \n      7       7       7",
                        "[1] 3",
                        "[1] 7",
                        "Artikel     Kat   Preis \n      1       1       1"
                    ],
                    "correct": "Artikel     Kat   Preis \n      7       7       7",
                    "explanation": "MARGIN=2 → über Spalten iterieren. length() jeder Spalte = nrow(Z) = 7. Ergebnis: benannter Vektor mit 7 für jede der 3 Spalten.",
                    "hint": "apply(Z, 2, length) wendet length() auf jede Spalte an. Jede Spalte hat 7 Einträge.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "klausur2_qf",
                    "difficulty": 2, "priority": "high",
                    "type": "interpret_conclude",
                    "context": K2_CONTEXT,
                    "question": "f) Was gibt Z[order(Z$Preis),]$Artikel aus?",
                    "code_snippet": None,
                    "console_output": DF_Z_SNIPPET + "\n> Z[order(Z$Preis),]$Artikel",
                    "options": [
                        "[1] \"E\" \"B\" \"G\" \"D\" \"F\" \"A\" \"C\"",
                        "[1] \"C\" \"A\" \"F\" \"D\" \"G\" \"B\" \"E\"",
                        "[1] \"A\" \"B\" \"C\" \"D\" \"E\" \"F\" \"G\"",
                        "[1] \"E\" \"B\" \"G\" \"F\" \"D\" \"A\" \"C\""
                    ],
                    "correct": "[1] \"E\" \"B\" \"G\" \"D\" \"F\" \"A\" \"C\"",
                    "explanation": "order(Z$Preis) sortiert aufsteigend: 129(E), 149(B), 179(G), 199(D), 249(F), 299(A), 499(C). $Artikel gibt die Artikel in dieser Reihenfolge.",
                    "hint": "Sortiere die Preise aufsteigend und lies die Artikel ab: 129→E, 149→B, 179→G, 199→D, 249→F, 299→A, 499→C.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "klausur2_qg",
                    "difficulty": 2, "priority": "high",
                    "type": "interpret_conclude",
                    "context": K2_CONTEXT,
                    "question": "g) Was gibt sum(Z[Z$Preis > 200, 3]) aus?",
                    "code_snippet": None,
                    "console_output": DF_Z_SNIPPET + "\n> sum(Z[Z$Preis>200,3])",
                    "options": ["[1] 1047", "[1] 3", "[1] 499", "[1] 796"],
                    "correct": "[1] 1047",
                    "explanation": "Z$Preis > 200 → Zeilen mit Preis > 200: A(299), C(499), F(249). Spalte 3 (Preis): c(299, 499, 249). sum = 1047.",
                    "hint": "Preis > 200: welche Artikel erfüllen das? A(299)✓, B(149)✗, C(499)✓, D(199)✗, E(129)✗, F(249)✓, G(179)✗.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "klausur2_qh",
                    "difficulty": 3, "priority": "high",
                    "type": "interpret_conclude",
                    "context": K2_CONTEXT,
                    "question": "h) Was gibt aggregate(Z$Preis ~ Z$Kat, FUN=max) aus?",
                    "code_snippet": None,
                    "console_output": DF_Z_SNIPPET + "\n> aggregate(Z$Preis~Z$Kat, FUN=max)",
                    "options": [
                        "  Z$Kat Z$Preis\n1  Elek     499\n2  Mode     149\n3 Sport     249",
                        "  Z$Kat Z$Preis\n1  Elek     179\n2  Mode     129\n3 Sport     199",
                        "  Z$Kat Z$Preis\n1  Elek     325\n2  Mode     139\n3 Sport     224",
                        "  Z$Kat Z$Preis\n1 Sport     249\n2  Elek     499\n3  Mode     149"
                    ],
                    "correct": "  Z$Kat Z$Preis\n1  Elek     499\n2  Mode     149\n3 Sport     249",
                    "explanation": "aggregate gruppiert Z$Preis nach Z$Kat und wendet max() an. Elek: max(299,499,179)=499. Mode: max(149,129)=149. Sport: max(199,249)=249. Alphabetisch: Elek, Mode, Sport.",
                    "hint": "aggregate(y~gruppe, FUN=max) gibt das Maximum pro Gruppe. Gruppen alphabetisch: Elek < Mode < Sport.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "klausur2_qfunc",
                    "difficulty": 2, "priority": "high",
                    "type": "interpret_conclude",
                    "context": "Klausur K2g – Funktion auf DataFrame",
                    "question": "Was gibt g(Z, 3) zurück?",
                    "code_snippet": "g <- function(df, n) return(df[order(df$Preis), ][1:n, ])",
                    "console_output": DF_Z_SNIPPET,
                    "options": [
                        "Die 3 günstigsten Artikel: E(129), B(149), G(179)",
                        "Die 3 teuersten Artikel: C(499), A(299), F(249)",
                        "Artikel an Position 3: C Elek 499",
                        "Einen Fehler, da n kein Spaltenname ist"
                    ],
                    "correct": "Die 3 günstigsten Artikel: E(129), B(149), G(179)",
                    "explanation": "df[order(df$Preis),] sortiert Z aufsteigend nach Preis. [1:n,] = [1:3,] gibt die ersten 3 Zeilen zurück: E(129), B(149), G(179).",
                    "hint": "Erst aufsteigend nach Preis sortieren, dann die ersten n Zeilen nehmen.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                },
                {
                    "id": "klausur2_qfuncs",
                    "difficulty": 3, "priority": "high",
                    "type": "mini_challenge",
                    "context": "Klausur K2h – Funktion schreiben",
                    "question": "Schreibe filter_pos(x, s): gibt alle Werte aus x zurück, die größer als s sind. Nur Vektorindizierung, kein Filter/subset.",
                    "code_snippet": "# Ziel:\n# filter_pos(c(3,7,1,5,9,2), 4)  →  [1] 7 5 9\n\nfilter_pos <- function(x, s) {\n  return( x[ _____ ] )\n}",
                    "options": [],
                    "correct": "x > s",
                    "correct_pattern": "x > s",
                    "explanation": "x[x > s] verwendet einen logischen Vektor zur Indizierung: x > s ergibt TRUE/FALSE für jedes Element, x[...] behält nur die TRUE-Positionen. Ergebnis: alle Elemente von x die größer als s sind.",
                    "hint": "Boolescher Index: x[bedingung] behält alle Elemente wo bedingung TRUE ist. Bedingung: x > s.",
                    "visual": None, "times_seen": 0, "times_correct": 0, "last_result": None
                }
            ]
        },
        {
            "unit_id": "ch_klausur2_summary",
            "unit_type": "summary",
            "title": "Klausur-Simulation 2 abgeschlossen",
            "estimated_minutes": 1,
            "items": []
        }
    ]
}

# ═══════════════════════════════════════════════════════════════
# Einfügen in content.json
# ═══════════════════════════════════════════════════════════════
idx_ch16 = next(i for i, c in enumerate(data['chapters']) if c['chapter_id'] == 'ch16')

# V12, V13, V14 vor ch16 einfügen
data['chapters'].insert(idx_ch16, ch_v12)
data['chapters'].insert(idx_ch16 + 1, ch_v13)
data['chapters'].insert(idx_ch16 + 2, ch_v14)

# ch16 (now at idx_ch16+3) → Klausur Sim 1
ch16 = data['chapters'][idx_ch16 + 3]
ch16['title'] = 'Klausur-Simulation 1 – Original'
ch16['description'] = 'Aufgabe K1 aus den Klausurübungsaufgaben – exakt wie in der Prüfung'
ch16['lecture'] = '–'
ch16['priority'] = 'high'
ch16['coming_soon'] = False
ch16['units'] = klausur1_units

# Klausur Sim 2 am Ende anhängen
data['chapters'].append(ch_klausur2)

with open('/Users/maxim/Documents/Studium/COMSTATISTIK/statr/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Bericht
total_q = sum(
    1 for ch in data['chapters']
    for u in ch['units']
    for i in u.get('items', [])
    if i.get('type') != 'concept_card'
)
new_chs = ['ch_v12','ch_v13','ch_v14','ch16 (Klausur1)','ch_klausur2']
print(f"Fertig! {len(new_chs)} neue Kapitel hinzugefügt: {', '.join(new_chs)}")
print(f"Gesamte Fragen jetzt: {total_q}")
for ch in data['chapters']:
    print(f"  {ch['chapter_id']}: {ch['title']}")
