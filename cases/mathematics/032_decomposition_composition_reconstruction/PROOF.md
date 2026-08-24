# Proof

## 1. Forward uniqueness is not inverse uniqueness

Once the Stage-VI record, term space `W_L`, and term map `T_L:C_L->W_L` are fixed, Stage VII defines one function

`Comp_L(F)=sum_{c in F}T_L(c)`.

This proves uniqueness of the **forward closure**.

It does not imply injectivity of `Comp_L`. A function can be uniquely defined and still send distinct inputs to the same output.

Therefore:

`unique Clause-VII completion` does not imply `unique source reconstruction`.

## 2. Fixed-support variable components

For subspaces `U_c <= W_L`, define

`Sigma_F((u_c))=sum_c u_c`.

Suppose the sum is direct. If

`Sigma_F(u)=Sigma_F(v)`,

then

`sum_c (u_c-v_c)=0`.

Uniqueness of the zero decomposition in a direct sum gives `u_c=v_c` for every `c`, so `Sigma_F` is injective.

Conversely, if `Sigma_F` is injective and a vector has two decompositions, equality of their sums implies equality of their tuples. Hence the decomposition is unique and the sum is direct.

Thus direct-sum decomposition is equivalent to injectivity of the canonical sum map on the full product of the selected subspaces.

## 3. Relation to the DSD fixed-support kernel theorem

The DSD static map on fixed support is

`S_F:W_L^F->W_L`, `S_F(y)=sum_c y_c`.

On the full product, if `W_L != {0}` and `|F|>=2`, choose distinct `c_1,c_2` and `u!=0`:

`y_{c_1}=u`, `y_{c_2}=-u`, all others zero.

Then `y!=0` but `S_F(y)=0`, so full arbitrary decomposition is nonunique.

For a restricted admissible class `A_F`, the source theorem gives the exact more general criterion

`(A_F-A_F) intersect ker S_F={0}`.

A direct-sum product `A_F=product_c U_c` satisfies this criterion exactly when the `U_c` form an internal direct sum. But non-linear or otherwise restricted `A_F` can also satisfy the DSD criterion without any direct-sum subspace model.

Therefore direct sum is a standard structured sufficient condition, not a DSD necessity for every admissible record class.

## 4. Exact Stage-VII support-reconstruction criterion

Fix finite `C_0 subset C_L` and define

`Phi_T(F)=sum_{c in F}T_L(c)` for `F subset C_0`.

Assume `Phi_T(F)=Phi_T(G)`. Subtracting gives

`sum_{c in F\G}T_L(c)-sum_{c in G\F}T_L(c)=0`.

Define `epsilon_c=1` on `F\G`, `-1` on `G\F`, and `0` elsewhere. Then

`sum_c epsilon_c T_L(c)=0`, `epsilon_c in {-1,0,1}`.

Conversely every nontrivial such signed relation determines two distinct disjoint supports from its positive and negative coefficients and hence a collision of subset sums.

Therefore `Phi_T` is injective iff there is no nontrivial signed `{-1,0,1}` relation among the channel-indexed terms.

When `T_L` is injective, this is exactly the standard dissociated-set condition on `T_L[C_0]`.

## 5. Linear independence is stronger than necessary

Linear independence forbids all nontrivial scalar relations and therefore implies the signed `{-1,0,1}` condition.

But it is not necessary. In `W_L=R`, the terms `1` and `2` are linearly dependent over `R`, yet their subset sums are

`0,1,2,3`,

all distinct. Hence Stage-VII support can be reconstructible without linear independence or a direct-sum decomposition of `W_L`.

## 6. Zero terms expose the DSD support boundary

If some admitted channel `c` has `T_L(c)=0`, then

`Comp_L(emptyset)=0=Comp_L({c})`.

Hence the support map is immediately noninjective. This is exactly why DSD distinguishes channel absence from an admitted channel with zero contribution.

At the analytic-record level, even channel-specific direct-summand coordinates cannot distinguish an absent coordinate from a selected coordinate whose value is zero unless support is separately retained or selection is constrained to nonzero values.

## 7. Combined record layer

The static paper's combined map

`S_{F,G}:W_L^F direct-sum U_A^G -> W_L direct-sum U_A`

has kernel `ker S_F direct-sum ker P_G` and the exact difference-set criterion for injectivity on an admissible class.

Thus the channel and typed-property reconstruction problem is the product of the same standard injectivity problem in the two aggregate coordinates.
