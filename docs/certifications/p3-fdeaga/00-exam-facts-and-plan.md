# 00 — Exam Facts + 4-Day Study Plan + Test Strategy

## Exam Facts

| Field | Detail |
| --- | --- |
| Code | **P3-FDEAGA** — "FDE–Agent Factory Model and Advanced General Agents" |
| Program | GIAIC Final Graduation Exam 2026 |
| Venue | Sindh Governor House, Karachi |
| Schedule | First week of September 2026 |
| Items | **100 MCQs** |
| Time | **140 minutes** |
| Pass | **70%** — 70/100 sahi chahiye |
| Consequence | Sirf pass karne wale GIAIC se graduate honge |

**Time math:** 140 min ÷ 100 = **1.4 min/question**. Plan: pehla pass ~90 min (aasan + medium),
doosra pass ~35 min (flagged/hard), ~15 min review. ~30 galtiyon ki gunjaish hai — har question par
atakna zaroori nahi.

## Syllabus Weight — Kaise Sochna Hai

Official syllabus 8 modules ko **equal-looking** list karta hai. Lekin content ki gehrai aur "advanced
general agents" naam se practical weight yeh banta hai:

| Group | Modules | Practical focus |
| --- | --- | --- |
| **Foundations / framing** | 1 Roles · 2 Ecosystem | vocabulary, "kaun kya karta hai", System of Record idea |
| **The agent reliability stack** (dil) | 4 Loop · 5 Harness · 6 Trusting the Checker · 7 Leaving the Laptop | yeh 4 ek dusre ke upar khare hain — inke beech ke **farq** par MCQ bante hain |
| **General agents** | 8 General Agents on the Web · 3 Local AI & Agentic Coding | browser agent surface, model kahan chalta hai (local/server/cloud) |

**Sabse zyada trap questions:** "Loop vs Harness", "Test vs Eval", "kaunsa layer is bug ke liye
zimmedar hai", "control plane vs execution plane". Inhe ratna nahi — **farq samajhna** hai.

## 4-Day Study Plan

| Din | Modules | Deliverable |
| --- | --- | --- |
| **Din 1** | M1 Roles · M2 Ecosystem | [01](01-roles-we-are-training-for.md), [02](02-agent-factory-ecosystem.md) padho + MCQ |
| **Din 2** | M3 Local AI & Agentic Coding · M4 Loop Engineering | [03](03-local-ai-and-agentic-coding.md), [04](04-loop-engineering.md) + MCQ |
| **Din 3** | M5 Harness Engineering · M6 Trusting the Checker | [05](05-harness-engineering.md), [06](06-trusting-the-checker.md) + MCQ |
| **Din 4** | M7 Leaving the Laptop · M8 General Agents · **full mock** | [07](07-leaving-the-laptop.md), [08](08-general-agents-on-the-web.md), [quiz](quiz.md) |
| **Exam raat** | Sirf [SUMMARY.md](SUMMARY.md) | koi naya topic nahi |

Har module ke baad: is repo ke deep notes ka `test-your-understanding` / `quiz` bhi chala lo (Loop ka
61-Q, Harness ka 18-Q sabse qeemti hain).

## Test-Day Strategy

1. **Do-pass method.** Pehle pass: jo 15 sec mein aata hai, mark karo, aage barho. Baaqi flag.
   Doosre pass: flagged. Aakhri: review.
2. **"Hamesha / kabhi nahi" wale options shak se dekho** — nuance-heavy course hai, absolute options
   aksar galat hote hain (exception: real invariants jaise "finished work exits the platform").
3. **Layer sawal:** pehle poochо "yeh Loop ka masla hai ya Harness ka?" — missing heartbeat vs
   missing deny-rule do alag bugs hain.
4. **Definition sawal:** exact wording yaad rakho — "Agent = Model + Harness", "Eval ek distribution
   estimate karta hai, Test ek property", "control plane = decide, execution plane = run".
5. **Numbers:** ~95% pilots fail, +729% postings, 4 homes, 3 tiers, 6 shared parts of an agent
   surface, 7 principles of problem solving — inhe cram sheet se ratо.

---
[⬅ P3-FDEAGA Index](README.md) · [Agla: 01 — Roles ➡](01-roles-we-are-training-for.md)
