# Result — LING-004 / Global Case 017

## 1. Main finding
Linguistic ambiguity is not faithfully represented as mere undefinedness.

The relevant external structure is:

`one surface sign/sentence -> multiple legitimate interpretation candidates`.

Each candidate may be individually well formed and semantically defined. The unresolved state therefore differs from both `no interpretation is available` and `one particular interpretation has already been selected`.

## 2. External distinction
The Stanford Encyclopedia of Philosophy distinguishes ambiguity from vagueness, context sensitivity, and underspecification. It treats lexical and syntactic/scope ambiguity as major families and notes that one surface form may correspond to multiple meanings or logical forms.

Hence:

`surface expression != unique interpretation`.

## 3. Finite scope witness
For

`Every woman squeezed a man`,

consider two readings:

`m1 = forall x exists y ...`

and

`m2 = exists y forall x ...`.

In a finite model where two women squeezed different men and no one man was squeezed by both, `m1` is true and `m2` false.

Thus the choice of interpretation can alter the truth condition while the surface sentence remains fixed.

## 4. Predefinition restraint
If `Cand(u)={m1,m2}`, unresolved ambiguity does not license

`Selected(u)=m1`

without an additional disambiguation rule or contextual bridge.

Later context may select `m1`, but that does not imply that `m1` was uniquely fixed before the selection step.

Therefore:

`multiple legitimate candidates + later selection != unique prior meaning`.

This is an independent linguistic corroboration of the general predefinition-restraint pattern.

## 5. Important pressure on Formation encoding
Formation Primitive Axiom V uses one partial function per quantity-kind. One exact assignment input cannot receive two ordinary output values simultaneously.

Therefore ambiguity must NOT be encoded naively as

`q(u)=m1` and `q(u)=m2`

for one exact input.

A faithful DSD application needs an explicit branching representation, e.g. distinct interpretation-candidate objects, distinct configurations, or distinct tagged channels. The application may then retain the common surface provenance while preserving candidate identity.

This is a useful design boundary rather than a contradiction: the core Formation system remains single-valued, while the linguistic bridge must expose ambiguity before assignment or encode candidate identity into the typed input/channel structure.

## 6. Ambiguity is not undefinedness
This case materially differs from LING-001.

- LING-001: an interpretation/reference may fail to be defined.
- LING-004: several interpretations may each be defined while no unique interpretation has yet been selected.

Therefore:

`undefined interpretation != unresolved multiple interpretation candidates`.

This distinction should be retained in any future DSD application taxonomy.

## 7. Ambiguity is not vagueness
The external literature also distinguishes ambiguity from vagueness. Ambiguity provides multiple candidate meanings/readings; vagueness concerns imprecise or borderline application under a meaning.

This justifies treating the next planned LING case on vagueness as an independent node rather than an extension of the present case.

## 8. Formation correspondence
The Formation system supports the application in two ways:

1. it does not force candidate expressions to be downstream-described or assigned;
2. its typed channel identity can preserve distinctions once the application supplies distinct candidate structures/tags.

But it does not supply lexical senses, parse trees, scope resolution, speaker intention, or context-driven disambiguation. Those remain external linguistic bridges.

## 9. Axis-Property system
Not required for the core result. Formation-level typing and candidate/channel differentiation are sufficient. Axis-Property structure would only become relevant if a later application attaches additional typed relations/properties to already distinguished interpretation candidates.

## 10. Final judgment
- No contradiction with the current Formation or Axis-Property systems was found.
- Ambiguity supplies an independent external node for `candidate multiplicity != selected value`.
- Preselecting one reading without a rule is structurally unjustified and can change truth conditions.
- The case exposes a real representation boundary: ambiguity must be represented by candidate branching or tags, not by violating single-valued assignment.
- DSD does not derive a linguistic theory of ambiguity.

Overall classification:
`structural reinterpretation = supported`,
`coherence = supported`,
`predefinition restraint = independently corroborated`,
`representation pressure = explicit candidate branching required`,
`DSD-original ambiguity theory = not supported`.
