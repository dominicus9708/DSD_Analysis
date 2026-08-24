# Standard Mathematics Sources

## Direct sums

1. Encyclopedia of Mathematics, **Direct sum**:
   https://encyclopediaofmath.org/wiki/Direct_sum

   Relevant standard facts:
   - direct sums are built from component structures with canonical embeddings;
   - for vector spaces and related additive structures, direct-sum decomposition is the standard structure for independent additive components.

2. Sheldon Axler, **Linear Algebra Done Right**, official open-access site:
   https://linear.axler.net/

   Relevant standard theorem used in this case:
   for subspaces `V_1,...,V_m`, the canonical sum map
   `Gamma(v_1,...,v_m)=v_1+...+v_m`
   is injective exactly when the sum is direct; equivalently the additive decomposition is unique.

## Distinct subset sums / dissociated sets

3. Benjamin Bedert, **On Unique Sums in Abelian Groups**, Combinatorica (Springer):
   https://link.springer.com/article/10.1007/s00493-023-00069-w

   Definition used:
   a subset `S` of an Abelian group is dissociated when the only signed relation
   `sum_s mu_s s=0`, `mu_s in {-1,0,1}`
   is the trivial one. Equivalently, distinct subsets of `S` have distinct subset sums.

## Source-use rule

Direct-sum uniqueness is used for variable component decompositions. Dissociativity is used for the different problem of recovering a finite selected support from a sum of fixed channel terms. The two conditions are related but not identified.
