"""P11 scaffold: run the 3-class evaluation set against agent_under_test and
report pass/fail PER CLASS — a strong aggregate score can hide a weak class,
so the class-level breakdown is the point, not a single percentage.

Run: python eval_runner.py
"""

from __future__ import annotations

import json
import os
import sys

from agent_under_test import answer

HERE = os.path.dirname(os.path.abspath(__file__))


def check_case(case: dict) -> tuple[bool, str]:
    result = answer(case)

    if result["status"] != case["expect_status"]:
        return False, f"expected status={case['expect_status']}, got {result['status']}"

    if case["expect_status"] == "answered":
        if "expect_citation" in case and result.get("citation") != case["expect_citation"]:
            return False, f"expected citation={case['expect_citation']}, got {result.get('citation')}"
        if "expect_needs_approval" in case and result.get("needs_approval") != case["expect_needs_approval"]:
            return False, (
                f"expected needs_approval={case['expect_needs_approval']}, "
                f"got {result.get('needs_approval')}"
            )

    return True, "ok"


def main() -> int:
    with open(os.path.join(HERE, "eval_cases.json"), encoding="utf-8") as f:
        cases = json.load(f)

    by_class: dict[str, list[tuple[str, bool, str]]] = {}
    for case in cases:
        ok, detail = check_case(case)
        by_class.setdefault(case["class"], []).append((case["id"], ok, detail))

    all_ok = True
    print("Per-class results:")
    for cls, results in by_class.items():
        passed = sum(1 for _, ok, _ in results if ok)
        total = len(results)
        status = "PASS" if passed == total else "FAIL"
        if passed != total:
            all_ok = False
        print(f"  [{status}] {cls}: {passed}/{total}")
        for case_id, ok, detail in results:
            if not ok:
                print(f"      - {case_id}: {detail}")

    print()
    if all_ok:
        print("All classes pass.")
        return 0
    print("FAILED: at least one class has a failing case (see above).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
