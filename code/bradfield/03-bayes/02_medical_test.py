# uv run --with numpy python code/bradfield/03-bayes/02_medical_test.py
# Bayes' rule and the base-rate fallacy: a "99% accurate" test, rare disease.
from fractions import Fraction
import numpy as np

prevalence = Fraction(1, 1000)     # P(disease)
sensitivity = Fraction(99, 100)    # P(positive | disease)       = true positive
specificity = Fraction(99, 100)    # P(negative | healthy)       = true negative

# Bayes: P(disease | positive) =
#   P(pos|dis) P(dis) / [ P(pos|dis)P(dis) + P(pos|healthy)P(healthy) ]
p_dis = prevalence
p_healthy = 1 - prevalence
p_pos_given_dis = sensitivity
p_pos_given_healthy = 1 - specificity     # false positive rate

posterior = (p_pos_given_dis * p_dis) / (
    p_pos_given_dis * p_dis + p_pos_given_healthy * p_healthy
)
# Despite the "99% accurate" test, a positive result means only ~9% chance of
# disease -- false positives from the huge healthy majority swamp the signal.
# Exact value: (99/100000) / (99/100000 + 999/100000) = 99/1098 = 11/122.
assert posterior == Fraction(11, 122)

# MCS 18.6 "natural frequencies": picture a concrete crowd and just count.
# Among N people: prevalence*N are sick, and almost all of those test positive;
# the vast healthy majority each have a small false-positive chance -- but there
# are so many of them that their false positives outnumber the true positives.
N0 = 1_000_000
true_pos = N0 * p_dis * p_pos_given_dis
false_pos = N0 * p_healthy * p_pos_given_healthy
print("Natural frequencies in", N0, "people:")
print("  true positives  (sick & +) =", int(true_pos))
print("  false positives (well & +) =", int(false_pos))
print("  share of positives who are sick =",
      Fraction(int(true_pos), int(true_pos + false_pos)))

# Simulate a population to make the base-rate effect concrete.
rng = np.random.default_rng(7)
N = 2_000_000
sick = rng.random(N) < float(prevalence)
pos = np.where(
    sick, rng.random(N) < float(sensitivity),
    rng.random(N) >= float(specificity),
)
sim_posterior = sick[pos].mean()
assert abs(sim_posterior - float(posterior)) < 0.01

print("\nP(disease | positive) exact =", round(float(posterior), 4),
      " simulated =", round(float(sim_posterior), 4))
print("=> a positive on a 99% test still leaves <10% chance, because the",
      "disease is rare.")
