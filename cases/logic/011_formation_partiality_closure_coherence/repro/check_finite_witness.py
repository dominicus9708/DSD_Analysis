from dataclasses import dataclass
from typing import Dict, FrozenSet, Tuple


@dataclass(frozen=True)
class Model:
    materials: FrozenSet[str]
    expressions: FrozenSet[str]
    configurations: FrozenSet[str]
    mat: Dict[str, FrozenSet[str]]
    act: Dict[str, FrozenSet[str]]
    anch_expr: Dict[Tuple[str, str], str]
    anch_cfg: Dict[Tuple[str, str], str]
    adm_expr: FrozenSet[str]
    des_expr: FrozenSet[str]
    restrictions: FrozenSet[Tuple[str, str]]
    realizations: FrozenSet[Tuple[str, str]]
    adm_cfg: FrozenSet[str]
    lc_cfg: FrozenSet[str]
    bc_cfg: FrozenSet[str]
    q_domain: FrozenSet[str]
    q: Dict[str, int]
    roles: FrozenSet[Tuple[str, str, str, str]]


def build_witness() -> Model:
    return Model(
        materials=frozenset({"a"}),
        expressions=frozenset({"h"}),
        configurations=frozenset({"p"}),
        mat={"h": frozenset({"a"})},
        act={"p": frozenset({"a"})},
        anch_expr={("h", "a"): "s0"},
        anch_cfg={("p", "a"): "s0"},
        adm_expr=frozenset({"h"}),
        des_expr=frozenset({"h"}),
        restrictions=frozenset({("h", "h")}),
        realizations=frozenset({("h", "p")}),
        adm_cfg=frozenset({"p"}),
        lc_cfg=frozenset({"p"}),
        bc_cfg=frozenset({"p"}),
        q_domain=frozenset({"a"}),
        q={"a": 0},
        roles=frozenset({("p", "a", "lambda", "rho")}),
    )


def check_axiom_i(model: Model) -> bool:
    return model.des_expr <= model.adm_expr


def check_axiom_ii(model: Model) -> bool:
    for source, target in model.restrictions:
        if target not in model.adm_expr:
            return False
        if not model.mat[target] <= model.mat[source]:
            return False
        for item in model.mat[target]:
            if model.anch_expr[(target, item)] != model.anch_expr[(source, item)]:
                return False
    return all((expr, expr) in model.restrictions for expr in model.adm_expr)


def check_axiom_iii(model: Model) -> bool:
    for expr, cfg in model.realizations:
        if not model.act[cfg] <= model.mat[expr]:
            return False
        for item in model.act[cfg]:
            if model.anch_cfg[(cfg, item)] != model.anch_expr[(expr, item)]:
                return False
    return True


def psi(model: Model, cfg: str) -> bool:
    if not (cfg in model.adm_cfg and cfg in model.lc_cfg and cfg in model.bc_cfg):
        return False
    return any(
        target in model.des_expr and (target, cfg) in model.realizations
        for _, target in model.restrictions
    )


def describable_configurations(model: Model) -> FrozenSet[str]:
    return frozenset(cfg for cfg in model.configurations if psi(model, cfg))


def active_union(model: Model) -> FrozenSet[str]:
    cfgs = describable_configurations(model)
    if not cfgs:
        return frozenset()
    return frozenset().union(*(model.act[cfg] for cfg in cfgs))


def check_axiom_v(model: Model) -> bool:
    return model.q_domain <= active_union(model) and set(model.q) == set(model.q_domain)


def admitted_channels(model: Model):
    result = set()
    for cfg in describable_configurations(model):
        for item in model.act[cfg] & model.q_domain:
            value = model.q[item]
            for role_cfg, role_item, quantity, role in model.roles:
                if role_cfg == cfg and role_item == item:
                    result.add((cfg, item, quantity, value, role))
    return frozenset(result)


def main() -> None:
    model = build_witness()
    print(f"Axiom I: {check_axiom_i(model)}")
    print(f"Axiom II: {check_axiom_ii(model)}")
    print(f"Axiom III: {check_axiom_iii(model)}")
    print(f"Axiom V: {check_axiom_v(model)}")
    print(f"Describable configurations: {sorted(describable_configurations(model))}")
    print(f"A*: {sorted(active_union(model))}")
    print(f"Channels: {sorted(admitted_channels(model))}")


if __name__ == "__main__":
    main()
