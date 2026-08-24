# Finite Witness Templates

Status: prepared; witness values are not yet adjudicated.

## Witness A — overlap obstruction template

Choose distinct admitted channels `c1, c2` and finite families

- `F = {c1}`,
- `G = {c1, c2}`.

Assign symbolic terms

- `T(c1) = x`,
- `T(c2) = y`.

Compare

- `Comp(F union G)`,
- `Comp(F) + Comp(G)`.

The calculation must identify exactly which assumptions on `x`, `y`, or the codomain make equality hold or fail.

## Witness B — disjoint-family template

Choose

- `F = {c1}`,
- `G = {c2}`,
- `c1 != c2`.

Compare the same preservation equation under `F intersect G = emptyset`.

## Witness C — non-injective aggregation template

Choose distinct finite families `F1 != F2` and term assignments with

`Comp(F1) = Comp(F2)`.

Use the Formation paper's existing finite non-injective-composition construction as the primary DSD witness before introducing any new example.

## Witness D — multiplicity-encoding boundary

Construct a source with explicit multiplicity and compare it with the Stage-VII finite-set convention. Record the exact point at which the source object ceases to be identical to `P_fin(C_L)`.

## Minimality rule

Prefer the smallest finite carrier and smallest number of channels sufficient to exhibit each preservation or failure claim.
