# Case 004 — Finite Witnesses

## Witness 1 — Exact expression-status space under Primitive Axiom I

Fix any full Formation model with one independent active kernel that already supplies a describable configuration and admitted channel. Add one inert candidate expression `x` whose material is disjoint from the active kernel, and do not use `x` in any realization unless stated.

For `x`, define Boolean coordinates

- `A(x) = 1` iff `Admexpr_L(x)`;
- `D(x) = 1` iff `Desexpr_L(x)`.

Primitive Axiom I is exactly

`D(x) <= A(x)`.

Therefore the only admissible status pairs are

- `(A,D)=(0,0)`;
- `(A,D)=(1,0)`;
- `(A,D)=(1,1)`.

The state `(0,1)` is forbidden.

### Realizability of the three allowed states

#### State S00 — candidate only
Declare

- `Admexpr_L(x)=false`;
- `Desexpr_L(x)=false`;
- no restriction or realization involving `x`.

All Formation axioms remain satisfied. Thus membership in the candidate-expression class does not imply admission.

#### State S10 — admitted but not describable
Declare

- `Admexpr_L(x)=true`;
- `Desexpr_L(x)=false`;
- the required identity restriction `Res_L(x,x)` with sound inherited data;
- no realization involving `x`.

All Formation axioms remain satisfied. Thus admission does not imply describability.

#### State S11 — admitted and describable
Declare

- `Admexpr_L(x)=true`;
- `Desexpr_L(x)=true`;
- the required sound identity restriction.

Primitive Axiom I is satisfied. No configuration realization is forced merely by `Desexpr_L(x)`.

### Forbidden state S01

If

- `Admexpr_L(x)=false`;
- `Desexpr_L(x)=true`,

then Primitive Axiom I fails.

Hence the theory does not collapse the statuses. It imposes one directional prerequisite and leaves the two converses open.

## Witness 2 — Sound realization without configuration describability

Let `h` be an admitted and describable expression with one material item `a` anchored at support `s`.

Let `p` be a candidate configuration with

- `act_L(p)={a}`;
- the same anchor `anch_p(a)=s`;
- `Realize_L(h,p)=true`.

Primitive Axiom III is satisfied because active material and anchoring are inherited soundly.

Now set one configuration-admission condition false, for example

`Admcfg_L(p)=false`.

Then `ConfAdm_L(p)=false`, so the witness formula `Psi_L(p)` is false and Closure Clause IV gives

`Descfg_L(p)=false`.

Thus

`Realize_L(h,p) does not imply Descfg_L(p)`.

This witness is a valid Formation structure; no axiom is violated.

## Witness 3 — Predefinition/promotion rules strictly strengthen the theory

Consider three hypothetical extra rules.

### Rule R1
`x in E^L_B => Admexpr_L(x)`.

R1 eliminates Witness S00. Therefore R1 is not derivable from the current Formation axioms.

### Rule R2
`Admexpr_L(x) => Desexpr_L(x)`.

R2 eliminates Witness S10. Therefore R2 is not derivable from the current Formation axioms.

### Rule R3
`Realize_L(h,p) => Descfg_L(p)`.

R3 eliminates Witness 2. Therefore R3 is not derivable from the current Formation axioms.

These are not harmless notational abbreviations. Each would define a strictly smaller model class.

## Mathematical interpretation

The current Formation system validates a controlled one-way implication

`describable expression => admitted expression`

but rejects automatic promotion in the reverse direction and rejects automatic promotion from candidate or realization status to later formation success.

This gives a precise formal version of the Case-004 target:

**earlier representational availability does not by itself justify later formation status.**