# Contradiction Audit — CS-002 / Global Case 030

## 1. External result

The external sources reject the following totalizations:

- `authentication = authorization`;
- `identity = effective permission`;
- `token possession = sufficient authorization for every resource`;
- `authorization allow = admission = successful effect`;
- `access denial = authentication failure`;
- `same principal = same permission for every request`.

A source-sensitive surviving separation is:

`authentication status != authorization relation/decision != bounded privilege or credential != downstream admission != execution/effect`.

## 2. Formation Axiom System

The Formation Axiom System is a static typed staged framework and explicitly requires domain-specific interpretation maps for applications. It separates multiple admissibility/formation operations and retains unsuccessful candidates rather than reducing all failure to one value.

CS-002 is compatible with that discipline: an access request can satisfy one upstream condition and fail a later independent condition.

However, the security pipeline is **not** identified with Formation Stages I–VII. Authentication, authorization, OAuth scope, and Kubernetes admission are native security concepts with their own semantics.

Rejected mappings:

- `authentication success = Stage-IV describability` by identity;
- `authorization deny = DSD undefined assignment`;
- `invalid_token = DSD channel absence`;
- `insufficient_scope = DSD defined zero`;
- `admission rejection = failed formation stage` without a supplied interpretation map.

No direct contradiction with the Formation axioms was found.

## 3. Axis-Property System

The Axis-Property System concerns properties of realized axes over a Stage-VI formation background. Security principals, roles, groups, tokens, scopes, or permissions are not realized DSD axes merely because they have hierarchy or relations.

Therefore CS-002 has **no default direct Axis-Property mapping**.

If a future DSD application independently realizes some relevant structure as axes and supplies typed property profiles, a partial application could be studied then. That extra realization is not supplied here.

This nonmapping is itself an audit result and prevents overextension.

## 4. Static Aggregation

Static Aggregation is not required for the core result. CS-002 does not depend on a numerical aggregate or reduced descriptor.

The finite witness does show that identical final non-effect can arise from different upstream denial points, but that observation is left at the source-domain level rather than forcing an aggregation analogy.

## 5. Structural Reorganization Dynamics

The core case is atemporal. Permission changes over time, revocation, stale checks, and TOCTOU are deliberately reserved for a later case.

Consequently the dynamics paper is not needed to establish CS-002. If those temporal changes are later modeled, its distinction between regular value evolution and status/domain transitions may become relevant, but no runtime authorization change is reclassified here as DSD reorganization by default.

## 6. Direct contradiction verdict

**No direct contradiction with the current DSD axioms was found.**

The principal effect is to constrain application:

1. preserve source-native authentication, authorization, credential, scope, admission, and effect states;
2. do not infer later states from earlier states without the missing policy/context data;
3. do not map security denial codes to DSD undefined/zero/absence labels by superficial similarity;
4. do not interpret security roles or permission hierarchies as realized axes without an independent axis realization.

## 7. Independence from CS-001

CS-001 established computational distinctions among typing, runtime construction/state, applicability, evaluation, and result.

CS-002 adds an independent relational-policy interface:

- authorization depends on subject/object/operation/environment/policy, not merely type or runtime state;
- delegated credentials can be valid yet insufficiently scoped;
- a concrete API pipeline can authorize and later reject at admission;
- the same authenticated principal can receive different request-specific decisions.

Thus CS-002 is not a restatement of `type-correct != operation-applicable` or `undefined != zero`.
