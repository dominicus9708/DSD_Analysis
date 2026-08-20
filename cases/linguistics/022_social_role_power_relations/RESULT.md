# LING-009 / Global Case 022 — Result

## Question
Can social role, power/authority, direction of command, compliance, legitimacy, and conflict resolution be collapsed into one relation or inferred from one another without additional rules?

## External result
No.

Social-institution literature treats institutions as structures of differentiated, often hierarchical roles with distinct degrees of authority and power relations. Authority theory further distinguishes de facto authority/obedience from normative authority.

Thus the source field independently supports at least the following separations:

`role != ordered authority relation != normative legitimacy != observed compliance/effect`.

## Directionality
Authority is naturally relation-sensitive and can be asymmetric:

`Authority(s,h,a,C) != Authority(h,s,a,C)`.

Therefore an encoding that erases ordered input identity is not source-faithful.

This is a strong match to the DSD axis-property rule that binary relation records take ordered tagged inputs and that symmetry is never inferred merely from profile length. The downstream static layer likewise retains input order unless symmetry/antisymmetry is separately established.

## Scope dependence
The same role label may support different authority relations by action, target, institution, time, or delegation state.

Therefore:

`Role(s)=R` does not imply one global `Authority(s,*)` value.

For a full DSD application, authority is better represented as a typed relation/profile than as an intrinsic scalar attached to one actor.

## De facto versus normative authority
Observed compliance does not reconstruct legitimacy:

`Compliance(h,s,a,C)=1`

is compatible with

`NormativeAuthority(s,h,a,C)=0`.

Fear, error, habit, or coercive capacity can generate obedience without establishing the normative right/power whose existence is separately debated in authority theory.

This produces a new predefinition restraint:

> Downstream obedience or successful enforcement cannot be used to back-fill a normative authority relation unless the source theory supplies the required legitimacy bridge.

## Conflicting authority
Two authority relations can both be valid in their own scope while producing incompatible directives. The pair of relations alone does not determine a unique obligation or action.

An additional bridge is required, such as:

- jurisdiction priority;
- hierarchy/office priority;
- recency rule;
- exception rule;
- conflict-resolution procedure.

Thus:

`multiple authority relations != resolved obligation`.

## Formation correspondence
Formation remains useful for preserving role-tagged event/channel identity. It does not derive who has authority over whom, in what direction, or over which action.

## Axis-Property correspondence
This case gives the strongest linguistic motivation so far for Axis-Property binary/higher-order records.

Useful features:
- ordered tagged inputs;
- binary relations;
- higher-order/mixed profiles for actor-target-action-context dependence;
- partial application domains;
- no automatic symmetry;
- preservation of relation identity downstream.

However, naming a property `authority`, `supervision`, or `power` supplies no social meaning by itself. The application still supplies the external institutional/normative bridge.

## Relation to LING-008
LING-008 separated role, delegation, jurisdiction, procedure, and institutional effect.

LING-009 adds a distinct relation-structural result:

- authority direction matters;
- obedience/effective power differs from normative legitimacy;
- multiple valid relations need not resolve themselves.

The new node is therefore a **directional and conflict-sensitive relation boundary**, not merely another institutional-success condition.

## Verdict
- Formation contradiction: **not found**.
- Structural reinterpretation: **established**.
- Predefinition restraint: **independently corroborated at relation-direction and legitimacy levels**.
- Formation: **core for role-tagged identity**.
- Axis-Property: **strongly useful/recommended for explicit relation-sensitive modeling, but not a source of social semantics**.
- Ordered relation preservation: **directly important**.
- DSD theory of social power/authority: **not claimed**.
- New DSD-analysis audit item: **confirmed — preserve direction, scope, legitimacy status, and conflict-resolution rules separately.**
