# CS-003 / Global Case 031 — Result

Status: first-pass cross-subfield analysis complete.

## Answer-first result

The source systems reject transfer of a successful check across time unless the relevant state is preserved, revalidated, or coupled to use by a source-native mechanism.

Surviving audit separation:

`check-time condition != cross-time preservation relation != use-time condition != operation admission != committed/effective result`.

This is not a universal five-stage architecture. It is a prohibition against silently treating past validity as current validity.

## External witness summary

### CWE-367

TOCTOU is defined by checking resource state and later using the resource after that state can change. The check can have been correct when performed and still be invalid as a basis for later use.

### SEI CERT POS35-C

The `lstat(path)` / `open(path)` example shows that the stable pathname string does not guarantee stable resource identity. Mitigations either combine the relevant check with use (`O_NOFOLLOW`) or bind later verification to the actually opened object (`fstat` plus identity comparison).

### RFC 9110

`If-Match` and related conditional requests prevent stale clients from applying state-changing methods to a resource whose current representation no longer matches the client's validator. An earlier valid representation is therefore not treated as automatically authoritative at mutation time.

### PostgreSQL

Serializable concurrency control can abort a transaction whose later effect would not fit any serial execution after concurrent state changes. The transaction must retry from a new valid state.

## Finite witnesses

1. Filesystem: `p -> A` at check time, `p -> B` at use time. Earlier check true; later operation targets a different effective object.
2. HTTP: client read ETag `E1`; resource changes to `E2`; `If-Match: E1` causes the stale mutation to fail.
3. Database: T1 reads; T2 commits conflicting change; T1's later commit is rejected with serialization failure and retried.

## Strong hypotheses

All seven initial totalizing hypotheses were rejected as general rules.

Most important rejected implication:

`Valid(t_check) => Valid(t_use)`.

## DSD result

### Formation

Compatible but insufficient by itself. Formation gives static typed/status/identity discipline, not temporal persistence or race prevention.

### Axis Property

No primary mapping. The theory is explicitly non-dynamical, so importing TOCTOU into it would exceed its declared scope.

### Structural Reorganization Dynamics

Strongest correspondence. The dynamics framework already treats states as time-indexed slices, separates ordinary value evolution from status/domain and stronger formation-level transitions, and requires explicit lineage for identity-sensitive changes instead of silently mutating one unchanged object.

CS-003 therefore does not falsify the current dynamics framework. It sharpens the application rule:

**A valid earlier DSD-interpreted slice cannot be transferred to a later use solely by temporal succession or label continuity. An application-specific cross-time preservation/revalidation relation is required.**

### Static Aggregation

Only secondary: equal reduced failure/no-effect outputs do not reconstruct the intervening temporal failure point or history.

## New DSD application boundaries

Reject:

- `same external name across time = same DSD object`;
- `earlier valid state = later valid state`;
- `all concurrent change = smooth value change of one fixed object`;
- `TOCTOU solved by Formation staging alone`;
- `filesystem handle/version token/transaction snapshot = DSD lineage by identity`.

## Independence judgment

CS-003 is independent of CS-001 and CS-002. It adds a temporal state-transfer problem that can occur despite correct typing, correct initial validation, successful authentication, and correct authorization at the earlier time.

## Final classification

`compatible + application-boundary strengthening + independent temporal computational node`.

No direct contradiction with the current DSD axioms or Structural Reorganization Dynamics was found.