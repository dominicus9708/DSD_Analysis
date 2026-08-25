"""Finite witness for PHIL-003 Mary's Room.

Shows that a new epistemic record can appear without a new world-fact target.
This does not settle physicalism; it only checks the non-implication used in the DSD audit.
"""

facts_physical = {"f_red_other"}

pre_records = {
    "k_phys": "f_red_other",
}

post_records = {
    "k_phys": "f_red_other",
    "k_phen": "f_red_other",
}

new_records = set(post_records) - set(pre_records)
pre_targets = set(pre_records.values())
post_targets = set(post_records.values())
new_targets = post_targets - pre_targets

assert new_records == {"k_phen"}
assert new_targets == set()
assert post_targets <= facts_physical

print("new_records:", sorted(new_records))
print("new_targets:", sorted(new_targets))
print("new_record_without_new_target:", bool(new_records) and not bool(new_targets))
print("all_targets_physical:", post_targets <= facts_physical)
print("witness_passed: True")
