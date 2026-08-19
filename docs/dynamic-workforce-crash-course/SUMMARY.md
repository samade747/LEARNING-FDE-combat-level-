# A Self-Expanding Workforce with Paperclip — Summary

90-Minute Crash Course. Pichle course ki fixed team ab **khud grow hoti hai:** gap detect → hire propose
(APPROVE/REJECT) → chota probation → pass ho to grants barhao → kaam khamosh ho to pause → ledger mein sab
likha jata hai → gap-check schedule par chal sakta hai.

## 00 — Scenario 1: Gap Spot Karna

- **Core idea:** workforce gap khud spot karti hai, hire draft karti hai, board approval ki tarah aapke
  saamne lati hai — **hiring ek function call ban jata hai, aap gate rehte ho.**
- **2 Decisions:** (1) Kya waqai gap hai — 3 signals mein se **2 chahiye**: role cover nahi karta, aata
  rehta/barhta hai, ghalat wapis ata hai. Trap: agar koi member chupke se theek handle kar raha hai to
  yeh routing problem hai, capability gap nahi. (2) Confirmed gap bhi auto-hire nahi — 4 forks: **HIRE**
  (durable+high-volume/risky), **ESCALATE** (consequential/rare, insan decide kare), **QUEUE** (seasonal/
  bursty), **DECLINE** (off-mission/cost not worth).
- 3 example candidates: Reader support (HIRE), issue shipping (QUEUE), analytics (DECLINE for now).

## 01 — Scenarios 2-3: Hire Likhna Aur Approval

- **Scenario 2:** Hire = job rec — Role, Capabilities (description hai, fence nahi), Engine, Budget
  (chota monthly cap), Receipt (source issue). **Work-sample par hire karo, resume par nahi** — probation
  (chota trial+budget+minimal authority), score: sahi jawab, **apni lane mein raha**, tone, cost. Kabhi
  compromise mat karo: lane-mein-rehna (galat jawab quality problem hai; lane-se-bahar governance problem).
- **Scenario 3:** Hiring wahi board-approval gate reuse karti hai. **Alfaz fence nahi, grants hain** — real
  fence Paperclip ki server-enforced permissions layer (scoped). 2 layers: coarse gate (company switch —
  approval chahiye ya nahi) + fine grant (permissions/scopes). Pre-approval discipline sirf apne-approve-
  karne-wale ko pre-filter kar sakti hai, kabhi zyada authority nahi de sakti.

## 02 — Scenarios 4-5: Probation Aur Lifecycle

- **Scenario 4:** Approve = paper "haan"; ab work sample real hota hai. Approve → first heartbeat. **Pehla
  din sabse sasta din hai bad hire pakarne ke liye** — pehle runs dekho, sausvi nahi. Pass → budget+specific
  grants barhao. Fail (especially lane se bahar) → terminate, almost kuch nahi khoya.
- **Scenario 5:** **Pause** = furlough — spend/heartbeats rukte, definition/history/permissions/track-record
  rehta hai, **reversible**. **Terminate** = one-way door, role genuinely khatam hone par. Resume = wahi
  Worker poori history ke sath — fresh hire se behtar.

## 03 — Scenarios 6-7: Ledger Aur Cadence

- **Scenario 6:** Har action ek row — gap detect, hire propose, probation approve, budget barha, cost par
  resolve, pause. 6 mahine baad chalti hui history hi honest jawab hai. Naya operator ledger se seedhe
  answers nikal sakta hai.
- **Scenario 7:** **Routine** = schedule par reminder — task likhta, worker ko deta, jagata hai. Zaroori
  catch: Worker sirf **on call** ho to jawab deta — table 3 setups (on call/off-call-timer-on/off-call-
  timer-off default) ka behavior. Setup 2 steps: CEO on call, routine point karo. Build: weekly gap-scan
  routine, auto-run watch karo (waiting → in progress → done/in-review, no manual poke).

## Aap Ne Kya Banaya

- Discipline: **authority woh cheez hai jo aap extend karte ho, default nahi.** Board decide karta hai
  kaun kar sakta hai, kitna kharch, kya chhu sakta hai — honest ledger ke sath jo agla operator parh sake.

## Recipe Vs Relationship (README table)

- Recipe (portable): capabilities description, probation plan, engine choice. Relationship (company mein
  rehta hai): permissions/scopes, budget/spend history, gap-history, reporting line. **Recipe hi aap carry
  karte ho** — workforce jiska reasoning handoff ho sake.
