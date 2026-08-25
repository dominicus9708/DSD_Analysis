"""Finite semantic witness for K_R-002 / Global Case 040.

This is not a full OWL 2 reasoner. It instantiates the Direct-Semantics
conditions for class membership, object-property domain/range, and
functionality over a two-object finite domain.
"""

models = [
    {
        "name": "M_empty",
        "C": {"a"},
        "D": {"b"},
        "P": set(),
    },
    {
        "name": "M_edge",
        "C": {"a"},
        "D": {"b"},
        "P": {("a", "b")},
    },
]


def class_assertion(model):
    return "a" in model["C"]


def domain_axiom(model):
    return all(x in model["C"] for x, _ in model["P"])


def range_axiom(model):
    return all(y in model["D"] for _, y in model["P"])


def functional_axiom(model):
    targets = {}
    for x, y in model["P"]:
        targets.setdefault(x, set()).add(y)
    return all(len(values) <= 1 for values in targets.values())


def p_ab(model):
    return ("a", "b") in model["P"]


admissible = []
for model in models:
    ok = (
        class_assertion(model)
        and domain_axiom(model)
        and range_axiom(model)
        and functional_axiom(model)
    )
    print(
        f"{model['name']}: class={class_assertion(model)} "
        f"domain={domain_axiom(model)} range={range_axiom(model)} "
        f"functional={functional_axiom(model)} P(a,b)={p_ab(model)}"
    )
    if ok:
        admissible.append(model)

print(f"ADMISSIBLE MODELS: {len(admissible)}")
print(f"CONSTRAINT SET entails P(a,b): {all(p_ab(m) for m in admissible)}")
print("REVERSE DIRECTION with actual P(a,b): domain classifies a in C and range classifies b in D")
