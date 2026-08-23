# LAW-005 Structural Model

## 1. Purpose

Represent legal/institutional acts without forcing all statuses into a binary `valid/invalid` value.

## 2. Generic carrier

Let a legal-act instance be

`a = (actor, act_type, object, regime, role, time, source_conditions)`.

The underlying event or declaration is preserved even if a later legal rule gives it no effect.

## 3. Status coordinates

Use separate partial status maps where the source regime actually distinguishes them:

- `F(a)` — formation/existence status in the selected legal regime;
- `E(a)` — present operative/effect status;
- `D(a)` — defect status, including the type and source of any defect;
- `R(a)` — remedial/defeasibility status, such as avoidable, confirmable, terminable, set-aside-eligible, suspended;
- `X(a)` — recognition/enforcement status in a receiving or downstream regime.

These maps are application-side structures. They are not Primitive Axiom V itself.

## 4. Non-collapse conditions

The candidate model refuses the following identities unless the source rule supplies them:

`F(a) = formed` does not imply `D(a) = none`.

`D(a) != none` does not imply `F(a) = absent`.

`D(a) != none` does not imply `E(a) = no_effect` under every regime.

`E(a) = operative` does not imply `R(a) = indefeasible`.

`X(a) = recognition_refused` does not imply `F(a) = absent`.

## 5. Rule-indexed consequence map

For a defect or procedural condition `delta`, define an external legal consequence operator

`C_rule(a, delta, regime, time) -> status package`.

Possible outputs may include, depending on the source rule:

- nonformation;
- formed but not yet effective;
- formed and binding;
- avoidable by a protected party;
- confirmed and no longer avoidable;
- partly ineffective or severable;
- suspended;
- set aside;
- recognition refused;
- enforcement refused;
- terminated prospectively;
- other regime-specific outcomes.

No universal default output is assumed.

## 6. Witness mappings

### CISG

The Convention governs formation while generally excluding validity from Article 4's scope.

Model consequence: `F` and validity-related status cannot be identified merely because both concern the same contract.

### UNIDROIT

An agreement may conclude a contract, while a later validity analysis may supply avoidance rights. Conditions may postpone present effect, and mandatory-rule infringement has rule-dependent consequences.

Model consequence: `F`, `E`, `D`, and `R` are genuinely distinct source coordinates.

### UNCITRAL Model Law on Arbitration

An award may exist and be treated as binding while recognition or enforcement is separately requested and may be refused; setting aside or suspension is another status.

Model consequence: source existence/formation and downstream `X` status must be distinguished.

## 7. DSD Formation bridge

The useful DSD correspondence is not `legal formation = Formation admission`.

The correspondence is structural:

- source stages remain typed rather than collapsed;
- later legal statuses may remain undefined until the governing rule applies;
- an existing event is not deleted merely because its downstream legal effect is absent;
- role and regime must remain in the application carrier;
- a downstream result does not reconstruct the complete earlier legal status package.

## 8. Dynamics boundary

If `a` is avoidable at `t1` and confirmed at `t2`, or an award is binding at `t1` and set aside at `t2`, static descriptors can represent both states:

`S(a,t1) != S(a,t2)`.

Formation alone does not derive the legal transition.

The transition relation

`T_legal : S_t -> S_(t+1)`

is supplied by the source law. DSD Dynamics would be relevant only if the research question later concerns structural transition itself.

## 9. Axis-Property audit

No realized-axis semantics are supplied by the selected sources. Axis-Property structure is therefore not needed for the core result.
