"""
r_simulator.py – Generates static SVG/PNG visualizations of R outputs.
Run once at server start to populate static/img/.
# HOOK: Agent5 – add more visualizations here
"""
import os
import json
import math

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "static", "img")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def _svg_header(w, h):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'

def _svg_footer():
    return "</svg>"


def gen_vector_visual():
    values = [7, -6, 10, 93, 1, 9, 20]
    w, h, bw = 560, 90, 70
    svg = [_svg_header(w, h)]
    svg.append('<rect width="100%" height="100%" fill="#F5F4F0" rx="8"/>')
    svg.append('<text x="10" y="22" font-family="JetBrains Mono,monospace" font-size="13" fill="#6B6B8A">x &lt;- c(7, -6, 10, 93, 1, 9, 20)</text>')
    for i, v in enumerate(values):
        x = 10 + i * (bw + 4)
        color = "#5B50E8" if v > 0 else "#E8506A"
        svg.append(f'<rect x="{x}" y="32" width="{bw}" height="36" fill="{color}" rx="6" opacity="0.85"/>')
        svg.append(f'<text x="{x+bw//2}" y="56" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="15" font-weight="bold" fill="#FFFFFF">{v}</text>')
        svg.append(f'<text x="{x+bw//2}" y="78" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" fill="#6B6B8A">[{i+1}]</text>')
    svg.append(_svg_footer())
    with open(os.path.join(OUTPUT_DIR, "vector_basic.svg"), "w") as f:
        f.write("\n".join(svg))


def gen_matrix_visual():
    M = [[1,4,7],[2,5,8],[3,6,9]]
    w, h, cw, rh = 280, 180, 70, 40
    svg = [_svg_header(w, h)]
    svg.append('<rect width="100%" height="100%" fill="#F5F4F0" rx="8"/>')
    svg.append('<text x="10" y="22" font-family="JetBrains Mono,monospace" font-size="12" fill="#6B6B8A">matrix(1:9, nrow=3)</text>')
    colors = ["#E8E6FF","#D4D1FF","#C0BCFF"]
    for ci, col in enumerate(M):
        for ri, val in enumerate(col):
            x, y = 20 + ci * (cw + 4), 34 + ri * (rh + 4)
            svg.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{rh}" fill="{colors[ci]}" rx="5" stroke="#5B50E8" stroke-width="1.5"/>')
            svg.append(f'<text x="{x+cw//2}" y="{y+rh//2+5}" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="16" font-weight="bold" fill="#1A1A2E">{val}</text>')
    for ci in range(3):
        x = 20 + ci * (cw + 4) + cw // 2
        svg.append(f'<text x="{x}" y="162" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" fill="#6B6B8A">[,{ci+1}]</text>')
    for ri in range(3):
        y = 34 + ri * (rh + 4) + rh // 2 + 5
        svg.append(f'<text x="8" y="{y}" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" fill="#6B6B8A">[{ri+1},]</text>')
    svg.append(_svg_footer())
    with open(os.path.join(OUTPUT_DIR, "matrix_basic.svg"), "w") as f:
        f.write("\n".join(svg))


def gen_confusion_matrix():
    matrix_data = [[5, 1, 1], [0, 6, 1], [0, 2, 4]]
    labels = ["1", "2", "3"]
    w, h, cw, rh = 340, 260, 70, 50
    svg = [_svg_header(w, h)]
    svg.append('<rect width="100%" height="100%" fill="#F5F4F0" rx="8"/>')
    svg.append('<text x="170" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="600" fill="#1A1A2E">Konfusionsmatrix</text>')
    svg.append('<text x="170" y="40" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" fill="#6B6B8A">Vorhergesagt →</text>')
    for ci, lbl in enumerate(labels):
        x = 100 + ci * (cw + 4) + cw // 2
        svg.append(f'<text x="{x}" y="60" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="600" fill="#5B50E8">{lbl}</text>')
    for ri, row in enumerate(matrix_data):
        y_label = 75 + ri * (rh + 4) + rh // 2 + 5
        svg.append(f'<text x="48" y="{y_label}" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="600" fill="#1A1A2E">{labels[ri]}</text>')
        for ci, val in enumerate(row):
            x = 60 + ci * (cw + 4)
            y = 65 + ri * (rh + 4)
            color = "#D4FAE8" if ri == ci else "#FFE4E9"
            border = "#2E9E6B" if ri == ci else "#E8506A"
            svg.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{rh}" fill="{color}" rx="5" stroke="{border}" stroke-width="2"/>')
            svg.append(f'<text x="{x+cw//2}" y="{y+rh//2+6}" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="18" font-weight="bold" fill="#1A1A2E">{val}</text>')
    svg.append('<text x="20" y="90" font-family="Inter,sans-serif" font-size="11" fill="#6B6B8A" transform="rotate(-90,20,130)">Tatsächlich</text>')
    svg.append(_svg_footer())
    with open(os.path.join(OUTPUT_DIR, "confusion_matrix.svg"), "w") as f:
        f.write("\n".join(svg))


def gen_apply_visual():
    w, h = 480, 200
    svg = [_svg_header(w, h)]
    svg.append('<rect width="100%" height="100%" fill="#F5F4F0" rx="8"/>')
    svg.append('<text x="10" y="20" font-family="Inter,sans-serif" font-size="13" font-weight="600" fill="#1A1A2E">apply(M, 1, sum)   vs   apply(M, 2, sum)</text>')
    M = [[1,2,3],[4,5,6],[7,8,9]]
    cw, rh = 44, 36
    for ri, row in enumerate(M):
        for ci, val in enumerate(row):
            x = 20 + ci * (cw + 3)
            y = 34 + ri * (rh + 3)
            svg.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{rh}" fill="#F0EDFF" rx="4" stroke="#5B50E8" stroke-width="1"/>')
            svg.append(f'<text x="{x+cw//2}" y="{y+rh//2+5}" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="14" fill="#1A1A2E">{val}</text>')
    row_sums = [sum(r) for r in M]
    for ri, s in enumerate(row_sums):
        y = 34 + ri * (rh + 3) + rh // 2 + 5
        svg.append(f'<text x="185" y="{y}" font-family="JetBrains Mono,monospace" font-size="13" fill="#2E9E6B">→ {s}</text>')
    svg.append('<text x="20" y="180" font-family="Inter,sans-serif" font-size="12" fill="#5B50E8">MARGIN=1: Zeilensummen [6, 15, 24]</text>')
    col_sums = [sum(M[r][c] for r in range(3)) for c in range(3)]
    for ci, s in enumerate(col_sums):
        x = 20 + ci * (cw + 3) + cw // 2
        svg.append(f'<text x="{x}" y="152" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="12" fill="#E8506A">↓{s}</text>')
    svg.append('<text x="240" y="180" font-family="Inter,sans-serif" font-size="12" fill="#E8506A">MARGIN=2: Spaltensummen [12, 15, 18]</text>')
    svg.append(_svg_footer())
    with open(os.path.join(OUTPUT_DIR, "apply_visual.svg"), "w") as f:
        f.write("\n".join(svg))


def gen_recycling_visual():
    w, h = 500, 130
    svg = [_svg_header(w, h)]
    svg.append('<rect width="100%" height="100%" fill="#F5F4F0" rx="8"/>')
    svg.append('<text x="10" y="20" font-family="Inter,sans-serif" font-size="13" font-weight="600" fill="#1A1A2E">Recycling: a &gt; c(8, 3)</text>')
    a = [7, 18, 2, 10]
    b = [8, 3, 8, 3]
    for i, (av, bv) in enumerate(zip(a, b)):
        x = 20 + i * 110
        svg.append(f'<rect x="{x}" y="30" width="80" height="32" fill="#F0EDFF" rx="5" stroke="#5B50E8" stroke-width="1.5"/>')
        svg.append(f'<text x="{x+40}" y="52" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="15" fill="#1A1A2E">{av}</text>')
        svg.append(f'<text x="{x+40}" y="80" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="13" fill="#E8506A">{bv}</text>')
        result = "TRUE" if av > bv else "FALSE"
        color = "#2E9E6B" if result == "TRUE" else "#E8506A"
        svg.append(f'<text x="{x+40}" y="108" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="12" fill="{color}" font-weight="bold">{result}</text>')
    svg.append('<text x="10" y="25" font-family="Inter,sans-serif" font-size="11" fill="#6B6B8A">a:</text>')
    svg.append('<text x="10" y="80" font-family="Inter,sans-serif" font-size="11" fill="#E8506A">c(8,3) recycelt:</text>')
    svg.append(_svg_footer())
    with open(os.path.join(OUTPUT_DIR, "recycling_visual.svg"), "w") as f:
        f.write("\n".join(svg))


def generate_all():
    gen_vector_visual()
    gen_matrix_visual()
    gen_confusion_matrix()
    gen_apply_visual()
    gen_recycling_visual()
    print(f"r_simulator: {len(os.listdir(OUTPUT_DIR))} Visualisierungen generiert in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate_all()
