# Cowork and OpenWork — Summary

90-Minute Crash Course, jin logon ka din documents/spreadsheets/email/meetings mein guzarta hai (lawyers,
accountants, marketers, HR, analysts, founders) unke liye — coding zaroori nahi. Core idea: yeh chatbot
nahi, **co-worker** hai jisay aap **assign** karte ho, sawal nahi poochte.

## 00 — Foundations

- **Concept 1 — Query vs Assignment:** "Ye PDF summarize karo" query hai; multi-step deliverable spec
  karna assignment hai. Chat mein worst case galat jawab (contained); yahan worst case confidently execute
  hui galat action (dazan files touch).
- **Concept 2 — Architecture 3 Pieces:** Desktop app (locally), Task loop (outcome → plan → approve →
  execute → approval before significant actions), Execution surface (local files, sandbox, connectors).
  Privacy farq: Cowork mein prompts+files Anthropic ko jate hain; OpenWork mein provider aap choose karte
  ho — files dono mein machine par rehti hain.
- **Concept 3 — Trust Model (Folders, Connectors, Approvals):** dedicated working folder banao (poori
  Documents nahi) — blast radius control. Connector = OAuth scope trust decision; **read scope ≠ send
  scope**. Approval modes: "Ask before acting" (default) vs "Act without asking"/stacked allow-always.
  **Deletions dono modes mein explicit permission maangti hain.** Table asymmetric hai jaan-boojh kar:
  reads automatic, writes/deletes/moves explicit click. Koi automatic version history nahi — backup aap
  par depend. Stop button turant halt karta hai. **Pehle 2 hafte approvals tight rakho.**
- **Pehla Real Task template (5 steps):** folder scope, explore-before-assigning, outcome framing, plan
  request+review, cautious approval mode jab content teesre banday ne likha ho.

## 01 — Context, Sessions, Aur Projects

- **Concept 4 — Plan Hi Leverage Hai:** discipline achhe prompts nahi, **intent-execution ke beech
  intercept karna** hai — har action ka pause point sabse sasta course-correction jagah hai. Check karo:
  scope, order, tools, assumptions. Galat plan ho to dobara shuru mat karo, one-sentence redirect do.
- **Concept 5 — Context Paisa Kharch Karta Hai:** har message context tokens cost karta hai. Poore folders
  unprompted context mein mat dumpo — pehle list karwao, phir zaroori files parhwao. Real example:
  340-doc matter folder — 2-prompt tareeqa (list+triage, phir sirf zaroori parho) → 12 files actually
  read, ~5% cost. Strong model thinking ke liye, economy model plumbing ke liye.
- **Concept 6 — Persistent Workspaces:** recurring kaam folder + context file (`CLAUDE.md`/`AGENTS.md`)
  mein rehna chahiye. Cowork: Projects (cross-session memory) + scheduled tasks. OpenWork: folder +
  AGENTS.md, khud re-fire. 2 failure modes: sab ek folder mein (context bleed), recurring kaam standalone
  sessions mein (missing context file symptom).

## 02 — Rules Aur Instructions

- **Concept 7 — Global/Folder/Session Instructions:** 3 layers, alag reach. Common ghalti: sab kuch
  global mein (3000-token system prompt har turn cost karta). **Rule: global sparse, folder specific,
  session goal.**
- **Concept 8 — "Poochho Pehle Execute Karne Se":** non-trivial tasks ke liye "1-2 clarifying questions
  poocho" instruction unstated assumptions surface karti hai. Multi-source tasks: "contradictions flag
  karo, chup chaap ek mat chuno" — warna model conflicts smooth kar deta hai (lawyer/auditor ke liye
  malpractice-level failure).

## 03 — Tool Extend Karna

- Decision tree: specific procedure → Skill; external service → Connector; role bundle → Plugin; richer
  surface → MCP server.
- **Concept 9 — Skills:** playbook folder (`SKILL.md` + optional scripts/references/assets). Dono tools
  same format use karte hain. `description` hi trigger field hai. 3 tareeqe: catalog, chat-generate
  (`/skill-creator`), manual author. Security warning: skills trusted code hain, sirf trusted sources se.
- **Concept 10 — Connectors:** Cowork broad catalog, OpenWork leaner. Asal power combinations mein hai
  (3 connectors ek task). Discipline: naya connector tab install karo jab specific workflow unlock ho —
  speculative install nayi prompt-injection vector kholta hai.
- **Concept 11 — Plugins:** lafz "plugin" **dono tools mein alag matlab** — Cowork plugin = role bundle
  (skills+connectors+commands+config); OpenCode plugin = npm package with event hooks. Interchangeable
  nahi. Real story: marketer ne 7 plugins install kiye → 43 overlapping options + ek chupka hua MCP server
  install ho gaya. Lesson: browser extensions ki tarah install karo, ek dafa mein ek, monthly audit.
- **Concept 12 — Subagents:** parallel work ke liye spawn hote hain — 20 contracts sequentially nahi, 4
  subagents parallel. 3 trigger patterns: Fan-out, Dimension, Compare. Mat use karo: sequential/dependent
  kaam, chhote batches (threshold ~5-7 items). Consistency rules main task description mein daalo, subagent
  prompts mein nahi.

## 04 — Safety Aur Autonomy Ladder

- **Regulated Data Warning:** Cowork standard plans PHI/FedRAMP/privileged-client data ke liye approved
  nahi (koi BAA). 3 checks: data residency, model provider BAA/DPA, logging/audit trail. "Local-first
  compliant nahi hai" — OpenWork files local hain lekin model calls provider ke pass jati hain.
- **Concept 13 — Autonomy Ladder (5 rungs):** Watching closely (default) → Ambient supervision → Walk
  away → Act without asking/allow-always → Scheduled (Cowork only). Deliberately chado, task type badalne
  par wapas neeche utro. Real story: HR recruiter ne candidate screening "walk away" par promote kiya,
  credential discrepancy miss hui — fix: wapas ambient supervision.
- **Concept 14 — Prompt Injection:** malicious content mein hidden instructions agent ko hijack karti
  hain. Defenses: untrusted-content tasks pe high-autonomy mat chalao, naye MCPs se ehtiyat, scope creep
  dekho to approve mat karo, drift ho to turant Stop karo. Real story: PDF ke white-on-white text mein
  exfiltration instruction — "Ask before acting" mode ne bacha liya.
- **Concept 15 — Scheduled Tasks:** Cowork built-in (`/schedule`); OpenWork manual re-fire. Rule: agar
  "walk away" mode mein trust nahi karte, schedule mat karo. Schedule kya kar sakte: bounded, supervised
  3x proven. Kya nahi: unreviewed messages, financial actions, sensitive files bina human-review, court
  filings bina nazar ke.

## 05 — Complete Worked Example: Weekly Industry Brief

- Recurring task jo dheere dheere autonomy ladder chadti hai. Cowork: Project banao → instructions likho →
  2x manual run → `/schedule` weekly → Monday review, feedback file karo. OpenWork: same but manual
  calendar-reminder re-fire (Step 7 sab ke liye same). Reusable shape: workspace + instructions + manual
  runs + trust-ke-baad-recur + feedback loop — har recurring workflow ka template.

## 06 — Where to Grow

- **Connector combinations** asal value hain — "aur phir main doosri tab kholta hoon" jumlay candidate
  hain. **Monthly audits** (10 min) — access review (folders/connectors/skills/plugins/scheduled).
- **Team scale:** Cowork owners private plugin marketplaces publish kar sakte; OpenWork shared repo se
  state distribute. Confidentiality: matter close hone par sessions delete karna (discoverable record ban
  sakta hai). Autonomy ladder **individual** hai — senior ka trust junior assume nahi karta.
- **Cross-model review** high-stakes outputs ke liye. **Portability dividend:** intercept pattern, subagents,
  autonomy discipline dono tools mein identical hain.

## 5 Sab Se Zaroori Baatein (README se)

1. Delegate karo, query mat karo
2. 3 trust levers: folders, connectors, approvals
3. Plan leverage hai, output nahi
4. Autonomy ladder deliberately chado
5. Untrusted content hamesha cautious mode maangta hai
