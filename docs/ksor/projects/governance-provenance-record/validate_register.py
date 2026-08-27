"""Governance/Provenance Record — validator.

docs/ksor/03-governance-and-ai-native-role.md's Governance Model pipeline is
Source -> Draft -> Review -> Approved -> Authoritative KSoR. This script enforces the one rule
that pipeline implies structurally: an entry marked "approved" must carry full governance
metadata (owner, effective_period, source_commit) before it is citable, and an entry still in
"draft" must never be treated as citable — no matter how complete its authority_class looks.

source_register.json's 4th entry (draft-loyalty-policy-001) is a deliberate bad example: it is
authority_class "authority" but review_state "draft", with empty owner/effective_period/
source_commit — exactly the shape a rushed team ships when they promote a draft policy without
finishing the approval trail. This script must catch it.

Run: python validate_register.py
"""
from __future__ import annotations

import json
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
REGISTER_PATH = os.path.join(ROOT, "source_register.json")
REQUIRED_WHEN_APPROVED = ["owner", "effective_period", "source_commit"]


def load_sources() -> list[dict]:
    with open(REGISTER_PATH, encoding="utf-8") as f:
        return json.load(f)["sources"]


def citable_sources(sources: list[dict]) -> list[dict]:
    """Only 'approved' entries are citable — draft/review entries are excluded, no exceptions."""
    return [s for s in sources if s.get("review_state") == "approved"]


def main() -> int:
    sources = load_sources()
    errors: list[str] = []

    seen_ids: set[str] = set()
    for s in sources:
        sid = s.get("stable_id", "<missing stable_id>")
        if sid in seen_ids:
            errors.append(f"{sid}: duplicate stable_id in register")
        seen_ids.add(sid)

        if s.get("review_state") == "approved":
            for field in REQUIRED_WHEN_APPROVED:
                if not s.get(field):
                    errors.append(f"{sid}: review_state=approved but '{field}' is empty")

    citable = citable_sources(sources)
    citable_ids = {s["stable_id"] for s in citable}
    if "draft-loyalty-policy-001" in citable_ids:
        errors.append("draft-loyalty-policy-001 leaked into citable_sources() despite review_state=draft")

    draft_entries = [s for s in sources if s.get("review_state") == "draft"]
    if not draft_entries:
        errors.append("expected at least one draft entry in the fixture to prove the exclusion works")

    if errors:
        print("FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"All checks passed: {len(sources)} register entries, no duplicate stable_ids, "
          f"{len(citable)} citable (approved), {len(draft_entries)} draft correctly excluded "
          f"from citable_sources().")
    return 0


if __name__ == "__main__":
    sys.exit(main())
