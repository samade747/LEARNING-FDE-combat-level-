# Designing Agent Experiences — Summary

18 Concepts, 4 Parts. Yeh us **patli, decisive layer** ke baare mein hai jahan insan agent se milta hai
aur decide karta hai trust karna hai ya nahi. **Thesis:** ek agentic product ke ek waqt mein 2 users hote
hain (insan jise trust karna hai, aur agents jinhe parse karna hai) — surface dono ki khidmat kare bina
kisi ko dhoka diye.

## 00 — The Shift (Concepts 1-3)

- **Concept 1 — Teesra Paradigm:** Batch → Command (drive karte the) → Agentic (outcome state karo, agent
  steps choose karta hai). "Kaise" ka bojh insan se machine ki taraf shift. 3 nayi design cheezein: **intent,
  trust, recovery.**
- **Concept 2 — 2 Audiences:** insan (Agentic Experience, John Maeda — Human surface) aur agent (Agent
  Experience, Matt Biilmann — Machine surface). Zyada tar courses sirf pehla sikhate hain, yeh course dono.
- **Concept 3 — Interface Gayab Nahi, Move Hota Hai:** har autonomous agent 3 naye interfaces banata hai —
  Configuration, Monitoring, Intervention. "Task ko widget mein translate karo" se "intent ka system shape
  karo" ki taraf shift.

## 01 — Human Surface — Trust Ke Liye Design (Concepts 4-12)

- **Concept 4 — Trust Kamaya Jata Hai:** Trust = Reliability × Transparency × Control × Mistakes (undo)
  — product hai, sum nahi (ek zero to poora zero). Pehla move: agent ko visibly uncertain hone do. Ulti
  galti: over-trust (100 baar sahi ho to check karna band).
- **Concept 5 — Pehla Contact:** expectations reset per jump, stakes ghata kar trust borrow, naya-hone
  mein honest raho. WCAG 2.2 floor (screen reader, keyboard, color-independent confidence).
- **Concept 6 — Load Redistribute:** cognitive/creative/logistical weight — chupke se move karna
  "agentic sludge" (sab dobara check karte ho). Fix: division of labor visible+adjustable.
- **Concept 7 — Progressive Transparency:** kuch na dikhana = no trust; sab dikhana = noise. 4 Layers:
  Outcome (1 line) → Plan (steps) → Why (honest confidence, real high/low/unsure not fake %) → Evidence
  (sources/trace).
- **Concept 8 — Autonomy Dial:** switch nahi, **dial** — banda pakarta hai. Human-in-the-loop (rukta hai)
  vs human-on-the-loop (act karta hai, insan dekhta hai). High-stakes/irreversible hamesha in-the-loop.
- **Concept 9 — Intent Preview:** act se pehle plan dikhao, edit ho sake. Preview stakes ke mutabiq scale,
  plan mid-flight editable.
- **Concept 10 — Asynchrony:** intent capture, glanceable progress, **nudge don't notify**, review-refine.
  Waiting design: honest progress, rough ETA, visible cost burn. "Silence broken lagta hai, busy nahi."
- **Concept 11 — Repair Aur Redress:** agent ghalat karega (will, not might). 4 Moves: undo (1-click,
  strongest trust-builder), straight apology, corrective action stated, visible human path. 2 numbers:
  escalation frequency (~5-15%), recovery success (~90%+).
- **Concept 12 — Kai Ko Supervise Karna:** 10 Workers = monitoring se **triaging** shift. 3 Surfaces:
  Fleet view, Attention triage, Drift signal (escalation rate double = over-trust caught). Circuit breaker:
  baseline-multiple cross kare to khud lower autonomy/pause.

## 02 — Machine Surface — Agents Ke Liye Design (Concepts 13-14)

- **Concept 13 — AX (Agent Experience):** aapke product ke robot users bhi hain — structure parhte hain,
  hostile structure = silent fail. 4 decisive factors: Access (scoped revocable credential), Context
  (model samajhta hai?), Tools (typed/discoverable?), Orchestration (chainable/idempotent?). Machine
  surface checklist: action-named tools, narrow typed schemas, declared side effects, structured errors,
  idempotent actions, provenance/permission, docs, contract tests. **MCP jaan-boojh kar chhodta hai:**
  orchestration, governance, state.
- **Concept 14 — Generative UI (MCP Apps):** tool text **aur** interactive `ui://` resource dono de sakta
  hai (sandboxed iframe). "MCP machine surface hai. MCP Apps interactive human surface hai." 4 properties:
  context rakhta hai, dono-taraf baat, host powers borrow, safe-by-construction. Widget kab jagah kamata
  hai: complex data, multi-option config, real-time monitoring — warna plain text kaafi hai. Discipline:
  progressive enhancement (open standard pehle, feature-detect extras).

## 03 — The New Craft (Concepts 15-18)

- **Concept 15 — Naye Design Objects:** Policy surfaces, Confidence conveyors, System temperament —
  screen-crafter se **choreographer** ban jate ho.
- **Concept 16 — Surface Ek Safety Control Hai:** OWASP Top 10 for LLM mapping — prompt injection
  (provenance+preview), excessive agency (autonomy dial+policy), misinformation (uncertainty+provenance),
  unbounded consumption (spend limits), sensitive-data disclosure (access pillar). Har system ko
  governance surface chahiye (approval, permission review, incident review, audit log, **kill switch**,
  drift review). "Clutter kam karna" = protection hatana ho sakta hai.
- **Concept 17 — Experience Measure Karna:** Eval-Driven Dev correctness measure karta hai; experience
  metrics **relationship** measure karte hain. Scorecard: plan-acceptance rate, intervention rate,
  recovery success, over/under-trust, notification precision, **time saved vs attention spent**. 6 Test
  Sequence before launch: plan-review, over-trust, recovery, interruption, accessibility, machine-surface
  contract.
- **Concept 18 — Anti-Patterns:** black box, agentic sludge, over-eager agent, over-trusted agent,
  notification spam, trap door, confused deputy, mystery-meat API — har ek ek concept se linked.
- **Agent Experience Brief (11 sections):** 2 audiences, first contact, trust surface, load map, autonomy
  ladder, async plan, recovery plan, scale, machine surface, safety surface, scorecard.

## 04 — Worked Example + Hands-On Lab + Projects

- **Worked Example (Support Worker):** Human surface — default 1-line outcome, plan on tap, autonomy stops
  (limits vs in-the-loop), 24h undo, fleet view. Machine surface — typed MCP tool, scoped credential,
  descriptive context, idempotent refund. Stakes barhein (vendor payments) → design weight recovery se
  prevention ki taraf shift, dual approval.
- **Hands-On Lab:** `create-mcp-app` skill install → 10-min scaffold/build/serve loop → local test host ya
  Claude tunnel se render → tool+resource pattern (`_meta.ui.resourceUri` = tool ko App banata hai) → Real
  Build: refund-approval card (confidence word not color, Approve/Escalate, 24h undo, >$50 disable Approve,
  idempotent). Design Pass Checklist 6 items, concept-linked.
- **7 Projects:** agent audit, autonomy dial draw, nudge budget, machine surface writeup, fleet view
  design, capstone 11-section brief, widget ship.
