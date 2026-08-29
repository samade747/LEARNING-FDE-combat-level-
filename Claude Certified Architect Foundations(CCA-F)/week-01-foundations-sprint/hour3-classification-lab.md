# Week 1, Hour 3 — Classification Lab

**Task:** 6 business problems ko in 6 categories mein classify karo. Har ek ke liye:
**{ type · enforcement mechanism · failure mode }**.

Categories: `direct call` · `workflow / prompt chaining` · `single agent` · `multi-agent system` ·
`Claude Code workflow` · `human-agent workflow`

---

### Problem 1 — "Har support email ko 5 categories mein se ek tag do, phir Zendesk mein route karo."

| | |
| --- | --- |
| **Type** | **Workflow / prompt chaining** |
| **Kyun** | Path fully known aur fixed: classify → map category to queue → API call. Koi runtime branching nahi. |
| **Enforcement** | Output constrained to enum (schema / `output_config.format`); routing table code mein, model ke paas nahi. |
| **Failure mode** | Model naya category invent kare ya out-of-enum de → downstream routing crash. Fix: enum + `other`+detail + `unclear`. |

### Problem 2 — "Naya microservice ke liye pura CRUD API + tests likho, existing repo conventions follow karte hue."

| | |
| --- | --- |
| **Type** | **Claude Code workflow** (plan mode) |
| **Kyun** | Multi-file, codebase context chahiye, architectural choices (schema, error handling). Yeh coding-agent ka kaam hai, raw API loop ka nahi. |
| **Enforcement** | `CLAUDE.md` conventions + plan-mode approval gate + CI (tests must pass) + code review in a fresh context. |
| **Failure mode** | Direct execution mein chala diya → galat direction par 40 min, rollback mehnga. Ya reviewer same context mein → generation ki assumptions challenge nahi hotीं. |

### Problem 3 — "Ek legal contract se 12 structured fields nikalo; कुछ contracts mein कुछ fields nahi hote."

| | |
| --- | --- |
| **Type** | **Workflow** (single constrained extraction call + semantic validation step) |
| **Kyun** | Fixed output shape, ek document at a time. Adaptive reasoning ki zaroorat nahi. |
| **Enforcement** | JSON Schema (required vs nullable); absent field → `null`, **invented value nahi**; `calculated_total` vs `stated_total` semantic check; targeted retry with the specific validation error. |
| **Failure mode** | Missing field ke liye model plausible value hallucinate kare. Ya syntactic-valid JSON ko "correct" maan lena (semantic validation skip). |

### Problem 4 — "Customer ka support issue end-to-end resolve karo: refund, replacement, ya escalation — jo bhi theek ho."

| | |
| --- | --- |
| **Type** | **Single agent** (with hard guardrails) — Track B Project 2 |
| **Kyun** | Next step unknown hai (customer ke jawab par depend karta hai), lekin domain ek hai — multi-agent ki zaroorat nahi. |
| **Enforcement** | 4 well-described tools; **programmatic refund controls** (amount cap in code/hook, prompt mein nahi); explicit escalation criteria (human maanga / policy gap / no progress); persistent case-facts block; structured tool errors. |
| **Failure mode** | Refund cap sirf prompt mein → model edge case mein cross kar de. Ya escalation "model confidence" / sentiment par base ho — reliable nahi. |

### Problem 5 — "Ek emerging technology par competitive intelligence brief banao — 8+ sources, conflicting claims possible."

| | |
| --- | --- |
| **Type** | **Multi-agent system** (coordinator + parallel subagents) — Track B Project 4 |
| **Kyun** | Independent research threads jo alag alag chal sakte hain; context/scale bottleneck (har source apna context khaता hai). Q5 = yes. |
| **Enforcement** | Coordinator explicit context har subagent ko pass kare (auto-inherit nahi hota); scoped tools per subagent; structured provenance (claim → source → date); conflicting sources **attribution ke sath preserve**, silently merge nahi. |
| **Failure mode** | Narrow decomposition — "creative industries" = sirf visual arts (guide ka apna example). Ya subagent timeout → coordinator ko empty result mile, use "valid empty" samajh le. Fix: partial results + report what failed. |

### Problem 6 — "Loan applications ko approve/reject karo underwriting rules ke mutabiq; regulator har decision ki human sign-off maangta hai."

| | |
| --- | --- |
| **Type** | **Human-agent workflow** |
| **Kyun** | Expensive + regulated mistake — decision par explicit human approval boundary chahiye. Agent draft karता hai, human commit karता hai. |
| **Enforcement** | Approval gate in code (agent `recommend` kar sakta hai, `approve` nahi — woh tool human ke paas hai); structured handoff with reasoning + cited rule; audit log. |
| **Failure mode** | "Human review" sirf prompt instruction ho → agent apne aap approve kar de. Ya handoff mein reasoning/citation na ho → human rubber-stamp kare. |

---

## Trade-off notebook entry — "Jo maine ALMOST galat classify kiya"

- **Problem:** #3 (legal contract extraction).
- **Almost-misclassification:** Pehle isko **single agent** likhne laga tha — "contracts alag alag
  structure ke hain, model ko adapt karna padega, isliye agent."
- **Woh clue jisne theek kiya:** Output shape **hamesha same 12 fields** hai, aur har document
  **independently** process hota hai — koi runtime "ab kya karun" decision nahi. Variability
  *input* mein hai, *control flow* mein nahi. Adaptive control flow = agent ka signature; yahan woh
  nahi tha. **Rule:** "input varied hai" ≠ "agent chahiye". Path known + fixed → workflow.
- **Choice:** Workflow — ek constrained extraction call + deterministic semantic-validation step +
  targeted retry.
- **Alternatives kyun kamzor:** Single agent = non-determinism + cost, bina koi control-flow
  benefit ke. Direct call (bina validation) = syntactic-valid-but-wrong JSON silently pass ho jata.
