# 06 — Part 5: Honest Frontiers (Concepts 11-14)

Parts 1-3 ne architecture banayi; Part 4 ne implementation walk ki. Part 5 EDD ke un hisson ko leti
hai jo abhi mushkil hain, emerging hain, ya genuinely unsolved hain. **Yeh pretend karna ke evals har
gap close kar dete hain, dishonest pedagogy hogi.**

## Concept 11 — Golden Dataset Construction: Sabse Undervalued Artifact

Eval frameworks tooling hain. **Golden dataset load-bearing artifact hai.** Ek khoobsurat suite ek
bure dataset par galat cheez ko rigor ke sath measure karti hai; ek modest suite achhe dataset par
matter karne wali failures surface karti hai. Zyada tar teams framework selection par zyada aur
dataset construction par kam kharch karti hain — Concept 11 isay ulta karta hai.

**Dataset ko "good" kya banata hai (importance order mein):**

1. **Representativeness** — production traffic ki actual distribution reflect kare. 70% refunds/20%
   inquiries/10% misc pattern wale agent ko waisa hi weighted dataset chahiye
2. **Edge case coverage** — jahan agent fail hone ka zyada chance hai, chahe woh common na hon —
   adversarial messages, ambiguous instructions, edge-of-envelope decisions. **70% representative + 30%
   edge cases**
3. **Difficulty stratification** — har example easy/medium/hard tag karo. "85% overall" ki jagah "95%
   easy, 80% medium, 60% hard" — ek score ko diagnostic banata hai
4. **Ground truth quality** — har example ko clear "correct behavior" spec chahiye. Judgment calls ke
   liye ground truth khud judgment maangta hai — multiple humans review karein, disagreements document
   karein
5. **Source diversity** — ek support shift, ek product team, ek demographic se sourced examples
   systematic blind spots rakhte hain
6. **Version control aur change discipline** — dataset code hai, git mein, PRs mein reviewed, documented
   change protocol ke sath

**5 common failure patterns jahan datasets fail karte hain:**
- **The Imagination Trap** — team apne mental model se likhti hai, actual distribution se nahi
- **The Easy-Mode Bias** — hard cases skip ho jate hain kyunki grade karna mushkil hai (30% hard cases
  explicitly carve out karo)
- **The Single-Author Problem** — ek insan ke blind spots dataset ke blind spots ban jate hain
- **The Stale-Dataset Problem** — 6 mahine purana dataset, product/customers/tools badal chuke
- **The Pass-Threshold Inflation Problem** — thresholds launch par set, agent improve ho gaya, suite
  checkbox ban gayi

**Sabse "false confidence" wala failure mode: Easy-Mode Bias** — jab humans hard cases skip karte hain
kyunki grading ambiguous hai, dataset easy-biased ban jata hai, high pass rate misleadingly "agent
reliable hai" parhi jati hai jabke asal mein sirf "easy cases handle karta hai" measure ho raha hai.

**Dataset construction ki economics:** 50 examples se shuru karke Decision 7 ke production promotion
se organically 500-1000 examples ek saal mein accumulate hote hain, bina "dataset construction sprint"
chalaye — **yehi recommended path hai.**

## Concept 12 — Eval-Improvement Loop

TDD ka analog: red, green, refactor. **EDD ka analog: task define karo, agent chalao, trace capture
karo, behavior grade karo, failure mode identify karo, prompt/tool/workflow improve karo, evals rerun
karo, compare karo, sirf tab ship karo jab behavior improve ho.**

**7 steps, detail mein:**
1. **Define task** — dataset se ek failing example, ya nayi category
2. **Run agent** — task par invoke karo
3. **Capture trace** — poora execution path
4. **Grade behavior** — poori suite chalao, sirf failing case nahi
5. **Identify failure mode** — output? tool-use? trace? RAG? safety? **failure mode fix layer decide
   karta hai** — retrieval failure knowledge layer mein fix hoti hai, reasoning failure prompt mein,
   tool-use failure tool definition mein. **Yeh step sabse zyada skip hota hai** — isi wajah teams
   baar-baar prompt change karti hain bina improvement ke
6. **Improve (targeted)** — sweeping rewrites nahi, ek specific change
7. **Rerun evals** — poori suite, sirf failing case nahi. "Fix karna" + "koi regression nahi" — dono
   sath hone chahiye, warna yeh fix nahi trade hai

**Concrete walkthrough — wrong-customer refund fix:** weekly triage mein 2 production traces mile
(same email, multiple accounts, disambiguation missing). Golden dataset mein promote hue. Agent
staging mein chalaya — dono responses "sahi" lagte hain. Trace inspect kiya: lookup → 3 results →
model ne `result[0]` pick kiya bina disambiguate kiye. Suite chalayi: output evals 5/5 (response sahi
lagta hai), tool-use evals fail (argument-correctness — galat account_id), trace evals fail
(reasoning-soundness — koi disambiguation step nahi). **Output evals ne miss kiya, hafton tak
production mein miss karta raha.** Failure mode: reasoning failure, prompt mein fix. Ek paragraph
prompt mein add kiya: "multiple results par action tools se pehle disambiguate karo." Rerun kiya — 2
naye examples pass, lekin 1 purana example regress hua (unnecessary confirmation question single-match
customers ke liye). Prompt tighten kiya: "sirf multiple results par." Rerun — sab 50 pass. Ship.
**Poora loop ~1 ghanta laga.**

## Concept 13 — Production Observability Aur Trace-to-Eval Pipeline

Decision 7 ne Phoenix wire ki. Concept 13 operational discipline leta hai jo Phoenix ko useful banata
hai — observability install karna asaan hai, **use karna** mushkil hai.

**Basic claim:** production traces sabse high-quality eval examples ka source hain — real, actual
distribution cover karte hain, un failure modes ko include karte hain jo asal mein hoti hain.

**Pipeline, 4 phases:**
1. **Sample** — errored traces (sabse high-signal), user-feedback-flagged traces, low-confidence
   traces, edge-of-envelope traces, random 1% baseline
2. **Triage** — koi (developer/eval owner) har sampled trace review karta hai: kya yeh eval-worthy
   hai? Sawal: kya isay dataset mein add karna recurrence prevent karega?
3. **Promote** — triaged examples golden dataset mein canonical format mein add hote hain
4. **Threshold review** — hafte mein, thresholds tighten/loosen honi chahiye ya nahi decide karo

**Jahan teams under-invest karti hain:** Triage step (Phase 2) bottleneck hai, jo teams systematically
skip karti hain. **Yehi failure mode hai jo production observability ko production decoration bana
deta hai.** Fix organizational hai, technical nahi: ek named individual (na ke "team") weekly triage
own kare — 30-minute weekly meeting.

**Drift se relation:** Phoenix ka drift-detection dashboard change surface karta hai; trace-to-eval
pipeline usse respond karta hai. Model upgrade se behavior badalta hai, regressed category se examples
promote hote hain, dataset evolve hota hai, agli drift better catch hoti hai.

> **Sabse likely root cause agar 6 mahine mein production se zero examples promote hue:** triage step
> ka koi named owner nahi, aur woh perpetually deferred ho raha hai. **Phoenix bina owner ke decoration
> hai.**

## Concept 14 — Evals Kya Measure Nahi Kar Sakte

**Jo evals achi tarah pakarte hain:**
- Pattern-matching behavior (A+B+C → X wale known patterns)
- Drift on known patterns
- Safety violations named bounds ke andar (refunds ≤ $2000)
- Tool-use correctness

**Jahan evals honestly limited hain:**
- **Novel situations jo dataset cover nahi karta** — suite kuch nahi keh sakti kyunki uske paas ground
  truth hi nahi. Mitigation: production-to-eval pipeline, lekin "abhi tak yeh nahi dekha" ka frontier
  hamesha rehta hai
- **Value alignment at edge cases** — 2 technically correct responses, alag underlying values wale.
  Eval sirf dataset-encoded values ke against grade kar sakti hai, values shift hone par dataset ko
  bhi shift hona parta hai
- **Subjective judgment about quality** — tone, verbosity, framing. LLM-as-judge kuch pakarta hai
  lekin "LLMs kya prefer karte hain" measure karta hai, "humans kya prefer karte hain" nahi
- **Long-tail edge cases** — dataset by definition inhe cover nahi karta
- **Emergent behavior over long interactions** — 30-turn conversations mein drift, contradictions —
  eval structure inhe naturally support nahi karta
- **Adversarial behavior** — novel attacks by definition dataset mein nahi hote. Red-teaming
  complementary discipline hai, EDD ka substitute nahi

**3 implications:**
1. Evals necessary hain, sufficient nahi — red-teaming, human review, monitoring, rollback-readiness
   sab complement karte hain
2. Eval coverage moving target hai — trace-to-eval pipeline coverage extend karta hai
3. Honest reporting mein honest scope include hona chahiye — "92% pass" ka matlab "jo failure modes
   humne test karne socha unka 92%," production ka 8% se kam rehne ki guarantee nahi

> **Fundamentally unsolvable, hard nahi:** Agent naye customer questions par fail hota hai jo dataset
> ne kabhi cover nahi kiye — by definition, evals woh grade nahi kar sakte jo dataset mein nahi hai.

## 5 Cheezein Jo Nahi Karni Chahiye (Anti-Patterns)

1. **Output-only evals ship karke agent ko "safe" mat kaho** — sabse common 2025-2026 failure mode.
   Poora pyramid ship karo, ya accept karo aapki suite jitna aap sochte hain usse kam measure karti hai
2. **LLM-as-judge bina calibration ke mat use karo** — 10-20 examples human judgment se spot-check
   karo, grader ki reliability report karo
3. **Failure categories samajhne se pehle bara dataset mat banao** — 30-50 se shuru karo, organically
   grow karo (500 examples day-1 par usually imagined, production se nahi)
4. **Observability dashboards ko evals mat samjho** — dashboard patterns dikhata hai, eval specific
   run ko specific rubric ke against grade karta hai aur score deta hai. Trace-to-eval pipeline dono ke
   beech pull hai
5. **Evals sirf ek baar launch se pehle mat chalao** — models drift karte hain, prompts edit hote hain,
   traffic shift hoti hai. CI/CD mein wire karo, production observability se dataset grow karo,
   thresholds quarterly review karo

---
[⬅ The Lab — Decisions 4-7](05-the-lab-part2.md) · [⬆ Index](README.md) · [Agla: Closing ➡](07-closing.md)
