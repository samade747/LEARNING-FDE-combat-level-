# 07 — Leaving the Laptop (Runtime)

*Source: `leaving-the-laptop-crash-course` (Zia Tutor AI, corpus gen 62). Deep notes:
[`docs/leaving-the-laptop/`](../../leaving-the-laptop/README.md).*

> **Trilogy ka 4th:** Loop ne agent ko **waqt** diya · Harness ne **limits** · Evals ne **track
> record** · yeh course usay **ek pata jo tumhara nahi hai** deta hai. Yeh course agent ka **behavior**
> nahi sikhati (woh 3 pichli courses ne tay kiya) — sirf **kahan rehta hai** aur **kaun usay zinda
> rakhta hai**.

---

## A. Aakhri Single Point of Failure

- Trilogy ne single points of failure ek-ek karke hataye: maker-checker (single unreviewed opinion) ·
  harness (single unguarded action) · evals (single unchecked checker).
- **Ek baaki hai — aur woh TUM ho.** Tumhara judgment nahi (jo human gate sahi rakhta hai) — tumhara
  **hardware**: laptop khula, session logged in, machine 9am par awake/power/network.
- **System us machine se zyada reliable hai jispar woh chalta hai** → signal ke woh apne ghar se
  bahar nikal chuka hai.

## B. Ek Sawal Jo Har Option Sort Karta Hai

> **Kaun agent loop operate karta hai, aur uska kaam kahan execute hota hai?**

| Plane | Kya |
| --- | --- |
| **Control plane** | loop khud — sessions start karta hai, model ko feed, events stream, 3am crash par restart |
| **Execution plane** | jahan actions land — sandbox jahan tools chalte hain, data jo woh touch karte hain |

## C. The 4 Homes

| Ghar | Control plane | Execution plane | 3am kaun jagta hai | Ek line |
| --- | --- | --- | --- | --- |
| **1. Tumhari session** | Tum | tumhara laptop | Tum | **banane + prove karne** ka sahi ghar; **depend karne** ka galat ghar. Trilogy yahan hui |
| **2. Cloud schedule** | Tum (scheduler ke zariye) | cloud runner | Shared | **sirf clock relocate** — config wahi. Sabse chhota move, sabse bara immediate payoff |
| **3. Managed runtime** | **Vendor** | vendor cloud sandbox (default) ya **self-hosted sandbox** (custody) | infra unka, outcomes tumhare | tum agent ki **definition** hand over karte ho; **loop operate karna chhor dete ho, uske ird-gird ka business operate karte raho** |
| **4. Apna process** | Tum | Tum | Tum, jaan-boojh kar | harness ek **library** ban jaati hai; **Agent SDK, Mode 2 ka ilaaka** — is course mein sirf darwaza |

> **Sawal technical nahi:** har business poochta hai — **khud karein ya kisi ko paisa den?** Rule:
> **sirf wahi own karo jo zaroori hai, jo chahte ho woh nahi.**

## D. Headless — Har Ghar Ka Pul

- **Tum yeh pul already paar kar chuke ho** — evals course mein runner ne `claude -p` / `opencode run`
  call kiya: agent ek **command** ki tarah, conversation nahi. Prompt jata hai, kaam hota hai, output
  aata hai, process khatam.
- **Jo bhi command chala sakta hai woh ab tumhara agent chala sakta hai** — shell, cron, CI runner,
  cloud scheduler. Ghar 2 se aage har ghar sirf iska alag jawab hai: **kis ka computer headless
  command chalata hai, aur kis ke clock par.**
- **Nayi aadat (koi dekh nahi raha):** **headless runs loudly fail hone chahiyen** — uncheck kiya
  exit code = chup-chaap na hui beat. **Chup ka matlab success — yeh tum enforce karte ho.**

## E. Ghar 2 — Cloud Schedule

- Claude Code: **`/schedule`** (alias `/routines`) — Anthropic-managed cloud, laptop khula ho ya na.
  - **3 honesty notes:** Routines research preview · scheduled run ghante ke kuch minute baad ("stagger");
    **"around 9am" asal promise hai** · **green run status sirf itna: session infrastructure error ke
    baghair khatam hua — task succeed hua yeh NAHI.**
  - **Trap:** desktop app mein **Local** choose karna = Desktop scheduled task **tumhari machine** par
    → yeh **ghar 1 timer ke sath**, move bilkul nahi.
- Vendor-neutral: **GitHub Actions** `schedule:` trigger par `claude -p` headless (best-effort — late/
  drop ho sakti hain).
- OpenCode: **scheduler tum chunte ho** (koi first-party hosted control plane nahi). "Tum ab khud
  vendor ho."

### Success ki definition (migration "done")

> **Kam se kam ek poora operating cycle + kam se kam 10 successful beats, laptop band, chup = baseline.**
> "Ek dafa cloud se chala" NAHI. + **loud-failure test** (jaan-boojh kar ek failure plant karo, alarm
> tum tak pohanche).

### Minimum Unattended Kit — 6 controls (koi optional nahi)

| Control | Rule | Rukti hui failure |
| --- | --- | --- |
| **Idempotency** | retried beat repeat hona safe | invoice do dafa bhej dena |
| **Missed-run detection** | ek doosra system notice kare jab pehla shuru hi na hua | jo process chali hi nahi woh apni gair-mojoodgi report nahi kar sakti |
| **Concurrency lock** | ek waqt ek beat | 2 agents ek hi files edit |
| **Credential discipline** | scoped service credentials, least privilege, rotated, **kabhi personal login nahi** | cloud runner tumhari poori identity hold kare |
| **Time semantics** | timezone likhi hui, daylight-saving pehle se decided | 6pm invoice saal mein 2 dafa 1 ghanta khisak jaye |
| **Cost + execution limits** | max duration/turns/retries/spend per beat | bhatakti run raat mein poora budget kha jaye |

> Yeh kit ghar 2 ki **entrance fee** hai — har agla ghar bhi yehi 6 mangta hai.
> **Trap:** laptop par human gate ki convenient property thi — **tum wahin the**. Ghar 2 mein
> escalations bina dekhe jama ho sakti hain → **escalation channel tumhare desk tak nahi, TUM tak
> pohanchna chahiye** (message, mention, issue jispar tumhara naam).

## F. Ghar 3 — Managed Runtime

- **Contract:** tum apna agent describe karte ho (model, prompt, tools/connectors, guardrails),
  service usay **operate** karta hai. Example: **Claude Managed Agents** (April 2026 public beta):
  | Object | Kya |
  | --- | --- |
  | **Agent** | definition — model, prompt, tools, guardrails (tumhari rules file + reviewer prompt, translated) |
  | **Environment** | walled space jahan actions execute (harness fences, service-side) — **execution plane, aur ek choice**: vendor cloud sandbox (default) ya self-hosted |
  | **Session** | chalti hui kaam ka tukda — preserved state + append-only event log; **pause, resume, din tak survive** kar sakti hai |
- **Yahan Concept 2 ke 2 planes visible + separable ban jate hain.**
- **2 boundary facts:** managed control plane **vendor-specific** · **Managed Agents ≠ Agent SDK**
  (alag products, code deploy nahi hota).
- **Kya milta hai:** sandboxing/session-state/context-mgmt/prompt-caching (jo operations tum kabhi
  nahi chahte the). **Infrastructure pager unka; business-outcome pager tumhara rehta hai.**
  Behavioral drift **yeh solve nahi karta** — scheduled baseline run apna poora kaam rakhti hai.
- **Kya dena parta hai (halki se bhari):** **Visibility** (service ka event log, machine nahi) ·
  **Custody** (tumhare inputs infra par jo tum control nahi karte — **koi feature list yeh sawal nahi
  badalta**) · **Portability** (definition vendor ki shapes mein — chhorne par **move nahi hoti,
  rewrite hoti hai**).
- **Keemat — nayi kisam ka bill:** runtime khud ka meter (~**8 cents per active session ghanta**,
  idle free) + tokens. Consequence: **bhatakti loop ab paisa bhi kharch karti hai** → **eval suite ek
  cost control bhi ban jaati hai, sirf quality gate nahi.**
- Ghar 3 mein **model AUR harness saath move karte hain** vendor ke schedule par — **defense bilkul
  nahi badalta** (scheduled full-set run, committed baseline, loud alert). **Operations burden
  hataata hai, measurement burden nahi.**

## G. The Move — Suitcase Test

> **Kya suitcase mein jata hai, kya arrival par rebuild hota hai?**

| Travel karta hai (koi software nahi — **decisions, likhi hui**) | Travel NAHI karta (jispar vendor/machine ka naam) |
| --- | --- |
| Spec (job kya, "done" ka matlab) · rubric + anchors · golden set + har case ki `origin` + baselines · ratchet log · maker-checker split, category bars, human gate | flags, output formats · file paths · session state · ek runtime ke API ke against likha code · cost assumptions |

> **Lock-in ka asal jawab:** **tumhara portable asset discipline layer hai, aur uski portability kuch
> aisi hai jo TUM maintain karte ho.** Aadat: **repo truth rakhta hai, har ghar wahin se configure
> hota hai.**

### Trust re-earn hoti hai, transfer nahi — Arrival Protocol

1. Naye ghar mein **poora golden set chalao, sabse pehle** (smoke nahi).
2. **Misses category se parho, count se pehle** (tone down = chhota; injection down naye reachable
   surfaces wale ghar mein = **emergency**).
3. **Bars hold karo, phir naya baseline record karo, ghar ke naam se labeled** (purana baseline
   comparison target rehta hai).
4. **Probation, dependence se pehle** — poora operating cycle + ≥10 successful beats; purana ghar
   available. Result = *"initial operational evidence"*, uptime ka proof nahi.

## H. Ghar Chunna — 4 Sawal (order mein)

| Q | Sawal | Faisla |
| --- | --- | --- |
| **Q1** | **User kaun hai?** | agar jawab **tum** ho → **ghar 2 taqreeban hamesha kaafi**. Jis lamhe **doosre log** (team/client/customer) → Q2 |
| **Q2** | **Kya own karna zaroori hai?** (chahte ho woh nahi) | kuch nahi → managed · sirf execution+data plane → ghar 3 self-hosted sandbox · control plane bhi → owned runtime / SDK / Mode 2 |
| **Q3** | **Kya koi insaan jawab ka wait karta hai?** | scheduled/background (triage, reports) → schedules/managed fit · screen par wait karta insaan → requirements badalta hai (owner nahi — woh Q2 se) |
| **Q4** | **Buri raat ki keemat kya?** | low blast radius → kit pass, jaldi move · high → kit **aur** poori suite (injection all-of-them) **kisi bhi unattended shift se pehle**. **Q4 destination nahi badalta — speed limit set karta hai.** |

- **Ghar permanent loyalty nahi** — har loop ke liye 4 sawalon ka jawab; **healthy system usually
  2–3 gharon mein phaila** (ghar 1 mein banao, ghar 2 mein schedule, ghar 3 se serve jab must
  demand kare). Heavy one-off jobs (quarterly cleanup) ghar 1 mein interactively.
- Mix ko mess banne se ek rule rokta hai: **repo truth rakhta hai, har ghar wahin se set hota hai.**

## I. Staying Honest

- **Lock-in ek RATE hai, event nahi** — leak hota hai: vendor-side tweak jo repo mein mirror nahi
  hui, eval case jo sirf service console mein add hua, bar jo dashboard mein renegotiate hua bina
  commit. Measure: *"agar yeh ghar is quarter gayab ho jaye, move ki keemat kya?"* **Defense: repo
  truth rakhta hai** + quarterly practice run (*"repo se akela ek fresh ghar configure karo"* =
  portability hold-out).
- **Ownership drift hoti hai chahe kuch leak na ho** — *"yeh system measured hai"* → *"yeh system
  theek hai"*. **Discipline mein koi step nahi jo kahe "aur phir yeh khud ko maintain karti hai."
  Scheduled run system ko watch karti hai. Calendar reminder TUMHE watch karta hai.**
- **Koi bhi ghar kya fix NAHI kar sakta:** agent **kitna acha** kaam karta hai. Weak spec Anthropic
  ke cloud par bhi weak. Uncalibrated judge 8 cents/ghanta par bhi uncalibrated. **Runtime decision
  aakhri course isi liye hai — pehli hoti to bekaar hoti.**
- **Aakhri unit:** specified + guarded + measured + housed unit of work → book ki vocabulary mein iska
  naam **Digital FTE**.

---

## Ek-Line Revision (M7)

> Aakhri SPOF = tumhara **hardware** · sort-sawal: **kaun control plane operate karta, kahan execution
> plane** · **4 homes:** session / cloud schedule (sirf clock) / managed runtime (definition hand
> over) / apna process (SDK, Mode 2) · headless = agent as command (already crossed in evals) · ghar 2
> = 6-control unattended kit + escalation TUM tak · green run status ≠ task succeeded · managed: 8
> cents/active-hr, custody+visibility+portability dena parta, drift defense same · **suitcase = spec/
> rubric/golden set/bars (decisions), NOT flags/paths/API code** · trust re-earn hoti hai (arrival
> protocol) · **4 sawal per loop, healthy = 2–3 homes** · lock-in ek rate, repo truth rakhta hai · ghar
> **kitna acha** nahi badalta.

---

## MCQ Practice (jawab neeche)

1. Trilogy ke baad aakhri single point of failure kya hai?
   a) Model b) Tumhara judgment c) Tumhara hardware (laptop khula, session logged in) d) Network

2. Har runtime option ko sort karne wala sawal:
   a) Cost kitni? b) Kaun agent loop operate karta hai, aur kaam kahan execute hota hai?
   c) Kaunsa model? d) Cloud ya local?

3. "Control plane" kya hai?
   a) Sandbox jahan tools chalte hain b) Loop khud — sessions start, model feed, crash par restart
   c) Data jo touch hota hai d) UI

4. Ghar 2 (cloud schedule) mein kya move hota hai?
   a) Poora control plane b) Sirf clock — config (rules/skills/subagents) wahi rehti hai
   c) Execution plane d) Kuch nahi

5. Ghar 3 (managed runtime) mein tum kya hand over karte ho?
   a) Apna data b) Agent ki definition (model, prompt, tools, guardrails) — vendor control plane
   operate karta hai c) Poora repo d) Credentials only

6. Claude Code Routine ka "green run status" kya guarantee karta hai?
   a) Task succeed hua b) Sirf: session infrastructure error ke baghair khatam hua — task succeed
   yeh NAHI c) Output correct hai d) Kuch nahi

7. Desktop app mein "Local" schedule choose karna:
   a) Ghar 2 hai b) Ghar 3 hai c) Ghar 1 timer ke sath — move bilkul nahi (tumhari machine par)
   d) Ghar 4

8. Minimum unattended kit mein "missed-run detection" kyun zaroori hai?
   a) Cost ke liye b) Jo process chali hi nahi woh apni gair-mojoodgi khud report nahi kar sakti
   c) Speed d) Logging

9. Ghar 2 mein escalation channel kahan pohanchna chahiye?
   a) Terminal par b) Desk par c) TUM tak (message, mention, issue jispar tumhara naam) — kyunki tum
   ab wahan nahi baithe d) Email inbox

10. Managed runtime ka bill kis par lagta hai?
    a) Sirf tokens b) ~8 cents per active session ghanta (idle free) + tokens c) Per beat d) Flat monthly

11. Managed runtime behavioral drift solve karta hai?
    a) Haan b) Nahi — scheduled baseline run apna poora kaam rakhti hai; measurement burden nahi hataata
    c) Sirf model drift d) Sirf harness drift

12. "Suitcase test" mein kya travel karta hai?
    a) Flags, file paths, API code b) Spec, rubric+anchors, golden set+bars, ratchet log — decisions
    likhi hui c) Session state d) Cost assumptions

13. Naye ghar par purana eval score (35/36):
    a) Transfer ho jaata hai b) Re-earn karna parta hai — arrival protocol (poora set pehle, category
    se parho, bars hold, probation) c) Delete ho jaata hai d) Automatically +1

14. 4 sawal mein Q1 ("user kaun hai") ka jawab agar "tum" ho:
    a) Ghar 4 chahiye b) Ghar 2 taqreeban hamesha kaafi hai c) Ghar 3 chahiye d) Managed runtime

15. Q4 ("buri raat ki keemat") kya decide karta hai?
    a) Destination b) Speed limit — kitni tezi move karo (destination Q1-Q3 se) c) Model choice
    d) Budget

16. Healthy system kitne gharon mein rehta hai?
    a) 1 (ek endgame ghar) b) 2–3 — har loop ke liye 4 sawal alag c) 4 (sab) d) 0

17. "Lock-in ek rate hai" ka matlab:
    a) Ek dafa ka contract b) Leak hota hai — vendor-side tweaks jo repo mein mirror nahi hote; defense
    = repo truth rakhta hai c) Fixed fee d) Kabhi nahi hota

18. Koi bhi ghar kya fix NAHI kar sakta?
    a) Uptime b) 3am restart c) Agent kitna acha kaam karta hai (weak spec cloud par bhi weak) d) Cost

### Jawab Key

1‑c · 2‑b · 3‑b · 4‑b · 5‑b · 6‑b · 7‑c · 8‑b · 9‑c · 10‑b · 11‑b · 12‑b · 13‑b · 14‑b · 15‑b · 16‑b
· 17‑b · 18‑c

---
[⬅ 06 — Trusting the Checker](06-trusting-the-checker.md) · [Agla: 08 — General Agents on the Web ➡](08-general-agents-on-the-web.md)
