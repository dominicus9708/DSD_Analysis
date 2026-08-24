# Proofs and Classification Tests

## Proposition A — invariants are quotient maps with possible collisions

Let `I:X->Y` satisfy `x~y => I(x)=I(y)`. Then `I` is constant on each equivalence class and so defines

`Ibar([x])=I(x)`.

This is well-defined. `I` is complete exactly when `Ibar` is injective.

Therefore incompleteness is witnessed by two inequivalent objects with the same invariant value.

## Proposition B — rank is a strict-axis-property invariant but not complete

Under strict axis-property isomorphism, the relevant ambient carrier maps are linear isomorphisms and the realized lines are transported to the corresponding realized lines. Hence the realized span is carried isomorphically to the target realized span, preserving dimension. Therefore `arank` is invariant.

Construction 11.11 / Proposition 12.1 supplies equal-rank nonisomorphic axis-property models. Hence `arank` is not complete for the full axis-property signature.

## Proposition C — the displayed scalar summary is not automatically an invariant

Definition 12.3 permits arbitrary maps

`chi_tau:Desc->K`.

Take two distinct but strictly isomorphic descriptors `D~D'` in a comparison class and choose an allowed indicator map with

`chi(D)=0`, `chi(D')=1`.

With nonzero weight and all other terms equal, `Scal(D) != Scal(D')`.

Therefore Definition 12.3 alone does not make `Scal` an invariant.

If instead each `chi_tau` is invariant under strict isomorphism, then every term in the finite weighted sum is invariant, so `Scal` is invariant.

## Proposition D — collision makes an invariant summary incomplete

Assume every selected `chi_tau` is an invariant, so `Scal` is an invariant. If Proposition 12.4's collision hypotheses hold, then there exist `D,D'` with

`Scal(D)=Scal(D')`

but the corresponding models are not strictly isomorphic. Hence `Scal` is not complete on that comparison class.

Thus Proposition 12.4 becomes an ordinary incomplete-invariant witness once invariance of the selected indicators is separately imposed.

Without that extra hypothesis, it remains correctly stated as a collision obstruction for a classifier/summary.

## Proposition E — characteristic data can be invariant but incomplete

Under matrix similarity, characteristic polynomial, trace, determinant, and eigenvalue multiset are invariants.

Take

`A=[[0,0],[0,0]]`,

`B=[[0,1],[0,0]]`.

Both have characteristic polynomial `lambda^2`, trace `0`, determinant `0`, and eigenvalue multiset `{0,0}`. But `rank(A)=0` and `rank(B)=1`, and rank is similarity invariant. Therefore `A` and `B` are not similar.

This is a standard finite-dimensional analogue of a reduced DSD summary collision.

## Proposition F — compression is not intrinsically incomplete

A summary is complete precisely when it separates equivalence classes. There is no general theorem that a scalar codomain or finite tuple codomain alone forces incompleteness.

Standard canonical-form data provide positive examples: over an appropriate field, Jordan block data classify matrices up to similarity. On any finite comparison class, equivalence classes can also be assigned distinct scalar labels set-theoretically.

Therefore the valid DSD conclusion is about the chosen displayed finite-coordinate summary under a proved collision, not about all possible scalar encodings.

This matches the paper's explicit statement that Definition 12.3 is not an arbitrary set-theoretic scalar coding of the full descriptor.