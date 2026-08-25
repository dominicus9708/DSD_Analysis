# Database / Information-Structure Field Synthesis

Status: **first-pass field closed**.

Scope: DB-001 through DB-005 / Global Cases 034-038.

## 1. Field-level conclusion

The database sequence gives **strong external structural convergence** with the DSD non-conflation discipline, but the five cases must not be counted as five fully independent confirmations.

The most defensible field-level conclusion is that relational information systems repeatedly require explicit separation among:

- support/record existence;
- target/reference existence;
- applicability;
- assignment/value presence;
- defined zero;
- reduced aggregate output;
- provenance or formation history.

No contradiction with the Formation Axiom System, the axis-property system, or Channel-Indexed Static Aggregation was found.

## 2. Case map

| Case | Main result | Independence note |
| --- | --- | --- |
| DB-001 | row absence / NULL / empty / zero are not automatically identical | baseline status-separation node |
| DB-002 | JOIN and filter order creates, preserves, or removes rows; projection can erase provenance | comparatively independent transformation/provenance node |
| DB-003 | property-kind existence / per-entity applicability / assignment / defined zero need separate coordinates when reconstruction matters | shares the non-conflation family with DB-001; strengthens it at schema/application level |
| DB-004 | relation-row support / nullable target / valid target / auxiliary-value status / referential action are separable | shares status logic with DB-001/003 but adds relation-support and transformation semantics |
| DB-005 | reduced aggregates cannot generally reconstruct support; zero may arise from absence, explicit zero, or cancellation | strongest independent algebraic/reconstruction node |

## 3. Independent convergence nodes

The first-pass database campaign should be counted conservatively as **three main structural convergence families**, not five unrelated proofs.

### Node A — status and support non-conflation

DB-001, DB-003, and part of DB-004 repeatedly show that a single value coordinate is not enough to identify record existence, applicability, reference support, assignment, or defined zero.

These cases are mutually reinforcing but not fully independent because they reuse related nullable/optional relational mechanisms.

### Node B — stage/order/provenance sensitivity

DB-002 and the referential-action portion of DB-004 show that downstream structure depends on the stage and rule by which rows are formed, filtered, null-extended, preserved, or deleted.

This supports the DSD practice of distinguishing formation conditions/history from a final reduced visible value, without identifying SQL query semantics with DSD formation semantics.

### Node C — aggregation and reconstruction obstruction

DB-005 gives the strongest independent result.

It exhibits both:

1. status-totalization loss: absence/missingness/defined zero can collapse under zero substitution;
2. summation-kernel loss: distinct nonzero components can cancel to the same aggregate.

This directly parallels the DSD static distinction between support-tagged structure and reduced aggregate value.

## 4. What remains encoding-dependent

The following are not universal DBMS laws:

- every application must distinguish every status layer;
- every nullable field represents unknown or inapplicable data in the same way;
- a relation must be represented by a separate relation table;
- provenance must always be retained;
- aggregation must be injective.

Schema designers may deliberately remove states with NOT NULL, subtype tables, constraints, cascades, defaults, or application conventions. A reduced aggregate can be completely correct when only that reduced result matters.

Therefore the DSD-supporting claim is conditional:

> when later reasoning requires reconstruction, provenance, applicability, relation support, assignment status, multiplicity, or cancellation history, collapsing these coordinates is information-losing unless an additional reconstruction theorem or encoding coordinate is retained.

## 5. Non-identity boundaries

Do not identify:

- SQL NULL with DSD undefined;
- a database row with a DSD channel;
- a foreign key with an operational channel or axis-property primitive;
- SQL JOIN formation with Formation Clause VI;
- SQL SUM with the full DSD composition semantics.

Only structural roles are compared.

## 6. Closed first-pass verdict

**Database / information structure: first-pass analysis closed.**

The field does not provide a new contradiction or force a revision of the current DSD papers. Instead it gives a useful external node showing that DSD's distinction among absence, applicability, assignment, zero, support, provenance, and reduced value is compatible with practical relational modeling and aggregation behavior.

The strongest transferable principle is:

`equal reduced output != equal support/status/provenance structure`.

## 7. Handoff to the next field

Next field: **Knowledge Representation / Ontology / Classification**.

The first case should avoid merely repeating SQL NULL behavior. It should test a logical knowledge-representation rule in which non-assertion and falsity are semantically distinct.

Prepared first case:

**K_R-001 / Global Case 039 — Open-World Non-Assertion versus Falsity**.

Primary target: OWL/RDF-style open-world reasoning, with explicit non-identity against DSD undefined/false semantics.