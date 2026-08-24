# Contradiction Audit

Status: COMPLETED.

## A. Direct-union homomorphism claim

Claim tested:

`Comp(F union G) = Comp(F) + Comp(G)` for all finite `F,G`.

### Result

**Falsified except in the trivial zero-term regime.**

Set `F=G={c}`. Since union is idempotent,

`F union F=F`.

A homomorphism law would force

`T(c)=2T(c)`,

hence `T(c)=0` in the vector space `W_L`. Because `c` is arbitrary, all terms must vanish.

This failure is external to DSD: the Formation Axiom System never asserts a union-monoid homomorphism.

## B. Disjoint finite additivity

Claim tested:

If `F intersect G=emptyset`, then

`Comp(F union G)=Comp(F)+Comp(G)`.

### Result

**Survives audit exactly.**

The finite sums separate without overlap and no extra DSD assumption is needed.

## C. Overlap correction

For arbitrary finite `F,G`, the exact identity is

`Comp(F)+Comp(G)=Comp(F union G)+Comp(F intersect G)`.

### Result

**Survives audit exactly.**

This identity explains both the disjoint-additive case and the obstruction to ordinary union homomorphism.

## D. DSD internal consistency

Checked against:

- ordinary finite-set source convention,
- no repeated exact channel in one finite set,
- channel identity retention,
- absence versus zero contribution,
- Stage-VI channel formation before Stage-VII term supply and finite composition,
- DSD's explicit permission of non-injective composition.

### Result

**No DSD contradiction found.**

The algebraic characterization does not alter any Formation axiom or closure clause.

## E. Category-strength inflation

Tested invalid inferences:

- equal aggregate => equal finite channel family,
- finite additivity => embedding,
- embedding => strict equivalence without the required bijective/reflection structure,
- one output equality => full structural equality.

### Result

**All rejected.**

The Formation paper already supplies a non-injective composition witness and a composite-level-coincidence-below-strict-equivalence result.

## F. Additional-encoding concealment

The free commutative monoid `N^(C_L)` permits repeated multiplicity of the same exact channel and supports a genuine homomorphic extension

`T_tilde(m+n)=T_tilde(m)+T_tilde(n)`.

### Result

**Valid only as additional encoding.**

It must not be identified with the original Stage-VII domain `P_fin(C_L)`.

## Final audit table

| Claim | Verdict |
|---|---|
| `Comp` is a full union-monoid homomorphism | falsified except `T=0` |
| `Comp` is finitely additive on disjoint finite supports | survives |
| overlap is handled by an intersection correction term | survives |
| free-commutative-monoid extension gives exact additive homomorphism | survives after additional encoding |
| equal composite output implies same source support | falsified |
| MATH-001 exposes a DSD axiom contradiction | no |

## Audit conclusion

MATH-001 does not refute the DSD Formation Axiom System. It sharply restricts the correct algebraic interpretation of Stage VII and rules out an over-strong union-homomorphism reading.
