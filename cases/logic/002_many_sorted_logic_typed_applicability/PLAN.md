# Case 002 — Many-Sorted Logic and Typed Applicability

## Status
Active mathematical analysis.

## Why this is the second case
The DSD Analysis roadmap places Many-Sorted Logic immediately after the partial-functions case. The original lightweight comparison asked whether a wrong-sort input can be treated as an ordinary false/zero result and compared this with the typed profiles of the Axis-Property System.

Case 002 refines that roadmap mapping before testing it. A wrong-sort expression is **not** identified with DSD `unavailable input`. In the DSD Axis-Property System:

- a wrong-sort object lies outside the typed input product required by the property profile, so the attempted application is not evaluated as an application of that property kind;
- `unavailable input` means that a carrier required by the profile is itself unavailable at the configuration;
- `undefined application` is evaluated only after the full typed input product is available and the chosen input lies inside that product but outside the partial assignment domain;
- `defined zero` is a well-typed input inside the assignment domain with the designated zero value.

This correction is part of the result, not a change to the Axis-Property axioms.

## Research question
Does the many-sorted distinction between well-sorted and ill-sorted applications support the DSD requirement that type applicability be resolved before an ordinary value such as zero is assigned?

Secondary question: does ordinary many-sorted logic also support DSD `unavailable input` and `undefined application`, or are those additional DSD layers requiring separate comparison frameworks?

## DSD layer under test
Primary:

- Shared axis-property signature, especially the sort universe and typed profile map.
- Definition 3.2, input-sort interpretation and carrier availability.
- Definition 3.3, typed partial property assignment.
- Definition 3.10, property status.
- Closure Clause 4.2, property typing.

Not directly tested:

- Primitive Axiom PI (total realization of selected axis channels).
- Primitive Axiom PII (bilinear-dependency compatibility).
- representation, closure, aggregation, or dynamics layers.

## External comparison target
Use standard many-sorted first-order typing practice as the external node.

Primary/authoritative references:

- SMT-LIB Standard Version 2.7, Barrett, Fontaine, Tinelli — official many-sorted formal language and signatures.
- CVC3 User Manual — explicitly states the usual first-order many-sorted typing rule: a function application has type T only when every argument has the corresponding declared input type; ill-typed terms are rejected.

Boundary reference:

- Standard translations from many-sorted to unsorted first-order logic preserve sort information by explicit predicates/constraints. Therefore the case does not claim that sorting is irreducible; it tests whether sort information may be discarded without loss.

## Minimal witness plan
Use two distinct sorts `A` and `B`, nonempty carriers, and a unary Boolean-valued predicate/property expecting only sort `A`.

Choose a well-sorted `a : A` for which the property value is false/zero and an object `b : B`.

Then compare:

1. the typed representation, where `P(a)=0` is a valid defined result while `P(b)` is not a well-sorted application;
2. a type-erased representation that puts both carriers into one raw universe and assigns the fallback value `0` to wrong-sort inputs.

If the second representation maps both states to the same raw value, it cannot reconstruct well-sortedness from the raw output alone.

## Success criterion
Case 002 supports the tested DSD typing distinction if:

- standard many-sorted syntax independently requires sort-correct inputs before semantic value evaluation;
- a finite witness proves that erasing the sort boundary and using an ordinary fallback value can collapse a valid zero result with an ill-typed attempted application;
- DSD's own typed profile already prevents this collapse without contradiction.

## Failure criterion
The case would count against the DSD typing design if the DSD definitions forced a wrong-sort object to receive an ordinary property value, or if its status definitions conflated wrong-sort, unavailable-carrier, undefined, and defined-zero cases.

## Expected classification
To be determined after proof. The likely mapping is strong for `typed profile / well-sortedness`, weak or absent for `carrier unavailable`, and dependent on Case 001 for partial undefinedness.
