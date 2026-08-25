from __future__ import annotations

import hashlib
import json
from pathlib import Path

EXPECTED_SHA256 = "50af7900f8d4d259a55604097e4774650c7ca1342c4b598a0d9a97559d21f0c4"

SEALED_DEFECT_PREDICTIONS = {
    "S-001": False,
    "S-002": True,
    "S-003": True,
    "S-004": False,
    "S-005": False,
    "S-006": True,
    "S-007": True,
    "S-008": True,
}


def main() -> None:
    case_dir = Path(__file__).resolve().parents[1]
    truth_path = case_dir / "GROUND_TRUTH.json"
    raw = truth_path.read_bytes()
    actual_sha = hashlib.sha256(raw).hexdigest()

    print("ground_truth_sha256:", actual_sha)
    print("commitment_matches:", actual_sha == EXPECTED_SHA256)
    assert actual_sha == EXPECTED_SHA256, "Ground truth does not match pre-seal commitment"

    truth = json.loads(raw.decode("utf-8"))
    counts = {"TP": 0, "TN": 0, "FP": 0, "FN": 0}

    for item in truth["cases"]:
        cid = item["case"]
        actual = bool(item["defect"])
        predicted = SEALED_DEFECT_PREDICTIONS[cid]

        if predicted and actual:
            result = "TP"
        elif not predicted and not actual:
            result = "TN"
        elif predicted and not actual:
            result = "FP"
        else:
            result = "FN"

        counts[result] += 1
        print(f"{cid}: actual_defect={actual} predicted_defect={predicted} result={result}")

    print("counts:", counts)
    print("total:", sum(counts.values()))

    assert counts == {"TP": 5, "TN": 3, "FP": 0, "FN": 0}
    assert sum(counts.values()) == 8
    print("verification_passed: True")


if __name__ == "__main__":
    main()
