# Source Notes

Global case: 030
Domain case: MATH-003

## DSD source: Axis Property Axiom System

The current axis-property paper explicitly separates:

- the inherited Stage-VI operational channel tag `c=(p,a,lambda,v,rho)`,
- the bare realized one-dimensional subspace `ell_c`,
- tagged realization records `(c,ell_c)`,
- typed property assignments,
- optional matrix/tensor/operator/quaternion representations,
- complete axis-property descriptors and strict isomorphism.

Relevant internal statements:

1. Distinct tagged channels may realize the same line; channel multiplicity need not determine rank.
2. A tag-sensitive property may assign different values to two tagged inputs that project to the same bare line.
3. A bare line does not generally determine unary properties.
4. Matrix size does not determine realized-axis rank.
5. Optional representations are not identified with the abstract property system.
6. Construction 11.11 gives two rank-three extensions over the same base, signature, and realized lines with different unary property values; the complete descriptors are not strictly isomorphic.
7. Proposition 12.1: equal rank does not imply strict property equivalence.
8. Proposition 12.2: equal matrix size does not imply strict property equivalence.
9. Corollary 12.5: rank, matrix size, and selected finite-coordinate summaries are incomplete classifiers on the stated comparison classes.

## Standard mathematics comparison set

### Plain vector spaces

Over a fixed field, finite-dimensional vector spaces are classified up to linear isomorphism by dimension. Thus equal dimension is sufficient in this restricted signature.

### Groups on the same carrier

The same underlying finite set can support nonisomorphic group structures. A minimal standard family is a four-element carrier carrying either the cyclic group `C4` or the Klein four group `V4`. Same cardinality and same underlying set do not determine the group operation.

### Symmetric bilinear spaces on the same vector carrier

The same real vector space `R^2` can carry different nondegenerate symmetric bilinear forms, e.g.

- positive-definite form with matrix `diag(1,1)`,
- indefinite form with matrix `diag(1,-1)`.

They are not isometric as real symmetric bilinear spaces because their inertia/signature differs.

### Matrices as representations

Equal matrix size alone never specifies the represented map or form. Classification depends on the relevant equivalence relation: equality, similarity, congruence, unitary equivalence, etc. A matrix is data representing a structure relative to choices; matrix dimension alone is only coarse metadata.

## Comparison discipline

The DSD claim should be matched to enriched structures, not to bare vector spaces. The correct standard principle is:

> An underlying carrier and coarse invariant can be fixed while additional operations, relations, property values, or representations vary; isomorphism is determined relative to the full signature.

The vector-space classification boundary must be retained as a counterweight against the overstatement that rank is intrinsically never complete.
