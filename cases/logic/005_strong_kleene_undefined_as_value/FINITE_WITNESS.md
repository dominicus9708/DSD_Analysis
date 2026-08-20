# Case 005 — Finite Witness

## 1. DSD partial assignment

Let

- `A = {u,z,n}`,
- `V = {0,1}`,
- `Q = {z,n}`,
- `q(z)=0`,
- `q(n)=1`.

Then `q(u)` is undefined because `u notin Q`.

The three local DSD states are therefore

- `u`: undefined assignment;
- `z`: defined zero;
- `n`: defined nonzero.

The crucial point is that the first state is determined by domain exclusion, while the latter two are graph/value states.

## 2. A three-symbol external encoding

Let `bot` be a fresh symbol with `bot notin V`, and define

`V^bot = V disjoint-union {bot}`.

Define the total encoding

`qhat(a) = q(a)` if `a in Q`, and `qhat(a)=bot` if `a notin Q`.

Thus

- `qhat(u)=bot`,
- `qhat(z)=0`,
- `qhat(n)=1`.

The original partial map is exactly recoverable:

- `Q = {a in A : qhat(a) != bot}`;
- `q = qhat restricted to Q`.

Hence using a fresh sentinel in an enlarged codomain can be a faithful external representation of partiality.

## 3. Why this is not yet Strong Kleene semantics

For this specific binary value carrier there is a set bijection

- `0 <-> false`,
- `bot <-> unknown`,
- `1 <-> true`.

But this bijection alone does not preserve mathematical role.

In Strong Kleene logic, `false`, `unknown`, and `true` are truth values, and logical connectives act on all three values.

In DSD:

- `0` is a distinguished assignment value, not logical falsity;
- `1` is merely another assignment value, not logical truth;
- `bot` is not supplied by the Formation value space at all;
- no Strong-Kleene conjunction, disjunction, or negation is defined on DSD assignment status.

Therefore the three-element cardinality coincidence does not constitute structural equivalence.

## 4. Channel test

Assume the configuration and role conditions required by Stage VI hold for all three items.

With the original DSD partial assignment:

- `z` can support a zero-valued channel;
- `n` can support a nonzero-valued channel;
- `u` cannot support any channel because there is no graph pair `(u,v)`.

If the external total encoding is incorrectly substituted for Stage V by setting the assignment domain to all of `A` and treating `bot` as an ordinary Stage-V value, then `(u,bot)` becomes an assignment-graph pair and may generate an extra channel.

Thus

`faithful external encoding != semantics-preserving substitution into the original formation layer`.

The sentinel is safe as representation metadata only while its external status is retained.

## 5. General theorem

For any partial map `q:Q -> V` and any fresh `bot notin V`, the lifted totalization

`L_bot(q): A -> V disjoint-union {bot}`

is injective as an encoding of partial maps, because both the original domain and values are reconstructible.

By contrast, replacing undefined inputs by an existing `v0 in V` is not injective whenever a genuinely defined input may also take `v0`.

This separates three operations:

1. original partial semantics;
2. faithful lifted representation with a fresh status symbol;
3. unfaithful value padding with an ordinary value.
