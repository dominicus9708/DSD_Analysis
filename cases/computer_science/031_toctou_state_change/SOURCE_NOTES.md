# CS-003 Source Notes

## 1. MITRE CWE-367

Source: https://cwe.mitre.org/data/definitions/367.html

CWE-367 defines the weakness as checking resource state before use while allowing that state to change between the check and the use so that the earlier result is no longer valid.

Structural point used by this case:

`checked property at t_check != guaranteed property at t_use`.

The weakness is temporal and concurrency-sensitive. It is not merely a malformed-input or static-type problem.

## 2. SEI CERT POS35-C

Source: https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152082

The noncompliant example calls `lstat()` on a pathname and later calls `open()` on that pathname. The pathname can be manipulated asynchronously in the interval, so the object checked need not be the object actually opened.

The compliant patterns are structurally important:

- collapse separate check/use by using `open(..., O_NOFOLLOW)` when appropriate; or
- after opening, use `fstat()` on the returned file descriptor and compare identity attributes such as inode/device with the earlier observation.

This shows that safety may require atomicity or an explicit identity relation between the checked state and the used object, not merely a more detailed first check.

## 3. RFC 9110 HTTP conditional requests

Source: https://www.rfc-editor.org/info/rfc9110/

`If-Match` is used with state-changing methods to prevent accidental overwrites when multiple agents act on the same resource. The origin server evaluates the precondition before performing the method; if the current entity tag is not among the supplied validators, the state-changing request does not proceed normally.

`If-Unmodified-Since` provides a time-based precondition when entity tags are unavailable.

Structural point:

An earlier representation obtained by a client is not presumed current at mutation time. The mutation carries a validator that is checked against the current server state.

Thus:

`previously observed version != current mutation-admissible version`.

## 4. PostgreSQL concurrency control

Source: https://www.postgresql.org/docs/current/mvcc.html
Source: https://www.postgresql.org/docs/18/sql-set-transaction.html

PostgreSQL documents transaction isolation as control over what a transaction can see while other transactions run concurrently. Under Serializable isolation, if concurrent reads/writes would produce a result inconsistent with every possible serial execution, one transaction is rolled back with a serialization failure and must be retried.

The current documentation also states that transactions must be prepared to retry after serialization failures.

Structural point:

A transaction can have a coherent earlier view and still be prevented from committing because concurrent state evolution makes the attempted later effect incompatible with the declared consistency regime.

Therefore:

`valid earlier snapshot != guaranteed admissible later commit`.

## Source-family independence

- CWE supplies the abstract weakness pattern.
- CERT supplies filesystem object-identity and atomicity counterpressure.
- HTTP supplies explicit version/precondition coupling at the use boundary.
- PostgreSQL supplies transactional concurrency, invalidation, rollback, and retry.

The latter three are not counted as three proofs of one theorem; they are distinct operational realizations of a common temporal non-transfer problem.