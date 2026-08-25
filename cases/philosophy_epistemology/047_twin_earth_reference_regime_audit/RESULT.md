# PHIL-004 / Global 047 — Twin Earth Reference-Regime Audit

Status: **first-pass analysis completed**.

## 1. Source target

Primary source: Hilary Putnam, **"The Meaning of 'Meaning'" (1975)**.

The first-pass result preserves Putnam's original target as linguistic reference/extension for natural-kind terms. Later broad mental-content externalism is treated as a further extension rather than silently folded into the source argument.

## 2. Neutral setup

Let:

- `O_E` = Earth Oscar;
- `O_T` = Twin-Earth Oscar;
- `I(x)` = selected narrow/internal psychological descriptor;
- `U(x)` = selected surface linguistic-use descriptor for the form `water`;
- `E(x)` = relevant environment/natural-kind structure;
- `R_B(x)` = broad/reference assignment under an environment-sensitive semantic signature;
- `R_N(x)` = narrow/internal semantic record under an internal-only signature.

The source setup admits:

`I(O_E) = I(O_T)`

and

`U(O_E) = U(O_T)`

while

`E(O_E) != E(O_T)`.

In the canonical example the relevant environmental kinds are Earth `H2O` and Twin-Earth `XYZ`.

## 3. Q1 — internal equality versus reference equality

### DSD result

The implication

`I(O_E) = I(O_T) -> R_B(O_E) = R_B(O_T)`

is not valid when the property signature for `R_B` explicitly includes environmental or causal-historical inputs.

Putnam's source argument is therefore **not refuted** by internal indistinguishability. His point is precisely that narrow psychological identity does not determine extension/reference.

### Classification

**Naive DSD attack fails.**

This is retained as a Mode-A-style failure record inside the ordinary PHIL case: DSD must not turn observer/internal equality into equality of an explicitly relational property.

## 4. Q2 — narrator-fixed difference versus subject-accessible difference

The source setup intentionally allows the narrator/analyst to distinguish `H2O` from `XYZ` while the 1750 speakers cannot.

Thus:

`E(O_E) != E(O_T)`

need not imply that either subject has an internal discriminator for that difference.

This is not a defect in Putnam's argument. It is part of the design: external reference can differ even when the relevant environmental microstructure is cognitively inert to the speakers.

### DSD result

The observer/regime distinction strongly **converges** with Putnam here. External analyst information and internally available subject information must remain separate.

## 5. Q3 — property signature before value comparison

The DSD axis-property discipline says that a property label alone has no mathematical content; profile, carrier, domain, assignment, and compatibility data must be supplied.

Applied here, the bare word `meaning` is too coarse for analysis.

At least the following semantic records can be separated:

1. internal/narrow psychological or conceptual record;
2. surface phonetic/syntactic form;
3. stereotype/ordinary recognition profile;
4. reference/extension;
5. environmental natural-kind relation;
6. causal-historical or community-mediated reference relation;
7. broad mental content, if that further layer is introduced.

Putnam already supplies substantial structure for the reference/extension layer: natural-kind sameness is not identified with mere observable similarity, and environment/indexical or social relations participate in extension determination.

Therefore a DSD criticism that merely says `meaning needs a signature` is **not enough to defeat Putnam**. The source already gives a constitutive externalist answer for the target reference property.

### Residual DSD sharpening

What remains useful is to keep the separate semantic records typed rather than allowing one umbrella word `meaning` to collapse them.

## 6. Q4 — same surface form versus same semantic record

The implication

`U(O_E) = U(O_T) -> full semantic identity`

fails in the source setup.

Putnam explicitly intends the same phonetic/syntactic form `water` to have different extensions on Earth and Twin Earth.

This is a direct convergence with DSD's reconstruction discipline: equality of a reduced/surface record does not reconstruct a complete support-tagged structure without an injectivity theorem.

### Classification

**Strong Mode-B-style convergence; no novelty.**

## 7. Q5 — linguistic reference versus broad mental content

The original Twin Earth argument first concerns linguistic reference/extension. It shows that intrinsic or narrow psychological identity does not suffice to determine the reference of the natural-kind term.

A further conclusion of the form

`same intrinsic subject state + different environment -> different belief/mental content`

requires an additional theory identifying or connecting linguistic reference conditions with propositional-attitude content individuation.

Later externalist literature supplies versions of that extension, but it must not be inserted into Putnam's original source as though no bridge were required.

### DSD result

This source-scope distinction **survives**. It is not a refutation of Putnam's linguistic argument; it is a boundary on what is licensed by that argument alone.

### Historical classification

The distinction is already standard in the externalism literature, which explicitly notes that Putnam's argument concerned linguistic content first and was later extended to mental content. Therefore there is **no historical novelty claim**.

## 8. Q6 — constitutive externalism versus inverse reconstruction

This is the strongest audit distinction.

### Constitutive externalism

If the semantic signature is explicitly of the form

`R_B = g(I, U, E, H, C)`

where `E` is environment, `H` a causal/historical relation, and `C` communal linguistic structure, then two internally identical speakers may have different reference values because the complete inputs differ.

This is not an illicit inference from internal output to hidden environment.

### Inverse reconstruction

A different task would attempt:

`I(O_E) = I(O_T)` or `U(O_E) = U(O_T)`

and then infer which external environment is present from those data alone.

That inverse inference is blocked by the Twin Earth construction itself because the internal/surface projection is deliberately non-injective across the two environments.

### DSD result

Putnam's central move belongs to the **constitutive** branch, not the illicit inverse branch. Therefore a reconstruction-based DSD attack against Putnam's main conclusion fails.

At the same time, the construction provides a clean DSD-style non-injectivity witness:

`same internal/surface descriptor != same full semantic-environmental record`.

## 9. Q7 — comparison-level matrix

The Earth/Twin-Earth comparison must retain separate equality statuses.

| Comparison level | First-pass relation |
|---|---|
| narrow/internal psychological state | equal by setup |
| selected surface form/use | equal by setup |
| relevant observable stereotype in 1750 | equal or intentionally indistinguishable |
| environmental microstructure/natural kind | different |
| causal/environmental embedding | different |
| broad reference/extension under Putnam's rule | different |
| narrow/internal semantic component, if admitted | may be equal |
| broad mental content | requires an additional content-individuation bridge |

Equality at the first three levels does not force equality at the later relational levels.

## 10. Semantic-Signature Fork

The first-pass DSD synthesis is a three-way fork.

### Branch N — internal/narrow signature

Let the semantic property depend only on the internal/surface profile:

`S_N = (I, U, stereotype)`.

Then the source setup permits:

`R_N(O_E) = R_N(O_T)`.

### Branch B — broad/externalist signature

Let the semantic/reference property include environment and causal/community embedding:

`S_B = (I, U, E, H, C)`.

Then Putnam's source rule permits:

`R_B(O_E) != R_B(O_T)`.

### Branch U — underspecified `meaning`

If no signature is fixed, a statement such as

`meaning_E = meaning_T`

or

`meaning_E != meaning_T`

is underdetermined because distinct legitimate semantic properties are being conflated under one label.

### Consequence

There is no contradiction in jointly holding:

`same narrow/internal semantic record`

and

`different broad reference/extension`.

They are values of different typed properties.

## 11. Finite witness

A finite witness is stored in:

`repro/check_semantic_signature_fork.py`.

It constructs Earth and Twin-Earth records with:

- identical internal descriptors;
- identical surface token/profile;
- different environmental natural kinds;
- equal narrow records under `S_N`;
- different broad references under `S_B`.

The same internal projection therefore has at least two distinct full semantic-environmental preimages.

## 12. External literature comparison

The post-analysis literature comparison yields three main results.

### 12.1 Putnam's linguistic-reference result is correctly preserved

Reference literature characterizes the Twin Earth argument as showing that intrinsic/narrow psychological properties do not by themselves determine the reference of natural-kind terms.

This agrees with the DSD verdict that the naive internal-equality attack fails.

### 12.2 Mental-content externalism is a later extension

Reference works explicitly distinguish Putnam's original linguistic argument from later extensions to propositional-attitude content by McGinn, Burge, and others.

This confirms the Q5 source-scope boundary.

### 12.3 Narrow/broad coexistence is established literature

A major response to content externalism accepts broad content while preserving a narrow component that is shared by intrinsic twins. Fodor-style narrow content and later two-dimensional approaches are examples.

This is very close to the DSD Semantic-Signature Fork:

- narrow/internal property may agree;
- broad/environment-indexed property may differ;
- neither claim eliminates the other when the signatures are kept distinct.

Therefore the philosophical core of this synthesis is **not historically new**.

## 13. What survives and what fails

### Survives

1. Putnam's central semantic-externalist conclusion for natural-kind reference survives the DSD audit.
2. Internal indistinguishability and external reference difference are structurally compatible.
3. Narrator knowledge and subject-accessible knowledge must be separated.
4. Linguistic-reference externalism does not by itself settle every thesis about mental content.
5. Narrow/internal semantic sameness can coexist with broad-reference difference if they are treated as different properties.

### Fails

1. `same internal state -> same broad reference`, without an internalist semantic rule.
2. `same word form -> same complete semantic record`.
3. attacking Putnam as if he inferred environment from internal output alone.
4. treating the subject's inability to distinguish H2O/XYZ as a counterexample to an argument that intentionally relies on such inability.
5. collapsing linguistic reference and broad mental content into one conclusion without an explicit bridge.

## 14. Final verdict

PHIL-004 does **not** refute Twin Earth.

Instead it produces a mixed but methodologically useful result:

1. a plausible naive DSD attack fails;
2. Putnam's constitutive externalist reference relation is compatible with DSD typed-property discipline;
3. DSD strongly converges with the established distinction between broad and narrow content;
4. DSD sharpens the case by representing narrow/internal record equality and broad/reference inequality as values of different semantic signatures rather than as contradictory answers to one untyped question;
5. the extension from linguistic reference to broad mental content remains a separate bridge question.

Project classification:

**PHIL-004 first pass complete — Putnam core survives; Mode-A-style failed attack preserved; Mode-B strong convergence with narrow/broad-content literature; DSD Semantic-Signature Fork retained as formal sharpening; no historical novelty claim.**