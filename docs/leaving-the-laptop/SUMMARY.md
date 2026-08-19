# Leaving the Laptop — Summary

Trilogy (Loop Engineering, Harness Engineering, Trusting the Checker) ke baad aakhri dependency hataata
hai: aapka **hardware**. Course sikhati hai agent **kahan rehta hai** aur **kaun usay zinda rakhta hai**
decide karna — uska behavior nahi (wo pichli 3 courses tay kar chuki hain).

## 00 — Overview: Aakhri Dependency

- System mukammal hai lekin trapped: laptop khula, session logged-in, machine awake/power/network hona
  chahiye — miss karo to beat chup chaap ruk jati hai. **System us machine se zyada reliable hai jispar
  chalta hai** — yehi signal hai ghar se bahar nikalne ka.
- **Concept 2:** Har option ek sawal se sort hota hai: **kaun agent loop operate karta hai, aur uska kaam
  kahan execute hota hai?** — 2 halves: **control plane** (loop khud) aur **execution plane** (jahan
  actions land karte hain). Laptop par dono ek machine hain; aage wale ghar inhe alag kar sakte hain.
- **4 Ghar table:** (1) Aapki session — control+execution dono aap; (2) Cloud schedule — control aap
  (scheduler se), execution cloud runner; (3) Managed runtime — dono vendor (ya self-hosted execution);
  (4) Apna process — dono aap (Agent SDK, Mode 2).
- Sawal technical nahi, business sawal hai: "khud karein ya kisi ko paisa den?" Rule: **sirf wahi own
  karo jo zaroori hai, jo chahte ho wo nahi.**
- Self-check example: Ayesha (load-shedding, 6pm daily invoice deadline) → Ghar 2 kaafi hai, Ghar 3 abhi
  zaroorat nahi.

## 01 — Headless: Har Ghar Ka Pul

- **Concept 3:** Headless mode already eval course mein use ho chuka tha (`claude -p`, `opencode run`) —
  agent command ki tarah, session nahi. **Jo bhi command chala sakta hai, wo agent chala sakta hai.**
  Ghar 2 se aage, har ghar sirf iska jawab hai: kiska computer, kis clock par.
- Nayi aadat: **headless runs loudly fail hone chahiye** — exit code check, failure par loud alert. Chup
  ka matlab success — yeh aap enforce karte ho.
- **Concept 4 (Ghar 2 — Cloud Schedule):** Sirf clock relocate hota hai, config wahi rehti hai. Claude
  Code Routine (`/schedule`), 3 honesty notes: research preview, "around" time promise (stagger), green
  status ≠ task succeeded. Trap: Desktop app ka "Local" = Ghar 1 hi hai, timer ke sath. GitHub Actions
  `schedule:` vendor-neutral option. OpenCode: koi first-party control plane nahi — scheduler khud chuno.
- Success ki definition: **kam se kam ek poora operating cycle + 10 successful beats**, laptop band, chup
  = baseline.
- **Minimum Unattended Kit (6 controls):** idempotency, missed-run detection, concurrency lock,
  credential discipline, time semantics, cost+execution limits — Ghar 2 ki entrance fee, aage bhi travel
  karti hai. Trap: escalation ab AAP tak pohanchni chahiye, desk tak nahi.

## 02 — Managed Runtime (Ghar 3)

- **Concept 5:** Aap definition bhejte ho (model, prompt, tools, guardrails), service **operate** karta
  hai. Claude Managed Agents (April 2026 beta): **Agent** (definition), **Environment** (execution plane —
  vendor cloud sandbox ya self-hosted), **Session** (pause/resume/days tak survive). Concept 2 ke 2 planes
  ab **visible aur separable** ban jate hain. 2 boundary facts: control plane vendor-specific hai; SDK aur
  Managed Agents alag products hain.
- **Concept 6:** Kya milta hai — sandboxing, session state, context mgmt; infra pager vendor ka,
  business-outcome pager aapka rehta hai. Kya dena parta hai — visibility, custody, portability (definition
  move nahi hoti, rewrite hoti hai). Keemat: naya bill type — ~8 cents/active-session-hour (idle free) +
  tokens; bhatakti loop paisa bhi kharch karti hai, sirf waqt nahi. Vendor updates model+harness dono
  saath move karte hain — defense wahi (scheduled full-set run, baseline, loud alert).

## 03 — Move Khud

- **Concept 7 (Suitcase Test):** Jo travel karta hai — spec, rubric, golden set, ratchet log,
  maker-checker split, human gate (**decisions, koi software nahi**). Jo travel nahi karta — flags,
  paths, session state, runtime-specific API code, cost assumptions. **Portable asset = discipline layer**,
  repo truth rakhta hai.
- **Concept 8 (Trust Re-Earn Hoti Hai):** Purana score ek **system** ka tha; move ne system badal diya.
  **Arrival protocol:** (1) naye ghar mein poora golden set chalao (smoke set nahi), (2) misses category
  se parho count se pehle, (3) bars hold karo phir naya baseline record karo (runtime-labeled, purana
  delete nahi), (4) probation before dependence (poora cycle + 10 beats). Warning: naya reach naye
  injection cases mangta hai.

## 04 — Ghar Chunna: 4 Sawal

- **Concept 9:** Q1 (User kaun? — sirf aap → Ghar 2 taqreeban hamesha kaafi), Q2 (Kya own karna zaroori?
  — kuch nahi/execution+data/control plane bhi → 3 answers), Q3 (Koi wait karta hai screen pe?), Q4 (Buri
  raat ki keemat? — speed limit, destination nahi badalta).
- **Concept 10:** Morning-triage worked example — Q1 team+2 teammates → Ghar 2 (GitHub Actions). Move:
  workflow file + kit + suitcase fix + arrival protocol + 2-week probation. **Mix:** healthy system
  usually 2-3 gharon mein phaila hota hai (loop Ghar 2, eval gate CI mein, heavy one-off Ghar 1). Ghar
  permanent loyalty nahi hai.

## 05 — Staying Honest: Lock-in Aur Limits

- **Concept 11:** **Lock-in rate hai, event nahi** — chhoti settings vendor-side mein leak hoti rehti
  hain. Measure: "agar ghar quarter mein gayab ho jaye, move ki keemat kya hogi?" Defense: repo truth +
  quarterly practice run. **Ownership drift** hoti hai chahe leak na ho — mahino ka chup-chaap-chalna
  "measured" se "theek hai" mein promote ho jata hai. Fix: repo single source of truth + calendar reminder
  jo AAPKO watch kare.
- **Concept 12:** Koi bhi ghar agent ko **kitna acha** kaam karta hai woh fix nahi karta — sirf kab/kaun/
  3am. Weak spec Anthropic cloud pe bhi weak rehti hai. Isiliye yeh course trilogy ki **aakhri** hai.
- **Poori trilogy ka ant:** drive → direct (spec) → delegate (loop) → harden (harness) → measure (evals)
  → **house** (runtime) = specified, guarded, measured, housed unit of work = **Digital FTE** ka darwaza.
  3 aage ke darwaze: Personal Agent Harnesses, Mode 1 Problem-Solving, Mode 2 Manufacturing.

## 06 — Practice Projects (8 Moves)

8 moves easy→hard, 2 rules hamesha (throwaway repo, failure khud plant karo): (1) Headless Wrapper —
network-nikal-kar-alarm test; (2) First Scheduled Beat — laptop-band-with-result; (3) Suitcase Audit —
hardcoded paths/names list; (4) Arrival Protocol — full golden set + runtime-labeled baseline; (5)
Probation — 1 cycle + 10 beats + planted failure; (6) Four Questions in Writing — Q1-Q4 per loop,
committed file; (7) One Session in Home 3 — managed agent + event log + cost note; (8) Vanishing-Home
Drill (Capstone) — repo-only fresh rebuild, timed, quarterly.
