# Case 006 — Result

## Final case judgment

**No falsification of the Formation Axiom System was found in Case 006.**

Public Announcement Logic (PAL) is not a direct semantic model of DSD observer/regime-dependent describability. It supplies a useful stress test because it sharply separates three things: factual truth at the actual world, an agent's epistemic alternatives, and an update that changes those alternatives.

The DSD Formation core likewise does not allow a metatheoretic fact to bypass its declared formation witness. However, the Formation core contains no agent-indexed accessibility relation or public-announcement operator. Therefore a PAL-style information update is **not derivable from Formation alone** and must not be silently identified with a change of DSD describability.

## 1. External-truth leakage test

The PAL two-world witness shows

`truth at the actual world != agent knowledge of that truth`.

The DSD finite witness independently shows

`external knowledge of the model != Descfg_L(p)`.

A candidate configuration with sound realization and valid configuration-admission predicates can remain non-describable when the required describable-expression conjunct is absent. Clause IV fixes `Descfg_L` exactly from `Psi_L`; external analyst knowledge is not an extra disjunct.

### Verdict

Pass. No hidden external-omniscience rule was found.

## 2. Information update versus formation update

In PAL, a truthful public announcement restricts the epistemic model to worlds satisfying the announcement. This can change what an agent knows without changing the atomic truth already holding at the actual world.

In DSD, changing `Desexpr_L`, `Admcfg_L`, coherence data, realization data, or other Clause-IV primitives can change `Descfg_L`. But the Formation core does not specify an update operator that says which primitive data must change when an observer receives information.

Thus

`PAL announcement update != DSD Closure Clause IV`.

Clause IV is a static definitional closure inside a regime, not an epistemic state transformer.

### Verdict

No contradiction, but a clear scope boundary.

## 3. Paired-regime result

Two regimes can share the same base, material items, candidate configuration, active material, anchors, and realization relation while differing in the primitive describability/admission data that enter `Psi`.

Then the same underlying structural record may be non-describable in one regime and describable in another.

This establishes consistency of regime-relative describability, but it does **not** establish that one regime is obtained from the other by learning or public announcement.

A bridge of the form

`epistemic state/update -> changes in DSD primitive regime data`

would be additional theory.

## 4. PAL-style deletion stress test

PAL updates are often implemented by restricting the set of epistemic alternatives.

The DSD Formation descriptor, by contrast, retains the full candidate-configuration class, including failed candidates. Moreover, arbitrary induced subsets need not be formation submodels: deleting the only witness of a retained configuration can change `Psi` and hence `Descfg`.

Therefore

`restriction of epistemic alternatives != arbitrary deletion of DSD candidate records`.

A future DSD information-update layer would have to preserve witness closure explicitly or classify the operation as a formation-level transition rather than assume semantic invariance.

## 5. Important non-correspondence

The following identifications are rejected:

- epistemic world = DSD candidate configuration;
- agent accessibility = DSD restriction/realization;
- knowledge = DSD describability;
- public announcement = Closure Clause IV;
- elimination of epistemic alternatives = arbitrary deletion from a DSD full descriptor.

The valid comparison is methodological:

- PAL forces a distinction between truth, information state, and update;
- DSD forces a distinction between primitive regime data, derived describability, and later formation stages;
- neither framework licenses inserting an external observer's information into the other's internal status without an explicit bridge.

## 6. Does Case 006 show that DSD is wrong?

### Primitive Axiom III
**No.** Sound realization remains weaker than configuration describability.

### Closure Clause IV
**No.** It does not import external truth or knowledge; it derives describability only from the declared witness formula.

### Full-descriptor policy / Remark 6.9
**No.** The warning that arbitrary induced subsets may fail to be submodels is exactly what prevents a naive identification with PAL model restriction.

### Observer-dependent interpretation
**Not established by Formation alone as epistemic logic.** The current core supports regime-relative structural describability, but it does not axiomatize agents, accessibility, knowledge, learning, or announcement updates.

This is a scope limitation, not an internal contradiction.

## 7. Revision status

**No corrective revision to the Formation paper is required from Case 006.**

Optional future clarification:

> A descriptive regime is not, without additional structure, an epistemic Kripke state or an agent knowledge model. Changes of observer information require an explicit bridge to changes in primitive regime data; they are not generated by the static configuration-closure clause itself.

If future DSD work intends to model learning or observation updates, the appropriate extension should be defined separately rather than folded into Closure Clause IV.

## 8. Case classification

- Domain: mathematical/philosophical logic
- External node: Public Announcement Logic / Dynamic Epistemic Logic
- DSD layer tested: Formation Stage III–IV, full candidate retention, submodel closure boundary
- Main distinction: factual truth vs epistemic information vs DSD structural describability
- Mapping strength: **methodological partial correspondence with important non-correspondence**
- Falsification status: **not falsified**
- Correction required to Formation paper: **no**
- Scope clarification opportunity: **yes — DSD regime is not automatically an epistemic state**
- Additional bridge needed for direct mapping: **yes**
- Cross-domain node status: **accepted as sixth provisional node**

## References

- Kwon Dominicus, *Formation Axiom System — Dimensional-Structural Describability*, 2026.
- Alexandru Baltag, Lawrence S. Moss, Slawomir Solecki, *The Logic of Public Announcements, Common Knowledge, and Private Suspicions*, TARK VII (1998); CWI report version 1999: https://ir.cwi.nl/pub/4497/
- Johan van Benthem, Jan van Eijck, Barteld Kooi, *Logics of Communication and Change*, ILLC PP-2005-09; Information and Computation 204(11), 1620–1662 (2006), DOI 10.1016/j.ic.2006.04.006.
