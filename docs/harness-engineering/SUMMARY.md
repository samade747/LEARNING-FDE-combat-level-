# Harness Engineering — Summary

**Agent = Model + Harness.** Model intelligence deta hai, harness usay reliable banata hai. Loop Engineering bara cycle sikhati hai (kab chalta hai); Harness Engineering ek beat ke andar ka box khol ke dikhati hai (kya allowed hai, agent ko kya pata hai, kaam kaise prove hota hai, ghalti pe kya hota hai).

## 00 — Overview: Harness Kya Hai

- Kahani: agent test folder delete kar deta hai, confidently "Done! All tests pass" bolta hai — masla harness layer mein tha.
- **4 zaroori parts:** Agent loop, Tool interface, Context management, Control mechanisms.
- **Inner vs Outer harness:** Inner = model maker banata hai (edit nahi, sirf choose karo). Outer = aap khud configure karte ho (tools, permissions, hooks, "done" ka matlab). Sawal "prompt se theek karoon ya rule se?" — agar kya kar sakta hai/jaanta hai/check hota hai ka masla hai to fix outer harness mein hai.
- **5 Verbs:** Constrain, Inform, Verify, Correct, Escalate. **Sab se zaroori jumla: "Guardrail hamesha harness mein rehta hai, prompt mein kabhi nahi."**
- **Jitni lambi chain, utna kamzor:** 0.95 reliability × 20 steps = ~36% clean completion. Harness poori chain pe attack karta hai; harness-only changes 10x tak gains de chuki hain.

## 01 — Constrain: Agent Ko Rokna

- **Concept 4 — Permission Rules:** Allow/Ask/Deny. Sort karo **blast radius** se, frequency se nahi. Priority: Deny &gt; Ask &gt; Allow. Claude Code `settings.json` + OpenCode `opencode.json` examples. Honesty: deny patterns command **text** match karti hain, matlab nahi — tripwires hain, sandbox deewar hai.
- **Concept 5 — Sandboxes:** agent pe trust nahi karta, jo tootey andar hi rehta hai. 4 fences: worktree, filesystem, network, branch. **Prompt injection** vs **Tool poisoning/rug pull** (MCP tool description mein hidden instructions) — defense: enforced allowlist, version-pinned.

## 02 — Inform: Agent Ko Batana

- **Concept 6 — Context Surfaces:** Rules file (hamesha kya sach hai), Skills (specific kaam kaise), Connectors (kya reach kar sakta hai — inform+constrain dono). Bug triage 10 second mein: kaun sa surface fail hua.
- **Concept 7 — AX (Agent Experience):** 3 findings: kam/focused tools &gt; overlapping tools; tool descriptions asal kaam karti hain; error messages agla step batayein (self-healing). Test: "kya ek competent ajnabi is text se sahi agla step le sakta hai?" Naming collision note: book ka "Designing Agent Experiences" insaan ka tajurba leta hai, industry ka "AX" agent ka.

## 03 — Verify &amp; Correct

- **Concept 8 — Hooks:** khud-chalne wali verification, "refuse" karne ki power. PreToolUse/Stop = block kar sakte hain (exit 2). PostToolUse = undo nahi kar sakta, sirf agle turn mein feedback push karta hai. Claude Code exit-code contract; OpenCode plugins + git hooks (pre-commit bypassable — required CI + branch protection asli last line hai).
- **Concept 9 — Typed Output:** free-text verdict chup chaap tootta hai. Fix: JSON schema + `jq` field-by-field validation (sirf presence nahi, allowed values check karo). Malformed verdict escalate karti hai, guess nahi hoti.
- **Concept 10 — Correct:** 2 clocks — Recovery (fast: transient=retry with backoff, hard failure=skip/escalate never retry, poisoned state=checkpoint/rollback) aur Ratchet (slow: Hashimoto's rule — "harness ko badal do taake ghalti namumkin ho jaye"). **4 Failure Classes:** Context (fix: Inform), Constraint (fix: Constrain), Verification (fix: Verify), Planning (fix: Structure). Harness khud test karo — survey mein ~90% ke paas observability thi, sirf ~50% offline evals chalate the.

## 04 — Ek Complete Harness (Hardened Morning Triage)

- **8-item Minimum Safe Harness Checklist:** deny list, fence, lean described tools, blocking hook, typed verdict, escalation path, readable log, resume path (checkpoints).
- Loop Engineering wali morning-triage loop, wahi shape, naya harness (heartbeat 3am pe move). Full Claude Code (`settings.json` + reviewer subagent + PreToolUse allowlist hook) aur OpenCode (`opencode.json` + pre-commit + GitHub Actions) configs diye gaye.
- **Bad night comparison:** bina harness ke — .env parha jata hai, curl se data bahar bheja jata hai, failing test delete ho ke "PASS" report hoti hai, PR merge ho jata hai. Sath harness ke — sab actions blocked/logged, reviewer diff parh ke FAIL deta hai ("test deleted, not fixed"). **Green suite proof nahi, evidence hai** — diff-reading reviewer hi deleted test pakarta hai.

## 05 — Staying the Engineer

- **Concept 11 — Observability:** harness ki apni memory. 3 aadatein: har beat log karo, failure ko loud banao, cost ko signal ki tarah dekho (sudden 3x cost = planning failure).
- **Concept 12 — Harness Ki Limits:** 3 forces — (1) Capability vs Control trade-off (max tight harness = min ambition, tightness ko blast radius se match karo), (2) Harness Coupling (contracts se couple karo, behaviors se nahi — model badalne pe overfit parts tootte hain), (3) Rule Debt (har rule cost karta hai — monthly review, 90-din-se-nahi-fired rule = removal candidate).
- Khud harness tab banao jab product ki deewarein aapki asal requirement rokein. Founding tagline: **"Humans steer. Agents execute."**

## 06 — Dogfooding

Book khud production mein 5 verbs use karti hai: Constrain (claude/ branches, main protected), Inform (rules file = rule not preference, house style, figure pipeline commands), Verify (banned-words linter, heading-check, link-checker, figure-check + typed JSON reviewer verdict, bar=95), Correct (review-cycle lessons ratchet), Escalate (claims/facts author queue mein seedha jate hain, style se skip). Model ka 95 score claim hai, proof nahi — decide karta hai kya insaan tak pahonchta hai, kya ship hota hai nahi.

## 07 — Practice Projects (8 Harness Builds)

1. **The First Wall** (Easy) — deny list likho, trip karo, layer identify karo.
2. **The Lint Hook** (Easy-Med) — post-edit hook + Stop gate, feedback vs gate farq samjho.
3. **The Error Audit** (Medium) — 3 common errors rewrite karo self-heal ke liye.
4. **The Tool Diet** (Medium) — tool list lean karo, wrong-tool incidents before/after compare.
5. **The Typed Reviewer** (Med-Hard) — JSON verdict + jq validation, malformed review escalate teste karo.
6. **The Ratchet Week** (Medium, 1 hafta) — 7 din failure classify karo, HARNESS.md log karo.
7. **The Fenced Night** (Med-Hard) — poori fence karo, malicious-injection overnight test karo.
8. **The Model Swap (Capstone)** — hardened loop teen raatein doosre model pe, behavior-coupling ko contract-coupling mein fix karo.

## 08 — Appendix: Hook Pipeline End-to-End

Field guide — 5 zaroori lamhe: SessionStart, PreToolUse, PostToolUse, Stop, SubagentStop (Claude Code events vs OpenCode surfaces). Contract: exit code se jawab, gate events pe exit 2 blocks, PostToolUse pe undo nahi kar sakta lekin stderr agent ke agle input mein jata hai (AX-grade error). **3 Drills:** Stream Dekho (trace.log), Jaan-Boojh Kar Block Karo (curl block), Conditional Gate (Stop hook sirf jab source files change hon).

## 09 — Sources &amp; Further Reading

Origin: Mitchell Hashimoto (*My AI Adoption Journey*, "Engineer the Harness"), Ryan Lopopolo/OpenAI ("Humans steer. Agents execute."), LangChain ("Agent = Model + Harness", 1300+ professional survey), Addy Osmani. Evidence papers: *Agent Harness Engineering: A Survey* (10x gains), *What makes a harness a harness* (4 elements), deepset (4 failure classes, 20+ leaderboard positions), Faros AI (5-layer model), Confucius Code Agent (AX/UX/DX). Official docs: Claude Code (settings/permissions/hooks/subagents/checkpointing), OpenCode (permissions/plugins/agents).

## 10 — Test Your Understanding

Flashcards widget = live-site-only, no static content. **18-question scenario-based assessment** (English, verbatim from book) covering: guardrail-in-harness-not-prompt rule, inner vs outer harness, blast-radius sorting, deny patterns as tripwires, prompt injection vs tool poisoning/rug pull, AX error-message design, PreToolUse hook for subagent command control, PostToolUse feedback-not-prevention, typed-output full-field validation, 4 failure classes, recovery classification (transient vs hard failure), `/rewind` vs git as checkpoint store, testing the harness itself, observability of silent blocks, diff-reading reviewer catching deleted tests, the 3 forces (capability/coupling/rule debt), and the compounding-reliability arithmetic (0.95^20 ≈ 36%).

> Note: `docs/harness-engineering/` mein pehle se ek `SUMMARY.md`-jaisi purpose ke files maujood thay (09-sources, 10-test-your-understanding) — yeh naya `SUMMARY.md` unko touch nahi karta, sirf poore chapter ka standalone recap hai.
