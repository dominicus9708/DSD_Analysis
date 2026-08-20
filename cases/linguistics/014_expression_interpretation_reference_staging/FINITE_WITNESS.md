# Finite Witness — LING-001 / Global Case 014

This is a finite comparison witness, not a model of natural language as a whole.

## Fragment
Semantic base types:

- `e`: individuals
- `t`: truth values

Lexical expressions:

- `mira : e`
- `sleeps : e -> t`
- `quickly : (e -> t) -> (e -> t)`
- `n0 : e` syntactically typed as an individual-denoting name but left non-denoting in the chosen partial-reference interpretation.

## Four states

### A. Successful composition and reference
Expression: `sleeps(mira)`

- syntactically formed: yes
- type-compatible: yes
- denotation of `mira`: defined
- semantic application: defined
- sentence truth value: defined

### B. Type failure
Attempted semantic application: `mira(sleeps)`

- lexical material exists: yes
- required functional type: no
- well-typed semantic application: no
- semantic output under ordinary typed functional application: not formed

This does not mean the expression has truth value `FALSE`; it means the selected typed composition rule does not apply.

### C. Non-denoting singular term
Expression schema: `sleeps(n0)`

- syntactic expression: available
- type label for `n0`: `e`
- reference of `n0`: undefined in the chosen partial-reference interpretation
- resulting sentence treatment: theory-dependent

A negative, positive, neutral, supervaluational, or other free-logical semantics can treat the containing formula differently. Therefore LING-001 does not identify reference failure with one universal DSD status or truth value.

### D. Defined false
Let `mira` denote an individual who does not sleep in model `M`.

- reference: defined
- predicate application: defined
- truth value: `FALSE`

This differs from C: defined falsity is not the same as reference failure.

## Structural separation witnessed

`expression present`

is not identical to

`well-typed semantic application`

which is not identical to

`reference defined`

which is not identical to

`truth value = FALSE`.

## DSD comparison
The witness supports only a structural analogy:

- candidate/present material versus admitted/usable stage;
- typed application domain versus out-of-domain status;
- partial assignment versus defined values;
- missing status versus a defined negative/zero-like value.

It does **not** establish a canonical one-to-one identification between linguistic statuses and Formation predicates.
