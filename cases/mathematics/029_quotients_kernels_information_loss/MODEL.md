# Formal Comparison Model

## 1. Fixed support

Fix finite `F subset C_L`. The DSD static aggregation paper defines the linear map

`S_F : W_L^F -> W_L`,

`S_F((y_c)_{c in F}) = sum_{c in F} y_c`.

This is an ordinary linear map. Hence `ker S_F` is a linear subspace and

`W_L^F / ker S_F ~= im(S_F)`.

If `F` is nonempty, `S_F` is surjective: for any `w in W_L`, place `w` in one coordinate and zero in the rest. Therefore

`W_L^F / ker S_F ~= W_L`.

This quotient identifies exactly those fixed-support component records whose coordinatewise difference lies in `ker S_F`.

## 2. Varying finite supports

On the Formation Stage-VII carrier define

`F ~_Comp G  iff  Comp(F)=Comp(G)`.

Because equality in `W_L` is reflexive, symmetric, and transitive, `~_Comp` is always an equivalence relation. Therefore the quotient set

`P_fin(C_L) / ~_Comp`

exists and is canonically in bijection with `im(Comp)` as a set.

However, to define a quotient join-semilattice using union, `~_Comp` must be a congruence:

`F ~ F' and G ~ G'  =>  F union G ~ F' union G'`.

MATH-002 tests this condition directly.

## 3. Additive lift

Let `K` be the scalar field and let `K^(C_L)` denote the free vector space of finitely supported coefficient functions on channels. Define

`L_T(a) = sum_c a(c) T_L(c)`.

Then `L_T` is linear and

`K^(C_L) / ker L_T ~= im L_T`.

For a finite support `F`, let `1_F` be its 0/1 indicator. Then

`L_T(1_F)=Comp(F)`.

Thus a collision `Comp(F)=Comp(G)` is equivalent to

`1_F - 1_G in ker L_T`.

This is an exact linear-kernel encoding, but it is additional structure beyond the original finite-set carrier.

## 4. Support-semantic warning

A naive finitely supported value function `y:C_L->W_L` cannot faithfully encode DSD support-tagged records if zero coordinates are allowed, because

- channel absent, and
- channel selected with value zero

both become the same zero coordinate.

A faithful global encoding must retain presence/support separately, for example by a support tag plus value data. Therefore a single ordinary vector-space carrier is not automatically a faithful replacement for the DSD disjoint-union record carrier.