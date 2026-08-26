#!/usr/bin/env python3
"""Validate one extraction result against entity_schema.json's shape, and
(when given multiple files) report entity names that look like the same
real thing under different surface forms.

Usage:
  python validate_extraction.py extracted-doc1.json                 # validate one file
  python validate_extraction.py extracted-doc1.json extracted-doc2.json extracted-doc3.json
                                                                       # validate all + find surface-form overlap
"""
import json
import sys

ENTITY_TYPES = {"Organization", "Person", "Component", "Incident", "Contract"}


def validate_one(path: str) -> tuple[list[str], set[str]]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    errors = []
    names = set()

    if "entities" not in data or "relations" not in data:
        errors.append(f"{path}: missing top-level 'entities' or 'relations' key")
        return errors, names

    for i, e in enumerate(data["entities"]):
        where = f"{path}: entities[{i}]"
        for field in ("name", "type", "description"):
            if field not in e:
                errors.append(f"{where}: missing '{field}'")
        if e.get("type") not in ENTITY_TYPES:
            errors.append(f"{where}: type '{e.get('type')}' not in {sorted(ENTITY_TYPES)}")
        if e.get("name"):
            names.add(e["name"])

    for i, r in enumerate(data["relations"]):
        where = f"{path}: relations[{i}]"
        for field in ("subject", "predicate", "object"):
            if field not in r:
                errors.append(f"{where}: missing '{field}'")
        if r.get("subject") and r["subject"] not in names:
            errors.append(f"{where}: subject '{r['subject']}' is not a declared entity in this document")
        if r.get("object") and r["object"] not in names:
            errors.append(f"{where}: object '{r['object']}' is not a declared entity in this document")

    return errors, names


def main(paths: list[str]) -> int:
    all_errors = []
    all_names = []

    for p in paths:
        errors, names = validate_one(p)
        all_errors.extend(errors)
        all_names.append((p, names))
        status = "INVALID" if errors else "schema-valid"
        print(f"{p}: {status} ({len(names)} entities)")

    if all_errors:
        print(f"\n{len(all_errors)} SCHEMA VIOLATION(S):")
        for e in all_errors:
            print(f"  - {e}")

    if len(paths) > 1:
        # Cheap surface-form overlap hint: names that share a token (case-insensitive)
        # across different files, but aren't identical strings.
        print("\nPossible same-entity-different-name candidates across files (eyeball these):")
        flat = [(p, n) for p, names in all_names for n in names]
        seen_pairs = set()
        for p1, n1 in flat:
            for p2, n2 in flat:
                if p1 >= p2 or n1 == n2:
                    continue
                t1, t2 = set(n1.lower().split()), set(n2.lower().split())
                if t1 & t2 and (n1, n2) not in seen_pairs and (n2, n1) not in seen_pairs:
                    seen_pairs.add((n1, n2))
                    print(f"  - '{n1}' ({p1}) <-> '{n2}' ({p2})")
        if not seen_pairs:
            print("  (none found by the cheap token-overlap heuristic - inspect manually too)")

    return 1 if all_errors else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python validate_extraction.py <file.json> [file2.json ...]", file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
