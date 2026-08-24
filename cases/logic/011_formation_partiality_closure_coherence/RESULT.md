# COH-001 Result

Status: **first analysis completed**.

Final judgment: **compatible**, with explicit design/signature boundaries. No internal contradiction or countermodel to the current Formation Axiom System was found within the declared typed set-theoretic scope.

This is a coherence and consistency-oriented model-class audit. It is not an absolute consistency proof for ZFC, not a completeness theorem for a separate proof calculus, and not a claim that every future DSD extension inherits the result automatically.

## 1. External formal reconstruction

The Formation Axiom System can be reconstructed using ordinary set-theoretic ingredients:

- set-sized typed carriers for material items, expressions, configurations, quantity kinds, roles, value spaces, and term spaces;
- predicates and relations on the declared carriers;
- partial assignment represented as an ordinary function on an explicitly declared subdomain;
- graphs and local restrictions derived from that function;
- induced relational structures on retained material subsets;
- explicit definitions that expand primitive data into later-stage derived coordinates;
- typed structure-preserving maps with progressively stronger preservation/reflection requirements.

No DSD-specific term has to be identified with a standard logical term in order to perform this reconstruction.

## 2. DSD clause-by-clause comparison

| DSD item | COH-001 judgment | Reason |
| --- | --- | --- |
| Stage-V partial assignment `q_{L,lambda}: Q_{L,lambda} -> V_{L,lambda}` | compatible | It is a total function on its declared domain and a genuine partial assignment relative to the wider active material carrier. No default value is assigned outside the domain. |
| Expression/configuration carrier separation | compatible | Separate typed carriers and typed relations are ordinary many-sorted/set-theoretic structure. |
| `Res_L` and `Realize_L` typing | compatible | `Res_L` relates expression data to expression data, while `Realize_L` relates expression data to configuration data; no sort collision is required. |
| Anchor restriction equations | compatible | Under the manuscript's explicit restriction convention, function equality forces the required domain inclusion. The displayed subset condition is therefore partly typing-induced rather than an independent constraint. |
| Induced material-record inheritance | design/signature boundary | The manuscript deliberately uses a relational material-internal signature. For that signature, retained subsets admit induced structures directly. Internal function symbols with codomain in the material carrier would require an additional closure condition. |
| Closure Clause IV | compatible | `Psi_L` and `A*_L` are already expressible in primitive vocabulary, so configuration describability can be fixed definitionally without a reverse dependency on Stage V. |
| Closure Clause VI | compatible | Once configuration describability, assignment graphs, and roles are fixed, channel membership is pointwise determined. |
| Closure Clause VII | compatible relative to supplied term data | Once `C_L`, `W_L`, and `T_L: C_L -> W_L` are supplied, the finite composition domain and finite sums are uniquely determined. |
| Theorem 3.3 unique relative closure | compatible in its stated model-class sense | The closure coordinates are functionally determined from the primitive core plus the explicitly supplied post-Stage-VI term data. No additional primitive admissibility condition is introduced by the closure equations themselves. |
| Forward map / embedding / strict isomorphism hierarchy | compatible | The hierarchy follows increasing preservation strength: forward preservation, then injectivity/reflection and witness reflection, then bijective full-structure comparison. |
| Identification with syntactic definitional/Morita/categorical equivalence | non-corresponding but not contradictory | The manuscript explicitly declines these identifications. Its result is presentation-sensitive and model-class based. |

## 3. Primitive versus definitional closure

The dependency order is acyclic in the declared presentation.

1. Primitive typed data, predicates, `Res_L`, `Realize_L`, assignments, and roles are supplied subject to Primitive Axioms I–III and V.
2. The primitive-vocabulary witness formula `Psi_L(p)` is evaluated and `A*_L` is obtained from it.
3. Closure IV fixes `Descfg_L`, `Kdes_L`, and `A_L`, with `A_L = A*_L`.
4. Stage-V assignment graphs and configuration-local restrictions are set-theoretically derived from the regime-global partial assignment maps.
5. Closure VI fixes `Chan_L` and therefore `C_L`.
6. Only after `C_L` has been fixed are the term space `W_L` and component-term map `T_L: C_L -> W_L` supplied.
7. Closure VII then fixes `P_fin(C_L)` and every finite composite sum.

The important anti-circularity point is that Primitive Axiom V is stated using `A*_L`, which is available in primitive vocabulary, rather than requiring the later symbol `A_L` as a logically prior input.

Theorem 3.3 should therefore be read exactly as the manuscript states it: a **unique relative expansion of model data**, not a proof-theoretic conservativity theorem. This scope distinction is mathematically important and was preserved in the audit.

## 4. Finite witness and limitations

The bundled deterministic witness checker was executed against the prepared one-material, one-expression, one-configuration model. The obtained output matches `expected_output.txt`:

```text
Axiom I: True
Axiom II: True
Axiom III: True
Axiom V: True
Describable configurations: ['p']
A*: ['a']
Channels: [('p', 'a', 'lambda', 0, 'rho')]
```

Thus the tested primitive data are jointly satisfiable and produce a nonempty channel set containing a defined-zero channel.

This finite execution is only a sanity check. It does not replace the manuscript's general ZFC model-existence argument, clause-independence proofs, or unique-expansion proof. It also does not enumerate all finite formation models.

## 5. Structure-preserving map comparison

The three comparison strengths are coherent but not interchangeable.

- A forward formation map preserves source-positive formation data and component terms in the declared direction.
- A formation embedding adds injectivity, reflection on the source image, exact retained-material behavior, and witness reflection. The witness-reflection clause is a genuine DSD strengthening needed because a target configuration could otherwise acquire a describability witness outside the image of the source.
- Strict base-fixed formation isomorphism is the bijective full-descriptor case and preserves both successful and unsuccessful candidate structure under the fixed comparison base.

This is compatible with the ordinary homomorphism/embedding/isomorphism pattern while remaining more specific because DSD declares additional typed coordinates and witness conditions.

## 6. Non-correspondences and design boundaries

### 6.1 Relational material signature

The claim that every retained material subset has an induced material-record structure depends on the declared relational internal signature. If material-internal function symbols with codomain in the material carrier were admitted, arbitrary subsets would not automatically be closed under those functions. This is a **declared signature boundary**, not a contradiction in the present theory.

### 6.2 Post-Stage-VI term supply

Closure VII is unique only relative to an explicitly supplied vector space and component-term map. The formation core does not derive a physically or analytically privileged `T_L`. This is a **declared data boundary** and is correctly separated from closure.

### 6.3 Definitional-extension terminology

The current theorem establishes unique model expansion relative to supplied data. It does not supply the syntactic apparatus needed to promote the claim to proof-theoretic definitional conservativity. The manuscript already states this limitation, so no correction is required.

### 6.4 Strict equivalence

Strict DSD equivalence is deliberately presentation-sensitive. It should not be used as a synonym for definitional equivalence, Morita equivalence, categorical equivalence, or empirical equivalence.

## 7. Final judgment

**COH-001: compatible.**

No internal contradiction was found among the tested Formation axioms, closure clauses, typing conventions, partial assignments, or comparison-map hierarchy. The key dependency graph is acyclic, the partial-function semantics are coherent, the closure construction is uniquely determined in the stated relative sense, and an explicit nonempty finite witness is reproducible.

The judgment carries two explicit boundaries:

1. induced-substructure claims rely on the manuscript's relational material signature;
2. Stage-VII closure is relative to supplied post-Stage-VI term data.

Neither boundary invalidates the current Formation Axiom System. Both become new obligations only if the signature or post-Stage-VI interface is enlarged in future work.

## 8. What is standard mathematics versus DSD-specific

### Standard mathematical infrastructure

- set-coded typed carriers and predicates;
- partial functions and function graphs;
- function restriction and domain equality;
- induced structures for relational signatures;
- reduct/expansion-style coordinate forgetting and addition;
- finite subsets and finite vector sums;
- preservation / reflection / bijection hierarchy for structure maps.

### DSD-specific organization and constraints

- the exact seven-stage formation order;
- `Psi_L` as the configuration-describability witness formula;
- `A*_L` as the assignment gate available in primitive vocabulary;
- operational channel identity `(p, a, lambda, v, rho)` including assigned value and role;
- separation of undefined assignment, defined zero, channel absence, and zero component term;
- formation traces that preserve witness history without adding it to channel identity;
- witness-reflecting formation embeddings;
- fixed-base strict comparison of the complete candidate formation descriptor, including unsuccessful candidates;
- the first-branching comparison theory built on the staged descriptor chain.

Accordingly, COH-001 does not support the claim that DSD created partial functions, typed structures, or model isomorphism. It supports the narrower and more useful conclusion that the Formation Axiom System combines those standard tools into a DSD-specific staged architecture without an internal coherence failure detected by this audit.