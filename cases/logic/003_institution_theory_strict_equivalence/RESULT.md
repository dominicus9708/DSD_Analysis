# Case 003 — Result

## Final case judgment

**No falsification of the Formation Axiom System's strict-equivalence layer was found in Case 003.**

The three tests separate three different notions that should not be conflated:

1. structure-preserving renaming;
2. equality of a downstream composite;
3. satisfaction-preserving translation/reduct across signatures.

The current Formation paper handles the first two correctly and does not claim that the third is the same relation.

## 1. Renaming test

A finite one-point witness shows that if two regimes differ only by bijective renaming of their material, expression, configuration, quantity-kind, and role labels while preserving the anchored base, assignments, roles, and terms, then conditions (E1)–(E9) are satisfied.

Therefore strict descriptive equivalence does **not** depend on literal names.

This agrees with the paper's base-fixing remark: coordinate names may differ when their change preserves the anchored base structure.

### Verdict
Pass. No label-sensitivity defect found.

## 2. Same-output/different-structure test

A one-channel model with term `0` and a two-channel model with terms `1` and `-1` have equal selected composites but different channel cardinalities.

Because a strict comparison must induce a bijection of admitted channel sets, the models are strictly non-equivalent.

Thus

`composite coincidence  !=>  strict formation equivalence`.

This is exactly the structural distinction already formalized by Proposition 6.22.

### Verdict
Pass. The equivalence relation does not collapse structural distinctions into aggregate equality.

## 3. Institution-Theory comparison

Institution Theory uses signature-indexed sentences, models, and satisfaction. Under a signature morphism `phi: Sigma -> Sigma'`, sentence translation and model reduct are required to preserve satisfaction:

`M' |=_{Sigma'} Sen(phi)(e)  iff  Mod(phi)(M') |=_{Sigma} e`.

This condition can hold under a proper signature extension. A richer model may contain additional structure that is forgotten by reduct.

Therefore satisfaction-preserving translation is generally weaker than isomorphism of full model structures.

DSD strict base-fixed formation isomorphism, by contrast, compares complete formation descriptors over a fixed base using bijections and preservation/reflection conditions (E1)–(E9).

### Verdict
No contradiction. The two notions have different domains and purposes.

## 4. Important scope correction to the roadmap

The earlier lightweight roadmap was correct in calling Institution Theory a methodological/structural partial correspondence, but the proposed phrase "same proposition in two formalisms -> DSD strict-equivalence test" is too direct.

The corrected comparison is:

- Institution Theory: what sentence/model translations preserve satisfaction when signatures change;
- DSD strict equivalence: what bijective structure-preserving comparison identifies two full formation descriptors over a fixed comparison base;
- shared methodological principle: an equivalence/translation claim must explicitly state the preserved structure;
- non-correspondence: satisfaction preservation alone is not DSD strict equivalence.

This is a refinement of the DSD Analysis roadmap, not a correction to the Formation paper.

## 5. Is strict equivalence too strong?

Strict equivalence is deliberately strong. For example, two regimes can have identical realized assignments and channels while differing only by an extra unused value in one declared value space. The pointed value spaces then need not be bijective, so strict equivalence can fail.

That behavior is mathematically consistent with the definition because the relation compares the full declared descriptor, not merely the realized operational fragment.

The Institution-Theory comparison suggests a possible **additional weaker relation** for future work, such as a signature translation/reduct or observational/semantic equivalence that intentionally forgets selected coordinates while preserving a declared readout or theory.

Such a relation should not replace strict equivalence. It would answer a different question.

## 6. Formation-paper status

### Definition 6.10
No contradiction found.

### Corollary 6.12
Consistent with the finite renaming witness: strict equivalence induces channel/composite preservation.

### Proposition 6.22
Confirmed by the finite same-composite/different-channel witness.

### Entire Formation Axiom System
Not proved by this case. Primitive Axioms I–III and V were not independently retested here.

## 7. Revision status

**No corrective revision is required from Case 003.**

Optional future clarification only:

> Strict descriptive equivalence is an isomorphism notion for complete formation descriptors over a fixed comparison base. It is intentionally stronger than aggregate coincidence, observational equivalence, or general satisfaction-preserving translation across changing signatures.

A separate weaker translation/reduct layer may be studied later if cross-signature comparison becomes a project requirement.

## 8. Case classification

- Domain: mathematical/philosophical logic
- External node: Institution Theory
- DSD layer tested: full formation descriptors and strict base-fixed formation isomorphism
- Main distinction: structural isomorphism vs output coincidence vs satisfaction-preserving translation
- Mapping strength: **methodological/structural partial correspondence only**
- Falsification status: **not falsified**
- Correction required to Formation paper: **no**
- Roadmap refinement required: **yes — satisfaction preservation must not be identified with strict equivalence**
- Future design opportunity: **yes — optional weaker signature-translation/reduct equivalence layer**
- Cross-domain node status: **accepted as third provisional node, explicitly non-identical to DSD strict equivalence**

## References

- Kwon Dominicus, *Formation Axiom System — Dimensional-Structural Describability*, 2026, Section 6.
- Joseph A. Goguen and Rod M. Burstall, *Institutions: Abstract Model Theory for Specification and Programming*, Journal of the ACM 39(1), 95–146 (1992), DOI: 10.1145/147508.147524.
