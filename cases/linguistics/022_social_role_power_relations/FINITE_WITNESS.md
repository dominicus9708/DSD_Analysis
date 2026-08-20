# LING-009 / Global Case 022 — Finite Witnesses

## Witness A — Directional authority
Let the actors be `s` (supervisor) and `h` (subordinate), with one action type `r = submit_report` in context `C`.

Define the external institutional relation

`Authority(s,h,r,C)=1`

and

`Authority(h,s,r,C)=0`.

Both can utter the same directive string `Submit the report.`

Thus the pair of participants alone does not determine the relation. Ordered participation matters:

`Authority(s,h,r,C) != Authority(h,s,r,C)`.

A DSD encoding that replaced the ordered pair `(s,h)` with the unordered set `{s,h}` would lose a source-theory distinction.

## Witness B — Compliance without normative authority
Let actor `x` lack normative authority over `h` for action `r`, but suppose `h` nevertheless complies because of fear, mistake, habit, or anticipated sanction.

Then

`Compliance(h,x,r,C)=1`

while

`NormativeAuthority(x,h,r,C)=0`

is coherent.

Therefore:

`compliance != normative authority`.

Observed effect does not reconstruct the legitimacy relation that would justify it.

## Witness C — Same role, different scope
Let `s1` and `s2` both have role `manager`.

- `Authority(s1,h,purchase_A,C)=1`
- `Authority(s2,h,purchase_A,C)=0`
- `Authority(s2,h,personnel_B,C)=1`

Hence role identity does not determine a single global authority value.

## Witness D — Conflict requires an extra rule
Suppose

`Authority(s1,h,a,C)=1`

and

`Authority(s2,h,a,C)=1`,

but `s1` directs `Do(a)` and `s2` directs `Do(not-a)`.

The existence of both authority relations does not select the action.

A further rule such as priority, recency, jurisdiction, exception, or conflict-resolution procedure is required.

Therefore:

`multiple valid authority relations -> unique obligation`

is not valid without an additional bridge.
