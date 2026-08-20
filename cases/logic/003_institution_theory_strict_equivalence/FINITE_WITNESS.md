# Case 003 — Finite Witnesses

## Test A — Pure renaming must preserve strict equivalence

Fix one common base `B` with support carrier `{s}` and scalar field `R`.

### Regime L
- material carrier: `{a}`
- expression carrier: `{x}`
- configuration carrier: `{p}`
- quantity kinds: `{lambda}`
- roles: `{rho}`
- value space: `V_lambda = R`, distinguished zero `0`
- `mat_L(x) = act_L(p) = {a}`
- both anchors send `a` to `s`
- `x` is admitted and describable
- `Res_L(x,x)` and `Realize_L(x,p)` hold
- all three configuration-admission predicates hold at `p`
- assignment domain `Q_{L,lambda}={a}` with `q_{L,lambda}(a)=1`
- `Role_L(p,a,lambda,rho)` holds
- hence one channel `c=(p,a,lambda,1,rho)` is admitted
- term space `W_L=R`, `T_L(c)=1`

### Regime M
Use fresh labels `{b}`, `{y}`, `{r}`, `{mu}`, `{sigma}` and copy every structural declaration through the bijections

- `Phi_M(a)=b`
- `Phi_E(x)=y`
- `Phi_P(p)=r`
- `tau_Lambda(lambda)=mu`
- `tau_R(rho)=sigma`
- `I_lambda=id_R`
- `J=id_R`.

Every anchor still lands at the same fixed support point `s`.

### Verification
- (E1): material structure, material/active membership, and anchors are preserved.
- (E2): expression admission/describability agree.
- (E3): restriction and realization agree.
- (E4): configuration predicates agree.
- (E5): assignment-domain membership agrees.
- (E6): assignment graphs agree under the induced maps.
- (E7): vacuous if no negligible-status kind is declared.
- (E8): role relation agrees.
- (E9): `J(T_L(c)) = 1 = T_M(Phi_C(c))`.

Therefore

`Sigma_L ~=^fix_B Sigma_M`.

### Result
Strict equivalence is invariant under pure renaming when the declared anchored structure is preserved. The definition is not accidentally dependent on literal object names.

---

## Test B — Composite equality must not force strict equivalence

Take two full finite formation models over the same base.

### Regime L
One admitted channel `c0` with

`T_L(c0)=0`.

For the selected nonempty family `{c0}`,

`Comp_L({c0})=0`.

### Regime M
Two admitted channels `d+`, `d-` with

`T_M(d+)=1`,
`T_M(d-)=-1`.

For the selected family `{d+,d-}`,

`Comp_M({d+,d-})=0`.

Hence the selected composites coincide under `J=id_R`.

But

`|C_L|=1 != 2=|C_M|`.

A strict comparison would have to induce a bijection of admitted channel sets, which is impossible. Therefore the descriptors are strictly non-equivalent.

### Result
`same composite output` does not imply `same formation structure`.

This reproduces the structural pattern formalized in Formation Proposition 6.22 and confirms that the strict relation is not collapsed to aggregate equality.

---

## Test C — Satisfaction preservation can be weaker than isomorphism

This witness belongs to the external Institution-Theory side and is used only as a comparison boundary.

Let

`Sigma = {P}`

be a first-order signature with one unary predicate and let

`Sigma' = {P,Q}`

extend it by another unary predicate. Let `phi: Sigma -> Sigma'` be the inclusion.

Take a `Sigma'`-model `M'` with domain `{0,1}` and

- `P^{M'}={0}`
- `Q^{M'}={1}`.

The reduct `Mod(phi)(M')` forgets `Q` and retains the same domain and interpretation of `P`.

Let

`e := exists x P(x)`.

Then

`M' |= Sen(phi)(e)`

and

`Mod(phi)(M') |= e`.

Thus the satisfaction condition holds for this sentence under a signature extension/reduct even though the richer model contains semantic structure (`Q`) that the reduct does not retain.

### Consequence for DSD comparison
This is not a counterexample to DSD strict equivalence because DSD strict base-fixed formation isomorphism is not defined as a general signature-reduct semantics. It deliberately requires bijective preservation of the full formation descriptor over a fixed comparison base.

If a future DSD layer were intended to compare changing formation signatures or to forget declared coordinates while preserving a selected theory/readout, it would need a separately defined weaker translation or reduct relation.

---

## Additional boundary witness — unused codomain extension

Suppose two formation regimes agree on every realized assignment and channel, but their declared pointed value spaces are

- `V_L={0,1}`
- `V_M={0,1,2}`,

with only `1` actually assigned in either regime.

There is no bijection `V_L -> V_M`, so strict equivalence fails even though the realized operational fragment can agree.

This is not an inconsistency. It shows that strict equivalence is **signature/background-sensitive**: it compares the declared full descriptor, not only realized behavior.

Institution Theory makes the alternative design possibility visible: a weaker translation/reduct relation could intentionally forget unused or extra signature structure while preserving selected semantics. The current Formation paper does not claim such a relation as strict equivalence.
