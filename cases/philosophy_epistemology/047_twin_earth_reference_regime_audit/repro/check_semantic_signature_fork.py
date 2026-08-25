from __future__ import annotations


def main() -> None:
    earth = {
        "internal": ("clear", "odorless", "drinkable", "falls_as_rain"),
        "surface_form": "water",
        "environment_kind": "H2O",
    }

    twin = {
        "internal": ("clear", "odorless", "drinkable", "falls_as_rain"),
        "surface_form": "water",
        "environment_kind": "XYZ",
    }

    # Narrow/internal signature: only the selected internal and surface records matter.
    def narrow_record(record: dict[str, object]) -> tuple[object, object]:
        return (record["internal"], record["surface_form"])

    # Broad/reference signature: the environmental natural-kind relation is constitutive.
    def broad_reference(record: dict[str, object]) -> object:
        return record["environment_kind"]

    same_internal = earth["internal"] == twin["internal"]
    same_surface = earth["surface_form"] == twin["surface_form"]
    narrow_equal = narrow_record(earth) == narrow_record(twin)
    broad_reference_equal = broad_reference(earth) == broad_reference(twin)

    internal_projection_earth = (earth["internal"], earth["surface_form"])
    internal_projection_twin = (twin["internal"], twin["surface_form"])
    full_records_distinct = earth != twin
    projection_noninjective_witness = (
        internal_projection_earth == internal_projection_twin and full_records_distinct
    )

    witness_passed = (
        same_internal
        and same_surface
        and narrow_equal
        and not broad_reference_equal
        and projection_noninjective_witness
    )

    print(f"same_internal: {same_internal}")
    print(f"same_surface: {same_surface}")
    print(f"narrow_equal: {narrow_equal}")
    print(f"broad_reference_equal: {broad_reference_equal}")
    print(f"projection_noninjective_witness: {projection_noninjective_witness}")
    print(f"witness_passed: {witness_passed}")

    if not witness_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
