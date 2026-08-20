# Case 008 — Result

## Final judgment

**No internal contradiction of Primitive Axis-Property Axiom PI was found.**

However, the direct attack identifies a more important structural fact:

> PI itself is only the totality condition for an already single-valued primitive axis-line map. The assumptions that selected channels are the axis channels and that each selected channel is represented by at most one one-dimensional subspace are introduced before PI, in the primitive extension data and the function type of Definition 2.7.

Accordingly, a Stage-VI-only attack cannot force PI to fail without an additional bridge that constrains axis eligibility or admissible geometric realization.

## 1. PI is nontrivially satisfiable over arbitrary selected channels

Fix any Stage-VI formation record, any axis-applicable configuration `p`, and any selected inherited-channel family

`S=C^ax_A,p ⊆ C_L(p)`.

Choose the one-dimensional ambient carrier `E^amb_A,p=F` and define every selected channel to realize the unique line `F` in `Gr_1(F)`.

Then

`Dom(AxLine_A,p)=S`.

Hence PI is satisfiable for every selected family, regardless of its cardinality. No injectivity is required; Proposition 2.11 explicitly permits distinct tagged channels to realize the same line.

### Consequence

There is no cardinality obstruction of the form

`too many selected channels for a finite-dimensional carrier`.

A one-dimensional carrier is already sufficient for any selected set.

## 2. The only elementary carrier obstruction is zero dimension

If `C^ax_A,p` is nonempty and `E^amb_A,p={0}`, then `Gr_1(E^amb_A,p)=∅`, so no total map from the selected set exists.

Thus PI implies

`C^ax_A,p != ∅  =>  dim(E^amb_A,p) >= 1`.

This is an unstated but immediate derived admissibility condition. It is not a contradiction: a primitive presentation using a zero-dimensional carrier with a selected channel simply fails PI and is not a full axis-property model.

An optional proposition could state this consequence explicitly, but no correction is required.

## 3. The strongest vulnerability lies before PI: single-line functionality

Definition 2.7 already declares

`AxLine_A,p : C^ax_A,p ⇀ Gr_1(E^amb_A,p)`.

Because `AxLine` is a function, one selected channel cannot be associated with two distinct realized lines in the core language.

For one channel `c` and two distinct lines `ell_x != ell_y` in `F^2`, an external branching relation

`R(c)={ell_x,ell_y}`

is compatible with the inherited Formation record in the weak sense that Formation has no axis-line coordinate that could contradict it. Nevertheless this candidate is not a legal axis-property premodel because it violates the function type before PI is evaluated.

Therefore:

- **at most one line per selected channel** is a pre-axiom typing choice;
- **at least one line per selected channel** is supplied by PI totality;
- the phrase “exactly one line” is obtained from both layers together.

This is the principal result of the direct attack.

## 4. Is the single-line choice an unjustified hidden theorem?

No hidden theorem claim was found. The paper consistently presents a bare realized axis as a one-dimensional subspace and calls `AxLine` primitive extension data. It also states that the ambient carrier is representational rather than automatically physical.

So the current formal system is internally clear if its scope is read as:

> one selected inherited channel represents one tagged realized axis line.

What the system does **not** establish is that every conceivable extension of a Formation channel into geometry must be single-line/function-valued.

If a future application requires one inherited operational channel to have simultaneous branching, multi-line, cone-valued, distribution-valued, or set-valued realization, that application lies outside the present core type and requires an explicit extension.

This is a **scope assumption / pre-axiom typing choice**, not a contradiction.

## 5. PI does not validate axis eligibility

Remark 2.6 is decisive: the Formation system determines admitted operational channels but does not designate which of them are axes. The set `C^ax_A,p` is primitive extension data.

Therefore PI does not prove

`admitted operational channel => axis`.

Nor does it derive axis eligibility from quantity-kind, role, assigned value, or formation trace.

PI says only:

`if the extension selects c as an axis channel, the primitive axis-line map must be defined at c`.

Any stronger rule requires an additional selection predicate or bridge.

## 6. Why a Stage-VI counterexample cannot directly refute PI

The inherited Stage-VI record contains channel identity and formation trace but no axis-line geometry. The extension is free to

1. choose no axis-applicable configurations at all (Theorem 11.1), or
2. choose nonempty selected channel families and supply a one-dimensional carrier with the same line for every selected channel.

Thus every Stage-VI base admits both a vacuous PI-satisfying extension and, whenever one chooses selected channels, a simple nontrivial PI-satisfying line realization.

A meaningful empirical or structural falsification of PI therefore requires **additional theory** that says which Formation channels must be selected and what geometric realization constraints they must obey.

Without such a bridge, PI is a relative model constraint, not a derived geometric law of Formation.

## 7. Relation to existing paper claims

- Countermodel 9.6 already shows PI is independent: one may supply a selected channel and omit its line while satisfying PII.
- Theorem 11.1 proves only trivial extension existence and does not claim nontrivial axes are forced.
- Theorem 11.4 assumes an explicit line for every selected channel; it does not derive those lines from Stage VI.
- Construction 11.5 likewise chooses nonzero representatives explicitly.
- The discussion section does not claim that the ambient carrier or line map has universal physical semantics.

No theorem was found that incorrectly upgrades primitive supplied line data into a derived consequence of the Formation system.

## 8. Revision status

**No corrective revision is required.**

Two optional clarifications would improve resistance to overreading:

1. after Definition 2.7 or PI:
   > Single-valued axis-line realization is part of the present core typing choice. PI imposes totality on that already functional map; it does not derive functionality from the Formation background.

2. after Remark 2.6:
   > PI does not determine which admitted Formation channels are axis-eligible. Any such eligibility law requires an additional bridge or selection predicate.

A small derived proposition could also record

`C^ax_A,p != ∅ => dim(E^amb_A,p) >= 1`.

These are clarifications, not repairs.

## 9. Case classification

- Domain: direct internal axiom stress test
- DSD layer: Axis-Property Primitive PI / Stage P1 typing
- Falsification status: **PI not falsified**
- Internal contradiction: **none found**
- Most important vulnerability found: **single-line functionality is pre-axiom typing, not a consequence of PI**
- Stage-VI-derived axis eligibility: **not established**
- Cardinality obstruction: **none**
- Zero-dimensional carrier obstruction: **yes, as an ordinary PI admissibility consequence**
- Corrective paper revision required: **no**
- Optional scope clarification: **recommended**
- Direct-attack campaign status: **Case 008 complete; next target is Primitive PII**
