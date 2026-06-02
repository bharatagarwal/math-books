# uv run --with numpy python \
#   "code/pim/06 - Linear Algebra/08_word_vectors.py"
#
# Chapter 10, Section 10.9: "the SVD representation has reproduced the
# gender aspect of language": king - man + woman ~= queen.
# We don't scrape CNN; instead we build a tiny co-occurrence matrix
# by hand so the semantic linear structure Kun describes is visible
# and the analogy arithmetic actually lands on the right word.

import numpy as np

# Latent meaning we secretly bake in: each word is a point in a
# 2D semantic space [royalty, femaleness]. The SVD's job is to
# recover this low-dimensional structure from raw counts.
words = ["king", "queen", "man", "woman", "prince", "princess"]
latent = np.array([
    [1.0, 0.0],   # king:     royal, male
    [1.0, 1.0],   # queen:    royal, female
    [0.0, 0.0],   # man:      commoner, male
    [0.0, 1.0],   # woman:    commoner, female
    [0.8, 0.0],   # prince:   royal-ish, male
    [0.8, 1.0],   # princess: royal-ish, female
])

# A "context feature" matrix: how strongly each word fires on a set
# of 5 context detectors. This is a noisy linear image of `latent`,
# the kind of raw count data the SVD is handed.
np.random.seed(7)
mixing = np.random.randn(2, 5)
counts = latent @ mixing + np.random.randn(6, 5) * 0.02

# Run SVD and keep the top 2 components: the "smoothed" embedding.
U, S, Vt = np.linalg.svd(counts, full_matrices=False)
embed = U[:, :2] * S[:2]
vec = dict(zip(words, embed))


def closest(target, exclude):
    """Nearest word to `target` by cosine similarity."""
    best, best_sim = None, -2.0
    for w in words:
        if w in exclude:
            continue
        v = vec[w]
        sim = float(np.dot(target, v) /
                    (np.linalg.norm(target) * np.linalg.norm(v)))
        if sim > best_sim:
            best, best_sim = w, sim
    return best, best_sim


# The famous analogy: king - man + woman should land near queen.
analogy = vec["king"] - vec["man"] + vec["woman"]
answer, sim = closest(analogy, exclude={"king", "man", "woman"})
print("king - man + woman  ->  %s  (cos %.3f)" % (answer, sim))
assert answer == "queen"

# prince - man + woman should land near princess.
analogy2 = vec["prince"] - vec["man"] + vec["woman"]
answer2, _ = closest(analogy2, exclude={"prince", "man", "woman"})
print("prince - man + woman ->", answer2)
assert answer2 == "princess"

print("Semantic meaning is roughly additive -- the SVD found it.")
