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
| P1 | Practicum — FDE/SoR Thesis + Setup | ✅ done (P2 blocked on vertical choice) | `practicum/P1-thesis-and-setup.md` |
| Week 2 | Architect — The Agentic Loop by Hand | ⏭ next | `stop_reason/` (partly started) |
| P2 | Practicum — Choose the Vertical | ⏭ next (needs user input) | — |

## Done

- 2026-08-29: Workspace set up. Auth verified (claude-agent-sdk).
- 2026-08-29: **Week 1 complete** — Hour 1 (`hour1_messages_api_demo.py` real run + `hour1-notes.md`:
  response fields explained, plan-vs-direct defense), Hour 2 (`hour2-concepts.md`: 4 architect
  distinctions), Hour 3 (`hour3-classification-lab.md`: 6 problems classified with enforcement +
  failure mode), trade-off notebook entry filled.
- 2026-08-29: **P1 complete** — thesis (governed knowledge vs chatbot, 4 reasons), 3 candidate
  verticals with screening notes, environment verified (Node 24.18 / pnpm 9.12 / uv 0.6).

## Open / Blocked

- **P2 needs user's personal-access input** — kaunsi vertical (3 candidates: PK tax/FBR compliance,
  SECP company compliance, AAOIFI Shariah-fintech rules). Sabse zyada wazan: kis domain mein real
  practitioners + real source docs tak access hai.
- Week 1 Hour 1 finding: claude-agent-sdk ke per-turn `AssistantMessage.stop_reason` `None` aata hai;
  sirf `ResultMessage` par populate hota hai. Week 2 mein iska asar dekhna hai.

## Readiness Targets (Week 13 decision)

- 80%+ on 2 full-length mocks
- 75%+ har domain
- Sab 4 architect projects complete
- Missed questions ka architectural principle explain kar sako
- Real exam: 720 scaled (alag threshold)
