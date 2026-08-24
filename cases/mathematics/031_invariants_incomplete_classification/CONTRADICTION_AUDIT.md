# Contradiction Audit

## Audit questions

### 1. Does DSD claim every scalar summary is an invariant?

No. Definition 12.3 calls the map a displayed finite-coordinate scalar summary/compression and allows arbitrary indicator maps.

### 2. Does DSD claim every scalar-valued or finite summary is necessarily incomplete?

No. The paper explicitly limits the construction to the displayed summary and says it is not an arbitrary set-theoretic scalar coding of the full descriptor. Proposition 12.4 is conditional on a collision hypothesis.

### 3. Does DSD claim rank is never a complete invariant under any signature?

No. Proposition 12.1 concerns strict equivalence of the full axis-property structure. MATH-003 already established that rank/dimension can be complete for the bare vector-space layer.

### 4. Is Proposition 12.4 compatible with standard invariant theory?

Yes. It has exactly the form of a collision witness: equal reduced coordinates but inequivalent full objects. If the selected indicators are invariants, the result witnesses an incomplete invariant. Without that added hypothesis it remains a valid incomplete-classifier/readout result.

### 5. Do downstream papers preserve the same distinction?

Yes.

- Static Aggregation requires injectivity/reconstruction conditions before aggregate equality is used for reconstruction.
- Dynamics states directly that a reduced readout need not be a complete classifier and supplies collision witnesses.

## Overstatement blocked by this audit

The following statement must not be attributed to DSD:

`Any scalar or finite-dimensional descriptor must lose structural information.`

The mathematically correct statement is:

`A chosen reduced descriptor loses classification information exactly when it fails to separate the relevant equivalence classes; the DSD papers provide explicit collision conditions for several particular reductions.`

## Audit result

No contradiction with standard classification theory or with the current Formation, Axis Property, Static Aggregation, or Dynamics papers was found.

One terminology condition is worth preserving in future writing: call a reduced map an `invariant` only after invariance under the declared equivalence has been established.