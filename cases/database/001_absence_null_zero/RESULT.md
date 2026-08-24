# DB-001 Result — Row Absence, NULL, Empty Value, and Defined Zero

Status: **first-pass analysis completed**.

Final judgment: **strong partial structural support** for DSD's non-conflation rule, with an important non-identity boundary: SQL NULL is not the same formal object as DSD undefined assignment.

## 1. State separation

Consider four states relative to a candidate key and field:

1. no row exists for the key;
2. a row exists and the field is NULL;
3. a row exists and the field has a defined numeric zero;
4. a row exists and the field has a defined empty character value, when the DBMS preserves that value separately.

These states are not universally interchangeable. Row absence is relation membership failure. NULL is a marker inside a present row. Zero is an ordinary defined numeric value. Empty string is implementation-sensitive: it is a defined zero-length string in many systems, while Oracle currently treats it as NULL.

## 2. DSD correspondence

| Database state | DSD comparison | Judgment |
| --- | --- | --- |
| no row / tuple absent | absent candidate record or absent formed channel, depending on modeling layer | partial structural correspondence |
| present row + NULL field | undefined / unavailable value only after an explicit encoding choice | non-identical but structurally analogous |
| present row + numeric 0 | defined zero | close structural correspondence |
| present row + empty string | defined value in systems that preserve it; collapsed to NULL in Oracle | implementation-dependent boundary |

The main reason SQL NULL cannot simply be renamed DSD undefined is that DSD partial assignment is represented by domain membership and a function graph. If the input lies outside the assignment domain, there is no value pair. SQL NULL instead remains a storable marker in a tuple that already exists.

## 3. Aggregation witness

For two rows

- `(id=1, x=0)`
- `(id=2, x=NULL)`

standard SQL-style aggregation distinguishes support from non-null value count:

- `COUNT(*) = 2`
- `COUNT(x) = 1`
- `SUM(x) = 0`

If `x` is first transformed with `COALESCE(x,0)`, then `COUNT(COALESCE(x,0)) = 2`. The numeric sum can remain 0 while the information that one row carried NULL is erased.

This is directly relevant to the DSD warning that equal reduced outputs need not identify the same support/status structure.

## 4. Empty relation versus defined zero

A query selecting no rows has different support from a query selecting one row whose value is zero. PostgreSQL documents that, except for `count`, aggregate functions such as `sum` return NULL when no rows are selected; one actual zero row instead sums to zero.

Thus

- empty relation under `SUM` -> NULL;
- one defined-zero row under `SUM` -> 0.

Applying an external default such as `COALESCE(SUM(x),0)` deliberately collapses those two output states. That may be useful application logic, but it is information-losing and should not be mistaken for structural identity.

## 5. Cross-engine boundary

Oracle provides a useful counterpressure. It explicitly distinguishes NULL from numeric zero, but currently treats a zero-length character value as NULL. Therefore the four-way distinction cannot be assumed to be natively representable by one bare SQL column in every DBMS.

This does not contradict DSD. It shows that a concrete implementation may require an explicit presence/status field, a separate relation, or another encoding if the application needs to preserve distinctions that the DBMS itself collapses.

## 6. Falsification attempt

The most direct attempted counterexample was: if SQL safely replaces every missing state by a conventional default, perhaps DSD's undefined/zero distinction is unnecessary. The aggregation tests fail to support that collapse. `COUNT(*)`, `COUNT(expr)`, empty-input `SUM`, NULL predicates, and vendor-specific empty-string behavior all expose information that is lost under indiscriminate default substitution.

No contradiction to the DSD distinction was found.

## 7. Final judgment

**Strong partial structural support.** Database systems independently require distinctions among tuple existence, missing/unknown field state, and defined values. DSD's separation of undefined assignment, defined zero, channel absence, and zero contribution is therefore not an alien bookkeeping device when viewed from information-structure practice.

However, the mapping is not one-to-one:

- SQL NULL is a value marker inside a tuple, not literally the absence of a partial-function graph pair;
- row absence and field NULL occupy different relational layers;
- empty string semantics depend on the DBMS;
- aggregation functions may intentionally discard or collapse status information.

Accordingly, DB-001 supports the DSD non-conflation principle while also clarifying that faithful database encoding sometimes requires more than one SQL column or explicit status/provenance data.