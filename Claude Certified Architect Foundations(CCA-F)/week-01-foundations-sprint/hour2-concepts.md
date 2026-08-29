# Week 1, Hour 2 — Architecture Concepts

*4 distinctions jo poori quarter ki base hain. Har ek: architect ki definition + ek misaal + exam
mein kaise aata hai.*

## 1. Architecture vs Implementation

- **Architecture** = kya banana hai aur kyun — components, boundaries, control flow, enforcement
  points, failure modes. Tool-neutral.
- **Implementation** = usay kis library/syntax/SDK se likha — badalta rehta hai.
- **Misaal:** "refund $100 se upar human approval maangega" = architecture. `PreToolUse` hook jo
  `amount > 100` par `deny` return karta hai = implementation.
- **Exam:** distractors aksar sahi *implementation* hote hain galat *architecture* ke liye (e.g.
  prompt mein likh dena "don't refund over $100" — sahi syntax, galthe enforcement layer).

## 2. Deterministic vs Probabilistic behaviour

- **Deterministic** = har baar same input → same output, guarantee ke sath. Code, hooks,
  permissions, gates, schema validation.
- **Probabilistic** = model ka faisla — usually theek, lekin *guarantee nahi*.
- **Rule:** agar ek business invariant **kabhi violate nahi hona chahiye**, prompt wording par
  bharosa mat karo — code/permissions/hooks mein enforce karo. "Preferred" behaviour → prompt
  guidance theek hai.
- **Misaal:** "PII kabhi log na ho" = deterministic (output normalization hook). "Jawab polite ho"
  = probabilistic (prompt).

## 3. Workflow vs Agent

- **Workflow** = control flow **design time par fixed**. Architect ne steps, order, tools pehle
  wire kiye. Predictable, cheaper, testable.
- **Agent** = control flow **runtime par model** ke paas. Goal + tools + feedback loop diya, model
  tay karta hai kya karna hai aur kab done hai.
- **Rule:** fixed predictable stages → workflow / prompt chaining. Unknown next steps → adaptive
  agent. Simplest pattern chuno jo task *asal mein* maangta hai.
- **Misaal:** invoice se 6 fields nikalna (hamesha same 6) = workflow. "Is customer ka issue
  resolve karo, jo bhi lagे" = agent.

## 4. Root cause vs Symptom

- **Symptom** = jo dikhta hai (galat tool chala, jawab adhoora, loop repeat).
- **Root cause** = kyun (tool description ambiguous, history pass nahi hui, stop signal galat handle
  hua).
- **Rule:** failure diagnosis mein **root cause fix karo, symptom nahi**. Galat tool routing ka fix
  = pehle names/descriptions/schemas/scope inspect karo — routing complexity (ek router agent) add
  karna symptom-patch hai.
- **Misaal:** agent do overlapping tools ke beech misroute karta hai → symptom-fix = teesra
  "dispatcher" tool. Root-cause-fix = do tools ko rename/split/merge karke ambiguity khatam karo.

---

## Connective tissue

Yeh 4 distinctions [[four-layers]] ke "kaunsi layer toti?" sawal aur [[choosing-agentic-architectures-crash-course]]
ke "architectural fit, capability matching nahi" se seedha judte hain. Architecture Decision
Framework (00-overview) inhi 4 ko ek lookup table bana deta hai.
