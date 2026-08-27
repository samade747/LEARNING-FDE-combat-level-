"""Corpus-to-Site Skeleton — structural validator.

Confirms the fixture follows docs/ksor/02-architecture-and-tooling.md's project-structure
convention (knowledge/, instance.md) and that every knowledge file carries the governance
frontmatter fields docs/ksor/03-governance-and-ai-native-role.md requires for authority content
(stable_id, owner, version, authority_class).

Run: python validate_corpus.py
"""
from __future__ import annotations

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
REQUIRED_FIELDS = ["stable_id", "owner", "version", "authority_class"]


def parse_frontmatter(path: str) -> dict:
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    assert m, f"{path}: no YAML frontmatter block found"
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fm[key.strip()] = value.strip()
    return fm


def main() -> int:
    errors: list[str] = []

    if not os.path.isfile(os.path.join(ROOT, "instance.md")):
        errors.append("instance.md missing at project root")

    knowledge_dir = os.path.join(ROOT, "knowledge")
    if not os.path.isdir(knowledge_dir):
        errors.append("knowledge/ directory missing")
        print("FAILED:\n  - " + "\n  - ".join(errors))
        return 1

    md_files = sorted(glob.glob(os.path.join(knowledge_dir, "**", "*.md"), recursive=True))
    if not md_files:
        errors.append("knowledge/ has no .md files")

    seen_stable_ids: set[str] = set()
    for path in md_files:
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        fm = parse_frontmatter(path)
        for field in REQUIRED_FIELDS:
            if field not in fm or not fm[field]:
                errors.append(f"{rel}: missing required frontmatter field '{field}'")
        stable_id = fm.get("stable_id")
        if stable_id:
            if stable_id in seen_stable_ids:
                errors.append(f"{rel}: duplicate stable_id '{stable_id}'")
            seen_stable_ids.add(stable_id)
        authority_class = fm.get("authority_class")
        if authority_class not in {"authority", "orientation"}:
            errors.append(
                f"{rel}: authority_class must be 'authority' or 'orientation', got {authority_class!r}"
            )

    if errors:
        print("FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"All checks passed: instance.md present, {len(md_files)} knowledge files, "
          f"all carry stable_id/owner/version/authority_class, no duplicate stable_ids.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
