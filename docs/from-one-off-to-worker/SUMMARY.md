# From One-Off to Worker: The Handoff to Manufacturing — Summary

Mode 1 ka aakhri chapter aur Mode 2 ka on-ramp: jab aap ek task ko haath se, baar baar, proven tareeqe se solve kar chuke ho, to usay ek permanent **worker** mein promote kaise karo — scratch se banane ki bajaye.

## 00 — Overview

- **Rule in one line:** "Aap worker scratch se nahi banate. Aap ek proven solution ko promote karte hain."
- Prerequisite: [Problem Solving with General Agents](../problem-solving-crash-course/README.md) aur [Is This an Agent Problem?](../is-this-an-agent-problem/README.md) pehle khatam karna chahiye.
- 4 core bullets: (1) sirf proven solution cross karo, (2) zero se shuru nahi kar rahe — 4 cheezein promote hoti hain, (3) crossing do rasto mein fork hoti hai (own vs manufacture), (4) payoff hai **task vs asset**.
- **Task vs Asset economics:** haath se solve karna = task (har baar time do, result milta hai, time gaya). Worker = asset (ek dafa time do, result baar baar milta hai). Chart analogy: Diego ki line seedhi upar chadhti hai (haath se, saal bhar), Ana ki line ek dafa jump karti hai (build cost) phir flat rehti hai — lines cross hoti hain, us ke baad Ana bohat aage.
- Yehi poori book ka dil hai: labour-as-task se labour-as-asset shift.

## 01 — The Signal: Kya Yeh Ready Hai Cross Karne Ke Liye?

- Rokti hai galti: proven na hone wale task ko permanent bana dena = ek hafta ghalat cheez banane mein waste, phir dobara banana.
- Gate 2 (pichle chapter se) signal ka pehla aadha deta hai: **often + same shape + worth it**.
- Doosra aadha (asli test): *kya aap ne isay abhi tak achhi tarah solve kiya hai?* — pichli teen baar same tareeqe se kiya?
- Agar method abhi bhi badalta hai → stable shape nahi mili → Mode 1 mein rehna chahiye.
- **Repetitions research hain, waste nahi:** har baar solve karte waqt edge case, behtar step order, ya important check milta hai. Week-1 worker sab miss karega; Week-5 worker hard-won knowledge par khara hoga. Cross karo jab learning slow ho jaye, pehle nahi.

## 02 — Reframe + The Four Promotions

- **Reframe:** har achhi Mode 1 session ek "trail" chhorti hai — brief, output shape, check, saved result — yehi worker ka raw material hai. Manufacturing = **Harvest** (pieces uthao) + **Harden** (har piece ko itna mazboot karo ke worker ke bina chal sake). Hardening asli engineering kaam hai.
- **4 Promotions table:**
  1. **Brief → Spec** — teen-line brief (works from / want at end / done when) ek likha hua document banta hai jo worker har run parhta hai. (Seekho: Spec-Driven Development)
  2. **Apna check → Eval** — khud verify karna saved example inputs + known-good answers ban jata hai; worker ke results automatically grade hote hain. (Seekho: Eval-Driven Development)
  3. **Aap loop mein → Exits design** — worker khud steps chalata hai; edges ke liye pehle se decide karna hai kab escalate karna hai, kisko, kis info ke sath. Shape: routine handle karo, exception escalate karo. (Seekho: Build AI Agents · Digital FTE)
  4. **Session → Runtime** — worker ko aapke bina exist karna hai; usay ek runtime chahiye jo usay zinda rakhe aur memory persist kare. (Seekho: Deploy the Agent Harness)
- **Kya carry hota hai, rebuild nahi hota:** Plugins — skills (packaged know-how) aur connectors (data/app links) open, cross-runtime formats par bane hote hain, isliye claude.ai, general agents, personal harnesses, aur manufactured workers sab mein carry hote hain.
- Research references: **Fred Brooks**, *The Mythical Man-Month* (1975) — "plan to throw one away — you will, anyway" (repeated Mode 1 solves = woh throwaway experiment). **Lisanne Bainbridge**, *Ironies of Automation* (1983) — jitna reliable automation hota hai, insaan ke rare interventions utne hi important/mushkil ho jate hain — isliye Promotion 3 exits ke baare mein hai, routine ke baare mein nahi.

## 03 — The Fork: Do Tareeqe Permanent Banane Ke

- **Own It — Personal Harness:** worker sirf aap ke liye (inbox, code, errands) → halka rasta. Spec = aapki notes, eval = muthi bhar examples, escalation = worker aapko message kare. Seekho: Personal Agent Harnesses (OpenClaw, Hermes).
- **Manufacture It — Digital FTE:** worker organization ke liye, dusre log rely karenge, governed/scale hona chahiye → 4 promotions **rigorously**: spec shared/reviewed, eval team ka trust kiya hua gate, escalation named human/team ko, runtime real production infra. Yehi poora Mode 2 — Manufacturing track hai.
- **Faisla karne wala sawal:** Worker kiske liye hai, aur kaun rely karta hai?
- 2026 table: Own it → OpenClaw/Hermes (open-source, khud chalao). Manufacture it → OpenAI Agents SDK ya managed Claude agent setup.
- General agent (Claude Code, OpenCode, Cowork, OpenWork) gayab nahi hota — dono rasto par yehi tool hai jisse worker banate/install karte ho.
- **Running cost note:** durable worker API par chalta hai (metered, per-call pay) — dono rasto par sach, chahe personal harness ho ya Digital FTE. Yeh claude.ai subscription/free-tier se alag hai.
- **Teesra mode nahi hai:** Ownership (aapka vs organization ka) aur Mode (ek dafa solve vs lasting banao) do alag sawal hain — koi bhi mode kisi bhi owned harness par chal sakta hai.

## 04 — Ana Ka Blueprint + Practice Exercise

- **Ana ka bhara hua blueprint** (Monday support-message task): Spec = teen-line brief (parho, group karo — complaint/question/order/other, summary likho); Eval = 12 pehle se haath-sorted messages jo instructions badalte hi test hoti hain; Exits = unhandled language ya limit-se-zyada refund par worker flag+ping karta hai; Runtime = har Monday ek chota always-on machine par khud chalta hai, apni list rakhta hai.
- **Practice Exercise — 3 steps:**
  1. Kya proven hai? (pichli teen baar same method?)
  2. 4 Promotions, har ek ek line mein (Spec, Eval, Exits, Runtime)
  3. The Fork — sirf aap ke liye ya organization ke liye?
  - Grading focus: form/concreteness par, task "achha" hai ya nahi us par nahi. Key tests: genuinely proven task, real specific exit case, concrete (vague nahi) promotions.
- **Aage kahan jana hai (Mode 2 — Manufacturing track):** Python in the AI Era, Build AI Agents, Eval-Driven Development, Building a Digital FTE, Deploy the Agent Harness.
