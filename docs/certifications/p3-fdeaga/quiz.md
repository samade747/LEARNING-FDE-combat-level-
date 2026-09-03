# P3-FDEAGA — Full Mock (60 Questions, Mixed)

*Timing target: 60 Q in ~85 min (real exam ~1.4 min/Q). Answer key + short rationale sab se neeche.
Yeh module MCQ sets ke upar hai — scenario-heavier, cross-module.*

---

### Part 1 — Roles & Ecosystem (Q1–16)

**1.** Ek company Claude Code deploy karti hai, har engineer ka output ~5x barh jaata hai, aur ab woh
shikayat karti hai ke "humein zyada product managers chahiye". Book is situation ko kya kehti hai?
a) PM shortage b) **Intent bottleneck — building scale hui, deciding-what-to-build nahi; Outcome
Architect sabse ahm seat ban jaati hai** c) Hiring freeze d) Over-automation

**2.** Ek engineer Palantir se resign karta hai. Book ka graduate ek client se doosre client jaata
hai. Structural farq jab woh move karte hain?
a) Salary b) **Palantir engineer ke jaate hi platform/leverage vendor ke paas reh jaati hai; graduate
apna method + vertical SoR sath le jaata hai** c) Title d) Koi farq nahi

**3.** MIT NANDA report ka ~95% figure kya batata hai?
a) AI models kaam nahi karte b) **~95% custom enterprise AI pilots ka koi measurable return nahi —
integration into messy real systems, AI nahi** c) 95% FDEs fail d) 95% companies AI use nahi kartin

**4.** Vendor-neutral FDE "dev shop of one" objection ka jawab kaunsi 2 cheezon se deta hai?
a) 2 models b) **The method (diya gaya, identical) + the profession/vertical SoR (khud banaya)**
c) 2 clients d) Code + docs

**5.** "Build first, sell second" kis ladder ko govern karta hai?
a) Service ladder b) **Vertical ladder — slice customer ka intezar nahi karti, woh customer paida
karti hai** c) Dono d) Koi nahi

**6.** Layer 4 "contract of success" ke 3 elements:
a) Price, timeline, scope b) **Baseline + target + acceptance criteria** c) Model, tool, runtime
d) Corpus, map, reflexes

**7.** "The One Law of the FDE AF Model":
a) Sab kuch promote hota hai b) **Jo kuch ek layer par repeat ho usay neeche wale layer mein
promotion ke liye evaluate karo** c) Customer decide karta hai d) Kuch promote nahi hota

**8.** Domain knowledge ke 3 forms mein — agent ko ek KYC section "action lene se pehle" parhna
zaroori hai. Yeh kahan specify hota hai?
a) Corpus b) **Map (always-available skill jo batata hai kab kaunsa source zaroori)** c) Reflex
d) Rules file

**9.** "Corpus vs skill" ka test:
a) Size b) **Find + cite → corpus; load + follow to do the task → skill** c) Age d) Format

**10.** SoR ke 3 scopes — "Postgres, pgvector, MCP, auth" kaunsa hai?
a) Kernel b) Instance c) **Machinery** d) Corpus

**11.** 80/20 split aur 10-80-10 rule:
a) Same b) **80/20 = product divide (shared core + customization); 10-80-10 = ek task divide
(intent/execute/judgment) — nest karte hain** c) Dono task d) Dono product

**12.** Ecosystem wiring mein "gateways" ka design:
a) Thick — saara logic b) **Thin — sirf decide karte hain audience kya reach kare; real functionality
ek layer neeche** c) Har audience ki apni DB d) Optional

**13.** Zia Tutor AI ki 4 records mein "Learner Record":
a) SoR khud b) Zia ki voice c) **Tumhara goal, kya demonstrate kiya, agla step** d) Tumhara background

**14.** Anthropic FDE role ko kya title deta hai?
a) FDE b) Solutions Engineer c) **Applied AI Engineer** d) Deployment Architect

**15.** Book fine-tuning ke baare mein:
a) Default b) Kabhi nahi c) **Last resort — sirf jab prompting/context/tools/retrieval kam pad
jayein; foundation-model pre-training out of scope** d) Sirf Architect track

**16.** Cherny ke 5 archetypes ke baare mein sahi:
a) Job titles hain b) Har banda exactly ek c) **Titles se bandhe nahi; zyada tar log 2–3 span karte
hain; mix product phase se badalta hai** d) Sirf engineers

---

### Part 2 — Local AI & Agentic Coding (Q17–24)

**17.** Local se cloud jaate waqt kya badalta hai?
a) Harness b) **Sirf address** c) Dono d) Verification loop

**18.** Ek local model tool calls "mangle" karta hai — plain text bhejta hai JSON ke bajaye. Yeh
kaunsi wall hai aur fix?
a) Throughput — GPU b) **Capability — strong/tool-use-trained model (hardware se fix nahi)** c) Cost
d) Context window

**19.** Ollama loop mein context chup-chaap trim ho raha hai. Kyun?
a) Model chhota b) **Default context sirf 4,096 tokens — `num_ctx` barhao** c) GPU kam d) Bug

**20.** vLLM ek single user ke liye kya karta hai?
a) Bahut tez b) **Ek user ke liye tez nahi — load ke neeche machine ko tez karta hai** c) Slow
d) Kuch nahi

**21.** Agentic coding course kis discipline ka full treatment hai?
a) Prompt engineering b) **Context engineering (model kya dekhe)** c) Model training d) DevOps

**22.** Karpathy ki "trust" wali baat:
a) Poora bharosa b) Kabhi nahi c) **Utna hi trust jitna output check ho sake → verification loop
(Attempt→Check→Fix→Repeat, no human)** d) Sirf tests

**23.** Hook kis se likhwana chahiye?
a) Model se b) **Khud paste karo — warna model apni hi rule follow karke safety check defeat kar
sakta hai** c) Koi farq nahi d) CI se

**24.** MCP server add karne se pehle asal sawal:
a) Free hai? b) **"Standing connection ke qabil hai, ya agent seedha call kar sakta hai?"** c) Popular
hai? d) Anthropic ka hai?

---

### Part 3 — Loop Engineering (Q25–34)

**25.** Ek loop har subah 9am chalti hai lekin har run zero se shuru hoti hai, kal ka kaam yaad nahi.
Kaunsa part missing hai?
a) Heartbeat b) Skill c) **Spine (state/memory) — no spine, no loop; pehla step hamesha repeat**
d) Connector

**26.** Maker-checker rule:
a) Ek agent sab kare b) **Jo agent kaam banata hai woh apna kaam khud approve nahi kar sakta**
c) Human har baar d) Tests kaafi

**27.** `/goal` ka checker kya kar sakta hai?
a) Commands chala sakta hai b) **Sirf dikhta transcript/output parh sakta hai — isliye condition
command-provable ho + `show me both`** c) Files edit d) PR khol sakta

**28.** Conditional (run-until-done) loop ke 3 zaroori stops:
a) Start/middle/end b) **Success condition + limit + no-progress check** c) Heartbeat/spine/checker
d) Prompt/repo/trigger

**29.** In-session `/loop` ka timer kahan?
a) Cloud b) **Tumhari open session ke andar — session band, loop khatam** c) Scheduler d) GitHub

**30.** "Human out of the loop" kaise banta hai?
a) Design decision se b) **Drift se — diffs parhna band, green checkmarks par trust, review skip → "on"
chup-chaap "out" ban jaati hai** c) Vendor default se d) Kabhi nahi

**31.** Loop mein connector writes kaisi honi chahiye?
a) Blind "create" b) **Idempotent — "update-or-create" (retry par duplicate na bane)** c) Read-only
d) Batched

**32.** Loop ki asal cost sabse zyada kis se badalti hai?
a) Model size b) **Frequency (har-5-min vs 5/din ≈ 100x)** c) Prompt length d) Repo size

**33.** Loop error message kaisa hona chahiye?
a) Chhota b) **Agla step bataye ("request the repo scope") — warna ek beat waste** c) Error code
d) Stack trace

**34.** Andrew Ng ka "context advantage":
a) Bara context window b) **Tum woh jaante ho jo agent nahi — kaun use karega, kya chahiye, "achha"
kaisa** c) Training data d) Compute

---

### Part 4 — Harness Engineering (Q35–44)

**35.** Loop aur Harness ka farq:
a) Same b) **Loop = kab chalta + kya yaad; Harness = ek beat ke andar allowed/known/proven/on-error**
c) Loop naya d) Harness = scheduler

**36.** 5 verbs mein "insaan ko visibly bhejna":
a) Constrain b) Verify c) **Escalate** d) Inform

**37.** Permission buckets kis se sort karne chahiyen?
a) Frequency b) **Blast radius (galat ho to kitna nuksan)** c) Alphabetical d) Cost

**38.** `Bash(rm -rf *)` deny rule `rm -fr` ya Python one-liner ko rokegi?
a) Haan b) **Nahi — text match karti hai, matlab nahi; tripwire hai, asli deewar sandbox** c) Sirf
Claude Code d) Haan auto mode mein

**39.** "Tool poisoning" kya hai?
a) Bug report mein command b) **Attack tool ki apni description/metadata mein chupa (jo agent decision
ke waqt trust karta hai)** c) Slow tool d) Duplicate tool

**40.** Hook ko "harness part" kya banata hai?
a) JSON b) **"Refuse" — agent skip/argue/bhool nahi sakta; harness chalati hai model nahi** c) Exit
code d) Speed

**41.** Typed reviewer verdict malformed aa gaya. Harness kya kare?
a) Hamesha retry b) Guess kar le c) **Escalate (verb 5) — visibly** d) Ignore

**42.** "Hard failure" (missing permission) ka recovery jawab:
a) Retry with backoff b) **Retry mat karo — wahi call hamesha fail degi; skip/escalate** c) Checkpoint
resume d) Ratchet

**43.** 4 failure classes ki mapping:
a) **Context→Inform, Constraint→Constrain, Verification→Verify, Planning→Structure(loop)** b) Sab
Verify c) Sab prompt d) Context→Constrain

**44.** "Rule debt" ka fix:
a) Zyada rules b) **Monthly review — 90 din se na-fire + koi linked incident nahi → removal candidate
(secrets ki deewarein exempt)** c) Kabhi delete mat karo d) Sirf hooks

---

### Part 5 — Trusting the Checker (Q45–52)

**45.** Test aur Eval ka farq:
a) Same b) **Test = ek property verify; Eval = repeated runs par behavior estimate (pass rate)**
c) Eval tez d) Test AI ke liye

**46.** Ek output-only eval ek mahine se pass ho raha hai. Raat ko agent ne function mein expected
value **hard-code** kar diya — jawab perfect lagta hai. Kaunsi depth pakregi?
a) Depth 1 (answer) b) **Depth 2 (actions — judge diff parhta hai)** c) Depth 3 only d) Koi nahi

**47.** "Bar nahi hili. Ruler hili." — kaunsi judge failure mode?
a) Leniency drift b) Surface bias c) **Drift — judge model neeche se update ho gaya** d) Self-preference

**48.** Golden set cases kahan se aane chahiyen?
a) Model invent kare b) **Ratchet — real caught failures pehle (reachable prove ho chuki)** c) Random
d) Docs se

**49.** "Grade the grader" mein sabse zaroori cell:
a) Correct pass b) False fail c) **False pass — bura kaam jo judge ne approve kiya; yehi ship hota hai**
d) Correct fail

**50.** Judge se disagree karne par pehla fix:
a) Model badlo b) **Rubric fix karo (unanchored score, no findable-answer question) — model sirf tab
jab acha rubric bhi gap na bhare** c) Judge hata do d) Bar giraо

**51.** Committed eval baseline bina explicit approval kis direction ja sakta hai?
a) Neeche b) **Upar — neeche jane ke liye explicit written approval (kisne, kyun)** c) Dono d) Koi nahi

**52.** 2 mahine baad tuned set 36/36 par chal raha hai lekin **hold-outs 90% → 70%** gir gaye. Kuch
maliciously nahi badla. Kya hua?
a) Model regression b) **Goodhart's law — system dheere dheere test seekh gaya jab general behavior
drift kar gaya** c) Bug d) Rubric error

---

### Part 6 — Leaving the Laptop & General Agents Web (Q53–60)

**53.** Trilogy ke baad aakhri single point of failure:
a) Model b) Judgment c) **Tumhara hardware (laptop khula, session logged in)** d) Network

**54.** Ayesha ki invoicing loop laptop se chalti hai; load-shedding shamon ko power kaat deti hai;
naya client 6pm daily invoices chahta hai bina fail. Kaunsa ghar pehle chahiye?
a) Ghar 1 b) **Ghar 2 (cloud schedule) — masla sirf clock hai; + minimum unattended kit** c) Ghar 3
d) Ghar 4

**55.** Claude Code Routine ka "green run status" kya guarantee karta hai?
a) Task succeed hua b) **Sirf: session infrastructure error ke baghair khatam hui — task succeed yeh
NAHI** c) Output correct d) Kuch nahi

**56.** "Suitcase test" mein kya travel karta hai?
a) Flags, paths, API code b) **Spec, rubric+anchors, golden set+bars, ratchet log — decisions likhi
hui** c) Session state d) Cost assumptions

**57.** Ghar 3 (managed runtime) — bhatakti hui loop ab kya kharch karti hai?
a) Sirf waqt b) **Paisa bhi (~8c/active-hr) — isliye eval suite ek cost control bhi ban jaati hai**
c) Kuch nahi d) Sirf tokens

**58.** Chat box aur agent surface ka test:
a) Speed b) **"Agar main type karna band kar doon, kya kaam ruk jayega?" (chat=haan, surface=nahi)**
c) Cost d) Model

**59.** Ek lawyer web session mein comparison memo banata hai aur platform link client ko share karta
hai. Do galtiyan mein se ek:
a) Model galat b) **Custody — memo sirf Tier 2 (vendor platform) mein exist karta hai, firm ke record
mein hole; fix = Tier 3 (DMS mein save)** c) Prompt chhota d) Connector missing

**60.** Ayesha 2 cheezein schedule karna chahti hai: (a) Monday summary of unpaid invoices (Drive se
parhna), (b) Friday automatic reminder emails late clients ko. Kaunsi abhi safe hai?
a) Dono b) **Sirf (a) — reporting schedule; (b) "acting" hai, real clients ko email karti hai
unattended → Loop Engineering chahiye** c) Sirf (b) d) Koi nahi

---

## Answer Key

| Q | A | Q | A | Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | b | 11 | b | 21 | b | 31 | b | 41 | c | 51 | b |
| 2 | b | 12 | b | 22 | c | 32 | b | 42 | b | 52 | b |
| 3 | b | 13 | c | 23 | b | 33 | b | 43 | a | 53 | c |
| 4 | b | 14 | c | 24 | b | 34 | b | 44 | b | 54 | b |
| 5 | b | 15 | c | 25 | c | 35 | b | 45 | b | 55 | b |
| 6 | b | 16 | c | 26 | b | 36 | c | 46 | b | 56 | b |
| 7 | b | 17 | b | 27 | b | 37 | b | 47 | c | 57 | b |
| 8 | b | 18 | b | 28 | b | 38 | b | 48 | b | 58 | b |
| 9 | b | 19 | b | 29 | b | 39 | b | 49 | c | 59 | b |
| 10 | c | 20 | b | 30 | b | 40 | b | 50 | b | 60 | b |

**Scoring:** 42/60 = 70% (pass line). 48+/60 comfortable. Jo galat hue, us module ki cram sheet ka
woh section dobara parho.

---
[⬅ P3-FDEAGA Index](README.md) · [Night-Before One-Pager](SUMMARY.md)
