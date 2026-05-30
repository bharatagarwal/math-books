# uv run --with matplotlib python code/bradfield/03-bayes/make_tree_figures.py
# Generates the two probability-tree figures referenced by the Bayes chapter
# (MCS 18.3 hockey series, and 18.6 medical test) into the chapter images dir.
# Re-run to regenerate. Drawn to mirror the MCS tree diagrams.
import os
from fractions import Fraction
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "markdown/bradfield/03 - Bayes' Rule_images"
os.makedirs(OUT, exist_ok=True)


def draw_tree(nodes, edges, leaves, title, path, figsize=(7.5, 5.0)):
    # nodes: name -> (x, y). edges: (a, b, label). leaves: name -> text.
    fig, ax = plt.subplots(figsize=figsize)
    for a, b, label in edges:
        xa, ya = nodes[a]
        xb, yb = nodes[b]
        ax.plot([xa, xb], [ya, yb], "-", color="#444", lw=1.3, zorder=1)
        ax.text((xa + xb) / 2, (ya + yb) / 2 + 0.06, label,
                ha="center", va="bottom", fontsize=10, color="#b00")
    for name, (x, y) in nodes.items():
        ax.plot(x, y, "o", ms=7, color="#fff",
                markeredgecolor="#333", zorder=2)
    for name, text in leaves.items():
        x, y = nodes[name]
        ax.text(x + 0.12, y, text, ha="left", va="center", fontsize=9)
    ax.set_title(title, fontsize=11)
    ax.axis("off")
    ax.margins(0.18)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, path), dpi=150, bbox_inches="tight")
    plt.close(fig)


# --- Figure 18.1: hockey best-of-three -----------------------------------
# Root -> game1 (W 1/2, L 1/2); then conditional 2/3 after W, 1/3 after L.
n = {
    "root": (0, 3),
    "W": (1, 4), "L": (1, 2),
    "WW": (2, 5), "WL": (2, 3.5),
    "LW": (2, 2.5), "LL": (2, 1),
    "WLW": (3, 4), "WLL": (3, 3),
    "LWW": (3, 2.5), "LWL": (3, 1.8),
}
e = [
    ("root", "W", "1/2"), ("root", "L", "1/2"),
    ("W", "WW", "2/3"), ("W", "WL", "1/3"),
    ("L", "LW", "1/3"), ("L", "LL", "2/3"),
    ("WL", "WLW", "2/3"), ("WL", "WLL", "1/3"),
    ("LW", "LWW", "2/3"), ("LW", "LWL", "1/3"),
]
lv = {
    "WW": "WW  1/3  ✓", "WLW": "WLW 1/9 ✓", "WLL": "WLL 1/9",
    "LWW": "LWW 1/9 ✓", "LWL": "LWL 1/9", "LL": "LL  1/3",
}
draw_tree(n, e, lv,
          "Best-of-three hockey series (✓ = wins series; Pr[win | win g1]=7/9)",
          "hockey-tree.jpeg")

# --- Figure 18.2: medical test -------------------------------------------
# Root -> sick 1/1000 / well 999/1000; then +/- by sensitivity/specificity.
m = {
    "root": (0, 2),
    "sick": (1, 3), "well": (1, 1),
    "sp": (2, 3.5), "sn": (2, 2.5),
    "wp": (2, 1.5), "wn": (2, 0.5),
}
me = [
    ("root", "sick", "0.001"), ("root", "well", "0.999"),
    ("sick", "sp", "0.99"), ("sick", "sn", "0.01"),
    ("well", "wp", "0.01"), ("well", "wn", "0.99"),
]
mlv = {
    "sp": "sick & +   0.00099",
    "sn": "sick & −   0.00001",
    "wp": "well & +   0.00999",
    "wn": "well & −   0.98901",
}
draw_tree(m, me, mlv,
          "Rare-disease test: positive leaves 0.00099 vs 0.00999 -> post ~ 0.09",
          "medical-tree.jpeg", figsize=(7.5, 4.2))

print("wrote hockey-tree.jpeg and medical-tree.jpeg to", OUT)
for f in ("hockey-tree.jpeg", "medical-tree.jpeg"):
    p = os.path.join(OUT, f)
    print(f"  {f}: {os.path.getsize(p)} bytes" if os.path.exists(p) else f"  {f}: MISSING")
