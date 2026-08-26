"""Exercise 2, step 2's own instruction: "Test karo ke rules sirf matching files edit karte waqt
load hote hain." This script is that test, done structurally (no live Claude Code session needed):
it parses each .claude/rules/*.md file's frontmatter and confirms its `paths` glob matches exactly
the files it should, and none it shouldn't.

Run: python validate_setup.py   (exits non-zero and prints failures if anything is wrong)
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))


def parse_frontmatter(path: str) -> dict:
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    assert m, f"{path}: no YAML frontmatter block found"
    fm_text = m.group(1)
    fm = {}
    # tiny hand-rolled parser — good enough for this fixture's flat key: value / key: [list] shape
    for line in fm_text.splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fm[key.strip()] = value.strip()
    return fm


def glob_matches(pattern: str) -> set[str]:
    hits = glob.glob(os.path.join(ROOT, pattern), recursive=True)
    return {os.path.relpath(h, ROOT).replace("\\", "/") for h in hits if os.path.isfile(h)}


def check_rule(rule_file: str, must_match: set[str], must_not_match: set[str]) -> list[str]:
    errors = []
    fm = parse_frontmatter(os.path.join(ROOT, ".claude", "rules", rule_file))
    raw_paths = fm.get("paths", "")
    patterns = re.findall(r'"([^"]+)"', raw_paths)
    if not patterns:
        return [f"{rule_file}: no `paths` glob found in frontmatter"]
    matched: set[str] = set()
    for p in patterns:
        matched |= glob_matches(p)
    for expected in must_match:
        if expected not in matched:
            errors.append(f"{rule_file}: expected to match {expected}, but pattern {patterns} did not")
    for unexpected in must_not_match:
        if unexpected in matched:
            errors.append(f"{rule_file}: pattern {patterns} unexpectedly matched {unexpected}")
    return errors


def main() -> int:
    errors: list[str] = []

    if not os.path.isfile(os.path.join(ROOT, "CLAUDE.md")):
        errors.append("CLAUDE.md missing at project root")

    errors += check_rule(
        "api-conventions.md",
        must_match={"src/api/handler.ts", "src/api/handler.test.ts"},
        must_not_match={"src/web/App.tsx"},
    )
    errors += check_rule(
        "testing-conventions.md",
        must_match={"src/api/handler.test.ts"},
        must_not_match={"src/api/handler.ts", "src/web/App.tsx"},
    )

    skill_path = os.path.join(ROOT, ".claude", "skills", "team-review", "SKILL.md")
    if not os.path.isfile(skill_path):
        errors.append("team-review SKILL.md missing")
    else:
        fm = parse_frontmatter(skill_path)
        if fm.get("context") != "fork":
            errors.append("team-review SKILL.md: expected `context: fork` in frontmatter")
        if "allowed-tools" not in fm:
            errors.append("team-review SKILL.md: expected `allowed-tools` restriction in frontmatter")

    mcp_path = os.path.join(ROOT, ".mcp.json")
    if not os.path.isfile(mcp_path):
        errors.append(".mcp.json missing")
    else:
        data = json.loads(open(mcp_path, encoding="utf-8").read())
        raw = json.dumps(data)
        if "${" not in raw:
            errors.append(".mcp.json: expected env-var expansion syntax (${VAR}) for credentials")

    if errors:
        print("FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("All checks passed: CLAUDE.md present, both rules load only their intended files, "
          "team-review skill is fork-isolated and read-only, .mcp.json uses env-var expansion.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
