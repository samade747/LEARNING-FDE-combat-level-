# CCAR-F Track B — Required Project 1: Agentic Loop, No Framework

*Root syllabus [`Claude Certified Architect Foundations (CCAR-F) FDE Track B Accelerated.md`](../../../../../Claude%20Certified%20Architect%20Foundations%20%28CCAR-F%29%20FDE%20Track%20B%20Accelerated.md), "Four Required Architect Projects" table, **Project 1** (Track B Week 2): "build a two-tool agentic loop with no agent framework. The instructor introduces missing history, a lost tool result, incorrect stop handling, repeated tool calls, and premature termination. Students diagnose each failure from its symptoms." This is also the loop-control foundation the guide's own Exercise 1 assumes. Domain: 1 (Agentic Architecture & Orchestration).*

Five isolated, hand-rolled agentic loops (raw Messages API shape — no SDK), each identical to the
correct version except for **one deliberately injected bug**. A diagnostic exercise: run the tests,
read the symptom each one exposes, then compare against `fixed_loop.py`'s single correct
implementation to see exactly what line fixes it.

## Files

- `broken_loop.py` — 5 functions, `loop_bug1_missing_history` through `loop_bug5_premature_termination`,
  each with one bug marked by a `# missing:` or inline comment at the exact broken line.
- `fixed_loop.py` — `agent_loop`, the reference implementation with all five bugs corrected, each fix
  commented against the bug number it resolves.
- `test_loop.py` — 5 offline pytest tests (`FakeClient`, no API key, no network). Each test runs the
  *same* scenario against the broken function and the fixed one, and asserts the specific,
  observable symptom (a missing history entry, a dropped tool call, a runaway call count, ...).

## Kaise Chalayein

```bash
pip install pytest
pytest test_loop.py -v
```

All 5 tests should pass — they are not testing "does the bug exist" (it does, by construction), they
are testing "does the diagnostic assertion correctly distinguish broken from fixed behavior."

## The 5 Bugs, In One Line Each

| # | Bug | Symptom | Fix |
| --- | --- | --- | --- |
| 1 | Missing history | 2nd API call has no "assistant" turn — model re-answers half-blind | Always `messages.append({"role": "assistant", ...})` |
| 2 | Lost tool result | Tool runs, result computed, never sent back — model never learns it happened | Always append a "user" message with the `tool_result` block |
| 3 | Incorrect stop handling | Stops on "any text present" instead of `stop_reason == "end_turn"` — a pending tool call gets silently dropped | Check `response.stop_reason`, never content shape |
| 4 | Repeated tool calls | No turn ceiling — a stuck model calls forever | A hard `MAX_TURNS` loop bound, with a clean error on exhaustion |
| 5 | Premature termination | Only `tool_use_blocks[0]` executed in a multi-tool turn | Loop over *every* `tool_use` block in the turn |

## Done Jab (Self-Check)

- [ ] `pytest test_loop.py -v` — all 5 pass
- [ ] Aap har bug ko symptom se pehchan sakte ho bina code dekhe (jaise "loop kabhi khatam nahi hota"
      → Bug 4, "half ka jawab mila, tool call ho hi nahi paya" → Bug 3)
- [ ] `fixed_loop.py` aur `broken_loop.py` ka diff parh liya — har fix ek single, precise line hai,
      koi restructure nahi

---
[⬅ CCAR-F Projects Index](../README.md)
