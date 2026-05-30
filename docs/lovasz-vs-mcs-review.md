# Lovász & Vesztergombi vs. MIT 6.042J (MCS): A Comparative Review

A reading review of two discrete-mathematics texts as they sit in this repo, written for a software engineer learning mathematics through programming and formal verification (curriculum: `docs/learning-plan.md`). The two books are:

1. **Lovász & Vesztergombi, *Discrete Mathematics*** (Yale lecture notes, 1999) — the full cleaned text in `markdown/dm/01–17`. ~125 pages, 16 short chapters plus answers.
2. **Lehman, Leighton & Meyer, *Mathematics for Computer Science* (MCS)**, MIT 6.042J — OCR'd Proofs part in `markdown/mcs/01 - Proofs/`, with the remaining three parts read from the source PDFs under `mcs/02 - Structures/`, `mcs/03 - Counting/`, `mcs/04 - Probability/`. ~950+ pages, 35 chapters, a full university course.

> Note on the Lovász reader: each chapter here carries inline "programmatic exploration" code (sympy/z3/Lean/Dafny/networkx/hypothesis demos) that was added *for this reader*. This review judges the **mathematical text**, not those demos — though they are mentioned where they bear on how this learner should use the book.

## TL;DR

- **MCS is the right primary text and the curriculum already says so.** It is built by computer scientists for computer scientists: it teaches *proof as a craft* with explicit reusable templates, it makes the logic/sets/relations/induction machinery rigorous and self-contained, and its State Machines & Invariants chapter is the single most curriculum-load-bearing thing in either book — it is essentially Dafny/TLA+ reasoning in mathematical prose.
- **Lovász is the better *first read* and the better re-read for intuition.** It is short, narrative, and discovery-driven — concepts arrive through a party dialogue and "let's experiment, conjecture, then prove" arcs. It covers graph theory (trees, MST/TSP, matchings, Hall, coloring) and a beautiful Pascal→Law-of-Large-Numbers thread far more vividly and with more *connective tissue* than MCS, but it is mathematically looser and assumes more from the reader.
- **They overlap heavily on number theory (Fermat/Euclid/RSA), induction, counting, and graphs — but treat them at different altitudes.** Lovász gives the *story and the why*; MCS gives the *rigor, the templates, and the depth*. Use Lovász to fall in love with a topic and MCS to nail it down.
- **Concrete recommendation:** read the matching Lovász chapter first for orientation, then do the corresponding MCS chapter(s) for rigor and exercises and tool practice. Detailed sequencing table at the end.

## Scope, Length, and Topic Overlap

Lovász is a one-semester *taster*: combinatorics, induction, binomial coefficients, Fibonacci, a single deep probability result, elementary number theory, and a graph-theory spine (graphs → trees → optimization → matchings → coloring → cryptography). It deliberately does **not** systematize logic, sets, relations, or proof method as standalone topics — those are used informally as needed. The authors say so up front: the goal is "to develop a feeling for what mathematics is all about," picking "a number of selected results and methods."

MCS is a *course*: it front-loads an entire Proofs part (logic, predicate logic, sets, relations, induction, recursion, infinite sets/cardinality, well ordering, state machines) before reaching number theory, graph *structures*, counting, and a full four-chapter probability sequence ending in random walks and PageRank. It is roughly 8× the length and goes materially deeper everywhere the topics coincide.

| Topic | Lovász | MCS | Notes on overlap |
|---|---|---|---|
| Proof method as an explicit skill | implicit, by example | **dedicated** (Ch 1–2: templates, contrapositive, cases, contradiction) | MCS unique in teaching proof *as craft* |
| Propositional & predicate logic | none (uses ∀/∃ informally) | **dedicated** (Ch 3–5) | MCS only |
| Sets, relations, functions | §2.2 only (sets, basic ops) | **dedicated** (Ch 6–7) | MCS only; relations → state machines |
| Induction & well ordering | Ch 3 (one chapter) | **Ch 2 (WOP) + Ch 5 (induction, strong, structural)** | both; MCS far more thorough |
| Counting / binomial coefficients | Ch 2, 4, 5 (Pascal) | Ch 25–27 (bijections, binomial, pigeonhole, incl–excl) | both; comparable depth, different flavor |
| Fibonacci / recurrences | Ch 6 (Binet, golden ratio) | Ch 6 (recursive data), Ch 23 partial | Lovász richer on the closed-form derivation |
| Generating functions / asymptotics | Stirling mentioned only | Ch 23–24 (sums, products, asymptotics, big-O) | MCS only |
| Number theory (divisibility, primes, Euclid) | Ch 8 (large, excellent) | Ch 12–14 (GCDs, congruences, Euler) | both; MCS more algebraic (rings, mod arithmetic) |
| Fermat / Euler / RSA | Ch 8 (Fermat) + Ch 16 (RSA) | Ch 14–15 (**Euler's theorem** → RSA) | both; MCS generalizes Fermat→Euler properly |
| Graphs (degrees, paths, connectivity) | Ch 9 | Ch 16–20 (digraphs, DAGs, degrees, coloring, connectivity) | both; MCS splits into many chapters |
| Trees (Cayley, Prüfer) | Ch 10 (**Prüfer bijection in full**) | Ch 21 | Lovász's Cayley/Prüfer treatment is a highlight |
| Optimization (MST, TSP, greedy) | Ch 11 | not as a focus | **Lovász only** |
| Matchings / Hall's theorem | Ch 12, 14 (Marriage Thm, NP/good-characterization) | Ch 22 (**stable matching**, Gale–Shapley) | both, but *different theorems* — see below |
| Graph coloring | Ch 13 | Ch 20 | both |
| Probability | Ch 7 (one chapter → Law of Large Numbers) | **Ch 28–35 (full sequence)** | MCS vastly deeper |
| Random variables, expectation, deviation bounds | none | Ch 31–34 (Markov, Chebyshev, sampling) | MCS only |
| Cardinality / infinite sets | mentioned in a footnote | Ch 11 (diagonalization, ℵ, Cantor) | MCS only |
| Cryptography motivation/commitments | Ch 15–16 (substitution, one-time pad, bit-commitment, RSA) | Ch 15 (RSA) | Lovász broader on *applications*; MCS deeper on *the math* |

The matchings overlap is worth flagging because the two books prove *different* theorems. Lovász proves **Hall's Marriage Theorem** (existence: a bipartite graph has a perfect matching iff every $k$-set on the left has $\geq k$ neighbors) and frames it gorgeously through "tribes and tortoises" and the King Arthur tale about P vs. NP and good characterizations. MCS instead does the **Stable Marriage Problem** and the Gale–Shapley "Mating Ritual" algorithm (every set of preferences admits a stable matching). Same vocabulary, genuinely complementary content — a reader gets *two* different matching theorems by reading both.

## Pedagogical Style and Voice

This is the sharpest difference between the books.

**Lovász teaches by discovery and narrative.** Chapter 2 literally opens at a birthday party where the guests *argue their way* to the formulas for permutations, combinations, and matchings — Carl proposes $7\cdot 6 = 42$ handshakes, Diane objects, Eve settles it with "every handshake was counted twice... 21." The lottery count and the bridge-hand count are derived *as dialogue*, and the chapter notes happily when "we arrived at the same figure by two really different arguments. At the least, it is reassuring." This is the book's signature move: experiment on small cases, stare at a table until a pattern jumps out, *conjecture*, then prove. The induction chapter sums odd numbers, notices "we get squares," and only then formalizes. The Fibonacci chapter computes ratios $\frac{377}{233}=1.618\ldots$, *guesses* a geometric progression, and derives Binet's formula "from scratch" — explicitly rejecting the option of just stating the answer ("Do you feel cheated by this? You should"). Graph theory is introduced by *strengthening* a problem step by step ("if a graph has an odd number of nodes then the number of nodes with even degree is odd... we made an important step toward the solution!"). It is warm, motivated, and very readable.

**MCS teaches by systematic rigor and reusable structure.** Chapter 1 is *about proof itself*: it defines proposition/predicate/axiom/theorem/lemma, lays down modus ponens and sound vs. unsound inference rules, then gives literal **fill-in-the-blank templates** — "To prove that $P$ implies $Q$: 1. Write 'Assume $P$.' 2. Show $Q$ logically follows." It teaches the contrapositive method, proof by cases, and proof by contradiction as named, drillable procedures, and even distinguishes scratchwork from a clean final proof. Where Lovász would *discover* the $\sqrt 2$ irrationality argument, MCS uses it to illustrate a *technique* and is careful to point out (in the Well Ordering chapter) that the "write $m/n$ in lowest terms" step itself needs the Well Ordering Principle — "We've been using the Well Ordering Principle on the sly from early on!" The voice is still friendly (Euler is "oiler"; counterexamples found "at a liberal arts school up Mass Ave") but the organizing unit is the *method*, not the story.

A representative contrast on the same idea — counting subsets of an $n$-set is $2^n$. Lovász gives **two** proofs (a decision tree, then a bijection to binary strings $0\ldots 2^n-1$) and then editorializes on *why* two proofs are valuable: "every proof reveals much more than just the bare fact stated in the theorem." MCS would present the same result inside its induction/bijection machinery with the proof obligations made explicit. Lovász optimizes for *insight per page*; MCS optimizes for *transferable rigor*.

## Mathematical Rigor and Formalism

MCS is the more rigorous book by design, and it is rigorous *about rigor*. It is explicit that it takes "all familiar facts from high school math" as axioms rather than building from ZFC ("a formal proof in ZFC that $2+2=4$ requires more than 20,000 steps"), it names its inference rules, and it repeatedly surfaces hidden assumptions. Proofs are laid out in a uniform shape (statement, "Proof.", structured argument, □) and the harder theorems (Markov, Chebyshev, Gale–Shapley termination/stability, Cantor's theorem) get complete, careful treatments.

Lovász is rigorous *where it matters to the argument* but cheerfully informal elsewhere. It uses "etc." in chapter 2 and then, in chapter 3, explicitly comes back to *replace* "etc." with induction — a deliberate pedagogical reveal. It states Stirling's formula and the Prime Number Theorem *without proof* ("the proof... needs calculus" / "is very difficult"), and it is honest about it. Some arguments are deliberately heuristic and labeled as such (the "$200$-digit prime density" estimate carries a "Warning: This argument is not precise"). The number-theory chapter's "minimal criminal" proof of unique factorization and its Euclid-based proof of the infinitude of primes are genuinely rigorous and elegant; the Prüfer-code bijection proving Cayley's $n^{n-2}$ theorem is a small masterpiece of constructive argument. So Lovász is not *loose* so much as *selective*: it proves what it can prove cleanly and gestures honestly at the rest. For a learner whose goal is formal verification, MCS's habit of never leaving a proof obligation unstated is the better model.

## CS Relevance

Both books are CS-flavored, but MCS is CS-*native* and maps almost one-to-one onto the curriculum's "skill transfer path."

The standout is **MCS Chapter 5, State Machines & Invariants** (`markdown/mcs/01 - Proofs/09`). It defines a state machine as "nothing more than a binary relation on a set," introduces **Floyd's Invariant Principle** ("If a preserved invariant... is true for the start state, then it is true for all reachable states"), and works the diagonally-moving robot example showing $m+n$ stays even — i.e. a *safety invariant*. This is exactly the Dafny loop-invariant / TLA+ safety-property reasoning the curriculum targets (Stages 6 and 8), stated in the cleanest possible mathematical form, with the explicit footnote distinguishing *preserved invariant* (the method) from *invariant-true-of-all-reachable-states* (the objective). No part of Lovász touches this. For *this* learner, that chapter alone justifies MCS as primary.

Other strong CS mappings in MCS: predicate logic → Z3 / Lean (`∀x∃y`); induction & well ordering → Lean proofs; recursive definition → recursive correctness; relations/DAGs/partial orders → scheduling and dependency reasoning; Gale–Shapley → an actual algorithm with termination + correctness proofs; the whole probability sequence (Markov/Chebyshev/sampling) → randomized-algorithm analysis. RSA is built properly on **Euler's Theorem** (the correct generalization of Fermat) and the **Pulverizer** (extended Euclid), so the number theory pays off in a real protocol.

Lovász frames applications more *broadly and atmospherically*: graphs model "highways," "bonds between atoms," "positions in a game"; the optimization chapter is openly about telephone-network construction (MST) and the Travelling Salesman Problem with a real $2$-approximation algorithm; the matchings chapter ends with the King Arthur / Merlin tale that is actually a clean introduction to **NP, P, good characterizations, and certificates** — "the non-existence of a perfect matching... is also an NP-property, while the non-existence of a Hamilton cycle is not." Its cryptography chapters (15–16) are unusually rich on the *applications* side: substitution-cipher frequency attacks, one-time pads and why pad reuse is catastrophic ($c_1\oplus c_2 = m_1\oplus m_2$), bit-commitment for "saving the last chess move," zero-knowledge-flavored password checking, and finally RSA with the Fermat-based correctness argument. So Lovász gives the *applied panorama*; MCS gives the *load-bearing machinery*.

## Problem and Exercise Culture

Lovász weaves exercises *into the flow* — small numbered prompts ("2.1 How many ways...?", "9.2 Is there a graph on 6 nodes with degrees 2,3,3,3,3,3?") appear mid-section, inviting you to test a pattern before the text proves it, and a full **Answers to Exercises** chapter (`markdown/dm/17`) gives terse solutions (often a single formula: "2.1. 7!."). The exercises are mostly short, conceptual, and confirmatory — they reinforce the discovery arc. Several are deliberately instructive *failures* to dissect (3.12 and 3.13 are flawed induction "proofs" you must debug — e.g. the classic "all lines through one point" fallacy), which is excellent training for spotting bad arguments.

MCS exercises are more numerous, harder, and tiered (in-text problems plus end-of-chapter problem sets, with a separate solutions track in `mcs/solutions/`). They demand full written proofs and frequently push past the text (e.g. RSA correctness for the non-coprime case is left as Problem 8.81; "no polynomial maps all naturals to primes" is Problem 1.17). MCS is the better book for *building proof stamina* and for the curriculum's calibration gates ("write a valid proof in <15 min," "≥8/10 counting problems correct"). Lovász is better for *quick intuition checks* and for learning to recognize a flawed proof.

## Prerequisites and Difficulty Ramp

**Lovász** assumes more mathematical maturity *implicitly* (comfort with summation, logs, a willingness to follow a fast-moving argument) but less *formal* machinery — there is no logic/sets prerequisite chapter because it doesn't formalize them. Its ramp is gentle at the start (the party) and then climbs steeply in spots (the Pascal-triangle concentration bounds in §5.2, Theorem 5.2, are genuinely demanding for a 5-page chapter). Because chapters are short and largely independent, you can parachute into any topic.

**MCS** is self-contained and assumes only high-school math, building everything else. Its ramp is long but smooth: ~250 pages of Proofs foundations before number theory. That front-loading is exactly what a verification-track learner wants (you cannot do Lean/Dafny without fluent logic + induction first), but it means MCS is slower to "get to the good stuff" if you only want graphs or probability. The dependency structure is more linear than Lovász's.

## Strengths and Weaknesses

**Lovász — strengths.** Concise and genuinely enjoyable; best-in-class motivation and "where did this come from" derivations; superb on graph theory breadth (MST/TSP/Hall/coloring in ~50 pages); the Prüfer/Cayley and Pascal→Law-of-Large-Numbers threads are small gems; honest about what it doesn't prove; the King Arthur P/NP framing is a delightful, correct first contact with complexity; exercises include instructive flawed proofs.

**Lovász — weaknesses.** Not self-contained for a verification curriculum: no systematic logic, sets, relations, recursion, or cardinality, and *no state machines/invariants at all*. Several key results are stated without proof (Stirling, PNT). Probability is a single chapter aimed at one theorem — no random variables, expectation, or general deviation bounds. Exercise solutions are terse. Some OCR-era source typos exist (flagged inline in this reader, e.g. the gcd example $18=2\cdot 3^3$ should be $2\cdot 3^2$, and a $\cup$/$\cap$ slip in Exercise 7.4). Density of hard material in short chapters can ambush a beginner.

**MCS — strengths.** The designated primary text and the best fit for the curriculum's goals; teaches proof as an explicit, transferable craft with templates; rigorous and self-contained; the State Machines & Invariants chapter maps directly onto Dafny/TLA+; full probability sequence (through Chebyshev, sampling, random walks/PageRank); strong, plentiful, tiered exercises with solutions; correct, deep number theory (Euler's theorem, the Pulverizer) feeding a real RSA.

**MCS — weaknesses.** Long; slower to reach graph/probability "payoffs"; the relentless template/rigor focus, while ideal for skill-building, can feel less *inspiring* than Lovász's discovery arcs; in this repo only the Proofs part is OCR'd to markdown — the other three parts (Structures, Counting, Probability) live only as PDFs, so they aren't yet in the reader and aren't tool-instrumented the way the Lovász chapters are.

## Best-Fit Reader

- **Lovász** fits a curious reader who wants a short, motivating tour of discrete math and graph theory, or an experienced reader who wants intuition and the "story" behind results — and specifically wants graph optimization and Hall's theorem, which MCS doesn't emphasize.
- **MCS** fits a CS student or self-learner who needs to *build proof skill from scratch*, wants logic/induction/state-machine foundations for formal methods, and values depth, rigor, and a large exercise bank. That's exactly this learner.

## Recommendation: How This Learner Should Use Them Together

The two books are complementary, not redundant. **MCS is the spine; Lovász is the lens.** The pattern that maximizes both understanding and the curriculum's verification goals is: **read the short Lovász chapter first for intuition and motivation, then do the MCS chapter(s) for rigor, depth, exercises, and tool practice.** Lovász's "experiment → conjecture → prove" loop is also a perfect match for the reader's "verify with a tool, not the answer key" methodology — and the Lovász chapters in this repo are already instrumented with sympy/z3/Lean/Dafny demos, so they double as a verification warm-up.

Where they reinforce vs. duplicate, and how to sequence against `docs/learning-plan.md`:

| Curriculum stage | Read in Lovász (intuition / first pass) | Then nail with MCS (rigor / primary) | Why this order |
|---|---|---|---|
| 1 Logic | — (Lovász has none) | **MCS Ch 3–5** | MCS only; do it straight, pair with Z3 |
| 2 Proofs | Ch 2–3 (subset counting, two-proofs ethos), the flawed-proof exercises 3.12–3.13 | **MCS Ch 1–2** (templates, WOP) | Lovász shows *why* proofs differ; MCS teaches the *how* and gates Lean |
| 3 Induction | Ch 3 (odd sums, regions), Ch 6 (Fibonacci recurrence) | **MCS Ch 5** (strong, structural) + Ch 10 recursion | Lovász makes induction feel inevitable; MCS systematizes it for Dafny |
| 4 Counting | Ch 2, 4, 5 (Pascal identities, two combinatorial proofs of each) | **MCS Ch 25–27** | Lovász's combinatorial-bijection style is the best intuition for counting |
| 4.5 Graphs/Algorithms | **Ch 9–13** (graphs, trees, MST/TSP, matchings, coloring) — Lovász's strongest area | MCS Ch 16–21 (structures) | Read Lovász *first and heavily* here; it's broader and more vivid than MCS on graphs/optimization |
| 5 Probability | Ch 7 (Pascal → Law of Large Numbers) for the combinatorial intuition | **MCS Ch 28–35** (the real depth) | Lovász gives one beautiful result; MCS gives the whole apparatus |
| 6 State Machines | — (Lovász has none) | **MCS Ch 5 / §5.4 (Invariants)** | The keystone for Dafny/TLA+ — MCS only, do it carefully |
| 7 Number Theory | **Ch 8 + Ch 16** (Euclid, Fermat, pseudoprimes, Miller–Rabin sketch, one-time pad, RSA) | **MCS Ch 12–15** (congruences, Euler, Pulverizer, RSA) | Lovász motivates and tells the crypto story; MCS supplies the algebra that makes RSA correctness a clean Euler-theorem proof for Lean |
| 8 TLA+ bridge | Ch 14 (King Arthur: P/NP, good characterizations, certificates) | MCS state machines + relations recap | Lovász's NP/certificate framing is a gentle, correct on-ramp to safety/liveness thinking |

Two specific "read both" wins:
- **Matchings (Stage 4.5):** Lovász Ch 12/14 (Hall + good characterizations) and MCS Ch 22 (Gale–Shapley stable matching) are *different theorems*. Read both; you get existence-via-Hall and an actual algorithm-with-proof.
- **RSA (Stage 7):** Lovász Ch 8/16 tells you *why* it's secure and *how* the pieces (primality, fast modular exponentiation, factoring hardness) fit, with the Fermat-based correctness sketch; MCS Ch 14–15 gives the clean Euler's-theorem proof and the Pulverizer, which is the version worth formalizing in Lean for the Stage 7 gate ("Prove Fermat's Little Theorem; explain RSA security").

Net: do **MCS cover-to-cover as the backbone**, and use **Lovász as a fast, motivating pre-read** — and as the *only* source for two things MCS underplays: graph optimization (MST/TSP) and the Hall/good-characterization view of matchings. Skip nothing in MCS's Proofs and State Machines parts; those are the curriculum's true constraint.
