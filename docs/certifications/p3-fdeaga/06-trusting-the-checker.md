# 06 — Trusting the Checker (Evals)

*Source: `trusting-the-checker-crash-course` (Zia Tutor AI, corpus gen 62). Deep notes:
[`docs/trusting-the-checker/`](../../trusting-the-checker/README.md).*

> **Trilogy:** Loop ne agent ko **waqt** diya · Harness ne **limits** diye · **Evals** usay ek
> **track record** dete hain. Loop: rubric score *"a claim, not a proof."* Harness: *"a harness
> change without a re-run eval is a guess."* Yeh course woh qarz chukati hai.

---

## A. Test vs Eval (definition MCQ — hamesha aata hai)

| | **Test** | **Eval** |
| --- | --- | --- |
| Kya | ek **specific expected property** verify karta hai (ye input → wo output) | estimate karta hai ke **probabilistic system representative cases mein kitna achha perform karta hai, usually repeated runs par** |
| Repeatability | dobara chalao → same jawab → green result mein real info | agent same task 2 baar → 2 alag runs; **ek green run agli run ke baare mein kuch nahi batati** |
| Analogy | machine se ek sawal, ek sahi jawab | ek worker ko kai shifts par judge karna — **ek shift par nahi** |
| Starting metric | — | **pass rate** — har case kai baar chalao, kitni baar pass hui grade karo |

> **"Demo mein chala" sabse kamzor evidence hai** — demo = ek run, demo-friendly task, kisi ke
> dekhte hue. 95% steps × 20 = ~36% clean finish → koi bhi clean demo aisi system se aa sakti hai jo
> zyada tar real tasks mein fail hoti hai.

## B. Ek Run Ki 3 Depths

| Depth | Kya parhta hai | Kya pakarta hai | Kya miss karta hai |
| --- | --- | --- | --- |
| **1 — Answer** | agent ne akhir mein kya kaha/produce kiya | galat jawab, broken format, ghadi hui claims | **har failure jo "sahi lagta hai"** (jaise hard-coded expected value) |
| **2 — Actions** | kaunse tools, kaunse args, kis order | galat file edit, galat command; **deleted-test failure yahan** (suite green, **diff** se pata) | process problems |
| **3 — Trace** | poora run: messages, tool calls order, retries, visible rationale | **bura process** jisne is dafa sahi kiya, agli dafa nahi | — |

- Teeno disk par already: answer = output · actions = diff+log · trace = session transcript.
- **Sasti cases depth 1 grade karti hain. Bachane wali cases depth 2 aur 3 grade karti hain.**
- **Ehtiyat:** visible rationale = evidence ki agent ne **kya kiya** — reliable window **nahi** ki woh
  **kya soch raha tha**.

## C. Judge Bhi Ek Model Hai — LLM-as-Judge Ke Failure Modes

| Failure mode | Kya |
| --- | --- |
| **Leniency drift** | borderline kaam pass karne lagta hai, khaas kar vague rubric par |
| **Self-preference** | apni family ke output ko narmi se grade karta hai |
| **Surface bias** | lamba/confident/well-formatted zyada score — **costume grade karta hai, kaam nahi** |
| **Drift** | judge model neeche se update ho jaata hai — kal ka 95 aaj ka 95 nahi. **"Bar nahi hili. Ruler hili."** |

> Yeh model judges ko bekaar nahi banata — **instruments jinhe calibration chahiye**, kisi bhi
> measuring device ki tarah. Judge = ek employee jo doosron ko grade karta hai — usay bhi performance
> review chahiye.

## D. Golden Set

### Concept 4 — har pakri failure ek case ban jaati hai

- Test cases **invent mat karo** — invented cases sirf woh test karti hain **jo tumne imagine kiya**.
- Sahi source = **ratchet**. Ratchet **harness** ko fix karta hai; **eval case prove karta hai fix
  hamesha kaam kar raha hai** — har future change par.
- **3 sourcing rules:**
  1. **Failures pehle** — real caught failures sabse valuable (woh **reachable prove ho chuki**).
  2. **Categories cover karo, volume nahi** — **20–40 cases**, difficulty mein phaili (kuch easy, ek
     solid middle, hard). **100 easy cases kuch measure nahi karti.**
  3. **Folder ko version-control karo** — golden set code hai (review, date, blame).

### Concept 5 — case ki shape + runner

- Case JSON: `case_id`, `category`, `judge_reads`, `input_diff`, `expected {verdict, risk}`,
  `must_mention`, `unacceptable`, `difficulty`, **`origin`** (us failure ki taraf point jisne isay
  kamaya).
- **Runner = koi framework nahi** — ek loop, har case ke liye **3 runs**, `jq` grade karta hai.
- **3 zaroori details:**
  1. **Reviewer verdict file mein likhta hai, runner file grade karta hai** (`claude -p` prose
     summary deta hai jab subagent ko delegate kare, raw JSON nahi).
  2. **Errors aur fails alag count** — protocol tootna (harness bug) ≠ galat judge karna (calibration
     finding).
  3. **Read-only** — sirf fixture parhne + ek verdict file likhne ki permission (fixtures injection
     cases ho sakti hain).
- **Eval suite = 3 chhoti cheezein:** cases folder + runner script + `jq` grade. **Koi framework
  nahi.**

## E. Calibrating the Judge

### Concept 6 — rubric = "achha" ki spec

- Bina rubric judge **mood** se grade karta hai.
- **Har score ko example se anchor karo** — *"4 = mostly correct"* kuch constrain nahi karta;
  *"4 = action aur amount sahi, timeline vague"* sab constrain karta hai. Best anchors **apni pichli
  runs** se (real 5, real 3, real 1 paste karo).
- **Judge se facts check karwao, impressions nahi** — *"ye jawab acha hai?"* surface bias invite
  karta hai; *"kya diff koi test hataata hai? kya fix sirf named function touch karta hai?"* = findable
  answers → judge ko **kaam parhne** par majboor.
- **Bar (threshold) = ek decision, discovery nahi.** Har category ke liye alag — miss ki cost poochो:
  false-green → *"sab, hamesha"*; tone-and-style → 8/10 theek.

### Concept 7 — grader ko grade karo (course ka naam isi par)

1. **20 graded items sample karo** — deliberately FAILs + borderline (sirf easy PASSes nahi). Judge
   ke verdicts chupao.
2. **Blind grade karo**, wahi rubric, peek se pehle likho.
3. **Compare + disagreements sort karo (count nahi):**

   | | Judge: PASS | Judge: FAIL |
   | --- | --- | --- |
   | **Tum: PASS** | correct pass | false fail |
   | **Tum: FAIL** | **false pass** ⚠️ | correct fail |

   **Sabse zaroori cell: false pass** — bura kaam jo judge ne approve kiya → **yehi ship hota hai.**
   PASS-heavy sample par 9/10 agreement ho sakta hai jabke judge har zaroori FAIL miss kar raha ho.
   **Rough guide:** overall >9/10 **aur** high-severity par **zero false passes**.
4. **Judge se pehle RUBRIC fix karo** — zyada tar disagreement rubric ki galti (unanchored score,
   koi findable-answer sawal nahi). Model **sirf tab** badlo jab acha rubric bhi gap na bharе.

- **Calibration score** = judge ka pass rate sirf **tumhare judgment** ke golden set par. Judge model
  badle → protocol dobara. **Tum reference ho, gold standard nahi** — high-stakes ke liye 2 log
  independent grade karein / domain expert.

## F. Evals in the Loop

### Concept 8 — regression suite

- **Golden set hi harness ki regression suite hai.** Rule: **system mein koi bhi change** (naya deny
  rule, edited rules file, reworded reviewer prompt, model swap) **set ko ship se pehle dobara
  chalata hai**, rate baseline se compare.
- Shared repos → **CI** job har PR par jo harness files touch kare; branch protection require kare.
  Committed `evals/baseline.json`.
- **Re-baseline karo jab set khud badle, usi commit mein.** Naya hard case rate ko **sahi wajah se**
  girata hai (suite sakht hui). **2 controls:** baseline sirf **neeche** ja sakta hai explicit
  written approval ke sath (kisne, kyun); purana baseline history mein.

### Concept 9 — drift ("zameen hilti hai")

- Code regression ki wajah hoti hai. Agent behavior ka **doosra failure channel** jiski **koi local
  wajah nahi**: **niche wala model update ho gaya.** Same prompt/rules/sab kuch — behavior alag.
- **Defense = scheduled measurement (yeh bhi ek loop hai):** poora set schedule par (active loops
  nightly, quiet weekly) · baseline commit + drops par alert (**chup = "abhi bhi baseline par"**) ·
  model change par judge dobara calibrate.

### Concept 10 — numbers parhna

- **Panic se pehle dobara chalao** — agents distributions hain; chhoti girawat noise ho sakti hai.
  Sirf newly-failing cases ko kuch baar aur chalao. **Real regression consistently fail; noise re-run
  par pass.** Policy: result dekhne se **pehle** decide karo, har attempt record. **Flakiness jo bani
  rahe khud ek finding hai** (2/3 pass = behavior genuinely unstable).
- **3 runs per case = development setting** (smoke signal, stable estimate nahi). 3-of-3 ≠ 100%.
  Sample ko decision ke barabar scale karo.
- **Konse cases fail hue pehle parho** — 31/36 mein 3 tone cases = koi baat nahi; 35/36 mein
  `deleted-test-001` = **emergency**. Isi liye cases **categories** carry karti hain.
- **Suite ko cost se tier karo:** **smoke set** (5–6 highest-stakes) har change par · **full set**
  nightly · **hold-outs** weekly.

## G. Staying Honest

### Concept 11 — Goodhart's Law

> **Jab ek measure target ban jaata hai, woh achha measure hona band kar deta hai.**

Jis lamhe *"suite ko 33/36 se upar rakho"* goal bane, sab kuch unhi 36 verdicts ke liye optimize hone
lagta hai. **Suite abhi bhi pass hoti hai — bas ab uska matlab kuch nahi.**

**3 defenses (sab sasti):**
- **Hold-outs** — chand cases jo authors **kabhi tune nahi karte**, sealed, sirf weekly. Tuned set aur
  hold-outs ke beech gap khulna = Goodhart khud ko dikha raha hai (**tum test seekh rahe ho, material
  nahi**).
- **Production se refresh** — naye real failures naye cases; ratchet pipeline kabhi nahi rukta.
  Retirement sakht: case sirf tab retire jab woh behavior exist na kare / requirement badal jaye.
  **High-severity (false greens, injections) permanently rehti hain.**
- **Agent ko kabhi answer key na dikhao** — cases/fixtures loop ki working context se bahar (na rules
  file, na maker skill). **Safety:** attack fixtures = **live ammunition** — answer-key-chupane wala
  rule fixtures par bhi.

### Concept 12 — evals kya PROVE nahi kar sakte

> **Calibrated 35/36 = known territory ke baare mein strong statement + unknown territory ke baare
> mein total khamoshi.**

Eval suite confidence sirf un situations par bound karti hai jo **usmein hain** — genuinely novel
input, folder mein kisi jaisi nahi failure, woh din jab duniya set ke refresh se tez badle — inpar
kuch nahi. **Isi liye kisi course ne human gate nahi hataya.** *Evals woh kaam karte hain jo gate tak
pohanchta hai + woh sharpen karte hain jo gate dekhta hai — us insaan ki jagah nahi lete jo gate par
khara hai.*

- **Bridge to Mode 2:** yehi ideas **Eval-Driven Development** mein scale hoti hain — 3 depths →
  nine-layer pyramid, case folder → DeepEval golden datasets, transcript judge → trace grading,
  scheduled Routine → Phoenix (production watching). **Har concept transfer, sirf tooling badhti hai.**
- **Managed option:** **Rubrics in Claude Managed Agents** (beta) — rubric-with-a-bar as platform
  feature; alag grader agent. **Managed judge bhi phir bhi ek model hai** — Concept 7 calibration
  chahiye, aur insaan ko bar choose karna hai.

---

## Ek-Line Revision (M6)

> Test = ek property; **Eval = repeated runs par behavior estimate (pass rate)** · "demo mein chala"
> sabse kamzor evidence · 3 depths: answer / actions (deleted-test yahan) / trace · **judge bhi model
> hai** — leniency drift, self-preference, surface bias, drift ("ruler hili") · golden set: **failures
> pehle, categories not volume, version-control** · rubric = anchored examples + fact questions ·
> **grade the grader** — sabse zaroori cell **false pass** · har system change → regression suite
> re-run · drift = niche model update, scheduled measurement se pakdo · **Goodhart** → hold-outs +
> refresh + hide answer key · evals known territory par strong, unknown par khamosh — **gate nahi
> hataate**.

---

## MCQ Practice (jawab neeche)

1. Test aur Eval ka farq:
   a) Same b) Test = ek property verify; Eval = repeated runs par behavior estimate (pass rate)
   c) Eval tez hai d) Test AI ke liye

2. "Ek green agent run" agli run ke baare mein kya batati hai?
   a) Sab kuch b) Kuch nahi — agent har baar alag run kar sakta hai c) 95% confidence d) Pass rate

3. Deleted-test failure kaunsi depth pakarti hai?
   a) Depth 1 (answer) b) Depth 2 (actions — diff parhna) c) Depth 3 only d) Koi nahi

4. Visible rationale kya evidence hai?
   a) Agent kya soch raha tha b) Agent ne kya kiya — NA ki woh kya soch raha tha c) Future behavior
   d) Pass rate

5. Judge ka "surface bias":
   a) UI ka rang b) Lamba/confident/well-formatted zyada score — costume grade karta hai kaam nahi
   c) Slow grading d) Self-preference

6. "Bar nahi hili, ruler hili" kis failure mode ko describe karta hai?
   a) Leniency drift b) Surface bias c) Drift — judge model neeche se update ho gaya d) Self-preference

7. Golden set cases kahan se aane chahiyen?
   a) Model invent kare b) Ratchet — real caught failures pehle (reachable prove ho chuki)
   c) Random d) Documentation se

8. Golden set ka size + shape:
   a) 100+ easy cases b) 20–40 cases, difficulty mein phaili, categories cover — volume nahi
   c) Sirf hard cases d) 5 cases

9. Runner mein "error" aur "fail" alag kyun count hote hain?
   a) Cosmetic b) Protocol tootna (harness bug) ≠ galat judge karna (calibration finding)
   c) Speed d) Cost

10. "Grade the grader" mein sabse zaroori cell:
    a) Correct pass b) False fail c) False pass — bura kaam jo judge ne approve kiya, yehi ship hota hai
    d) Correct fail

11. Judge se disagree karne par pehla fix kya?
    a) Model badlo b) Rubric fix karo (unanchored score, no findable-answer question) — model sirf tab
    jab acha rubric bhi gap na bhare c) Judge hata do d) Bar giraо

12. Golden set = harness ki kya hai?
    a) Documentation b) Regression suite — har system change ship se pehle re-run c) Backup d) Config

13. Committed baseline kis direction mein ja sakta hai bina approval?
    a) Neeche b) Upar — neeche jane ke liye explicit written approval (kisne, kyun) chahiye
    c) Dono d) Koi nahi

14. "Drift" ki wajah kya hai (regression ke muqable)?
    a) Kisi ne code badla b) Niche wala model update ho gaya — koi local wajah nahi
    c) Rubric badla d) Bar badla

15. Eval rate gir gayi — pehla kadam?
    a) Panic + rollback b) Newly-failing cases ko dobara chalao (real regression consistently fail;
    noise re-run par pass) — policy pehle decide karo c) Model badlo d) Cases delete karo

16. Goodhart's Law:
    a) Zyada measure = behtar b) Jab measure target ban jaye, woh achha measure hona band kar deta hai
    c) Measure kabhi galat nahi d) Targets zaroori hain

17. Goodhart ke against "hold-outs":
    a) Zyada cases b) Cases jo authors kabhi tune nahi karte, sealed, weekly — tuned set se gap khulna
    = test seekh rahe ho material nahi c) Backup baseline d) Extra runs

18. Evals human gate ke baare mein:
    a) Replace kar dete hain b) Gate tak pohanchne wale kaam ko karte hain + gate dekhne wale ko
    sharpen karte hain — insaan ki jagah nahi lete c) Optional bana dete hain d) Sirf CI mein

### Jawab Key

1‑b · 2‑b · 3‑b · 4‑b · 5‑b · 6‑c · 7‑b · 8‑b · 9‑b · 10‑c · 11‑b · 12‑b · 13‑b · 14‑b · 15‑b · 16‑b
· 17‑b · 18‑b

---
[⬅ 05 — Harness Engineering](05-harness-engineering.md) · [Agla: 07 — Leaving the Laptop ➡](07-leaving-the-laptop.md)
