# Week 2 — The Agentic Loop by Hand

*Required course: **The Loop by Hand**. Exam mapping: **Task 1.1**; `tool_choice` in Tasks 2.3, 4.3.
Domain 1 (Agentic Architecture & Orchestration, 27%).*

## 3-hour rhythm

| Hour | File | Status |
| --- | --- | --- |
| 1 — Concepts | [`concepts.md`](concepts.md) | ✅ |
| 2 — Guided lab | [`by_hand_loop.py`](by_hand_loop.py) (correct 2-tool loop) + [`diagnostic-lab.md`](diagnostic-lab.md) (5-bug diagnosis) | ✅ |
| 3 — Scenario practice | [`scenario-practice.md`](scenario-practice.md) (12 items) | ✅ |
| Homework | [`homework.md`](homework.md) — "what does the Agent SDK now do for you" | ✅ |

## What got built

- **`by_hand_loop.py`** — reference-correct two-tool agentic loop, **no framework**. Offline
  `FakeClient` (Track B auth = claude-agent-sdk, no raw key). Demonstrates: per-turn history
  management, parallel tool_use in one turn, the `tool_use → tool_result` round-trip keyed by
  `tool_use_id`, `stop_reason` branching, and a hard `MAX_TURNS` ceiling.
- **`lib/sdk_parser/stop_reason.py`** (NEW — completes `stop_reason/plan.md`) — `classify_stop_reason()`,
  `is_tool_turn()`, `text_is_final()`, `next_step()`. Maps the protocol signal to a loop decision so
  the loop never has to guess from content shape.
- **`test_week2.py`** — 6 offline tests (classifier + loop). ✅ pass.

## Project 1 (required architect project) — the 5-bug diagnostic

Scaffold: [`../../docs/certifications/ccar-f/projects/00-agentic-loop-no-framework/`](../../docs/certifications/ccar-f/projects/00-agentic-loop-no-framework/README.md)

```bash
python -m pytest docs/certifications/ccar-f/projects/00-agentic-loop-no-framework/test_loop.py -q
# 5 passed
```

Diagnosis writeup: [`diagnostic-lab.md`](diagnostic-lab.md).

## Done jab

- [x] Concepts: statelessness, content blocks, stop_reason table, tool round-trip, ceiling, parallel, tool_choice
- [x] Correct by-hand loop runs (real offline run, 3 turns, parallel tools)
- [x] `stop_reason/plan.md` deliverable done — `sdk_parser` extended + tested
- [x] 5-bug diagnostic: each bug named from its symptom, `pytest` green
- [x] Scenario practice: 12 items with rationale
- [x] Homework answered
- [x] Trade-off notebook entry

**Next:** Week 3 (Claude Agent SDK I — tools, permissions, MCP) + P3 (Design the Vertical SoR).
