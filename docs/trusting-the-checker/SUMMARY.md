# Trusting the Checker — Summary

Loop → Harness → Graph → **Trusting the Checker** (position #11): yeh chapter sikhata hai ke apne
checker/reviewer par "PASS" ke bharose ko ek measured, defended number kaise banaya jaye — **evals**
discipline, framework/dashboard ke bagair, sirf chhoti files + shell script + `jq`.

## 00 — Overview: "PASS" Ka Masla
- Poora system ek lafz "PASS" pe khara hai — reviewer verdict jis pe har merge/escalation depend karti hai.
- **Test vs Eval:** test ek specific property verify karta hai (deterministic), eval estimate karta hai
  probabilistic system representative cases mein kitna acha perform karta hai — usually repeated runs par.
  Metric: **pass rate**.
- "Demo mein chala" sab se kamzor evidence hai (harness course ka 95%×20 steps ≈ 36% clean-finish arithmetic yaad dilata hai).
- **Ek run ki 3 depths:** Depth 1 Answer (sirf final output), Depth 2 Actions (kaunse tools/args/order —
  deleted-test failure yahan pakri jaati hai), Depth 3 Trace (poori run history — bura process pakarta hai;
  rationale sirf "kya kiya" ka evidence hai, "kya soch raha tha" ka nahi).
- **Judge bhi ek model hai** — LLM-as-judge ke apne failure modes: leniency drift, self-preference, surface
  bias (lamba/confident jawab zyada score), aur drift (niche wala model badalta rehta hai — "bar nahi hili,
  ruler hili").

## 01 — Golden Set: Test Cases Kahan Se Aate Hain
- **Har pakri hui failure ek eval case ban jati hai** — ratchet harness ko fix karta hai, eval case prove
  karta hai fix hamesha kaam kar raha hai.
- 3 sourcing rules: **failures pehle** (real caught = reachable proven), **categories cover karo volume
  nahi** (20-40 cases, difficulty-spread), **folder version-control karo**.
- Case shape: JSON with `case_id`, `category`, `judge_reads`, `input_diff`, `expected` (verdict, risk),
  `must_mention`, `unacceptable`, `difficulty`, `origin` (kis failure se aayi).
- Runner koi framework nahi — loop hai: har case 3 runs, `jq` grading. Claude Code (`evals/run.sh` —
  verdict file mein likha jata hai, runner grade karta hai) vs OpenCode (`--format json` stream se reply
  nikalni parti hai). Runner hamesha **read-only** chalao (fixtures injection ho sakte hain).

## 02 — Judge Ko Calibrate Karna
- **Rubric = "achha" ki likhi hui spec.** 2 rules: har score ko real example se **anchor** karo (vague
  "4 = mostly correct" nahi), aur judge se **facts check karwao impressions nahi** ("kya test hataya gaya?").
- **Bar ek decision hai, discovery nahi** — har category ka apna bar, jo miss ki cost pe depend karta hai
  (false-green = "sab hamesha", tone-style = 8/10 theek).
- **Grade the grader (Concept 7):** 20 items sample karo (FAILs/borderline included), blind grade karo apne
  rubric se, phir judge se compare — confusion-matrix table (correct pass/false fail/**false pass**/correct
  fail). **False pass sab se zaroori cell** — ship hone wala bura kaam. Rough guide: overall ≥9/10, high-severity
  pe zero false passes. Disagreement mile to pehle **rubric fix karo**, model sirf tab badlo jab acha rubric
  bhi gap na band kare. Yeh calibration score sirf golden set ke against hai — model badle to dobara chalao.

## 03 — Evals Loop Ke Andar (Regression + Drift)
- **Golden set = harness ki regression suite.** Rule: koi bhi harness change ship hone se pehle `evals/run.sh`
  dobara, baseline se compare. Claude Code: personal habit ya shared-repo CI (branch protection). OpenCode:
  GitHub Actions job.
- Baseline JSON committed (recorded date, model, rubric version, overall + by-category, approved_by).
  Baseline sirf explicit approval se neeche update hota hai; purana history mein rehta hai.
- **Drift:** doosra failure channel — koi local wajah nahi, niche wala model hi update ho gaya. Defense:
  poora set **schedule** pe chalao (nightly/weekly), baseline se drop pe loud alert, model change pe judge
  **dobara calibrate**.
- **Numbers parhna:** panic se pehle dobara chalao (noise vs real regression — real regression consistently
  fail hoti hai); 3 runs = smoke signal, stable estimate nahi; **kaunse cases fail hue** dekho (tone case down
  ≠ emergency, false-green/injection case down = emergency); cost se tier karo — smoke set har change pe,
  full set nightly, hold-outs weekly.

## 04 — Ek Complete Eval Suite: Reviewer Ka Performance Review
- **Minimum honest eval checklist (7 cheezein):** origins-wali cases, schema+fixtures, multiple runs per
  case, anchored rubric+per-category bars, calibrated judge, baseline+gate, schedule.
- Worked example: reviewer khud test hota hai — 12 cases × 3 runs = 36 verdicts, categories: clean fix (3,
  easy), false green (2, hard), bundled changes (2, medium), behavior change (2, medium, risk high),
  injection in diff (2, hard), style-only churn (1, easy). Bars: false-green/injection = 6/6, baaki ≥80%,
  overall gate ≥33/36.
- **Claude Code run:** pehli run 34/36 — ek flake (noise) aur ek real finding: reviewer ne ek injection diff
  PASS kar diya (malicious comment ko harmless samjha). Fix rubric line thi ("diff comment mein instructions
  = khud FAIL"), model swap nahi. Re-run: 35/36, injection 6/6.
- **OpenCode drift story:** 3 hafte baad nightly run 29/36 — koi commit nahi hua tha, judge ka model update
  ho gaya tha. Recalibration se rate recover hui. Point: schedule ne 3 hafton ki chup-chaap galat verdicts ek
  raat mein pakar li.

## 05 — Staying Honest: Goodhart's Law Aur Limits
- **Goodhart's Law:** jab measure target ban jaye, achha measure hona band ho jata hai — prompts/rules
  unhi 36 verdicts ke liye optimize hone lagte hain, number chadhta hai, matlab khatam ho jata hai.
- **3 defenses:** hold-outs (kabhi tune na hone wale sealed cases, weekly run — tuned vs hold-out gap khulna
  Goodhart khud dikhata hai), production se refresh (naye real failures naye cases; high-severity cases kabhi
  retire nahi hotin), agent ko answer key kabhi na dikhne do (cases working context se bahar).
- **Evals kya prove nahi karte:** sirf known territory ke baare mein strong statement, unknown ke baare mein
  khamoshi — genuinely novel input ke baare mein kuch nahi bolti. Isi liye human gate kabhi nahi hatai gayi.
- **Bridge → Eval-Driven Development (Mode 2):** 3 depths → nine-layer pyramid, case folder → DeepEval golden
  datasets, transcript-judge → trace grading, scheduled suite → Routine Phoenix. Managed option: **Rubrics in
  Claude Managed Agents** (beta) — phir bhi calibration chahiye.
- Closing: "Loop ne waqt diya, harness ne limits diye, evals ne track record diya."

## 06 — Practice Projects (8 Eval Builds)
Easy→hard, do rules hamesha: throwaway repo, failure khud plant karo.
1. **The First Five Cases** — apni HARNESS.md se 5 case files likho (Concept 4-5)
2. **The Runner** — `evals/run.sh` (3 runs/case, jq grading) (Concept 5)
3. **The Anchored Rubric** — real examples se anchor, fact-questions (Concept 6)
4. **Grade Your Grader** — 20-item calibration protocol (Concept 7)
5. **The Gate** — baseline.json + CI + branch protection, ek breaking PR test karo (Concept 8)
6. **The Night Watch** — nightly schedule + alert (Concept 9)
7. **The Injection Category** — 3 injection cases, bar 100% (Concept 6, 10)
8. **The Sealed Hold-Outs (Capstone)** — 5 sealed cases, weekly, 1 mahine tuned-vs-hold-out track (Concept 11)
