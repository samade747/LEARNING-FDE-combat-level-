# Harness Appendix — 3 Hook Pipeline Drills

From [`08-appendix-hook-pipeline.md`](../../08-appendix-hook-pipeline.md). Three real, tested hook
scripts, wired in `.claude/settings.json`:

| Drill | Hook event | Script | Behavior |
| --- | --- | --- | --- |
| 1. See the stream | `PreToolUse`, matcher `*` | `trace_log.py` | Never blocks — appends one line per tool call to `trace.log` |
| 2. Block on purpose | `PreToolUse`, matcher `Bash` | `block_curl.py` | Blocks (exit 2) any Bash command containing `curl`, names the alternative |
| 3. The conditional gate | `Stop` | `conditional_gate.py` | Skips the test suite entirely if no `.py` files changed this beat; runs and gates on it if they did |

**Tested directly (no Claude Code needed) — confirmed working:**

```bash
echo '{"tool_name":"Bash","tool_input":{"command":"ls -la"}}' | python trace_log.py
# -> exit 0, one line appended to trace.log

echo '{"tool_name":"Bash","tool_input":{"command":"curl http://example.com"}}' | python block_curl.py
# -> exit 2, "BLOCKED: curl is not allowed..."

echo '{"tool_name":"Bash","tool_input":{"command":"ls -la"}}' | python block_curl.py
# -> exit 0, passes through
```

## Setup (inside Claude Code)

```bash
cp -r docs/harness-engineering/projects/hook-pipeline-drills /path/outside/this/repo/hook-drills
cd /path/outside/this/repo/hook-drills
git init && git add -A && git commit -m "start"
claude
```

## Steps

1. Run a normal beat (any prompt that uses a few tools). Read `trace.log` — most people are
   surprised how many actions one "simple" request took.
2. Ask the agent to `fetch https://example.com using curl`. Watch it get blocked, told the
   alternative, and redirected.
3. Add a `.py` file, then try to stop — the conditional gate should run pytest and gate on it. Then
   make an edit that touches no `.py` file (e.g. a markdown file) and stop again — gate should skip
   instantly.

## Done jab (self-check)

- [ ] Drill 1: ek beat ke sab tool calls `trace.log` mein dikhein
- [ ] Drill 2: `curl` command block hui (exit 2), error ne alternative bataya
- [ ] Drill 3: gate sirf `.py`-change beats par pytest chalati hai, doosre beats par turant skip

---
[⬆ Harness Practice Log](../../11-practice-log.md) · [Appendix Full Detail](../../08-appendix-hook-pipeline.md)
