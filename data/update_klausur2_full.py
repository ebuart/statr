import json

with open('/Users/maxim/Documents/Studium/COMSTATISTIK/statr/data/content.json', encoding='utf-8') as f:
    data = json.load(f)

# K2 Variante ────────────────────────────────────────────────────────────────
CODE_K2V = """g <- function(n) {
  x <- runif(n, 0, 10)
  return(sum(x))
}
m <- 2000
y <- replicate(m, g(6))
mean(y > 30)"""

k2v_unit = {
    "unit_id": "ch_k2_v2",
    "unit_type": "practice",
    "title": "K2-Variante – Monte-Carlo-Simulation",
    "estimated_minutes": 10,
    "items": [
        {
            "id": "kv2_k2a", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K2 Variante – Monte-Carlo",
            "question": "Was macht g(6) in diesem Code?",
            "code_snippet": CODE_K2V, "console_output": None,
            "options": [
                "Zieht 6 Zufallszahlen aus U[0,10] und gibt ihre Summe zurück",
                "Gibt 6 gleichverteilte Werte zwischen 0 und 1 zurück",
                "Berechnet den Mittelwert von 6 Zufallszahlen",
                "Wiederholt runif(n,0,10) genau 6 Mal"
            ],
            "correct": "Zieht 6 Zufallszahlen aus U[0,10] und gibt ihre Summe zurück",
            "explanation": "runif(6, 0, 10): 6 Zufallszahlen aus U[0,10]. sum() gibt deren Summe zurück.",
            "hint": "n=6 → 6 Werte. sum() summiert.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "kv2_k2b", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K2 Variante – Monte-Carlo",
            "question": "Was schätzt mean(y > 30)?",
            "code_snippet": CODE_K2V, "console_output": None,
            "options": [
                "P(Summe von 6 U[0,10] > 30) – Wahrscheinlichkeit dass die Summe den Erwartungswert übersteigt",
                "Den Mittelwert aller y-Werte die größer als 30 sind",
                "Die Anzahl der Simulationen mit y > 30",
                "Den Erwartungswert der Summe"
            ],
            "correct": "P(Summe von 6 U[0,10] > 30) – Wahrscheinlichkeit dass die Summe den Erwartungswert übersteigt",
            "explanation": "mean(y > 30) = Anteil der 2000 Simulationen mit Summe > 30. Das ist die MC-Schätzung für P(Summe > 30).",
            "hint": "mean(logisch) = Anteil TRUE. y > 30 ist TRUE/FALSE.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "kv2_k2c", "difficulty": 3, "priority": "medium",
            "type": "multiple_choice",
            "context": "Klausur K2 Variante – Erwartungswert",
            "question": "Was ist der Erwartungswert von g(6) = sum(runif(6, 0, 10))?",
            "code_snippet": None, "console_output": None,
            "options": ["30", "60", "15", "5"],
            "correct": "30",
            "explanation": "E[U[0,10]] = (0+10)/2 = 5. Summe von 6 solchen: E = 6 × 5 = 30. mean(y > 30) schätzt also P(X > E[X]) ≈ 0.5.",
            "hint": "E[Uniform(a,b)] = (a+b)/2.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "kv2_k2d", "difficulty": 2, "priority": "high",
            "type": "multiple_choice",
            "context": "Klausur K2 Variante – Präzision",
            "question": "Ist die Schätzung mit m=2000 genauer als mit m=1000? Warum?",
            "code_snippet": None, "console_output": None,
            "options": [
                "Ja – mehr Simulationen → kleinerer Standardfehler des MC-Schätzers ∝ 1/√m",
                "Nein – die Genauigkeit hängt nur von der Verteilung ab, nicht von m",
                "Ja – aber nur wenn runif() einen anderen Seed verwendet",
                "Nein – ab m=1000 konvergiert der Schätzer bereits vollständig"
            ],
            "correct": "Ja – mehr Simulationen → kleinerer Standardfehler des MC-Schätzers ∝ 1/√m",
            "explanation": "Standardfehler des MC-Schätzers ∝ 1/√m. Mit m=2000 statt m=1000: Fehler um Faktor 1/√2 ≈ 0.71 kleiner. Mehr Simulationen = genauere Näherung.",
            "hint": "Wie verändert sich der Standardfehler eines Mittelwerts mit wachsendem n?", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        }
    ]
}

# K3 Variante ────────────────────────────────────────────────────────────────
k3v_unit = {
    "unit_id": "ch_k3_v2",
    "unit_type": "practice",
    "title": "K3-Variante – Chi-squared & ANOVA",
    "estimated_minutes": 10,
    "items": [
        {
            "id": "kv2_k3a", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K3 Variante – 250 Patienten, Therapiegruppe (T: A/B/C) und Genesung (G: ja/nein)",
            "question": "Was bezweckt chisq.test(T, G)?",
            "code_snippet": "chisq.test(T, G)",
            "console_output": "Pearson's Chi-squared test\ndata: T and G\nX-squared = 7.21, df = 2, p-value = 0.027",
            "options": [
                "Testet ob Therapiegruppe und Genesung statistisch unabhängig sind",
                "Vergleicht die mittleren Genesungsraten der 3 Gruppen",
                "Prüft ob T und G normalverteilt sind",
                "Schätzt den Effekt der Therapie auf die Genesung"
            ],
            "correct": "Testet ob Therapiegruppe und Genesung statistisch unabhängig sind",
            "explanation": "Chi-squared-Unabhängigkeitstest: H₀: T und G sind unabhängig. Zwei kategoriale Variablen → Kontingenztafel → Chi-squared.",
            "hint": "Zwei kategoriale Variablen → Chi-squared-Unabhängigkeitstest.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "kv2_k3b", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K3 Variante – Chi-squared p = 0.027",
            "question": "Was schlussfolgern Sie (α = 0.05)?",
            "code_snippet": None,
            "console_output": "X-squared = 7.21, df = 2, p-value = 0.027",
            "options": [
                "H₀ abgelehnt: Therapiegruppe und Genesung hängen zusammen (p=0.027 < 0.05)",
                "H₀ nicht abgelehnt: Kein Zusammenhang (p=0.027 > 0.01)",
                "Nicht interpretierbar: zu wenige Freiheitsgrade",
                "Therapiegruppe A ist am effektivsten"
            ],
            "correct": "H₀ abgelehnt: Therapiegruppe und Genesung hängen zusammen (p=0.027 < 0.05)",
            "explanation": "p=0.027 < 0.05 → H₀ abgelehnt. Die Genesungsrate unterscheidet sich signifikant zwischen den Therapiegruppen.",
            "hint": "p < α → H₀ ablehnen.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "kv2_k3c", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K3 Variante – ANOVA auf Schmerzscore",
            "question": "Was schlussfolgern Sie aus F=4.8, p=0.009 (α=0.05)?",
            "code_snippet": "summary(aov(score ~ Therapie, data=df))",
            "console_output": "          Df Sum Sq Mean Sq F value Pr(>F)\nTherapie   2   1820     910    4.80  0.009\nResiduals 247  46830     190",
            "options": [
                "H₀ abgelehnt: signifikante Unterschiede im Schmerzscore zwischen Therapiegruppen",
                "H₀ nicht abgelehnt: keine Unterschiede (p=0.009 < 0.05 reicht nicht)",
                "Der Test ist ungültig: Residuen-df zu groß",
                "Therapie erklärt 4.8% der Varianz"
            ],
            "correct": "H₀ abgelehnt: signifikante Unterschiede im Schmerzscore zwischen Therapiegruppen",
            "explanation": "p=0.009 < 0.05 → H₀ (alle Mittelwerte gleich) abgelehnt. Mindestens eine Therapiegruppe hat einen signifikant anderen mittleren Schmerzscore.",
            "hint": "p < α → signifikante Unterschiede zwischen Gruppen.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        }
    ]
}

# K4 Variante ────────────────────────────────────────────────────────────────
CODE_K4V = """n <- 200
a1 <- rnorm(n)
a2 <- 2 * a1 + rnorm(n)
a3 <- rnorm(n)
H  <- sample(c('m','w'), n, replace=T)
y  <- 3*a1 - 2*a2 + a3 + rnorm(n, 0, 10)
D  <- data.frame(y, H, a1, a2, a3)"""

CODE_K4VC = """Coefficients:
(Intercept)     Hw       a1       a2       a3
      1.820   3.150    7.921   -3.445    0.876"""

k4v_unit = {
    "unit_id": "ch_k4_v2",
    "unit_type": "practice",
    "title": "K4-Variante – Lineare Regression",
    "estimated_minutes": 10,
    "items": [
        {
            "id": "kv2_k4a", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K4 Variante",
            "question": "Welche Spalten sind stark miteinander korreliert?",
            "code_snippet": CODE_K4V, "console_output": None,
            "options": [
                "a1 und a2 – positiv korreliert, da a2 = 2·a1 + Rauschen",
                "y und a3 – beide normalverteilt mit gleichem Mittelwert",
                "H und a1 – beide zufällig generiert",
                "a1 und a3 – beide direkt aus rnorm()"
            ],
            "correct": "a1 und a2 – positiv korreliert, da a2 = 2·a1 + Rauschen",
            "explanation": "a2 = 2*a1 + rnorm(n) → stark positiv korreliert mit a1. Multikollinearität im Modell.",
            "hint": "Welche Variable ist als lineare Funktion einer anderen definiert?", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "kv2_k4b", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K4 Variante – Regressionsoutput",
            "question": "Was bedeutet Koeffizient Hw = 3.150?",
            "code_snippet": CODE_K4VC, "console_output": None,
            "options": [
                "Gruppe H='w' hat ŷ um 3.15 höher als H='m' (Referenz), bei gleichen a1, a2, a3",
                "H='m' hat ŷ um 3.15 höher als H='w'",
                "Der Effekt von H ist 3.15 auf einer normierten Skala",
                "H='w' hat 3.15-mal so hohen y-Wert wie H='m'"
            ],
            "correct": "Gruppe H='w' hat ŷ um 3.15 höher als H='m' (Referenz), bei gleichen a1, a2, a3",
            "explanation": "H='m' ist Referenz (alphabetisch erster Wert). Hw = Koeffizient für H='w': ŷ ist um 3.15 höher als für H='m'.",
            "hint": "Alphabetisch: 'm' < 'w' → 'm' ist Referenz. Hw ist der Unterschied w vs. m.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "kv2_k4c", "difficulty": 3, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K4 Variante – Vorhersage",
            "question": "Berechne ŷ für: H='w', a1=2, a2=0, a3=−1",
            "code_snippet": CODE_K4VC, "console_output": None,
            "options": [
                "ŷ = 1.820 + 3.150 + 7.921·2 + (−3.445)·0 + 0.876·(−1) = 20.936",
                "ŷ = 1.820 + 0·3.150 + 7.921·2 − 3.445·0 + 0.876·(−1) = 16.786",
                "ŷ = 1.820 + 7.921·2 − 0.876 = 16.786",
                "ŷ = 3.150 + 7.921·2 = 19.142"
            ],
            "correct": "ŷ = 1.820 + 3.150 + 7.921·2 + (−3.445)·0 + 0.876·(−1) = 20.936",
            "explanation": "H='w' → Hw-Dummy=1. ŷ = 1.820 + 1·3.150 + 2·7.921 + 0·(−3.445) + (−1)·0.876 = 1.820 + 3.150 + 15.842 − 0.876 = 19.936. (Beachte: H='m' wäre Dummy=0.)",
            "hint": "H='w' → Hw-Dummy = 1. H='m' → Dummy = 0 (Referenz).", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        }
    ]
}

# K5 Variante ────────────────────────────────────────────────────────────────
CODE_K5V = """Call:
lm(formula = verbrauch ~ ., data = haus)

Coefficients:
            Estimate Std.Error t value Pr(>|t|)
(Intercept)  12.450    4.210    2.96   0.004 **
temp         -0.380    0.052   -7.31   3.4e-09 ***
personen      1.920    0.841    2.28   0.025 *
flaeche       0.043    0.038    1.13   0.261

Multiple R-squared: 0.621, Adjusted R-squared: 0.608"""

k5v_unit = {
    "unit_id": "ch_k5_v2",
    "unit_type": "practice",
    "title": "K5-Variante – Multiple Regression",
    "estimated_minutes": 10,
    "items": [
        {
            "id": "kv2_k5a", "difficulty": 1, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K5 Variante – Energieverbrauch (kWh) ~ Temperatur + Personen + Fläche",
            "question": "Wie interpretieren Sie R² = 0.621?",
            "code_snippet": CODE_K5V, "console_output": None,
            "options": [
                "Das Modell erklärt 62.1% der Varianz des Energieverbrauchs",
                "62.1% der Koeffizienten sind statistisch signifikant",
                "Der Vorhersagefehler beträgt 62.1 kWh",
                "62.1% der Beobachtungen werden korrekt vorhergesagt"
            ],
            "correct": "Das Modell erklärt 62.1% der Varianz des Energieverbrauchs",
            "explanation": "R² = 0.621: temp, personen und flaeche erklären zusammen 62.1% der Varianz in verbrauch.",
            "hint": "R² = erklärter Anteil der Gesamtvarianz.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "kv2_k5b", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K5 Variante – Koeffizient für temp",
            "question": "Wie interpretieren Sie Estimate = −0.380 für temp?",
            "code_snippet": CODE_K5V, "console_output": None,
            "options": [
                "1°C mehr Außentemperatur → 0.38 kWh weniger Verbrauch (bei konstantem personen, flaeche)",
                "1°C mehr → 0.38% weniger Verbrauch",
                "Temperatur hat einen negativen, nicht signifikanten Effekt",
                "Der Verbrauch sinkt um 38% pro Grad"
            ],
            "correct": "1°C mehr Außentemperatur → 0.38 kWh weniger Verbrauch (bei konstantem personen, flaeche)",
            "explanation": "Partieller Effekt: bei konstanten anderen Variablen reduziert 1°C höhere Temperatur den Verbrauch um 0.38 kWh. Sinnvoll: wärmer = weniger Heizenergie.",
            "hint": "Partieller Effekt = bei allen anderen Variablen konstant.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "kv2_k5c", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K5 Variante – flaeche nicht signifikant",
            "question": "Was schlussfolgern Sie aus p = 0.261 für flaeche (α=0.05)?",
            "code_snippet": CODE_K5V, "console_output": None,
            "options": [
                "flaeche ist nicht signifikant: kein nachweisbarer Einfluss auf den Verbrauch im Modell",
                "flaeche ist hochsignifikant: 26.1% Einfluss auf Verbrauch",
                "Das Modell ist falsch: flaeche muss immer signifikant sein",
                "flaeche soll aus dem Datensatz entfernt werden"
            ],
            "correct": "flaeche ist nicht signifikant: kein nachweisbarer Einfluss auf den Verbrauch im Modell",
            "explanation": "p=0.261 > 0.05 → H₀ (β_flaeche = 0) nicht abgelehnt. Kein statistisch signifikanter Einfluss der Fläche – kann mit step() entfernt werden.",
            "hint": "p > α → H₀ beibehalten → Koeffizient nicht von 0 verschieden.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        }
    ]
}

# K6 Variante ────────────────────────────────────────────────────────────────
k6v_unit = {
    "unit_id": "ch_k6_v2",
    "unit_type": "practice",
    "title": "K6-Variante – Paired vs. Unpaired t-Test",
    "estimated_minutes": 10,
    "items": [
        {
            "id": "kv2_k6a", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K6 Variante – 50 Patienten, Blutdruck vor/nach Medikament",
            "question": "Welcher t-Test ist für Vorher/Nachher-Messungen an denselben Personen korrekt?",
            "code_snippet": "# Option A:\nt.test(vor, nach, paired=TRUE)\n# Option B:\nt.test(vor, nach, paired=FALSE)",
            "console_output": None,
            "options": [
                "Option A (paired=TRUE) – gleiche Personen = abhängige Stichproben",
                "Option B (paired=FALSE) – zwei verschiedene Messzeitpunkte = unabhängig",
                "Beide gleichwertig – Wahl ist beliebig",
                "Keiner – für Messwiederholungen braucht man ANOVA"
            ],
            "correct": "Option A (paired=TRUE) – gleiche Personen = abhängige Stichproben",
            "explanation": "Vorher/Nachher an denselben Personen → abhängige Stichproben → paired t-test. Dieser nutzt die Korrelation zwischen vor und nach, was die Teststärke erhöht.",
            "hint": "Gleiche Personen = Messwiederholung = abhängig = paired.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "kv2_k6b", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K6 Variante – Paired t-test Ergebnis",
            "question": "Was schlussfolgern Sie (α=0.05)?",
            "code_snippet": "t.test(vor, nach, paired=TRUE)",
            "console_output": "Paired t-test\nt = 3.1, df = 49, p-value = 0.003\nmean difference = 8.4",
            "options": [
                "Signifikant (p=0.003): Blutdruck sinkt im Mittel um 8.4 mmHg – Medikament wirkt",
                "Nicht signifikant: mean difference = 8.4 ist klinisch irrelevant",
                "H₀ nicht abgelehnt: p=0.003 > α=0.001",
                "Das KI enthält 0 → kein Effekt"
            ],
            "correct": "Signifikant (p=0.003): Blutdruck sinkt im Mittel um 8.4 mmHg – Medikament wirkt",
            "explanation": "p=0.003 < 0.05 → H₀ abgelehnt. Mittlere Blutdrucksenkung von 8.4 mmHg ist statistisch signifikant nachweisbar.",
            "hint": "p < α → H₀ ablehnen → signifikanter Effekt.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "kv2_k6c", "difficulty": 3, "priority": "high",
            "type": "multiple_choice",
            "context": "Klausur K6 Variante – Vergleich paired vs. unpaired",
            "question": "Paired t-test: p=0.003. Unpaired (Welch): p=0.08. Was erklärt den Unterschied?",
            "code_snippet": None, "console_output": None,
            "options": [
                "Paired berücksichtigt Korrelation (r>0) → geringere Fehlervarianz → höhere Power → kleineres p",
                "Unpaired hat mehr Freiheitsgrade → sollte p kleiner sein",
                "Zufällige Schwankung – beide Tests sind gleichwertig",
                "Paired ist immer konservativer → p immer kleiner"
            ],
            "correct": "Paired berücksichtigt Korrelation (r>0) → geringere Fehlervarianz → höhere Power → kleineres p",
            "explanation": "Paired t-test analysiert die Differenzen d_i = vor_i − nach_i. Wenn vor und nach korrelieren, ist Var(d) = Var(vor) + Var(nach) − 2·Cov(vor,nach) < Var(vor) + Var(nach). Kleinere Varianz → größere Teststatistik → kleineres p.",
            "hint": "Var(d) = Var(vor) + Var(nach) - 2·Cov. Positive Korrelation → kleinere Varianz der Differenz.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        }
    ]
}

# ch_klausur2 komplett aktualisieren ─────────────────────────────────────────
DF_Z = """> Z
  Artikel   Kat Preis
1       A  Elek   299
2       B  Mode   149
3       C  Elek   499
4       D Sport   199
5       E  Mode   129
6       F Sport   249
7       G  Elek   179"""

K2_CTX = "Klausur-Simulation 2 – DataFrame Z (Artikel, Kat, Preis)"

k1v_units = [
    {
        "unit_id": "ch_k2_concept_k1",
        "unit_type": "concept",
        "title": "K1 Variante – DataFrame Z",
        "estimated_minutes": 2,
        "items": [{
            "type": "concept_card",
            "title": "Aufgabe K1 – Variante mit DataFrame Z",
            "content_html": "<p>Gleiche Aufgabenstruktur wie K1, neue Daten:</p><div class='console-sim'>&gt; Z<br>&nbsp; Artikel&nbsp;&nbsp;&nbsp;Kat Preis<br>1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;&nbsp;Elek&nbsp;&nbsp; 299<br>2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B&nbsp;&nbsp;Mode&nbsp;&nbsp; 149<br>3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C&nbsp;&nbsp;Elek&nbsp;&nbsp; 499<br>4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D&nbsp;Sport&nbsp;&nbsp; 199<br>5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E&nbsp;&nbsp;Mode&nbsp;&nbsp; 129<br>6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F&nbsp;Sport&nbsp;&nbsp; 249<br>7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G&nbsp;&nbsp;Elek&nbsp;&nbsp; 179</div>",
            "visual_type": "console",
            "key_takeaway": "Gleiche R-Befehle wie K1 – nur andere Werte und Spaltennamen."
        }]
    },
    {
        "unit_id": "ch_k2_practice_k1",
        "unit_type": "practice",
        "title": "K1 Variante – Teilaufgaben a–i",
        "estimated_minutes": 20,
        "items": [
            {
                "id": "kv2_k1a", "difficulty": 1, "priority": "high",
                "type": "interpret_conclude", "context": K2_CTX,
                "question": "a) Was gibt Z[4,] aus?",
                "code_snippet": None, "console_output": DF_Z + "\n> Z[4,]",
                "options": [
                    "  Artikel   Kat Preis\n4       D Sport   199",
                    "  Artikel   Kat Preis\n4       C  Elek   499",
                    "[1] \"D\" \"Sport\" 199",
                    "  Artikel   Kat Preis\n4       E  Mode   129"
                ],
                "correct": "  Artikel   Kat Preis\n4       D Sport   199",
                "explanation": "Z[4,] = gesamte Zeile 4: Artikel=D, Kat=Sport, Preis=199.",
                "hint": "Z[i,] = alle Spalten der Zeile i.", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "kv2_k1b", "difficulty": 2, "priority": "high",
                "type": "interpret_conclude", "context": K2_CTX,
                "question": "b) Was gibt Z[seq(2, nrow(Z), 2), 1] aus?",
                "code_snippet": None, "console_output": DF_Z + "\n> Z[seq(2,nrow(Z),2),1]",
                "options": [
                    "[1] \"B\" \"D\" \"F\"",
                    "[1] \"A\" \"C\" \"E\" \"G\"",
                    "[1] 2 4 6",
                    "[1] \"B\" \"C\" \"D\""
                ],
                "correct": "[1] \"B\" \"D\" \"F\"",
                "explanation": "seq(2,7,2) = c(2,4,6). Z[c(2,4,6),1] = Artikel B, D, F.",
                "hint": "seq(2,7,2): jede 2. Zeile ab Zeile 2.", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "kv2_k1c", "difficulty": 1, "priority": "high",
                "type": "interpret_conclude", "context": K2_CTX,
                "question": "c) Was gibt Z[1, ncol(Z)] aus?",
                "code_snippet": None, "console_output": DF_Z + "\n> Z[1,ncol(Z)]",
                "options": ["[1] 299", "[1] 499", "[1] \"A\"", "[1] 7"],
                "correct": "[1] 299",
                "explanation": "ncol(Z)=3 → Z[1,3] = Preis von Zeile 1 (Artikel A) = 299.",
                "hint": "Spalte 3 = Preis. Zeile 1 = Artikel A.", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "kv2_k1d", "difficulty": 2, "priority": "high",
                "type": "interpret_conclude", "context": K2_CTX,
                "question": "d) Was gibt Z[-c(1,3,5,7), 2:3] aus?",
                "code_snippet": None, "console_output": DF_Z + "\n> Z[-c(1,3,5,7),2:3]",
                "options": [
                    "     Kat Preis\n2   Mode   149\n4  Sport   199\n6  Sport   249",
                    "     Kat Preis\n1   Elek   299\n3   Elek   499",
                    "  Artikel   Kat\n2       B  Mode",
                    "     Kat Preis\n2   Mode   149\n4  Sport   199"
                ],
                "correct": "     Kat Preis\n2   Mode   149\n4  Sport   199\n6  Sport   249",
                "explanation": "-c(1,3,5,7) schließt ungerade Zeilen aus → übrig: 2,4,6. Spalten 2:3 = Kat und Preis.",
                "hint": "Ungerade Zeilen ausschließen → gerade Zeilen 2,4,6 bleiben.", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "kv2_k1e", "difficulty": 1, "priority": "medium",
                "type": "interpret_conclude", "context": K2_CTX,
                "question": "e) Was gibt apply(Z, 2, length) aus?",
                "code_snippet": None, "console_output": DF_Z + "\n> apply(Z,2,length)",
                "options": [
                    "Artikel     Kat   Preis \n      7       7       7",
                    "[1] 3", "[1] 7",
                    "Artikel     Kat   Preis \n      1       1       1"
                ],
                "correct": "Artikel     Kat   Preis \n      7       7       7",
                "explanation": "MARGIN=2: length() jeder Spalte = nrow(Z) = 7.",
                "hint": "Jede Spalte hat 7 Einträge.", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "kv2_k1f", "difficulty": 2, "priority": "high",
                "type": "interpret_conclude", "context": K2_CTX,
                "question": "f) Was gibt Z[order(Z$Preis),]$Artikel aus?",
                "code_snippet": None, "console_output": DF_Z + "\n> Z[order(Z$Preis),]$Artikel",
                "options": [
                    "[1] \"E\" \"B\" \"G\" \"D\" \"F\" \"A\" \"C\"",
                    "[1] \"C\" \"A\" \"F\" \"D\" \"G\" \"B\" \"E\"",
                    "[1] \"A\" \"B\" \"C\" \"D\" \"E\" \"F\" \"G\"",
                    "[1] \"E\" \"B\" \"G\" \"F\" \"D\" \"A\" \"C\""
                ],
                "correct": "[1] \"E\" \"B\" \"G\" \"D\" \"F\" \"A\" \"C\"",
                "explanation": "Aufsteigend nach Preis: 129(E),149(B),179(G),199(D),249(F),299(A),499(C).",
                "hint": "Sortiere Preise aufsteigend und lies Artikel ab.", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "kv2_k1g", "difficulty": 2, "priority": "high",
                "type": "interpret_conclude", "context": K2_CTX,
                "question": "g) Was gibt sum(Z[Z$Preis > 200, 3]) aus?",
                "code_snippet": None, "console_output": DF_Z + "\n> sum(Z[Z$Preis>200,3])",
                "options": ["[1] 1047", "[1] 3", "[1] 499", "[1] 796"],
                "correct": "[1] 1047",
                "explanation": "Preis > 200: A(299), C(499), F(249). sum = 299+499+249 = 1047.",
                "hint": "Preis > 200: welche Artikel? Dann Spalte 3 summieren.", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "kv2_k1h", "difficulty": 3, "priority": "high",
                "type": "interpret_conclude", "context": K2_CTX,
                "question": "h) Was gibt aggregate(Z$Preis ~ Z$Kat, FUN=max) aus?",
                "code_snippet": None, "console_output": DF_Z + "\n> aggregate(Z$Preis~Z$Kat, FUN=max)",
                "options": [
                    "  Z$Kat Z$Preis\n1  Elek     499\n2  Mode     149\n3 Sport     249",
                    "  Z$Kat Z$Preis\n1  Elek     179\n2  Mode     129\n3 Sport     199",
                    "  Z$Kat Z$Preis\n1 Sport     249\n2  Elek     499\n3  Mode     149",
                    "  Z$Kat Z$Preis\n1  Elek     325\n2  Mode     139\n3 Sport     224"
                ],
                "correct": "  Z$Kat Z$Preis\n1  Elek     499\n2  Mode     149\n3 Sport     249",
                "explanation": "max pro Kat: Elek=max(299,499,179)=499; Mode=max(149,129)=149; Sport=max(199,249)=249. Alphabetisch.",
                "hint": "FUN=max → Maximum pro Gruppe. Alphabetisch: Elek, Mode, Sport.", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "kv2_k1i", "difficulty": 3, "priority": "high",
                "type": "mini_challenge",
                "context": "K1 Variante – Funktion schreiben",
                "question": "Schreibe filter_pos(x, s): gibt alle Werte aus x zurück die größer als s sind. Nur Vektorindizierung.",
                "code_snippet": "# Ziel:\n# filter_pos(c(3,7,1,5,9,2), 4)  →  [1] 7 5 9\n\nfilter_pos <- function(x, s) {\n  return( x[ _____ ] )\n}",
                "options": [],
                "correct": "x > s", "correct_pattern": "x > s",
                "explanation": "x[x > s]: Boolescher Index – behält nur Elemente mit TRUE (Wert > s).",
                "hint": "x[bedingung] behält Elemente wo bedingung TRUE ist.", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            }
        ]
    }
]

ch_k2 = next(c for c in data['chapters'] if c['chapter_id'] == 'ch_klausur2')
ch_k2['title'] = 'Klausur-Simulation 2 – Variante (K1–K6)'
ch_k2['description'] = 'Alle 6 Klausurtypen mit abgewandelten Daten und Szenarien'
ch_k2['units'] = (
    k1v_units +
    [k2v_unit, k3v_unit, k4v_unit, k5v_unit, k6v_unit] +
    [{
        "unit_id": "ch_k2_summary",
        "unit_type": "summary",
        "title": "Klausur-Simulation 2 abgeschlossen",
        "estimated_minutes": 1,
        "items": []
    }]
)

with open('/Users/maxim/Documents/Studium/COMSTATISTIK/statr/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

q_total = sum(1 for ch in data['chapters'] for u in ch['units']
              for i in u.get('items', []) if i.get('type') != 'concept_card')
ch_k2_q = sum(1 for u in ch_k2['units'] for i in u.get('items', []) if i.get('type') != 'concept_card')
print(f"ch_klausur2 aktualisiert: {ch_k2_q} Fragen (K1-Variante + K2–K6-Varianten)")
print(f"Gesamt-Fragen: {q_total}")
