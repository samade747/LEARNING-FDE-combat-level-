# Claude Certified Architect Foundations (CCA-F) — Track B Working Directory

Yeh **CCAR-F / PCAR-F Track B (Accelerated, 13-week)** course ka hands-on workspace hai. Notes
chapter alag hai ([`../docs/ccar-f-fde-track-b/`](../docs/ccar-f-fde-track-b/README.md)); yahan asal
coursework hota hai — weekly labs, 4 architect projects, aur FDE practicum (P1-P13).

## Structure

```
TRACK-B-WORKLOG.md              ← is course ki spine — kaunsi week done, kya decision, kya blocked
trade-off-notebook.md            ← graded artifact (7%) — har lab ke baad 3 sawal
week-01-foundations-sprint/       ← Week 1: entry verify + architecture decision framework  ✅
practicum/                        ← P1-P13: Vertical System of Record banana
  P1-thesis-and-setup.md            ← governed-knowledge thesis + 3 candidate verticals  ✅
stop_reason/                      ← Week 2 groundwork: Messages API stop_reason by hand
lib/sdk_parser/                   ← helper package (offline formatter + logger), Week 2 mein extend hoga
hello_world/                      ← smoke-test scripts
.claude/                          ← project-level Claude Code settings
```

## Status

| Item | Status |
| --- | --- |
| Week 1 — Foundations Sprint | ✅ done (2026-08-29) |
| P1 — Thesis + Setup | ✅ done (P2 = vertical choice, user input pending) |
| Week 2 — Agentic Loop by Hand | ⏭ next (`stop_reason/` partly started) |

Auth: **claude-agent-sdk** (bundled Claude Code CLI login) — koi `ANTHROPIC_API_KEY` nahi chahiye.
