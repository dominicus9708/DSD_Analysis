from __future__ import annotations


def main() -> None:
    normal_world = {
        "world": "ordinary",
        "visual": "room",
        "auditory": "fan",
        "proprioception": "seated",
        "source_cue": "external_coherent",
    }

    biv_world = {
        "world": "vat",
        "visual": "room",
        "auditory": "fan",
        "proprioception": "seated",
        "source_cue": "generated_pipeline",
    }

    weak_channels = ("visual", "auditory", "proprioception")
    strong_channels = weak_channels + ("source_cue",)

    weak_projection_normal = tuple(normal_world[k] for k in weak_channels)
    weak_projection_biv = tuple(biv_world[k] for k in weak_channels)
    strong_projection_normal = tuple(normal_world[k] for k in strong_channels)
    strong_projection_biv = tuple(biv_world[k] for k in strong_channels)

    weak_indistinguishable = weak_projection_normal == weak_projection_biv
    worlds_different = normal_world["world"] != biv_world["world"]
    weak_projection_noninjective = weak_indistinguishable and worlds_different
    strong_indistinguishable = strong_projection_normal == strong_projection_biv
    added_discriminator_breaks_equivalence = weak_indistinguishable and not strong_indistinguishable

    surface_sentence = "I am a BIV"
    semantics = {
        "ordinary_english": {
            "surface": surface_sentence,
            "brain_ref": "ordinary_brain",
            "vat_ref": "ordinary_vat",
        },
        "vat_english": {
            "surface": surface_sentence,
            "brain_ref": "brain_in_image_or_program_correlate",
            "vat_ref": "vat_in_image_or_program_correlate",
        },
    }

    same_surface = (
        semantics["ordinary_english"]["surface"]
        == semantics["vat_english"]["surface"]
    )
    different_reference_regime = (
        semantics["ordinary_english"]["brain_ref"]
        != semantics["vat_english"]["brain_ref"]
        and semantics["ordinary_english"]["vat_ref"]
        != semantics["vat_english"]["vat_ref"]
    )

    witness_passed = (
        weak_projection_noninjective
        and added_discriminator_breaks_equivalence
        and same_surface
        and different_reference_regime
    )

    print(f"worlds_different: {worlds_different}")
    print(f"weak_indistinguishable: {weak_indistinguishable}")
    print(f"weak_projection_noninjective: {weak_projection_noninjective}")
    print(f"strong_indistinguishable: {strong_indistinguishable}")
    print(f"added_discriminator_breaks_equivalence: {added_discriminator_breaks_equivalence}")
    print(f"same_surface: {same_surface}")
    print(f"different_reference_regime: {different_reference_regime}")
    print(f"witness_passed: {witness_passed}")

    if not witness_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
