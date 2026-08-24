# CS-003 Structural Model

## 1. Minimal temporal separation

Let a resource-bearing system have states `S(t)` and let a predicate `P(r,S(t))` state the condition required before an operation on resource designator `r` is allowed.

A separated check/use design has:

`Check(r,t_c) = P(r,S(t_c))`

followed later by

`Use(r,t_u)` with `t_c < t_u`.

The strong but invalid transfer rule is:

`P(r,S(t_c)) => P(r,S(t_u))`.

Without an invariant, lock, atomic primitive, version match, identity-preserving handle, or equivalent relation, the implication is unsupported.

## 2. State and identity should not be collapsed

The following coordinates may differ:

- resource designator/name;
- resource identity actually referenced;
- relevant property/value;
- version or modification token;
- permission/policy state;
- transaction/snapshot state;
- use-time effect.

A stable name is not by itself a stable resource identity, and a stable identity is not by itself a stable property value.

## 3. Safe-use relation

Rather than assuming temporal persistence, introduce an explicit relation

`R_safe(check_state, use_state)`

whose source-native realization may be one of:

- one atomic operation that combines check and use;
- a lock excluding relevant intervening change;
- an identity-preserving opened handle plus post-open verification;
- a version/entity-tag precondition evaluated at mutation time;
- transaction isolation plus conflict detection and retry;
- another source-specific mechanism that proves the required property remains applicable.

The case does not assert that these mechanisms are equivalent.

## 4. Finite filesystem witness

Times: `t0 < t1 < t2`.

- `t0`: pathname `p` denotes ordinary file `A`; check says `A` is acceptable.
- `t1`: another actor changes pathname resolution so `p` denotes object `B` (e.g. a disallowed symlink target).
- `t2`: the program calls `open(p)` and acts on `B`.

The check was true at `t0`; it is not thereby false retroactively. The failure is transfer of a past result to a later changed state.

## 5. Finite HTTP version witness

- Client reads resource version `E1`.
- Another client changes it to `E2`.
- First client sends an update based on `E1`.
- With `If-Match: E1`, the server evaluates current state and rejects the mutation when the validator no longer matches.

The earlier read was valid, but it is stale for the later mutation.

## 6. Finite transactional witness

- Transaction T1 reads a state satisfying its intended consistency condition.
- Concurrent transaction T2 commits a conflicting change.
- T1 later attempts an effect.
- Under Serializable isolation, the database may abort T1 with a serialization failure; T1 must retry from a new state.

Again:

`valid earlier observation != guaranteed later commit`.

## 7. Surviving source-sensitive separation

`check-time condition != cross-time preservation relation != use-time condition != operation admission != committed/effective result`.

This is a temporal audit schema, not a claim that every system exposes five named stages.