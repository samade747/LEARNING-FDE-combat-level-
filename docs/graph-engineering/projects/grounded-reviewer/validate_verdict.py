#!/usr/bin/env python3
"""Check a reviewer verdict is actually GROUNDED, not just shaped right.

A verdict can be valid JSON and still be a lie: it can cite a claim id that
doesn't exist, or cite only inference-sourced claims (an inference cannot
ground anything on its own — Concept 8). This checks both, not just the shape.

Usage: python validate_verdict.py verdict.json
Exit 0 = grounded. Exit 1 = protocol break -> route to a human.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent


def main(path: str) -> int:
    with open(path, encoding="utf-8") as f:
        verdict = json.load(f)
    with open(HERE / "claims.json", encoding="utf-8") as f:
        claims = {c["id"]: c for c in json.load(f)["claims"]}

    errors = []

    decision = verdict.get("decision")
    if decision not in ("PASS", "REVISE", "FAIL"):
        errors.append(f"decision '{decision}' is not one of PASS/REVISE/FAIL -> route to a human")

    if not verdict.get("reason"):
        errors.append("missing 'reason'")

    if decision == "PASS":
        grounded_in = verdict.get("grounded_in")
        if not grounded_in:
            errors.append("decision=PASS but 'grounded_in' is missing or empty -> this is an impression, not an audit")
        else:
            for cid in grounded_in:
                if cid not in claims:
                    errors.append(f"grounded_in cites '{cid}', which does not exist in claims.json -> fabricated citation")
                elif claims[cid]["source"]["kind"] == "inference":
                    errors.append(f"grounded_in cites '{cid}', which is source.kind='inference' -> an inference cannot ground a PASS on its own")
    elif decision in ("REVISE", "FAIL"):
        if not verdict.get("required_evidence"):
            errors.append(f"decision={decision} but 'required_evidence' is missing or empty -> this is a mood ('seems off'), not a work order")

    if errors:
        print(f"NOT GROUNDED ({len(errors)} issue(s)) -> route to NEEDS_HUMAN:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"GROUNDED: decision={decision}, every cited claim resolves and is not inference-only.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python validate_verdict.py <verdict.json>", file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
