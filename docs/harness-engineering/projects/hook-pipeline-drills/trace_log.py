"""Drill 1 — See the stream. PreToolUse hook, matcher "*".

Appends one line per tool call to trace.log. Never blocks (always exit 0) —
this hook is pure observability, not a gate.
"""
import json
import sys
from datetime import datetime, timezone

try:
    data = json.load(sys.stdin)
except Exception:
    data = {}

tool_name = data.get("tool_name", "unknown")
tool_input = data.get("tool_input", {})
summary = str(tool_input)[:120]

with open("trace.log", "a", encoding="utf-8") as f:
    f.write(f"{datetime.now(timezone.utc).isoformat()} | {tool_name} | {summary}\n")

sys.exit(0)
