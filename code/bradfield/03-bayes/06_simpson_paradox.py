# uv run python code/bradfield/03-bayes/06_simpson_paradox.py
# DISCOVER Simpson's paradox: a trend that holds in every subgroup REVERSES
# once the groups are pooled. Conditioning on the wrong (or no) variable lies.
# (MCS ch 18, Simpson's Paradox.) Classic shape: UC Berkeley 1973 admissions.
from fractions import Fraction

# Two departments, two applicant groups. (applicants, admitted) per cell.
# Dept E is easy to get into; Dept H is hard. Men crowd into E, women into H.
data = {
    "Dept E (easy)": {"men": (80, 60), "women": (10, 9)},
    "Dept H (hard)": {"men": (20, 1), "women": (180, 30)},
}


def rate(cell):
    applicants, admitted = cell
    return Fraction(admitted, applicants)


print("Within EACH department, women are admitted at the higher rate:")
for dept, cells in data.items():
    mr, wr = rate(cells["men"]), rate(cells["women"])
    print(f"  {dept:<14} men {float(mr):.0%}   women {float(wr):.0%}"
          f"   women higher? {wr > mr}")
    assert wr > mr     # women win in every single department


# Now POOL the departments and recompute the overall admit rates.
def overall(group):
    apps = sum(cells[group][0] for cells in data.values())
    adm = sum(cells[group][1] for cells in data.values())
    return Fraction(adm, apps)


men_all, women_all = overall("men"), overall("women")
print("\nPooled across BOTH departments, the comparison flips:")
print(f"  men   {float(men_all):.0%}   women {float(women_all):.0%}"
      f"   men higher? {men_all > women_all}")
assert men_all > women_all   # aggregate says men do better -- the reversal!

print("\nThe lurking variable: men applied mostly to the EASY dept, women to")
print("the HARD one. Pr[admit] depends on dept; ignoring it inverts the trend.")
