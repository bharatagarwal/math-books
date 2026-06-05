# Guess, Test, Refine

You have a guess. Maybe it came from tabulating cases, maybe from analogy, maybe from a vague feeling that something ought to be true. The guess is not the finish. It is the beginning of a second problem. Before, you had a problem to find. Now you have a problem to prove, or to disprove. What you do next determines whether the guess becomes a theorem, a stepping stone, or a dead end.

"No idea is really bad, unless we are uncritical. What is really bad is to have no idea at all."


## Examine your guess

Your guess may be right, but it is foolish to accept a vivid guess as a proven truth, as primitive people often do. Your guess may be wrong. But it is also foolish to disregard a vivid guess altogether, as pedantic people sometimes do. Guesses that arise after you have attentively considered and genuinely understood a problem deserve to be taken seriously. They usually contain at least a fragment of the truth. Yet there is a chance to extract the whole truth only if you examine them appropriately.

Examining a guess means three things:

**State it precisely.** A vague feeling cannot be tested. A precise statement can. If you suspect the number of subsets of $\{1, 2, \ldots, n\}$ is "always a power of two," force yourself to write: the number of subsets is $2^n$. The act of stating it commits you, and a committed conjecture is one you can attack.

**Test it against cases you have not yet checked.** You found the pattern using $n = 1, 2, 3$. Now try $n = 5$. Better still, try $n = 0$; boundary cases are the most informative. The empty set has exactly one subset (itself), and $2^0 = 1$. If the guess survives, your confidence rises. If it fails, you learn something specific.

**Ask why it might be true.** Can you see even the outline of a proof? For the subset conjecture, you might notice that adding one element to the set doubles the count: every old subset spawns two new ones (with and without the new element). That recursive structure is not just evidence. It is the skeleton of a proof by induction.

Many a guess has turned out to be wrong but nevertheless useful in leading to a better one.


## Extreme cases test the rule

Not all test cases are equal. Extreme cases (boundary, degenerate, unusual) provide stronger evidence than ordinary ones. Why? Because they are the most likely to be counterexamples. If a general statement survives its hardest test, the evidence is worth far more than a hundred easy confirmations.

Check $n = 0$ before $n = 10$. Check the empty graph before the complete graph. Check the degenerate triangle before the equilateral one. If your formula for the edges of a complete graph is $\binom{n}{2}$, the case $n = 1$ (zero edges) and $n = 2$ (one edge) are where off-by-one errors live. Go there first.

In the subset-counting thread: the extreme case is $n = 0$. One subset, one binary string (the empty string). The formula gives $2^0 = 1$. If it had failed here, you would know the conjecture needs a patch, or a replacement.

The habit of testing extreme cases is plausible reasoning applied to your own work. You are asking: *if my formula is wrong, where is it most likely to fail?* And you go there first.


## The guess that breaks

Here is the common sequence:

- You guess a formula.
- You test it: it fails for some case.
- You examine *why* it fails.
- The failure reveals a structural feature you had missed.
- You revise the guess, incorporating the new feature.
- The revised guess works.

The wrong guess was not wasted. It was a probe. The failure was informative.

Suppose you conjecture that every $n$ satisfying $2^n - 2 \equiv 0 \pmod{n}$ is prime. You check small primes ($2, 3, 5, 7, 11$) and the congruence holds. But then you test $n = 341 = 11 \times 31$, a composite, and find it also satisfies the congruence. The conjecture breaks. The counterexample does not destroy the original observation (Fermat's little theorem says every prime passes this test). It destroys the converse. And the failure teaches you something precise: this test is necessary for primality but not sufficient. Pseudoprimes exist.

Don't do as Mr. John Jones does. Polya tells the story of a man who suspected his boss was sabotaging his career. The suspicion was not unreasonable; there were some signs. The real mistake was that, after conceiving the suspicion, Mr. Jones became blind to all signs pointing in the opposite direction. He worried himself into firm belief and behaved so stupidly that he almost created the very enemy he imagined.

The trouble with Mr. Jones is that he never examines his opinions. Don't let your conjecture harden into conviction before the evidence justifies it. In theoretical matters, the best of ideas is hurt by uncritical acceptance and thrives on critical examination.


## Determination, hope, and the will to persist

It would be a mistake to think that testing a guess is a purely intellectual affair. Determination and emotions play an important role. Lukewarm determination may be enough for a routine problem. But to solve a serious problem, will power is needed that can outlast bitter disappointments.

Determination fluctuates with hope and hopelessness, with satisfaction and disappointment. You are elated when your forecast comes true. You are depressed when the path you followed with confidence is suddenly blocked.

You do not despise little successes — on the contrary, you seek them. Each case that confirms your conjecture, each clause of the condition satisfied, sustains the work. If you had no opportunity to familiarize yourself with these fluctuations (the small elations, the discouragement when a promising path closes), your mathematical education failed in the most vital point.


## Persist, switch, or rest

When progress stalls, you face a decision with three options.

**Persist** when you have a plan not yet fully executed, when signs of progress appeared recently, or when you can identify a specific obstacle and see at least the shape of how to overcome it.

**Switch** when you have been on a path for a substantial time with no signs at all, or when a sign that once looked favorable has turned misleading. Switching is not giving up; it is choosing a different formulation, representation, or auxiliary problem. The next trial should not be the last one repeated.

Why does variation help? You remember things by mental association: what you have in mind tends to recall what was in contact with it before. Varying the problem brings in new points, new contacts, new possibilities of reaching something relevant. There is also a simpler reason: you cannot sustain concentration on the same point indefinitely. If you fail to make progress, your attention falters. To vary the problem is to renew the object of concentration.

The hardest version of switching is to abandon a line of work that has cost you significant effort. Ask yourself: *if I were starting fresh right now, with everything I currently know, would I choose this path?* If the answer is no, switch.

**Rest** when you have worked hard and are going in circles, when your attention has dulled, or when you have the impression of almost having the idea but not quite. Before you rest, leave the problem in the best state you can. Settle some small point. Write down where you are and what you have tried. This gives your future self a running start.


## Subconscious work

You work hard on a problem, fail, set it aside. The next morning the key idea appears, seemingly from nowhere. The phenomenon is common and well-attested.

Polya recalled wishing to discuss a certain author with a friend but being unable to remember the name. He tried repeatedly. Nothing came. The next morning, as soon as he thought of the annoyance of the evening before, the name occurred to him without effort.

The conscious mind prepares the ground: it understands the problem, mobilizes knowledge, tries and fails along several paths, builds tension. Then something continues to process it below the surface — rearranging, recombining, testing connections the conscious mind did not finish trying.

You cannot command this process, but you can set conditions for it:

- **Work hard first.** Subconscious work requires conscious preparation. "It would be too easy if it were not so; we could solve difficult problems just by sleeping and waiting for a bright idea."
- **Desire the solution.** Only problems you care about come back improved.
- **Know when to stop.** When each attempt feels like the last one wearing a different hat, it is time to stop. "If today will not, tomorrow may."
- **Leave a clean campsite.** Write down what you know, what you have tried, what seems promising, what failed and why.

Past ages regarded a sudden good idea as an inspiration, a gift of the gods. You must deserve such a gift by work, or at least by a fervent wish.


## Questions to keep

- *Have I stated my guess precisely enough to test it, and have I tested it against the extreme case most likely to break it?*
- *If the guess broke, what exactly failed, and does the failure point toward a better guess?*
- *Am I persisting because new signs keep appearing, or because I cannot face abandoning the effort I have sunk?*
- *Have I worked hard enough to earn a rest, and have I written down where I am before stopping?*
