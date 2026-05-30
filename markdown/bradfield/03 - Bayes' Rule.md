# Bayes' Rule

*Bradfield session 3 · Monday 22 June · pre-work: MCS chapter 18
(Conditional Probability), problems 18.2, 18.7, 18.26 · post-work: 18.37*

Probability so far has been counting with a denominator. This session is about
the single most practically important move in the subject: **how should a
probability change when you learn something?** Every monitoring alert, spam
filter, medical screening, and "users who did $X$ also did $Y$" is a
conditional-probability question. The mathematics is one short definition and one
one-line theorem — but the *intuition* they correct is worth more than the
formulas, because human intuition about conditioning is reliably, expensively
wrong.

MCS chapter 18 is deliberate about how it teaches this, and it is worth
imitating. It does **not** open with the definition. It opens with a paradox
(Monty Hall) that even professional mathematicians botched, shows *where the
reasoning breaks*, and only then extracts the definition that would have kept us
honest. Then it gives a mechanical, always-works procedure — the **Four-Step
Method** with tree diagrams — so that "be careful about conditioning" becomes an
algorithm rather than a warning. We follow that arc, and at each step we *build
the objects and look* before trusting any formula.

## Monty Hall: where conditioning intuition breaks

You pick one of three doors; the host — who knows where the car is — opens a
*different* door revealing a goat, then offers you the switch. Should you switch?

MCS §18.1 walks through a tempting wrong argument. Say you pick door $A$ and a
goat is revealed behind $B$. There are three outcomes consistent with "picked
$A$, goat behind $B$" — written as (car, pick, opened): $(A,A,B)$, $(A,A,C)$,
$(C,A,B)$, with probabilities $\tfrac1{18}, \tfrac1{18}, \tfrac19$. Switching
wins only on $(C,A,B)$, whose $\tfrac19$ exactly matches the other two combined —
so switching looks no better than staying, a probability of $\tfrac12$.

This is wrong, and the bug is **the wrong condition.** We didn't merely learn
"there is a goat behind $B$"; we learned "Monty *opened* $B$." That precise event
excludes the outcome $(A,A,C)$ — the one where Monty opens $C$, not $B$.
Conditioning on the looser event silently folds in an extra outcome. The same
trap is the heart of the classic "two children" puzzle: a family has two
children; given *at least one is a boy*, the probability *both* are boys is
$1/3$, not $1/2$, because the condition leaves three equally likely families
$\{BB, BG, GB\}$ and only one is $BB$. But given *the older child is a boy*, the
answer is $1/2$. Same family, different fact learned, different restricted space.
Let's compute both restricted spaces by literally restricting and counting, and
connect them to Monty's blunder.

```python
<!-- include: code/bradfield/03-bayes/01_conditional.py -->
```

## Conditional probability, defined

The fix MCS §18.2 extracts is a definition. The probability of $X$ **given** $Y$
is
$$\Pr[X \mid Y] = \frac{\Pr[X \cap Y]}{\Pr[Y]}, \qquad \Pr[Y] > 0.$$
Operationally, conditioning **shrinks the sample space**: throw away every
outcome where $Y$ did not happen, then renormalize over what remains. In the
uniform case it is once again pure counting — restrict to the outcomes
consistent with $Y$, count the fraction that also satisfy $X$. The `01` demo is
exactly this restrict-then-count operation, and it reproduces the $1/3$-vs-$1/2$
split that fools so many people.

The whole Monty Hall confusion, then, is a one-line lesson: **condition on what
you actually observed, not on a looser event that it happens to imply.**

## The Four-Step Method: build the tree, read off the answer

MCS turns "be careful" into a procedure. Conditional-probability questions
succumb to the same **Four-Step Method** used for ordinary probability, organized
around a tree diagram (MCS §18.3):

1. **Find the sample space** — every root-to-leaf path of the tree.
2. **Define the events of interest** — as sets of leaf outcomes.
3. **Determine outcome probabilities** — multiply the edge probabilities along
   each path.
4. **Compute event probabilities** — sum, then divide per the definition.

MCS's worked example is a best-of-three hockey series. The local team wins game 1
with probability $1/2$; thereafter they win with probability $2/3$ if they won
the previous game (invigorated) and $1/3$ if they lost it (demoralized). *Given
they win the first game, what is the probability they win the series?*

Rather than copy the textbook's tree picture, let's **grow the tree in code** and
read the conditional probability straight off the leaves — Step 1 and Step 3
build the leaf list with path probabilities, Step 2 and Step 4 restrict and
divide. It lands on the book's $\Pr[\text{win series} \mid \text{win game 1}] =
7/9$.

```python
<!-- include: code/bradfield/03-bayes/04_four_step_tree.py -->
```

For reference, here is the MCS tree this code reconstructs — each edge carries the
probability of that step *given* the path so far, and each leaf's probability is
the product down its path:

![Figure 18.1: MCS tree diagram for the best-of-three hockey series; leaves are the outcomes $WW, WLW, WLL, LWW, LWL, LL$, and checkmarks flag the wins-the-series outcomes.](03 - Bayes' Rule_images/hockey-tree.jpeg)

## Why tree diagrams work: the product rule

The tree felt like a "funny little picture," but MCS §18.4 justifies it. The
numbers we wrote on the edges *are conditional probabilities*: the $2/3$ on the
second edge of the $WW$ path is $\Pr[\text{win game 2} \mid \text{win game 1}]$.
Multiplying down a path is exactly the **Product Rule for conditional
probabilities**, which is just the definition rearranged:
$$\Pr[E_1 \cap E_2] = \Pr[E_1]\cdot\Pr[E_2 \mid E_1],$$
and for three events,
$$\Pr[E_1 \cap E_2 \cap E_3] =
  \Pr[E_1]\cdot\Pr[E_2 \mid E_1]\cdot\Pr[E_3 \mid E_1 \cap E_2].$$
So $\Pr[WW] = \tfrac12 \cdot \tfrac23 = \tfrac13$ is not a coincidence of the
diagram — it is this rule evaluated. The `04` demo asserts the leaf probabilities
sum to $1$, which is the tree-level statement that the root-to-leaf paths
partition the whole sample space.

## The law of total probability

Step 4 quietly used another idea worth naming. To get an unconditional
probability, **split into cases and weight each by its likelihood** (MCS §18.5).
If $H_1, \dots, H_n$ partition the sample space,
$$\Pr[E] = \sum_i \Pr[E \mid H_i]\,\Pr[H_i].$$

MCS's example: flip a fair coin; on heads roll one die, on tails roll two dice
and sum. What is $\Pr[\text{result} = 2]$? Condition on the hidden coin —
$\tfrac16$ on heads, $\tfrac1{36}$ on tails — and weight by $\tfrac12$ each to
get $7/72$. Let's both compute it and watch a three-million-trial simulation
converge to it, so the law is assembled from real outcomes rather than asserted.

```python
<!-- include: code/bradfield/03-bayes/05_total_probability.py -->
```

## Medical testing and the base-rate fallacy

Total probability is the denominator of the subject's most famous trap (MCS
§18.6). A disease affects $1$ in $1000$ people. A test is "$99\%$ accurate" —
$99\%$ sensitivity ($\Pr[+ \mid \text{sick}]$) *and* $99\%$ specificity
($\Pr[- \mid \text{well}]$). You test positive. What is the chance you are sick?

Most people say $99\%$. The real answer is about **$9\%$**. The denominator
$\Pr[+]$ is dominated by the enormous healthy majority: even a $1\%$
false-positive rate over $99.9\%$ of the population produces far more positives
than the tiny sick group does. We compute the exact posterior, then use the MCS
"natural frequencies" framing — picture a concrete crowd of a million and just
count the true vs. false positives — and finally simulate a two-million-person
population so the effect is a fact you can see in the counts, not just a formula.

```python
<!-- include: code/bradfield/03-bayes/02_medical_test.py -->
```

The exact posterior is $\tfrac{99/100000}{99/100000 + 999/100000} =
\tfrac{99}{1098} = \tfrac{11}{122} \approx 0.09$. MCS makes the punchline sharp:
you can build a "$99.9\%$ accurate" test trivially by *always returning
negative* — it is right about everyone except the $0.1\%$ who are sick, and tells
you nothing. Percent-accuracy is no guarantee of value; the base rate is. This is
exactly why a "highly accurate" intrusion-detection rule that fires on a rare
attack drowns analysts in false positives. When you act on a positive signal,
always ask: *what was the base rate?*

Here is the tree for this test, the same shape as the hockey tree — the posterior
$\Pr[\text{sick}\mid+]$ is the true-positive leaf $0.00099$ divided by the total
positive mass $0.00099 + 0.00999 = 0.01098$, which is exactly the $\approx 0.09$
above:

![Figure 18.2: Probability tree for the rare-disease test (prevalence $1/1000$, $99\%$ sensitivity and specificity); the two positive leaves have probabilities $0.00099$ (sick and $+$) and $0.00999$ (well and $+$), so $\Pr[\text{sick}\mid+]=0.00099/0.01098\approx 0.09$.](03 - Bayes' Rule_images/medical-tree.jpeg)

## Bayes' rule: flipping the conditioning

Often you know the conditionals in one direction — $\Pr[\text{symptom} \mid
\text{disease}]$ — but want the other — $\Pr[\text{disease} \mid
\text{symptom}]$. **Bayes' rule** (MCS Theorem 18.4.1) flips them, and its proof
is one line: both $\Pr[A \mid B]\Pr[B]$ and $\Pr[B \mid A]\Pr[A]$ equal
$\Pr[A \cap B]$, so
$$\Pr[B \mid A] = \frac{\Pr[A \mid B]\,\Pr[B]}{\Pr[A]}
  = \frac{\Pr[A \mid B]\,\Pr[B]}{\sum_i \Pr[A \mid H_i]\,\Pr[H_i]},$$
where the denominator is total probability over a partition $H_i$. The
vocabulary is worth internalizing: $\Pr[B]$ is the **prior** (belief before the
evidence), $\Pr[A \mid B]$ is the **likelihood** (how well the hypothesis
predicts the evidence), and $\Pr[B \mid A]$ is the **posterior** (updated
belief). The medical-test calculation above *is* Bayes' rule with the partition
$\{\text{sick}, \text{well}\}$.

MCS frames Bayes through **a posteriori** probability — reasoning about an earlier
event from a later one (the hockey team "in reverse": given they won the series,
did they win game 1?). Probability theory has no notion of time, so this is
perfectly well-posed. Monty Hall is the same flip wearing a game-show costume:
the host's *informed, deliberate* opening of a goat door is evidence, and Bayes
concentrates the posterior. Let's compute the exact posterior over the three door
locations — staying wins $1/3$, switching wins $2/3$ — and then settle it with a
million simulated games of each strategy.

```python
<!-- include: code/bradfield/03-bayes/03_monty_hall.py -->
```

The clean intuition: switching wins exactly when your *first* pick was wrong, and
your first pick is wrong with probability $2/3$. The host's action does not change
that $2/3$; it merely collapses it onto the single remaining door.

## Simpson's paradox: when conditioning reverses the trend

One last way conditioning can fool you, and the most dangerous in practice
because it hides in real datasets. **Simpson's paradox**: a trend that holds in
*every* subgroup can *reverse* once the groups are pooled. It is the dark twin of
total probability — averaging over a partition without respecting it.

The canonical example is the 1973 UC Berkeley graduate admissions data. Take two
departments. In *each one separately*, women are admitted at a higher rate than
men. Yet pooled across both departments, men are admitted at a higher rate. Both
statements are true of the same numbers. Let's build a concrete dataset with that
exact shape and watch the comparison flip when we drop the department variable.

```python
<!-- include: code/bradfield/03-bayes/06_simpson_paradox.py -->
```

The lurking variable is *which department people applied to*. Men applied mostly
to the easy-admit department, women mostly to the hard-admit one. The admit rate
depends on department; aggregating over it without conditioning on it inverts the
signal. The engineering lesson is direct: before comparing two groups on a pooled
metric — conversion by variant, latency by region, error rate by cohort — ask
*what confound is being averaged over.* The aggregate and the per-segment story
can point in opposite directions, and the per-segment story is usually the true
one.

## Working the problem set (MCS Chapter 18)

The session's problems live in MCS chapter 18, which packages this chapter's
ideas as a small, reusable kit — keep it as a checklist:

- **Definition / shrink-the-space.** $\Pr[X \mid Y] = \Pr[X \cap Y]/\Pr[Y]$;
  condition on *exactly* what you observed (18.2, and the Monty Hall trap).
- **Four-Step Method + tree diagram.** Sample space → events → outcome
  probabilities (multiply edges) → event probabilities (sum, divide). The
  always-works procedure for 18.7-style multi-stage problems.
- **Product rule.** $\Pr[E_1 \cap E_2] = \Pr[E_1]\Pr[E_2 \mid E_1]$ — why
  multiplying edges is legitimate.
- **Law of total probability.** $\Pr[E] = \sum_i \Pr[E \mid H_i]\Pr[H_i]$ — split
  into cases, weight each.
- **Bayes' rule.** Flip the conditioning; carry the **prior**, watch the **base
  rate** (18.26's medical-test family, and 18.37).
- **Independence & Simpson's paradox.** Conditioning can leave a probability
  unchanged (independence) — or *reverse* a trend when a confound is pooled away.

Almost every conditioning mistake in practice is one of these wearing a costume,
plus the constant discipline of *building the small case and counting.*

## Where to go deeper

Bayes' rule is the engine behind naive-Bayes classifiers, A/B-test analysis,
Kalman filters, and probabilistic programming. The mechanics are trivial; the
discipline — always carry the prior, always sanity-check against base rates,
always be precise about *what* you are conditioning on, and always ask what
confound a pooled metric is hiding — is what separates a correct analysis from a
confident wrong one. The full treatment with exercises is MCS chapter 18; for a
deeper, very well-written next text the syllabus recommends Bertsekas &
Tsitsiklis's *Introduction to Probability*.
