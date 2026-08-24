# Finite Witnesses

## Witness A — incomplete standard similarity invariant

Let

`A = [[0,0],[0,0]]`,

`B = [[0,1],[0,0]]`.

Then:

- `char_A(lambda)=lambda^2=char_B(lambda)`;
- `tr(A)=tr(B)=0`;
- `det(A)=det(B)=0`;
- both have eigenvalues `0,0`;
- `rank(A)=0`, `rank(B)=1`.

Similar matrices have equal rank, so `A` and `B` are not similar. Characteristic/eigenvalue data are invariant but incomplete.

## Witness B — complete standard classifier after richer retention

For matrices over a field where Jordan form exists, retain the multiset of Jordan blocks. Two Jordan matrices are similar exactly when they have the same blocks up to order. The richer structured record is therefore complete for matrix similarity.

## Witness C — DSD equal rank, different full structure

Use Axis Property Construction 11.11:

- same Stage-VI base;
- same shared signature;
- same realized lines;
- rank three in both models;
- same bilinear data;
- same closure data;
- one declared unary property value equals `1` in one model and `2` in the other.

The rank agrees but strict isomorphism fails.

## Witness D — DSD displayed-summary collision

Use Proposition 12.4's hypothesis:

- equal rank;
- equal selected indicator values `chi_tau`;
- one typed defined property value differs.

Then the displayed scalar summaries agree while strict isomorphism fails.

If the `chi_tau` are separately required to be isomorphism invariants, this is an explicit witness that the scalar invariant is incomplete.

## Witness E — why arbitrary indicators are not automatically invariants

Take a one-axis descriptor with ambient carrier `R^2` and realized line `span(e1)`, and a strictly isomorphic copy with the same inherited channel data but realized line `span(e2)`. The linear isometry swapping `e1` and `e2` gives the structural isomorphism when all typed properties are transported accordingly.

Define an allowed indicator on the comparison class by

`chi(D)=1` if the represented line literally equals `span(e1)`, and `0` otherwise.

Then the two strictly isomorphic descriptors receive different indicator values. Hence an arbitrary `chi` in Definition 12.3 need not be an invariant.