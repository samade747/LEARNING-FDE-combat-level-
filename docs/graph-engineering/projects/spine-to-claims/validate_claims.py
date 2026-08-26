#!/usr/bin/env python3
"""Validate a claims.json against the Part 6 schema invariants.

Usage: python validate_claims.py claims.json
Exit 0 = all claims valid. Exit 1 = at least one invariant violated.
"""
import json
import sys

REQUIRED_FIELDS = ["id", "subject", "predicate", "object", "source", "produced_by", "created"]


def validate(path: str) -> int:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    claims = data["claims"] if isinstance(data, dict) else data
    errors = []
    seen_ids = set()
    inference_count = 0

    for i, claim in enumerate(claims):
        where = f"claims[{i}] (id={claim.get('id', '?')})"

        for field in REQUIRED_FIELDS:
            if field not in claim:
                errors.append(f"{where}: missing required field '{field}'")

        if "supersedes" not in claim:
            errors.append(f"{where}: missing 'supersedes' field (use null if none)")

        cid = claim.get("id")
        if cid in seen_ids:
            errors.append(f"{where}: duplicate id '{cid}'")
        seen_ids.add(cid)

        source = claim.get("source", {})
        kind = source.get("kind")
        if kind is None:
            errors.append(f"{where}: source.kind missing")
        elif kind == "inference":
            inference_count += 1
        elif kind in ("tool_output", "document"):
            if "ref" not in source and "command" not in source:
                errors.append(f"{where}: source.kind='{kind}' but no 'ref' or 'command' given")
        else:
            errors.append(f"{where}: unknown source.kind '{kind}' (expected tool_output/document/inference)")

    for i, claim in enumerate(claims):
        sup = claim.get("supersedes")
        if sup and sup not in seen_ids:
            errors.append(f"claims[{i}] (id={claim.get('id')}): supersedes '{sup}' does not resolve to any claim in this file")

    total = len(claims)
    print(f"Checked {total} claims. Inference-sourced: {inference_count}/{total}.")

    if errors:
        print(f"\n{len(errors)} INVARIANT VIOLATION(S):")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("All invariants hold: every claim has a source (or honest inference mark), no duplicate ids, all supersedes resolve.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python validate_claims.py <claims.json>", file=sys.stderr)
        sys.exit(2)
    sys.exit(validate(sys.argv[1]))
