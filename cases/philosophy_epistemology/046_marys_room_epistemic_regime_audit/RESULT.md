# PHIL-003 / Global 046 — Mary's Room: Epistemic-Regime Audit

Status: **first-pass analysis completed; two distinct DSD arguments preserved**.

PHIL-003 now keeps two complementary arguments rather than replacing the first with the second.

- **Argument 1 — epistemic-record / fact-target non-implication:** a new epistemic record does not by itself identify a new world-fact target.
- **Argument 2 — temporal snapshot-completeness / diachronic-completeness non-implication:** complete physical knowledge at one time does not by itself remain complete after the physical world changes.

The first is primarily a static attribution/reconstruction audit. The second is a dynamic time-indexing/update audit.

# Argument 1 — Epistemic Record versus Fact Target

## 1. Narrow target

The audit does not attempt to prove that qualia are physical or nonphysical.

It asks whether this inference is licensed without an additional bridge:

`Mary acquires a new epistemic record after release -> there exists a new nonphysical fact not contained in the pre-release physical fact set.`

## 2. Application-level encoding

Let:

- `F` be the set of world-fact targets relevant to the argument;
- `F_P subseteq F` be the physical fact targets;
- `K_0` be Mary's pre-release knowledge records;
- `K_1` be Mary's post-release knowledge records;
- `tau_0 : K_0 -> F` and `tau_1 : K_1 -> F` be application-level target maps saying which world fact a knowledge record is about.

Jackson stipulates:

`F_P subseteq tau_0(K_0)`

and the learning intuition supplies at least:

`K_1 \ K_0 != empty`.

Let `k_phi` be a genuinely new post-release record concerning what another person's red experience is like.

The crucial question is whether:

`k_phi in K_1 \ K_0`

entails

`tau_1(k_phi) notin F_P`.

It does not by logic alone.

## 3. Core DSD non-implication

The central result is:

`K_1 \ K_0 != empty`

**does not imply**

`tau_1(K_1) \ tau_0(K_0) != empty`.

A new knowledge record can target an already targeted fact under a newly available descriptive/access mode.

Finite countermodel:

- world fact target: `f_red_other`;
- pre-release record: `k_phys` with `tau_0(k_phys) = f_red_other`;
- post-release new record: `k_phen` with `tau_1(k_phen) = f_red_other`;
- `k_phen != k_phys`.

Then:

- Mary has a genuinely new epistemic record;
- Mary may even have genuinely new propositional knowledge if records are propositionally fine-grained;
- no new world-fact target has been introduced.

Thus the inference from **record novelty** to **target-fact novelty** requires an independent identification rule.

## 4. Why the Ability Hypothesis is not required

Jackson's 1986 reply explicitly argues that Mary gains more than abilities. PHIL-003 grants this for the sake of argument.

Even if `k_phen` is propositional/factual knowledge, it remains open whether it is:

1. a new fact target; or
2. a new proposition/representation/conceptual access route to an old fact target.

Therefore the DSD pressure survives Jackson's objection to an ability-only response.

## 5. Three completeness notions that must not be collapsed

### C-Fact — world-fact completeness

Mary's knowledge targets every physical fact:

`F_P subseteq tau_0(K_0)`.

### C-Representation — representational completeness

For every admissible way of representing/accessing a physical fact, Mary already has a corresponding record.

Jackson does **not** independently establish this stronger condition; the color-room setup is designed so that at least one experiential/phenomenal mode is unavailable before release.

### C-Ontology — ontological completeness

Every fact is physical:

`F = F_P`.

Physicalism is primarily the target ontological thesis. The Knowledge Argument attempts to move from failure of a pre-release epistemic/representational completeness condition to failure of ontological completeness.

That move needs a bridge connecting representation-sensitive knowledge novelty to fact individuation.

## 6. The strongest surviving Jackson branch

The DSD countermodel does not refute Jackson if the following bridge is independently defended:

`NEW-FACT BRIDGE:` every genuinely new item of propositional phenomenal knowledge must have a fact target not already contained in the complete physical fact set.

Equivalently:

`k_phi notin K_0 -> tau_1(k_phi) notin F_P`.

If a defensible individuation theory of facts/propositions supplies this bridge, the Knowledge Argument survives Argument 1.

## 7. Historical comparison for Argument 1

Argument 1 strongly converges with the established **New Knowledge / Old Fact** and phenomenal-concept / new-representation families.

Therefore the core philosophical objection is **not new**. The DSD contribution is a typed/set-theoretic sharpening in terms of knowledge-record carriers, target maps, and the invalidity of inferring target novelty from record novelty without a reconstruction/identification bridge.

Classification: **Mode B historical convergence with DSD-specific formal sharpening.**

# Argument 2 — Temporal Snapshot Completeness versus Diachronic Completeness

## 8. Dynamic target

Argument 2 does not ask whether a new epistemic record identifies a new fact. Instead it asks whether the premise `Mary knows all physical facts` remains true automatically after the world changes.

Let:

- `F_P(t)` be the physical fact targets at time `t`;
- `K_M(t)` be Mary's epistemic records at time `t`;
- `tau_t` be the application-level target map;
- `T_M(t) := tau_t(K_M(t))` be the fact targets Mary knows at time `t`.

Define snapshot completeness:

`C_snap(t) : F_P(t) subseteq T_M(t)`.

Define diachronic completeness on an interval `I`:

`C_dia(I) : for every t in I, F_P(t) subseteq T_M(t)`.

These are not the same condition.

## 9. Argument 2 reconstruction

### P1 — pre-opening snapshot completeness

At the instant immediately before the door opens, `t0`, grant:

`C_snap(t0)`.

### P2 — physical world evolution

There may be a later time `t1 > t0` and a physical fact target `f*` with:

`f* in F_P(t1)` and `f* notin F_P(t0)`.

For example, a new event may begin at a remote location after `t0`.

### P3 — no automatic zero-delay update bridge

P1 alone does not provide a rule requiring every later physical fact to enter Mary's known target set at the same instant it comes into existence.

Therefore P1 does not entail:

`for every t > t0, F_P(t) subseteq T_M(t)`.

### Conclusion

`C_snap(t0) !=> C_snap(t1)`

and more generally:

`C_snap(t0) !=> C_dia([t0,t1])`.

Complete physical knowledge at one time is not automatically complete physical knowledge at every later time.

## 10. Minimal dynamic witness

Take `t0 < t1 < t2`.

At `t0`:

- `F_P(t0) = {f_a, f_b}`;
- `T_M(t0) = {f_a, f_b}`.

At `t1`, after a remote event begins:

- `F_P(t1) = {f_a, f_b, f_remote}`;
- `T_M(t1) = {f_a, f_b}`.

At `t2`, after the relevant information/access route updates Mary:

- `F_P(t2) = {f_a, f_b, f_remote}`;
- `T_M(t2) = {f_a, f_b, f_remote}`.

Hence snapshot completeness is true at `t0`, false at `t1`, and can be restored at `t2`.

This establishes the bare non-implication:

`snapshot completeness at t0 !=> preserved completeness after t0`.

## 11. DSD dynamic grounding and propagation boundary

The Structural Reorganization Dynamics paper models dynamics as a time-indexed family of admissible component-resolved states `S(t)` rather than silently treating one static state as if its coordinates simply changed. This supports attaching completeness claims to explicit time slices.

That paper also permits finite structural-information propagation only under explicit localization, metric-time, constitutive, locality, and support-faithfulness assumptions.

Accordingly, Argument 2 has a stronger **conditional** form: if an application supplies a localized event, a propagation metric, a positive Mary/event distance, an admissible finite propagation bound, and a local support-faithful representation, then the event's distinguishability need not be available at Mary's location before the propagation front can reach it.

This does **not** identify the DSD structural propagation bound with the speed of light, neural delay, or any empirical information speed. Such a physical interpretation would require an additional constitutive bridge.

## 12. Required bridge for sustained completeness

To turn snapshot completeness into continuous completeness, the argument must add or derive an update condition such as:

`UPDATE BRIDGE:` for every `t` in the declared interval, every physical fact target in `F_P(t)` is already in `T_M(t)`.

This is a stronger premise than one-time completeness. In an evolving world it amounts to diachronic, effectively zero-lag completeness over the declared target domain.

## 13. Scope relative to canonical Mary's Room

Argument 2 does **not** by itself refute Jackson's canonical Knowledge Argument.

Jackson may restrict the relevant target to already existing facts about other people's color experiences and treat later unrelated events as outside the comparison domain. Under that restricted reading, Argument 2 identifies a time-indexing requirement rather than defeating Jackson's target.

Therefore:

- Argument 1 remains the primary PHIL-003 pressure on `epistemic novelty -> fact novelty`;
- Argument 2 is an independent dynamic pressure on `snapshot completeness -> sustained completeness`;
- neither replaces the other.

Argument 2 is currently classified as a **DSD-constructed dynamic extension; historical novelty not yet audited and not claimed**.

# Combined Verdict

## 14. What survives

1. Mary can acquire something epistemically significant after release.
2. Even genuine propositional novelty may be granted.
3. Jackson's core argument can survive Argument 1 if a strong fact-individuation / new-fact bridge is independently justified.
4. Jackson can avoid Argument 2 by fixing the relevant fact domain and time slice, or by explicitly assuming a diachronic update/completeness condition.

## 15. What fails as an unqualified inference

1. `new experience -> new nonphysical fact`.
2. `new knowledge record -> new world-fact target`.
3. `pre-release lack of one descriptive/access mode -> physical ontology incomplete`.
4. `complete physical knowledge at t0 -> complete physical knowledge at every t > t0`.
5. treating fact completeness, representation/access completeness, ontological completeness, snapshot completeness, and diachronic completeness as one predicate.

## 16. Final project classification

PHIL-003 is preserved as a **two-argument analysis**:

- **Argument 1:** Mode B strong historical convergence with New Knowledge / Old Fact; DSD formal sharpening; no historical novelty claim.
- **Argument 2:** DSD dynamic extension based on time-indexed completeness and update/propagation discipline; historical novelty not yet assessed or claimed.

The two arguments are cumulative but logically independent. Argument 1 can be tested in a fixed fact domain. Argument 2 becomes relevant when the physical fact domain or Mary's access state evolves with time.