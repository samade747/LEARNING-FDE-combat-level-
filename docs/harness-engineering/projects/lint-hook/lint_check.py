"""Tiny dependency-free linter: flags any *.py line over 79 chars.

Usage: python lint_check.py [dir]   (defaults to current dir)
Exit 0 = clean. Exit 1 = violations found (printed to stdout).
"""
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
violations = []

for path in root.rglob("*.py"):
    if path.name == Path(__file__).name:
        continue
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if len(line) > 79:
            violations.append(f"{path}:{lineno}: line too long ({len(line)} > 79 chars)")

if violations:
    print("LINT FAILED:")
    for v in violations:
        print(f"  - {v}")
    sys.exit(1)

print("LINT OK: no lines over 79 chars.")
sys.exit(0)
