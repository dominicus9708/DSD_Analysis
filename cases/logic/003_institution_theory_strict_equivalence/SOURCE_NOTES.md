# Case 003 — Source Notes

## External source discipline
Primary comparison source:

- Joseph A. Goguen and Rod M. Burstall, *Institutions: Abstract Model Theory for Specification and Programming*, Journal of the ACM 39(1), 95–146 (1992), DOI: 10.1145/147508.147524.

Author-maintained UCSD material describes institutions as an abstraction of the notion of a logical system. The core data are signatures, sentence translation, model reduct/translation, and a signature-indexed satisfaction relation.

## Satisfaction condition
For a signature morphism

`phi: Sigma -> Sigma'`,

Institution Theory pairs:

- covariant sentence translation `Sen(phi): Sen(Sigma) -> Sen(Sigma')`, and
- contravariant model reduct `Mod(phi): Mod(Sigma') -> Mod(Sigma)`.

The satisfaction condition requires truth to be invariant under the translation/reduct pair:

`M' |=_{Sigma'} Sen(phi)(e)  iff  Mod(phi)(M') |=_{Sigma} e`.

The conceptual content is invariance of truth under a declared change of notation/signature.

## What this condition does not say
The satisfaction condition does not require:

- `Sigma` and `Sigma'` to be isomorphic signatures;
- `M'` and its reduct to have identical signatures;
- the model translation to be bijective;
- all internal structure of the richer model to be reconstructible from the reduct.

A signature inclusion may add symbols, and reduct then forgets their interpretation while preserving truth of sentences from the smaller signature.

## DSD source discipline
The current Formation Axiom System defines strict base-fixed formation isomorphism by bijections on the material, expression, configuration, quantity-kind, and role carriers; zero-preserving bijections on pointed value spaces; and a linear isomorphism on term spaces, together with conditions (E1)–(E9).

The paper explicitly states:

- coordinate names may differ when the anchored base structure is preserved;
- strict comparison induces a bijection on admitted channels and preserves finite composites;
- composite-level coincidence does not imply strict equivalence;
- forward formation maps and embeddings are weaker structure-preserving notions than strict isomorphism.

## Comparison warning
Institution Theory's satisfaction condition and DSD strict formation isomorphism are not the same mathematical relation.

Institution Theory asks whether truth is invariant under signature translation/model reduct. DSD strict equivalence asks whether two complete formation descriptors over a fixed comparison base are isomorphic through all declared formation coordinates.

Therefore the external node can support only the methodological principle that a comparison must state what is translated and what is preserved. It cannot independently prove the DSD conditions (E1)–(E9).
