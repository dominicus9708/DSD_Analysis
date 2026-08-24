# Finite Witnesses

Global case: 030
Domain case: MATH-003

## Witness A — same carrier, different group structure

Let the carrier be `U={0,1,2,3}`.

Structure A is cyclic of order four. It contains an element of order four.

Structure B is the Klein four group. Every nonidentity element has order two.

The underlying set and cardinality agree, but the groups are not isomorphic because element order is preserved by group isomorphism.

Purpose: falsify `same carrier => same algebraic structure`.

## Witness B — same vector carrier and rank, different bilinear structure

Let `V=R^2`.

Define

- `b1(x,y)=x1*y1+x2*y2`,
- `b2(x,y)=x1*y1-x2*y2`.

Both are symmetric nondegenerate bilinear forms on the same two-dimensional vector space. The first is positive definite; the second has one positive and one negative direction.

No invertible linear map can pull one form to the other because inertia is preserved under real congruence.

Purpose: show that vector-space dimension is insufficient after bilinear structure is added.

## Witness C — positive boundary: bare vector spaces

Let `V` and `W` be finite-dimensional vector spaces over the same field with `dim V=dim W=n`.

Choose bases of length `n` and map one basis bijectively to the other. The linear extension is an isomorphism.

Purpose: falsify the overstatement `dimension/rank is never complete`.

## Witness D — DSD same rank, different unary property

Use Axis Property Construction 11.11:

- same Stage-VI base,
- same shared signature,
- same realized rank-three line family,
- same bilinear and closure data,
- same unary property kind,
- assigned value `1` in one extension and `2` in the other.

Strict axis-property isomorphism must preserve that typed property value, so the complete descriptors are not strictly isomorphic.

Purpose: direct DSD witness for `same rank != same enriched structure`.

## Witness E — DSD same matrix size, different encoded relation

Use Axis Property Proposition 12.2:

- two `2x2` block declarations,
- same tagged axes and entry carrier,
- all entries equal except one defined relation entry, `0` versus `1`.

Block size agrees but representation-inclusive strict isomorphism fails.

Purpose: falsify `same matrix size => same represented structure`.

## Witness F — same bare line, different tagged property

Use two distinct admitted channels `c1 != c2` that realize the same line `ell`. For a tag-sensitive unary property, assign distinct values on `(c1,ell)` and `(c2,ell)`.

The bare line is identical, but the full tagged inputs and property values differ.

Purpose: show why forgetting the formation tag can destroy DSD property information.
