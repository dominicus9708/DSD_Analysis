"""Finite semantic witness for K_R-004 / Global Case 042.

This is NOT a complete OWL 2 reasoner. It instantiates the equality,
inequality, annotation-insensitivity, substitution, and functionality patterns
used in the analysis.
"""

base_models = [
    {"a": "x", "b": "x"},
    {"a": "x", "b": "y"},
]


def same(model):
    return model["a"] == model["b"]


def different(model):
    return model["a"] != model["b"]


same_models = [model for model in base_models if same(model)]
different_models = [model for model in base_models if different(model)]

print(f"BASE MODELS: {len(base_models)}")
print(f"BASE entails SameIndividual(a,b): {all(same(m) for m in base_models)}")
print(
    "BASE entails DifferentIndividuals(a,b): "
    f"{all(different(m) for m in base_models)}"
)
print(f"SAME-AXIOM MODELS: {len(same_models)}")
print(
    "SAME ontology entails SameIndividual(a,b): "
    f"{all(same(m) for m in same_models)}"
)
print(f"DIFFERENT-AXIOM MODELS: {len(different_models)}")
print(
    "DIFFERENT ontology entails DifferentIndividuals(a,b): "
    f"{all(different(m) for m in different_models)}"
)

same_relation_model = {
    "a": "x",
    "b": "x",
    "c": "z",
    "P": {("x", "z")},
}
p_ac = (same_relation_model["a"], same_relation_model["c"]) in same_relation_model["P"]
p_bc = (same_relation_model["b"], same_relation_model["c"]) in same_relation_model["P"]
print(f"SAME substitution P(a,c)->P(b,c): {p_ac and p_bc}")

annotation_models = base_models[:]
print(f"SAME-LABEL annotation models retained: {len(annotation_models)}")
print(f"SAME-LABEL entails identity: {all(same(m) for m in annotation_models)}")

functional_models = []
for model in base_models:
    targets = {model["a"], model["b"]}
    if len(targets) <= 1:
        functional_models.append(model)

print(f"FUNCTIONAL+two-edges MODELS: {len(functional_models)}")
print(
    "FUNCTIONAL+two-edges entails SameIndividual(a,b): "
    f"{all(same(m) for m in functional_models)}"
)
