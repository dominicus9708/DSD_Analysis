# Formal Comparison Model

Global case: 030
Domain case: MATH-003

## Layer 0 — underlying carrier

Let `U` denote an underlying set or let `V` denote a vector space over a fixed field.

Carrier identity means only that the same elements are available. It does not yet fix operations, relations, forms, property assignments, or representations.

## Layer 1 — bare linear structure

For vector spaces `(V,+,scalar multiplication)`, finite dimension over a fixed field is a complete isomorphism invariant.

Thus if `dim V = dim W < infinity` over the same field, then `V ~= W` as vector spaces.

This is the positive boundary case against universal incompleteness claims.

## Layer 2 — enriched structures

An enriched structure adds operations, relations, forms, labels, or typed partial assignments to the carrier. Examples:

- `(U,*)` for a group operation,
- `(V,b)` for a symmetric bilinear form,
- `(V,{Xi_varpi})` for typed property maps,
- `(V,b,{Xi_varpi},Rep,Closure,...)` for the DSD axis-property layer.

Isomorphism must preserve every coordinate required by the relevant signature.

## Standard finite witnesses

### Group witness

On a four-element carrier, compare a cyclic group of order four and the Klein four group. The carrier cardinality agrees, but one structure has an element of order four and the other does not. They are not group-isomorphic.

### Bilinear witness

On `R^2`, compare

`b_plus(x,y) = x1*y1 + x2*y2`

and

`b_pm(x,y) = x1*y1 - x2*y2`.

The underlying vector carrier and dimension agree. The first form is positive definite and the second indefinite; no linear isometry identifies them.

## DSD mapping

The DSD axis-property system fixes a Stage-VI formation base and then adds:

1. selected axis channels,
2. realized line map,
3. tagged realized axes,
4. typed property declarations and partial assignments,
5. optional bilinear data,
6. optional representation and closure layers,
7. complete descriptor.

Therefore `arank` is analogous to a coarse invariant of one underlying linear layer, not to the complete signature of the enriched model.

## Classification rule

For every proposed invariant `I`, ask:

1. What signature is being classified?
2. Does equality `I(A)=I(B)` imply an isomorphism in that signature?
3. If not, exhibit the smallest missing preserved coordinate.
4. If yes in a restricted signature, record that restricted completeness rather than calling the invariant universally incomplete.
