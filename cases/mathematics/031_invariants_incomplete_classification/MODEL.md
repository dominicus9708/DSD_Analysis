# Mathematical Model

Let `X` be a comparison class and let `~` be an equivalence relation on `X`.

## Invariant

A map

`I:X->Y`

is an invariant for `~` when

`x~y => I(x)=I(y)`.

Equivalently, `I` factors through the quotient map `q:X->X/~`.

## Complete invariant

An invariant is complete when

`I(x)=I(y) => x~y`.

Hence `I` is complete iff its induced map

`Ibar:X/~ -> Y`

is injective.

## DSD specialization

Take `X` to be a fixed comparison class of complete axis-property descriptors/models over the fixed Stage-VI base and shared signature, and let `~` be strict axis-property isomorphism.

Candidate reduced maps include:

- realized-axis rank,
- active representation/block size data,
- selected indicator families,
- the displayed finite-coordinate scalar summary,
- later static aggregates or dynamic readouts.

The classification question is always relative to the chosen equivalence relation and signature.

## Scalar summary condition

For

`Scal(D)=kappa(arank(D))+sum_tau omega_tau chi_tau(D)`,

`Scal` is automatically an invariant only if every contributing coordinate is invariant. `arank` is preserved by strict isomorphism because the induced carrier isomorphism preserves the realized span dimension. But arbitrary indicator maps `chi_tau` are not invariant merely by being called indicators.

Therefore:

- invariant indicators -> invariant weighted scalar summary;
- arbitrary indicators -> summary/readout only, with no automatic invariant status.

Completeness is a further independent property.