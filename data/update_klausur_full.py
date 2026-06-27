import json

with open('/Users/maxim/Documents/Studium/COMSTATISTIK/statr/data/content.json', encoding='utf-8') as f:
    data = json.load(f)

# ── Neue K1-Werte aus neuem PDF ──────────────────────────────────────────────
DF_X = """> X
  Stadt  BL Einw
1     A Nds   78
2     B Bay   58
3     C Bay  128
4     D Sac   98
5     E Nds  118
6     F Sac   91
7     G Bay   68"""

K1_CTX = "Klausur K1 – DataFrame X (Stadt, BL, Einw)"

k1_units = [
    {
        "unit_id": "ch16_concept_k1",
        "unit_type": "concept",
        "title": "K1 – DataFrame X",
        "estimated_minutes": 2,
        "items": [{
            "type": "concept_card",
            "title": "Aufgabe K1 – DataFrame X",
            "content_html": "<p>Gegeben ist folgender DataFrame X:</p><div class='console-sim'>&gt; X<br>&nbsp; Stadt&nbsp;&nbsp;BL Einw<br>1&nbsp;&nbsp;&nbsp;&nbsp; A Nds&nbsp;&nbsp; 78<br>2&nbsp;&nbsp;&nbsp;&nbsp; B Bay&nbsp;&nbsp; 58<br>3&nbsp;&nbsp;&nbsp;&nbsp; C Bay&nbsp;&nbsp;128<br>4&nbsp;&nbsp;&nbsp;&nbsp; D Sac&nbsp;&nbsp; 98<br>5&nbsp;&nbsp;&nbsp;&nbsp; E Nds&nbsp;&nbsp;118<br>6&nbsp;&nbsp;&nbsp;&nbsp; F Sac&nbsp;&nbsp; 91<br>7&nbsp;&nbsp;&nbsp;&nbsp; G Bay&nbsp;&nbsp; 68</div><p>Teilaufgaben a)–i): Was geben die R-Befehle aus?</p>",
            "visual_type": "console",
            "key_takeaway": "DF[i,j]: Zeile i, Spalte j. Negativer Index = ausschließen. order() sortiert aufsteigend."
        }]
    },
    {
        "unit_id": "ch16_practice_k1",
        "unit_type": "practice",
        "title": "K1 – Teilaufgaben a–i",
        "estimated_minutes": 20,
        "items": [
            {
                "id": "k16_k1a", "difficulty": 1, "priority": "high",
                "type": "interpret_conclude", "context": K1_CTX,
                "question": "a) Was gibt X[3,] aus?",
                "code_snippet": None, "console_output": DF_X + "\n> X[3,]",
                "options": [
                    "  Stadt  BL Einw\n3     C Bay  128",
                    "  Stadt  BL Einw\n3     B Bay   58",
                    "[1] \"C\" \"Bay\" 128",
                    "  Stadt  BL Einw\n3     D Sac   98"
                ],
                "correct": "  Stadt  BL Einw\n3     C Bay  128",
                "explanation": "X[3,] = gesamte Zeile 3: Stadt=C, BL=Bay, Einw=128.",
                "hint": "X[i,] liefert alle Spalten der Zeile i.", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "k16_k1b", "difficulty": 2, "priority": "high",
                "type": "interpret_conclude", "context": K1_CTX,
                "question": "b) Was gibt X[seq(2, nrow(X), 3), 1] aus?",
                "code_snippet": None, "console_output": DF_X + "\n> X[seq(2,nrow(X),3),1]",
                "options": [
                    "[1] \"B\" \"E\"",
                    "[1] \"B\" \"C\" \"D\"",
                    "[1] 2 5",
                    "[1] \"A\" \"D\" \"G\""
                ],
                "correct": "[1] \"B\" \"E\"",
                "explanation": "seq(2,7,3) = c(2,5). X[c(2,5),1] = Spalte 1 (Stadt) der Zeilen 2 und 5 → \"B\", \"E\".",
                "hint": "seq(from,to,by): seq(2,7,3) = c(2,5).", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "k16_k1c", "difficulty": 1, "priority": "high",
                "type": "interpret_conclude", "context": K1_CTX,
                "question": "c) Was gibt X[nrow(X), ncol(X)] aus?",
                "code_snippet": None, "console_output": DF_X + "\n> X[nrow(X),ncol(X)]",
                "options": ["[1] 68", "[1] 91", "[1] \"G\"", "[1] 7"],
                "correct": "[1] 68",
                "explanation": "nrow(X)=7, ncol(X)=3 → X[7,3] = Einw von Zeile 7 (G, Bay) = 68.",
                "hint": "Letzte Zeile, letzte Spalte = Einw der letzten Stadt.", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "k16_k1d", "difficulty": 2, "priority": "high",
                "type": "interpret_conclude", "context": K1_CTX,
                "question": "d) Was gibt X[-c(1,2,4,5), 2:3] aus?",
                "code_snippet": None, "console_output": DF_X + "\n> X[-c(1,2,4,5),2:3]",
                "options": [
                    "   BL Einw\n3 Bay  128\n6 Sac   91\n7 Bay   68",
                    "   BL Einw\n1 Nds   78\n3 Bay  128",
                    "   BL Einw\n3 Bay  128\n4 Sac   98",
                    "  Stadt  BL\n3     C Bay\n6     F Sac"
                ],
                "correct": "   BL Einw\n3 Bay  128\n6 Sac   91\n7 Bay   68",
                "explanation": "-c(1,2,4,5) schließt Zeilen 1,2,4,5 aus → übrig: Zeilen 3,6,7. Spalten 2:3 = BL und Einw.",
                "hint": "7 Zeilen minus 4 ausgeschlossene = Zeilen 3, 6, 7.", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "k16_k1e", "difficulty": 1, "priority": "medium",
                "type": "interpret_conclude", "context": K1_CTX,
                "question": "e) Was gibt apply(X, 2, length) aus?",
                "code_snippet": None, "console_output": DF_X + "\n> apply(X,2,length)",
                "options": [
                    "Stadt    BL  Einw \n    7     7     7",
                    "[1] 3", "[1] 7",
                    "Stadt    BL  Einw \n    1     1     1"
                ],
                "correct": "Stadt    BL  Einw \n    7     7     7",
                "explanation": "MARGIN=2 → über Spalten. length() jeder Spalte = nrow(X) = 7.",
                "hint": "apply(X,2,f) wendet f auf jede Spalte an. Jede Spalte hat 7 Werte.", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "k16_k1f", "difficulty": 2, "priority": "high",
                "type": "interpret_conclude", "context": K1_CTX,
                "question": "f) Was gibt X[order(X$Einw),]$Stadt aus?",
                "code_snippet": None, "console_output": DF_X + "\n> X[order(X$Einw),]$Stadt",
                "options": [
                    "[1] \"B\" \"G\" \"A\" \"F\" \"D\" \"E\" \"C\"",
                    "[1] \"C\" \"E\" \"D\" \"F\" \"A\" \"G\" \"B\"",
                    "[1] \"A\" \"B\" \"C\" \"D\" \"E\" \"F\" \"G\"",
                    "[1] \"B\" \"G\" \"A\" \"D\" \"F\" \"E\" \"C\""
                ],
                "correct": "[1] \"B\" \"G\" \"A\" \"F\" \"D\" \"E\" \"C\"",
                "explanation": "Aufsteigend nach Einw: 58(B),68(G),78(A),91(F),98(D),118(E),128(C).",
                "hint": "F=91 < D=98 – deshalb kommt F vor D.", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "k16_k1g", "difficulty": 2, "priority": "high",
                "type": "interpret_conclude", "context": K1_CTX,
                "question": "g) Was gibt sum(X[X$Einw > 100, 3]) aus?",
                "code_snippet": None, "console_output": DF_X + "\n> sum(X[X$Einw>100,3])",
                "options": ["[1] 246", "[1] 2", "[1] 128", "[1] 118"],
                "correct": "[1] 246",
                "explanation": "Einw > 100: C(128) und E(118). sum(128,118) = 246.",
                "hint": "Welche Städte haben Einw > 100? Dann Spalte 3 (Einw) summieren.", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "k16_k1h", "difficulty": 3, "priority": "high",
                "type": "interpret_conclude", "context": K1_CTX,
                "question": "h) Was gibt aggregate(X$Einw ~ X$BL, FUN=min) aus?",
                "code_snippet": None, "console_output": DF_X + "\n> aggregate(X$Einw~X$BL, FUN=min)",
                "options": [
                    "  X$BL X$Einw\n1  Bay     58\n2  Nds     78\n3  Sac     91",
                    "  X$BL X$Einw\n1  Bay    128\n2  Nds    118\n3  Sac     98",
                    "  X$BL X$Einw\n1  Bay     85\n2  Nds     98\n3  Sac     95",
                    "  X$BL X$Einw\n1  Nds     78\n2  Bay     58\n3  Sac     91"
                ],
                "correct": "  X$BL X$Einw\n1  Bay     58\n2  Nds     78\n3  Sac     91",
                "explanation": "min pro BL: Bay=min(58,128,68)=58; Nds=min(78,118)=78; Sac=min(98,91)=91. Alphabetisch.",
                "hint": "FUN=min → Minimum pro Gruppe. Bay hat B(58),C(128),G(68).", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            },
            {
                "id": "k16_k1i", "difficulty": 2, "priority": "high",
                "type": "interpret_conclude",
                "context": "K1i – Funktion f auf DataFrame X",
                "question": "i) Was macht f(X, c(3,1,2))?",
                "code_snippet": "f <- function(Y, rf) return(Y[, rf])",
                "console_output": None,
                "options": [
                    "Gibt X mit Spalten in Reihenfolge Einw, Stadt, BL zurück",
                    "Gibt Zeilen 3, 1, 2 von X zurück",
                    "Gibt nur Spalte 3 (Einw) zurück",
                    "Fehler: rf ist kein gültiger Spaltenname"
                ],
                "correct": "Gibt X mit Spalten in Reihenfolge Einw, Stadt, BL zurück",
                "explanation": "Y[, c(3,1,2)] selektiert Spalten in dieser Reihenfolge: 3(Einw), 1(Stadt), 2(BL).",
                "hint": "Y[, rf] mit Vektor = Spalten umsortieren.", "visual": None,
                "times_seen": 0, "times_correct": 0, "last_result": None
            }
        ]
    }
]

# ── K2: Monte-Carlo ──────────────────────────────────────────────────────────
CODE_K2 = """f <- function(n) {
  x <- runif(n, 10, 20)
  return(sum(x))
}
n <- 1000
x <- replicate(n, f(10))
mean(x > 150)"""

k2_unit = {
    "unit_id": "ch16_practice_k2",
    "unit_type": "practice",
    "title": "K2 – Monte-Carlo-Simulation",
    "estimated_minutes": 10,
    "items": [
        {
            "id": "k16_k2a", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K2 – Monte-Carlo-Simulation",
            "question": "Was macht f(10) in diesem Code?",
            "code_snippet": CODE_K2, "console_output": None,
            "options": [
                "Zieht 10 Zufallszahlen aus U[10,20] und gibt ihre Summe zurück",
                "Gibt 10 gleichverteilte Zufallszahlen zwischen 0 und 1 zurück",
                "Wiederholt den Ausdruck runif(n,10,20) exakt 10 Mal",
                "Gibt die Anzahl Zufallszahlen > 10 zurück"
            ],
            "correct": "Zieht 10 Zufallszahlen aus U[10,20] und gibt ihre Summe zurück",
            "explanation": "runif(10, 10, 20) zieht 10 Werte aus Uniform[10,20]. return(sum(x)) gibt deren Summe zurück.",
            "hint": "n=10 Argumente → 10 Zufallszahlen. sum() summiert.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "k16_k2b", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K2 – Monte-Carlo-Simulation",
            "question": "Was berechnet replicate(1000, f(10))?",
            "code_snippet": CODE_K2, "console_output": None,
            "options": [
                "Wiederholt f(10) genau 1000 Mal und gibt die 1000 Ergebnisse als Vektor zurück",
                "Gibt f(10000) zurück (n=1000×10)",
                "Erstellt eine 1000×10-Matrix mit Zufallszahlen",
                "Berechnet den Mittelwert von f(10) über 1000 Iterationen"
            ],
            "correct": "Wiederholt f(10) genau 1000 Mal und gibt die 1000 Ergebnisse als Vektor zurück",
            "explanation": "replicate(n, expr) wertet expr n-mal aus und sammelt die Ergebnisse in einem Vektor. Hier: 1000 Summenwerte.",
            "hint": "replicate = Schleife über n Wiederholungen.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "k16_k2c", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K2 – Monte-Carlo-Simulation",
            "question": "Was gibt mean(x > 150) aus und was bedeutet das?",
            "code_snippet": CODE_K2, "console_output": None,
            "options": [
                "Den Anteil der Simulationen mit Summe > 150 – Näherung für P(Summe von 10 U[10,20] > 150)",
                "Den Mittelwert aller Simulationswerte die > 150 sind",
                "TRUE oder FALSE: ob der Mittelwert von x größer als 150 ist",
                "Die Anzahl der Simulationen mit Summe > 150"
            ],
            "correct": "Den Anteil der Simulationen mit Summe > 150 – Näherung für P(Summe von 10 U[10,20] > 150)",
            "explanation": "x > 150 ist ein logischer Vektor (TRUE/FALSE). mean() darauf = Anteil TRUE = relative Häufigkeit. Das ist eine MC-Schätzung für die Wahrscheinlichkeit.",
            "hint": "mean(logischer Vektor) = Anteil TRUE.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "k16_k2d", "difficulty": 2, "priority": "high",
            "type": "multiple_choice",
            "context": "Klausur K2 – Monte-Carlo-Simulation",
            "question": "Warum ist mean(x > 150) nur eine Näherung?",
            "code_snippet": None, "console_output": None,
            "options": [
                "Es werden nur 1000 Simulationen verwendet; mit n→∞ konvergiert der Schätzer gegen den wahren Wert",
                "runif() ist nicht wirklich zufällig – es ist deterministisch",
                "sum() rundet auf Ganzzahlen, was den Schätzer verzerrt",
                "Die Bedingung > 150 ist unscharf definiert"
            ],
            "correct": "Es werden nur 1000 Simulationen verwendet; mit n→∞ konvergiert der Schätzer gegen den wahren Wert",
            "explanation": "Monte-Carlo-Schätzer sind Näherungen durch endliche Stichprobengröße. Nach dem Gesetz der großen Zahlen: Schätzer → wahrer Wert wenn n→∞.",
            "hint": "Mehr Simulationen = genauere Schätzung.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "k16_k2e", "difficulty": 3, "priority": "medium",
            "type": "multiple_choice",
            "context": "Klausur K2 – Monte-Carlo-Simulation",
            "question": "Was ist der theoretische Erwartungswert von f(10) = sum(runif(10, 10, 20))?",
            "code_snippet": None, "console_output": None,
            "options": ["150", "100", "200", "15"],
            "correct": "150",
            "explanation": "E[U[10,20]] = (10+20)/2 = 15. Summe von 10 solchen Werten: E = 10 × 15 = 150. Die MC-Simulation schätzt also P(X > E[X]) ≈ 0.5.",
            "hint": "E[Uniform(a,b)] = (a+b)/2. Dann 10 mal nehmen.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        }
    ]
}

# ── K3: Chi-squared + ANOVA ──────────────────────────────────────────────────
k3_unit = {
    "unit_id": "ch16_practice_k3",
    "unit_type": "practice",
    "title": "K3 – Chi-squared-Test & ANOVA",
    "estimated_minutes": 12,
    "items": [
        {
            "id": "k16_k3a", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K3 – 176 Studierende, Variablen: p (Klausurergebnis), SG (Studiengruppe A/B/C), G (Geschlecht m/w)",
            "question": "Was bezweckt der Chi-squared-Test (Output [3b])?",
            "code_snippet": None,
            "console_output": "Pearson's Chi-squared test\ndata:  SG and G\nX-squared = 6.5205, df = 2, p-value = 0.03838",
            "options": [
                "Testet ob Studiengruppe (SG) und Geschlecht (G) statistisch unabhängig sind (H₀: Unabhängigkeit)",
                "Testet ob die Mittelwerte von p in den Gruppen gleich sind",
                "Testet ob SG und G normalverteilt sind",
                "Testet ob der Anteil m/w in jeder Gruppe gleich groß ist"
            ],
            "correct": "Testet ob Studiengruppe (SG) und Geschlecht (G) statistisch unabhängig sind (H₀: Unabhängigkeit)",
            "explanation": "Der Chi-squared-Unabhängigkeitstest prüft H₀: SG und G sind unabhängig. df=2 entspricht (3 SG-Gruppen - 1) × (2 Geschlechter - 1) = 2.",
            "hint": "Chi-squared auf zwei kategoriale Variablen → Unabhängigkeitstest.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "k16_k3b", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K3 – Chi-squared-Test",
            "question": "Was schlussfolgern Sie aus p-value = 0.038 (α = 0.05)?",
            "code_snippet": None,
            "console_output": "X-squared = 6.5205, df = 2, p-value = 0.03838",
            "options": [
                "H₀ abgelehnt: SG und Geschlecht sind nicht unabhängig (signifikanter Zusammenhang)",
                "H₀ nicht abgelehnt: SG und Geschlecht sind unabhängig",
                "Der Test ist nicht aussagekräftig: p-Wert zu nah an 0.05",
                "Das Ergebnis ist zufällig: X-squared ist zu klein"
            ],
            "correct": "H₀ abgelehnt: SG und Geschlecht sind nicht unabhängig (signifikanter Zusammenhang)",
            "explanation": "p = 0.038 < α = 0.05 → H₀ abgelehnt. Es gibt einen signifikanten Zusammenhang zwischen Studiengruppe und Geschlecht.",
            "hint": "p < α → H₀ ablehnen.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "k16_k3c", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K3 – ANOVA",
            "question": "Was bezweckt die ANOVA (aov(p ~ SG, data=X))?",
            "code_snippet": "A <- aov(p ~ SG, data=X)\nsummary(A)",
            "console_output": "           Df Sum Sq Mean Sq F value Pr(>F)\nSG          2   2548    1274   1.635  0.198\nResiduals 173 134773     779",
            "options": [
                "Testet ob die mittleren Klausurergebnisse (p) in den 3 Studiengruppen (A/B/C) gleich sind",
                "Testet ob SG und Geschlecht zusammenhängen",
                "Testet ob p normalverteilt ist",
                "Testet ob die Varianz von p in allen Gruppen gleich ist"
            ],
            "correct": "Testet ob die mittleren Klausurergebnisse (p) in den 3 Studiengruppen (A/B/C) gleich sind",
            "explanation": "ANOVA: H₀: μ_A = μ_B = μ_C (alle Gruppenmittelwerte gleich). Prädiktor SG, Zielvariable p.",
            "hint": "ANOVA testet Gleichheit der Mittelwerte über Gruppen.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "k16_k3d", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K3 – ANOVA",
            "question": "Was schlussfolgern Sie aus F = 1.635, p = 0.198 (α = 0.05)?",
            "code_snippet": None,
            "console_output": "SG  2  2548  1274  1.635  0.198",
            "options": [
                "H₀ nicht abgelehnt: Keine signifikanten Unterschiede zwischen den Studiengruppen",
                "H₀ abgelehnt: Studiengruppe hat signifikanten Einfluss auf Klausurergebnis",
                "Das Modell erklärt 19.8% der Varianz",
                "Studiengruppe C hat signifikant bessere Ergebnisse"
            ],
            "correct": "H₀ nicht abgelehnt: Keine signifikanten Unterschiede zwischen den Studiengruppen",
            "explanation": "p = 0.198 > α = 0.05 → H₀ nicht abgelehnt. Die Klausurergebnisse unterscheiden sich nicht signifikant zwischen den 3 Studiengruppen.",
            "hint": "p > α → H₀ beibehalten.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        }
    ]
}

# ── K4: Lineare Regression mit Faktoren ─────────────────────────────────────
CODE_K4A = """n <- 288
x1 <- rnorm(n)
x2 <- 4 * x1 + rnorm(n)
x3 <- rnorm(n)
G  <- sample(1:2, n, replace=T)
y  <- 2*x1 - 3*x2 + x3 + rnorm(n, 0, 20)
X  <- data.frame(y, G, x1, x2, x3)"""

CODE_K4B = "k <- which(G == 1)\ny[k] <- y[k] - 12"

CODE_K4C = """> G <- as.factor(G)
> model <- lm(y ~ ., data = X)
> model
Coefficients:
(Intercept)      G2       x1       x2       x3
      3.440  -2.005   10.324   -5.287    0.492"""

k4_unit = {
    "unit_id": "ch16_practice_k4",
    "unit_type": "practice",
    "title": "K4 – Lineare Regression",
    "estimated_minutes": 12,
    "items": [
        {
            "id": "k16_k4a", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K4 – Datenframe X mit y, G, x1, x2, x3",
            "question": "Welche Spalten sind stark miteinander korreliert?",
            "code_snippet": CODE_K4A, "console_output": None,
            "options": [
                "x1 und x2 – stark positiv korreliert, weil x2 = 4·x1 + Rauschen",
                "y und x3 – beide normalverteilt",
                "G und x1 – G teilt den Datensatz in zwei Hälften",
                "x1 und x3 – beide aus rnorm()"
            ],
            "correct": "x1 und x2 – stark positiv korreliert, weil x2 = 4·x1 + Rauschen",
            "explanation": "x2 = 4*x1 + rnorm(n) → x2 ist eine lineare Funktion von x1 + kleines Rauschen. Starke positive Korrelation. Dies verursacht Multikollinearität im Regressionsmodell.",
            "hint": "Welche Variable ist als Funktion einer anderen definiert?", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "k16_k4b", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K4 – Codeabschnitt [4b]",
            "question": "Was bewirkt der Code in [4b]?",
            "code_snippet": CODE_K4B, "console_output": None,
            "options": [
                "Subtrahiert 12 von allen y-Werten der Gruppe G == 1",
                "Entfernt alle Beobachtungen mit G == 1 aus dem Datensatz",
                "Setzt y auf 12 für alle Beobachtungen mit G == 1",
                "Gibt die Indizes der Gruppe G == 1 zurück"
            ],
            "correct": "Subtrahiert 12 von allen y-Werten der Gruppe G == 1",
            "explanation": "which(G == 1) gibt die Indizes mit G==1. y[k] <- y[k] - 12 zieht von diesen y-Werten 12 ab. Das simuliert einen Gruppenunterschied.",
            "hint": "which() liefert Indizes. y[k] <- ... verändert genau diese Positionen.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "k16_k4c", "difficulty": 2, "priority": "high",
            "type": "multiple_choice",
            "context": "Klausur K4 – Regressionsoutput [4c]",
            "question": "Was bedeutet der Koeffizient G2 = -2.005 im Modell?",
            "code_snippet": CODE_K4C, "console_output": None,
            "options": [
                "G=2 hat im Vergleich zu G=1 (Referenz) einen um 2.005 kleineren y-Wert",
                "Der Einfluss von G ist -2.005 auf einer Skala von 0 bis 1",
                "G=1 hat einen um 2.005 kleineren y-Wert als G=2",
                "G2 ist nicht signifikant und kann ignoriert werden"
            ],
            "correct": "G=2 hat im Vergleich zu G=1 (Referenz) einen um 2.005 kleineren y-Wert",
            "explanation": "R kodiert Faktoren als Dummy-Variablen. G1 ist Referenz (=0). Koeffizient G2 = -2.005 bedeutet: für G=2 ist ŷ um 2.005 kleiner als für G=1, bei gleichen x1, x2, x3.",
            "hint": "In R ist die erste Faktorstufe immer Referenz. G2 ist der Unterschied G2 vs G1.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "k16_k4d", "difficulty": 3, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K4 – Vorhersage mit Modell [4c]",
            "question": "Berechne ŷ für: G=1, x1=0, x2=−5, x3=0",
            "code_snippet": CODE_K4C, "console_output": None,
            "options": [
                "ŷ = 3.440 + 0·(−2.005) + 0·10.324 + (−5)·(−5.287) + 0·0.492 = 29.875",
                "ŷ = 3.440 + 1·(−2.005) + 0 + (−5)·(−5.287) + 0 = 27.870",
                "ŷ = 3.440 + (−5)·(−5.287) = 29.875",
                "ŷ = 3.440 + 0·10.324 + (−5)·(−2.005) = 13.465"
            ],
            "correct": "ŷ = 3.440 + 0·(−2.005) + 0·10.324 + (−5)·(−5.287) + 0·0.492 = 29.875",
            "explanation": "G=1 ist Referenz → G2-Dummy = 0. ŷ = 3.440 + 0·(−2.005) + 0·10.324 + (−5)·(−5.287) + 0·0.492 = 3.440 + 26.435 = 29.875.",
            "hint": "G=1 ist Referenz → G2-Koeffizient nicht anwenden (Dummy = 0).", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        }
    ]
}

# ── K5: Multiple Regression Interpretation ───────────────────────────────────
CODE_K5 = """Call:
lm(formula = aus ~ ., data = X)

Coefficients:
            Estimate Std. Error t value Pr(>|t|)
(Intercept) 39.2457   18.7431    2.09   0.039 *
gaus         1.8434    0.3068    5.85   2.1e-06 ***
e            8.8002    0.0098    0.22   0.824
m            1.3288    5.9522    0.22   0.824

Multiple R-squared: 0.387, Adjusted R-squared: 0.368"""

k5_unit = {
    "unit_id": "ch16_practice_k5",
    "unit_type": "practice",
    "title": "K5 – Multiple Regression: Interpretation",
    "estimated_minutes": 12,
    "items": [
        {
            "id": "k16_k5a", "difficulty": 1, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K5 – Supermarkt-Datensatz: aus (tatsächliche Ausgaben), gaus (geplante), e (Einkommen), m (Haushaltsgröße)",
            "question": "Wie interpretieren Sie Multiple R-squared: 0.387?",
            "code_snippet": CODE_K5, "console_output": None,
            "options": [
                "Das Modell erklärt 38.7% der Varianz der tatsächlichen Ausgaben (aus)",
                "38.7% der Koeffizienten sind signifikant",
                "Das Modell hat eine Genauigkeit von 38.7%",
                "Der Fehler des Modells beträgt 38.7 Euro"
            ],
            "correct": "Das Modell erklärt 38.7% der Varianz der tatsächlichen Ausgaben (aus)",
            "explanation": "R² = 0.387: 38.7% der Varianz von 'aus' werden durch gaus, e und m erklärt. Die restlichen 61.3% sind durch nicht modellierte Faktoren bedingt.",
            "hint": "R² = Anteil erklärter Varianz an der Gesamtvarianz.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "k16_k5b", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K5 – Pr(>|t|) im summary()",
            "question": "Welche Problematik fällt in der Spalte Pr(>|t|) auf?",
            "code_snippet": CODE_K5, "console_output": None,
            "options": [
                "e und m haben p-Werte von 0.824 – beide sind nicht signifikant trotz signifikantem Gesamtmodell",
                "Der Intercept ist nicht signifikant (p=0.039 < 0.05 stimmt nicht)",
                "Alle Koeffizienten sind hoch signifikant (***)",
                "gaus hat einen zu kleinen p-Wert – das ist verdächtig"
            ],
            "correct": "e und m haben p-Werte von 0.824 – beide sind nicht signifikant trotz signifikantem Gesamtmodell",
            "explanation": "gaus ist hochsignifikant (***), aber e (Einkommen) und m (Haushaltsgröße) haben identische p-Werte von 0.824 – beide nicht signifikant. Identische p-Werte sind ebenfalls auffällig.",
            "hint": "Schau auf die Sterne: *** = hoch signifikant. Kein Stern = nicht signifikant.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "k16_k5c", "difficulty": 3, "priority": "high",
            "type": "multiple_choice",
            "context": "Klausur K5 – identische p-Werte 0.824 für e und m",
            "question": "Welchen Grund könnte es haben, dass e und m identische p-Werte (0.824) haben?",
            "code_snippet": None, "console_output": None,
            "options": [
                "Multikollinearität – e und m korrelieren stark miteinander, VIF-Analyse empfohlen",
                "Datenfehler – beide Variablen wurden identisch gemessen",
                "Das Modell hat zu viele Beobachtungen",
                "R² ist zu niedrig für signifikante Koeffizienten"
            ],
            "correct": "Multikollinearität – e und m korrelieren stark miteinander, VIF-Analyse empfohlen",
            "explanation": "Identische t-Werte (0.22) und p-Werte (0.824) für e und m deuten auf starke Kollinearität hin. Wenn zwei Prädiktoren hoch korrelieren, können ihre Einzeleffekte nicht mehr zuverlässig geschätzt werden. Prüfen mit: car::vif(model).",
            "hint": "Was passiert wenn zwei Prädiktoren sehr ähnliche Information tragen?", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "k16_k5d", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K5 – Durbin-Watson-Test [5b]",
            "question": "Was wird mit dem Durbin-Watson-Test getestet und was bedeutet das Ergebnis?",
            "code_snippet": None,
            "console_output": "Durbin-Watson test\ndata: model\nDW = 2, p-value = 0.5\nalternative hypothesis: true autocorrelation is greater than 0",
            "options": [
                "Testet Autokorrelation der Residuen; DW=2, p=0.5 → keine signifikante Autokorrelation (Modellannahme erfüllt)",
                "Testet ob Residuen normalverteilt sind; p=0.5 → normalverteilt",
                "Testet Heteroskedastizität; DW=2 → konstante Varianz",
                "Testet ob alle Koeffizienten = 0; p=0.5 → Modell nicht signifikant"
            ],
            "correct": "Testet Autokorrelation der Residuen; DW=2, p=0.5 → keine signifikante Autokorrelation (Modellannahme erfüllt)",
            "explanation": "Durbin-Watson testet H₀: keine Autokorrelation der Residuen. DW=2 bedeutet keine Autokorrelation (DW ∈ [0,4], ideal=2). p=0.5 > 0.05 → H₀ nicht abgelehnt. Residuen sind unkorreliert.",
            "hint": "DW=2 = ideal (keine Autokorrelation). DW < 2: positive, DW > 2: negative Autokorrelation.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        }
    ]
}

# ── K6: Gepaarter vs. ungepaarter t-Test ────────────────────────────────────
k6_unit = {
    "unit_id": "ch16_practice_k6",
    "unit_type": "practice",
    "title": "K6 – Korrelation & t-Test (gepaart vs. ungepaart)",
    "estimated_minutes": 12,
    "items": [
        {
            "id": "k16_k6a", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K6 – 70 Testpersonen, Gewicht vor und nach Diät",
            "question": "Was bezweckt der Test in [6b]?",
            "code_snippet": None,
            "console_output": "Pearson's product-moment correlation\ndata: vor and nach\nt = 7.8, df = 68, p-value = 6e-11\n95 percent confidence interval:\n 0.5371 0.7928\nsample estimates:\ncor = 0.6856",
            "options": [
                "Testet ob vor- und nach-Messungen signifikant miteinander korrelieren (entscheidend für die Wahl paired vs. unpaired)",
                "Testet ob die Diät erfolgreich war (Gewichtsabnahme signifikant)",
                "Testet ob die Gewichtsmessungen normalverteilt sind",
                "Testet ob die Varianzen vor und nach gleich sind"
            ],
            "correct": "Testet ob vor- und nach-Messungen signifikant miteinander korrelieren (entscheidend für die Wahl paired vs. unpaired)",
            "explanation": "Der Korrelationstest prüft H₀: ρ=0. r=0.686, p < 0.001 → starke signifikante Korrelation. Das bestätigt: paired t-test ist angemessen (Messwiederholung, abhängige Stichproben).",
            "hint": "Warum korrelieren vor und nach? Weil es dieselben Personen sind.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "k16_k6b", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K6 – Konfidenzintervall [6c]",
            "question": "Was schlussfolgern Sie aus dem 95%-KI [0.3818, 5.8125]?",
            "code_snippet": None,
            "console_output": "95 percent confidence interval:\n 0.3818 5.8125",
            "options": [
                "Die mittlere Gewichtsabnahme liegt mit 95% Wahrscheinlichkeit zwischen 0.38 und 5.81 kg – signifikant (0 nicht im Intervall)",
                "Der Korrelationskoeffizient liegt zwischen 0.38 und 5.81",
                "Das KI enthält 0 → kein signifikanter Unterschied",
                "95% der Testpersonen haben zwischen 0.38 und 5.81 kg abgenommen"
            ],
            "correct": "Die mittlere Gewichtsabnahme liegt mit 95% Wahrscheinlichkeit zwischen 0.38 und 5.81 kg – signifikant (0 nicht im Intervall)",
            "explanation": "KI für die mittlere Differenz (vor − nach): [0.38, 5.81]. Da 0 nicht enthalten ist → signifikante Gewichtsabnahme. Schätzung: mittlere Abnahme zwischen 0.38 und 5.81 kg.",
            "hint": "Wenn 0 nicht im KI → signifikant. Beide Grenzen positiv → Abnahme.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "k16_k6c", "difficulty": 2, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K6 – gepaarter t-Test [6d]",
            "question": "Was schlussfolgern Sie aus dem Paired t-test (p = 0.03)?",
            "code_snippet": "t.test(vor, nach, paired=TRUE)",
            "console_output": "Paired t-test\nt = 2.2, df = 69, p-value = 0.03\nmean difference = 3.057",
            "options": [
                "Signifikant (p=0.03 < 0.05): mittlere Gewichtsabnahme von 3.06 kg ist statistisch nachweisbar",
                "Nicht signifikant (p=0.03 zu klein für Aussagen)",
                "Die Diät hat keinen Effekt: mean difference = 3.057 ist zu gering",
                "H₀ nicht abgelehnt: Es gibt keinen Unterschied"
            ],
            "correct": "Signifikant (p=0.03 < 0.05): mittlere Gewichtsabnahme von 3.06 kg ist statistisch nachweisbar",
            "explanation": "p=0.03 < α=0.05 → H₀ (kein mittlerer Unterschied) abgelehnt. Die Diät zeigt einen signifikanten Effekt: mittlere Abnahme von 3.057 kg.",
            "hint": "p < α → H₀ ablehnen → signifikanter Effekt.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        },
        {
            "id": "k16_k6d", "difficulty": 3, "priority": "high",
            "type": "interpret_conclude",
            "context": "Klausur K6 – Vergleich gepaart [6d] vs. ungepaart [6e]",
            "question": "Warum gibt paired p=0.03 aber unpaired p=0.2, und welcher ist besser geeignet?",
            "code_snippet": "# [6d] t.test(vor, nach, paired=TRUE)  → p=0.03\n# [6e] t.test(vor, nach, paired=FALSE) → p=0.20",
            "console_output": None,
            "options": [
                "Paired ist besser: gleiche Personen → abhängige Stichproben. Paired nutzt Korrelation → mehr Power → kleineres p",
                "Unpaired ist besser: konservativer und daher sicherer",
                "Beide sind gleichwertig, paired hat zufällig kleineres p",
                "Unpaired ist korrekt weil vor und nach verschiedene Zeitpunkte sind"
            ],
            "correct": "Paired ist besser: gleiche Personen → abhängige Stichproben. Paired nutzt Korrelation → mehr Power → kleineres p",
            "explanation": "Paired t-test ist korrekt bei Messwiederholungen (Vorher/Nachher bei denselben Personen). Er berücksichtigt die Korrelation (r=0.686) → geringere Fehlervarianz → höhere Teststärke → kleineres p. Unpaired ignoriert diese Abhängigkeit → überschätzt die Varianz → p größer.",
            "hint": "Gleiche Personen = abhängige Stichproben = paired. Die Korrelation erhöht die Teststärke.", "visual": None,
            "times_seen": 0, "times_correct": 0, "last_result": None
        }
    ]
}

# ── ch16: Klausur-Simulation 1 komplett zusammenbauen ───────────────────────
ch16 = next(c for c in data['chapters'] if c['chapter_id'] == 'ch16')
ch16['title'] = 'Klausur-Simulation – Vollständig (K1–K6)'
ch16['description'] = 'Alle 6 Klausuraufgaben: DataFrame, Monte-Carlo, Tests, Regression, t-Test'
ch16['units'] = (
    k1_units +
    [k2_unit, k3_unit, k4_unit, k5_unit, k6_unit] +
    [{
        "unit_id": "ch16_summary",
        "unit_type": "summary",
        "title": "Klausur-Simulation abgeschlossen",
        "estimated_minutes": 1,
        "items": []
    }]
)

with open('/Users/maxim/Documents/Studium/COMSTATISTIK/statr/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

q_total = sum(1 for ch in data['chapters'] for u in ch['units']
              for i in u.get('items', []) if i.get('type') != 'concept_card')
ch16_q = sum(1 for u in ch16['units'] for i in u.get('items', []) if i.get('type') != 'concept_card')
print(f"ch16 aktualisiert: {ch16_q} Fragen (K1–K6)")
print(f"Gesamt-Fragen: {q_total}")
print(f"ch16 units: {[u['unit_id'] for u in ch16['units']]}")
