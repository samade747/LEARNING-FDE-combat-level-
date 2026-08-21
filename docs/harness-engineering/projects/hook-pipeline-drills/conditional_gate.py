"""Drill 3 — The conditional gate. Stop hook.

Only runs the (slow, imaginary) test suite when source files changed in
this beat. Untouched beats exit 0 immediately — slow checks that only run
when they matter are what keeps a harness fast enough to keep using.
"""
import subprocess
import sys

try:
    changed = subprocess.run(
        ["git", "diff", "--name-only", "HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.splitlines()
except Exception:
    changed = []

source_changed = any(f.endswith(".py") for f in changed)

if not source_changed:
    print("No source files changed this beat — skipping test suite.")
    sys.exit(0)

print(f"Source files changed ({len(changed)} files) — running test suite...")
result = subprocess.run([sys.executable, "-m", "pytest", "-q"])
if result.returncode != 0:
    print("BLOCKED: tests failed, cannot stop until they pass.", file=sys.stderr)
    sys.exit(2)

sys.exit(0)
