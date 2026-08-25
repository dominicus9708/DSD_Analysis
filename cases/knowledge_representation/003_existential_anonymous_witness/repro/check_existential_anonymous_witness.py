"""Finite witness for K_R-003 / Global Case 041.

This is not a complete OWL 2 reasoner. It instantiates the
ObjectSomeValuesFrom(P C) semantic condition over a tiny domain.
"""

DOMAIN = ("A", "B", "W")
A = "A"  # interpretation of named individual a
B = "B"  # interpretation of named individual b

M_UNNAMED = {
    "C": {"W"},
    "P": {("A", "W")},
}

M_NAMED_B = {
    "C": {"B"},
    "P": {("A", "B")},
}


def satisfies_existential(model):
    return any((A, y) in model["P"] and y in model["C"] for y in DOMAIN)


def p_ab(model):
    return (A, B) in model["P"]


def c_b(model):
    return B in model["C"]


models = [M_UNNAMED, M_NAMED_B]

print(f"M_UNNAMED satisfies existential: {satisfies_existential(M_UNNAMED)}")
print(f"M_UNNAMED P(a,b): {p_ab(M_UNNAMED)}")
print(f"M_UNNAMED C(b): {c_b(M_UNNAMED)}")
print(f"M_NAMED_B satisfies existential: {satisfies_existential(M_NAMED_B)}")
print(f"M_NAMED_B P(a,b): {p_ab(M_NAMED_B)}")
print(f"M_NAMED_B C(b): {c_b(M_NAMED_B)}")
print(
    "EXISTENTIAL entails existence of some P-successor in C: "
    f"{all(satisfies_existential(model) for model in models)}"
)
print(f"EXISTENTIAL entails P(a,b): {all(p_ab(model) for model in models)}")
print(f"EXISTENTIAL entails C(b): {all(c_b(model) for model in models)}")
