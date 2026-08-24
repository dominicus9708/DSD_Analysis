# Reproducibility

Global case: 030
Domain case: MATH-003

## No code required

No Python enumeration is needed for this case. Every decisive witness is finite and reconstructible by hand.

## Reconstruction A — same carrier, different groups

1. Fix a four-element set `U`.
2. Put a cyclic order-four group operation on `U`.
3. Put a Klein-four group operation on the same `U`.
4. Check that the cyclic structure contains an element of order four.
5. Check that every nonidentity element in the Klein structure has order two.
6. Since isomorphisms preserve element order, conclude the group structures are not isomorphic.

## Reconstruction B — same vector carrier, different bilinear forms

1. Fix `V=R^2`.
2. Define matrices `B1=diag(1,1)` and `B2=diag(1,-1)`.
3. Evaluate `x^T B1 x` and verify it is positive for every nonzero `x`.
4. Evaluate `x^T B2 x` at `e1` and `e2`; obtain positive and negative values.
5. Conclude the forms have different inertia and are not congruent/isometric over `R`.

## Reconstruction C — dimension-complete boundary

1. Fix two `n`-dimensional vector spaces over the same field.
2. Choose ordered bases of length `n`.
3. Map one basis bijectively to the other.
4. Extend linearly.
5. The resulting map is bijective and linear, hence an isomorphism.

## Reconstruction D — DSD same-rank witness

Use Axis Property Construction 11.11:

1. keep the Stage-VI base fixed;
2. keep the shared signature fixed;
3. keep the same three realized lines;
4. keep bilinear and closure data fixed;
5. change one defined unary property value from `1` to `2`;
6. apply strict-isomorphism preservation of typed property values;
7. conclude the two complete descriptors are not strictly isomorphic despite equal rank.

## Reconstruction E — same-line / different-tag witness

1. choose distinct admitted channels `c1,c2`;
2. realize both as the same one-dimensional subspace;
3. choose a declared tag-sensitive unary property;
4. assign distinct defined values on the two tagged inputs;
5. project both tagged inputs to the line coordinate;
6. observe that line equality remains while property equality fails.

## Completion criterion

The case is reproducible when each positive and negative classification can be reconstructed without hidden coordinate changes, and when the bare-vector-space exception is stated explicitly.
