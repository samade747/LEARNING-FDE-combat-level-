"""Drill 2 — Block on purpose. PreToolUse hook, matcher "Bash".

Blocks any Bash command containing "curl", exit 2 (blocking) with a message
naming the allowed alternative. Everything else passes through, exit 0.
"""
import json
import sys

try:
    data = json.load(sys.stdin)
except Exception:
    data = {}

command = data.get("tool_input", {}).get("command", "")

if "curl" in command:
    print(
        "BLOCKED: curl is not allowed in this harness. "
        "Use the project's fetch_record()/connector functions instead — "
        "see error-audit/connector_after.py for the pattern.",
        file=sys.stderr,
    )
    sys.exit(2)

sys.exit(0)
