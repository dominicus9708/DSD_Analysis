# Reproducibility

No Python program is required for MATH-005.

Reason:

- the direct-sum criterion is an exact elementary theorem about injectivity of the sum map;
- the DSD fixed-support criterion is already an exact kernel theorem in the source paper;
- the Stage-VII support criterion follows by one subtraction and coefficients in `{-1,0,1}`;
- all decisive witnesses use at most three scalar channel terms.

A brute-force subset-sum script could verify particular finite examples, but it would not strengthen the proof and would add an unnecessary implementation layer.

The reproducible objects are therefore the explicit finite witnesses and the algebraic derivations recorded in `PROOF.md` and `FINITE_WITNESS.md`.
