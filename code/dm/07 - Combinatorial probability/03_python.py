# uv run --with hypothesis --with pytest pytest -q
#
# Probability axioms and identities from DM 7.1-7.2, checked as PROPERTIES.
#
# We model a finite UNIFORM probability space (DM 7.1): the sample space S is a
# finite set, an event A is a subset, and P(A) = |A| / |S|. Hypothesis throws
# hundreds of random sample spaces and random events at each law below; if any
# law could fail, Hypothesis finds a counterexample. Since all pass, the book's
# axioms and the exercise identities hold universally on uniform spaces.
#
# Laws checked:
#   * Axiom (a): P(A) >= 0.
#   * Exercise 7.2: P(A) <= 1 for every event.
#   * Axiom (b) form: P(S) = 1, P(empty) = 0.
#   * Complement rule: P(complement of A) = 1 - P(A).
#   * Exercise 7.4 (exclusive events): if A,B disjoint then P(A)+P(B)=P(A∪B).
#   * Exercise 7.5 (inclusion-exclusion): P(A∩B)+P(A∪B)=P(A)+P(B).
#   * Independence sanity: book's dice example E={2,4,6}, T={3,6} are
#     independent: P(E∩T)=1/6=P(E)P(T)=(1/2)(1/3).

from fractions import Fraction

from hypothesis import given, settings
from hypothesis import strategies as st


def prob(event: frozenset, space: frozenset) -> Fraction:
    """Uniform probability P(A) = |A| / |S|  (DM 7.1)."""
    return Fraction(len(event), len(space))


# A random nonempty finite sample space, plus two subsets (events) of it.
@st.composite
def space_and_two_events(draw):
    space = frozenset(
        draw(st.sets(st.integers(0, 40), min_size=1, max_size=20))
    )
    elems = sorted(space)
    a = frozenset(e for e in elems if draw(st.booleans()))
    b = frozenset(e for e in elems if draw(st.booleans()))
    return space, a, b


@settings(max_examples=400)
@given(space_and_two_events())
def test_axioms_and_bounds(data):
    space, a, b = data
    # Axiom (a) and Exercise 7.2.
    assert prob(a, space) >= 0
    assert prob(a, space) <= 1
    # Whole space and empty event.
    assert prob(space, space) == 1
    assert prob(frozenset(), space) == 0


@settings(max_examples=400)
@given(space_and_two_events())
def test_complement_rule(data):
    space, a, _ = data
    complement = space - a
    assert prob(complement, space) == 1 - prob(a, space)


@settings(max_examples=400)
@given(space_and_two_events())
def test_exclusive_events_add(data):
    # Exercise 7.4: if A and B are exclusive (disjoint), P(A)+P(B)=P(A∪B).
    space, a, b = data
    b = b - a  # force disjointness to test the exclusive case
    assert prob(a, space) + prob(b, space) == prob(a | b, space)


@settings(max_examples=400)
@given(space_and_two_events())
def test_inclusion_exclusion(data):
    # Exercise 7.5: P(A∩B) + P(A∪B) = P(A) + P(B), for ANY two events.
    space, a, b = data
    lhs = prob(a & b, space) + prob(a | b, space)
    rhs = prob(a, space) + prob(b, space)
    assert lhs == rhs


def test_book_dice_independence():
    # DM 7.2 worked example, exact: E even, T multiple of 3 on a fair die.
    S = frozenset({1, 2, 3, 4, 5, 6})
    E = frozenset({2, 4, 6})
    T = frozenset({3, 6})
    assert prob(E, S) == Fraction(1, 2)
    assert prob(T, S) == Fraction(1, 3)
    assert (E & T) == frozenset({6})
    # Independence: P(E∩T) = P(E) P(T).
    assert prob(E & T, S) == prob(E, S) * prob(T, S) == Fraction(1, 6)
