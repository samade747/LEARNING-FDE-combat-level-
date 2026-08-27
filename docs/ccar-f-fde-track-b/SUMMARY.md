# Summary — CCAR-F FDE Track B (Accelerated)

Root file [`Claude Certified Architect Foundations (CCAR-F) FDE Track B Accelerated.md`](../../Claude%20Certified%20Architect%20Foundations%20%28CCAR-F%29%20FDE%20Track%20B%20Accelerated.md)
ka structured chapter — Panaversity ka 13-week accelerated syllabus, do strands mein: Architect
(CCAR-F exam prep) + FDE Practicum (Vertical System of Record banana).

**Kya hai:** Track B = accelerated version (Track A se tez, zyada demanding). 4.5 hrs/week instructor-
led + 5-7 hrs guided practice, ~120-150 hrs total quarter mein.

**Architect strand (70% grade):** Week 1 foundations sprint, phir Weeks 2-11 CCAR-F blueprint ke 5
domains cover karti hain (Agentic Loop by hand → Agent SDK tools/multi-agent/hooks → Claude Code
architecture/Teams/CI → Structured output → Context/reliability) — 4 required projects isi mein bante
hain. Week 12-13: 6-scenario workshop + 2 full mocks + readiness decision.

**FDE Practicum (30% grade):** P1-P13, ek governed Vertical SoR banata hai — human projection
(Fumadocs site) + agent projection (stateless MCP server) same governed corpus se. 4 milestones: live
human surface (P5), working agent surface (P8), governed KSoR + evaluation (P11), capstone (P13).

**Is repo mein scaffold hua:** sab 4 practicum milestones ke local-runnable scaffolds
(`projects/p4-p5-fumadocs-corpus-to-site/`, `projects/p6-p7-stateless-mcp/`, `projects/p8-agent-
surface/`, `projects/p11-proving-behaviour/`) — koi live deployment nahi, sab localhost par chalte
hain. 4 required architect projects `docs/certifications/ccar-f/projects/` mein scaffold hote hain
(is chapter se cross-referenced, duplicate nahi).

**Sourcing note:** yeh syllabus khud Panaversity ka document hai (book se bahar), lekin is chapter ke
andar jo Claude/Anthropic technical facts likhi gayin (stateless MCP), unhe book se cross-check kiya
gaya — `context-layer-crash-course` stateless-core ko confirm karti hai, MRTR ke exact field-mechanics
book mein nahi hain (syllabus/MCP-spec apna source hai, honestly note kiya).

**Quiz:** 12 self-authored scenario questions (`quiz.md`), harness-engineering format follow karte hue.

---
[⬆ Index](README.md)
