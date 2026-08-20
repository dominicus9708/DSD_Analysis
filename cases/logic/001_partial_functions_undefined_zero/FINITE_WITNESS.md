# Case 001 — Finite Witness and Mathematical Analysis

## 1. Abstract setup

Let `A` be a nonempty input carrier and let `(V,0)` be a pointed value set. A partial assignment is represented by a pair

`(Q,q)` with `Q ⊆ A` and `q: Q -> V`.

Define the naive zero-totalization operator

`T0(Q,q): A -> V`

by

- `T0(Q,q)(a) = q(a)` if `a ∈ Q`,
- `T0(Q,q)(a) = 0` if `a ∉ Q`.

The question is whether `T0(Q,q)` alone retains the original partial-assignment structure.

## 2. Minimal finite witness

Take

- `A = {u,z,n}`,
- `V = {0,1}`,
- `Q = {z,n}`,
- `q(z)=0`,
- `q(n)=1`,
- `q(u)` undefined because `u ∉ Q`.

Then

- `T0(Q,q)(u)=0`,
- `T0(Q,q)(z)=0`,
- `T0(Q,q)(n)=1`.

Thus `u` and `z` have identical totalized values even though their original statuses differ:

- `u`: outside the assignment domain;
- `z`: inside the assignment domain with defined value zero.

This is exactly the collision asserted by DSD Formation Proposition 5.4.

## 3. Theorem 1 — Global non-injectivity of naive zero-totalization

**Theorem.** If `A` is nonempty, then `T0` is not injective on the class of all partial maps from subsets of `A` into `(V,0)`.

**Proof.** Choose `a ∈ A`. Consider

- `P1 = (∅, empty map)`,
- `P2 = ({a}, q2)` with `q2(a)=0`.

For every `x ∈ A`, both totalizations return `0`; hence

`T0(P1)=T0(P2)`.

But `P1 != P2` because their domains differ. Therefore `T0` is not injective. ∎

This proves a stronger statement than the single collision example: as soon as undefinedness and the ordinary zero share one numerical output after domain erasure, distinct partial structures can have the same total representation.

## 4. Theorem 2 — Exact information forgotten by zero-totalization

Let `P1=(Q1,q1)` and `P2=(Q2,q2)`. Then

`T0(P1)=T0(P2)`

if and only if all three conditions hold:

1. for every `a ∈ Q1 ∩ Q2`, `q1(a)=q2(a)`;
2. for every `a ∈ Q1 \ Q2`, `q1(a)=0`;
3. for every `a ∈ Q2 \ Q1`, `q2(a)=0`.

**Proof.**

Assume the totalizations are equal. On the common domain both use their original values, so condition 1 follows. If `a ∈ Q1 \ Q2`, the first totalization gives `q1(a)` while the second gives the padding value `0`; equality forces `q1(a)=0`. Condition 3 is symmetric.

Conversely, if conditions 1–3 hold, inspect each `a ∈ A` according to whether it lies in both domains, only one domain, or neither. In every case the two totalized values are equal. ∎

**Interpretation.** Zero-totalization forgets exactly the information saying which zero-valued points were genuinely inside the original domain. Nonzero values remain recoverable; defined-zero membership does not.

## 5. Corollary — When naive totalization becomes recoverable

Restrict attention to partial assignments satisfying

`q(a) != 0` for every `a ∈ Q`.

Then

`Q = {a ∈ A : T0(Q,q)(a) != 0}`,

and `q` is the restriction of `T0(Q,q)` to that recovered domain. Hence `T0` is injective on this zero-free subclass.

Therefore the DSD objection is **not** that every totalization is mathematically invalid. The information loss occurs when the padding value is also allowed as a legitimate defined value and the original domain/status is discarded.

## 6. Theorem 3 — Status-preserving totalization is injective

Define the status-preserving map

`E(Q,q): A -> V × {0,1}`

by

- `E(Q,q)(a)=(q(a),1)` if `a ∈ Q`,
- `E(Q,q)(a)=(0,0)` if `a ∉ Q`.

Then `E` is injective.

**Proof.** From the second coordinate one reconstructs

`Q = {a ∈ A : second(E(Q,q)(a))=1}`.

On this reconstructed domain, the first coordinate gives `q(a)`. Therefore the original pair `(Q,q)` is uniquely recoverable. ∎

Equivalent recovery is possible by extending the codomain to a disjoint union `V ⊔ {⊥}` and mapping undefined inputs to a new symbol `⊥` that is not an element of `V`.

Thus a total representation can be faithful, but it must preserve the status distinction explicitly.

## 7. DSD channel-level lift

Now interpret the same witness inside the Formation Axiom System.

Choose one describable configuration `p` whose active material contains `u,z,n`, one quantity kind `λ`, and one role `ρ` that is declared for all three items. Let the Stage-V assignment be

- `Q_{L,λ}={z,n}`,
- `q_{L,λ}(z)=0`,
- `q_{L,λ}(n)=1`.

By Closure Clause VI, channel formation requires assignment-graph membership. Therefore:

- `(p,z,λ,0,ρ)` is admitted;
- `(p,n,λ,1,ρ)` is admitted;
- no channel `(p,u,λ,v,ρ)` is admitted for any `v`, because `u` has no assignment-graph pair.

Now construct a second valid formation input by replacing the partial assignment with the zero-totalized assignment:

- `Q'_{L,λ}={u,z,n}`,
- `q'_{L,λ}(u)=0`,
- `q'_{L,λ}(z)=0`,
- `q'_{L,λ}(n)=1`.

Provided the same describability and role data are retained, Closure Clause VI now admits the additional channel

`(p,u,λ,0,ρ)`.

Hence treating the zero-totalized surrogate as if it were the original Stage-V assignment does not merely alter notation; it changes the Stage-VI admitted-channel set.

## 8. Structural comparison of the two DSD models

The two formation structures have different assignment domains and different channel cardinalities:

- partial model: two assignment points and two channels;
- zero-totalized model: three assignment points and three channels.

Therefore they are not strictly formation-equivalent under an identification that is required to preserve assignment domains and channel structure.

This is compatible with the Formation Axiom System's assignment-domain and channel-cardinality obstruction results.

## 9. What this witness proves and does not prove

### Proves

1. DSD Proposition 5.4 is mathematically correct.
2. Its content can be sharpened to a non-injectivity theorem for the zero-totalization map.
3. The lost information is exactly defined-zero domain membership.
4. A status/domain mask or a genuinely new bottom value restores injectivity.
5. In DSD, loss of assignment-domain information can propagate into a different admitted-channel set.

### Does not prove

1. That all total-function encodings are invalid.
2. That undefinedness must be represented in exactly the DSD way.
3. That Primitive Axiom V's regime-global assignment principle follows from standard partial-function logic.
4. That the entire Formation Axiom System is true under every intended application.
5. That LPF and DSD are the same formal theory.
