"""Finite model-theoretic witness for K_R-001 / Global Case 039.

This is NOT a complete OWL 2 reasoner. It instantiates the single
object-property relation-membership pattern used in the OWL 2 Direct
Semantics to witness non-entailment under an unconstrained pair.
"""

models = [
    {"P_ab": False},
    {"P_ab": True},
]


def entails_positive(candidate_models):
    return all(model["P_ab"] for model in candidate_models)


def entails_negative(candidate_models):
    return all(not model["P_ab"] for model in candidate_models)


base_models = models[:]
negative_assertion_models = [model for model in models if not model["P_ab"]]
positive_assertion_models = [model for model in models if model["P_ab"]]

print(f"BASE MODELS: {len(base_models)}")
print(f"BASE entails P(a,b): {entails_positive(base_models)}")
print(f"BASE entails not P(a,b): {entails_negative(base_models)}")
print(f"NEGATIVE-ASSERTION MODELS: {len(negative_assertion_models)}")
print(
    "NEGATIVE ontology entails not P(a,b): "
    f"{entails_negative(negative_assertion_models)}"
)
print(f"POSITIVE-ASSERTION MODELS: {len(positive_assertion_models)}")
print(
    "POSITIVE ontology entails P(a,b): "
    f"{entails_positive(positive_assertion_models)}"
)
print(f"CLASS-ONLY: C(a) leaves P(a,b) free across {len(base_models)} P-variants")
print("CLOSED-WORLD policy on absent P(a,b): false (extra rule, not OWL entailment)")
