# LAW-003 / Global Case 014 — Agency, Delegation, and Representation

Status: prepared, analysis not yet executed.

## 1. Purpose

Test whether legal and institutional structures of acting for another person or entity remain jointly describable with DSD distinctions without collapsing:

- underlying natural or legal person
- institutional/legal role
- source of authority
- scope of authority
- actual act
- attribution of the act or its legal effect

The case does not assume in advance that agency, mandate/delegation, and representation are one legal concept. Source-law distinctions must be preserved first.

## 2. Primary question

When the same human actor appears under different representative or delegated capacities, does the source legal structure require role-sensitive distinctions compatible with DSD's preservation of typed role/tag information, or does a genuine contradiction arise after the comparison types are aligned?

## 3. Source-first decomposition

Before any DSD mapping, the analysis must identify from primary or authoritative sources:

1. who or what holds the underlying legal position;
2. who performs the act;
3. what legal relation or rule supplies authority;
4. the scope and limits of that authority;
5. what conditions make the act attributable to another person or institution;
6. how excess, absence, termination, defect, or later ratification of authority is treated;
7. which of `agency`, `representation`, `mandate`, `delegation`, or related terms are legally distinct in the selected legal system.

No DSD term is inserted into this source description.

## 4. DSD comparison targets

### Formation Axiom System

First test whether the source distinctions can be compared with:

- typed candidate and admitted structures;
- realization conditions;
- partial assignment rather than automatic totalization;
- operational channel identity including role `rho`;
- channel absence versus a defined zero contribution;
- strict comparison requiring preservation of the relevant formation structure.

### Axis-Property extension

Use only if the legal source requires additional properties or relations attached to an already formed role-tagged actor/channel, for example:

- authority-scope property sensitive to the representative tag;
- relation between principal and representative;
- higher-order or mixed relation among actor, represented party, act, and institutional context.

The case must explicitly test whether Formation role identity is already sufficient before invoking Axis-Property machinery.

## 5. Minimal formal skeleton

Let `u` denote an underlying actor and let `r` range over legally distinguished capacities. A source-side action token is provisionally represented only as a typed tuple

`a = (u, r, authority_source, scope, act, context)`.

The comparison must test, rather than assume, whether two tuples sharing `u` but differing in `r` or authority data may have different legal admissibility or attribution status.

A useful non-collapse condition is:

`same underlying actor != same legally operative role-tagged act`.

This is a test statement, not a source-law conclusion.

## 6. Required stress cases

At least one ordinary authorized case and at least two boundary cases must be analyzed. Candidate boundary classes include:

- no authority / unauthorized representation;
- authority exceeded;
- authority terminated before the act;
- later ratification or confirmation;
- conflict between personal capacity and representative capacity;
- one actor holding multiple capacities for the same institution.

The final selection depends on what the authoritative source law actually distinguishes.

## 7. Falsifiable / decidable criteria

### Coherence-supporting result

The case supports an external coherence node only if:

1. source-law distinctions are independently established;
2. a typed mapping can preserve all legally relevant status distinctions without inventing a DSD theorem;
3. apparent conflicts disappear only through legitimate type/role/regime separation;
4. no source-required identity forces DSD to distinguish objects that the source requires to be literally identical in the same comparison role, and no DSD-required identity forces the source to separate what it requires to be identical;
5. any extra encoding is stated explicitly.

### Direct contradiction candidate

Record a direct contradiction candidate if, after matching the same objects, roles, stages, and legal regime, the source structure requires a relation or identification that cannot coexist with the relevant DSD axiom/definition, or DSD requires a distinction that makes the source rule impossible to represent without changing its meaning.

### No meaningful mapping

If the source doctrine operates at a normative or semantic level not represented by Formation or Axis-Property structure, record `no meaningful mapping` rather than forcing an analogy.

## 8. Output files for execution

When analysis begins, complete:

- `SOURCE_NOTES.md` — primary/authoritative legal sources and exact source claims
- `MODEL.md` — source-side typed model and DSD comparison map
- `FINITE_WITNESS.md` — minimal authorized and boundary constructions if useful
- `RESULT.md` — derivation, correspondence class, contradiction audit, boundaries
- `REPRODUCIBILITY.md` — URLs/versions/dates and any deterministic checks

## 9. Result discipline

Do not write `DSD proves representation law` or an equivalent claim.

The strongest permitted conclusion from this case is that an independently established representative/authority structure is structurally compatible with specified DSD distinctions under an explicit mapping, or that a genuine contradiction/non-mapping was found.
