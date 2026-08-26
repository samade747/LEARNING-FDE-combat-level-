#!/usr/bin/env python3
"""Pre-commit-style guard for graph/claims.json: schema + append-only.

The book's own version uses a jq pre-commit hook; this machine had no jq
installed, so this is the portable Python equivalent, doing the same job:
required fields, unique ids, resolvable supersedes, and (given a previous
version to diff against) append-only enforcement.

Usage:
  python precommit_check.py graph/claims.json                    # schema only
  python precommit_check.py graph/claims.json --against old.json # + append-only check
"""
import json
import sys

REQUIRED_FIELDS = ["id", "subject", "predicate", "object", "source", "produced_by", "supersedes", "created"]


def load_claims(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    claims = data["claims"] if isinstance(data, dict) else data
    return {c["id"]: c for c in claims}


def check_schema(claims: dict) -> list[str]:
    errors = []
    for cid, c in claims.items():
        for field in REQUIRED_FIELDS:
            if field not in c:
                errors.append(f"{cid}: missing required field '{field}'")
        sup = c.get("supersedes")
        if sup and sup not in claims:
            errors.append(f"{cid}: supersedes '{sup}' does not resolve")
        source = c.get("source", {})
        if "kind" not in source:
            errors.append(f"{cid}: source.kind missing")
    return errors


def check_append_only(old_claims: dict, new_claims: dict) -> list[str]:
    errors = []
    for cid, old_c in old_claims.items():
        if cid not in new_claims:
            errors.append(f"APPEND-ONLY VIOLATION: '{cid}' existed before and is now DELETED")
        elif new_claims[cid] != old_c:
            errors.append(f"APPEND-ONLY VIOLATION: '{cid}' existed before and has been MUTATED (fields changed) - write a new claim with 'supersedes' instead")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) < 1:
        print("usage: python precommit_check.py <claims.json> [--against <old.json>]", file=sys.stderr)
        return 2

    new_path = argv[0]
    new_claims = load_claims(new_path)
    errors = check_schema(new_claims)

    if "--against" in argv:
        old_path = argv[argv.index("--against") + 1]
        old_claims = load_claims(old_path)
        errors.extend(check_append_only(old_claims, new_claims))

    print(f"Checked {len(new_claims)} claims in {new_path}.")
    if errors:
        print(f"\nBLOCKED - {len(errors)} issue(s):")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("OK to commit: schema holds, append-only holds (if checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
