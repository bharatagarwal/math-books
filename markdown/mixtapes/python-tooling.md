# Tooling Mix: the Python stack behind the demos

Every chapter in this library leans on the same small set of Python tools. They run the inline demos, check the proofs, and translate notation into something executable. This mix sequences the best readings about them so that each track sets up the next — because the tools themselves form a sequence: a way of running code leads to a way of writing mathematics as code, which leads to a way of asking a solver whether the mathematics is true.

## Side A — notation becomes computation

1. **[Running scripts](https://docs.astral.sh/uv/guides/scripts/)** (uv docs) — The substrate comes first. Everything in this repo runs through uv, and this is the page that documents the whole arrangement: `uv run`, the inline `# /// script` dependency block, and `--with` for one-off imports. The command lines scattered through these chapters stop looking magical after a single read.

2. **[Building Python tools with a one-shot prompt](https://simonwillison.net/2024/Dec/19/one-shot-python-tools/)** (Simon Willison) — The previous track showed the mechanics; this one supplies the philosophy. A script that declares its own dependencies is a different kind of artifact from a project — disposable yet reproducible — and every demo in this library is that kind of artifact.

3. **[SymPy: the introductory tutorial](https://docs.sympy.org/latest/tutorials/intro-tutorial/intro.html)** — With the substrate in place, the first real instrument. SymPy makes the most direct version of this repo's claim, that notation can be executed: it opens with exact computation, $\sqrt{8}$ becoming $2\sqrt{2}$ rather than $2.828$, which is the whole idea of the library in miniature.

4. **[SymPy: Gotchas and Pitfalls](https://docs.sympy.org/latest/tutorials/intro-tutorial/gotchas.html)** — Read this immediately after, because it is really a lesson in representation: a `Symbol` is not a Python variable, `==` is not equality of expressions, and `1/2` is consumed by Python before SymPy ever sees it. Understanding why these trip people up teaches more than the happy path does.

5. **[A basic introduction to einsum](https://ajcr.net/Basic-guide-to-einsum/)** (Alex Riley) — SymPy executes the calculus notation; the summation notation belongs to einsum, and the bridge is the same — a compact written form expanding into loops. This is the gentlest way to learn the subscript-string reading rules, one operation at a time.

6. **[Einsum is All You Need](https://rockt.ai/2018/04/30/einsum)** (Tim Rocktäschel) — The payoff for track 5: dot product, outer product, matrix multiplication, and transpose all collapse into one uniform notation, which is exactly the fluency that makes $\Sigma_i a_i b_i$ readable at a glance. Keep Eli Bendersky's [careful derivation](https://eli.thegreenplace.net/2025/understanding-numpys-einsum/) and the [reference page](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html) on hand for when a subscript string misbehaves.

7. **[JAX: automatic differentiation](https://docs.jax.dev/en/latest/automatic-differentiation.html)** — Side A closes where SymPy cannot go: `jax.grad` differentiates *programs*, not symbols, and $\nabla f$ becomes a function you can call. When you want the machinery — Jacobians forward and reverse, Hessians as forward-over-reverse — [The Autodiff Cookbook](https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html) goes as deep as this library will ever need.

## Side B — computation becomes proof

8. **[The Z3Py guide](https://ericpony.github.io/z3py-tutorial/guide-examples.htm)** — Side B turns the direction around: Side A computed what notation describes, Side B checks what notation claims. The standard hands-on walkthrough carries you from arithmetic puzzles up to `ForAll` and `Exists` — the point where $\forall x\, \exists y$ stops being philosophy and becomes a query.

9. **[Satisfiability Modulo Theories: A Beginner's Tutorial](https://hanielbarbosa.com/papers/fm2024.pdf)** (Barrett, Tinelli, et al.) — Once the API is in your hands, the conceptual question arrives on schedule: what is the solver actually doing? Written by the people who build Z3 and cvc5, this is the best single answer — a SAT solver consulting theory solvers, explained from the ground up.

10. **[Programming Z3](https://theory.stanford.edu/~nikolaj/programmingz3.html)** (Bjørner, de Moura, Nachmanson) — The long-form treatment sitting between the two previous tracks and beyond them, connecting the API to the decision procedures underneath. Read it slowly and in pieces, the way one reads a textbook rather than a blog post.

11. **[Property Tests + Contracts = Integration Tests](https://www.hillelwayne.com/pbt-contracts/)** (Hillel Wayne) — The keystone of the verification triad that closes this mix. Once your functions carry contracts, "no input can violate any contract" becomes a single universal property, and your contracts quietly become test oracles. Read this before any of the triad's docs and the three tools stop looking like separate choices.

12. **[Hypothesis: the tutorial introduction](https://hypothesis.readthedocs.io/en/latest/tutorial/introduction.html)** — The triad in order of increasing ambition, starting with testing by generated example: `@given`, strategies, and shrinking. The [quickstart](https://hypothesis.readthedocs.io/en/latest/quickstart.html) exists if you would rather be running in five minutes, and Wayne's [Property Testing with Complex Inputs](https://www.hillelwayne.com/post/property-testing-complex-inputs/) takes on the two genuinely hard parts — finding good properties and generating structured inputs.

13. **[Deal: intro](https://deal.readthedocs.io/basic/intro.html)** — The contracts themselves: pre- and postconditions as decorators, framed as "typing on steroids." This is where the properties from track 11 move into the code they describe.

14. **[CrossHair: introduction](https://crosshair.readthedocs.io/en/latest/introduction.html)** — The most ambitious of the three: where Hypothesis approximates by example, CrossHair attempts proof. [How Does It Work?](https://crosshair.readthedocs.io/en/latest/how_does_it_work.html) reveals the trick that closes Side B's loop — your function is called with symbolic values backed by Z3, so the solver from track 8 is now exploring execution paths no example generator would find.

15. **[Programming and Interactive Proving With Z3Py](https://www.philipzucker.com/programming-and-interactive-proving-with-z3py/)** (Philip Zucker) — The closer: Z3 bent toward genuine theorem proving, for when the basics have settled and you want to see how far the engine underneath everything on this side can be pushed.

## Hidden track

16. **[NetworkX: tutorial](https://networkx.org/documentation/stable/tutorial.html)** — NetworkX stands apart from both sides; it neither executes notation nor checks claims, it is simply the graph chapters' workbench. The tutorial is short, and the reference [introduction](https://networkx.org/documentation/stable/reference/introduction.html) is the better conceptual read for the one design decision that explains the whole API: a node can be any hashable Python object. Save both for the week a graphs chapter is open in the other tab — the same just-in-time principle the Foundations Mix is built on.
