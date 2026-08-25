# PHIL-004 / Global 047 — Twin Earth Reference-Regime Audit

Status: **first-pass analysis completed; precedent-convergence case**.

## 1. Primary result

PHIL-004 is not best characterized as a DSD attack on Putnam.

The central result is that Putnam's Twin Earth argument independently preserves several structural distinctions that are strongly congenial to the Formation Axiom System, Axis-Property Axiom System, and DSD reconstruction discipline.

Accordingly, PHIL-004 is recorded as a **precedent-convergence case**: an established external argument whose source-level reasoning survives because it already respects a structural rule that DSD also enforces.

This is not a claim that Putnam was doing DSD, that the two theories are identical, or that DSD has historical priority.

## 2. Source setup

Let:

- `O_E` = Earth Oscar;
- `O_T` = Twin-Earth Oscar;
- `I(x)` = selected narrow/internal psychological descriptor;
- `U(x)` = selected surface linguistic-use descriptor for `water`;
- `E(x)` = relevant external environmental/natural-kind structure;
- `R_N(x)` = narrow/internal semantic record under an internal-only signature;
- `R_B(x)` = broad/reference assignment under an environment-sensitive signature.

The canonical setup permits:

`I(O_E) = I(O_T)`

and

`U(O_E) = U(O_T)`

while

`E(O_E) != E(O_T)`.

The environmental kinds are Earth `H2O` and Twin-Earth `XYZ`.

## 3. Convergence A — reduced/internal equality does not fix a fuller relational property

If broad reference is defined through a signature such as

`R_B = g(I, U, E, H, C)`,

where `E` is environment, `H` causal/history information, and `C` community structure, then equality of `I` and `U` alone does not force equality of `R_B`.

Thus:

`I(O_E) = I(O_T)`

is compatible with

`R_B(O_E) != R_B(O_T)`.

This mirrors the DSD discipline that equality of a selected/reduced descriptor does not imply equality of a fuller typed structure or of a property whose signature contains additional inputs.

Putnam's argument therefore does not need to be rescued from this DSD audit; its own structure already respects the distinction.

## 4. Convergence B — narrator information and subject-accessible information remain separate

The narrator/analyst can distinguish `H2O` from `XYZ` while the 1750 speakers cannot.

Therefore:

`E(O_E) != E(O_T)`

need not imply that either subject has an internal discriminator for the difference.

This is an intended part of Twin Earth and strongly parallels DSD's observer/regime discipline: externally available information must not be silently inserted into an internal subject's admitted description.

## 5. Convergence C — property signature precedes value comparison

The umbrella word `meaning` is too coarse for a typed comparison.

At least the following layers can be separated:

1. narrow/internal psychological or conceptual record;
2. surface phonetic/syntactic form;
3. stereotype/ordinary recognition profile;
4. reference/extension;
5. environmental natural-kind relation;
6. causal-historical/community-mediated relation;
7. broad mental content, if separately introduced.

This aligns directly with the Axis-Property rule that a property label alone does not determine mathematical content; signature/profile/carrier/domain/assignment data must be fixed.

Putnam already supplies substantial constitutive structure for the reference/extension layer. The DSD contribution is therefore not to say that Putnam forgot a signature, but to formalize why multiple semantic records should not be collapsed under one untyped label.

## 6. Convergence D — equal surface records do not reconstruct full semantic-environmental structure

The same surface form `water` and matching internal state are compatible with different environmental embeddings.

Hence the projection from full semantic-environmental records to the selected internal/surface descriptor is non-injective.

This independently mirrors DSD's reconstruction discipline:

`equal reduced/surface record !=> equal full typed source structure`.

Twin Earth is therefore a particularly clear philosophical precedent for this structural rule.

## 7. Semantic-Signature Fork

The retained DSD formalization separates three branches.

### Branch N — narrow/internal signature

`S_N = (I, U, stereotype)`.

The source setup permits:

`R_N(O_E) = R_N(O_T)`.

### Branch B — broad/externalist signature

`S_B = (I, U, E, H, C)`.

Under Putnam's externalist rule:

`R_B(O_E) != R_B(O_T)`.

### Branch U — underspecified `meaning`

Without a fixed signature, asking simply whether

`Meaning(O_E) = Meaning(O_T)`

or not is under-specified because different legitimate semantic properties have been merged under one label.

Therefore:

`same narrow/internal semantic record`

and

`different broad reference/extension`

are not contradictory statements. They concern different typed properties.

The Semantic-Signature Fork is recorded as a **DSD typed restatement and sharpening of a structure already present in the precedent argument**, not as a new refutation.

## 8. Source-scope boundary

Putnam's 1975 Twin Earth argument first targets linguistic reference/extension for natural-kind terms.

A stronger conclusion of the form

`same intrinsic subject state + different environment -> different belief/mental content`

requires an additional content-individuation theory or bridge.

Later externalist literature develops that extension. Therefore the distinction between linguistic reference and broader mental-content externalism is preserved, but no historical novelty is claimed for this boundary.

## 9. Subordinate negative-control check

One hypothetical inference is useful only as a check on DSD itself:

`same narrow/internal state -> same broad reference`.

This inference fails when broad reference explicitly has environmental/causal/community inputs.

The project retains this as a **subordinate negative-control result** demonstrating that DSD must respect its own typed-property discipline. It is not the principal characterization of Putnam and is not treated as an adversarial attack that the source argument happened to survive.

## 10. Finite witness

The reproducibility witness constructs Earth and Twin-Earth records with:

- equal internal descriptors;
- equal surface forms;
- different environmental kinds;
- equal narrow records under `S_N`;
- different broad references under `S_B`.

Thus one reduced/internal projection has multiple full semantic-environmental preimages.

Run:

```bash
python cases/philosophy_epistemology/047_twin_earth_reference_regime_audit/repro/check_semantic_signature_fork.py
```

Expected key output:

```text
same_internal: True
same_surface: True
narrow_equal: True
broad_reference_equal: False
projection_noninjective_witness: True
witness_passed: True
```

## 11. Historical comparison

Post-analysis literature comparison confirms that:

1. Putnam's source argument is a classic semantic-externalist argument showing that narrow/intrinsic psychological state alone does not determine natural-kind reference;
2. later literature separately develops broad mental-content externalism;
3. narrow-content, two-factor, and two-dimensional approaches already preserve coexistence between an intrinsic/narrow component and an externally individuated component.

Therefore the philosophical content is established prior art.

The project-level significance is not novelty but **independent structural recurrence**.

## 12. Final classification

**PHIL-004 / Global 047 — precedent convergence.**

Putnam's Twin Earth is recorded as an established predecessor whose core distinctions independently align with DSD Formation/Axis-Property/reconstruction rules:

- internal/reduced equality need not determine a fuller relational property;
- observer/narrator information and subject-accessible information remain distinct;
- semantic values depend on a declared property signature;
- equal surface records do not reconstruct full semantic-environmental structure.

DSD contributes a typed formal restatement through the Semantic-Signature Fork, not a historical-priority claim and not a new philosophical refutation.

Within the current philosophy-analysis sequence, this is treated as a relatively uncommon and especially informative outcome: the external argument is better understood as a structurally aligned precedent than as a target that needed to be attacked.