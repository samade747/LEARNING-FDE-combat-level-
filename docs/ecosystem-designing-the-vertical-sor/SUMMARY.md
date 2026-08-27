# Designing the Vertical System of Record — Summary

**First-principles, legacy-informed redesign.** Purane workflow ka har piece khud profession nahi —
zyada tar insaani limits (attention, scattered info, dept handoffs) ya purani technology ka workaround
hai. Method: purane kaam ko study karo (workflow archaeology), har element ko teen bins mein sort karo
(keep law/trust, redesign human-limits, delete old-tech), phir reflexes ko un sachaiyon se scratch se
rebuild karo — insaano ke liye nahi, AI Workers ke liye. Ek complete, proven **thin slice** — ek outcome,
poora covered, governance din-1 se — hi woh credential hai jo sponsor conversation kamati hai.

## 00 — First Principles: Kyun Purana Workflow Blueprint Nahi Hai

- 5 pre-agentic limits (scarce attention, scattered info, software jo samajh nahi sakti, department
  divisions, manager blindness) ne har purana workflow shape kiya — accounting/credit/recruitment nahi,
  human-only era ka jawab hai.
- The Operating Layer: SaaS = system of record + capabilities + workflow UI. Agent capabilities khud
  chalata hai to **workflow UI sabse pehle marta hai** — iska purpose hi insaan tha.
- PwC 2026 data: 56% CEOs ko koi financial return nahi mila AI se — wajah models nahi, **skipped
  fundamentals** (clean data, sound processes, governance) hain.
- First principles **asymmetrically** apply hoti hai: corpus = given (faithful service, kabhi redesign
  nahi), reflexes = scratch se derive, map = Worker ki zaroorat ke around redraw.

## 01 — Outcome Se Shuru Karo, Phir Workflow Archaeology

- Professional outcome pehle likho (jo reviewer recognize/judge kar sake), phir outcome contract
  (Template 1). Main number abhi likho, uska starting-value baseline sirf customer de sakta hai.
- Archaeology copy karne ke liye nahi, dig karne ke liye — 5 real cases expert ke sath (normal,
  difficult, failed, escalated, expert-catch). Abhi koi customer nahi, isliye expert ki files par chalti
  hai. Unwritten layer = expert twin ka source.

## 02 — Three-Bin Sort Aur Source Hierarchy

- Har element se ek sawal: **yeh kyun exist karta hai?** Bin 1 (law/trust — keep, invariants likho),
  Bin 2 (human limits — redesign, purpose survive karta hai capability+checker mein), Bin 3 (old tech —
  delete). Sharpest refinement: control ka purpose Bin 1, mechanism zyada tar Bin 2.
- Chesterton's Fence: shak ho to Bin 1 mein rakho jab tak expert confirm na kare. Sort khud governed
  content hai — reason ke sath record hota hai.
- Source hierarchy: 7-rung typical ladder, **relevance kaafi nahi — applicable bhi hona chahiye**.
  Cross-border: naya country = naya ladder-set isi SoR mein, kabhi blend nahi.

## 03 — Do Content Classes: Authority Vs Orientation

- One source, two readers. **Authority** (citation/change/dispute test, kam se kam ek pass) — Worker
  cite karta hai. **Orientation** (short, context-marked, kabhi cited nahi) — insaan ke liye, professional
  reader lost na ho.
- Formatting (tip/info boxes) sirf visible mark hai — build 3 validation rules bhi chalata hai taake real
  threshold orientation mein na chhupe.
- Teen bars: simple (beginner), exact (Worker — sirf simple hona kaafi nahi), structured (invisible,
  Worker-only). Whole design target: **best junior handbook likho, phir machine layer add karo.**

## 04 — Decisions, Rules/Judgment/Permissions, Exceptions, Rebuild Reflexes

- Departments nahi, **decisions** map karo — customer inhe kisi bhi team ko de sakta hai.
- Rules (clear condition→result, automatic checks) vs Judgment (interpretation, supported/tested, kabhi
  prompt mein chupaya nahi jata) vs Permissions (Read→Execute-irreversible, alag grants, prepare ≠
  release).
- Exceptions normal path se pehle design hoti hain — useful escalation insaan ka kaam kam karti hai.
- Reflexes scratch se rebuild: batch-vs-event aur sequence dono fresh sawal. **Thin slice**: ek complete
  outcome — coverage register mein fact ki tarah likha jata hai, feeling nahi.

## 05 — 8 Failure Modes + Ayesha Ka Worked Example

- Document dump, AI-readable SOP, technology first, rules hidden in prompts, authority before evidence,
  happy-path demo, first-principles theater, unmarked textbook.
- Ayesha apni khala ki 41-item checklist sort karti hai — photocopy delete, tick-and-tie redesign
  (exception report), 3-level review purpose se split, partner ka going-concern sign-off untouched.
  4 ghante → 40 minute. Uske aunt ka number **design-against** hai, baseline nahi — baseline sirf
  customer se aata hai.

## 06 — 7 Templates + Definition Of Done

- Outcome Contract, Sort Record, Invariants List, Source Register, Decision Map, Exception Entry,
  Coverage Register — har ek governed content hai (owner, review, version).
- Definition of done = 16-box checklist, do lists ek mein: "outcome complete" aur "**ready to sell**."

## 07 — Appendix A: Sales System Of Record (End To End)

- CRM ≠ Sales SoR — CRM deals hold karta hai, SoR profession hold karta hai (qualification evidence,
  claims, stage-advance rules).
- Trust-governed, shallow policy-driven hierarchy. Worker routine messages khud bhej sakta hai (send
  permission) lekin pricing/negotiate/new-prospect kabhi nahi.
- 6 evidence states (confirmed→outdated) taake CRM field apni evidence se zyada certain na lage.
  Evaluation set ka special case: seller ka apna pressure (pipeline inflate karne ka).

## 08 — Appendix B: General Ledger System Of Record (End To End)

- ERP ≠ Ledger SoR — ERP numbers hold karta hai, SoR profession (close kaise hota hai) hold karta hai.
- Law-governed, deep hierarchy — **ek ladder per question** (reporting vs tax), ek overall ladder nahi.
  Worker sirf prepare+recommend karta hai, kabhi post/close/master-data nahi.
- Month-end batch classic split-across-bins example: deadline Bin 1 (legal), batching-the-work Bin 2.
  Executive-requested unsupported entry invariant se refuse hoti hai, seniority se nahi.

## 09 — Dono Appendices Ka Contrast, Poster, Flashcards, Aage Kya

- Shared spine: outcome→archaeology→sort→rebuild→prove, dono appendices mein identical. Jo differ karta
  hai: hierarchy depth, permission boundary, invariant ka focus, corruption ka shape.
- Poster = 8-step visual summary. Flashcards = live-site-only widget (yahan sirf pointer).
- Aage kya: AI Searchable Context → Skills & Connectors → Spec-Driven Development → Eval-Driven
  Development → expert twin → domain builder → first Worker. Sort khud "real kaam" hai, prep nahi —
  value reason (jo koi copy nahi kar sakta) aur sequence reason (vendor-neutral FDE do SoRs le kar
  jaati hai: method + profession).

## 10 — Test Your Understanding / Quiz

Book ka apna **59-question `<Quiz>` component**, verbatim (English mein, precision ke liye) — har
question ek section ka scenario-based test hai, 4 options + detailed explanation + source-section.
Dono [10-test-your-understanding.md](10-test-your-understanding.md) aur [quiz.md](quiz.md) mein same
content hai (standalone practice ke liye), jaisa `docs/harness-engineering/` ka pattern hai.

## Practice Project

[`projects/fill-the-templates/`](projects/fill-the-templates/README.md) — 7 templates ko apne chune hue
vertical/outcome par fill karo, Ayesha ka worked example reference-solution ki tarah use karo.

---
[⬅ Chapter Index](README.md)
