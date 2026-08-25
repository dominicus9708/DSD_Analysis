# PHIL-003 — Argument 2: Temporal Snapshot Completeness and Dynamic Describability

Status: **preserved as a second argument alongside the original PHIL-003 record/target argument**.

This argument does not replace Argument 1 and does not modify Jackson's original Knowledge Argument into a different argument. It is a DSD dynamic extension that audits what follows when the phrase `all physical facts` is interpreted in a world whose physical state continues to change with time.

## 1. Relation to Argument 1

PHIL-003 now preserves two distinct arguments.

### Argument 1 — epistemic-record / fact-target non-implication

The first argument holds the relevant fact target fixed and asks whether a new epistemic record forces a new world-fact target:

`new epistemic record !=> new world-fact target`.

Its finite witness permits:

`Delta K != empty` and `Delta F = empty`.

### Argument 2 — temporal snapshot completeness / diachronic completeness non-implication

The second argument asks whether complete physical knowledge at one time remains complete after the physical world changes:

`snapshot completeness at t0 !=> diachronic completeness after t0`.

The two arguments are complementary. Argument 1 concerns identity and attribution across epistemic records and fact targets. Argument 2 concerns time-indexing, world evolution, accessibility, update, and propagation.

## 2. Application-level notation

Let:

- `F_P(t)` be the set of physical fact targets instantiated or relevant at time `t`;
- `K_M(t)` be Mary's epistemic records at time `t`;
- `tau_t : K_M(t) -> F_P(t) union F_other(t)` be the application-level target map;
- `T_M(t) := tau_t(K_M(t))` be the set of fact targets Mary knows at time `t`.

Define **snapshot physical completeness** at time `t` by

`C_snap(t) : F_P(t) subseteq T_M(t)`.

Define **diachronic physical completeness** on an interval `I` by

`C_dia(I) : for every t in I, F_P(t) subseteq T_M(t)`.

These are different predicates.

## 3. The argument

### Premise P1 — pre-opening snapshot completeness

Immediately before the door opens, at time `t0`, grant the strongest relevant snapshot premise:

`F_P(t0) subseteq T_M(t0)`.

Mary knows every physical fact in the chosen physical fact set at `t0`.

### Premise P2 — the world may evolve after t0

There may be a later time `t1 > t0` and a new physical fact target `f*` such that

`f* in F_P(t1)` but `f* notin F_P(t0)`.

For example, an event may begin at a remote location after `t0`.

### Premise P3 — no zero-delay global update bridge is contained in P1

Snapshot completeness at `t0` does not itself supply a rule requiring every later physical fact to enter Mary's epistemic target set at the same instant it comes into existence.

In particular, P1 does not entail

`for every t > t0, F_P(t) subseteq T_M(t)`.

A separate diachronic update/access condition would be needed.

### Conclusion

Therefore

`C_snap(t0) !=> C_snap(t1)`

and, more generally,

`C_snap(t0) !=> C_dia([t0,t1])`.

Complete physical knowledge at one time is not automatically complete physical knowledge at every later time.

## 4. Minimal countermodel

Take three times `t0 < t1 < t2`.

At `t0`:

- `F_P(t0) = {f_a, f_b}`;
- `T_M(t0) = {f_a, f_b}`.

Thus `C_snap(t0)` is true.

At `t1`, a remote event has occurred:

- `F_P(t1) = {f_a, f_b, f_remote}`;
- `T_M(t1) = {f_a, f_b}`.

Thus the world has gained a new physical fact while Mary has not yet received or integrated information about it. Hence `C_snap(t1)` is false.

At a later time `t2`, after an admissible information/access route has delivered the relevant information:

- `F_P(t2) = {f_a, f_b, f_remote}`;
- `T_M(t2) = {f_a, f_b, f_remote}`.

Snapshot completeness can therefore be restored later without having been preserved continuously.

## 5. DSD dynamic grounding

The Structural Reorganization Dynamics paper treats dynamics as a time-indexed family of admissible component-resolved states `S(t)`, rather than as one frozen state whose coordinates are silently changed. It also distinguishes regular value evolution from stronger status/domain/support transitions.

This supports the formal discipline required here: a completeness statement attached to one time slice should not be silently promoted to a statement about all later slices.

The dynamics paper additionally defines finite structural-information propagation only under supplied localization, metric-time, constitutive, locality, and support-faithfulness assumptions. Therefore a stronger conditional version is available:

If a remote physical change is represented by a localized distinguishability perturbation, the application supplies a propagation metric and an admissible finite propagation bound `c_bound`, the Mary-location is a positive metric distance `L` from the event, and the representation is local and support-faithful, then the perturbation need not be distinguishable at Mary's location before the propagation front can reach it.

This is a **conditional structural propagation statement**, not a claim that DSD itself derives the speed of light, neural processing time, or a physical information law for Mary's world.

## 6. Required bridge for sustained completeness

To preserve complete physical knowledge throughout an interval, an additional bridge must be stipulated. For example:

`UPDATE BRIDGE:` for every `t` in the interval, every physical fact target in `F_P(t)` is already in `T_M(t)`.

Equivalently:

`C_dia(I)` must be assumed or derived from a separate update/access theory.

This is substantially stronger than one-time snapshot completeness. In an evolving world, it amounts to continuous or effectively zero-lag completeness over the declared domain.

## 7. Scope relative to Jackson

This second argument does **not** by itself refute Jackson's canonical Knowledge Argument.

Jackson can restrict the target to physical facts about already existing color experiences of other people and can formulate the comparison so that later unrelated world events are irrelevant. In that restricted reading, Argument 2 identifies a time-indexing requirement but does not defeat the original target.

Accordingly:

- Argument 1 remains the primary PHIL-003 pressure on `epistemic novelty -> fact novelty`;
- Argument 2 is retained as an independent DSD dynamic audit of `snapshot completeness -> sustained completeness`;
- neither argument is deleted or merged into the other.

## 8. Conservative status

Project status:

**DSD-constructed dynamic extension of PHIL-003; preserved as a second argument; historical novelty not assessed and not claimed.**

The next external-literature audit, if opened later, should search specifically for time-indexed or diachronic variants of the Knowledge Argument rather than treating ordinary New Knowledge / Old Fact literature as a direct precedent for this second argument.