# PHIL-003 / Global 046 — Mary's Room: Epistemic-Regime Audit

Status: **first-pass analysis completed**.

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

The thought experiment becomes clearer if three different completeness predicates are separated.

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

Equivalently, for the relevant class of knowledge records, new record identity must track new fact identity strongly enough that:

`k_phi notin K_0 -> tau_1(k_phi) notin F_P`.

If a defensible individuation theory of facts/propositions supplies this bridge, the Knowledge Argument survives the present DSD attack.

DSD itself does not decide that individuation theory.

## 7. Historical comparison

The result strongly converges with the established **New Knowledge / Old Fact** and phenomenal-concept / new-representation families.

Those views allow that Mary gains significant, and in some versions genuinely propositional, knowledge after release while maintaining that the truthmaking physical fact was already present in her pre-release physical knowledge under a different conceptualization.

Therefore:

- the core philosophical objection is **not new**;
- the DSD contribution here is a typed/set-theoretic sharpening in terms of knowledge-record carriers, target maps, and the invalidity of inferring target novelty from record novelty without a reconstruction/identification bridge.

Classification: **Mode B historical convergence with DSD-specific formal sharpening.**

## 8. What survives and what fails

### Survives

1. The learning intuition: Mary can acquire something epistemically significant after release.
2. Even genuine propositional novelty may be granted.
3. The question whether phenomenal access is reducible to physical description remains substantive.
4. Jackson's argument survives if a strong fact-individuation / new-fact bridge is independently justified.

### Fails as an unqualified inference

1. `new experience -> new nonphysical fact`.
2. `new knowledge record -> new world-fact target`.
3. `pre-release lack of one descriptive/access mode -> physical ontology incomplete`.
4. treating fact completeness, representational completeness, and observer-access completeness as one predicate.

## 9. Final verdict

The Knowledge Argument is **not destroyed wholesale** by DSD.

Its strongest unqualified step is narrowed to a bridge problem:

`epistemic novelty -> ontological/fact novelty`.

Without an explicit bridge, a finite countermodel allows:

`new propositional/phenomenal knowledge record + old physical fact target`.

This is a strong historical convergence with the New Knowledge / Old Fact family rather than a novel philosophical refutation.

Project classification:

**PHIL-003 completed first pass — Mode B strong convergence; DSD formal sharpening; no historical novelty claim; Jackson's argument survives conditionally on an independently defended fact-individuation bridge.**