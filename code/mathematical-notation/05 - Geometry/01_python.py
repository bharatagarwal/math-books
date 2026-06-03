# uv run --with sympy python
# Geometric notation → SymPy geometry objects.
# Points, distances, angles, lines, triangles.
from sympy.geometry import (
    Point, Line, Segment, Triangle, Circle
)
from sympy import pi, simplify, sqrt, cos, N

# --- Points: (x, y) tuples become Point objects ---
A = Point(0, 0)
B = Point(4, 0)
C = Point(2, 3)
print(f"A = {A}, B = {B}, C = {C}")

# --- Distance: |AB| = sqrt((x2-x1)² + (y2-y1)²) ---
print(f"|AB| = {A.distance(B)}")      # 4
print(f"|AC| = {A.distance(C)}")      # sqrt(13)

# --- Lines: AB (through two points) ---
line_AB = Line(A, B)
print(f"Line AB: {line_AB.equation()}")  # y = 0

# --- Segments: the segment from A to B ---
seg = Segment(A, B)
print(f"Segment AB length = {seg.length}")  # 4

# --- Triangle △ABC ---
tri = Triangle(A, B, C)

# Sides opposite each vertex (standard labeling):
#   a = |BC| (opposite A), b = |AC|, c = |AB|
a = B.distance(C)   # opposite ∠A
b = A.distance(C)   # opposite ∠B
c = A.distance(B)   # opposite ∠C
print(f"\n△ABC sides: a={a}, b={b}, c={c}")

# Angles at each vertex
angle_A = tri.angles[A]
angle_B = tri.angles[B]
angle_C = tri.angles[C]
print(f"∠A = {angle_A}")
print(f"∠B = {angle_B}")
print(f"∠C = {angle_C}")

# --- Law of cosines: c² = a² + b² − 2ab·cos(C) ---
lhs = c**2
rhs = a**2 + b**2 - 2*a*b*cos(angle_C)
print(f"\nLaw of cosines check:")
print(f"  c² = {simplify(lhs)}")
print(f"  a²+b²−2ab·cos C = {simplify(rhs)}")
print(f"  Equal? {simplify(lhs - rhs) == 0}")

# --- Congruence & similarity ---
# Two triangles are similar (∼) iff angles match
D = Point(0, 0)
E = Point(8, 0)
F = Point(4, 6)
tri2 = Triangle(D, E, F)
print(f"\n△DEF is similar to △ABC? "
      f"{tri.is_similar(tri2)}")

# --- Perpendicularity: AB ⊥ CD ---
line_v = Line(Point(2, 0), Point(2, 5))
print(f"\nLine AB ⊥ vertical? "
      f"{line_AB.is_perpendicular(line_v)}")

# --- Parallelism: AB ∥ XY ---
line_XY = Line(Point(0, 3), Point(4, 3))
print(f"Line AB ∥ XY? "
      f"{line_AB.is_parallel(line_XY)}")

# --- Circle / sphere notation: S¹ ---
circ = Circle(A, 5)
print(f"\nCircle S¹ centered at {A}, r=5")
print(f"  area = {circ.area}")       # 25*pi
print(f"  circumference = {circ.circumference}")
