# Reproducibility Protocol

## Minimal manual checks

No code is required for the decisive witnesses.

### Check 1 — fixed-support kernel

Use `F={a,b}`, `W_L=R`, and records

`x=(1,-1)`, `y=(0,0)`.

Verify `S_F(x)=S_F(y)=0` and `x-y in ker S_F`.

### Check 2 — failure of union congruence

Use `T(a)=T(b)=1`,

`F={a}`, `G={b}`, `H={a}`.

Verify:

1. `Comp(F)=Comp(G)=1`;
2. `Comp(F union H)=1`;
3. `Comp(G union H)=2`.

Therefore equal-aggregate classes are not stable under union.

### Check 3 — additive lift

In the free vector space with basis `e_a,e_b`, verify

`L_T(e_a-e_b)=0`.

This is equivalent to `Comp({a})=Comp({b})`.

### Check 4 — zero-padding semantic loss

Compare the DSD support-tagged records

`({a},(0))` and `(emptyset,())`.

Verify that both map to the same naive zero-padded value vector while remaining distinct DSD records.

## Completion criterion

The case is independently reconstructible when a reader can verify:

- the fixed-support linear kernel statement,
- the two-channel congruence counterexample,
- the free-vector-space kernel lift,
- the absence-versus-zero encoding failure,

without relying on software or numerical approximation.