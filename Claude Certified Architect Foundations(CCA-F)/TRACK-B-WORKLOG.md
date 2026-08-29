# Track B Worklog — CCAR-F / PCAR-F (Accelerated, 13 weeks)

*Yeh is course ki apni spine hai (Loop Engineering ka pattern). Har session ke baad update: kaunsi
week/practicum-week done, kya artifact bana, kaunsa decision liya, kya blocked hai.*

Syllabus: [`../Claude Certified Architect Foundations (CCAR-F) FDE Track B Accelerated.md`](../Claude%20Certified%20Architect%20Foundations%20%28CCAR-F%29%20FDE%20Track%20B%20Accelerated.md)
Notes chapter: [`../docs/ccar-f-fde-track-b/`](../docs/ccar-f-fde-track-b/README.md)

## Setup Decisions (2026-08-29)

| Decision | Choice |
| --- | --- |
| Strands | **Dono saath** — har session architect week + practicum week dono aage badhte hain |
| API auth | **claude-agent-sdk** (bundled Claude Code CLI login) — alag `ANTHROPIC_API_KEY` nahi. Verified working 2026-08-29 (`AUTH_OK`, `stop_reason=end_turn`) |
| Practicum vertical | **P2 par decide** — P1 mein sirf 3 candidates evaluate honge |
| Environment | Python 3.13.2 · Node v24.18.0 · pnpm 9.12.3 · uv 0.6.0 · git 2.44.0 — sab entry baseline se ✅ |

## Progress

| Week | Strand | Status | Artifact |
| --- | --- | --- | --- |
| Week 1 | Architect — Foundations Sprint | ✅ done | `week-01-foundations-sprint/` |
| P1 | Practicum — FDE/SoR Thesis + Setup | ✅ done | `practicum/P1-thesis-and-setup.md` |
| Week 2 | Architect — The Agentic Loop by Hand | ✅ done | `week-02-agentic-loop-by-hand/` |
| P2 | Practicum — Choose the Vertical | 🟡 scored, blocked on user's vertical confirmation | `practicum/P2-choose-the-vertical.md` |
| Week 3 | Architect — Claude Agent SDK I | ⏭ next | — |
| P3 | Practicum — Design the Vertical SoR | ⏭ blocked on P2 | — |

## Done

- 2026-08-29: Workspace set up. Auth verified (claude-agent-sdk). `HOW-TO-RUN.md` operating guide.
- 2026-08-29: **Week 1 complete** — Hour 1 (`hour1_messages_api_demo.py` real run + notes), Hour 2
  (4 architect distinctions), Hour 3 (classification lab: 6 problems → type/enforcement/failure mode).
- 2026-08-29: **P1 complete** — governed-knowledge-vs-chatbot thesis, 3 candidate verticals, env verified.
- 2026-08-29: **Week 2 complete** — `concepts.md` (statelessness, content blocks, stop_reason table,
  tool round-trip, ceiling, parallel, tool_choice); `by_hand_loop.py` correct 2-tool loop (offline
  FakeClient, real run: 3 turns, parallel tools); **`lib/sdk_parser/stop_reason.py`** NEW — completes
  `stop_reason/plan.md` (`classify_stop_reason`/`is_tool_turn`/`text_is_final`/`next_step`);
  `test_week2.py` 6 tests pass; 5-bug diagnostic (`diagnostic-lab.md`, scaffold `pytest` 5 pass);
  `scenario-practice.md` 12 items; `homework.md`; 2 trade-off notebook entries.
- 2026-08-29: **P2 scored** — 5-criteria matrix, provisional recommendation **Vertical #1 (PK
  freelancer/software-house tax & FBR compliance)**. Source register template started.

## Open / Blocked

- **P2/P3 blocked on user** — vertical confirm karna hai (#1 recommended). Aur personal-access check:
  (a) 1 practitioner jisse verify kara sako, (b) 3+ real source docs. Yeh bina P3 ka
  scope/ownership/sources define nahi ho sakta.
- Week 1 finding (still relevant): claude-agent-sdk per-turn `AssistantMessage.stop_reason` = `None`;
  `classify_stop_reason(None)` → `"unknown"` + warning by design.

## Readiness Targets (Week 13 decision)

- 80%+ on 2 full-length mocks
- 75%+ har domain
- Sab 4 architect projects complete
- Missed questions ka architectural principle explain kar sako
- Real exam: 720 scaled (alag threshold)
