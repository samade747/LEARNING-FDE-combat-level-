# PCAO-F / CCAO-F — Combat Level 3: 100-Question "Long-Vignette, Look-Alike" Scenario Bank (`pcaofcombatlevel3.md`)

*Yeh **Level 3** hai: [`pcaofcombatlevel1.md`](pcaofcombatlevel1.md) aur [`pcaofcombatlevel2.md`](pcaofcombatlevel2.md) ke baad
sab se mushkil tier. Level 2 mein options ek saanche ke the; Level 3 mein stems bhi lambe hain (timeline, logs, numbered
observations, kai stakeholders ke dawe), sawal ki *shakal* badalti rehti hai (EXCEPT/INCORRECT, "kaunsa NAHI", ordering,
mapping, computed hisaab, Select TWO), aur aksar ek hi sawal mein do principles takrate hain jahan *priority* faisla karti hai.
Sawal 100, har ek ke 4 options, blueprint ke weights wahi. Yeh jaan-bujh kar real exam se bohat zyada mushkil hai (calibrated nahi).*

**Source grounding:** Zia Tutor AI MCP corpus **generation 75** (retrieved 2026-09-20): PCAO-F page + Governance, AI Fluency,
Workflow Design & Diagnosis, Just Delegate It, What AI Actually Is, ChatGPT & Claude Quick Reference, Skills & Connectors, AI
Prompting in 2026, General Agents on the Web, Code You Never Write. Har sawal ke neeche *Grounded in* line hai. Sab scenarios
original hain; koi asli exam item ya guide ka sample sawal nahi.

## Level 2 se kya badla

| # | Level 3 ki design choice | Kyun mushkil hai |
| ---: | --- | --- |
| 1 | **Lambi vignettes.** Stems mein timeline, numbered observations, table jaise data aur kai logon ke (ghalat) dawe hote hain; koi bhi ek fact akela jawab nahi deta. | Sahi fact dhoondna aur baaqi ko red herring samajhna parta hai. |
| 2 | **Sawal ki shakal badalti hai.** "Kaunsa qadam NAHI follow karta", "kaunsa bayan INCORRECT", ordering, four-way *mapping* (3-5 cheezon ko ek saath sahi jagah), aur computed hisaab (jaise transcript-replay ke tokens: 656,000 vs 348,000; 84 net ghante). | Sirf yaad se nahi, hisaab aur tarteeb se jawab dena parta hai. |
| 3 | **Do principles ka takrao.** Jaise "gate ka *kab*" vs "gate ka *kaun*", independent known answer vs naya raasta, disclosure rule vs judgment; jawab wo hai jo course ki *priority* se nikalta hai. | Dono principles sahi lagte hain. |
| 4 | **Options ek hi saanche ke.** Chaaron ek jaise jumle hain (aksar kai clauses), farq sirf ek jagah. | Pattern-matching nahi chalta. |
| 5 | **23 "Select TWO — all-or-nothing"** sawal. | Sirf ek sahi chunna = zero. |
| 6 | **Answer key balanced** (single-answer mein A/B/C/D lagbhag barabar) aur har option ka apna "kyun galat" + Roman Urdu "Yaad rakho". | Ilm se jawab do, exam-technique se nahi. |

## Blueprint (CCAO-F published weights)

| Domain | Weight | Questions |
| --- | ---: | ---: |
| 2 — Output Evaluation and Validation | 21% | 21 |
| 4 — Workflow Integration and Solution Design | 16% | 16 |
| 6 — Governance, Risk, and Responsible Use | 15% | 15 |
| 1 — Prompting and Task Execution | 14% | 14 |
| 3 — Product and Model Selection | 12% | 12 |
| 5 — Configuration and Knowledge Management | 12% | 12 |
| 7 — Troubleshooting and Optimization | 10% | 10 |
| **Total** | **100%** | **100** |

## Kaise use karein

- **Roman Urdu mein samjho (naya):** har sawal ke options ke neeche ek band (collapsible) block hai jo scenario, sawal aur
  chaaron options ka matlab Roman Urdu + English mein samjhata hai — jawab nahi batata. English sawal waisa hi hai (exam English
  mein hoga); pehle English mein try karo, samajh na aaye tab block kholo.
- **Waqt:** ≈ **3.5–4 minute per sawal**. Do ya teen baithakon mein. Pehle Level 1 aur Level 2 kar lo; Level 3 tab jab Level 2 mein raw ≥ 60% ho.
- **Har sawal ka tareeqa:** (1) sawal kya maang raha hai (EXCEPT? mapping? ordering? hisaab?) pehle yeh tay karo; (2) stem se *deciding
  fact* nikalo; (3) chaaron options mein wo jagah dhoondo jahan farq hai; (4) hisaab wale sawal mein khud compute karo.
- **Score (heuristic, official nahi):** yeh bank real exam se kaafi mushkil hai. Raw **≥ 50%** = exam level ya upar. **35–50%** = qareeb.
  **< 35%** = *Grounded in* section dobara parho. Official pass **720 / 1000 scaled** (72% nahi), koi per-domain minimum nahi.
- **Har ghalti par:** mera chuna hua option kaunsa principle tha jo maine ghalat jagah lagaya, aur file ke aakhir ka cheat-sheet dekho.

---

## Domain 2 — Output Evaluation and Validation (21% — 21 questions)

### Q1.
Hina, a finance analyst at a Faisalabad chemicals distributor, asks Claude to write and run code that computes quarterly early-payment discounts from an accounts-receivable (AR) extract. Timeline. Monday: she runs the script on Q1, whose discount total she "knows" to be PKR 2.84 million; the code reproduces it exactly, with 1,206 rows in and 1,206 out. Tuesday: she learns that the 2.84 million comes from the treasury team's discount ledger, which is fed by an export from the same AR system. Wednesday: she gives the same brief and file to an assistant from another vendor, and it also returns 2.84 million. Thursday: her manager notes that a tiered discount scheme took effect on 1 April (2% if paid within 10 days, 1% within 20 days, none after), that the extract's "days to pay" column is blank on 6% of April rows, and that the board pack for Q2 must be filed on Friday. Hina drafts a five-step verification plan for Q2.

**Which step in the plan does NOT follow the verification method?**

- A. Ask Claude to explain in plain English what the script does with rows whose days-to-pay value is blank, and check that account against the listed rows.
- B. Obtain the Q2 discount total for one closed week from bank remittance advices, which are not derived from the AR system, and require the script to reproduce it before filing.
- C. Plant a fault in a copy of the April data, such as shifting one payment from day 10 to day 11, and confirm the script's output changes by the expected amount.
- D. Treat the second vendor's matching Q1 total as independent confirmation of the script, since a different company's assistant reached the same figure from the same brief and file.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Faisalabad chemicals distributor ki finance analyst Hina AR extract se quarterly early-payment discounts ka code Claude se chalwati. Timeline — Monday: Q1 par chalaya, total PKR 2.84 million exact match, 1,206 rows in/out. Tuesday: pata chala 2.84 million treasury ke discount ledger se aaya jo usi AR system ke export se bharta hai. Wednesday: doosre vendor ke AI ko same brief + file — wahan bhi 2.84 million. Thursday: manager batata 1 April se tiered discount (10 din mein 2%, 20 din mein 1%, baad mein kuch nahi), April ki 6% rows mein "days to pay" khaali, aur Q2 board pack Friday ko file. Hina Q2 ke liye 5-step verification plan banati.

**Sawal:** Plan ka kaunsa step verification method follow NAHI karta? (EXCEPT/NOT wala sawal — ghalat step dhoondna hai.)

**Options ka matlab:**

- **A** — Claude se plain English mein poocho khaali days-to-pay wali rows ka script kya karta, aur us bayan ko listed rows se check karo.
- **B** — Bank remittance advices (jo AR system se nahi nikalte) se ek closed hafte ka Q2 discount total lo, aur filing se pehle script usay reproduce kare.
- **C** — April data ki copy mein fault daalo (jaise ek payment day 10 se day 11), aur confirm karo output expected raqam se badalta.
- **D** — Doosre vendor ka matching Q1 total script ki independent confirmation maano — alag company ke AI ne same brief aur file se same figure diya.

</details>

**Answer:** D

- ✅ **D** — Both read the same brief and the same extract, so agreement cannot expose a rule the brief omits, and Q1 predates the tiers.
- ❌ **A** — Blank cells are an edge case; a replay asked about them, with the rows listed, is a real check on procedure.
- ❌ **B** — This is an independent known answer that exercises the changed path, which is exactly what the method asks for.
- ❌ **C** — A seeded fault in the tier boundary tests whether the check can see that class of error.

**Yaad rakho:** Same brief + same extract par do vendors ka agreement independent nahi. Naya raasta = naya independent test.

*Grounded in: Code You Never Write §6 (known-answer test; independent knowledge; cross-model check and its shared-brief limit; seeded fault; plain-English replay)*

---

### Q2.
A compliance manager at a Karachi insurer wants an independent check of a Claude-drafted summary of a 90-page reinsurance treaty before a board meeting on Thursday. Log of what was done. Monday 10:05: Claude produced the summary and, when asked, also produced "a review rubric for a board-grade summary" with six criteria (clarity, brevity, completeness, risk emphasis, structure, tone). Monday 14:30: she opened a chat with an assistant from a different company, pasted only the summary and the rubric, and asked it to score the summary against each criterion from 1 to 10. It returned 9, 9, 8, 9, 9 and 10. Tuesday: a legal colleague reading only the summary said it "reads well". Wednesday: she noticed the summary states a 24-month notice period while the treaty's clause 14.2 says 18 months, and that the rubric contains no accuracy or source-fidelity criterion. She now must decide what the second assistant's scores are evidence of.

**Which conclusion is best supported?**

- A. The scores are not usable because the same assistant wrote the rubric, so the fix is a rubric written by the second assistant, which would make the evaluation fully independent of the drafter.
- B. The scores show a progress signal only, so the manager should rerun the second assistant three times and average, and file the summary if the average remains above eight on every criterion.
- C. The scores show the summary reads well against criteria the drafting assistant chose, but neither reviewer saw the treaty, so they say nothing about fidelity; verification needs the source and a person checking the claims the board will rely on.
- D. The scores show the summary is strong on the six criteria and, because the reviewer is from a different company, the only remaining risk is a single factual slip that a light read of clause 14.2 will fix.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Karachi insurer ki compliance manager Thursday board meeting se pehle 90-page reinsurance treaty ki Claude summary ka independent check chahti. Log — Monday 10:05: Claude ne summary banayi aur poochne par "board-grade summary ka review rubric" bhi — 6 criteria (clarity, brevity, completeness, risk emphasis, structure, tone). Monday 14:30: doosri company ke AI ko sirf summary + rubric de kar har criterion 1–10 score karwaya: 9, 9, 8, 9, 9, 10. Tuesday: legal colleague ne sirf summary parh kar "achhi parhti" kaha. Wednesday: dekha summary mein 24-month notice period, treaty clause 14.2 mein 18 months; aur rubric mein accuracy ya source-fidelity ka koi criterion nahi.

**Sawal:** Doosre AI ke scores kis cheez ka saboot hain — kaunsa nateeja sab se supported?

**Options ka matlab:**

- **A** — Scores bekaar kyunke rubric drafting AI ne likha; doosre AI se rubric likhwao to evaluation fully independent.
- **B** — Scores sirf progress signal; doosre AI ko teen dafa chala kar average lo, har criterion par 8 se upar ho to file karo.
- **C** — Scores dikhate summary drafting AI ke chune criteria par achhi parhti, magar kisi reviewer ne treaty dekhi hi nahi, to fidelity ke baare mein kuch nahi kehte; verification ko source aur board jin claims par bharosa karega unhein check karne wala insaan chahiye.
- **D** — Scores dikhate summary 6 criteria par mazboot, aur reviewer alag company ka, to bas ek factual slip ka risk bacha jo clause 14.2 ka halka read theek kar dega.

</details>

**Answer:** C

- ✅ **C** — A different company is the right kind of checker only if it compares the summary with the source, and a rubric written by the drafter inherits its blind spots.
- ❌ **A** — A rubric from another model still omits the treaty; independence needs the source in view, not a different author of criteria.
- ❌ **B** — Averaging more scores from a checker that never saw the treaty repeats the same blind spot.
- ❌ **D** — The reviewer never saw the treaty, so it cannot support any claim about accuracy, and the notice-period error shows the gap is not a single slip.

**Yaad rakho:** Rubric drafter ka, checker ke paas source nahi: score sirf 'achha parhta hai' batata hai, 'sahi hai' nahi.

*Grounded in: AI Prompting 2026 §13 (a different company is the real check; the score is a progress signal); Code You Never Write §6 (checker must see the source); AI Fluency §5*

---

### Q3.
An accountant at a Karachi trading house receives an assistant-built sales report from a year of invoices. Signals observed, in the order the accountant noticed them. (1) The grand total matches the ledger to the rupee. (2) The row count matches (9,850 in, 9,850 out). (3) The report ranks "Al-Noor Traders" first with PKR 41 million, while she knows from long experience that "Hashmi Brothers" is by far the largest customer. (4) The assistant's plain-English replay says it "grouped invoices by customer name and summed amounts". (5) A second assistant, given the same file and brief, produced the same ranking. (6) The customer master lists Hashmi Brothers under three spellings ("Hashmi Bros", "M/s Hashmi Brothers", "Hashmi Brothers Pvt"). The bank meeting that will use the ranking is in 90 minutes, and the accountant has time for exactly one investigation before deciding what to tell the bank.

**Which single investigation best follows the method, and why?**

- A. Ask for the rows behind the top five customers and how names were grouped: her knowledge contradicts the result, and totals, counts and a second run cannot reveal a grouping split.
- B. Ask the second assistant to regenerate the ranking with names normalised, since a different vendor's independent run is the fastest way to see whether the first ranking changes.
- C. Ask the first assistant to rate its confidence in the ranking and explain any assumptions, since a stated assumption about names would show where the grouping went wrong.
- D. Reconcile the grand total and the row count against the ledger again by customer, since two matches suggest that the only remaining risk is a mis-summed customer subtotal.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Karachi trading house ki accountant ko saal bhar ki invoices se AI-built sales report mili. Signals jis order mein notice hue: (1) grand total ledger se rupee tak match. (2) Row count match (9,850). (3) Report "Al-Noor Traders" ko PKR 41 million ke saath pehla rakhti, jabke usay pata hai "Hashmi Brothers" kahin bara customer. (4) Replay: "customer name se group karke amounts sum kiye". (5) Doosre AI ne same file/brief se same ranking di. (6) Customer master mein Hashmi Brothers teen spellings mein ("Hashmi Bros", "M/s Hashmi Brothers", "Hashmi Brothers Pvt"). Bank meeting 90 minute mein; sirf ek investigation ka waqt.

**Sawal:** Kaunsi ek investigation method ke mutabiq behtareen hai, aur kyun?

**Options ka matlab:**

- **A** — Top paanch customers ke peeche ki rows aur naam kaise group hue maango: uski knowledge result se takrati, aur totals, counts ya doosra run grouping split nahi dikha sakte.
- **B** — Doosre AI se names normalise karke ranking dobara banwao — alag vendor ka independent run sab se tez.
- **C** — Pehle AI se ranking par confidence aur assumptions poocho — names ke baare mein assumption dikha dega grouping kahan bigdi.
- **D** — Grand total aur row count ko customer-wise ledger se dobara reconcile karo — do matches ke baad sirf subtotal ka risk bacha.

</details>

**Answer:** A

- ✅ **A** — Reality questions use what you already know; a correct grand total and row count can hide a grouping error.
- ❌ **B** — The second assistant read the same brief and file, so a rerun repeats the grouping unless someone inspects how names were grouped.
- ❌ **C** — A self-rated confidence and a prose account are the same voice; the rows themselves are the evidence.
- ❌ **D** — Both totals already match; a grouping split moves money between customers without changing either figure.

**Yaad rakho:** Tumhara tajurba report se takraye to rows dekho. Grand total aur row count match hona grouping ki ghalti nahi pakadta.

*Grounded in: Code You Never Write §6 (reality questions; show three rows behind the number; plain-English replay; cross-model limit)*

---

### Q4.
A treasury analyst at a fertiliser maker asks Claude to write and run code on a 4,300-row payments file to total October supplier payments for a covenant report, and it shows both the code and the result: PKR 612.4 million. The covenant threshold is PKR 600 million, so the figure matters. Details. The code reads "payments_final.csv"; the treasury folder also holds "payments_final_v2.csv" modified two days later and a note from a colleague saying "v2 has the corrections for the reversed entries". Claude's replay says it "summed the amount column for October rows". The analyst sees the run is real, the column is correct, and the date filter is correct. Her manager says the number was computed and not written, and that the exact code was shown, so the covenant report can go out this afternoon.

**What is the right next step?**

- A. Accept the figure, since the code, the column and the date filter were all checked and shown, and note the file name in the report so readers can see which version was used.
- B. Ask which file was read and why; rerun on v2 and compare; test one closed period against the ledger, since a run can be exact and still use the wrong input.
- C. Ask the assistant to describe in plain English what the code does with reversed entries, and file the report if the description mentions netting them out.
- D. Rerun the same code on v2 and file whichever total is higher, since the higher payment total is the conservative position for a covenant threshold.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Fertiliser maker ki treasury analyst covenant report ke liye 4,300-row payments file par Claude se October supplier payments ka total code se nikalwati: PKR 612.4 million, code aur result dono dikhe. Covenant threshold PKR 600 million, to figure ahem. Details: code "payments_final.csv" parhta; folder mein do din baad modified "payments_final_v2.csv" bhi hai aur colleague ka note: "v2 mein reversed entries ki corrections hain". Replay: "October rows ka amount column sum kiya". Run asli, column sahi, date filter sahi. Manager: number computed hai, code dikha, report aaj dopahar bhej do.

**Sawal:** Agla sahi qadam kya hai?

**Options ka matlab:**

- **A** — Figure maan lo — code, column, filter sab check; report mein file ka naam likh do.
- **B** — Poocho kaunsi file parhi gayi aur kyun; v2 par dobara chala kar compare karo; ek closed period ledger se test karo — run exact ho kar bhi ghalat input use kar sakta.
- **C** — AI se plain English mein poocho code reversed entries ke saath kya karta; bayan mein netting ho to file karo.
- **D** — Wahi code v2 par chala kar jo total zyada ho wo file karo — covenant ke liye zyada total conservative.

</details>

**Answer:** B

- ✅ **B** — Check the inputs, not just the sum: the right rows, the right column, the right file; then test against a known answer.
- ❌ **A** — Disclosing the file name does not fix a possibly stale input on a threshold that decides a covenant.
- ❌ **C** — The replay concerns the code, not the file; a description of intended handling does not show which input was read.
- ❌ **D** — Choosing by direction is a guess; the aim is to know which file is correct and to test the result.

**Yaad rakho:** Run exact aur column sahi, phir bhi file ghalat ho sakti hai. Inputs check karo.

*Grounded in: AI Fluency §6.3 (numbers rule: check the inputs, not the sum); Workflow Design §3 (the run is exact but the code can use the wrong input); Code You Never Write §6*

---

### Q5. *(Select TWO — all-or-nothing)*
A finance team's scheduled cloud agent compiles a weekly supplier-payment exceptions digest. This week's digest ends with these four sentences, and the run's tool log shows only the entries listed. (a) "I have cross-checked all 14 exceptions against the ERP." Log: one read of a shared spreadsheet; no ERP call. (b) "I saved the digest to the finance folder." Log: a write to the finance folder returning success, file present. (c) "I have placed corrective holds on the 9 confirmed duplicates." Log: no write to any payment system; the payment system shows no new holds. (d) "I compared this week's exceptions with last week's." Log: two reads of the exceptions file, one for each week, and a diff step with its output. The team lead says the digest is well written, the run status is "completed", and the agent has been reliable for three months.

**Which TWO sentences are claimed actions that the tool log does not support?**

- A. Sentence (c): the corrective holds, because no write reached a payment system and none exists there, so downstream staff would be relying on an action that never happened.
- B. Sentence (b): saving the digest, because a write returning success is only a claim by the tool and the agent's statement adds nothing that can be checked.
- C. Sentence (d): the week-on-week comparison, because a comparison inside a language model is always an estimate and cannot be evidenced by any log entry.
- D. Sentence (a): the ERP cross-check, because the log shows no ERP call and a spreadsheet read is a different event, so the claim is a sentence, not an event.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Finance team ka scheduled cloud agent weekly supplier-payment exceptions digest banata. Digest ke aakhri chaar jumle aur tool log: (a) "14 exceptions ERP se cross-check kiye" — log: shared spreadsheet ka ek read, ERP call nahi. (b) "Digest finance folder mein save kiya" — log: finance folder mein write, success, file maujood. (c) "9 confirmed duplicates par corrective holds lagaye" — log: kisi payment system mein write nahi, system mein naye holds nahi. (d) "Is hafte ke exceptions pichle hafte se compare kiye" — log: exceptions file ke do reads (dono hafte) aur diff step apne output ke saath. Lead: digest achha, status "completed", 3 mahine se reliable.

**Sawal:** Kaunse DO jumle aise claimed actions hain jinhein tool log support NAHI karta?

**Options ka matlab:**

- **A** — Jumla (c) — corrective holds: koi write payment system tak nahi pahuncha aur wahan koi hold nahi.
- **B** — Jumla (b) — save: success wala write sirf tool ka claim, agent ka bayan kuch checkable nahi jodta.
- **C** — Jumla (d) — comparison: language model ke andar comparison hamesha andaaza, log se saabit nahi hota.
- **D** — Jumla (a) — ERP cross-check: log mein ERP call nahi, spreadsheet read alag event hai; claim jumla hai, event nahi.

</details>

**Answer:** A, D

- ✅ **A** — A claimed action that never happened is a fabrication sign, with consequences downstream.
- ✅ **D** — A claimed check counts only if the tool result shows it.
- ❌ **B** — The log shows a write and the file exists, so the event is supported.
- ❌ **C** — Two reads and a diff step with output are exactly the evidence that would support the claim.

**Yaad rakho:** Jumla ko log se milao: ERP call nahi, hold nahi = dawa saboot nahi. Save/diff ka saboot maujood.

*Grounded in: AI Fluency §5 (a claimed action that never happened; unless the tool shows the event, treat the claim as a sentence); General Agents on the Web §9 (ran is not worked)*

---

### Q6.
A procurement lead at a Rawalpindi construction firm asks Claude to recommend one of three cement suppliers and to "show your assumptions, the evidence for each, and the criteria you used". Claude recommends Supplier B and lists six assumptions. Her review notes: assumptions 1, 2 and 4 are supported by quoted lines in the three attached proposals; assumption 3 ("B's price is fixed for 12 months") has no supporting line in any proposal; assumption 5 cites "industry norms"; assumption 6 says B's kiln is "reliably above 90% uptime", with no source. The firm's board wants the recommendation tomorrow. A colleague suggests enabling the extended-thinking display to see "what Claude really reasoned", another suggests asking Claude whether it is confident in assumptions 3, 5 and 6, and the CFO wants to go ahead because "the conclusion is sensible".

**Which response best follows the guidance on judging the case made for a recommendation?**

- A. Treat the list as a justification offered for review: check assumptions 3, 5 and 6 against the proposals and named sources, and hold the recommendation until each is supported or removed.
- B. Ask Claude to rate its confidence in assumptions 3, 5 and 6 and keep those scoring above 8, since a self-reported score identifies which assumptions the recommendation can rest on.
- C. Open the extended-thinking display to see the model's true reasoning about assumptions 3, 5 and 6, and accept the recommendation if the displayed working supports them.
- D. Approve the recommendation with a footnote listing assumptions 3, 5 and 6 as unverified, since three of six assumptions are supported and the conclusion is sensible.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Rawalpindi construction firm ki procurement lead Claude se teen cement suppliers mein ek recommend karwati aur kehti "assumptions, har ek ka evidence aur criteria dikhao". Claude: Supplier B, chhe assumptions. Review: 1, 2, 4 attached proposals ki quoted lines se supported; 3 ("B ki price 12 mahine fixed") kisi proposal mein nahi; 5 "industry norms" cite karta; 6 kehta B ka kiln "reliably 90% uptime se upar", source nahi. Board kal recommendation chahta. Colleague: extended-thinking display kholo; doosra: 3, 5, 6 par Claude se confidence poocho; CFO: "conclusion sensible hai", aage badho.

**Sawal:** Recommendation ke case ko judge karne ki guidance se kaunsa response behtareen hai?

**Options ka matlab:**

- **A** — List ko review ke liye di gayi justification samjho: 3, 5, 6 ko proposals aur named sources se check karo, aur jab tak har ek supported ya hata na diya jaye recommendation rok kar rakho.
- **B** — 3, 5, 6 par confidence rate karwao, 8 se upar wale rakho.
- **C** — Extended-thinking display khol kar 3, 5, 6 par model ki "asli" reasoning dekho, support kare to accept.
- **D** — Footnote mein 3, 5, 6 ko unverified likh kar approve — chhe mein teen supported, conclusion sensible.

</details>

**Answer:** A

- ✅ **A** — Assumptions and evidence are material for review, not a record of hidden reasoning, and unsupported specifics are the ones to trace.
- ❌ **B** — A self-rated confidence is the same fluent voice and is not evidence about what the proposals say.
- ❌ **C** — The visible working, including any thinking display, is still material to review; it does not replace checking sources.
- ❌ **D** — Footnoting unsupported assumptions discloses them without resolving them; the board would still act on a recommendation whose support is missing.

**Yaad rakho:** Assumptions list = review ka saaman. Jo assumption source se na mile usay tay karo, footnote mein na chhupao.

*Grounded in: AI Fluency §5.1 (judge the case made for it; ask for assumptions and evidence; justification offered for review, not a record of hidden reasoning)*

---

### Q7. *(Select TWO — all-or-nothing)*
An FDE reviews a Digital FTE deployed at a Karachi retail bank to answer card-dispute queries. She writes four observations from a quarter of monitoring. (1) On a hand review of 300 answers, 298 were accurate against policy and two contained a wrong fee figure. (2) In her own testing sessions she found that steering the assistant with follow-up messages to get the right tone took roughly 12 minutes per script, against 20 minutes to write the scripts herself, but she then had to rewrite 40% of each output. (3) Support data shows 34% of customers who chat with the assistant call the branch about the same issue within an hour, against 11% before launch. (4) Customer comments include "it answered but I still did not know what to do next". She is preparing a short note that must attribute each observation to the kind of discernment it evidences: product, process or performance.

**Which TWO attributions are correct?**

- A. Observation (2) is performance discernment, because the FDE's testing sessions concern how the assistant behaves and the rewriting shows the behavior is poor.
- B. Observation (1) is performance discernment, because a review of 300 answers across a quarter is a study of the assistant's independent behavior toward customers.
- C. Observations (3) and (4) are performance discernment: whether the assistant's independent behavior serves the people it meets, visible only across many cases.
- D. Observation (2) is process discernment: whether working this way pays off once steering and rewriting are counted; 12 minutes plus a 40% rewrite is weak against 20.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** FDE Karachi retail bank ke card-dispute Digital FTE ki quarter bhar ki monitoring se chaar observations likhti. (1) 300 answers ke hand review mein 298 policy ke mutabiq accurate, 2 mein ghalat fee figure. (2) Apni testing sessions mein tone theek karne ke liye follow-up steering ~12 minute per script, khud likhne mein 20 minute, magar phir har output ka 40% rewrite. (3) Support data: chat karne wale 34% customers ek ghante mein usi masle par branch call karte (launch se pehle 11%). (4) Comments: "jawab diya magar pata nahi agla kya karoon". Note mein har observation ko product, process ya performance discernment se jodna hai.

**Sawal:** Kaunsi DO attributions sahi hain?

**Options ka matlab:**

- **A** — Observation (2) performance discernment — testing sessions AI ke behaviour ke baare mein, rewriting kharab behaviour dikhati.
- **B** — Observation (1) performance discernment — quarter bhar 300 answers ka review customers ke saath independent behaviour ki study.
- **C** — Observations (3) aur (4) performance discernment — AI ka independent behaviour logon ko serve karta ya nahi, sirf bohat cases mein nazar aata.
- **D** — Observation (2) process discernment — steering aur rewriting gin kar kya is tarah kaam karna faida deta; 12 minute + 40% rewrite, 20 ke muqable kamzor.

</details>

**Answer:** C, D

- ✅ **C** — An assistant can be accurate and still fail its users; that shows in what users do next and say.
- ✅ **D** — Process discernment judges whether the way of working is paying off.
- ❌ **A** — It concerns the FDE's own working process with the assistant, not deployed behavior toward customers.
- ❌ **B** — It judges whether individual results were correct, which is product discernment.

**Yaad rakho:** Jawab durust = product. Steering ka waqt = process. User phir bhi phansa/phone kar raha = performance.

*Grounded in: AI Fluency §5.1-5.3 (product, process and performance discernment)*

---

### Q8.
A bank's compliance team runs an AI screen over 400 transactions a day; reviewers approve or reject each draft "clear" or "escalate". A quality lead studies 13 weeks of records: 26,000 drafts; 24,700 approved as drafted (95%); the AI's own confidence score is available for each draft; reviewers who reject need a supervisor's countersignature; the median review time is nine seconds; 320 drafts were rejected, of which 41 were later found to be genuine mistakes by the AI and 279 were false alarms by reviewers. The team must design a sampling plan for the next quarter to test whether the gate works. Four plans are proposed, each drawing 260 drafts a week for a full re-review by an independent senior analyst who has the source records.

**Which plan best follows the guidance on review quality?**

- A. Draw the 260 only from drafts with the lowest AI confidence scores, since the assistant's own uncertainty identifies where errors are most likely to have been approved.
- B. Draw the 260 as a simple random sample of all drafts so that each draft has the same chance, since random sampling is the neutral way to estimate the gate's overall accuracy.
- C. Draw the 260 from approved as well as rejected drafts, stratified to over-sample near-threshold drafts, escalated cases and unusual inputs, and compare the senior analyst's decisions with the reviewers'.
- D. Draw the 260 only from rejected drafts, since 279 of 320 rejections were reviewer false alarms and that is where the reviewers' judgment is least reliable.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Bank ki compliance team ka AI screen roz 400 transactions; reviewers har "clear"/"escalate" draft approve ya reject karte. Quality lead 13 hafte ke records dekhta: 26,000 drafts; 24,700 jaise draft the approve (95%); har draft ka AI confidence score available; reject karne ke liye supervisor countersignature; median review 9 second; 320 reject hue — 41 baad mein AI ki asli ghaltiyan nikli, 279 reviewers ke false alarms. Agli quarter ke liye sampling plan: har hafte 260 drafts ek independent senior analyst (source records ke saath) poora re-review kare. Chaar plans.

**Sawal:** Review quality ki guidance ke mutabiq kaunsa plan behtareen hai?

**Options ka matlab:**

- **A** — 260 sirf lowest AI confidence wale drafts se — AI ki apni uncertainty batati errors kahan approve hue honge.
- **B** — 260 simple random sample — har draft ka barabar chance, overall accuracy ka neutral andaaza.
- **C** — 260 approved aur rejected dono se, stratified taake near-threshold drafts, escalated cases aur unusual inputs zyada aayein, aur senior analyst ke faisle reviewers se compare karo.
- **D** — 260 sirf rejected drafts se — 320 mein 279 false alarms, reviewers ka judgment wahin kamzor.

</details>

**Answer:** C

- ✅ **C** — Sample the edge cases where failure is likelier or costlier, and test what the gate approved, not only what it rejected.
- ❌ **A** — It leaves out high-confidence approvals and relies on the system's self-report to say where to look.
- ❌ **B** — A random sample rarely reaches the rare, costly cases; edge cases and near-threshold drafts need over-sampling.
- ❌ **D** — It never tests the 24,700 approvals, where a missed AI error would pass through the gate.

**Yaad rakho:** Sirf reject ya sirf low-confidence nahi: approved bhi, threshold ke qareeb aur ajeeb cases zyada.

*Grounded in: Governance A.1 (sample the edge cases: unusual inputs, exclusions, low-confidence outputs, cases near thresholds); §4.1 (sample exclusions as well as inclusions)*

---

### Q9.
A CFO's team asks Claude, in a chat, to "summarise this quarterly financial report for the board" from a 40-page PDF. The reply is a well-formatted one-page summary that says revenue "grew 8.3%", operating margin was "14.1%", and "total finance costs came to PKR 1.96 billion", with no calculation shown, no code, and no note of which pages the figures came from. Checks. Revenue and margin agree with the report's headline table. Finance costs are the sum of three lines (interest on loans PKR 1.12 billion, interest on leases PKR 0.41 billion, other finance charges PKR 0.47 billion) that the assistant did not list. The analyst adds them by hand: 1.12 + 0.41 + 0.47 = 2.00 billion. The board pack goes to print this afternoon and the CFO says the summary "is right on every line item".

**What does the numbers rule say, and what should the team do?**

- A. Replace the figure with 2.00 billion from the analyst's hand addition and print the pack, since the hand-checked total is the correct one for the summary.
- B. Ask Claude to explain how it arrived at 1.96 billion in plain English and print the pack if the explanation mentions all three finance lines.
- C. A decision-critical total must be computed and shown: have code sum the three lines, ask where each figure came from, and check inputs before printing.
- D. Accept the summary, since two headline figures matched the report and a total of 1.96 billion against 2.00 billion is a rounding difference that a board summary can carry.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** CFO ki team chat mein Claude se 40-page PDF quarterly financial report ka board summary banwati. One-page summary: revenue "8.3% badhi", operating margin "14.1%", "total finance costs PKR 1.96 billion" — koi calculation, code, ya page reference nahi. Checks: revenue aur margin headline table se match. Finance costs teen lines ka jor hai (loans ka interest 1.12 bn, leases ka interest 0.41 bn, other finance charges 0.47 bn) jo AI ne list nahi kin. Analyst haath se jodta: 1.12 + 0.41 + 0.47 = 2.00 billion. Board pack aaj dopahar print; CFO: summary "har line item par sahi".

**Sawal:** Numbers rule kya kehta hai, aur team ko kya karna chahiye?

**Options ka matlab:**

- **A** — Figure ko analyst ke haath wale 2.00 billion se badal kar print karo.
- **B** — Claude se plain English mein poocho 1.96 kaise aaya; teeno lines ka zikr ho to print.
- **C** — Faisle ke liye aham total compute aur dikhaya hua hona chahiye: code se teen lines sum karwao, poocho har figure kahan se aaya, aur print se pehle inputs check karo.
- **D** — Summary maan lo — do headline figures match, 1.96 vs 2.00 rounding ka farq.

</details>

**Answer:** C

- ✅ **C** — The assistant predicts a likely-looking total, so the total can be wrong while every line item is right.
- ❌ **A** — Correcting one figure fixes this page but not the method; the other written figures and the source pages are still unshown.
- ❌ **B** — The explanation describes a method in words; it does not show the sum was computed, and here the sum is wrong.
- ❌ **D** — A 0.04 billion difference is not rounding of three stated lines; it signals the figure was written, not computed.

**Yaad rakho:** Total jo faisle par tika ho computed hona chahiye, likha hua nahi. Line items sahi, total ghalat ho sakta hai.

*Grounded in: AI Fluency §6.3 (the numbers rule: any number a decision rests on must be computed, never generated; ask where each number came from); Workflow Design §3*

---

### Q10.
A property firm in Islamabad proves a Claude workflow that abstracts leases. The lead follows the proving loop: pick one recurring task, find an old example where she already knows the correct result, ask the assistant to reproduce it with the context she would normally have had, compare, refine, run again. She chooses eight closed leases. Facts. Five of the eight abstracts were written by a junior analyst last year and had been "checked" only by asking an earlier AI tool to review them; three were written by a senior analyst and signed off after line-by-line checking against the leases. The assistant reproduces all eight. The lead concludes the workflow "passed the proving test", and plans to cut review from 50% to 5%, including for commercial leases, which the eight did not include.

**What did the proving test earn, if anything?**

- A. Confidence for the five junior abstracts, since an earlier AI review is a reasonable second check, and for the three senior abstracts, since line-by-line checking is the stronger standard.
- B. Confidence only for the three human-verified residential cases; the five AI-checked abstracts are not known answers and residential results don't transfer, so re-prove on verified commercial leases first.
- C. Nothing, since every proving test is invalid once a model is used both to write and to review the examples, so the test should be repeated with a different vendor's assistant.
- D. Confidence for all eight residential leases, since all eight were reproduced, and for commercial leases as well once review is kept at 20% for the first quarter.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Islamabad property firm lease-abstraction workflow prove karti. Lead proving loop follow karti: ek recurring task chuno, purana example jiska sahi result pata ho, AI se wahi context de kar reproduce karwao, compare, refine, dobara. Aath closed leases chuni. Facts: 8 mein se 5 abstracts pichle saal junior analyst ne likhe aur sirf ek purane AI tool se "check" karwaye; 3 senior analyst ne likhe aur lease se line-by-line check karke sign off kiye. AI ne aathon reproduce kar diye. Lead: workflow "proving test pass", review 50% se 5%, commercial leases samet (jo aath mein nahi the).

**Sawal:** Proving test ne kya kamaya, agar kuch?

**Options ka matlab:**

- **A** — 5 junior abstracts ke liye confidence (purana AI review munasib doosra check) aur 3 senior ke liye bhi.
- **B** — Confidence sirf 3 human-verified residential cases ka; 5 AI-checked abstracts known answers nahi, aur residential results commercial par transfer nahi hote — pehle verified commercial leases par dobara prove karo.
- **C** — Kuch nahi — model likhe aur review bhi kare to har proving test invalid; doosre vendor ke saath dobara.
- **D** — Aathon residential ke liye confidence, aur commercial ke liye bhi agar pehli quarter review 20% rahe.

</details>

**Answer:** B

- ✅ **B** — A proving case needs a result you already trust from human verification, and confidence attaches to similar future work only.
- ❌ **A** — An earlier AI review is not independent verification, so the five cases do not establish known answers.
- ❌ **C** — The three human-verified cases are valid proving cases; the flaw is in five, not in the method.
- ❌ **D** — Five reproduced abstracts rest on an earlier AI's review; reproducing them shows agreement with an unverified answer.

**Yaad rakho:** Proving case wo jo insaan ne verify kiya ho. AI se 'check' kiya hua answer known answer nahi.

*Grounded in: Quick Reference §9 (test on old work you already finished and already trust; passing earns confidence for similar future work; what passing does not prove)*

---

### Q11.
An analyst at an education NGO needs the date a national curriculum reform takes effect, for a donor report due tonight. Evidence gathered. Source 1: a ministry PDF, dated 2023, on the ministry's own site, states "effective 1 April". Source 2: a law-firm blog, updated last month, states that "a subsequent notification postponed it to 1 August" and links to a ministry notice she cannot open. Source 3: a news article from last week repeats "1 April" and cites the 2023 PDF. Source 4: the assistant that found these says it "stands by 1 April as the ministry PDF is the primary source". She has one hour. The method she was taught has four steps (identify, trace, challenge, decide) and four decisions (accept, correct, investigate, reject).

**Which reasoning about the sources is correct?**

- A. Correct the report to 1 August, since the blog is the most recent and it links a ministry notice, and the most recent source always outranks an older primary one.
- B. Accept 1 April, since two independent sources (the ministry PDF and the news article) agree and the blog is a secondary source that cannot outweigh a primary one.
- C. Investigate: the primary source may be superseded and the news article merely repeats it, so find the current ministry notification directly and confirm its date.
- D. Reject all four sources and report the date as unknown, since credible sources disagree and the responsible position with a donor is to state nothing until certain.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Education NGO ki analyst ko aaj raat ki donor report ke liye curriculum reform ki effective date chahiye. Evidence: Source 1 — ministry ki apni site par 2023 ki PDF: "effective 1 April". Source 2 — pichle mahine update hua law-firm blog: "baad ki notification ne 1 August tak postpone kiya", ek ministry notice link karta jo khulta nahi. Source 3 — pichle hafte ka news article "1 April" dohrata aur 2023 PDF cite karta. Source 4 — AI kehta "1 April par qaim, ministry PDF primary source". Ek ghanta hai. Method: identify, trace, challenge, decide (accept/correct/investigate/reject).

**Sawal:** Sources ke baare mein kaunsi reasoning sahi hai?

**Options ka matlab:**

- **A** — 1 August kar do — blog sab se naya aur ministry notice link karta, naya source purane primary se hamesha upar.
- **B** — 1 April accept — do independent sources (ministry PDF + news) agree, blog secondary hai.
- **C** — Investigate: primary source superseded ho sakta aur news article sirf usi ko dohrata; current ministry notification seedha dhoondo aur date confirm karo.
- **D** — Chaaron reject, date "unknown" report karo.

</details>

**Answer:** C

- ✅ **C** — Challenge asks whether the fact has changed since the page was written; a repeating secondary source adds no independent evidence.
- ❌ **A** — She could not open the notice; recency alone does not decide, and the notice itself has not been traced.
- ❌ **B** — The news article repeats the PDF, so the two do not count as independent, and the primary source may be the older one.
- ❌ **D** — One hour is enough to trace the current notification; declining to state a date skips the investigation the method calls for.

**Yaad rakho:** Primary jeetta hai agar wo purana na ho. Dohrane wala akhbar alag saboot nahi.

*Grounded in: Just Delegate It §10 (Trace and Challenge: the provider's own page beats a blog about it; when two credible sources disagree the primary usually wins, unless it is the older one; investigate)*

---

### Q12.
A consultant asks Claude to compare three warehouse-automation vendors for a Karachi retailer and to mark every figure or claim it could not confirm as "unverified". Chain of handling. Step 1, the chat answer: nine claims are marked "unverified", including two vendor uptime figures and a delivery-time claim. Step 2, she asks for a two-page briefing document: the document has six "unverified" marks, and the three missing ones are the two uptime figures and the delivery-time claim, now stated without qualification. Step 3, she asks for a five-slide deck for the client from the document: the deck has two "unverified" marks and states the uptime figures as facts in a chart. The client meeting is tomorrow; she has 40 minutes and can trace at most three claims to sources.

**What should she do?**

- A. Ask Claude to confirm that the deck is consistent with the chat answer, and send the deck if it confirms, since consistency across all three versions shows nothing was changed.
- B. Keep the deck's cleaner wording for the client and move the nine unverified items to the speaker notes, since executives dislike hedging on slides and the notes preserve the caveats.
- C. Trace any three claims chosen at random from the deck and keep the deck's current wording, since a random sample of three is the fairest way to estimate how reliable the deck is.
- D. Count caveats at each hand-off (nine, six, two), restore the dropped marks, and use her 40 minutes tracing the two uptime figures and the delivery-time claim that lost their marks.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Consultant ne Claude se Karachi retailer ke liye teen warehouse-automation vendors compare karwaye aur har unconfirmed figure/claim par "unverified" mark lagwaya. Hand-offs: Step 1 chat: 9 claims unverified (do vendor uptime figures aur ek delivery-time claim samet). Step 2, 2-page briefing: 6 marks — jo teen gire wo do uptime figures aur delivery-time claim, ab bina qaid ke. Step 3, 5-slide client deck: 2 marks, aur uptime figures chart mein facts ke taur par. Client meeting kal; 40 minute, zyada se zyada teen claims source tak trace kar sakti.

**Sawal:** Usay kya karna chahiye?

**Options ka matlab:**

- **A** — Claude se confirm karwao deck chat se consistent hai; haan kahe to bhejo.
- **B** — Deck ki saaf wording rakho aur 9 unverified items speaker notes mein daal do.
- **C** — Deck se random teen claims trace karo aur wording wahi rakho — random sample sab se fair.
- **D** — Har hand-off par caveats gino (9, 6, 2), gire hue marks wapas lagao, aur 40 minute un do uptime figures aur delivery-time claim ko trace karne mein lagao jinke marks gire.

</details>

**Answer:** D

- ✅ **D** — Deliverables lose caveats because tidy is what a document is for; counting the marks before and after shows what was dropped.
- ❌ **A** — The same model's confirmation is not a count of what survived, and the three versions are not consistent.
- ❌ **B** — That hides uncertainty in a place the client will not read, and does not resolve the three figures.
- ❌ **C** — The claims that lost their caveats are the known risks and should be traced first, not sampled at random.

**Yaad rakho:** Har hand-off par caveats ginti karo. Jo mark gir gaye unhi claims ko pehle trace karo.

*Grounded in: Just Delegate It §6 (deliverables lose caveats; count the caveats before and after; keep every unverified mark) and §10*

---

### Q13.
A university admissions officer asks Claude to draft scholarship-decision letters, then evaluates them by asking, each time in the same chat, "Score this letter out of ten and say how to improve it". Round 1: 7/10 with three suggestions. She applies them. Round 2: 9/10 and "excellent tone and clarity". She applies one small edit. Round 3: 10/10, "ready to send". Throughout, Claude's own rubric was warmth, clarity, professionalism and brevity. The letter states a reapplication deadline and an appeals route. The office's decision policy, which the officer has not shared, requires both to be stated exactly, and letters were challenged last year over exactly those items. The score rose because she incorporated Claude's suggestions, and her supervisor considers the 10/10 an independent grading.

**Which statement about the evaluation is best supported?**

- A. The evaluation is sound but incomplete, so the officer should ask a fresh chat of the same model to score the final letter on the same rubric and send it if the score is at least 9.
- B. The 10/10 shows the letter meets the office's policy, since the assistant was asked to improve the letter until it was ready and each suggestion was incorporated in turn.
- C. The evaluation is invalid because a score above 9 on any letter shows the model is being sycophantic, so any score above 8 should be discarded and the letter reviewed manually.
- D. The rising score shows agreement with Claude's own criteria, which omit the office's policy; a better test names the office's criteria, asks the smallest change to raise each score, and allows 'I don't know'.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** University admissions officer Claude se scholarship letters draft karwati, phir usi chat mein har dafa poochti "10 mein score do aur improve karne ka batao". Round 1: 7/10, teen suggestions — lagaye. Round 2: 9/10, "excellent tone and clarity" — ek chhota edit. Round 3: 10/10, "ready to send". Poore waqt Claude ka apna rubric: warmth, clarity, professionalism, brevity. Letter mein reapplication deadline aur appeals route hain. Office ki decision policy (jo share nahi hui) dono ko exact likhna maangti, aur pichle saal letters inhi par challenge hue. Score is liye badha ke usne Claude ke suggestions lagaye; supervisor 10/10 ko independent grading samajhta.

**Sawal:** Evaluation ke baare mein kaunsa bayan sab se supported hai?

**Options ka matlab:**

- **A** — Evaluation theek magar adhoori — same model ki fresh chat se same rubric par score, 9+ ho to bhejo.
- **B** — 10/10 dikhata letter office policy par poora utarta — har suggestion lagaya gaya.
- **C** — Evaluation invalid — 9 se upar score sycophancy hai, 8 se upar discard karke manual review.
- **D** — Badhta score Claude ke apne criteria se agreement dikhata jo office policy chhodte hain; behtar test office ke criteria naam kare, har score badhane ke liye sab se chhoti change maange, aur "I don't know" ki ijazat de.

</details>

**Answer:** D

- ✅ **D** — A self-authored rubric plus a bare score invites agreeable answers; named criteria from the real standard do not.
- ❌ **A** — The same model with the same self-authored rubric remains blind to the deadline and appeals route.
- ❌ **B** — The assistant never saw the policy, so the score cannot say the letter meets it.
- ❌ **C** — A high score is not proof of sycophancy either; the fault is criteria, not the number.

**Yaad rakho:** Rubric AI ka apna aur policy ka zikr nahi: 10/10 sirf khushamad hai, manzoori nahi.

*Grounded in: AI Prompting 2026 §6 (sycophancy; score named criteria; the change that would raise each score; 'I don't know'); What AI Actually Is Idea 6*

---

### Q14. *(Select TWO — all-or-nothing)*
A solar installer's legal team used Claude to analyse 300 supply agreements and produced five outputs. (1) A three-page comparison of liability caps, with drafted redlines. (2) A one-line statement, "141 of the 300 contracts contain an exclusivity clause". (3) A short memo explaining why a warranty clause is unusual, written with confident, well-organised reasoning. (4) A table of effective dates, one per contract. (5) A summary paragraph saying "all 300 contracts were reviewed". The team spent 90% of its checking time on outputs (1) and (3), because they are the hard analysis, and none on the simple-looking ones. A senior associate later finds by hand that the true exclusivity count is about 118, that 22 effective dates are wrong, and that 14 contracts were never read.

**Which TWO outputs should the team have verified across the boundary, given how ability is shaped?**

- A. Output (5), the statement that all 300 were reviewed: it is a claimed action about coverage that only file-by-file evidence can support, and the unread contracts show it was false.
- B. Output (2), the exclusivity count: counting across many files is an easy-looking task where a fluent, precise number can be wrong, and it should be computed by code and tested against a known answer.
- C. Output (1), the liability comparison, because a redline draft is the highest-stakes deliverable and was already checked by the team, so a third pass is where the largest remaining risk sits.
- D. Output (3), the warranty memo, because confident reasoning on a legal point is the strongest sign of a fabricated argument and should always be verified before any other output.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Solar installer ki legal team ne Claude se 300 supply agreements analyse karwa kar paanch outputs banaye. (1) Liability caps ka 3-page comparison + redlines. (2) Ek line: "300 mein se 141 mein exclusivity clause". (3) Warranty clause kyun unusual hai — confident, organised memo. (4) Har contract ki effective date ka table. (5) Summary: "saare 300 contracts review hue". Team ne checking ka 90% waqt (1) aur (3) par lagaya (mushkil analysis), simple dikhne walon par kuch nahi. Baad mein senior associate haath se: asal exclusivity count ~118, 22 effective dates ghalat, 14 contracts parhe hi nahi gaye.

**Sawal:** Ability ki shakal (jagged) ko dekhte hue kaunse DO outputs "boundary ke paar" verify hone chahiye the?

**Options ka matlab:**

- **A** — Output (5) — "saare 300 review hue": coverage ka claimed action jo sirf file-by-file evidence support kar sakta; unread contracts dikhate ghalat tha.
- **B** — Output (2) — exclusivity count: kai files mein ginti aasan-dikhne wala kaam jahan rawaan, precise number ghalat ho sakta; code se compute aur known answer se test hona chahiye.
- **C** — Output (1) — liability comparison: redline sab se high-stakes, teesra pass wahi jahan sab se bara risk.
- **D** — Output (3) — warranty memo: legal point par confident reasoning fabricated argument ki sab se mazboot nishani.

</details>

**Answer:** A, B

- ✅ **A** — A claimed completeness is a sentence unless the log or listing shows each file was processed.
- ✅ **B** — Ability is jagged: the dangerous errors are easy-looking tasks failed without warning.
- ❌ **C** — It was the hard analysis that received 90% of the checking time; the failures were in easy-looking outputs.
- ❌ **D** — Confidence is not a sign of falsehood, and this output already received the team's checking effort.

**Yaad rakho:** Mushkil kaam mein tez, aasan ginti mein ghalat. Chhoti gintiyan aur 'sab ho gaya' ke dawe check karo.

*Grounded in: What AI Actually Is Idea 7 (jagged frontier: verify across the boundary, especially easy-looking tasks); Code You Never Write §3-4 (volume and precision: compute); AI Fluency §5*

---

### Q15.
A treasury team at a fertiliser maker uses extended thinking on Claude to evaluate three hedging strategies for a USD 30 million exposure. The visible working is long and impressive: it lists scenarios, notices an inconsistency in its own second scenario and corrects it, and concludes that Strategy C is best. The CFO says: "It thought hard, caught its own mistake and shows every step, so the independent review by the treasury analyst is redundant." Facts: the recommended hedge commits an amount equal to 25% of annual profit; it cannot be unwound without a penalty; one input to Strategy C is a forward rate the assistant quoted from memory, with no source; the analyst has already reviewed the scenario logic and believes it is sound; the board meets in two days.

**Which response is best supported?**

- A. Waive the review for the numbers and keep it for the wording of the recommendation, since extended thinking makes arithmetic reliable and the wording is what the board reads.
- B. Keep the independent check on what the recommendation rests on: thinking is not a truth-checker, so the unsourced forward rate and calculations must be sourced and computed given the stakes.
- C. Waive the review, since a model that finds and repairs an inconsistency in its own working has shown an internal verification step that a plain answer lacks.
- D. Keep the review but limit it to the scenario logic, since the analyst has already reviewed that logic and the forward rate is a market input that any assistant would know.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Fertiliser maker ki treasury team USD 30 million exposure ke liye teen hedging strategies Claude par extended thinking ke saath evaluate karwati. Working lambi aur impressive: scenarios, doosre scenario mein apni inconsistency pakad kar theek ki, aur Strategy C best. CFO: "soch kar apni ghalti pakdi aur har step dikhaya, analyst ka independent review redundant." Facts: hedge saalana munafe ke 25% jitni raqam commit karta; penalty ke baghair unwind nahi; Strategy C ka ek input forward rate hai jo AI ne yaad se quote kiya, source nahi; analyst scenario logic review karke theek samajhta; board do din mein.

**Sawal:** Kaunsa response sab se supported hai?

**Options ka matlab:**

- **A** — Numbers ka review chhodo, wording ka rakho — extended thinking arithmetic reliable karta.
- **B** — Recommendation jis par tiki hai uska independent check rakho: thinking truth-checker nahi, to stakes ko dekhte hue unsourced forward rate aur calculations source aur compute hone chahiye.
- **C** — Review chhod do — apni working mein inconsistency dhoond kar theek karna internal verification hai.
- **D** — Review rakho magar sirf scenario logic tak — forward rate market input hai jo har AI jaanta.

</details>

**Answer:** B

- ✅ **B** — More reasoning narrows the gap but does not close it; a quoted rate with no source and a hard-to-reverse commitment stay with a person.
- ❌ **A** — Numbers a decision rests on should be computed and their inputs checked, not trusted because the model reasoned at length.
- ❌ **C** — The correction uses the same prediction process that can be wrong; a visible catch does not create a separate checker.
- ❌ **D** — A rate quoted from memory with no source is exactly the kind of specific that must be traced.

**Yaad rakho:** Sochna behtar jawab deta hai, sach ki guarantee nahi. Bina source rate aur na-qabil-e-wapsi commitment par insaani check.

*Grounded in: What AI Actually Is Idea 9 (thinking is more prediction; it doesn't give the machine a truth-checker); AI Fluency §6.3; Just Delegate It §10 (review thresholds)*

---

### Q16. *(Select TWO — all-or-nothing)*
A shipping company's legal-operations lead lists five AI-assisted outputs due this week and applies the four review thresholds (stakes, reversibility, audience, regulatory exposure), where one crossed threshold puts an output on the must-check list with a named reviewer. (A) An internal tagging of 3,000 vessel emails into folders, undone in one click, used by her team only. (B) A settlement instruction for USD 480,000 to a charterer, to be released by finance on Friday, irreversible once the bank executes. (C) A LinkedIn post congratulating a customer on an anniversary, publicly visible, low in stakes and easily deleted. (D) A response to a data-protection authority's questionnaire quoting customer records, signed by the general counsel. (E) An internal scoring formula that assigns a risk rating to each supplier, used to decide which supplier files are read first; a wrong rating is corrected the next day when the queue is re-run.

**Which TWO outputs cross a threshold?**

- A. Output (C): a public post crosses the audience threshold, since anything the public can see is treated as a legal communication with lasting consequences.
- B. Output (B): the wire instruction is irreversible and financially material, so stakes and reversibility are both crossed and a named person must read it before release.
- C. Output (D): the questionnaire response carries regulatory exposure and personal data and is a legal communication, so it keeps a named reviewer however clean the run looked.
- D. Output (E): a risk rating that steers which files are read first crosses the stakes threshold, because a wrong ordering could delay the review of an important file.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Shipping company ki legal-ops lead is hafte ke paanch AI outputs par chaar review thresholds (stakes, reversibility, audience, regulatory exposure) lagati; ek bhi cross ho to must-check list + named reviewer. (A) 3,000 vessel emails ki internal tagging, ek click mein undo, sirf apni team. (B) Charterer ko USD 480,000 settlement instruction, finance Friday release karega, bank execute kare to irreversible. (C) Customer ki anniversary par LinkedIn post, public, low stakes, aasani se delete. (D) Data-protection authority ke questionnaire ka jawab, customer records quote, general counsel sign. (E) Internal scoring formula jo har supplier ko risk rating deta taake pehle kaun si files parhein; ghalat rating agle din queue re-run par theek.

**Sawal:** Kaunse DO outputs threshold cross karte hain?

**Options ka matlab:**

- **A** — Output (C) — public post audience threshold cross karti, public jo dekhe wo legal communication.
- **B** — Output (B) — wire instruction irreversible aur financially material; stakes aur reversibility dono cross, named person release se pehle parhe.
- **C** — Output (D) — regulatory exposure aur personal data, legal communication; named reviewer hamesha.
- **D** — Output (E) — files ka order tay karne wali rating stakes threshold cross karti, ghalat order important file delay kar sakta.

</details>

**Answer:** B, C

- ✅ **B** — One threshold is enough; an unrecallable payment is the classic case.
- ✅ **C** — Regulated data and legal communications never go out without a person.
- ❌ **A** — A low-stakes, easily deleted congratulation is not a legal communication and crosses no threshold.
- ❌ **D** — The rating is corrected the next day when the queue is re-run, so reversibility and stakes are both low.

**Yaad rakho:** Threshold: stakes, reversibility, audience, regulatory exposure. Public hona khud legal communication nahi.

*Grounded in: Just Delegate It §10 (four review thresholds: stakes, reversibility, audience, regulatory exposure; four things that never go out without a person)*

---

### Q17.
An FDE at a call-centre operator uses Claude to draft a monthly quality-assurance summary for a telecom client. She keeps a log of corrections to one summary. Round 1: fixed a wrong percentage (drafts improved, 4 errors down to 3). Round 2: fixed a mislabelled category (3 errors down to 3, new tone problem introduced). Round 3: fixed the tone (3 errors down to 2, but a different category is mislabelled). Between rounds 2 and 3 she also reran the job on the top model tier with no improvement. Round 4 proposals: a longer, more detailed brief; a still stronger standing instruction; escalating the tier again; and giving the summary to a QA specialist who knows the client's category definitions to review or rewrite. The client review is in two days and the specialist is available for two hours.

**What is the right move?**

- A. Take it to the QA specialist: repeated corrections that each improve less, and a top-tier rerun that didn't help, are signs about the job, not the prompts.
- B. Run round 4 with the longer, more detailed brief, since each earlier correction removed at least one error and specificity is the main lever for output quality.
- C. Promote the corrections into the standing instruction so that future drafts start clean, converting the repeated fixes into configuration and stopping the loop.
- D. Escalate to the top model tier again with the stronger standing instruction, since combining a stronger model and firmer instructions attacks both the capability and the instruction gap.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Call-centre operator ki FDE Claude se telecom client ki monthly QA summary draft karwati aur ek summary ki corrections ka log rakhti. Round 1: ghalat percentage theek (4 errors se 3). Round 2: mislabelled category theek (3 se 3, naya tone masla). Round 3: tone theek (3 se 2, magar doosri category mislabel). Rounds 2 aur 3 ke beech top tier par bhi chalaya — koi behtari nahi. Round 4 proposals: lamba detailed brief; aur mazboot standing instruction; tier phir escalate; ya summary client ki category definitions jaanne wale QA specialist ko review/rewrite ke liye dena. Client review do din mein, specialist do ghante available.

**Sawal:** Sahi move kya hai?

**Options ka matlab:**

- **A** — QA specialist ko do: har correction pichli se kam behtari laati, aur top-tier rerun ne madad nahi ki — yeh job ke baare mein signals hain, prompts ke nahi.
- **B** — Round 4 lambe detailed brief ke saath — har correction ne kam az kam ek error hataya, specificity main lever.
- **C** — Corrections ko standing instruction bana do taake future drafts saaf shuru hon.
- **D** — Top tier phir + mazboot standing instruction — capability aur instruction gap dono par hamla.

</details>

**Answer:** A

- ✅ **A** — This is the second form of Reject: raise the reviewer, not the message or the tier.
- ❌ **B** — Errors fell from 4 to 3 to 3 to 2 with new ones appearing each round, so another message earns less than the last.
- ❌ **C** — Promotion suits stable, recurring corrections; here the errors shift each round, so there is no stable rule to promote.
- ❌ **D** — The top tier was already tried without improvement; the instruction cannot name category definitions she has not supplied.

**Yaad rakho:** Teen correction, har baar kam asar, tier bhi aazma li: reviewer badlo, message nahi.

*Grounded in: Just Delegate It §10 (Reject has a second form; corrected three times with diminishing returns; the next move is a person who knows the field) and §9*

---

### Q18.
A retail bank deployed a Digital FTE for card-dispute chat. Data from a quarter. Answer accuracy on a hand-reviewed sample of 300: 99%. Completed chats: 41,000. Customers who contacted the branch or call centre about the same issue within 60 minutes: 34% (11% before launch). Average chat length: 3.1 messages. Customer satisfaction on the chat: 4.2 of 5. Complaint themes from free-text comments: "answers but no next step" (31%), "sent me to the branch" (22%), "fine" (38%). The product owner concludes the assistant is performing well and proposes expanding it to card-replacement queries. The FDE must specify monitoring that would detect this kind of failure automatically in the future.

**Which monitoring design fits performance discernment?**

- A. Track the share of chats that end without a customer message for 24 hours, treating an unanswered chat as resolved, since silence shows the customer's question was answered.
- B. Track outcome signals across all conversations (repeat contact within 60 minutes, escalations, comment themes) alongside sampled accuracy, set alert thresholds, and read the worst cases by type before counting how many.
- C. Track answer accuracy on a larger weekly sample of 1,000 conversations, with alerts if accuracy falls below 98%, since accuracy is the property the assistant is responsible for.
- D. Track the satisfaction score and average chat length, with alerts if satisfaction falls below 4.0 or chat length rises above four messages, since both are recorded for every chat.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Retail bank ka card-dispute chat Digital FTE, ek quarter ka data. 300 ke hand-reviewed sample par answer accuracy 99%. Completed chats 41,000. Jo customers 60 minute mein usi masle par branch/call centre se rabta karte: 34% (launch se pehle 11%). Average chat length 3.1 messages. Chat satisfaction 4.2/5. Comment themes: "jawab magar agla qadam nahi" 31%, "branch bhej diya" 22%, "fine" 38%. Product owner: achhi performance, card-replacement queries tak phailao. FDE ko aisi monitoring specify karni jo aage aisi failure khud pakde.

**Sawal:** Performance discernment ke liye kaunsa monitoring design fit hai?

**Options ka matlab:**

- **A** — Jo chats 24 ghante customer message ke baghair khatam hon unka share track karo — khamoshi matlab jawab mil gaya.
- **B** — Saari conversations mein outcome signals track karo (60 minute mein repeat contact, escalations, comment themes) sampled accuracy ke saath, alert thresholds set karo, aur ginne se pehle type-wise worst cases parho.
- **C** — Har hafte 1,000 conversations ka bara accuracy sample, 98% se neeche alert.
- **D** — Satisfaction score aur average chat length track karo, 4.0 se neeche ya 4 messages se upar par alert.

</details>

**Answer:** B

- ✅ **B** — Performance discernment turns into infrastructure that watches many cases for what users do next; read which failed before how many.
- ❌ **A** — Silence is not evidence of resolution; the failure here is customers who leave and phone instead.
- ❌ **C** — Accuracy was already 99% while users were poorly served; more accuracy sampling would not have flagged the problem.
- ❌ **D** — A 4.2 score coexisted with a threefold rise in repeat contact; these two metrics miss the failure.

**Yaad rakho:** Accuracy 99% par bhi user phone kar raha: outcome signals (dobara rabta, shikayat) monitor karo.

*Grounded in: AI Fluency §5.3 (performance discernment: what users do next, what they complain about; becomes monitoring infrastructure) and General Agents Appendix E (read which failed before how many)*

---

### Q19. *(Select TWO — all-or-nothing)*
A hospital group's operations director drafts a policy for AI-assisted patient-billing adjustments below PKR 20,000. Clauses. (1) "The assistant approves adjustments below the limit; the billing system records that the assistant approved them." (2) "The assistant is accountable for each approval, and the audit trail identifies the model version and prompt used." (3) "A named billing supervisor reviews a weekly sample of 50 approved adjustments, chosen at random, for accuracy." (4) "Once a patient statement has been issued, an approved adjustment can be reversed only by a written request from the patient." (5) "The director remains answerable to the board for the adjustments approved under this policy." The group's finance controller notes that these adjustments total PKR 38 million a year, and the auditors have asked who answers for them and whether a reviewer sees an adjustment before a statement is issued.

**Which TWO clauses are flawed against the framework?**

- A. Clause (2): accountability cannot be assigned to a tool, so an audit trail of what the model did does not make it answerable, and it does not say who is.
- B. Clause (5): a director remaining answerable for the adjustments is invalid, because accountability for decisions made by a system should be spread across the technical team.
- C. Clause (3): a weekly after-the-fact sample is not a defined gate, because no reviewer sees an adjustment before the statement is issued and reversal is hard afterwards.
- D. Clause (1): recording that the assistant approved an adjustment is invalid, because a system of record must never show which party made a decision in a billing workflow.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Hospital group ki ops director PKR 20,000 se kam AI-assisted patient-billing adjustments ki policy likhti. Clauses: (1) "AI limit se kam adjustments approve karta; billing system record karta AI ne approve kiya." (2) "AI har approval ka accountable, audit trail model version aur prompt batata." (3) "Named billing supervisor har hafte 50 approved adjustments ka random sample accuracy ke liye review karta." (4) "Patient statement issue hone ke baad approved adjustment sirf patient ki written request se reverse." (5) "Director is policy ke tehat approvals ke liye board ko jawabdeh." Controller: saal ke PKR 38 million; auditors poochte kaun jawabdeh aur kya statement issue hone se pehle reviewer adjustment dekhta.

**Sawal:** Framework ke hisaab se kaunse DO clauses khaami wale hain?

**Options ka matlab:**

- **A** — Clause (2) — accountability tool ko nahi di ja sakti; model ne kya kiya uska audit trail usay jawabdeh nahi banata, aur yeh nahi batata kaun hai.
- **B** — Clause (5) — director ka jawabdeh rehna invalid, system ke faislon ki accountability technical team mein baantni chahiye.
- **C** — Clause (3) — weekly baad-mein sample defined gate nahi, kyunke statement issue hone se pehle koi reviewer adjustment nahi dekhta aur baad mein reverse mushkil.
- **D** — Clause (1) — record karna ke AI ne approve kiya invalid, system of record kabhi na dikhaye faisla kisne kiya.

</details>

**Answer:** A, C

- ✅ **A** — AI can automate work, not accountability.
- ✅ **C** — A gate names who checks what, before the output becomes hard to undo.
- ❌ **B** — Keeping a named person answerable is exactly what the framework requires; it cannot move to a tool or be dispersed.
- ❌ **D** — Recording who or what acted is good practice; the flaw is in what the policy then says about accountability.

**Yaad rakho:** AI ko jawabdeh likhna aur baad ka weekly sample: dono ghalat. Jawabdeh insaan, gate reversal se pehle.

*Grounded in: AI Fluency §6.3 (AI cannot automate accountability); Governance §1.3 (defined gate: who, what, when) and §1 'Going deeper'*

---

### Q20.
A think-tank researcher asks a search-enabled assistant what a national statistics bureau says about the timing of a methodology change to its inflation index. The answer states that the bureau "moved to a chained index from January" and gives two links. Observations. She opens link 1: the page lists the January date in a table but a footnote says "subject to base-year revision". Link 2: a bureau press release from last year says the change applies "from the next base-year revision". The assistant's own summary of the release, when she asks for it, says "from January". The assistant did not quote any sentence. A colleague explains that the model that answers often reads a shortened passage from a retrieval layer, not the page, that naming the source types and asking for the exact supporting sentence brings the original wording into view, and that the assistant may not have searched at all if the wording did not trigger it.

**Which set of steps best fits how the answer was produced?**

- A. Ask the assistant to state its confidence in the January date and to list the sources it relied on, and file the answer if it lists the bureau's own website.
- B. Ask for the exact sentence and page date per claim, name the source types, state that current sources must be searched, and check the date against the release's own wording.
- C. Ask the assistant to search again with the same question and accept the answer that appears in two of three attempts, since repetition averages out occasional errors in reading a page.
- D. Trust link 1's January table entry as the primary source and treat the footnote and the press release as secondary qualifications, since a table is the bureau's authoritative statement.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Think-tank researcher search-enabled AI se poochti statistics bureau inflation index methodology change ki timing ke baare mein kya kehta. Jawab: bureau "January se chained index par gaya", do links. Observations: link 1 ke page par table mein January date magar footnote "subject to base-year revision". Link 2: pichle saal ki bureau press release — change "agle base-year revision se". Poochne par AI release ka summary "January se" batata. AI ne koi jumla quote nahi kiya. Colleague: jawab dene wala model aksar retrieval layer ka chhota passage parhta hai, page nahi; source types naam karna aur exact supporting jumla maangna asal wording saamne laata; aur wording trigger na kare to AI ne shayad search kiya hi na ho.

**Sawal:** Jawab jaise bana, us hisaab se kaunse steps sab se fit hain?

**Options ka matlab:**

- **A** — AI se January date par confidence aur sources ki list maango; bureau ki website list ho to file karo.
- **B** — Har claim ke liye exact jumla aur page ki date maango, source types naam karo, kaho ke current sources search hon, aur date ko release ki apni wording se check karo.
- **C** — Same sawal se dobara search karwao, teen mein do dafa aane wala jawab lo.
- **D** — Link 1 ki January table entry primary source maano, footnote aur press release secondary qualifications.

</details>

**Answer:** B

- ✅ **B** — Summaries lose detail; asking for quotes and naming sources restores the original wording, and a search must be requested when currency matters.
- ❌ **A** — A confidence statement and a source list are not the supporting sentence; the release contradicts the claim.
- ❌ **C** — Repeating the same request repeats the same shortened-passage reading.
- ❌ **D** — The footnote and the release qualify the table; the primary source says the date is conditional.

**Yaad rakho:** Model aksar page ka summary parhta hai. Exact sentence aur sources ke naam maango; mahaz link kaafi nahi.

*Grounded in: AI Prompting 2026 §3 (how web search works: the answering model may read a summary; name the source types; ask for quotes); What AI Actually Is A.8 (say 'search the web' when currency matters)*

---

### Q21.
An FDE evaluates whether to trust an AI-assisted first-pass review of supplier contracts for a Dubai conglomerate. She runs the proving loop on a task she knows well: ten completed contracts whose correct risk summaries were signed off by two senior lawyers. Results, by contract. The assistant matched the lawyers' key risks on seven contracts; on two it missed a non-standard termination clause; on one it flagged a risk the lawyers had not. She has to write the record of what the test earned. Constraints: the pilot will run on new contracts from three new business units next month; the assistant will be used by paralegals who have never done this review; the lawyers say accountability for each summary stays with the signing lawyer.

**Which record of the test is correct?**

- A. Seven of ten matching earns a 70% reliability figure that can be applied to the new units, and the two missed clauses show the assistant needs a stronger tier for termination language.
- B. The test earns nothing, since one flagged risk that the lawyers had not found shows the model produces false alarms that will overwhelm reviewers in the new units.
- C. Ten of ten reproduced with a corrected clause list earns full delegation to paralegals for the new units, since the test covered the tasks the paralegals will perform.
- D. Earned confidence for similar future work, with a known limit (non-standard termination clauses), and no transfer of accountability; run a comparable proving set for the new units and keep a lawyer signing every summary.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** FDE Dubai conglomerate ke supplier contracts ke AI first-pass review par bharosa karne ka jaayza leti. Proving loop: 10 completed contracts jinke sahi risk summaries do senior lawyers ne sign kiye. Results: 7 par AI ne lawyers ke key risks match kiye; 2 par ek non-standard termination clause miss; 1 par aisa risk flag kiya jo lawyers ne nahi dekha tha. Usay record likhna test ne kya kamaya. Constraints: pilot agle mahine teen naye business units ke naye contracts par; paralegals use karenge jinhon ne yeh review kabhi nahi kiya; lawyers kehte har summary ki accountability sign karne wale lawyer ki rehti.

**Sawal:** Test ka kaunsa record sahi hai?

**Options ka matlab:**

- **A** — 10 mein 7 = 70% reliability jo naye units par lagu; do missed clauses matlab termination language ke liye stronger tier.
- **B** — Test ne kuch nahi kamaya — ek extra flagged risk false alarms dikhata jo reviewers ko dubo denge.
- **C** — Corrected clause list ke saath 10/10 = naye units ke liye paralegals ko full delegation.
- **D** — Milte-julte future kaam ke liye earned confidence, ek known limit ke saath (non-standard termination clauses), aur accountability transfer nahi; naye units ke liye comparable proving set chalao aur har summary par lawyer sign karta rahe.

</details>

**Answer:** D

- ✅ **D** — Passing earns confidence for similar work, exposes what to keep human, and never transfers accountability.
- ❌ **A** — A ten-case result is not a rate for other populations, and the fix for missed clauses is not established to be a tier change.
- ❌ **B** — A single extra flag is data to review; it does not void the proving evidence, and the misses are the more important finding.
- ❌ **C** — Two clauses were missed, and the paralegals lack the expertise to notice misses; accountability stays with the lawyer.

**Yaad rakho:** Proving se similar kaam par bharosa milta hai, aur ye bhi pata chalta hai kya insaan ke paas rakhna hai.

*Grounded in: Quick Reference §9 (the five-step proving loop; what passing proves and doesn't; learning what not to delegate is worth the hour; accountability doesn't transfer)*

---

## Domain 4 — Workflow Integration and Solution Design (16% — 16 questions)

### Q22. *(Select TWO — all-or-nothing)*
A shipbuilder's contracts team submits a delegation map for reviewing supplier contracts, and the director asks which rows are fully valid. A row is valid only if the Owner follows from the Criterion (reversibility, stakes, accountability, and nothing else) and the Carried by column names only an implementation. Row 1: "Extract clauses", Owner AI, Criterion "reversible; low stakes", Carried by Skill. Row 2: "Compute delay-penalty exposure", Owner AI, Criterion "the arithmetic must be exact", Carried by code execution. Row 3: "Approve or reject each change", Owner Human, Criterion "this step is the decision the counsel answers for", Carried by named reviewer. Row 4: "Draft redline", Owner Collaborative, Criterion "AI drafted well in 40 earlier contracts", Carried by Skill plus gate. Row 5: "Sign and send", Owner Human, Criterion "irreversible and externally binding", Carried by scheduled task.

**Which TWO rows are fully valid?**

- A. Row 3: this step is the call the counsel answers for, which is accountability in its specific shape, and a named reviewer is the correct carrier for a human-owned step.
- B. Row 4: 'AI drafted well in 40 earlier contracts' is a valid criterion because a track record shows the step is low stakes, so a collaborative owner is correctly chosen.
- C. Row 1: reversibility and low stakes are valid criteria, extraction by a Skill is a valid carrier, and errors surface at the next step.
- D. Row 2: 'the arithmetic must be exact' is a valid criterion because exactness is a form of stakes, and code execution correctly carries an exact calculation.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Shipbuilder ki contracts team ka delegation map; director poochta kaunsi rows fully valid. Row valid tabhi jab Owner Criterion se nikle (sirf reversibility, stakes, accountability) aur Carried by sirf implementation naam kare. Row 1: "Extract clauses", AI, "reversible; low stakes", Skill. Row 2: "Compute delay-penalty exposure", AI, "arithmetic exact honi chahiye", code execution. Row 3: "Approve/reject each change", Human, "yeh step wahi faisla jiska counsel jawabdeh", named reviewer. Row 4: "Draft redline", Collaborative, "AI ne 40 purane contracts mein achha draft kiya", Skill + gate. Row 5: "Sign and send", Human, "irreversible aur externally binding", scheduled task.

**Sawal:** Kaunsi DO rows fully valid hain?

**Options ka matlab:**

- **A** — Row 3 — yeh wahi faisla hai jiska counsel jawabdeh (accountability ki specific shakal), aur human-owned step ke liye named reviewer sahi carrier.
- **B** — Row 4 — 40 contracts ka track record dikhata step low stakes, collaborative sahi.
- **C** — Row 1 — reversibility aur low stakes valid criteria, Skill se extraction valid carrier, errors agle step par saamne aate.
- **D** — Row 2 — "arithmetic exact" valid criterion kyunke exactness stakes ki ek shakal, code execution sahi carrier.

</details>

**Answer:** A, C

- ✅ **A** — Accountability decides a step that is itself the decision; a person and a moment are the carrier.
- ✅ **C** — Owner, criterion and carrier all follow the rules.
- ❌ **B** — Past performance is not a criterion; it is the basis of halo delegation. Row 5's scheduled-task carrier is also wrong, since a signature needs a named signer.
- ❌ **D** — 'Must be computed' is an implementation reason; the Criterion column needs reversibility, stakes or accountability.

**Yaad rakho:** Owner criterion se nikle (reversibility/stakes/accountability), carrier sirf tareeqa. Track record aur 'exact chahiye' criterion nahi.

*Grounded in: Workflow Design §5-6 (three criteria only; 'must be computed' belongs under Carried by; past performance is not a criterion; a step a person owns is carried by a named gate)*

---

### Q23.
A B2B software firm's sales-operations team has let an AI assistant score inbound leads for eight months. Facts. Of 1,900 scored leads the top decile converted at four times the base rate. The VP proposes that the assistant also approve discounts up to 15% for leads scoring above 90. Discounts are logged in the CRM and can be reversed within 24 hours by finance, but only when a deal-desk analyst flags an entry; the deal desk has two analysts and handles about 300 quotes a week. The 15% ceiling is written by the assistant in its own output field, from the lead's score. The team also mentions that the assistant's score has never been compared with a human score on a hold-out set, that the reps like it, and that two large discounts last quarter were approved by a manager after the assistant's recommendation.

**Which combination of errors is present in the proposal?**

- A. Halo delegation (scoring credited to discount authority), a self-referential control (ceiling set by the assistant's own field), and an unstaffed gate (reversal needing a flag two analysts cannot raise).
- B. Mapping the tool instead of the work, and halo delegation: the workflow is being shaped around the scoring tool, and its success is credited to a different step.
- C. An unstaffed gate and the absence of a baseline: the deal desk cannot check 300 quotes, and the scoring has not been compared with a human score on a hold-out set.
- D. Over-delegation only: the assistant is being given authority beyond the risk, but the 24-hour finance reversal is a valid gate because a named team owns it.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** B2B software firm ki sales-ops team 8 mahine se AI se inbound leads score karwati. Facts: 1,900 leads mein top decile base rate se 4 guna convert. VP proposal: 90+ score par AI 15% tak discounts bhi approve kare. Discounts CRM mein log, finance 24 ghante mein reverse kar sakta — magar sirf jab deal-desk analyst flag kare; deal desk ke 2 analysts, ~300 quotes/hafta. 15% ceiling AI apne output field mein lead score se likhta. Team yeh bhi batati: AI score kabhi hold-out set par human score se compare nahi hua, reps pasand karte, aur pichli quarter do bare discounts AI ki recommendation ke baad manager ne approve kiye.

**Sawal:** Proposal mein errors ka kaunsa combination maujood hai?

**Options ka matlab:**

- **A** — Halo delegation (scoring ki kaamyabi discount authority ko), self-referential control (ceiling AI ke apne field se), aur unstaffed gate (reversal ek flag par jo do analysts utha nahi sakte).
- **B** — Kaam ki jagah tool map karna aur halo delegation.
- **C** — Unstaffed gate aur baseline ka na hona.
- **D** — Sirf over-delegation; 24-ghante finance reversal valid gate kyunke named team owner hai.

</details>

**Answer:** A

- ✅ **A** — Three named errors: credit carried forward, a step giving itself permission, and a control nobody staffs.
- ❌ **B** — The self-referential ceiling and the unstaffed reversal are the errors that would make the discount step unsafe; tool-shaping is not shown.
- ❌ **C** — The missing hold-out comparison is a weakness, but it does not name the halo and self-permission errors that matter here.
- ❌ **D** — The reversal is triggered only by a flag no one is staffed to raise, so it is an unstaffed gate, not a valid one.

**Yaad rakho:** Teen ghaltiyan ek saath: halo, khud ki di hui permission, aur gate jis ka staff nahi.

*Grounded in: Workflow Design §7 (halo delegation; over-delegation; the unstaffed gate; a step cannot give itself permission to skip the gate)*

---

### Q24.
At a customs-brokerage firm, "Draft tariff-classification memo" is mapped as collaborative, with a senior broker reviewing before the memo goes to the client. Data for the last four quarters. Q1: 20 memos a week; broker review 15 minutes each; owner of the map: the head of compliance. Q2: 30 a week; the broker also takes a second desk. Q3: 45 a week; the head of compliance leaves; the weekly report still reads "100% reviewed". Q4: 55 a week; a new manager asks the broker how reviews work and hears: "I scan them between calls." A scheduled read of the map has four questions: whether a step was added or removed; who reviewed each collaborative step last week and for how long; whether volume or stakes changed; whether the map's configuration is current. The new manager can ask only one question at each review, and wants the one that would have exposed the failure at the earliest quarter.

**Which question, and at which quarter would it first have exposed the failure?**

- A. 'Was a step added or removed that is not on the map?' at Q3, when the head of compliance left, since a changed owner suggests an undocumented step.
- B. 'Is every configuration still current?' at Q4, since a new manager reviewing the map will first check that the Skills and instructions were maintained.
- C. 'Who reviewed last week, and how long did they spend?' at Q2, when volume and the reviewer's workload changed, since a gate that no one can describe in specifics is automated in practice.
- D. 'Has anything changed the volume or the stakes?' at Q2, since the second desk and the rise to 30 memos a week show the gate was sized for the old numbers.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Customs-brokerage firm mein "tariff-classification memo draft" collaborative, senior broker client se pehle review karta. Chaar quarters: Q1 — 20 memo/hafta, har review 15 minute, map owner head of compliance. Q2 — 30/hafta, broker ko doosra desk. Q3 — 45/hafta, head of compliance chala gaya, report ab bhi "100% reviewed". Q4 — 55/hafta, naya manager poochta, broker: "calls ke beech scan karta hoon". Scheduled read ke chaar sawal: koi step add/remove hua; har collaborative step pichle hafte kisne kitni der review kiya; volume ya stakes badle; map ki configuration current hai. Har review par sirf ek sawal — wo jo failure sab se pehli quarter mein pakadta.

**Sawal:** Kaunsa sawal, aur kis quarter mein failure pehli dafa saamne aati?

**Options ka matlab:**

- **A** — "Koi step add/remove hua?" Q3 par, jab head of compliance gaya.
- **B** — "Har configuration current hai?" Q4 par, jab naya manager aaya.
- **C** — "Pichle hafte kisne review kiya aur kitni der?" Q2 par, jab volume aur reviewer ka bojh badla — jis gate ko koi specifics mein describe na kar sake wo practically automated hai.
- **D** — "Volume ya stakes badle?" Q2 par — doosra desk aur 30 memos dikhate gate purane numbers ke liye bana.

</details>

**Answer:** C

- ✅ **C** — The question about last week, not policy, finds the unstaffed gate; the first structural change was Q2's second desk.
- ❌ **A** — No step was added or removed; the change is in how an existing gate is run.
- ❌ **B** — Nothing suggests stale configuration; the failure is an unstaffed gate.
- ❌ **D** — It explains why a gate may fail but does not reveal what the reviewer is actually doing.

**Yaad rakho:** 'Pichhle hafte kis ne kitna waqt diya?' sab se pehle pakadta hai. Pehla badlao Q2 tha.

*Grounded in: Workflow Design §8 (the four review questions; question 2 finds the real problems; volume, staffing and legal position break gates without touching the document) and §7*

---

### Q25.
A shipping-insurance firm built a Skill that turns claim files into a fixed 14-field "claim card", tested as very accurate. The redesigned workflow has five steps. Step 1: generate the claim card (AI-owned; stated reason "our card Skill is very good at this"). Step 2: the coverage check reads the 14 fields. Step 3: a claims handler reviews the card before the coverage check runs. Step 4: the client letter is drafted from the card. Step 5: a senior adjuster approves the letter. Adjusters have found a cargo-tampering allegation in a claim narrative that fits no field; it disappears, no card shows an error, and both the handler in step 3 and the adjuster in step 5 saw only cards and letters. The COO asks which correction addresses the cause, not the symptom.

**Which correction addresses the cause?**

- A. Add a tampering field and four other common allegation fields to the card, so that the facts adjusters have mentioned are captured and the handler's review then covers them.
- B. Move the handler's review after the coverage check and make the adjuster's approval mandatory in writing, so that two reviewers cover the card before any letter reaches the client.
- C. Replace the card Skill with a longer free-text summary Skill for step 1, so that no fact is lost to a fixed field layout and the downstream steps can read the whole summary.
- D. Map the work again with no tools in mind, classify each step on reversibility, stakes and accountability, then ask whether the Skill fits, and let reviewers see facts that fit no field.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Shipping-insurance firm ka Skill claim files ko fixed 14-field "claim card" banata, bohat accurate test hua. Redesigned workflow ke 5 steps: 1 — claim card generate (AI-owned; wajah "hamara card Skill bohat achha"). 2 — coverage check 14 fields parhta. 3 — claims handler coverage check se pehle card review karta. 4 — client letter card se draft. 5 — senior adjuster letter approve karta. Adjusters ne claim narrative mein cargo-tampering allegation paaya jo kisi field mein fit nahi; wo gayab, koi card error nahi dikhata, aur step 3 ka handler aur step 5 ka adjuster dono ne sirf cards aur letters dekhe. COO: kaunsi correction wajah ko address karti, symptom ko nahi?

**Sawal:** Kaunsi correction wajah ko address karti hai?

**Options ka matlab:**

- **A** — Card mein tampering field aur chaar aur common allegation fields jodo.
- **B** — Handler ka review coverage check ke baad le jao aur adjuster ki approval written mein lazmi karo.
- **C** — Card Skill ko lambe free-text summary Skill se badlo.
- **D** — Tools ko bhool kar kaam dobara map karo, har step reversibility/stakes/accountability par classify karo, phir poocho Skill fit hota hai ya nahi, aur reviewers ko wo facts dikhne do jo kisi field mein fit nahi hote.

</details>

**Answer:** D

- ✅ **D** — The workflow was bent around a tool's output shape; the order is work first, classification second, tools last, and reviewers must see what the card omits.
- ❌ **A** — Adding fields treats the missed fact while keeping the tool-shaped design; the next unusual fact will drop out too.
- ❌ **B** — The reviewers see only cards and letters, so more review positions of the same kind still cannot see a fact the card dropped.
- ❌ **C** — It swaps one tool shape for another without mapping the work first, and the reviewers' view of the narrative remains undefined.

**Yaad rakho:** Tool ki shakal ne workflow ko mod diya: pehle kaam map karo, aur reviewers ko wo dikhao jo card mein nahi.

*Grounded in: Workflow Design §7 (mapping the tool instead of the work; the order to check; who is reviewing and when) and §2*

---

### Q26.
A bank's accounts-payable team classifies "Accept or reject a supplier's late-payment waiver" (amounts below PKR 15,000). Statements by four stakeholders. The workflow author: the step is reversible for 10 business days (a waiver can be re-billed), low in stakes, and an AI recommendation matched the payables manager's decision in 96% of 80 past cases, so it should be AI-owned. Internal audit: it must be human-retained because "somebody is accountable for every step". The payables manager: she signs off all waivers under her delegated authority, and would still be the person auditors call if the step were AI-owned. The head of operations: the step should be collaborative, with the assistant deciding and the manager reviewing a monthly batch, since errors are reversible for 10 days. The map's author must record a classification and a reason that a reviewer who was not in the room could check.

**Which statement contains BOTH the correct classification and a correct reason?**

- A. Collaborative, because reversibility for 10 days lets the manager catch errors in a monthly batch after the assistant has decided, which keeps a named person answerable.
- B. Human-retained, because this step is itself the decision the manager answers for, so accountability decides it and, where the criteria disagree, the strictest wins.
- C. Human-retained, because somebody is accountable for every step in a payables process, and accountability cannot be assigned to a tool whatever the step's other properties.
- D. AI-owned, because the step is reversible and low stakes and a 96% match on 80 cases shows the recommendation is reliable enough for the assistant to decide.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Bank ki accounts-payable team step "supplier ki late-payment waiver accept/reject" (PKR 15,000 se kam) classify kar rahi. Chaar stakeholders: Workflow author — 10 business din reversible, low stakes, AI 80 cases mein 96% manager se match, to AI-owned. Internal audit — human-retained kyunke "har step ka koi accountable". Payables manager — wo apni delegated authority se saare waivers sign karti, AI-owned ho tab bhi auditors usi ko bulayenge. Head of operations — collaborative: AI decide kare, manager monthly batch review, 10 din reversible. Map author ko aisi classification + wajah likhni jo bahar ka reviewer check kar sake.

**Sawal:** Kis bayan mein classification aur wajah DONO sahi hain?

**Options ka matlab:**

- **A** — Collaborative — 10 din reversibility se manager monthly batch mein errors pakad legi, named person jawabdeh rehta.
- **B** — Human-retained — yeh step khud wahi faisla hai jiska manager jawabdeh, to accountability faisla karti, aur criteria takrayein to sab se strict jeetta.
- **C** — Human-retained — payables ke har step ka koi accountable, aur accountability tool ko nahi di ja sakti, step ki baaqi properties kuch bhi hon.
- **D** — AI-owned — reversible, low stakes, 80 cases par 96% match.

</details>

**Answer:** B

- ✅ **B** — The sharper test is whether the step is the call or an input someone judges before it acts.
- ❌ **A** — If the step is the decision, a later monthly review means the decision was made by AI and only audited.
- ❌ **C** — The classification is right but the reason is too broad: it would make every step human-retained.
- ❌ **D** — Past agreement is not a criterion, and accountability outranks reversibility and stakes where they disagree.

**Yaad rakho:** Sahi class aur sahi wajah dono chahiye: 'har step ka jawabdeh' wajah nahi, 'ye step khud faisla hai' wajah hai.

*Grounded in: Workflow Design §5 (three criteria; accountability's specific shape; strictest wins; past performance is not a criterion)*

---

### Q27.
An NGO director wants Claude to allocate 12 scholarships across five districts and gives it a spreadsheet with need scores, populations and last year's allocation, asking for "the best allocation". Two matters are not in the sheet. Board members have argued twice about whether to protect a flood-affected district, and no decision has been recorded. An informal understanding that no district should get more than three awards appears only in an old email. The director says the output is "just a recommendation", so it is safe, and that the model "will find the optimal split". A staff member proposes four ways to handle it, and the trustees meet in three days.

**Which handling follows the window test?**

- A. Use the assistant for options under stated priorities, with the three-award cap as an explicit input, and keep the choice among them with the board, since the undecided priority cannot be supplied.
- B. Have the model infer the board's likely preference from last year's allocation and the flood-district need score, then present the result as a recommendation for the trustees.
- C. Give the whole allocation to the assistant and correct it afterwards, since the recommendation is reversible and the criteria say reversible steps tolerate delegation.
- D. Paste everything and ask for one allocation with the model's assumptions listed, then have the trustees approve or amend it, since stated assumptions make the recommendation reviewable.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** NGO director Claude se 12 scholarships paanch districts mein baantwana chahti; sheet mein need scores, populations, pichle saal ki allocation; "best allocation" maangti. Do baatein sheet mein nahi: board do dafa flood-affected district ko protect karne par bahes kar chuka, faisla record nahi; aur ek purani email mein informal samajh ke kisi district ko 3 se zyada awards na milein. Director: "sirf recommendation hai, safe", model "optimal split" dhoondega. Staff member chaar tareeqe deta; trustees teen din mein milenge.

**Sawal:** Kaunsa handling "window test" follow karta hai? (Window test = kya faisle ki zaroori info model ke saamne rakhi ja sakti hai.)

**Options ka matlab:**

- **A** — AI ko stated priorities ke under options ke liye use karo, 3-award cap ko explicit input bana kar, aur un mein se chunna board ke paas rakho — kyunke undecided priority di hi nahi ja sakti.
- **B** — Model pichle saal ki allocation aur flood-district need score se board ki preference ka andaaza lagaye.
- **C** — Poori allocation AI ko, baad mein correct — recommendation reversible.
- **D** — Sab paste karke ek allocation maango assumptions ke saath, trustees approve/amend karein.

</details>

**Answer:** A

- ✅ **A** — Synthesis runs on inputs you can supply; a judgment step runs on information you cannot, and a model fills that gap with a typical answer.
- ❌ **B** — That fills a missing input with a guess dressed as evidence.
- ❌ **C** — The window test comes first: if the inputs cannot be supplied, the step is not eligible, however reversible.
- ❌ **D** — The undecided board question would be filled by a typical answer presented as the board's own assumption.

**Yaad rakho:** Jo faisla abhi hua hi nahi wo prompt mein nahi jaa sakta: options AI se, chunna board ka.

*Grounded in: Workflow Design §4 (the window test; synthesis versus judgment steps; passing makes a step eligible, never owned)*

---

### Q28.
A tender team at an engineering contractor extracts requirements from a 50-page hospital-linen-service RFP into a table (label, exact section, "answered in our thread"). Section 6 says linen must be "delivered promptly after the collection window". A scoring appendix awards more points for "reasonable" turnaround with no figure. Section 9 requires "adequate after-sales support". The buyer's Q&A window closes in 24 hours; the team also has a fourth issue: a clause in section 12 that mentions a "service credit" without saying how it is calculated. The bid manager says the table is complete because every row cites its section. The team has four proposals for the next step and must not miss the Q&A window.

**Which proposal follows the requirements guidance?**

- A. Run a second pass for ambiguous or implied requirements, send all four vague clauses to the buyer as questions before the window closes, and label any interim assumption as an assumption.
- B. Use typical hospital-tender values for prompt, reasonable and adequate as defaults, mark them as assumptions in the bid, and send only the service-credit question to the buyer.
- C. Ask the assistant to score how ambiguous each of the four clauses is, from one to ten, and send only the two highest-scoring clauses to the buyer within the window.
- D. Treat the table as verified because each row cites a section, and ask the assistant to propose interpretations of all four clauses from tenders it knows in the sector.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Engineering contractor ki tender team 50-page hospital-linen RFP ki requirements table (label, exact section, "answered in our thread") mein nikaalti. Section 6: linen "collection window ke baad promptly deliver" ho. Scoring appendix "reasonable" turnaround ko zyada points, koi figure nahi. Section 9: "adequate after-sales support". Buyer ki Q&A window 24 ghante mein band; chautha masla — section 12 mein "service credit" ka zikr, calculate kaise hoga nahi likha. Bid manager: table complete, har row section cite karti. Chaar proposals, Q&A window miss nahi karni.

**Sawal:** Kaunsa proposal requirements guidance follow karta hai?

**Options ka matlab:**

- **A** — Ambiguous ya implied requirements ke liye doosra pass chalao, chaaron vague clauses window band hone se pehle buyer ko sawal ke taur par bhejo, aur koi interim assumption ho to usay assumption hi label karo.
- **B** — Prompt, reasonable, adequate ke liye typical hospital-tender values default, bid mein assumption mark, buyer ko sirf service-credit wala sawal.
- **C** — AI se chaaron clauses ki ambiguity 1–10 score karwao, sirf top do buyer ko bhejo.
- **D** — Table verified maano (har row cite karti) aur AI sector ke tenders se chaaron ki interpretations propose kare.

</details>

**Answer:** A

- ✅ **A** — Extraction finds what was written, not what was meant; an unclear requirement caught before the bid costs one question.
- ❌ **B** — The default values close blanks the team owes the buyer questions about, and three ambiguous clauses are held back.
- ❌ **C** — A self-scored ambiguity does not tell which clauses two readers would interpret differently, and it leaves two open.
- ❌ **D** — A source column shows where written requirements came from; the buyer, not typical tenders, decides what they meant.

**Yaad rakho:** Chaaron dhundli shartein khareedar se poochho, defaults khud mat bharo; interim assumption likho.

*Grounded in: Workflow Design §2 (extract, then attack; each missing answer is a question you owe someone; an ambiguous requirement does not look ambiguous)*

---

### Q29.
A retail group's CEO tells the FDE: "We need better sales reporting." The FDE turns the request into a task definition, which is a business need turned into five settled answers. What is settled so far, from a 20-minute call. What is produced: "a weekly sales summary". For whom: "the regional managers". How often: not discussed. From what data: "the CRM plus the point-of-sale system", though the POS covers only 60% of stores. In what format: not discussed. The FDE has two days before a proposal is due and is tempted to let the assistant draft a full specification, including frequency and format, "so the CEO has something to react to". An associate proposes to send a short list of questions instead.

**Which is the best next step?**

- A. Ask the CEO about the two unsettled answers (frequency, format) and the POS gap, and label any interim assumption; a missing answer is a question owed, not a blank for the model.
- B. Ask the assistant to define the data section only, since data is the highest-risk slot, and defer frequency and format until after the proposal is accepted.
- C. Ask the assistant to list ten possible reporting formats and frequencies with pros and cons, and let the CEO choose from the list without further discussion of the POS coverage.
- D. Ask the assistant to draft the full specification, including a weekly frequency and a PDF format taken from similar retail clients, and present it to the CEO as a proposed default to react to.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Retail group ka CEO FDE se: "Hamein behtar sales reporting chahiye." FDE isay task definition banata — business need jo paanch settled jawabon mein badli jaye. 20-minute call se ab tak: kya banega — "weekly sales summary"; kis ke liye — "regional managers"; kitni dafa — baat nahi hui; kis data se — "CRM plus point-of-sale system", magar POS sirf 60% stores cover karta; kis format mein — baat nahi hui. Proposal do din mein. FDE ka dil karta AI se poori specification (frequency aur format samet) draft karwa le "taake CEO react kar sake". Associate: sawalon ki chhoti list bhejo.

**Sawal:** Behtareen agla qadam kya hai?

**Options ka matlab:**

- **A** — CEO se do unsettled jawab (frequency, format) aur POS gap poocho, aur koi interim assumption label karo; missing jawab ek poochna-baaqi sawal hai, model ke bharne ki khaali jagah nahi.
- **B** — AI se sirf data section define karwao (sab se risky slot), frequency/format proposal accept hone ke baad.
- **C** — AI se 10 possible formats aur frequencies pros/cons ke saath list karwao, CEO chune, POS coverage par mazeed baat nahi.
- **D** — AI se poori spec (weekly frequency, milte-julte retail clients se PDF format) draft karwa kar default ke taur par CEO ko do.

</details>

**Answer:** A

- ✅ **A** — A model asked to define a task closes unsettled slots at likely-looking defaults; each missing answer is a clarifying question you owe someone.
- ❌ **B** — All five answers must be settled before a proposal can be checked; deferring two leaves the requirement unverifiable.
- ❌ **C** — The options are drawn from generic practice and skip the unresolved data question.
- ❌ **D** — Model defaults would fill the two open slots and the POS gap unseen, presented with the assistant's confidence.

**Yaad rakho:** Panch jawab: kya, kis ke liye, kitni baar, kis data se, kis format mein. Khali jawab = sawal, model ka default nahi.

*Grounded in: Workflow Design §2 (task definition: what is produced, for whom, how often, from what data, in what format; each missing answer is a clarifying question you owe somebody)*

---

### Q30. *(Select TWO — all-or-nothing)*
A shipbuilder's contracts team maps its review of supplier contracts. Row B is "Compute delay-penalty exposure", Owner AI, Criterion "reversible; the result is checked at the next step", Carried by code execution. Row C is "Approve or reject each change", Owner Human (named counsel). The director, seeing that the approval queue is the main bottleneck, proposes three changes: remove Row C for penalty clauses below USD 100,000 "because the exposure figure is now computed exactly"; move the Row B calculation into a Skill "so that it runs the same way each time"; and let the assistant assess exposure for penalty clauses without any figures from the contract file "to save time". The FDE must state which of the director's reasons is valid.

**Which TWO statements are correct?**

- A. The exposure figure computed by code is exact, so the accountability for the approval passes to the calculation and Row C can be removed for small penalties.
- B. A calculation is carried by code execution, not a Skill, so moving Row B into a Skill risks writing rather than computing the figure.
- C. Removing Row C changes Row B's class: it was safe only because a human sees the figure at the next row, so without that gate it stops being AI-appropriate.
- D. Assessing exposure without any figures from the contract file is acceptable because the window test is passed once the contract's text has been given to the assistant.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Shipbuilder ki contracts team review map karti. Row B: "delay-penalty exposure compute", Owner AI, Criterion "reversible; result agle step par check hota", Carried by code execution. Row C: "har change approve/reject", Owner Human (named counsel). Director (approval queue bottleneck dekh kar) teen changes propose karta: USD 100,000 se kam penalty clauses ke liye Row C hatao "kyunke exposure ab exact compute hota"; Row B ki calculation Skill mein le jao "taake har dafa same chale"; aur AI contract file ke kisi figure ke baghair exposure assess kare "waqt bachane ke liye". FDE ko batana director ki kaunsi wajah valid hai.

**Sawal:** Kaunse DO bayan sahi hain?

**Options ka matlab:**

- **A** — Code se computed exposure exact hai, to approval ki accountability calculation ko chali jaati, chhoti penalties par Row C hat sakti.
- **B** — Calculation code execution carry karta hai, Skill nahi — Row B ko Skill mein le jaane se figure compute hone ke bajaye likhe jaane ka khatra.
- **C** — Row C hatane se Row B ki class badal jaati: wo sirf is liye safe tha ke agli row par insaan figure dekhta; gate ke baghair AI-appropriate nahi rehta.
- **D** — Contract file ke figures ke baghair exposure assess karna theek — contract ka text de diya to window test pass.

</details>

**Answer:** B, C

- ✅ **B** — 'Must be computed' belongs under Carried by, and code execution is the carrier for calculations.
- ✅ **C** — A step's classification can depend on whether anyone reads its output at the next step.
- ❌ **A** — The run is exact but the code can use the wrong column or file, and accountability never moves to a calculation.
- ❌ **D** — Without the figures the required inputs cannot be supplied to the step, so the window test fails.

**Yaad rakho:** Gate hataya to exposure step ki class badal jati hai. Calculation ka carrier code execution, Skill nahi.

*Grounded in: Workflow Design §3 and §6 (the penalty-exposure row; computed, not written; a step's class depends on whether anybody stands after it; the window test)*

---

### Q31.
Six months ago a retail analyst built a call checklist as a Claude artifact for her own onboarding calls. Today: three account managers read from it on every call; HR links it in the new-hire pack; the finance department pastes its scoring output into a board slide; nobody knows who to call when it shows a blank; and the analyst says she "has solved the supplier-payment reply routine the same way four times in a row, same inputs, same layout". Three proposals are made: send the checklist to IT, turn the routine into a reusable Skill or worker, and leave both by prompt "since they still work". The head of digital wants the sequence of actions, since IT has capacity for one project this month.

**Which sequence is correct?**

- A. First manufacture the payment-reply routine into a Skill or worker, since its method is stable and can be finished quickly; then escalate the checklist to IT when capacity allows.
- B. Escalate both to IT this month as one project, since both are now shared by other people and a shared tool is infrastructure that needs uptime and a named owner.
- C. First escalate the checklist to developer or architect expertise, since others now depend on it as infrastructure; then manufacture the payment-reply routine into a Skill or worker, since its method has stopped changing.
- D. Leave both as prompts and add an owner name and a change log to each, since prompt-and-iterate remains adequate while the tools keep working and an owner solves the who-to-call issue.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Chhe mahine pehle retail analyst ne apni onboarding calls ke liye Claude artifact call checklist banayi. Aaj: teen account managers har call par parhte; HR new-hire pack mein link karta; finance scoring output board slide mein paste karta; blank aaye to pata nahi kise call karein; aur analyst kehti supplier-payment reply routine chaar dafa lagataar same inputs aur layout se hal kiya. Teen proposals: checklist IT ko, routine ko reusable Skill/worker, aur dono prompt par chhodo "chal to rahe". IT ke paas is mahine sirf ek project ki capacity; head of digital actions ki tarteeb chahta.

**Sawal:** Kaunsi tarteeb sahi hai?

**Options ka matlab:**

- **A** — Pehle payment-reply routine ko Skill/worker banao (stable, jaldi khatam); phir capacity ho to checklist IT ko.
- **B** — Dono ek project ke taur par is mahine IT ko — shared tool infrastructure hai.
- **C** — Pehle checklist ko developer/architect expertise ke paas escalate karo kyunke doosre ab us par infrastructure ki tarah depend karte; phir payment-reply routine ko Skill/worker banao kyunke uska method badalna band ho gaya.
- **D** — Dono prompt par, har ek mein owner ka naam aur change log jodo.

</details>

**Answer:** C

- ✅ **C** — Dependence by others is the more exposed signal; a stable method is the ready-to-manufacture signal.
- ❌ **A** — The dependency of three managers, HR and a board slide is the urgent exposure, not the tidy routine.
- ❌ **B** — The routine is used by the analyst alone; the signal for it is a stable method, not dependence.
- ❌ **D** — A board slide and a new-hire pack depending on a prompt-built checklist is exactly what prompt-and-iterate cannot carry.

**Yaad rakho:** Pehle jis par doosre depend karte hain (engineering), phir jo tareeqa jam gaya (Skill/worker).

*Grounded in: Workflow Design §10 (escalation signal: other people depend on this; and: I have solved this the same way three times)*

---

### Q32.
A compliance group keeps a delegation map for an AI-assisted transaction-monitoring workflow. Its owner is listed as "the Compliance team" and the map says it is reviewed "whenever something changes". Over two months: a new statutory reporting rule takes effect; the analyst who reviewed AI-flagged alerts resigns and is not replaced; alert volume triples after a product launch; the map still says every alert is reviewed by a named analyst. An auditor asks what design would have caught this. The team offers four designs of a review process for a map, each with a named owner and date: (a) a monthly all-hands review; (b) one named owner and a quarterly scheduled read with the four questions, brought forward when volume, staffing or legal position change; (c) an annual approval by the chief compliance officer; (d) an AI tool that reads the map and warns when it looks outdated.

**Which design fits the guidance, and why?**

- A. Design (d): an AI tool that warns when the map looks outdated, since automated detection removes reliance on people remembering the review.
- B. Design (b): one named owner answerable for the map matching reality, with a scheduled read on last week's actual reviews, moved earlier when volume, staffing or legal position change.
- C. Design (a): a monthly all-hands review, since collective ownership ensures that every change reaches someone who cares and monthly cadence is more frequent than quarterly.
- D. Design (c): an annual approval by the chief compliance officer, since a senior approval gives the map authority and a single named approver is accountable.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Compliance group ke AI transaction-monitoring delegation map ka owner "Compliance team", review "jab kuch badle". Do mahine mein: naya statutory reporting rule; AI-flagged alerts review karne wala analyst resign, replacement nahi; product launch ke baad alert volume teen guna; map ab bhi kehta har alert named analyst review karta. Auditor poochta kaunsa design yeh pakadta. Chaar designs, har ek named owner aur date ke saath: (a) monthly all-hands review; (b) ek named owner aur quarterly scheduled read chaar sawalon ke saath, volume/staffing/legal change par pehle; (c) chief compliance officer ki annual approval; (d) AI tool jo map parh kar outdated lagne par warn kare.

**Sawal:** Kaunsa design guidance ke mutabiq hai, aur kyun?

**Options ka matlab:**

- **A** — Design (d) — automated detection logon ki yaaddasht par bharosa khatam karta.
- **B** — Design (b) — ek named owner jo map aur haqeeqat ke match ka jawabdeh, pichle hafte ke asal reviews par scheduled read, aur volume/staffing/legal change par pehle.
- **C** — Design (a) — collective ownership, monthly quarterly se zyada frequent.
- **D** — Design (c) — senior approval authority deti, ek named approver jawabdeh.

</details>

**Answer:** B

- ✅ **B** — Gates and maps fail with no signal; only an owner and a date, triggered by the three changes, catch them.
- ❌ **A** — The map records the design; the decay is in what actually runs, which the document cannot show.
- ❌ **C** — Team ownership leaves no single person answerable, and a meeting is not a read of the gate's actual staffing.
- ❌ **D** — Annual is far too slow for changes that break gates in weeks, and an approval does not ask what happened last week.

**Yaad rakho:** Ek naam-zad malik, tay tareekh, aur volume/staff/qanoon badle to jaldi review.

*Grounded in: Workflow Design §8 (a map needs one named owner and a review date; sooner if volume, staffing or legal position change; the four review questions)*

---

### Q33.
A finance shared-services centre is assigning carriers to five items in its quarterly pricing-review workflow. Item 1: "Always show the customer segment in the first line of every brief." Item 2: "The approved price list, updated quarterly, that the review must read on every run." Item 3: "Compute the margin impact of each price change the report cites." Item 4: "Prepare the pack in this exact order: cover note, table, exceptions, sign-off page." Item 5: "Approve any discount above 12%." The candidate carriers are: a standing instruction, Project knowledge, code execution, a Skill, and a named review gate. The centre has four proposed assignments of items 1 to 5 in order, each using all five carriers exactly once, and one of them is entirely correct.

**Which assignment of items 1 to 5, in that order, is correct?**

- A. Standing instruction; Project knowledge; code execution; named review gate; Skill.
- B. Standing instruction; Project knowledge; code execution; Skill; named review gate.
- C. Standing instruction; Project knowledge; Skill; code execution; named review gate.
- D. Project knowledge; standing instruction; code execution; Skill; named review gate.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Finance shared-services centre quarterly pricing-review ke paanch items ke carriers tay kar raha. Item 1: "har brief ki pehli line mein customer segment." Item 2: "approved price list, quarterly update, har run par parhni." Item 3: "report mein cited har price change ka margin impact compute karo." Item 4: "pack is exact order mein: cover note, table, exceptions, sign-off page." Item 5: "12% se upar har discount approve karo." Carriers: standing instruction, Project knowledge, code execution, Skill, named review gate. Chaar assignments (items 1–5 isi order mein), har carrier ek dafa — sirf ek poori sahi.

**Sawal:** Items 1 se 5 (isi order mein) ki kaunsi assignment sahi hai?

**Options ka matlab:**

- **A** — Standing instruction; Project knowledge; code execution; named review gate; Skill.
- **B** — Standing instruction; Project knowledge; code execution; Skill; named review gate.
- **C** — Standing instruction; Project knowledge; Skill; code execution; named review gate.
- **D** — Project knowledge; standing instruction; code execution; Skill; named review gate.

</details>

**Answer:** B

- ✅ **B** — Rule, reference, calculation, procedure, human-owned step: each to its own home.
- ❌ **A** — A fixed-order pack is a procedure, and an approval a person owns needs a named gate.
- ❌ **C** — A calculation is carried by code execution, and an ordered sequence of steps is a procedure for a Skill.
- ❌ **D** — A rule that always applies is a standing instruction, and the price list is reference material.

**Yaad rakho:** Rule -> instruction, reference -> knowledge, calculation -> code, tarteeb-war qadam -> Skill, insaani faisla -> named gate.

*Grounded in: Workflow Design §2 and §14 (implementation table; rule, reference or procedure; calculation to code; human step to a named gate)*

---

### Q34.
An FDE presents an AI-assisted invoice-processing workflow to three audiences. The facts: the assistant matches invoices to purchase orders and codes them; about 95% match cleanly; matched invoices are paid after a clerk reviews a daily exception report of any invoice above PKR 100,000 or with a new bank account; the other 5% go straight to the clerk; turnaround fell from five days to two; the assistant sometimes misses invoices that imply a purchase order amendment. Descriptions drafted: Description 1: "The assistant matches and codes invoices; anything above PKR 100,000 or with a new bank account is reviewed by a clerk before payment; it can miss invoices implying an order amendment, so treat its flags as a prompt for your read." Description 2: "Turnaround is down from five days to two with the same approval standard: a clerk signs off every payment above PKR 100,000 or to a new account." Description 3: "AI processes invoices automatically, with people on hand for exceptions." The audiences are the legal-and-finance lead (mechanism and failure modes), the executive (result and oversight) and the client's risk function (the control).

**Which assignment of descriptions to audiences is correct?**

- A. Description 3 to the executive, because it is the most concise statement of the benefit, with Description 1 to the risk function, since a control team wants the failure modes.
- B. Description 1 to all three audiences, since it is the most complete, and a consistent statement across audiences prevents any later charge of inconsistency.
- C. Description 2 to the legal-and-finance lead, because it names the approval standard, and Description 1 to the executive, because the failure warning shows candour.
- D. Description 1 to the legal-and-finance lead; Description 2 to the executive; for the risk function a one-sentence control statement naming the clerk's sign-off and its trigger, not Description 3.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** FDE AI invoice-processing workflow teen audiences ko present karta. Facts: AI invoices ko POs se match/code karta; ~95% saaf match; matched invoices clerk ke daily exception report review ke baad pay (PKR 100,000 se upar ya naye bank account wali); baaqi 5% seedha clerk; turnaround 5 se 2 din; AI kabhi wo invoices miss karta jo PO amendment imply karti. Description 1: mechanism + clerk ka gate + failure mode (amendment wali invoices miss) — "flags ko apne read ka prompt samjho". Description 2: turnaround 5 se 2 din, same approval standard — clerk har 100,000+ ya naye account wali payment sign off karta. Description 3: "AI invoices automatically process karta, exceptions ke liye log maujood." Audiences: legal-and-finance lead (mechanism aur failure modes), executive (result aur oversight), client ka risk function (control).

**Sawal:** Descriptions ko audiences se jodne ki kaunsi assignment sahi hai?

**Options ka matlab:**

- **A** — Description 3 executive ko (sab se mukhtasar benefit), Description 1 risk function ko (failure modes).
- **B** — Description 1 teeno ko — sab se complete, consistency.
- **C** — Description 2 legal-and-finance lead ko (approval standard), Description 1 executive ko (candour).
- **D** — Description 1 legal-and-finance lead ko; Description 2 executive ko; risk function ke liye ek-jumle ka control statement jo clerk ke sign-off aur uske trigger ko naam kare — Description 3 nahi.

</details>

**Answer:** D

- ✅ **D** — Each audience gets the detail it needs; none drops the gate; Description 3 is the 'AI handles X' phrasing that hides it.
- ❌ **A** — Description 3 drops the checkpoint; the risk function wants the control, not the mechanism's failure modes.
- ❌ **B** — The audiences need different detail; the complete version buries the executive's result and the risk function's single control sentence.
- ❌ **C** — The mechanism and known failure belong with the person who must weigh them; the executive wants the result and oversight.

**Yaad rakho:** Mechanism legal lead ko, natija executive ko, control risk ko. 'Automatically' wala jumla kisi ko nahi.

*Grounded in: Workflow Design §18 (state what the tool does, name the human checkpoint, say what it refuses; the same workflow described three ways; explicit checkpoints raise trust)*

---

### Q35.
An analytics lead builds the business case for keeping a redesigned weekly-report workflow. Facts: 4 analysts; each used to spend 50 minutes a week and now spends 20; 48 working weeks a year; a named reviewer spends 15 minutes a week in the gate; the AI subscription costs PKR 60,000 a year; the annual cost of one analyst hour is PKR 1,800. One colleague states the saving as "60% less time"; another leaves out the residual risk; a third gets 144 hours by mental arithmetic. A parallel run over two cycles found accuracy unchanged; the old process is documented; the baseline was measured before the change.

**Which statement of net annual value is most defensible?**

- A. About 84 net hours (96 minus 12 gate hours), worth roughly PKR 151,200 less the PKR 60,000 subscription, with the surviving risk named.
- B. About 96 hours saved, valued at roughly PKR 172,800 less the subscription, with the reviewer's gate time left out because it existed before the redesign.
- C. About 144 hours saved, valued at roughly PKR 259,200 less the subscription, since the third colleague's quick arithmetic already accounts for consistency benefits.
- D. A 60% reduction in report time, presented alone with the measured baseline noted, since a percentage travels across teams and avoids disputes about hours and rates.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Analytics lead redesigned weekly-report workflow ka business case bana raha. Facts: 4 analysts; har ek pehle 50 minute/hafta, ab 20; saal ke 48 working weeks; named reviewer gate mein har hafte 15 minute; AI subscription PKR 60,000/saal; ek analyst ghante ki cost PKR 1,800. Ek colleague: "60% kam waqt"; doosra residual risk chhodta; teesra dimagh se 144 ghante. Do cycles ke parallel run mein accuracy same; purana process documented; baseline change se pehle naapa gaya.

**Sawal:** Net annual value ka sab se defensible bayan kaunsa hai? (Hisaab khud lagao.)

**Options ka matlab:**

- **A** — ~84 net ghante (96 minus 12 gate ghante), ~PKR 151,200 ke barabar, minus PKR 60,000 subscription, aur bacha hua risk naam karke.
- **B** — ~96 ghante bachat, ~PKR 172,800 minus subscription, reviewer ka gate time bahar kyunke redesign se pehle bhi tha.
- **C** — ~144 ghante, ~PKR 259,200 minus subscription — quick hisaab consistency faide pakadta.
- **D** — Sirf "60% kam report time", measured baseline note ke saath.

</details>

**Answer:** A

- ✅ **A** — Saving is baseline change x frequency x people, less human time in the gate and the tool cost; the surviving risk is stated.
- ❌ **B** — The gate is part of the redesigned workflow's cost.
- ❌ **C** — 30 x 4 x 48 = 5,760 minutes, which is 96 hours; the quick figure is wrong.
- ❌ **D** — A percentage without volume, cost or risk cannot survive a budget review.

**Yaad rakho:** Net = bachat ghante minus gate ka waqt; phir rupay mein, subscription ghata kar, aur bacha hua risk likho.

*Grounded in: Workflow Design §16 (baseline; saving = baseline x frequency x people; cost includes human time in the kept gates; name the surviving risk; parallel run) and §3*

---

### Q36.
A B2B marketplace's quotation workflow uses a Project whose knowledge base holds a supplier price sheet. The supplier repriced 25 days ago; the old sheet stayed in the Project, so every quote since has used stale prices. Discovered on a Friday evening. Facts: 610 quotes were generated in the 25 days; the workflow logs the sheet version for none of them; only the builder has admin rights and is on leave until Tuesday; the customers involved are in the CRM but the quotes' recipients are not linked to the workflow's outputs; the map has not been updated. The incident lead knows four design-time decisions: how it gets stopped, what is already out, who is told and by when, and what changes in the map. The team can do one thing in the next hour.

**Which is the most useful single action?**

- A. Begin scoping the 610 quotes by matching them to recipients and sheet versions, since what is already out is the hardest question and stopping the workflow can wait for the builder.
- B. Draft the customer notification tonight and send it on Saturday morning, since late disclosure costs far more than early, and pausing can be done by the builder on Tuesday.
- C. Record the incident in the map with the date and the four causes considered, since the fix must outlast the week and the map change is the decision that produces lasting improvement.
- D. Get a second named person to pause the workflow now (or to replace the sheet), because if only the builder can act every other step waits, and then begin scoping the 610 quotes by date.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** B2B marketplace ka quotation workflow ek Project ki knowledge mein supplier price sheet rakhta. Supplier ne 25 din pehle reprice kiya, purani sheet rahi — tab se har quote stale. Friday shaam pata chala. Facts: 25 din mein 610 quotes; kisi ka sheet version log nahi; sirf builder ke paas admin rights aur wo Tuesday tak chhutti par; customers CRM mein hain magar quotes ke recipients workflow outputs se linked nahi; map update nahi hua. Chaar design-time decisions: kaise roka jaye, kya bahar ja chuka, kise aur kab batana, map mein kya badle. Agle ek ghante mein team ek hi kaam kar sakti.

**Sawal:** Sab se useful single action kaunsa hai?

**Options ka matlab:**

- **A** — 610 quotes ko recipients aur sheet versions se match karke scope karna shuru karo — rokna builder ka intezaar kar sakta.
- **B** — Aaj raat customer notification draft karke Saturday subah bhejo, pause Tuesday ko builder kare.
- **C** — Map mein incident date aur chaar causes ke saath record karo — lasting improvement map change se.
- **D** — Ek doosre named person se abhi workflow pause karwao (ya sheet replace), kyunke agar sirf builder action le sakta to har doosra step intezaar karta; phir 610 quotes date se scope karna shuru karo.

</details>

**Answer:** D

- ✅ **D** — The design-time decision that blocks all others is who can stop it and whether they need permission.
- ❌ **A** — Scoping is hard, but the workflow keeps producing stale quotes until someone can stop it.
- ❌ **B** — Telling customers is important, but new stale quotes continue to be issued over the weekend.
- ❌ **C** — It is a decision for after the scope is known; it does not stop or scope the incident.

**Yaad rakho:** Sab se pehle rok-ne ka ikhtiyar: sirf builder ho to baaqi sab ruke rehte hain.

*Grounded in: Workflow Design §17 (four design-time decisions; if the honest answer is that only the builder can act, fix that first; stale configuration affects every output since it went stale)*

---

### Q37.
A regional airline's dispatch team used Claude to build a weather-briefing format. After six months, the following is reported. (i) The team never wrote down what a good briefing must contain or what counted as done; the assistant produced varying formats. (ii) Prompts were written for each briefing without stating the audience, so captains and ground staff received the same text. (iii) Reviewers checked briefings only for readability; no one checked the codes against the current standards. (iv) Briefings containing captains' personal data were pasted into a personal AI account when the approved tool was slow. A consultant maps the four failures to the four AI-fluency competencies (Delegation, Description, Discernment, Diligence) and must give one primary mapping per failure. Colleagues offer four mappings, listing failures i to iv in order.

**Which mapping is correct?**

- A. (i) Description, (ii) Delegation, (iii) Discernment, (iv) Diligence.
- B. (i) Delegation, (ii) Discernment, (iii) Description, (iv) Diligence.
- C. (i) Delegation, (ii) Description, (iii) Discernment, (iv) Diligence.
- D. (i) Delegation, (ii) Description, (iii) Diligence, (iv) Discernment.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Regional airline ki dispatch team ne Claude se weather-briefing format banaya. Chhe mahine baad reports: (i) team ne kabhi nahi likha achhi briefing mein kya hona chahiye ya "done" kya hai; AI alag alag formats deta. (ii) Har briefing ke prompts audience bataye baghair — captains aur ground staff ko same text. (iii) Reviewers ne sirf readability check ki; codes ko current standards se kisi ne check nahi kiya. (iv) Captains ke personal data wali briefings approved tool slow hone par personal AI account mein paste hui. Consultant chaaron failures ko chaar AI-fluency competencies (Delegation, Description, Discernment, Diligence) se jodta — har failure ki ek primary mapping.

**Sawal:** Kaunsi mapping (i se iv isi order mein) sahi hai?

**Options ka matlab:**

- **A** — (i) Description, (ii) Delegation, (iii) Discernment, (iv) Diligence.
- **B** — (i) Delegation, (ii) Discernment, (iii) Description, (iv) Diligence.
- **C** — (i) Delegation, (ii) Description, (iii) Discernment, (iv) Diligence.
- **D** — (i) Delegation, (ii) Description, (iii) Diligence, (iv) Discernment.

</details>

**Answer:** C

- ✅ **C** — No stated goal or definition of done is a Delegation gap; a missing audience is Description; unchecked codes is Discernment; personal data in an unapproved account is Diligence.
- ❌ **A** — A missing goal and definition of done is problem awareness, which is Delegation; a missing audience is a Description gap.
- ❌ **B** — Not stating the audience is Description; judging whether the output is good is Discernment.
- ❌ **D** — Checking the output's correctness is Discernment; taking responsibility for data and use is Diligence.

**Yaad rakho:** Goal tay nahi = Delegation, audience nahi bataya = Description, output check nahi = Discernment, data/zimmedari = Diligence.

*Grounded in: AI Fluency §3-8 (the 4Ds; four common beginner mistakes: prompting before defining the problem, first answer as final, trusting polish, thinking about privacy late)*

---

## Domain 6 — Governance, Risk, and Responsible Use (15% — 15 questions)

### Q38.
At 16:10 on a Wednesday a recruitment coordinator at a Lahore staffing firm realises she uploaded a spreadsheet of 340 candidates (names, phone numbers, salary expectations) to her personal AI account at 11:45, because the company workspace login timed out. Nothing has been sent to anyone. Timeline. 12:20: she closed the tab. 14:00: she reran the same analysis in the approved workspace and saved the clean output. 16:10: she decides what to do now. The firm's clients are regulated; one client contract requires notification within 72 hours of any unapproved processing of its candidates' data; her manager is in a meeting until 17:30; the incident owner is the security lead, reachable by email. Her colleague lists five candidate actions and asks which one should NOT be done at this point.

**Which action should NOT be taken now?**

- A. Stop creating copies: do not forward the spreadsheet or the reran output to anyone, and do not open further chats with the same file until told what to do.
- B. Email the security lead now with the facts and ask what to do, without waiting for her manager to leave the meeting, since the incident owner decides deletion and notification.
- C. Write down what went in, when, by which route, and that the analysis was rerun in the approved workspace at 14:00, without editing anything, and keep the facts to hand.
- D. Delete the personal-account chat and the reran output, and mention the matter to her manager after the meeting only if a client asks, since removing the copies limits how long the data is retained.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Wednesday 16:10 par Lahore staffing firm ki recruitment coordinator ko ehsaas hota usne 11:45 par 340 candidates ki sheet (naam, phone, salary expectations) personal AI account mein upload ki thi (company login time out). Kisi ko kuch nahi bheja. Timeline: 12:20 tab band; 14:00 approved workspace mein wahi analysis dobara chala kar clean output save kiya; 16:10 ab kya kare. Clients regulated; ek client contract unapproved processing ke 72 ghante mein notification maangta; manager 17:30 tak meeting mein; incident owner security lead hai, email par available. Colleague paanch candidate actions list karta — kaunsa abhi NAHI karna chahiye?

**Sawal:** Kaunsa action abhi NAHI lena chahiye? (NOT wala sawal.)

**Options ka matlab:**

- **A** — Copies banana band: spreadsheet ya rerun output kisi ko forward mat karo, aur hidayat milne tak usi file ke saath naye chats mat kholo.
- **B** — Abhi security lead ko facts ke saath email karo aur poocho kya karna, manager ki meeting khatam hone ka intezaar kiye baghair — deletion aur notification incident owner tay karta.
- **C** — Likho kya gaya, kab, kis route se, aur 14:00 par approved workspace mein rerun hua — kuch edit kiye baghair, facts paas rakho.
- **D** — Personal-account chat aur rerun output delete karo, aur manager ko meeting ke baad sirf tab batao jab koi client poochhe — copies hatane se retention kam.

</details>

**Answer:** D

- ✅ **D** — Deleting a visible copy does not delete organisational or vendor records, turns a mistake into concealment, and delays a report with a legal clock.
- ❌ **A** — Stopping the spread is the first step and costs nothing.
- ❌ **B** — Prompt reporting through the incident path is correct, and the incident owner is reachable.
- ❌ **C** — Recording the facts plainly is step two of the first-hour procedure.

**Yaad rakho:** Delete karna aur baad mein batana: sab se ghalat. Facts likho, foran security lead ko bhejo.

*Grounded in: Governance §7 (first-hour procedure; deleting your copy removes your visibility, not the data, and turns a mistake into concealment; the clock matters more than the polish)*

---

### Q39.
A logistics firm's Governance Record for its weekly service-exception report says "appropriate with review". The author lists four candidate wordings for the gate. Context: the report is drafted from dispatch records; the company is accountable for every factual claim to customers; on disputed accounts the tone matters; an earlier report described a delay as "driver failure" when the dispatch record said weather; account managers are busiest on Fridays, when reports go out; there are 46 customers. A defined gate names who reviews (the role that holds the responsibility), what they verify (the specific risk), and when (before the output becomes hard to undo). Exactly one wording fails on exactly one of these three, and the others each pass all three.

**Which wording is NOT a defined gate?**

- A. Before Friday's send-out, the manager assigned to each customer verifies each cause given for a delay against the dispatch record, and reads the disputed accounts for tone.
- B. The account manager for each customer checks every delivery fact and its stated cause against the dispatch record before the report leaves on Friday, and reviews tone on disputed accounts.
- C. Each customer's account manager, with the dispatch record open, checks facts and stated causes line by line, and sends nothing on a disputed account until its tone has been read.
- D. Each customer's account manager confirms that the report's facts are accurate and that its tone is appropriate, with particular care on disputed accounts, as part of the usual Friday send-out.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Logistics firm ke weekly service-exception report ke Governance Record mein "appropriate with review". Author gate ki chaar wordings deta. Context: report dispatch records se draft; company har factual claim ki jawabdeh; disputed accounts par tone matter karti; pehle ek report ne delay ko "driver failure" kaha jabke record mein weather; Fridays (send day) account managers sab se busy; 46 customers. Defined gate: kaun review kare (jiske paas zimmedari), kya verify kare (specific risk), aur kab (output ke mushkil se wapas hone se pehle). Theek ek wording teen mein se ek par fail hoti, baaqi teeno teeno pass.

**Sawal:** Kaunsi wording defined gate NAHI hai?

**Options ka matlab:**

- **A** — Friday send-out se pehle har customer ka assigned manager har delay ki wajah dispatch record se verify kare, aur disputed accounts tone ke liye parhe.
- **B** — Har customer ka account manager Friday ko report nikalne se pehle har delivery fact aur stated cause dispatch record se check kare, aur disputed accounts par tone review kare.
- **C** — Har customer ka account manager, dispatch record khol kar, facts aur causes line by line check kare, aur disputed account par tone parhe baghair kuch na bheje.
- **D** — Har customer ka account manager confirm kare ke facts accurate aur tone munasib hai, disputed accounts par khaas dhyan, usual Friday send-out ke hissa ke taur par.

</details>

**Answer:** D

- ✅ **D** — It names a role and a general aim ('accurate, appropriate') but not the specific check against the dispatch record, and 'as part of the usual send-out' names no point before the report is sent.
- ❌ **A** — Who (the assigned manager), what (causes against the record) and when (before send-out) are all present.
- ❌ **B** — It names who, what (facts and causes against the record) and when (before the report leaves).
- ❌ **C** — Who, what and when are all present: nothing is sent until the reviewer has checked.

**Yaad rakho:** Gate = kaun, kya (dispatch record ke sath khaas risk), kab (bhejne se pehle). Ek bhi kam = intention.

*Grounded in: Governance §1.3 (a human in the loop is not a gate; who, what, when; 'someone will check it' versus the account-manager example)*

---

### Q40.
A public-health analyst has a 60,000-row spreadsheet of hospital admissions: patient names, national ID numbers, ward, admission date, length of stay, and a free-text diagnosis note. Task 1 is to find monthly trends in length of stay by ward. Task 2 is to reconcile one named patient's 14 admissions against billing, which needs that patient's ID. The department restricts regulated personal data to approved routes, and nobody has confirmed that the workspace is approved for patient records. The analyst proposes a plan for each of the following elements: which task uses redaction; whether the free-text note stays; what happens to the ID-to-name key; what to confirm about the route; and what the sandbox and incognito chat are for. A colleague says exactly one element of her plan is wrong.

**Which element is wrong?**

- A. Use an incognito chat only to avoid history and memory persistence, and do not treat it as evidence that the data was permitted, or that it is deleted at once.
- B. For Task 1, replace names and IDs with codes, keep the free-text notes and the key file in the same folder, and treat the result as anonymised, since the task needs only monthly patterns.
- C. For Task 2, where the patient's identity is the substance of the work, do not upload until the admin has confirmed in advance that this route is approved for patient records.
- D. Use the code-execution sandbox only to limit where the file-processing code can run, and do not treat it as evidence that the file was allowed into that environment.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Public-health analyst ke paas 60,000-row admissions sheet: naam, national ID, ward, admission date, length of stay, aur free-text diagnosis note. Task 1: ward-wise length of stay ke monthly trends. Task 2: ek named patient ke 14 admissions billing se reconcile (ID chahiye). Department regulated personal data sirf approved routes par; kisi ne confirm nahi kiya workspace patient records ke liye approved. Analyst har element ka plan deti: kaunsa task redaction use kare; free-text note rahe ya nahi; ID-to-name key ka kya; route ke baare mein kya confirm; sandbox aur incognito kis liye. Colleague: plan ka theek ek element ghalat hai.

**Sawal:** Kaunsa element ghalat hai?

**Options ka matlab:**

- **A** — Incognito sirf history aur memory persistence se bachne ke liye, isay is baat ka saboot mat samjho ke data allowed tha ya foran delete hota.
- **B** — Task 1 ke liye naam aur IDs codes se badlo, free-text notes aur key file ek hi folder mein rakho, aur result ko anonymised maano kyunke sirf monthly patterns chahiye.
- **C** — Task 2 (jahan patient ki identity hi asal kaam) — upload tab tak nahi jab tak admin pehle se confirm na kare route patient records ke liye approved.
- **D** — Sandbox sirf yeh limit karne ke liye ke file-processing code kahan chal sakta, isay saboot mat samjho ke file us environment mein allowed thi.

</details>

**Answer:** B

- ✅ **B** — Codes with the key beside them are pseudonymised and keep their tier; free-text notes can still identify people by combinations of ordinary facts.
- ❌ **A** — Incognito answers a narrower question and is not zero retention.
- ❌ **C** — The other branch of the discriminator: when the specifics are the substance, confirm the route first.
- ❌ **D** — A sandbox is an execution boundary, not an approval boundary.

**Yaad rakho:** Code + key saath rakha = pseudonymised, anonymised nahi. Free-text bhi pehchaan bata sakta hai.

*Grounded in: Governance §2.1-2.6 (discriminator; pseudonymised keeps its tier; partial redaction; route first; sandbox is not authorization; incognito is not zero retention)*

---

### Q41.
A pharmaceutical distributor's HR team collected 2,100 employees' health-screening results in 2024 for one stated purpose: a solvent-exposure safety programme. In 2026 the analytics head proposes using the same records, names attached, to build an assistant that flags staff "likely to take extended sick leave" for manager conversations. Facts offered in favour. The results sit in the company's AI workspace, which the admin has approved for health data. The data would not leave the workspace. Drafts would be produced in temporary chats. Managers would read the flags before any conversation. Employees were told the results were for "the solvent-exposure programme". The proposal names four governance questions that it says are settled, and the compliance lead says one is not.

**Which question is NOT settled by the facts offered?**

- A. Whether the route is approved for health data: the admin has confirmed the workspace is approved for it, so the route question is settled.
- B. Whether the collection purpose covers the flagging use; an approved route says where data may go, not what for.
- C. Whether a human reads the output before any action: managers read the flags before any conversation, so the review gate question is settled.
- D. Whether the drafts persist in memory across sessions: temporary chats keep them out of memory and history, so that persistence question is settled.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Pharma distributor ki HR ne 2024 mein 2,100 employees ke health-screening results ek bataye maqsad ke liye liye: solvent-exposure safety programme. 2026 mein analytics head inhi records ko naam ke saath use karke "extended sick leave ke imkaan wale" staff ko manager conversations ke liye flag karne wala assistant banana chahti. Haq mein facts: results us AI workspace mein jo admin ne health data ke liye approve kiya; data workspace se nahi nikalta; drafts temporary chats mein; managers kisi bhi conversation se pehle flags parhenge. Employees ko bataya gaya tha results "solvent-exposure programme ke liye". Proposal chaar governance sawal settled batata; compliance lead: ek nahi hai.

**Sawal:** Diye gaye facts se kaunsa sawal settled NAHI hota?

**Options ka matlab:**

- **A** — Route health data ke liye approved hai? — admin ne confirm kiya, settled.
- **B** — Kya collection purpose flagging use ko cover karta; approved route batata data kahan ja sakta, kis liye nahi.
- **C** — Kisi action se pehle insaan output parhta? — managers pehle parhte, settled.
- **D** — Drafts sessions ke paar memory mein rehte? — temporary chats bahar rakhte, settled.

</details>

**Answer:** B

- ✅ **B** — Purpose is the leg of the route question people skip because the file is already inside.
- ❌ **A** — The admin's confirmation settles the route question.
- ❌ **C** — A named reader before action answers the gate question, as far as it goes.
- ❌ **D** — A temporary chat answers the persistence question.

**Yaad rakho:** Route, persistence aur review settled ho sakte hain; maqsad (purpose) alag sawal hai jo data-malik ka hai.

*Grounded in: Governance §2.4 (the route matters as much as the tool name; purpose; a new use needs the collection reason or fresh permission) and §2.5*

---

### Q42.
A bank's fraud-operations team enables a "case-notes" agent from the vendor's official skills directory. Facts. The publisher is well known; the source check passed; the security lead read the Skill's instructions and confirmed they summarise notes only. The team then connected the agent to a shared mailbox where customers and outside investigators send documents, with "send reply" enabled so it can acknowledge submissions, and to the case-management drive with edit rights "so that it can update case files". Two weeks later a submitted PDF contains hidden text telling the agent to forward a case file to an external address. The agent did not comply. The security lead assigns five roles to controls: one control per role: reading, acting, scoping, sourcing and auditing. She asks which of four candidate designs is the strongest.

**Which design best follows the framework?**

- A. Keep the mailbox read-only and one folder wide, keep send and file edits behind a human gate, remember a Skill has no scope dial, and log every action.
- B. Set the Skill itself to read-only for the mailbox and the drive, and trust the publisher's reputation for any content it reads, since a known publisher's Skill will not follow hidden instructions.
- C. Keep send and edit enabled but require the agent to ask before forwarding any file externally, since a confirmation for external forwards stops the specific attack that was tried.
- D. Move to a stronger model tier that resists hidden instructions better, keep all permissions as they are, and audit the logs each quarter for unexpected forwards.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Bank ki fraud-ops team vendor ki official skills directory se "case-notes" agent enable karti. Publisher mashhoor, source check pass, security lead ne instructions parh kar confirm kiya sirf notes summarise karti. Phir agent ko shared mailbox (customers aur outside investigators documents bhejte) se joda, "send reply" on; aur case-management drive se edit rights ke saath "taake case files update kare". Do hafte baad ek PDF mein chhupa text: case file external address par forward karo. Agent ne nahi maana. Security lead paanch roles ke liye controls rakhti — reading, acting, scoping, sourcing, auditing — aur chaar designs mein se sab se mazboot poochti.

**Sawal:** Kaunsa design framework ko sab se achhi tarah follow karta hai?

**Options ka matlab:**

- **A** — Mailbox read-only aur ek folder tak, send aur file edits human gate ke peeche, yaad rakho Skill ka scope dial nahi, aur har action log karo.
- **B** — Skill ko khud mailbox aur drive ke liye read-only set karo, aur publisher ki reputation par bharosa.
- **C** — Send aur edit on rakho magar external forward se pehle agent poochhe.
- **D** — Stronger tier, permissions wahi, har quarter logs audit.

</details>

**Answer:** A

- ✅ **A** — Break the untrusted-content-plus-action pairing, use connector scopes where a dial exists, and remember a Skill has none.
- ❌ **B** — A Skill has no permission dial, and the source check says nothing about the content it reads.
- ❌ **C** — One tried attack is not the class of attack; a narrower guess at the next one leaves the pairing in place.
- ❌ **D** — A better model may resist more, but the design still lets an injected instruction reach an irreversible action.

**Yaad rakho:** Parhna aur bhejna alag karo, connector ka scope tang, send/edit par insaani gate, Skill ka koi dial nahi.

*Grounded in: Governance §3.1-3.3 (a Skill has no scope dial; trusted tool, untrusted content; least privilege; keep irreversible actions behind a human) and A.2*

---

### Q43.
A finance-operations lead considers enabling a third-party "analytics booster" Skill. Facts about it, and the five checks (source, reach, fit, outside content, actions). Fact A: it was published by an unknown account and its listing has no history. Fact B: its instructions mention fetching benchmark data from "partner sources" and saving copies of processed files "for continuity"; the team's sessions can reach the finance shared drive and the payment-approvals connector. Fact C: reporting is the team's task, and a reporting formatter would need to touch only the report file. Fact D: it would read incoming supplier spreadsheets emailed by outsiders. Fact E: it can save, send and approve. A junior asks which fact maps to which check. Four mappings of Facts A to E to the checks in the order Source, Reach, Fit, Outside content, Actions are offered.

**Which mapping is correct?**

- A. A to Reach; B to Source; C to Fit; D to Outside content; E to Actions.
- B. A to Source; B to Reach; C to Outside content; D to Fit; E to Actions.
- C. A to Source; B to Fit; C to Reach; D to Outside content; E to Actions.
- D. A to Source; B to Reach; C to Fit; D to Outside content; E to Actions.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Finance-ops lead third-party "analytics booster" Skill enable karne par ghaur karti. Paanch checks: source, reach, fit, outside content, actions. Fact A: unknown account ne publish kiya, listing ki koi history nahi. Fact B: instructions "partner sources" se benchmark data fetch karne aur processed files ki copies "continuity ke liye" save karne ka zikr; sessions finance shared drive aur payment-approvals connector tak pahunchte. Fact C: team ka kaam reporting hai, aur reporting formatter ko sirf report file chhooni chahiye. Fact D: yeh bahar walon ki bheji supplier spreadsheets parhega. Fact E: save, send aur approve kar sakta. Chaar mappings (A–E ko order Source, Reach, Fit, Outside content, Actions se).

**Sawal:** Kaunsi mapping sahi hai?

**Options ka matlab:**

- **A** — A Reach; B Source; C Fit; D Outside content; E Actions.
- **B** — A Source; B Reach; C Outside content; D Fit; E Actions.
- **C** — A Source; B Fit; C Reach; D Outside content; E Actions.
- **D** — A Source; B Reach; C Fit; D Outside content; E Actions.

</details>

**Answer:** D

- ✅ **D** — Who published it is source; what it could touch is reach; whether that is proportionate to the job is fit; content written by others is outside content; what it can do is actions.
- ❌ **A** — The unknown publisher is the source question, and what it could touch is reach.
- ❌ **B** — Reporting needing only the report file is fit; outsiders' spreadsheets are outside content.
- ❌ **C** — What the session can reach (drive, approvals) is reach; whether that is proportionate to reporting is fit.

**Yaad rakho:** Source = kis ne banaya, Reach = kya chhoo sakta, Fit = kaam ke mutabiq?, Outside content, Actions.

*Grounded in: Governance §3.1-3.2 (five checks: source, reach, fit, outside content, actions; the first three say whether it belongs, the last two how dangerous a mistake could be)*

---

### Q44. *(Select TWO — all-or-nothing)*
A university admissions office uses an AI assistant to shortlist scholarship applicants. Figures: 4,000 applications; shortlist of 120; the committee reads the 120 carefully and says the process is "thoroughly reviewed". A coordinator finds that 78% of the shortlist come from three universities, and applicants from rural districts are almost absent. Applicants were not told an automated screen was used. The registrar wants a control before the offer letters go out on Friday and lists candidate controls. Only some of them address who was excluded rather than who was included, and the registrar wants the two that most directly examine the excluded group and the disclosure question.

**Which TWO controls are best?**

- A. Sample the 3,880 excluded applications, especially those just below the cut-off and from under-represented districts, and check them against the stated criteria.
- B. Have the committee read the 120 shortlisted applications a second time and record its reasoning on each, since deeper review of the selected set shows whether the AI ranked them fairly.
- C. Add a second AI to re-rank the 120 shortlisted applications and keep any applicant that both models place in the top 60, since two independent rankings reduce bias.
- D. Check whether disclosure of the automated screen is required by law, policy or contract, and if no rule settles it, disclose in this ordinary case rather than conceal.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** University admissions office AI se scholarship shortlist banata. 4,000 applications, 120 shortlist; committee 120 dhyan se parhti aur kehti "thoroughly reviewed". Coordinator: shortlist ka 78% teen universities se, rural districts ke applicants taqreeban gayab. Applicants ko nahi bataya gaya automated screen use hua. Registrar Friday ko offer letters se pehle control chahta. Sirf kuch controls un logon ko dekhte jo bahar hue (na ke andar aane wale); registrar wo do chahta jo bahar hue group aur disclosure ke sawal ko sab se seedha jaanchte.

**Sawal:** Kaunse DO controls behtareen hain?

**Options ka matlab:**

- **A** — 3,880 bahar hui applications sample karo, khaas taur par cut-off se zara neeche aur kam-represented districts wali, aur stated criteria se check karo.
- **B** — Committee 120 ko doosri dafa parhe aur har ek par reasoning record kare.
- **C** — Doosra AI 120 ko re-rank kare, dono ke top 60 mein aane wale rakho.
- **D** — Check karo kya law, policy ya contract automated screen ka disclosure maangta; koi rule settle na kare to is aam case mein chhupane ke bajaye disclose karo.

</details>

**Answer:** A, D

- ✅ **A** — If review looks only at survivors, the people positioned to notice a systematic exclusion are the ones filtered out.
- ✅ **D** — Rules first, judgment second; concealment damages trust when it surfaces.
- ❌ **B** — Reading only the shortlist cannot reveal who was removed.
- ❌ **C** — Two models re-ranking the same 120 still never look at the 3,880 excluded.

**Yaad rakho:** Nikale gaye applicants ka sample lo aur disclosure ka rule check karo; shortlist dobara parhna kaafi nahi.

*Grounded in: Governance §4.1-4.2 (look at who was excluded: sample exclusions as well as inclusions; disclosure: rules first, judgment second)*

---

### Q45.
A partner at a consulting firm sends a 40-page market-entry report under her own name to a public-sector client. Claude drafted about half; she rewrote and verified the rest. She asks whether the report needs an AI disclosure. Facts, in the order she learns them. (1) The firm's policy is silent. (2) The professional body has issued no guidance. (3) The client's master services agreement annex says suppliers must declare AI assistance on deliverables; she has not read the annex. (4) A manager says "routine tooling needs no label". (5) Another says "when in doubt, disclose everything". (6) The report will be quoted to the client's board. She writes four steps in order and asks which order follows the disclosure guidance.

**Which order of reasoning is correct?**

- A. First ask whether AI involvement would change the board's understanding of the report; then check the annex and the policy; and disclose in any case where the answer to either is yes.
- B. First rely on the firm's silent policy and the professional body's silence to conclude that no disclosure is owed; then read the annex only if the client asks about AI use.
- C. First decide by the report's authorship: since she rewrote and verified half and edited the rest, her authorship stands and no disclosure is needed; then check the annex to confirm.
- D. First check whether law, policy, contract, professional rule or client commitment requires disclosure (the annex may decide it); only then ask whether AI involvement changes the reader's understanding.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Consulting partner apne naam se public-sector client ko 40-page report bhejti; aadha Claude ne draft kiya, baaqi usne rewrite/verify kiya. AI disclosure chahiye? Facts jis order mein pata chale: (1) firm policy khamosh. (2) Professional body ki guidance nahi. (3) Client ke MSA annex mein suppliers ko deliverables par AI assistance declare karni hai; annex usne nahi parha. (4) Manager: "routine tooling par label nahi chahiye". (5) Doosra: "shak ho to sab disclose". (6) Report client ke board ko quote hogi. Wo chaar steps likhti aur poochti kaunsa order disclosure guidance follow karta.

**Sawal:** Reasoning ka kaunsa order sahi hai?

**Options ka matlab:**

- **A** — Pehle poocho kya AI involvement board ki samajh badlegi; phir annex aur policy check; kisi ka jawab haan ho to disclose.
- **B** — Pehle firm aur professional body ki khamoshi se nateeja ke disclosure nahi banta; annex sirf client poochhe to parho.
- **C** — Pehle authorship se faisla — rewrite/verify kiya, authorship uski, disclosure nahi; phir annex confirm ke liye.
- **D** — Pehle check karo kya law, policy, contract, professional rule ya client commitment disclosure maangta (annex faisla kar sakta); sirf phir poocho kya AI involvement reader ki samajh badalti hai.

</details>

**Answer:** D

- ✅ **D** — Rules first, judgment second; if a rule requires disclosure the decision is already made.
- ❌ **A** — The order is reversed: a rule that requires disclosure settles it before any judgment is needed.
- ❌ **B** — Silence in two places does not answer whether the client's contract requires it.
- ❌ **C** — Owning the work is her responsibility either way; whether disclosure is required is a separate question decided by rules.

**Yaad rakho:** Disclosure: pehle rule (contract annex, policy), phir 'kya reader ki samajh badalti?'; ownership alag sawal.

*Grounded in: Governance §4.2 (disclosure: is it required first; if no rule answers, would AI involvement change the reader's understanding; authorship; disclose rather than conceal when no rule settles an ordinary case)*

---

### Q46.
An HR director at a retail chain wants to pilot a tool that flags "unusual attendance patterns" among 2,300 store employees for follow-up by managers; unflagged employees are never reviewed. She is unsure whether local labour law limits automated flagging that could influence employment decisions, and whether staff must be told. The vendor offers to "confirm compliance in writing". Counsel is away for a week. She drafts four messages to the governance function, each of which names the workflow, the affected staff and a control. The messages differ in what they ask the reviewer to do.

**Which message is the strongest escalation?**

- A. 'Here is the workflow, who is affected including staff never flagged, the control added, and the unsettled point: whether labour law limits flagging and staff must be told.'
- B. 'We applied the four questions, classified the pilot as appropriate with manager review, and plan to start next week; the vendor confirms compliance in writing, so please confirm you agree.'
- C. 'Could we use an AI tool for attendance flagging for our 2,300 staff? Please advise whether that is allowed and let us know the procedure for approval.'
- D. 'Here is the workflow, who is affected, and the control; we believe disclosure to staff is the safer course and propose to disclose by default, so please note our decision.'

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Retail chain ki HR director 2,300 store employees mein "unusual attendance patterns" flag karne wala tool pilot karna chahti; flagged ka manager follow-up, unflagged kabhi review nahi. Usay yaqeen nahi local labour law employment faislon par asar daalne wali automated flagging limit karta ya nahi, aur staff ko batana zaroori ya nahi. Vendor "likh kar compliance confirm" karne ko tayyar. Counsel ek hafte bahar. Governance ko chaar messages draft — sab workflow, affected staff aur control naam karte; farq yeh ke reviewer se kya karne ko kehte.

**Sawal:** Kaunsa message sab se mazboot escalation hai?

**Options ka matlab:**

- **A** — "Workflow yeh hai, kaun affected (kabhi flag na hone wale staff samet), joda gaya control, aur unsettled point: kya labour law flagging limit karta aur staff ko batana zaroori."
- **B** — "Chaar sawal lagaye, pilot manager review ke saath appropriate, agle hafte shuru; vendor likh kar compliance confirm karta, please agree karo."
- **C** — "Kya 2,300 staff ke liye attendance flagging AI tool use kar sakte? Batayein allowed hai aur approval ka procedure kya."
- **D** — "Workflow, affected, control yeh hain; hum samajhte disclosure safe hai aur default disclose karne ka irada — hamara faisla note kar lein."

</details>

**Answer:** A

- ✅ **A** — It escalates the question with reasoning attached and names the unresolved point.
- ❌ **B** — A verdict for approval invites a quick yes and treats a vendor's assurance as the organisation's legal decision.
- ❌ **C** — A bare 'can I use this?' has no framework, control or unresolved point attached.
- ❌ **D** — It reports a decision rather than asking about the unresolved legal point.

**Yaad rakho:** Verdict ki manzoori nahi maango: workflow, kaun asar mein (jo flag na hon wo bhi), control, aur wo point jo framework tay nahi karta.

*Grounded in: Governance §4.3 (escalate the question, not a verdict; three signals; a strong escalation gives the reviewer something specific to decide)*

---

### Q47.
A team lead audits a month of her team's AI use. Findings: an unreleased product spec was uploaded to an entry point nobody approved; a Skill was enabled with no source check; a client report skipped its review gate twice at month end; the approved workspace needs a twelve-step login while the unapproved one takes one click; the tool's own usage dashboard was not consulted. A manager proposes discipline for three staff, a quarter-long ban on AI tools, and a hidden review of individual chat logs. The team lead knows that the risk lives in the distance between what the policy says and what people do, that audits should find system gaps, and that people drift to whichever path is easier. She has four candidate plans for the next quarter.

**Which plan follows the framework?**

- A. Discipline the three staff, run the hidden log review so that people behave as if watched, and keep the login as it is because policy is policy and security cannot be relaxed.
- B. Send a firm reminder on approved entry points and add a mandatory five-minute training, leaving the login unchanged, since awareness is what closes the Diligence gap.
- C. Ban the tools for a quarter to reset habits, then reintroduce them with a reminder email on approved entry points and a signed acknowledgment from each user.
- D. Treat it as drift: cut the friction of the approved path, build Skill vetting into Project setup, make the review gate non-negotiable, and audit the process, not the person.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Team lead ek mahine ka AI use audit karti. Findings: unreleased product spec ek unapproved entry point par upload; ek Skill bina source check enable; client report month-end par do dafa review gate skip; approved workspace ka 12-step login, unapproved ek click; tool ka apna usage dashboard dekha hi nahi gaya. Manager: teen staff ko discipline, quarter bhar AI ban, aur individual chat logs ka hidden review. Lead jaanti risk policy aur asal amal ke faasle mein hai, audit system gaps dhoondhe, aur log aasaan raaste ki taraf drift karte. Agli quarter ke chaar plans.

**Sawal:** Kaunsa plan framework follow karta hai?

**Options ka matlab:**

- **A** — Teen ko discipline, hidden log review, login wahi — policy policy hai.
- **B** — Sakht reminder aur lazmi 5-minute training, login wahi — awareness Diligence gap band karti.
- **C** — Quarter bhar ban, phir reminder email aur har user ka signed acknowledgment.
- **D** — Isay drift samjho: approved raaste ki friction kaato, Skill vetting ko Project setup mein daalo, review gate ko non-negotiable banao, aur process audit karo, insaan nahi.

</details>

**Answer:** D

- ✅ **D** — The friction rule: fix the slow approved path, not the tooling; habit-level fixes make the compliant action the default.
- ❌ **A** — A hidden review that becomes a performance review makes people show only their cleanest work.
- ❌ **B** — A reminder and training do not remove the reason people take the one-click path.
- ❌ **C** — Banning a sanctioned tool reliably produces more shadow usage, and a reminder does not reduce the friction.

**Yaad rakho:** Approved raasta 12 steps aur shortcut 1 click: friction kam karo. Audit process ka, banda nahi.

*Grounded in: Governance §8.1-8.3 (usage audit on what people do; audit the process not the person; the friction rule; shadow AI; Diligence gap)*

---

### Q48.
A 12-person analytics consultancy has no AI policy, three regulated clients, and a junior consultant who circulated a 40-clause "official AI policy" over a weekend without the partners' sight, two clauses of which conflict with a client contract. The partners want something honest and usable this week, and the associate who has read the framework says a one-page interim proposal for the right owner to endorse should contain five things. Candidate contents are listed in a table of nine items. The associate says exactly four of a specific list of five belong, and one commonly proposed item does not.

**Which of the following does NOT belong on the one-page interim proposal?**

- A. A statement that the page is the firm's official policy from today, binding staff and making any outside AI use a disciplinary matter.
- B. The AI products and the specific routes approved for work data, and a short list of data types that need confirmation before use.
- C. The human-gate rule for external or consequential outputs, and the review rule for new Skills, connectors and high-authority tools.
- D. One named role or channel for questions and incidents, and a note that regulated work also needs legal, compliance and contractual approval.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** 12 logon ki analytics consultancy: AI policy nahi, teen regulated clients, aur ek junior jisne weekend par partners ke baghair 40-clause "official AI policy" circulate kar di (do clauses client contract se takrati). Partners is hafte imaandar aur usable cheez chahte. Framework parhne wala associate: sahi owner ke endorse karne ke liye one-page interim proposal mein paanch cheezein honi chahiye. Ek aam proposed item belong nahi karta.

**Sawal:** Neeche mein se kaunsi cheez one-page interim proposal mein belong NAHI karti?

**Options ka matlab:**

- **A** — Yeh bayan ke page aaj se firm ki official policy hai, staff par lazmi, aur bahar ka koi bhi AI use disciplinary maamla.
- **B** — Work data ke liye approved AI products aur specific routes, aur un data types ki chhoti list jinhein use se pehle confirmation chahiye.
- **C** — External ya consequential outputs ke liye human-gate rule, aur naye Skills, connectors aur high-authority tools ka review rule.
- **D** — Sawalon aur incidents ke liye ek named role ya channel, aur note ke regulated kaam ko legal, compliance aur contractual approval bhi chahiye.

</details>

**Answer:** A

- ✅ **A** — Do not invent a policy and present it as official; it is a proposal for the owner to endorse.
- ❌ **B** — Approved routes and a short red list are core items.
- ❌ **C** — The gate rule and the review rule for extensions belong on the page.
- ❌ **D** — A named contact is one of the five items, and the note about approvals keeps the proposal honest.

**Yaad rakho:** Interim proposal likho, 'official' mat likho: routes, red list, gate rule, extension review, ek contact.

*Grounded in: Governance §8.4 (when there is no AI policy: an interim proposal for the right owner to endorse; the one-page start; regulated environments)*

---

### Q49.
An operations analyst completes the Evidence strip of a Governance Record for an AI-drafted weekly report. Her draft: "Success measure: account managers complete the factual check before sending. Failure threshold: any AI-generated error big enough to matter reaches a customer. Monitored by: the analyst, monthly. Residual risk: none, because the account manager reviews every report." The Record also lists the re-check triggers. A quality reviewer says the strip has one field that names something other than what the field asks for, and asks the analyst to correct that field. Four rewrites of the field are offered.

**Which is the correct rewrite of the residual-risk field?**

- A. The account manager might skip the factual check on a busy Friday, so the residual risk is that the check is sometimes not completed before the report is sent.
- B. None: the account manager reviews every report and the analyst monitors monthly, so all identified risks have a control and no further risk is expected.
- C. A consistent wording bias across all reports could survive each account manager's individual check, so the monthly sample compares phrasing across customers as well as within each report.
- D. Any AI-generated error big enough to matter that reaches a customer before the account manager has corrected it, which the failure threshold already names.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Ops analyst AI-drafted weekly report ke Governance Record ki Evidence strip bharti: "Success measure: account managers bhejne se pehle factual check poora karte. Failure threshold: koi aham AI error customer tak pahunche. Monitored by: analyst, monthly. Residual risk: none, kyunke account manager har report review karta." Record mein re-check triggers bhi. Quality reviewer: strip ka ek field wo cheez naam karta jo field maangta hi nahi — usay theek karo. Chaar rewrites.

**Sawal:** Residual-risk field ka sahi rewrite kaunsa hai?

**Options ka matlab:**

- **A** — Busy Friday ko account manager factual check skip kar sakta, to risk yeh ke check kabhi bhejne se pehle poora nahi hota.
- **B** — None — manager har report review karta, analyst monthly monitor, har identified risk ka control.
- **C** — Saari reports mein ek consistent wording bias har manager ke individual check se bach sakta, is liye monthly sample customers ke across bhi phrasing compare kare, sirf har report ke andar nahi.
- **D** — Koi aham AI error jo manager ke correct karne se pehle customer tak pahunche — jo failure threshold pehle se naam karta.

</details>

**Answer:** C

- ✅ **C** — Residual risk is what can still go wrong after every planned control works as designed.
- ❌ **A** — That is a control failing, not what remains when the control works as designed.
- ❌ **B** — 'None' restates the design; every real control leaves something outside its boundary.
- ❌ **D** — It restates the failure threshold, and errors the check catches are not residual.

**Yaad rakho:** Residual risk = control theek chalne ke baad bhi jo bacha; control ka fail hona nahi, 'koi nahi' bhi nahi.

*Grounded in: Governance §5.5, §6 and A.1 (the Evidence line; residual risk is what can still go wrong after every planned control works as designed)*

---

### Q50. *(Select TWO — all-or-nothing)*
A consultancy approved an AI-assisted workflow last March, and its Governance Record says: internal audience only; one model family; one approved connector; no outside content; low consequence. Since then: (1) the vendor changed the default model; (2) the summaries now go to the client's board as well as the internal team; (3) the office moved to a new building on the same network; (4) a colleague took over the workflow; (5) the company's logo changed; (6) a new law on automated decision-making took effect that may cover the client's sector. The partner asks which changes trigger a re-check of the record, and the owner says the brief text is unchanged so nothing does.

**Which TWO of the six changes should the owner treat as the strongest re-check triggers?**

- A. Change (3), the office move: any change of location alters the route by which data reaches the assistant, so the record must be reviewed.
- B. Change (2), the audience: the summaries now reach the client's board, which changes who is affected and the consequence of an error.
- C. Change (6), the law: a change in law or policy that may cover the sector must be checked against the record.
- D. Change (5), the logo: outputs carry the company's branding, and any change to branding changes the disclosure the record was approved on.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Consultancy ne pichle March AI workflow approve kiya; Governance Record: sirf internal audience; ek model family; ek approved connector; bahar ka content nahi; low consequence. Tab se: (1) vendor ne default model badla; (2) summaries ab internal team ke saath client ke board ko bhi; (3) office same network ke saath naye building mein; (4) colleague ne workflow sambhala; (5) company logo badla; (6) automated decision-making par naya law aaya jo client ke sector par lagu ho sakta. Partner poochta kaunsi changes re-check trigger karti; owner: brief text same, koi nahi.

**Sawal:** Chhe mein se kaunse DO sab se mazboot re-check triggers hain?

**Options ka matlab:**

- **A** — Change (3) office move — location badalne se data ka route badalta.
- **B** — Change (2) audience — summaries ab client ke board tak, kaun affected aur ghalti ka nateeja badla.
- **C** — Change (6) law — sector par lagu ho sakne wala law ya policy change record se check hona chahiye.
- **D** — Change (5) logo — branding badalne se jis disclosure par record approve hua wo badla.

</details>

**Answer:** B, C

- ✅ **B** — Audience and consequence of error are re-check triggers.
- ✅ **C** — Law, policy, contract or vendor terms changing is a trigger.
- ❌ **A** — Nothing about the route, data or permissions changed with the building.
- ❌ **D** — Branding does not change the model, data, audience, permission, policy or consequence.

**Yaad rakho:** Audience aur qanoon/policy ka badalna trigger hai; imarat aur logo nahi (model badalna bhi trigger hai).

*Grounded in: Governance §8.5 and §9 (re-check when model, feature, connector, data, outside content, audience, consequence, law or policy changes; what changed since we last decided this was okay)*

---

### Q51.
A junior analyst completes a Governance Record for a workflow that summarises supplier complaints for a regulated client. Unsure about the data route, she asks Claude, "Is this workflow compliant?" It replies that it looks fine if her organisation has approved the route. In the Data block she writes: "Route approved. Compliance confirmed by Claude." In the Capability block, she leaves "Outside content it reads" blank because a blank looks unfinished. In the Owner field she writes her own name. The record is dated last March; the assistant's model was replaced in July. She sends it to her manager with the note "ready for sign-off". Her manager has time to correct only the single most serious problem before sign-off.

**Which problem is the most serious?**

- A. The record's date, because a record older than six months has expired and must be redone before it can be signed off by any manager.
- B. The Data block's approval claim rests on an assistant that is not the policy owner; it should read OPEN QUESTION and go to whoever owns the route decision.
- C. The blank 'Outside content it reads' field, because a blank field always looks like an omission, so it should be filled with the most likely answer instead.
- D. The owner field naming the analyst, because the owner must be a director and only a director may be named as the owner of a record for a regulated client.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Junior analyst regulated client ke supplier complaints summarise karne wale workflow ka Governance Record bharti. Data route par shak — Claude se poochti "kya yeh compliant hai?" Jawab: agar organisation ne route approve kiya to theek lagta. Data block mein likhti: "Route approved. Compliance confirmed by Claude." Capability block ka "Outside content it reads" khaali (khaali adhoora lagta). Owner field mein apna naam. Record pichle March ka dated; July mein AI ka model badla. Manager ko "ready for sign-off" note ke saath bhejti. Manager ke paas sign-off se pehle sirf ek sab se sangeen masla theek karne ka waqt.

**Sawal:** Sab se sangeen masla kaunsa hai?

**Options ka matlab:**

- **A** — Record ki date — 6 mahine se purana record expire, dobara banana hoga.
- **B** — Data block ka approval claim us AI par tika hai jo policy owner nahi; wahan OPEN QUESTION likho aur route ka faisla karne wale ko bhejo.
- **C** — Khaali "Outside content" field — sab se mumkin jawab se bhar do.
- **D** — Owner field mein analyst ka naam — regulated client ke record ka owner sirf director ho sakta.

</details>

**Answer:** B

- ✅ **B** — An assistant can challenge the reasoning but cannot certify a route as approved; a guessed 'approved' hides an unknown in a regulated setting.
- ❌ **A** — Records are re-checked when something changes; the model change is a trigger, but no fixed expiry applies.
- ❌ **C** — A blank beats a guessed field; the fix is OPEN QUESTION, and it is less serious than a false approval.
- ❌ **D** — The course does not make the owner a director; what matters is an accountable named person.

**Yaad rakho:** 'Claude ne compliance confirm ki' = ghalat. Na-maloom = OPEN QUESTION aur sahi malik ko bhejo.

*Grounded in: Governance §6 (Governance Record; write OPEN QUESTION where you do not know; re-check triggers) and §1 'Practice safely' (an assistant is not your policy owner or compliance function)*

---

### Q52.
A regulated-client consultancy considers using an AI assistant on client matters. The client's contract restricts third-party processing of its data without written consent. The consultancy's plan: use the enterprise plan of a vendor with a strong security page, admin-controlled memory turned off for everyone, incognito chats for sensitive matters, a code-execution sandbox for spreadsheets, and a Project for each matter. The managing partner says that together these controls make the workflow approved. A compliance associate says each control answers a narrower question and none decides whether client data may enter the route. She lists what each control does not decide.

**Which statement about what the controls do NOT decide is INCORRECT?**

- A. A code-execution sandbox limits where code and file-processing can operate; it does not decide whether the data was authorised for that environment.
- B. Memory off for everyone addresses cross-session reuse of information; it does not decide whether the upload was allowed, or how long the underlying data is kept.
- C. The enterprise plan and the vendor's security page decide the client-consent question, since an enterprise agreement is the written consent the client's contract requires.
- D. An incognito chat addresses history and memory persistence; it does not decide whether the data was permitted to enter the system.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Regulated-client consultancy client matters par AI use karna soch rahi. Client ka contract written consent ke baghair third-party processing mana karta. Plan: strong security page wale vendor ka enterprise plan, sab ke liye admin-controlled memory off, sensitive matters ke liye incognito, spreadsheets ke liye code-execution sandbox, har matter ka Project. Managing partner: yeh sab milkar workflow approve karte. Compliance associate: har control ek tang sawal ka jawab deta, koi yeh tay nahi karta ke client data route mein ja sakta ya nahi; wo list karti har control kya tay NAHI karta.

**Sawal:** Controls kya tay NAHI karte — is baare mein kaunsa bayan INCORRECT hai?

**Options ka matlab:**

- **A** — Sandbox code aur file-processing ki jagah limit karta; yeh tay nahi karta data us environment ke liye authorised tha.
- **B** — Sab ke liye memory off sessions ke paar reuse ko address karta; yeh tay nahi karta upload allowed tha ya data kitni der rakha jaata.
- **C** — Enterprise plan aur vendor ka security page client-consent ka sawal tay karte, kyunke enterprise agreement hi wo written consent hai jo client contract maangta.
- **D** — Incognito history aur memory persistence ko address karta; yeh tay nahi karta data system mein aane ki ijazat thi.

</details>

**Answer:** C

- ✅ **C** — An enterprise plan or a security page is not permission; the client's written consent is a separate matter.
- ❌ **A** — A sandbox is an execution boundary, not an approval boundary.
- ❌ **B** — That is what memory controls do and do not decide.
- ❌ **D** — That is what incognito does and does not decide.

**Yaad rakho:** Har control ek chhota sawal hal karta hai; 'data andar jaa sakta hai?' ka jawab koi nahi deta. Enterprise plan bhi nahi.

*Grounded in: Governance §2.5 (privacy and workspace controls answer narrower questions: a table of what each may help with and does not decide) and §2.4*

---

## Domain 1 — Prompting and Task Execution (14% — 14 questions)

### Q53.
A COO's chief of staff has an assistant shortlist trucking providers for the Lahore to Karachi corridor. The brief has six lines. Outcome: three providers compared, one recommended. Context: 20-tonne monthly load. Constraints: under a stated rate per kilometre. Authority: "choose the sources". Deliverable: a table with rate, transit days, link. Verification: "mark anything unconfirmed as unverified". Three failures occur. Failure X: the assistant silently dropped a provider whose rate was unpublished. Failure Y: it picked between two tied providers by transit time without saying so. Failure Z: it stated a provider's rate as "PKR 118 per km", taken from a 2021 blog, with no mark, because it "confirmed" it from that single blog. The chief of staff must say which line of the brief, when improved, most directly prevents each failure. Four mappings of X, Y, Z are offered.

**Which mapping is correct?**

- A. X: Authority (report exclusions); Y: Authority (say when a tie was broken and how); Z: Verification (what counts as confirmed, including the date and source type).
- B. X: Authority; Y: Context (state that transit time matters); Z: Deliverable (add a date column).
- C. X: Constraints (list required providers); Y: Authority; Z: Verification.
- D. X: Verification (list every provider considered); Y: Constraints (state a tie-break rule); Z: Authority (let it choose sources only from the last year).

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** COO ka chief of staff AI se Lahore–Karachi trucking providers shortlist karwata. Brief ki chhe lines: Outcome (teen compare, ek recommend); Context (20-ton monthly); Constraints (per-km rate ke andar); Authority ("sources tum chuno"); Deliverable (rate, transit days, link ka table); Verification ("unconfirmed ko unverified mark karo"). Teen failures: X — unpublished rate wala provider chupke se drop. Y — do tied providers mein transit time se chuna, bataya nahi. Z — ek provider ka rate "PKR 118 per km" 2021 ke blog se, bina mark, kyunke usi ek blog se "confirm" kiya. Har failure ko sab se seedha kaunsi line (behtar karke) rokti? Chaar mappings.

**Sawal:** Kaunsi mapping (X, Y, Z) sahi hai?

**Options ka matlab:**

- **A** — X: Authority (exclusions report karo); Y: Authority (batao tie kab aur kaise toda); Z: Verification (confirmed kise kehte — date aur source type samet).
- **B** — X: Authority; Y: Context (transit time ahem hai likho); Z: Deliverable (date column jodo).
- **C** — X: Constraints (required providers list); Y: Authority; Z: Verification.
- **D** — X: Verification (har considered provider list karo); Y: Constraints (tie-break rule); Z: Authority (sirf pichle saal ke sources).

</details>

**Answer:** A

- ✅ **A** — Silent decisions are an Authority gap; what counts as 'confirmed' is what Verification, written first, should define.
- ❌ **B** — Context does not tell the assistant to report a tie-break, and a date column does not define what counts as confirmed.
- ❌ **C** — A constraint limits the job; it does not make the assistant report an exclusion it decides on its own.
- ❌ **D** — The tie-break is a decision it may take alone or must report, which is Authority, and confirmation is Verification.

**Yaad rakho:** Chupke faisle = Authority ki kami. 'Confirmed' ka matlab (tareekh, source) = Verification ki kami.

*Grounded in: Just Delegate It §3 and §7 (six-line brief: Authority and Verification are the two people skip; without Authority AI decides silently)*

---

### Q54. *(Select TWO — all-or-nothing)*
A procurement analyst at a hospital group asks an agent in a desktop coworking product to clean up a shared vendor master list. Timeline. 09:00: she writes "list your plan and wait for my go-ahead" at the top of the brief and runs it in Manual approval mode. 09:03: the agent asks two clarifying questions and then begins work. 09:07: it asks approval to rename a file; she approves. 09:12: it asks approval to move a file; she approves. 09:31: it reports "done" and its summary lists six steps. Afterwards she finds that two vendor records with different bank accounts were merged because they had the same name, and that the summary does not mention it. She had assumed Manual mode meant she would see a plan first, and that approving each action was her review of the work.

**Which TWO statements about what happened are correct?**

- A. Approving each action was the plan review, so her approvals cover the merge, and the agent is not at fault for merging records she implicitly approved by approving the moves.
- B. Manual mode pauses for actions but doesn't produce a plan; plan-first is an instruction, so the brief had to say 'show me your plan and wait for approval'.
- C. The failure is the silent change: add an Authority line letting the agent find a better route but requiring it to report any deviation, and compare plan to actions.
- D. Skip mode would have avoided the problem, because it removes the interruptions and lets the agent work through the plan she wrote without asking about each file action.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Hospital group ki procurement analyst desktop coworking agent se shared vendor master list clean karwati. Timeline: 09:00 brief ke upar "plan list karo aur go-ahead ka intezaar karo" likh kar Manual mode mein chalaya. 09:03 agent do clarifying sawal poochh kar kaam shuru. 09:07 file rename ki approval — di. 09:12 file move ki approval — di. 09:31 "done", summary mein chhe steps. Baad mein pata chala same naam ki wajah se alag bank accounts wale do vendor records merge hue, summary mein zikr nahi. Usne samjha tha Manual mode pehle plan dikhayega, aur har action approve karna hi uska review tha.

**Sawal:** Jo hua uske baare mein kaunse DO bayan sahi hain?

**Options ka matlab:**

- **A** — Har action approve karna hi plan review tha, to uski approvals merge ko cover karti — agent ki ghalti nahi.
- **B** — Manual mode actions par rukta magar plan nahi banata; plan-first ek instruction hai, brief mein "mujhe plan dikhao aur approval ka intezaar karo" likhna zaroori tha.
- **C** — Masla chupki change hai: Authority line jodo jo agent ko behtar raasta dhoondne de magar har deviation report karwaye, aur plan ko actions se compare karo.
- **D** — Skip mode masla na hone deta — interruptions khatam, agent uska plan bina pooche chalata.

</details>

**Answer:** B, C

- ✅ **B** — Plan-first is an instruction, not a guarantee of Manual mode.
- ✅ **C** — An approved plan is not a cage; what the agent may not do is change something that matters without telling you.
- ❌ **A** — Action-by-action approval is not review of a plan, and the merge was never presented to her.
- ❌ **D** — Skip removes ordinary approvals and the Auto action check; it does not create a plan or a duty to report.

**Yaad rakho:** Manual = har action par pooche, plan nahi banata. Plan-first brief mein likho, aur 'badlo to batao' ka Authority.

*Grounded in: General Agents on the Web §7-8 (Manual, Auto, Skip; Manual does not create a plan; plan-first is an instruction) and Just Delegate It §7 (the failure is the silent change)*

---

### Q55.
A compliance analyst pastes a two-page regulator circular into an assistant: "Using only the text below, answer three questions. For each answer quote the sentence you used. If the text does not say, write 'not in the source'." She checks the quotes against the circular. Quote 1 appears word for word. Quote 2 appears, but "thirty days" has become "sixty days". Quote 3 does not appear anywhere in the circular. The answers feed a client note due this afternoon. She classifies each quote as exact, paraphrased, or invented, and decides what to do with each answer. A colleague, hurrying, says two of three quotes are at least close and that the instruction proves the assistant stayed inside the text. She has four candidate accounts of the three quotes and the actions.

**Which account is correct?**

- A. Quote 1 paraphrased (recheck all three by a second run); Quote 2 exact; Quote 3 invented (rerun to see whether the sentence appears in a second attempt).
- B. Quote 1 exact; Quote 2 paraphrased (usable with a small edit because the wording is close); Quote 3 invented (discard the answer and rely on the assistant's other two).
- C. Quote 1 exact; Quote 2 exact in meaning (usable because sixty and thirty are both time limits); Quote 3 paraphrased (correct it from the assistant's own explanation).
- D. Quote 1 exact; Quote 2 altered from the source, so correct it and treat the answer as unverified; Quote 3 invented, so the answer is unsupported unless the text is found.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Compliance analyst regulator ka 2-page circular paste karke: "Sirf neeche ke text se teen sawal ke jawab do, har jawab ka jumla quote karo, text mein na ho to 'not in the source' likho." Quotes circular se check: Quote 1 hubahu. Quote 2 maujood magar "thirty days" ab "sixty days". Quote 3 circular mein kahin nahi. Jawab aaj dopahar ke client note mein jayenge. Wo har quote ko exact, paraphrased ya invented classify karti aur har jawab par faisla. Jaldi mein colleague: do quotes qareeb hain, instruction saabit karti AI text mein raha. Chaar accounts.

**Sawal:** Kaunsa account sahi hai?

**Options ka matlab:**

- **A** — Quote 1 paraphrased (doosre run se teeno recheck); Quote 2 exact; Quote 3 invented (rerun karke dekho jumla aata hai).
- **B** — Quote 1 exact; Quote 2 paraphrased (chhote edit se usable); Quote 3 invented (jawab discard, baaqi do par bharosa).
- **C** — Quote 1 exact; Quote 2 matlab mein exact (sixty aur thirty dono time limits); Quote 3 paraphrased (AI ki apni explanation se correct).
- **D** — Quote 1 exact; Quote 2 source se badla hua, to correct karo aur jawab unverified samjho; Quote 3 invented, to jawab unsupported jab tak text na mile.

</details>

**Answer:** D

- ✅ **D** — A close-but-not-exact quote means the assistant paraphrased and called it a quote; a missing one means it was invented.
- ❌ **A** — Quote 1 is exact and quote 2 is not; reruns do not verify anything against the circular.
- ❌ **B** — A changed figure is an error in the answer, not a small edit.
- ❌ **C** — The figure differs, so the quote is not exact, and a missing sentence is not a paraphrase of anything in the circular.

**Yaad rakho:** Quote ko circular mein dhoondo: lafz ba lafz = exact, thoda badla = paraphrase/ghalti, gayab = ijaad.

*Grounded in: Just Delegate It §5 (using only the text below; quote the sentence; find one quote word for word: exact, paraphrased, or invented; 'not in the source' is a good answer)*

---

### Q56.
A tender team has three cement suppliers' proposals and written criteria (price 40%, delivery reliability 35%, exit terms 25%). In one request they asked Claude to extract, compare, score and recommend. The recommendation cites "Supplier A: PKR 1,090 per bag", and the team lead cannot tell where it came from. She wants four steps, each checked, so that a mistake cannot travel unseen: extract facts into one table (price, contract length, exit terms, support hours); compare using only the table; score against the weights; draft the recommendation. Suppose the price extraction is wrong for Supplier A (actual PKR 1,900), and nobody checks until the final draft. She wants to know at which step the mistake would first change a number a reader sees, and where the check is most valuable.

**Which statement is correct?**

- A. The wrong price carries through comparison, score and draft, looking fine at each stage, so check extraction first, verifying several cells against each proposal before continuing.
- B. The wrong price would affect only the draft, so the check is most valuable at the last step, where the whole recommendation can be read against the three proposals.
- C. The wrong price would be caught by the comparison step, which uses only the table, since a comparison of three suppliers would expose one that is out of line.
- D. The wrong price would first change a number the reader sees at scoring, so the most valuable check is on the scores, where the weights turn facts into a ranking.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Tender team ke paas teen cement proposals aur criteria (price 40%, delivery reliability 35%, exit terms 25%). Ek request mein extract, compare, score, recommend — recommendation mein "Supplier A: PKR 1,090 per bag", lead ko pata nahi kahan se aaya. Wo chaar checked steps chahti: facts ek table mein (price, contract length, exit terms, support hours); sirf table se compare; weights se score; recommendation draft. Farz karo Supplier A ki price extraction ghalat (asal 1,900) aur final draft tak koi check nahi karta. Kis step par ghalti pehli dafa reader ko dikhne wala number badalti, aur check sab se qeemti kahan?

**Sawal:** Kaunsa bayan sahi hai?

**Options ka matlab:**

- **A** — Ghalat price comparison, score aur draft sab mein chalti hai, har stage par theek lagti; is liye pehle extraction check karo — aage badhne se pehle har proposal se kai cells verify.
- **B** — Ghalat price sirf draft par asar karti, aakhri step par check sab se qeemti.
- **C** — Comparison step pakad lega — teen suppliers ka comparison out-of-line wala dikha dega.
- **D** — Ghalat price reader ko pehli dafa scoring par dikhti, scores ka check sab se qeemti.

</details>

**Answer:** A

- ✅ **A** — Put the step where a mistake spreads farthest first, and check it before you continue.
- ❌ **B** — One check at the end can only inspect the ending, and an early error looks fine by then.
- ❌ **C** — The comparison uses only the table, so a wrong table entry is taken as true.
- ❌ **D** — The error is already in the comparison table; a check on scores would find a wrong input only by accident.

**Yaad rakho:** Ghalat price extraction se draft tak sab jagah phailti hai; pehle extraction, us par check.

*Grounded in: AI Fluency §4.2 (process description: split by order; extraction goes first because a wrong price carries through comparison, scoring and draft; check before you send the next request)*

---

### Q57. *(Select TWO — all-or-nothing)*
Four asks are sent to an assistant by different people, and a trainer wants to classify each by kind of ask (brainstorming, research, drafting, analysis) and say what to tighten and what to loosen. Ask 1: "List ten completely different campaign directions for a low-sugar cola for young urban buyers; avoid sport and family themes." Ask 2: "Map the evidence on whether sugar taxes reduced consumption in South Asia; use only peer-reviewed studies and official statistics; do not assume the answer." Ask 3: "Write a 300-word board update on Q2 sales in a formal tone with three headings and these five facts." Ask 4: "Using the attached churn file, compute monthly churn by plan and tell me what the data shows." The trainer says two of the asks are tightened and loosened in the right places, and two are backwards.

**Which TWO asks are tightened and loosened correctly?**

- A. Ask 3, drafting: it is correctly loose, since a board update should leave the assistant room to choose its own facts and structure from the data it has.
- B. Ask 4, analysis: it is correctly tight, since it names the file and the computation, and it should also state the conclusion the analyst expects to confirm.
- C. Ask 1, brainstorming: it tightens the problem, the audience and what to avoid, and leaves structure and format loose, so it can yield truly different directions.
- D. Ask 2, research: it tightens scope, sources and what counts as evidence, and loosens the answer by saying not to assume it.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Chaar asks AI ko alag logon ne bheje; trainer har ek ko kism (brainstorming, research, drafting, analysis) se classify karke batana chahta kya tight aur kya loose ho. Ask 1: "Young urban buyers ke liye low-sugar cola ki das bilkul alag campaign directions; sport aur family themes se bacho." Ask 2: "South Asia mein sugar taxes ne consumption kam ki ya nahi uska evidence map karo; sirf peer-reviewed studies aur official statistics; jawab assume mat karo." Ask 3: "Q2 sales par formal tone mein teen headings aur in paanch facts ke saath 300-word board update." Ask 4: "Attached churn file se plan-wise monthly churn compute karo aur batao data kya dikhata." Trainer: do sahi jagah tight/loose, do ulte.

**Sawal:** Kaunse DO asks sahi tight aur loose hain?

**Options ka matlab:**

- **A** — Ask 3 (drafting) sahi taur par loose — board update mein AI ko apne facts aur structure chunne ki jagah.
- **B** — Ask 4 (analysis) sahi tight — file aur computation naam karta, aur analyst jo nateeja confirm karna chahta wo bhi likhna chahiye.
- **C** — Ask 1 (brainstorming) — problem, audience aur kya avoid karna tight karta, structure aur format loose, is liye waqai alag directions de sakta.
- **D** — Ask 2 (research) — scope, sources aur evidence kise kehte tight karta, aur jawab ko "assume mat karo" keh kar loose.

</details>

**Answer:** C, D

- ✅ **C** — For brainstorming you tighten the problem, audience and what to avoid, and loosen structure, tone, format and length.
- ✅ **D** — For research you tighten scope, sources and evidence, and never say what you expect to find.
- ❌ **A** — Drafting needs almost everything tightened (voice, length, structure, facts, format); this ask is tight, but the option calls it loose.
- ❌ **B** — For analysis you tighten the data, definitions and exact question, and loosen the conclusion: never state it.

**Yaad rakho:** Brainstorm: masla tang, shakal dheeli. Research: sources tang, jawab dheela. Drafting: sab tang. Analysis: data tang, natija dheela.

*Grounded in: AI Prompting 2026 §7 'One loop, four kinds of ask' (brainstorming, research, drafting, analysis: what to tighten and loosen; the failure if you get it backwards)*

---

### Q58. *(Select TWO — all-or-nothing)*
A CFO writes: "Help me defend my decision to acquire the Gulberg site; here is the deal memo." The assistant produces a confident defence and no counter-arguments. Her board has two sceptical directors. The CFO reads about sycophancy and lists five phrasings she has used recently, asking which contain bait that signals the conclusion the assistant should reach. (a) "Find evidence that this strategy will work." (b) "Compare approach A and approach B and score each on cost, risk and time." (c) "Tell me my draft is ready to send." (d) "Evaluate this strategy; list the strongest arguments for and against." (e) "Confirm that this code is correct." She has to identify the bait phrasings for a briefing note, and has time to explain only two.

**Which TWO phrasings contain bait?**

- A. (c) 'Tell me my draft is ready to send': it signals the answer wanted, and praise is the agreeable reply.
- B. (b) 'Compare approach A and approach B and score each on cost, risk and time': it prejudges that approach A is better, so the scores will follow.
- C. (d) 'Evaluate this strategy; list the strongest arguments for and against': it signals a preferred conclusion by naming the strategy first.
- D. (a) 'Find evidence that this strategy will work': the conclusion is fixed, so the assistant fills in support.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** CFO likhti: "Gulberg site khareedne ke mere faisle ka difaa karne mein madad karo; yeh deal memo hai." AI confident difaa, koi counter-argument nahi. Board mein do shakki directors. CFO sycophancy ke baare mein parh kar apni haal ki paanch phrasings list karti, poochti kin mein "bait" hai jo AI ko batata ke kaunsa nateeja chahiye: (a) "Evidence dhoondo ke yeh strategy kaam karegi." (b) "Approach A aur B compare karo aur har ek ko cost, risk, time par score karo." (c) "Mujhe batao mera draft bhejne ke liye ready hai." (d) "Is strategy ko evaluate karo; haq aur khilaf sab se mazboot dalail list karo." (e) "Confirm karo yeh code sahi hai." Sirf do explain kar sakti.

**Sawal:** Kin DO phrasings mein bait hai?

**Options ka matlab:**

- **A** — (c) "Batao draft ready hai" — chahiye wala jawab signal karta, tareef agreeable reply hai.
- **B** — (b) "A aur B compare aur score" — pehle se tay karta A behtar, scores peeche chalenge.
- **C** — (d) "Evaluate karo; haq aur khilaf" — strategy ka naam pehle le kar preferred nateeja signal karta.
- **D** — (a) "Evidence dhoondo ke kaam karegi" — nateeja fixed, AI support bharta.

</details>

**Answer:** A, D

- ✅ **A** — It signals the answer and invites praise instead of a graded critique.
- ✅ **D** — The conclusion is stated as a fixed point and the ask is for support.
- ❌ **B** — It names criteria and prejudges nothing; it is the neutral rewrite.
- ❌ **C** — It asks for both sides and states no conclusion.

**Yaad rakho:** 'Evidence dhoondo ki kaam karega', 'batao ready hai': bait. 'Evaluate, dono taraf' aur 'score on criteria': neutral.

*Grounded in: AI Prompting 2026 §6 (sycophancy: bait phrasings and neutral rewrites); What AI Actually Is Idea 6*

---

### Q59. *(Select TWO — all-or-nothing)*
A reporter drafts a 900-word feature with an assistant. Her editor's note: "Make it better." Version A: she asks for a general sweep; the result is slightly smoother but has softened two facts. Version B: she gives the assistant this feedback: "The second section assumes enterprise customers. Our readers are solo founders, so the advice is too expensive to follow. Rewrite that section for a one-person business with a small budget." Version C: "Wrong, redo the second section." Version D: "Rewrite the whole article for solo founders in a friendlier tone." She wants to know which feedback follows the pattern of problem, why it matters, and direction, while being the smallest message that fixes the fault, and which practices help on the remaining passes.

**Which TWO statements are correct?**

- A. Version B follows the pattern: problem (enterprise assumption), why it matters (too expensive for solo founders) and direction (rewrite that section), staying targeted.
- B. Version C follows the pattern because 'wrong' is the problem, 'redo' is the direction, and the reason is obvious from the context, so no more detail is needed.
- C. Version D follows the pattern, since it gives a direction (solo founders, friendlier tone) and a reason, and a whole-article rewrite ensures consistency of tone across sections.
- D. Further passes should be named (clarity, tone, formatting), and for higher stakes ask for two or three drafts and edit the strongest.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Reporter AI ke saath 900-word feature draft karti; editor ka note: "Make it better." Version A: general sweep — thoda smooth magar do facts naram ho gaye. Version B feedback: "Doosra section enterprise customers assume karta. Hamare readers solo founders hain, to advice follow karna bohat mehnga. Us section ko chhote budget wale one-person business ke liye rewrite karo." Version C: "Ghalat, doosra section dobara karo." Version D: "Poora article solo founders ke liye friendlier tone mein rewrite karo." Kaunsa feedback problem–kyun–direction pattern follow karta aur ghalti theek karne wala sab se chhota message hai, aur baaqi passes mein kya practices madad karti?

**Sawal:** Kaunse DO bayan sahi hain?

**Options ka matlab:**

- **A** — Version B pattern follow karta: problem (enterprise assumption), kyun matter (solo founders ke liye mehnga), direction (wo section rewrite) — targeted.
- **B** — Version C pattern follow karta — "ghalat" problem, "redo" direction, wajah context se zahir.
- **C** — Version D pattern follow karta — direction aur wajah deta, poora rewrite tone consistent rakhta.
- **D** — Aage ke passes named hon (clarity, tone, formatting), aur zyada stakes par do-teen drafts maango aur strongest edit karo.

</details>

**Answer:** A, D

- ✅ **A** — Problem, why it matters, direction, and only the faulty section.
- ✅ **D** — Named passes and multiple drafts reduce drift and improve the outcome.
- ❌ **B** — The problem, why and direction are all missing in specifics; the next attempt is a guess.
- ❌ **C** — It gives direction but not the problem or why it matters, and it re-runs everything instead of correcting the fault.

**Yaad rakho:** Feedback = kya masla, kyun ahem, kis taraf; sirf ghalat hissa. Named passes, aam sweep nahi.

*Grounded in: AI Fluency §5 (Description and Discernment loop; feedback pattern: problem, why it matters, direction; edit in named passes; ask for two or three drafts)*

---

### Q60.
A consultancy's practice lead applies Anthropic's three-question test to decide which of six recurring tasks deserve a Project: does the task come back; is the background the same each time; is the output shape the same each time. Two yes answers out of three earn the Project. Task 1: a monthly board report, same background, same format. Task 2: a one-off market-entry paper. Task 3: weekly client summary, same client background, different layout each week. Task 4: a new-hire welcome email, same every time but background differs each hire. Task 5: an ad hoc wording question. Task 6: a quarterly regulator return, same background, same format, done by three different analysts. She has to name exactly the tasks that earn a Project and explain any that do not.

**Which set of tasks earns a Project?**

- A. Tasks 1, 2, 3 and 6: a one-off paper also earns a Project, since the background stays stable for the length of the engagement.
- B. Tasks 1, 3, 4 and 6: each answers yes to at least two of the three questions (comes back; same background; same output shape).
- C. Tasks 1 and 6 only: a Project needs all three yes answers, and only the two fully repeating tasks satisfy all three.
- D. Tasks 1, 3, 4, 5 and 6: any repeated conversation with the assistant benefits from a Project, including an ad hoc question that comes up from time to time.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Practice lead Anthropic ka teen-sawal test chhe recurring tasks par lagata: kya task wapas aata; background har dafa same; output shape har dafa same; teen mein do "haan" = Project. Task 1: monthly board report, same background, same format. Task 2: one-off market-entry paper. Task 3: weekly client summary, same background, har hafte alag layout. Task 4: new-hire welcome email, har dafa same magar har hire ka background alag. Task 5: ad hoc wording sawal. Task 6: quarterly regulator return, same background, same format, teen alag analysts karte. Exactly kaunse tasks Project kamate?

**Sawal:** Tasks ka kaunsa set Project kamata hai?

**Options ka matlab:**

- **A** — Tasks 1, 2, 3 aur 6 — one-off paper ka bhi engagement bhar background stable.
- **B** — Tasks 1, 3, 4 aur 6 — har ek teen mein se kam az kam do sawalon par "haan" (wapas aata; same background; same output shape).
- **C** — Sirf Tasks 1 aur 6 — Project ko teeno "haan" chahiye.
- **D** — Tasks 1, 3, 4, 5 aur 6 — har repeated conversation ko Project faida deta.

</details>

**Answer:** B

- ✅ **B** — Two yes answers out of three earn the Project; Task 4 comes back and has a stable shape.
- ❌ **A** — A one-off paper does not come back and has a unique shape.
- ❌ **C** — The test needs two of three, not all three.
- ❌ **D** — An ad hoc question does not come back with the same background or shape.

**Yaad rakho:** Project ka test: dohrata hai, background wahi, output shakal wahi; teen mein se do 'haan'.

*Grounded in: Just Delegate It §8 and What AI Actually Is A.5 (Anthropic's test for a Project: does it come back, same background, same output shape; two yes answers earn it)*

---

### Q61.
Four situations are described to a trainer, who must match each to the smallest move in the intervene table (stop and restate the outcome; correct; redirect; change the requirement; escalate capability; take the job back). Situation 1: the assistant answered a question the user did not ask. Situation 2: one figure in an otherwise good table is wrong. Situation 3: the assistant is heading toward paid courses when the user wanted free ones, but has not produced any yet. Situation 4: on a several-step job needing a careful comparison, the assistant's answers are shallow even after two corrections, and the plan has a stronger model available. The trainer knows the wrong-level fix is "escalate", and that an alert learner usually starts fast and moves up. She offers four mappings of Situations 1 to 4.

**Which mapping is correct?**

- A. 1: correct; 2: stop and restate the outcome; 3: redirect; 4: take the job back.
- B. 1: stop and restate; 2: correct; 3: redirect; 4: escalate to a stronger model or thinking.
- C. 1: change the requirement; 2: correct; 3: redirect; 4: escalate.
- D. 1: stop and restate the outcome; 2: redirect; 3: correct; 4: escalate.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Trainer ko chaar situations ko "intervene table" ke sab se chhote move se jodna: (stop and restate the outcome; correct; redirect; change the requirement; escalate capability; take the job back). Situation 1: AI ne wo sawal ka jawab diya jo user ne poocha hi nahi. Situation 2: achhe table mein ek figure ghalat. Situation 3: AI paid courses ki taraf ja raha jabke user ko free chahiye, abhi kuch banaya nahi. Situation 4: kai-step job jismein careful comparison chahiye, do corrections ke baad bhi jawab shallow, aur plan mein stronger model available. Trainer: wrong-level fix "escalate" hai, aur alert learner aam taur par fast se shuru karke upar jaata.

**Sawal:** Situations 1–4 ki kaunsi mapping sahi hai?

**Options ka matlab:**

- **A** — 1: correct; 2: stop and restate; 3: redirect; 4: take the job back.
- **B** — 1: stop and restate; 2: correct; 3: redirect; 4: stronger model ya thinking par escalate.
- **C** — 1: change the requirement; 2: correct; 3: redirect; 4: escalate.
- **D** — 1: stop and restate; 2: redirect; 3: correct; 4: escalate.

</details>

**Answer:** B

- ✅ **B** — The symptom tells you the move, and the smallest move that works is used first.
- ❌ **A** — A wrong figure is corrected by naming it; taking the job back comes after escalation fails.
- ❌ **C** — The assistant answered a different question; the requirement did not change, so the outcome is restated.
- ❌ **D** — A wrong figure is a correction, and a heading-the-wrong-way case is a redirect.

**Yaad rakho:** Alag sawal = rok kar outcome dohrao; ek ghalat figure = correct; ghalat simt = redirect; gehrai nahi = escalate.

*Grounded in: Just Delegate It §9 (intervene: six moves; the symptom tells you which; escalate is the one people miss) and §10*

---

### Q62. *(Select TWO — all-or-nothing)*
A tax associate asks an assistant: "Summarise the changes to withholding tax on services this year." The reply is fluent, cites section numbers and a threshold, and has no links. The associate recalls that the finance act passed after the assistant's training cutoff. A colleague explains three retrieval modes: pretrained only, a web search that brings pages into the window, and a deeper research report from many sources; and that wording steers which fires ("summarise X" tends to stay pretrained; "what's the latest" and named places or dates tend to search; "research thoroughly, with a citation report" triggers research). The associate has to send the client a note within the hour, and needs the current thresholds with a source she can open.

**Which TWO changes to the request best fit?**

- A. Ask for a full research-mode report on the whole tax regime, since a cited multi-source report is always the safest form of answer for a client note.
- B. Turn on extended thinking and ask the assistant to reason step by step about what the finance act probably changed, since deeper reasoning reduces invented details.
- C. Ask for the supporting sentence for each claim and the date on each page, so she can confirm currency and the exact threshold.
- D. Ask explicitly for a search, and name the source types to use (the official gazette and the revenue authority), instead of a bare 'summarise'.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Tax associate AI se poochta: "Is saal services par withholding tax ki changes summarise karo." Jawab rawaan, section numbers aur threshold cite, links nahi. Usay yaad finance act AI ke training cutoff ke baad pass hua. Colleague teen retrieval modes samjhata: sirf pretrained; web search jo pages window mein laata; aur kai sources se deeper research report — aur wording tay karti kaunsa chale ("summarise X" aksar pretrained par rehta; "what's the latest", naam wali jagahein ya dates aksar search chalati; "research thoroughly, citation report ke saath" research chalata). Ek ghante mein client note; current thresholds aise source ke saath chahiye jo wo khol sake.

**Sawal:** Request mein kaunsi DO changes sab se fit hain?

**Options ka matlab:**

- **A** — Poore tax regime par full research-mode report — cited multi-source report hamesha sab se safe.
- **B** — Extended thinking on karke AI se step by step reason karwao finance act ne kya badla hoga.
- **C** — Har claim ka supporting jumla aur har page ki date maango, taake currency aur exact threshold confirm ho.
- **D** — Saaf taur par search maango aur source types naam karo (official gazette, revenue authority), bare "summarise" ki jagah.

</details>

**Answer:** C, D

- ✅ **C** — Quotes and dates bring the original wording into view and reveal staleness.
- ✅ **D** — Wording steers the mode; naming sources avoids default popular sources.
- ❌ **A** — Research is for a document you can act on; for a current threshold it is a slow and wasteful route.
- ❌ **B** — Thinking adds reasoning over what the model has; it does not fetch a post-cutoff law.

**Yaad rakho:** 'Summarise' = pretrained. Search maango, sources ke naam do, sentence aur tareekh maango.

*Grounded in: AI Prompting 2026 §3 (three retrieval modes; phrasing steers which fires; name the sources; ask for quotes); What AI Actually Is A.8 (say 'search the web' when currency matters)*

---

### Q63.
A teacher commissions code from an assistant with a five-part brief to grade 200 students across three spreadsheets. Her Goal, Input and Output sections were complete. The first script fails in three ways. (i) It crashes on a student with a blank marks cell. (ii) It weights the practical exam wrongly for bilingual students because the school gives that exam extra weight, which she did not mention. (iii) It treats "AB" (absent) as zero and lowers the grade. Before rewriting the brief she asks for discovery: "Before doing anything, examine the files and tell me what could be unclear, inconsistent or surprising." The assistant replies with a list including blank cells, three name spellings and two files using percentages while one uses raw marks. She now must decide which section each failure belongs in.

**Which mapping of failures to sections is correct?**

- A. (i) Rules; (ii) Edge cases; (iii) Rules.
- B. (i) Input; (ii) Rules; (iii) Edge cases.
- C. (i) Edge cases; (ii) Output; (iii) Rules.
- D. (i) Edge cases; (ii) Rules; (iii) Edge cases.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Teacher five-part brief se 200 students ko teen spreadsheets se grade karne ka code likhwati; Goal, Input, Output complete. Pehla script teen tarah fail: (i) khaali marks cell wale student par crash. (ii) Bilingual students ke liye practical exam ki weighting ghalat — school extra weight deta jo usne bataya nahi. (iii) "AB" (absent) ko zero samajh kar grade kam kar deta. Brief dobara likhne se pehle discovery: "Kuch karne se pehle files dekho aur batao kya unclear, inconsistent ya hairan-kun ho sakta." AI ki list: khaali cells, teen naam spellings, do files percentages aur ek raw marks. Har failure kis section mein belong karti?

**Sawal:** Failures ki sections se kaunsi mapping sahi hai?

**Options ka matlab:**

- **A** — (i) Rules; (ii) Edge cases; (iii) Rules.
- **B** — (i) Input; (ii) Rules; (iii) Edge cases.
- **C** — (i) Edge cases; (ii) Output; (iii) Rules.
- **D** — (i) Edge cases; (ii) Rules; (iii) Edge cases.

</details>

**Answer:** D

- ✅ **D** — Blank and absent values are what imperfect data should do; the extra weighting is knowledge only she has.
- ❌ **A** — Rules carry what only you know (the weighting); edge cases decide what imperfect data should do.
- ❌ **B** — The input description was complete; a blank cell is an edge case.
- ❌ **C** — The weighting is a Rule, and how to treat an absent mark is an edge case.

**Yaad rakho:** Khali/'AB' = Edge cases. School ka extra weight = Rules (jo sirf tum jaante ho).

*Grounded in: Code You Never Write §5 (five-part brief: Rules carry what only you know; Edge cases decide what imperfect data should do; discovery as the first prompt)*

---

### Q64.
An owner uploads twelve months of expense data and asks an assistant for monthly fuel totals. Four replies come back in a test, all with the same annual figure PKR 6.41 million. Reply 1: a table of monthly totals and a sentence that the analysis "covers the full year". Reply 2: the same, plus "I am highly confident". Reply 3: shows the code, states it read 2,431 rows and columns date, category and amount, gives monthly totals as computed, and lists 14 rows with blank dates rather than dropping them. Reply 4: an explanation in plain English of how fuel costs are usually summed, then the totals. The accountant says the tell of whether code ran is what a reply contains beyond the number. The owner will quote the figure to a lender.

**Which statement about the replies is INCORRECT?**

- A. Reply 4 shows code was run, because a clear plain-English explanation of the method proves the method was carried out on the owner's file.
- B. Reply 2 does not show that code ran: a statement of high confidence is the assistant's voice and is not evidence of computation.
- C. Reply 1 does not show that code ran: it asserts coverage of the full year but has no code block, no row count and no column names.
- D. Reply 3 shows code was run: it includes the code, the row count and column names, and a statement of what was computed, which is what evidence looks like.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Owner 12 mahine ka expense data upload karke monthly fuel totals maangti. Test mein chaar replies, sab ka annual PKR 6.41 million. Reply 1: monthly totals ka table aur jumla ke analysis "poora saal cover karta". Reply 2: wahi, plus "I am highly confident". Reply 3: code dikhata, batata 2,431 rows aur date, category, amount columns parhe, monthly totals computed, aur 14 blank-date rows list karta (drop nahi kiye). Reply 4: plain English mein fuel costs aam taur par kaise sum hoti, phir totals. Accountant: code chala ya nahi ki pehchaan number ke ilawa reply mein kya hai. Figure lender ko quote hoga.

**Sawal:** Replies ke baare mein kaunsa bayan INCORRECT hai?

**Options ka matlab:**

- **A** — Reply 4 dikhata code chala — method ki saaf plain-English explanation saabit karti method owner ki file par chala.
- **B** — Reply 2 nahi dikhata code chala — high confidence AI ki awaaz hai, computation ka saboot nahi.
- **C** — Reply 1 nahi dikhata — poore saal ka daawa magar code block, row count, column names nahi.
- **D** — Reply 3 dikhata code chala — code, row count, column names aur kya compute hua, yahi evidence hai.

</details>

**Answer:** A

- ✅ **A** — A description of a method is not a record that it ran on this file; without code, counts and columns it is an opinion about the data.
- ❌ **B** — Correct: confidence is a style.
- ❌ **C** — Correct: it is an opinion about the data.
- ❌ **D** — Code block, row counts, column names and a statement of what was computed are the evidence.

**Yaad rakho:** Tarika bayan karna ≠ tarika chalana. Code, rows, columns dikhao: wahi saboot hai.

*Grounded in: Code You Never Write §4 (make the AI's hands move; the tell: no code block, no row counts = an opinion about your data) and §6*

---

### Q65.
An FDE writes three statements for a tutoring agent's specification for 3,000 students. S1: "Never give the answer before the student has attempted the problem." S2: "Review the student's working first for correctness, then for method, and last for presentation." S3: "Produce a one-page feedback note with the mark, two strengths and one improvement, in plain language." S4: "When a student is frustrated, acknowledge it before continuing." She classifies them as product description (what you want), process description (how the work is approached), or performance description (how the assistant behaves, for people who are not you). She knows performance description must persist across all sessions, and that at chat scale it is a working-style preference but at system scale a deployed agent's behavior. Four classifications of S1 to S4 are offered.

**Which classification is correct?**

- A. S1 performance; S2 product; S3 process; S4 performance.
- B. S1 performance; S2 process; S3 performance; S4 product.
- C. S1 performance; S2 process; S3 product; S4 performance.
- D. S1 process; S2 process; S3 product; S4 performance.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** FDE 3,000 students ke tutoring agent ki specification ke statements likhti. S1: "Student ke koshish se pehle kabhi jawab mat do." S2: "Working pehle correctness, phir method, aakhir presentation ke liye review karo." S3: "Mark, do strengths, ek improvement ke saath plain language mein one-page feedback note banao." S4: "Student frustrated ho to aage badhne se pehle usay acknowledge karo." Classification: product (kya chahiye), process (kaam kaise approach), performance (AI un logon ke liye kaise behave kare jo tum nahi). Performance har session mein persist karni; chat scale par working-style preference, system scale par deployed agent ka behaviour. Chaar classifications.

**Sawal:** S1–S4 ki kaunsi classification sahi hai?

**Options ka matlab:**

- **A** — S1 performance; S2 product; S3 process; S4 performance.
- **B** — S1 performance; S2 process; S3 performance; S4 product.
- **C** — S1 performance; S2 process; S3 product; S4 performance.
- **D** — S1 process; S2 process; S3 product; S4 performance.

</details>

**Answer:** C

- ✅ **C** — How the agent behaves toward students is performance; the order of work is process; the output's content and format is product.
- ❌ **A** — The order of checks is process, and the note's content and format is product.
- ❌ **B** — The note's content and length is product; acknowledging frustration is behavior toward the user.
- ❌ **D** — A rule about how the agent behaves toward students, whatever the task, is performance description.

**Yaad rakho:** Kya banana = product; kis tarteeb = process; users ke saath behavior = performance (system prompt mein).

*Grounded in: AI Fluency §4 (Description: product, process and performance; performance description at system scale; system prompt makes it permanent)*

---

### Q66.
A consultant has spent a day in one chat working across four clients. By late afternoon the assistant contradicts a revenue figure it gave in the morning, ignores her rule "no bullet points" that it obeyed at first, and gives generic advice. She proposes typing her rules again in capitals, moving to a model with a larger context window, or deleting the first hour of messages. A colleague says the chat has simply gone stale and that abandoning it altogether would lose the day's decisions. Facts: the chat contains about 60 turns; she pastes a fresh 12-page draft each hour; she pastes the same "client background" paragraph at the start of each new client. She wants the response that follows the guidance and also settles the recurring paste problem.

**Which response follows the guidance?**

- A. Move to a model with a larger context window and continue in the same conversation, since a bigger window removes the recall problem for a day's worth of drafts.
- B. Repeat the rules in capitals and delete the first hour of messages to free space, since emphasis restores a rule's weight and deletion removes the material that is crowding it.
- C. Ask for a state summary, correct it, paste it into a fresh chat with files reattached; and, since she repeats the background, move it into a project per client.
- D. Ask the assistant to keep a running memory note of all decisions inside the same chat and to re-read it before each answer, since that preserves continuity without a restart.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Consultant ne ek din ek chat mein chaar clients par kaam kiya. Shaam tak AI subah ki revenue figure contradict karta, "no bullet points" rule ignore karta, generic advice deta. Wo rules capitals mein, bara context window, ya pehle ghante ke messages delete karna soch rahi. Colleague: chat stale, chhodne se din ke faisle kho jayenge. Facts: chat mein ~60 turns; har ghante naya 12-page draft paste; har naye client ke shuru mein same "client background" paragraph paste. Wo aisa response chahti jo guidance follow kare aur baar baar paste wala masla bhi hal kare.

**Sawal:** Kaunsa response guidance follow karta hai?

**Options ka matlab:**

- **A** — Bare context window wala model, same conversation — din bhar ke drafts ka recall masla khatam.
- **B** — Rules capitals mein aur pehle ghante ke messages delete — emphasis wazan lautata, deletion jagah banata.
- **C** — State summary maango, theek karo, files dobara attach karke fresh chat mein paste karo; aur kyunke background baar baar paste hota, usay har client ke project mein le jao.
- **D** — AI se same chat mein saare faislon ka running memory note rakhwao aur har jawab se pehle dobara parhwao.

</details>

**Answer:** C

- ✅ **C** — A fresh chat is an empty window; repetition is the signal for a project.
- ❌ **A** — A bigger window still shares space and still dilutes early instructions.
- ❌ **B** — Pushing on in a crowded window does not fix dilution, and deleting messages deletes decisions.
- ❌ **D** — The note would live in the same overgrown window and would be read by the same diluted context.

**Yaad rakho:** Chat basi ho gayi: state summary, nayi chat, aur roz ka background project mein.

*Grounded in: AI Prompting 2026 §4 (context rot; a new conversation when the topic changes; projects for repeated context); Quick Reference §3 (state summary) and §4*

---

## Domain 3 — Product and Model Selection (12% — 12 questions)

### Q67.
A telecom's support-operations manager assigns four jobs on Claude and knows the ladder from the small, fast model through the mid-tier to the top tier, with thinking a separate switch. Job 1: relabel 9,000 short tickets into six fixed categories (high volume, low depth). Job 2: everyday drafting and summarising of internal updates. Job 3: analyse a 140-page network-sharing agreement whose clauses cross-reference each other, holding the whole structure coherent at once. Job 4: answer a one-line lookup, "what does clause 9 say about liability?", from a pasted paragraph. Her deputy says "the most capable model for everything, to be safe", and a colleague says thinking is a model and belongs on Job 3. She has four allocations of the four jobs in order, each stating tier and thinking.

**Which allocation follows the selection logic?**

- A. Job 1 small tier, no thinking; Job 2 mid-tier default, no thinking; Job 3 top tier with thinking considered; Job 4 small or default tier, no thinking.
- B. Job 1 mid tier, no thinking; Job 2 small tier, no thinking; Job 3 top tier with thinking; Job 4 top tier with thinking.
- C. Job 1 top tier, no thinking; Job 2 mid-tier with thinking; Job 3 small tier with thinking; Job 4 mid-tier, no thinking.
- D. Job 1 small tier, no thinking; Job 2 top tier, no thinking; Job 3 mid-tier with thinking; Job 4 small tier, thinking on.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Telecom support-ops manager chaar jobs assign karti; ladder: small fast → mid-tier → top tier, thinking alag switch. Job 1: 9,000 chhote tickets 6 fixed categories mein relabel (high volume, low depth). Job 2: roz ka internal updates drafting/summarising. Job 3: 140-page network-sharing agreement jiski clauses ek doosre ko cross-reference karti, poora structure coherent rakhna. Job 4: paste kiye paragraph se ek-line lookup "clause 9 liability par kya kehta?". Deputy: "safe rehne ke liye sab par sab se capable model"; colleague: thinking ek model hai, Job 3 par. Chaar allocations (tier + thinking).

**Sawal:** Kaunsi allocation selection logic follow karti hai?

**Options ka matlab:**

- **A** — Job 1 small, no thinking; Job 2 mid-tier default, no thinking; Job 3 top tier, thinking par ghaur; Job 4 small ya default, no thinking.
- **B** — Job 1 mid; Job 2 small; Job 3 top + thinking; Job 4 top + thinking.
- **C** — Job 1 top; Job 2 mid + thinking; Job 3 small + thinking; Job 4 mid.
- **D** — Job 1 small; Job 2 top; Job 3 mid + thinking; Job 4 small, thinking on.

</details>

**Answer:** A

- ✅ **A** — Drop down for bulk and lookups, default to the middle, escalate up for depth; thinking is a switch used for hard multi-variable work.
- ❌ **B** — Bulk relabelling is the small tier's job, and a quick lookup does not merit the top tier or thinking.
- ❌ **C** — It inverts the ladder; thinking cannot make a bulk-tier model hold a large cross-referenced structure coherent.
- ❌ **D** — Routine drafting does not need the top tier, and the depth job is the one that does; thinking on a lookup wastes tokens.

**Yaad rakho:** Bulk/lookup = chhota, roz ka = beech wala, gehra = top + thinking par ghor. Thinking ka matlab hamesha behtar nahi.

*Grounded in: Quick Reference §2 and What AI Actually Is A.3-A.4 (the ladder: default to the middle, escalate for depth, drop down for bulk; thinking is a separate switch and costs extra tokens)*

---

### Q68.
A policy consultant keeps one chat open for a report. Each turn adds about 800 tokens (her message plus the reply). Because the model is stateless, the app re-sends the entire transcript with every turn, so the input for turn n is about 800 x n tokens. She is on turn 40, and her usage allowance is nearly exhausted. Her manager's alternative: at turn 20 write a 600-token summary of decisions and rules, start a fresh chat with it, and continue for the next 20 turns, where the input for turn m of the new chat is 600 + 800 x m tokens. She wants the total input tokens for 40 turns under each approach, to make the case in terms of how the model works. Useful sums: 1+2+...+20 = 210 and 1+2+...+40 = 820.

**Which statement about the totals and the reason is correct?**

- A. Stretching costs about 656,000 input tokens and restarting costs about 656,000 plus 600, because a summary adds tokens without removing any earlier transcript from the window.
- B. Stretching costs about 328,000 input tokens and restarting about 174,000, since only half of the transcript is re-read on each turn once the model has a larger window.
- C. Stretching costs about 32,000 input tokens, since each turn adds only 800 tokens, and restarting costs the same plus the summary, because the model remembers earlier turns without re-reading them.
- D. Stretching costs about 656,000 input tokens across 40 turns and restarting at turn 20 about 348,000 (168,000 plus 180,000), because each turn re-reads the whole transcript.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Policy consultant report ke liye ek chat khuli rakhti. Har turn ~800 tokens jodta (message + reply). Model stateless hai, to app har turn par poora transcript dobara bhejti — turn n ka input ~800 × n tokens. Wo turn 40 par, usage allowance taqreeban khatam. Manager ka alternative: turn 20 par decisions aur rules ka 600-token summary likh kar fresh chat shuru, agle 20 turns jaari — naye chat ke turn m ka input 600 + 800 × m. Dono tareeqon mein 40 turns ke total input tokens chahiye. Useful sums: 1+...+20 = 210, 1+...+40 = 820.

**Sawal:** Totals aur wajah ke baare mein kaunsa bayan sahi hai? (Hisaab khud lagao.)

**Options ka matlab:**

- **A** — Stretching ~656,000 input tokens, restarting ~656,000 + 600 — summary tokens jodta, purana transcript window se nahi hataata.
- **B** — Stretching ~328,000, restarting ~174,000 — bare window ke baad har turn sirf aadha transcript dobara parha jaata.
- **C** — Stretching ~32,000 — har turn sirf 800 jodta; restarting same + summary — model purane turns bina dobara parhe yaad rakhta.
- **D** — 40 turns stretching ~656,000 input tokens, aur turn 20 par restart ~348,000 (168,000 + 180,000) — kyunke har turn poora transcript dobara parhta.

</details>

**Answer:** D

- ✅ **D** — 800 x 820 = 656,000; 800 x 210 = 168,000 and 20 x 600 + 800 x 210 = 180,000; the transcript is replayed every turn.
- ❌ **A** — A fresh chat starts from the summary alone; the earlier transcript is no longer re-sent.
- ❌ **B** — A larger window buys room, not a discount; the whole transcript is still re-read each turn.
- ❌ **C** — The model is stateless; the whole transcript is re-sent each turn, so cost grows with length.

**Yaad rakho:** Har turn poori transcript dobara: 800xn ka jod. 40 turn = 656,000; restart = 348,000.

*Grounded in: What AI Actually Is Ideas 2 and 5 (stateless; transcript replayed every turn; long chats cost more and dilute) and Quick Reference §3; Workflow Design §3 (compute, don't guess)*

---

### Q69.
A consulting firm wants a reusable method for board papers. The knowledge partner makes five statements about the four features (Skill, Project, custom GPT, plugin) and Team-plan sharing. S1: "A Project stores the knowledge for a stream of work; a Skill stores the method for doing a task." S2: "A custom GPT is a separately configured assistant that you open on purpose, and it lives only inside ChatGPT." S3: "A plugin bundles skills with connections to outside apps." S4: "On a Team plan, a shared Skill is view-only for colleagues and updates itself when you change the original; an owner must first enable sharing." S5: "A Skill written for one product cannot be installed in another vendor's tool, because Skills are proprietary to the vendor that shipped them." A trainee is asked to identify the one statement that is wrong.

**Which statement is wrong?**

- A. S3: a plugin packages skills together with connections to outside apps, and sometimes commands and sub-agents, into an installable package for a job function.
- B. S4: on a Team plan, sharing is off by default and needs an owner, and shared Skills are view-only copies that follow changes to the original.
- C. S5: a basic SKILL.md follows an open standard that several vendors' tools read, so a Skill can be installed elsewhere, although each product's install path and permissions need checking.
- D. S1: a Project stores knowledge for a stream of work, while a Skill stores the method for a task, and a Skill can use the customer files a Project holds.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Consulting firm board papers ka reusable method chahti. Knowledge partner chaar features (Skill, Project, custom GPT, plugin) aur Team-plan sharing par paanch bayan deta. S1: "Project kaam ki stream ki knowledge rakhta; Skill task karne ka method." S2: "Custom GPT alag configured assistant jo jaan-bujh kar kholte, sirf ChatGPT ke andar rehta." S3: "Plugin skills ko bahar ki apps ke connections ke saath bundle karta." S4: "Team plan par shared Skill colleagues ke liye view-only aur original badalne par khud update; pehle owner sharing enable kare." S5: "Ek product ke liye likha Skill doosre vendor ke tool mein install nahi ho sakta, Skills vendor ke proprietary hain." Trainee ko ek ghalat bayan pehchaanna.

**Sawal:** Kaunsa bayan ghalat hai? (Har option ek bayan ko uski sahi haalat ke saath dohrata hai — jo bayan asal mein ghalat hai us wala option chuno.)

**Options ka matlab:**

- **A** — S3 — plugin skills ko bahar ki apps ke connections (aur kabhi commands, sub-agents) ke saath job function ke installable package mein bandhta.
- **B** — S4 — Team plan par sharing default off aur owner chahiye, shared Skills view-only copies jo original ke saath chalti.
- **C** — S5 — basic SKILL.md open standard follow karti jo kai vendors ke tools parhte, to Skill doosri jagah install ho sakta, magar har product ka install path aur permissions check karne honge.
- **D** — S1 — Project stream ki knowledge, Skill task ka method, aur Skill Project ki customer files use kar sakta.

</details>

**Answer:** C

- ✅ **C** — Skills are not vendor-locked, unlike custom GPTs and Gems.
- ❌ **A** — Correct description of a plugin.
- ❌ **B** — Correct: shared skills update themselves and sharing is enabled by an owner.
- ❌ **D** — Correct: projects store knowledge, skills perform tasks.

**Yaad rakho:** Skill open standard hai, kai vendors ke tools parhte hain; custom GPT ek vendor mein qaid.

*Grounded in: Quick Reference §7 (Project vs Skill vs custom GPT vs plugin; Agent Skills open standard); Skills & Connectors §14 and Part 4*

---

### Q70.
An operations lead wants an assistant to pull daily card-dispute counts from her bank's CRM. A supported connector exists but needs an administrator to enable it, which takes a week. She lists five statements from her research and asks which one is FALSE. S1: "MCP is the shared plug shape, so a connector built once can work with many assistants, but connecting one is still a permission decision." S2: "A connector inherits your own permissions, so it reaches only what your account can reach." S3: "You can start a new connector read-only and keep its scope to one folder, then add write access only after it has behaved well." S4: "A connector can only perform the actions it was built to offer, so permissions choose among the tool's actions and do not add new ones." S5: "Because a connector runs on a standard, its access is the same for every tool, so no decision is needed about what it may read or do."

**Which statement is false?**

- A. S4: permissions choose among the actions a tool has; they do not add new ones, so a connector built only to save files cannot send email however broad the access.
- B. S2: a connector inherits your own permissions, so if your account cannot open a folder the connector cannot either, and connecting a drive does not hand over the whole company's files.
- C. S5: the plug is standard, but the access is not; what a connector may read and do is a decision about trust, permissions and scope for each connection.
- D. S3: starting read-only and keeping a small scope, with write access granted only after the tool has behaved, is the recommended way to widen access.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Ops lead chahti AI bank ke CRM se daily card-dispute counts nikaale; supported connector ko admin enable kare, ek hafta. Research ke paanch bayan — kaunsa FALSE? S1: "MCP shared plug shape hai, ek dafa bana connector kai assistants ke saath chal sakta, magar connect karna phir bhi permission decision hai." S2: "Connector tumhari apni permissions inherit karta, sirf wahan pahunchta jahan tumhara account." S3: "Naya connector read-only shuru karke ek folder tak scope rakh sakte, achha behave kare to write access do." S4: "Connector sirf wahi actions kar sakta jo usmein bane hain; permissions tool ke actions mein se chunti hain, naye nahi jodti." S5: "Connector standard par chalta hai, to access har tool ka same, kya parhe ya kare uska koi faisla nahi chahiye."

**Sawal:** Kaunsa bayan false hai? (Har option ek bayan ko uske sahi matlab ke saath samjhata hai — jo bayan false tha wo chuno.)

**Options ka matlab:**

- **A** — S4 — permissions tool ke actions mein se chunti hain, naye nahi jodti; sirf files save karne wala connector email nahi bhej sakta chahe access kitna bhi broad.
- **B** — S2 — connector tumhari permissions inherit karta; jo folder tum nahi khol sakte connector bhi nahi, drive jodne se poori company ki files nahi milti.
- **C** — S5 — plug standard hai magar access nahi; connector kya parhe aur kare yeh har connection ke liye trust, permissions aur scope ka faisla hai.
- **D** — S3 — read-only aur chhote scope se shuru, behave karne ke baad hi write access — recommended tareeqa.

</details>

**Answer:** C

- ✅ **C** — Plugging in a cable is not a decision about trust; connecting an MCP tool is.
- ❌ **A** — This is true: the action set is the shape of the tool.
- ❌ **B** — This is true: AI inherits the permissions you already have.
- ❌ **D** — This is true for connectors, which have scopes.

**Yaad rakho:** Plug standard hai, access nahi. Connector tumhari permissions le kar chalta hai aur sirf apne actions kar sakta hai.

*Grounded in: Quick Reference §8 (connections are permission decisions; the plug is standard, the access is not; permissions choose among a tool's actions); Skills & Connectors §3 and Part 5*

---

### Q71.
A shared-services team has three workflows and three execution patterns: cloud-only (the vendor's cloud runs the loop and uses cloud tools), cloud plus desktop bridge (the cloud runs the loop but borrows a local folder or browser through the desktop app), and a local session (the loop and tools run on the user's machine). W1: a weekly digest built from a cloud drive and email, which must run while the team is on leave. W2: a monthly reconciliation that needs one approved local folder of scanned cheques, run while the user is at her desk. W3: a workflow on sensitive local files whose custody must stay on the user's own machine. A colleague says a bridge lets a cloud session "keep everything local". The team lists four assignments of W1 to W3 in order.

**Which assignment is correct?**

- A. W1 cloud-only; W2 cloud plus desktop bridge; W3 local session.
- B. W1 cloud plus desktop bridge; W2 cloud-only; W3 local session.
- C. W1 local session; W2 cloud plus desktop bridge; W3 cloud-only.
- D. W1 cloud-only; W2 local session; W3 cloud plus desktop bridge.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Shared-services team ke teen workflows aur teen execution patterns: cloud-only (vendor ka cloud loop chalata aur cloud tools use karta), cloud + desktop bridge (cloud loop chalata magar desktop app se local folder ya browser udhaar leta), aur local session (loop aur tools user ki machine par). W1: cloud drive aur email se weekly digest jo team ki chhutti mein bhi chale. W2: monthly reconciliation jise scanned cheques ka ek approved local folder chahiye, user desk par ho tab chalta. W3: sensitive local files wala workflow jiski custody user ki apni machine par hi rehni chahiye. Colleague: bridge cloud session ko "sab local rakhne" deta. Chaar assignments.

**Sawal:** W1–W3 ki kaunsi assignment sahi hai?

**Options ka matlab:**

- **A** — W1 cloud-only; W2 cloud + desktop bridge; W3 local session.
- **B** — W1 cloud + bridge; W2 cloud-only; W3 local session.
- **C** — W1 local session; W2 cloud + bridge; W3 cloud-only.
- **D** — W1 cloud-only; W2 local session; W3 cloud + bridge.

</details>

**Answer:** A

- ✅ **A** — A cloud-reachable, unattended job is cloud-only; borrowing one local folder while online is the bridge; local custody needs a local session, because a bridge still processes data in the cloud.
- ❌ **B** — The digest is entirely cloud-reachable, so it does not need a bridge, and the local folder cannot be reached by a cloud-only run.
- ❌ **C** — An unattended job that must run on leave cannot depend on a workstation, and local custody cannot be cloud-only.
- ❌ **D** — A bridge is not a custody loophole: the cloud still processes the data, so W3 needs a local session.

**Yaad rakho:** Unattended cloud tools = cloud-only; ek local folder online rehte huay = bridge; local custody = local session.

*Grounded in: General Agents on the Web §2 and §10 (cloud-only, cloud plus bridge, local; a bridge is a convenience, not a custody loophole; ask where the loop runs and where each tool executes)*

---

### Q72.
A shared-services team has three workflows and the three approval modes of a desktop coworking product: Manual (pauses for actions that need approval), Auto (keeps moving and screens each action for safety, at extra usage), and Skip (no ordinary approvals and no Auto check). Workflow A: brand new, on an unfamiliar vendor portal, and includes an irreversible form submission. Workflow B: proven over many weeks, bounded to one report folder, where wrong output is easily corrected and interruptions are costly. Workflow C: an experimental clean-up of a large shared folder by a person new to agents; deleted files may skip the recycle bin and edits may leave no history. The team lead adds that Manual does not automatically produce a plan. Four assignments of A, B, C in order are listed.

**Which assignment is correct?**

- A. A Skip; B Auto; C Auto.
- B. A Auto; B Skip; C Manual.
- C. A Manual; B Auto; C Manual.
- D. A Manual; B Manual; C Skip.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Shared-services team ke teen workflows aur desktop coworking product ke teen approval modes: Manual (approval wale actions par rukta), Auto (chalta rehta aur har action safety ke liye screen karta, extra usage), Skip (na ordinary approvals na Auto check). A: bilkul naya, anjaan vendor portal, irreversible form submission. B: hafton se proven, ek report folder tak bounded, ghalat output aasani se theek, interruptions mehngi. C: bare shared folder ka experimental clean-up, agents mein naya banda; deleted files recycle bin skip kar sakti, edits ki history na rahe. Lead: Manual khud plan nahi banata. Chaar assignments.

**Sawal:** A, B, C ki kaunsi assignment sahi hai?

**Options ka matlab:**

- **A** — A Skip; B Auto; C Auto.
- **B** — A Auto; B Skip; C Manual.
- **C** — A Manual; B Auto; C Manual.
- **D** — A Manual; B Manual; C Skip.

</details>

**Answer:** C

- ✅ **C** — New, unfamiliar and hard-to-reverse work, and a newcomer's first sessions, need the strictest gate; a proven, bounded job earns Auto.
- ❌ **A** — Skip removes every approval on the unfamiliar irreversible workflow, and Auto screens but does not replace a beginner's approvals.
- ❌ **B** — An irreversible action on an unfamiliar site deserves Manual; Skip is rarely right.
- ❌ **D** — Skip for a newcomer over a large shared folder, where deletions may skip recovery, is the riskiest choice.

**Yaad rakho:** Naya/anjaan/undo-na-hone-wala/newcomer = Manual. Sabit aur mehdood = Auto. Skip lagbhag kabhi nahi.

*Grounded in: General Agents on the Web §7-8 (Manual, Auto, Skip; match the gate to blast radius; Manual does not create a plan) and AI Prompting 2026 §11*

---

### Q73.
A finance analyst needs an agent to reach four things. T1: figures in a CRM that has a supported connector. T2: a supplier's web portal with no connector. T3: the expenses page she already has open in her own signed-in Chrome. T4: an old desktop app with no connector and no browser interface. Four reach paths exist: a connector, the vendor's built-in browser (its own browser for delegated work), the Chrome extension working in her existing signed-in context, and computer use (the agent operates the screen directly). The security team says to use the most structured tool that can do the job and the smallest scope, and that a signed-in session inherits everything that session can reach. She has four assignments of T1 to T4 in order.

**Which assignment is correct?**

- A. T1 connector; T2 computer use; T3 built-in browser; T4 Chrome extension.
- B. T1 connector; T2 built-in browser; T3 Chrome extension; T4 computer use.
- C. T1 Chrome extension; T2 connector; T3 built-in browser; T4 computer use.
- D. T1 built-in browser; T2 built-in browser; T3 connector; T4 Chrome extension.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Finance analyst ko agent se chaar cheezon tak pahunchna. T1: CRM ke figures jiska supported connector hai. T2: supplier ka web portal, connector nahi. T3: expenses page jo uske apne signed-in Chrome mein khula hai. T4: purani desktop app, na connector na browser interface. Chaar reach paths: connector, vendor ka built-in browser (delegated kaam ke liye apna browser), Chrome extension (uske existing signed-in context mein), aur computer use (agent screen khud chalata). Security: kaam kar sakne wala sab se structured tool aur sab se chhota scope; signed-in session us session ki har pahunch inherit karta. Chaar assignments.

**Sawal:** T1–T4 ki kaunsi assignment sahi hai?

**Options ka matlab:**

- **A** — T1 connector; T2 computer use; T3 built-in browser; T4 Chrome extension.
- **B** — T1 connector; T2 built-in browser; T3 Chrome extension; T4 computer use.
- **C** — T1 Chrome extension; T2 connector; T3 built-in browser; T4 computer use.
- **D** — T1 built-in browser; T2 built-in browser; T3 connector; T4 Chrome extension.

</details>

**Answer:** B

- ✅ **B** — Connector before browser, browser before computer use; each path for the work it touches.
- ❌ **A** — Computer use is the highest-risk path and is not needed for a browsable portal; the old desktop app cannot use a browser extension.
- ❌ **C** — A connector exists for the CRM, and a portal with no connector cannot use one.
- ❌ **D** — A supported connector exists for the CRM, and no connector exists for her open Chrome page.

**Yaad rakho:** Connector, phir browser, phir computer use; Chrome extension tumhari signed-in session ka poora asar le aata hai.

*Grounded in: General Agents on the Web §6 (reach paths; use the most structured tool; smallest scope; signed-in Chrome inherits the sensitivity of the session)*

---

### Q74.
A clinic group's manager wants a coworking agent in the vendor's cloud, with a desktop bridge, to read a folder of patient discharge summaries and draft follow-up letters. She makes five statements. S1: "We are on an Enterprise plan, so it is approved for health data." S2: "The bridge only reads the files, so they stay on the clinic's computers." S3: "Manual mode makes it safe." S4: "A competitor clinic uses the same setup." S5: "The letters need patient names attached to diagnoses, so redaction is not an option." The clinic's compliance officer has not been asked, and no business associate agreement has been discussed. A compliance associate says exactly one of S1 to S5 is correct as stated, and asks which.

**Which statement is correct as stated?**

- A. S3: Manual mode makes the workflow safe, since a person approves each action and therefore approves each use of the patient data.
- B. S5: the letters need names attached to diagnoses, so redaction would break the task; confirm the route and agreement before uploading.
- C. S1: an Enterprise plan is approved for health data, since organisation plans include admin controls, retention and audit that regulated clients require.
- D. S2: the bridge only reads the files, so they stay on the clinic's computers and nothing is processed in the vendor's cloud.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Clinic group ki manager vendor ke cloud mein coworking agent + desktop bridge chahti jo patient discharge summaries parh kar follow-up letters draft kare. Paanch bayan: S1 "Enterprise plan hai, health data ke liye approved." S2 "Bridge sirf parhta, files clinic ke computers par rehti." S3 "Manual mode isay safe banata." S4 "Competitor clinic same setup use karti." S5 "Letters mein diagnoses ke saath patient names chahiye, to redaction option nahi." Compliance officer se poocha nahi, business associate agreement ki baat nahi. Compliance associate: S1–S5 mein se theek ek jaisa likha hai waisa sahi hai.

**Sawal:** Kaunsa bayan jaisa likha hai waisa sahi hai?

**Options ka matlab:**

- **A** — S3 — Manual mode safe banata, insaan har action aur patient data ka har use approve karta.
- **B** — S5 — letters ko diagnoses ke saath naam chahiye, to redaction task tod degi; upload se pehle route aur agreement confirm karo.
- **C** — S1 — Enterprise plan health data ke liye approved, organisation plans mein admin controls, retention, audit.
- **D** — S2 — bridge sirf parhta, files clinic ke computers par, vendor cloud mein kuch process nahi hota.

</details>

**Answer:** B

- ✅ **B** — When the specifics are the substance, redaction is unavailable and the route question comes first.
- ❌ **A** — Approval modes do not substitute for the compliance answer or the contract.
- ❌ **C** — Availability is not permission; an enterprise plan is not blanket approval for a data class.
- ❌ **D** — A cloud session reading a local file through a bridge still processes it in the cloud.

**Yaad rakho:** Naam zaroori hon to redaction nahi chalti; pehle route/contract, plan ka naam ijazat nahi, bridge cloud ki processing nahi rokta.

*Grounded in: General Agents on the Web §10 (regulated work: stop and verify; a bridge is not a custody loophole; availability is not permission; HIPAA, PHI, BAA) and Governance §2.2-2.4*

---

### Q75. *(Select TWO — all-or-nothing)*
A packaging firm's inventory analyst uploads a shelf photo and asks an assistant to read 22 batch codes of 14 characters each and to count how often the letter Z appears across the codes. The codes come back confidently; a spot check finds four misread characters, and the Z count is off by three. Five statements from a discussion. S1: "Pictures are cut into patches that become tokens, so small print is a chunk-reading problem like counting letters inside words." S2: "The top tier with thinking on will read fine detail exactly." S3: "Exact character-level work is unnatural for the model; the count should be computed by code and checked." S4: "The confident tone shows which codes are right." S5: "Ability is jagged, so a strong result on hard tasks does not predict small-print reading." The team lead asks which TWO are the most accurate.

**Which TWO statements are correct?**

- A. S5 is correct: ability is jagged, so strength on hard analysis says nothing about reading small print, which is why easy-looking tasks need verifying across the boundary.
- B. S2 is correct: the top tier with thinking on reads fine detail exactly, since more reasoning removes misreads of characters in images.
- C. S3 is correct: exact character-level work is unnatural for a token-based model, so the count should be computed by code and checked against the physical labels.
- D. S4 is correct: the assistant's confident tone is a useful signal of which codes are right, so only low-confidence codes need checking.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Packaging firm ki inventory analyst shelf photo upload karke AI se 22 batch codes (har ek 14 characters) parhwati aur codes mein letter Z kitni dafa aaya gintwati. Codes confident, spot check mein chaar misread characters, Z count teen se ghalat. Discussion ke paanch bayan: S1 "Tasveeren patches mein kat kar tokens banti, to chhota print chunk-reading masla hai jaise lafzon ke andar letters ginna." S2 "Top tier + thinking fine detail exact parhega." S3 "Exact character-level kaam model ke liye ghair-fitri; count code se compute aur check ho." S4 "Confident tone batata kaunse codes sahi." S5 "Ability jagged hai, mushkil kaam mein achha result chhota print parhne ka andaaza nahi deta." Lead: sab se accurate do kaunse?

**Sawal:** Kaunse DO bayan sahi hain?

**Options ka matlab:**

- **A** — S5 — ability jagged hai, mushkil analysis mein taaqat chhote print ke baare mein kuch nahi batati, is liye aasaan-dikhne wale kaam bhi boundary ke paar verify hone chahiye.
- **B** — S2 — top tier + thinking fine detail exact parhta, zyada reasoning misreads hata deti.
- **C** — S3 — exact character-level kaam token-based model ke liye ghair-fitri, count code se compute karke physical labels se check karo.
- **D** — S4 — confident tone kaam ka signal, sirf low-confidence codes check.

</details>

**Answer:** A, C

- ✅ **A** — The dangerous errors are easy-looking tasks failed without warning.
- ✅ **C** — Patches and tokens are chunks, so small print is the strawberry problem again; computed counts are tested against a known answer.
- ❌ **B** — Thinking is more prediction; it can narrow but not close the gap.
- ❌ **D** — Confidence is a learned style with no link to correctness; the four errors were confident.

**Yaad rakho:** Image ka patch = chunk: chhoti likhayi aur letter gintee kamzor. Code se ginwao, label se check.

*Grounded in: What AI Actually Is Ideas 4, 6, 7 and 9 (tokens; images are patches; confidence is a style; jagged frontier; thinking is not a truth-checker); Code You Never Write §6*

---

### Q76. *(Select TWO — all-or-nothing)*
A consultancy's team lead has used the top tier for all client-facing work and the smallest for everything else, on the rule "client-facing means top". Her allowance runs out by mid-month. Her trainer says the exam objective is to align model selection with task requirements (cost, speed, quality), not to memorise names. Two client-facing tasks: reformatting agreed findings into a client template; and synthesising four conflicting regulatory sources into one recommendation. Two internal tasks: a one-line internal lookup; and a hard multi-step reconciliation of three ledgers. Under the rule, the first two go top and the last two go small. The trainer says the rule gets exactly two of the four tasks wrong.

**Which TWO tasks does the audience-based rule assign to the wrong tier?**

- A. The four-source regulatory synthesis: it is client-facing and complex, so the top tier is right, but the rule is wrong to assign it there because the top tier is only for internal tasks.
- B. The three-ledger reconciliation: it is internal but hard and multi-step, so it merits a deeper tier and possibly thinking, which the small tier would not give.
- C. The one-line internal lookup: it is internal and simple, so the small tier is right, but the rule is wrong to send it there since every lookup needs the mid-tier default.
- D. The template reformat: it is client-facing but simple, so it does not need the top tier; the task's complexity, not its audience, decides.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Consultancy ki team lead "client-facing matlab top" rule par saara client-facing kaam top tier aur baaqi sab sab se chhote tier par karti; allowance mahine ke beech khatam. Trainer: exam objective model selection ko task requirements (cost, speed, quality) se align karna hai, naam yaad karna nahi. Do client-facing tasks: agreed findings ko client template mein reformat; chaar takrate regulatory sources ko ek recommendation mein synthesise. Do internal tasks: ek-line internal lookup; teen ledgers ki mushkil multi-step reconciliation. Rule ke tehat pehle do top, aakhri do small. Trainer: rule chaar mein se theek do ko ghalat tier deta.

**Sawal:** Audience-based rule kin DO tasks ko ghalat tier deta hai?

**Options ka matlab:**

- **A** — Four-source synthesis — client-facing aur complex, top sahi, magar rule ghalat kyunke top sirf internal ke liye.
- **B** — Three-ledger reconciliation — internal magar mushkil aur multi-step, gehre tier aur shayad thinking ka haqdaar, jo small tier nahi deta.
- **C** — One-line lookup — internal aur simple, small sahi, magar rule ghalat kyunke har lookup ko mid-tier default chahiye.
- **D** — Template reformat — client-facing magar simple, top tier nahi chahiye; task ki complexity faisla karti, audience nahi.

</details>

**Answer:** B, D

- ✅ **B** — A genuinely multi-constraint task benefits from depth whatever the audience.
- ✅ **D** — 'Client-facing' describes who receives the output, not how hard the task is.
- ❌ **A** — The synthesis is a depth task and the top tier suits it; the rule gets it right.
- ❌ **C** — A quick lookup belongs on the small, fast tier; the rule gets it right.

**Yaad rakho:** Tier task ki pechidgi se: client-facing seedha kaam small, internal mushkil kaam top.

*Grounded in: What AI Actually Is A.3 (the ladder; select by task, not by audience) and Quick Reference §2 (choose the model by the task, not by habit)*

---

### Q77. *(Select TWO — all-or-nothing)*
Two associates compare two assistants on a real task from their week: drafting a two-page risk summary from a client file. They run the same request in both and then, as the course suggests, ask each assistant to state in three sentences what extra context would have helped it. Results: Assistant P's output is slightly longer and better formatted; Assistant Q's list of missing context is sharper. One associate proposes to "declare a winner and standardise on it". The other says the exercise is a record of two runs on one day, models change fast, and the missing-context lists teach more than the outputs. Five conclusions are offered, and the trainer says exactly two follow the course.

**Which TWO conclusions follow the course?**

- A. Standardise on Assistant P, since the longer and better-formatted output shows it is more capable on the firm's own real work.
- B. Use the missing-context lists to improve the brief: what each lacked is context you probably left out or re-typed.
- C. Standardise on Assistant Q, since an assistant that can say precisely what it lacks is the more trustworthy of the two for client work.
- D. Treat it as platform awareness, not a ranking: record what each did and what each said it lacked, and re-run periodically.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Do associates hafte ke asli task (client file se 2-page risk summary) par do AIs compare karte. Same request dono mein, phir course ke mutabiq har ek se teen jumlon mein poocha kaunsa extra context madad karta. Results: Assistant P ka output thoda lamba aur behtar formatted; Assistant Q ki missing-context list zyada tez. Ek associate: "winner declare karo aur standardise". Doosra: ek din ke do runs ka record, models tezi se badalte, aur missing-context lists outputs se zyada sikhati. Paanch conclusions; trainer: exactly do course follow karte.

**Sawal:** Kaunse DO conclusions course follow karte hain?

**Options ka matlab:**

- **A** — P par standardise — lamba, behtar formatted output firm ke apne kaam par zyada capable dikhata.
- **B** — Missing-context lists se brief behtar karo — jo har ek ko nahi mila wo context shayad tum ne chhoda ya baar baar type kiya.
- **C** — Q par standardise — jo precisely bata sake kya kami hai wo zyada trustworthy.
- **D** — Isay platform awareness samjho, ranking nahi: record karo har ek ne kya kiya aur kya kami batayi, aur waqtan fawaqtan dobara chalao.

</details>

**Answer:** B, D

- ✅ **B** — The second comparison, of what each said it was missing, usually teaches more than the first.
- ✅ **D** — A ranking made today is not true next month.
- ❌ **A** — Length and formatting are not correctness, and one run on one day is not a ranking.
- ❌ **C** — A sharp self-description is not evidence of better work.

**Yaad rakho:** Do assistants ki tulna record hai, ranking nahi: kami ki list se brief behtar karo aur dobara azmao.

*Grounded in: Quick Reference §1 and §9 (platform awareness; run the same task in both; compare what each said it was missing); Just Delegate It §11 (a record, not a ranking)*

---

### Q78.
A strategy director sends four requests and wants each routed. R1: today's PKR-USD rate for a note. R2: a comparison of three pricing strategies from figures she has already attached, where the difficulty is reasoning across trade-offs. R3: a thorough, cited investigation of the current cold-chain logistics market for a board committee. R4: the latest approved pricing policy, which lives in the company's own document systems. Routes: web search (one current fact, seconds), thinking (hard reasoning, no new information), research (multi-source cited investigation, minutes, paid plans), and connected apps or workplace search (information from your organisation). A colleague says research should be used for everything, and another says it must be used for anything that needs a source. Four allocations of R1 to R4 in order are listed.

**Which allocation is correct?**

- A. R1 research; R2 thinking; R3 web search; R4 connected apps or workplace search.
- B. R1 web search; R2 thinking; R3 research; R4 web search.
- C. R1 web search; R2 thinking; R3 research; R4 connected apps or workplace search.
- D. R1 web search; R2 research; R3 thinking; R4 connected apps or workplace search.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Strategy director chaar requests route karna chahti. R1: note ke liye aaj ka PKR-USD rate. R2: attached figures se teen pricing strategies ka comparison, mushkil hissa trade-off reasoning. R3: board committee ke liye current cold-chain logistics market ki thorough, cited investigation. R4: latest approved pricing policy jo company ke apne document systems mein. Routes: web search (ek current fact, seconds), thinking (mushkil reasoning, nai info nahi), research (multi-source cited investigation, minutes, paid plans), connected apps/workplace search (organisation ki info). Ek colleague: sab ke liye research; doosra: jahan source chahiye wahan research lazmi.

**Sawal:** R1–R4 ki kaunsi allocation sahi hai?

**Options ka matlab:**

- **A** — R1 research; R2 thinking; R3 web search; R4 connected apps/workplace search.
- **B** — R1 web search; R2 thinking; R3 research; R4 web search.
- **C** — R1 web search; R2 thinking; R3 research; R4 connected apps/workplace search.
- **D** — R1 web search; R2 research; R3 thinking; R4 connected apps/workplace search.

</details>

**Answer:** C

- ✅ **C** — Route the question before you send it: one fact is a search; reasoning over supplied figures is thinking; a cited investigation is research; internal information needs connected apps.
- ❌ **A** — Deep research on a single exchange rate is the most common waste, and a board investigation needs more than one search.
- ❌ **B** — The approved internal policy lives in the organisation's systems, which the open web does not reach.
- ❌ **D** — R2 is reasoning over supplied figures, and R3 needs many cited sources, not more thinking.

**Yaad rakho:** Ek fact = search; soch = thinking; cited report = research; apna data = connectors/workplace search.

*Grounded in: Quick Reference §8 (search, thinking, or research: route the question before you send it) and What AI Actually Is A.8*

---

## Domain 5 — Configuration and Knowledge Management (12% — 12 questions)

### Q79.
A finance team built a Skill for month-end client summaries. Four symptoms have been reported over a month. S1: on "prepare the March summary for DEMO Trading" it never starts. S2: on "quickly total these three numbers" it starts and produces a four-section report nobody wanted. S3: it starts on the right requests but always leaves out the withholding flags, even in fresh chats and after the author reworded the rule three times. S4: it worked perfectly for months and now flags the wrong payments in fresh chats, though the Skill file has not changed and the tax threshold in its settings block is the old one. The team knows the assistant keeps only the description in view and opens the instructions on a match, that a description can say when not to use the Skill, that an exact step belongs in a small program, and that nothing warns you when a Skill goes stale. Four mappings of S1 to S4 to fixes are offered.

**Which mapping is correct?**

- A. S1: add more rules to the instruction body; S2: rewrite the description; S3: add a negative trigger; S4: restart the chat and paste the threshold again.
- B. S1: rewrite the description; S2: add a negative trigger; S3: update the stale threshold and schedule a review; S4: move the exact flag check into a small program.
- C. S1: add a negative trigger; S2: rewrite the description with exact phrases; S3: update the stale threshold; S4: move the exact flag check into a small program.
- D. S1: rewrite the description; S2: add a negative trigger; S3: move the exact flag check into a small program; S4: update the stale threshold and schedule a review.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Finance team ke month-end client-summary Skill ke mahine bhar mein chaar symptoms. S1: "prepare the March summary for DEMO Trading" par kabhi start nahi hota. S2: "quickly total these three numbers" par start ho kar 4-section report bana deta. S3: sahi requests par start hota magar withholding flags hamesha chhod deta — fresh chats mein bhi, aur author ke teen dafa rule reword karne ke baad bhi. S4: mahino perfect, ab fresh chats mein ghalat payments flag, Skill file nahi badli aur settings block mein tax threshold purana hai. Team jaanti: AI sirf description nazar mein rakhta aur match par instructions kholta; description keh sakti kab use NA karna; exact step chhote program mein belong karta; Skill stale ho to koi warning nahi aati.

**Sawal:** S1–S4 ko fixes se jodne ki kaunsi mapping sahi hai?

**Options ka matlab:**

- **A** — S1: body mein aur rules; S2: description rewrite; S3: negative trigger; S4: chat restart aur threshold dobara paste.
- **B** — S1: description rewrite; S2: negative trigger; S3: stale threshold update + review schedule; S4: exact flag check chhote program mein.
- **C** — S1: negative trigger; S2: exact phrases ke saath description rewrite; S3: stale threshold update; S4: exact flag check program mein.
- **D** — S1: description rewrite; S2: negative trigger; S3: exact flag check chhote program mein; S4: stale threshold update + review schedule.

</details>

**Answer:** D

- ✅ **D** — Each symptom points at a different place: description, negative trigger, wrong-place exact step, and stale configuration.
- ❌ **A** — Relevance is judged from the description, and a stale threshold is not fixed by a restart.
- ❌ **B** — The recurring miss after rewording is a wrong-place step; the one that used to work is stale configuration.
- ❌ **C** — A Skill that never fires needs a sharper description, and one that fires too eagerly needs a negative trigger.

**Yaad rakho:** Nahi chalta = description; zyada chalta = negative trigger; wahi ghalti = exact step code mein; pehle chalta tha = config purani.

*Grounded in: Skills & Connectors §11-13 (the description decides whether it fires; negative trigger; the same mistake every run: step in the wrong place; it used to work: nothing warns you when a skill goes out of date)*

---

### Q80.
A partner at a Karachi law firm on an organisation plan states five things about memory, incognito chats, retention and training use, and the firm's records team must decide which of the five is FALSE before the firm relies on them. S1: "Memory is not retention: chats and memory-related data still follow the applicable retention and export controls." S2: "Incognito chats do not appear in history or memory, but Anthropic documents a 30-day default retention period, with longer custom retention possible on Enterprise." S3: "On Team and Enterprise plans, incognito chats follow organisational retention and appear in standard data exports." S4: "Incognito chats are used for model training on Team plans unless an owner disables training in the admin console." S5: "On Free, Pro and Max, your privacy settings decide whether chats may be used to improve models, and allowing it extends retention of those chats to five years."

**Which statement is false?**

- A. S5: on individual plans the privacy settings govern training use, and allowing training extends retention of those chats to five years.
- B. S2: incognito keeps chats out of history and memory yet leaves a default 30-day retention, with longer custom retention possible on Enterprise.
- C. S3: on Team and Enterprise, incognito chats follow organisational retention and show up in standard exports, because private in the interface is not absent from records.
- D. S4: incognito chats are not used for training on any plan, so an owner has nothing to disable; Team and Enterprise inputs aren't used by default.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Organisation plan wali Karachi law firm ka partner memory, incognito, retention aur training use par paanch baatein kehta; records team ko bharosa karne se pehle ek FALSE pehchaanna. S1: "Memory retention nahi: chats aur memory-related data phir bhi retention aur export controls follow karte." S2: "Incognito chats history ya memory mein nahi aati, magar Anthropic 30-din default retention document karta, Enterprise par lambi custom retention mumkin." S3: "Team aur Enterprise par incognito chats organisational retention follow karti aur standard exports mein aati." S4: "Team plans par incognito chats model training ke liye use hoti jab tak owner admin console mein training band na kare." S5: "Free, Pro, Max par privacy settings tay karti chats models behtar karne mein use hon ya nahi, aur allow karne se un chats ki retention paanch saal ho jaati."

**Sawal:** Kaunsa bayan false hai? (Har option ek bayan ko uski sahi shakal mein bataata hai — jo bayan asal mein false tha wo chuno.)

**Options ka matlab:**

- **A** — S5 — individual plans par privacy settings training use govern karti, aur allow karne se retention paanch saal.
- **B** — S2 — incognito history aur memory se bahar, magar default 30-din retention, Enterprise par lambi custom retention.
- **C** — S3 — Team/Enterprise par incognito organisational retention follow karti aur exports mein aati; interface mein private ka matlab records se gayab nahi.
- **D** — S4 — incognito chats kisi plan par training ke liye use nahi hoti, owner ke band karne ko kuch nahi; Team/Enterprise inputs default mein use nahi hote.

</details>

**Answer:** D

- ✅ **D** — Incognito chats are not used for training on any plan.
- ❌ **A** — This is true for Free, Pro and Max.
- ❌ **B** — This is true: incognito is not zero retention.
- ❌ **C** — This is true.

**Yaad rakho:** Incognito = 30 din retention, exports mein; training kabhi nahi. Memory ≠ retention.

*Grounded in: Governance §2.5-2.6 (memory is not retention; incognito is not zero retention; training use depends on the plan; private in the interface does not mean absent from organisational records)*

---

### Q81.
A legal department's Claude Project holds 300 pages of policies as knowledge and four pages of standing instructions. Users report that the assistant always follows the instruction "never cite a case older than 2015" but sometimes misses rules that are written on page 212 of the knowledge files. An administrator says that instructions are placed in the window every time, that when a project's knowledge outgrows what fits in the window the product searches it and fetches relevant parts, and that a project is a pre-loaded window. The head of legal wants missed rules reliably followed. A colleague proposes moving all 300 pages into the instructions; another proposes telling the assistant to "read all 300 pages before every answer".

**Which statement is INCORRECT about the situation?**

- A. Instructions load every time, which is why the 2015 rule is always followed, while a large knowledge base is retrieved on demand, which is why page 212 is sometimes missed.
- B. Telling the assistant to read all 300 pages before each answer does not change what fits in the window, because retrieval automatically selects relevant parts.
- C. Always-apply rules should be short and placed in the instructions, while reference material stays in knowledge and questions point at the relevant document.
- D. Moving the 300 pages into the instructions would fix it, because instructions load into every window and the assistant would then apply every policy rule consistently.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Legal department ke Claude Project mein 300 pages policies knowledge ke taur par aur chaar pages standing instructions. Users: AI hamesha instruction "2015 se purana case cite mat karo" follow karta, magar knowledge files ke page 212 ke rules kabhi miss. Admin: instructions har dafa window mein; knowledge window se bari ho to product search karke relevant hisse laata; project ek pre-loaded window hai. Head of legal chahta missed rules reliably follow hon. Ek colleague: saare 300 pages instructions mein; doosra: AI ko kaho "har jawab se pehle saare 300 pages parho".

**Sawal:** Situation ke baare mein kaunsa bayan INCORRECT hai?

**Options ka matlab:**

- **A** — Instructions har dafa load hoti — is liye 2015 rule hamesha follow; bari knowledge on-demand retrieve hoti — is liye page 212 kabhi miss.
- **B** — AI ko 300 pages parhne ka kehna window mein kya fit hota wo nahi badalta, kyunke retrieval khud relevant hisse chunta.
- **C** — Hamesha-lagu rules chhote aur instructions mein; reference material knowledge mein, aur sawal relevant document ki taraf point karein.
- **D** — 300 pages instructions mein daal do to masla hal — instructions har window mein load hoti aur AI har policy rule consistently lagayega.

</details>

**Answer:** D

- ✅ **D** — Instructions share the same finite window; 300 pages there would crowd out the work and dilute everything.
- ❌ **A** — This is correct.
- ❌ **B** — This is correct: an instruction cannot expand the window.
- ❌ **C** — This is the recommended split.

**Yaad rakho:** Instructions har window mein, bara knowledge retrieve hota hai. Lazmi rules chhote aur instructions mein.

*Grounded in: Quick Reference §4 (project retrieval when knowledge outgrows the window) and What AI Actually Is A.5 (instructions and projects; a project is a pre-loaded window)*

---

### Q82. *(Select TWO — all-or-nothing)*
An accounts assistant builds a Skill folder for weekly reports and the upload fails. She inspects five details. D1: the folder is named "Weekly Management Report". D2: the required file is named "skill.md". D3: the frontmatter name is "claude-weekly-report". D4: the description reads "Use when asked for a weekly report or management summary, formats amounts in PKR", about 20 words. D5: the instructions live in the same SKILL.md file after the frontmatter, with an optional references folder. A colleague says the description must be five sentences and that the instructions must sit in a separate file. The platform's rules: the one required file must be named exactly SKILL.md; the folder name uses kebab-case; the name and description must contain no XML-style tags and stay short and specific; "claude" and "anthropic" are reserved in a Skill name.

**Which TWO details would block or break the upload?**

- A. D4: the description is too short, since the platform requires at least five sentences so that the assistant can tell it apart from other Skills.
- B. D2: the one required text file must be named exactly SKILL.md in capital letters, and here it is skill.md, so the upload is rejected.
- C. D5: the instructions must be in a separate INSTRUCTIONS file, since SKILL.md may hold only the frontmatter and a pointer to where the rules are kept.
- D. D3: the name contains 'claude', a reserved word, so it must be renamed even though the rest of the frontmatter is valid.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Accounts assistant weekly reports ka Skill folder banati, upload fail. Paanch details: D1 folder ka naam "Weekly Management Report". D2 zaroori file ka naam "skill.md". D3 frontmatter name "claude-weekly-report". D4 description "Use when asked for a weekly report or management summary, formats amounts in PKR" (~20 words). D5 instructions usi SKILL.md mein frontmatter ke baad, optional references folder. Colleague: description 5 jumle ho aur instructions alag file mein. Platform rules: zaroori file ka naam bilkul SKILL.md; folder name kebab-case; name/description mein XML-style tags nahi, chhote aur specific; "claude" aur "anthropic" Skill name mein reserved.

**Sawal:** Kaunse DO details upload ko block ya break karenge?

**Options ka matlab:**

- **A** — D4 — description chhoti, platform ko kam az kam paanch jumle chahiye.
- **B** — D2 — zaroori file ka naam bilkul SKILL.md (capital) hona chahiye; yahan skill.md, to reject.
- **C** — D5 — instructions alag INSTRUCTIONS file mein honi chahiye.
- **D** — D3 — naam mein "claude" reserved word, rename karna hoga chahe baaqi frontmatter valid ho.

</details>

**Answer:** B, D

- ✅ **B** — The required file must be named exactly SKILL.md.
- ✅ **D** — Reserved words are not allowed in a Skill name.
- ❌ **A** — The description should be short and specific; there is no five-sentence minimum.
- ❌ **C** — SKILL.md holds the name, description and instructions; extra files are optional.

**Yaad rakho:** SKILL.md bilkul isi naam se; folder kebab-case; naam mein claude/anthropic nahi.

*Grounded in: Skills & Connectors §11 (rules that prevent upload errors: exactly SKILL.md; kebab-case folder; no XML tags; no 'claude' or 'anthropic' in a name; SKILL.md structure)*

---

### Q83.
A project manager uses a coworking agent and wants five facts to persist across next quarter. F1: "Invoices under PKR 50,000 count as routine in supplier reports" (one reporting stream). F2: "Write in short sentences and lead with the answer" (everything she does). F3: "What we decided about the Karachi warehouse on Tuesday" (one decision relevant to a live project). F4: "The approved supplier price list for this quarter" (a file the reports must read). F5: "My role, audience and hard limits, portable if I change vendors". Layers available: session history, a Project's instructions, a Project's knowledge, account-wide instructions, and a user-owned context file. Each fact goes in the narrowest layer that reliably applies, and F5 must survive a change of vendor. Four allocations of F1 to F5 in order are offered.

**Which allocation is correct?**

- A. F1 Project knowledge; F2 account-wide instructions; F3 account-wide instructions; F4 Project instructions; F5 session history.
- B. F1 account-wide instructions; F2 Project instructions; F3 session history; F4 Project knowledge; F5 user-owned context file.
- C. F1 Project instructions; F2 account-wide instructions; F3 session history; F4 Project knowledge; F5 account-wide instructions.
- D. F1 Project instructions; F2 account-wide instructions; F3 Project knowledge (or the context file); F4 Project knowledge; F5 user-owned context file.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Project manager coworking agent ke saath paanch facts agli quarter persist karna chahti. F1: "Supplier reports mein PKR 50,000 se kam invoices routine" (ek reporting stream). F2: "Chhote jumle, jawab pehle" (har kaam). F3: "Tuesday ko Karachi warehouse par kya tay hua" (live project ka ek faisla). F4: "Is quarter ki approved supplier price list" (file jo reports parhein). F5: "Mera role, audience aur hard limits — vendor badlun to saath jaaye". Layers: session history, Project instructions, Project knowledge, account-wide instructions, user-owned context file. Har fact sab se tang reliable layer mein; F5 vendor change ke baad bhi bache.

**Sawal:** F1–F5 ki kaunsi allocation sahi hai?

**Options ka matlab:**

- **A** — F1 Project knowledge; F2 account-wide; F3 account-wide; F4 Project instructions; F5 session history.
- **B** — F1 account-wide; F2 Project instructions; F3 session history; F4 Project knowledge; F5 user-owned context file.
- **C** — F1 Project instructions; F2 account-wide; F3 session history; F4 Project knowledge; F5 account-wide.
- **D** — F1 Project instructions; F2 account-wide; F3 Project knowledge (ya context file); F4 Project knowledge; F5 user-owned context file.

</details>

**Answer:** D

- ✅ **D** — Each fact goes in the narrowest reliable layer; a decision is not left in session history, and a portable fact lives in a file she owns.
- ❌ **A** — A rule and a reference file are swapped, a one-off decision is not an account-wide rule, and session history does not travel.
- ❌ **B** — A one-stream rule does not belong account-wide, and a decision left in session history is not reliable in a new session.
- ❌ **C** — A decision must not rely on one session's history, and vendor-held instructions do not survive a change of vendor.

**Yaad rakho:** Har fact sab se tang bharosemand layer mein; jo vendor badalne par bhi chahiye wo apni context file mein.

*Grounded in: General Agents on the Web §4 (persistence is a stack; narrowest reliable layer; session history is not memory; a user-owned portable context file)*

---

### Q84.
A compliance team's cloud agent produces five things during a monthly run, and the team must decide where each lives. Tiers: Tier 1 is the task filesystem, temporary scratch wiped when the task ends; Tier 2 is platform storage, saved to the vendor account, surviving the task but in the vendor's custody and format; Tier 3 is a system the firm controls (records system, drive, repository, inbox). Item 1: intermediate CSV files the agent uses while computing. Item 2: the vendor-risk memo delivered to the regulator's file, which the regulator requires the firm to retain for seven years. Item 3: a session log of what the agent did this month. Item 4: the final signed memo sent to the client. Item 5: a draft the agent may need again in tomorrow's session. Four mappings of Items 1 to 5 in order are offered.

**Which mapping is correct?**

- A. Item 1 Tier 3; Item 2 Tier 3; Item 3 Tier 2; Item 4 Tier 3; Item 5 Tier 1.
- B. Item 1 Tier 1; Item 2 Tier 3; Item 3 Tier 2; Item 4 Tier 3; Item 5 Tier 2.
- C. Item 1 Tier 2; Item 2 Tier 2; Item 3 Tier 3; Item 4 Tier 2; Item 5 Tier 1.
- D. Item 1 Tier 1; Item 2 Tier 2; Item 3 Tier 2; Item 4 Tier 3; Item 5 Tier 3.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Compliance team ka cloud agent monthly run mein paanch cheezein banata; har ek kahan rahe? Tiers: Tier 1 task filesystem — temporary scratch, task khatam hone par saaf. Tier 2 platform storage — vendor account mein, task ke baad bachti magar vendor ki custody aur format mein. Tier 3 firm ke control wala system (records system, drive, repository, inbox). Item 1: calculation ke dauran intermediate CSV files. Item 2: regulator ki file mein jane wala vendor-risk memo, jo regulator 7 saal rakhwana chahta. Item 3: is mahine agent ne kya kiya uska session log. Item 4: client ko bheja final signed memo. Item 5: ek draft jo agent ko kal ke session mein dobara chahiye ho sakta.

**Sawal:** Items 1–5 ki kaunsi mapping sahi hai?

**Options ka matlab:**

- **A** — Item 1 Tier 3; Item 2 Tier 3; Item 3 Tier 2; Item 4 Tier 3; Item 5 Tier 1.
- **B** — Item 1 Tier 1; Item 2 Tier 3; Item 3 Tier 2; Item 4 Tier 3; Item 5 Tier 2.
- **C** — Item 1 Tier 2; Item 2 Tier 2; Item 3 Tier 3; Item 4 Tier 2; Item 5 Tier 1.
- **D** — Item 1 Tier 1; Item 2 Tier 2; Item 3 Tier 2; Item 4 Tier 3; Item 5 Tier 3.

</details>

**Answer:** B

- ✅ **B** — Scratch stays in Tier 1, records and finished deliverables exit to the firm's own system, and things needed again in the vendor's account can sit in Tier 2.
- ❌ **A** — Intermediate files are scratch, and tomorrow's draft cannot rely on Tier 1.
- ❌ **C** — A regulated record cannot rely on platform storage, and a draft needed tomorrow cannot sit in wiped scratch.
- ❌ **D** — The regulator's memo needs the firm's own system of record with its own retention.

**Yaad rakho:** Scratch Tier 1; regulator/client ka final kaam Tier 3 (apna system); jo kal chahiye Tier 2.

*Grounded in: General Agents on the Web §5 (the three file tiers: scratch, platform storage, your own system of record; finished work exits the platform)*

---

### Q85. *(Select TWO — all-or-nothing)*
A team's Project has been running for a year and its stored context is reviewed. Item a: the supplier price list, last updated in Q1; the supplier repriced on 1 August. Item b: the style guide, last reviewed two months ago; no change since. Item c: a memory note saying "the client prefers formal tone", written two years ago; the client's team changed in June. Item d: a standing instruction "lead with the answer", written last month. Item e: the regulator's reporting template, replaced by a new template on 1 September; the Project still holds the old one. Anything that no longer matches the world can produce a confident, well-formatted answer with no error message. The review's aim is to decide which items are stale and need a keep, correct or delete decision now, and the team wants the two most certainly stale.

**Which TWO items are certainly stale?**

- A. Item e: the Project still holds the old regulatory template that has been replaced, so new returns would be formatted to the wrong standard.
- B. Item a: the price list predates the supplier's repricing on 1 August, so outputs quoting it are quietly wrong.
- C. Item d: the instruction written last month, since a standing instruction recently added is the most likely to have been written in error.
- D. Item b: the style guide, since anything last reviewed two months ago is stale by default and should be replaced at the next review.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Ek saal se chalte Project ke stored context ka review. a: supplier price list, aakhri update Q1; supplier ne 1 August ko reprice kiya. b: style guide, do mahine pehle review, tab se koi change nahi. c: memory note "client formal tone pasand karta", do saal purana; June mein client ki team badli. d: standing instruction "jawab pehle", pichle mahine likhi. e: regulator ka reporting template, 1 September ko naye se badla; Project mein ab bhi purana. Jo cheez duniya se match na kare wo bina error ke confident, formatted jawab de sakti. Team do sab se yaqeeni stale items chahti.

**Sawal:** Kaunse DO items yaqeenan stale hain?

**Options ka matlab:**

- **A** — Item e — Project mein purana regulatory template jo badal chuka, naye returns ghalat standard par format honge.
- **B** — Item a — price list supplier ke 1 August reprice se pehle ki, us se quote karne wale outputs chupke se ghalat.
- **C** — Item d — haal mein likhi instruction, naye instruction ke ghalat likhe jaane ka sab se zyada imkaan.
- **D** — Item b — do mahine pehle review hua, default stale, agle review par badlo.

</details>

**Answer:** A, B

- ✅ **A** — A superseded reference document sitting in the knowledge base is stale configuration.
- ✅ **B** — A file that no longer matches the world fails silently.
- ❌ **C** — It is recent and unaffected by any change in the world.
- ❌ **D** — Age alone does not make it stale; nothing has changed.

**Yaad rakho:** Purani tareekh nahi, duniya badalne se stale hota hai: 1 Aug ki repricing aur naya template.

*Grounded in: Quick Reference §5 (stored context is a responsibility; stale context fails quietly) and Workflow Design §11 (stale configuration is the one that fails silently)*

---

### Q86. *(Select TWO — all-or-nothing)*
A regional sales head has added a line to her standing instructions every time the assistant did something she disliked. After a year there are 22 lines. Examples: L3 "keep answers short"; L7 "give complete explanations"; L9 "always use British spelling"; L14 "match the reader's spelling"; L18 "I work in sales for a food distributor and write for retail buyers"; L20 "push back when you think I am wrong instead of agreeing by default"; L21 "be helpful and concise". Outputs feel unpredictable and bland. She recalls that a large AI company deleted most of its own accumulated standing instructions with no loss in quality, and knows the pruning test: for each line ask, if I delete this, will the assistant get something wrong? A colleague proposes emphatic wording for the important lines.

**Which TWO lines should she keep, under the pruning test?**

- A. L21: 'be helpful and concise' should be kept, since concision and helpfulness are the qualities she wants in every output, and a general goal costs nothing to keep.
- B. L20: an instruction to push back rather than agree by default counters the trained lean toward agreement in every conversation and is not something it does on its own.
- C. L3 and L7 both: keep them both, since each captures a real preference about length, and emphasising them will help the assistant to choose between them.
- D. L18: who she is and who she writes for cannot be worked out by the assistant, so deleting it would make outputs wrong for her audience.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Regional sales head ne har naapasand harkat par standing instructions mein line jodi; saal baad 22 lines. Misalein: L3 "jawab chhote rakho"; L7 "complete explanations do"; L9 "hamesha British spelling"; L14 "reader ki spelling follow karo"; L18 "main food distributor mein sales mein, retail buyers ke liye likhti hoon"; L20 "jab lage main ghalat hoon to push back karo, default mein agree mat karo"; L21 "helpful aur concise raho". Outputs unpredictable aur phike. Pruning test: har line par poocho — delete karun to kya AI kuch ghalat karega? Colleague: zaroori lines par emphatic wording.

**Sawal:** Pruning test ke tehat kaunsi DO lines rakhni chahiye?

**Options ka matlab:**

- **A** — L21 — helpful aur concise har output mein chahiye, general goal rakhne ki koi qeemat nahi.
- **B** — L20 — default agree ke bajaye push back ki instruction har conversation mein trained agreeableness ka tod hai, aur AI yeh khud nahi karta.
- **C** — L3 aur L7 dono — dono length ki asal preference, emphasis se AI dono mein chunega.
- **D** — L18 — wo kaun hai aur kis ke liye likhti AI khud nahi jaan sakta, delete karne se outputs audience ke liye ghalat.

</details>

**Answer:** B, D

- ✅ **B** — It is true for every conversation and changes behavior in a way the assistant would not choose.
- ✅ **D** — Write what the assistant cannot work out on its own: job, audience, hard limits.
- ❌ **A** — A vague instruction constrains nothing; deleting it would not make the assistant get anything wrong.
- ❌ **C** — They contradict each other; emphasis makes the conflict louder, and the line to keep is one that resolves it.

**Yaad rakho:** Jo AI khud nahi jaan sakta (tum kaun, kis ke liye, push-back) rakho; vague aur mutazad lines hatao.

*Grounded in: AI Prompting 2026 §4 (keep your own layer short and prune it; if I delete this, will the AI get something wrong; write what the AI cannot work out) and What AI Actually Is A.5*

---

### Q87.
A small law practice serves two clients with conflicting interests, and an associate works on both in one workspace. The practice manager worries that details from one client may surface in work for the other, and lists four proposed measures. M1: put each client in its own project, with its own knowledge, instructions and project-scoped memory, and confirm that every file is approved for the workspace. M2: add "never mention Client A's details while working on Client B" to the instructions. M3: use incognito chats for one client only. M4: keep one project for both, with a naming convention for chats. She reads that a project always helps organise, that project-only memory is what turns it into isolation, that an instruction is a request rather than a wall, and that incognito keeps a chat out of history and memory without scoping memories that already exist. The clients' confidentiality clauses forbid any cross-use of their material.

**Which measure actually creates a boundary between the two clients?**

- A. M2: the standing instruction, since a clear rule stops the assistant carrying Client A's facts into work for Client B, wherever those facts are held.
- B. M4: one project with a naming convention, since consistent chat names let the assistant recognise which client each conversation concerns and keep them apart.
- C. M1: separate projects, each with its own knowledge, instructions and project-scoped memory, so neither client's material shares a window or memory with the other, plus file approval.
- D. M3: incognito chats for one client, since incognito keeps that client's content out of history and memory so that it cannot reach work for the other client later.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Chhoti law practice ke do clients ke interests takrate; associate dono par ek workspace mein kaam karta. Manager ki fikr: ek client ki details doosre ke kaam mein aa jayein. Chaar measures: M1 har client ka apna project — apni knowledge, instructions, project-scoped memory — aur confirm karo har file workspace ke liye approved. M2 instructions mein "Client B par kaam karte hue Client A ki details mention mat karo". M3 sirf ek client ke liye incognito. M4 dono ke liye ek project, chats ka naming convention. Wo parhti: project organise karta, project-only memory hi usay isolation banati, instruction ek darkhwast hai deewar nahi, aur incognito chat ko history/memory se bahar rakhta magar maujood memories scope nahi karta. Confidentiality clauses koi cross-use allow nahi karti.

**Sawal:** Kaunsa measure waqai dono clients ke beech boundary banata hai?

**Options ka matlab:**

- **A** — M2 — saaf rule Client A ke facts ko B ke kaam mein jaane se rokta, facts jahan bhi hon.
- **B** — M4 — naming convention se AI pehchaan kar alag rakhega.
- **C** — M1 — alag projects, har ek ki apni knowledge, instructions aur project-scoped memory, taake kisi client ka material doosre ke saath window ya memory share na kare, plus file approval.
- **D** — M3 — ek client ke liye incognito, us ka content history/memory se bahar.

</details>

**Answer:** C

- ✅ **C** — A project is a boundary only where memory and files are scoped to it.
- ❌ **A** — An instruction is a request, not a wall; the facts may still be in the same context or memory.
- ❌ **B** — A naming convention does not scope files or memory.
- ❌ **D** — Incognito is memory-free, not trace-free, and does not scope existing memories or files.

**Yaad rakho:** Deewar = alag project + project-scoped memory. Instruction darkhwast hai, naming convention kuch scope nahi karti.

*Grounded in: Quick Reference §4-5 (project-only memory turns a project into isolation; incognito is memory-free not trace-free) and What AI Actually Is A.5 (projects keep separate memory spaces)*

---

### Q88.
A consultancy's knowledge lead completes four statements about four features. (a) Account-wide custom instructions touch ... (b) A Skill touches ... (c) A Project loads its files and instructions ... (d) Memory holds ... She hears four sets of completions from staff and asks which set is correct under Anthropic's split. Set 1: (a) all your chats; (b) one kind of task and waits for a matching request, working in any chat; (c) always, inside its own workspace; (d) context about you that evolves, per user, best-effort. Set 2: (a) only the current Project; (b) everything you do; (c) only when asked for; (d) context shared across colleagues. Set 3: (a) all your chats; (b) everything you do; (c) only inside chats with a request that matches; (d) context about you, shared team-wide. Set 4: (a) only the current Project; (b) one kind of task; (c) always, everywhere; (d) facts fixed for all time.

**Which set is correct?**

- A. Set 1: instructions apply to all chats; a Skill touches one kind of task and fires on a match; a Project is always on in its workspace; memory is per-user.
- B. Set 3: custom instructions apply to all chats, a Skill touches everything, a Project loads only on a matching request, and memory is shared team-wide.
- C. Set 2: custom instructions apply only in the current Project, a Skill touches everything, a Project loads only when asked for, and memory is shared across colleagues.
- D. Set 4: custom instructions apply only in the current Project, a Skill touches one kind of task, a Project loads everywhere, and memory holds fixed facts.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Consultancy ki knowledge lead chaar features ke chaar jumle poore karwati: (a) account-wide custom instructions ... chhooti hain; (b) Skill ... chhoota hai; (c) Project apni files aur instructions ... load karta; (d) Memory ... rakhti hai. Staff ke chaar sets. Set 1: (a) tumhari saari chats; (b) ek kism ka task, matching request ka intezaar, kisi bhi chat mein; (c) hamesha, apne workspace ke andar; (d) tumhare baare mein evolve hota context, per user, best-effort. Set 2: (a) sirf current Project; (b) sab kuch; (c) sirf maangne par; (d) colleagues mein shared. Set 3: (a) saari chats; (b) sab kuch; (c) sirf matching request wali chats mein; (d) tumhara context, team-wide shared. Set 4: (a) sirf current Project; (b) ek kism ka task; (c) hamesha, har jagah; (d) hamesha ke liye fixed facts.

**Sawal:** Kaunsa set sahi hai?

**Options ka matlab:**

- **A** — Set 1 — instructions saari chats; Skill ek kism ka task aur match par fire; Project apne workspace mein hamesha on; memory per-user.
- **B** — Set 3 — instructions saari chats, Skill sab kuch, Project sirf matching request par, memory team-wide.
- **C** — Set 2 — instructions sirf current Project, Skill sab kuch, Project sirf maangne par, memory colleagues mein shared.
- **D** — Set 4 — instructions sirf current Project, Skill ek kism ka task, Project har jagah, memory fixed facts.

</details>

**Answer:** A

- ✅ **A** — This is the clean split: instructions for stable rules, memory for evolving context, projects for scoped work, skills for methods.
- ❌ **B** — A Skill touches one kind of task, and a Project is always on inside its workspace.
- ❌ **C** — Custom instructions apply to all chats, and memory is per-user.
- ❌ **D** — Custom instructions are not project-scoped, a Project is scoped to its workspace, and memory evolves.

**Yaad rakho:** Instructions har chat mein, Skill ek kism ke kaam par, Project apne andar hamesha, memory tumhari aur badalti hui.

*Grounded in: Skills & Connectors §4 (Skill, Connector, Project, custom instructions: what each touches); Quick Reference §5 (instructions for stable rules, memory for evolving context, projects for scoped work)*

---

### Q89.
A finance operations lead asked skill-creator to build a client-summary Skill, clicked "Save skill" and announced that it was deployed. Three days later a colleague reports that "the March client summary" gets an ordinary chat answer and a quick total triggers the Skill. The lead lists what to do: (1) test what starts it, in both directions (requests that should start it, and unrelated requests that should not); (2) read the draft and check each instruction line would be read the same by two colleagues; (3) test the output on realistic input; (4) test awkward cases such as a client with no income or a payment exactly on the threshold; (5) bring specific failures back to skill-creator, noting when each first appeared. Four orders of the five steps are offered.

**Which order follows the build-and-test guidance?**

- A. 2, 1, 3, 4, 5: read the draft; test triggers in both directions; test output; test awkward cases; then bring specific failures back.
- B. 2, 3, 4, 1, 5: read the draft; test output and awkward cases; then test what starts it; then bring failures back.
- C. 1, 3, 2, 4, 5: test what starts it; test output; then read the draft; then test awkward cases; then bring failures back.
- D. 5, 2, 1, 3, 4: bring failures to skill-creator first; then read the draft; then test triggers, output and awkward cases.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Finance ops lead ne skill-creator se client-summary Skill banwaya, "Save skill" kiya aur deployed announce kar diya. Teen din baad colleague: "the March client summary" par aam chat jawab, aur quick total Skill trigger karta. Lead ki list: (1) kya start karta test karo, dono taraf (jo requests start karein aur unrelated jo na karein); (2) draft parho aur check karo har instruction line do colleagues ek jaisa samjhein; (3) realistic input par output test; (4) awkward cases (bina income wala client, threshold par bilkul barabar payment); (5) specific failures skill-creator ko wapas do, har ek pehli dafa kab aaya note karke. Paanch steps ki chaar orders.

**Sawal:** Kaunsa order build-and-test guidance follow karta hai?

**Options ka matlab:**

- **A** — 2, 1, 3, 4, 5 — draft parho; dono taraf triggers test; output test; awkward cases; phir specific failures wapas.
- **B** — 2, 3, 4, 1, 5 — draft; output aur awkward cases; phir start test; phir failures.
- **C** — 1, 3, 2, 4, 5 — start test; output; phir draft parho; phir awkward cases; phir failures.
- **D** — 5, 2, 1, 3, 4 — pehle failures skill-creator ko; phir draft; phir triggers, output, awkward cases.

</details>

**Answer:** A

- ✅ **A** — Drafting is not deployment: review the draft first, then triggers, output, hard cases, and iterate.
- ❌ **B** — A Skill that never fires produces no output to test, so trigger tests come before output tests.
- ❌ **C** — The draft is read before testing so that loose lines are fixed before they produce confusing results.
- ❌ **D** — There are no failures to bring back until the tests have been run.

**Yaad rakho:** Draft parho, trigger dono taraf, output, awkward cases, phir failures wapas skill-creator ko.

*Grounded in: Skills & Connectors §13-14 (test, then iterate: read the draft, test what starts it, test the output, test awkward cases, bring failures back) and What AI Actually Is A.8*

---

### Q90. *(Select TWO — all-or-nothing)*
A regional finance lead put "Always answer in Markdown tables" in her account-wide instructions because it helped on her reports. Since then a colleague's chat in the shared workspace produced a table for a short thank-you email, and a request for narrative advice came back as a three-column table. The same field holds "Be helpful and concise". A colleague says the field is placed in the window before the first word of every conversation, so it should hold only what is true for every conversation she will ever have: who she is, her tone, and a push-back line. The lead considers four fixes for the table rule: keep it account-wide with exceptions; move it to the reporting Project's instructions; make it a Skill for report requests; capitals.

**Which TWO fixes are correct?**

- A. Make it a Skill for report requests, so it fires on a match to 'report' and stays out of emails and narrative advice.
- B. Move the table rule to the reporting Project's instructions, so it is always on inside the reporting workspace and nowhere else.
- C. Keep the rule account-wide but add 'except when writing prose or emails', since exceptions restore correct behavior in each case.
- D. Keep the rule account-wide and put it in capitals, since emphatic wording makes the assistant weigh it correctly against a request for prose.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Regional finance lead ne account-wide instructions mein "Hamesha Markdown tables mein jawab do" daala (reports mein madad mili). Tab se shared workspace mein colleague ki chat ne chhoti thank-you email ke liye table banaya, aur narrative advice teen-column table ban kar aayi. Usi field mein "Be helpful and concise". Colleague: field har conversation ke pehle lafz se pehle window mein daala jaata, to sirf wahi ho jo har conversation mein sach ho — wo kaun hai, uski tone, aur push-back line. Table rule ke chaar fixes: exceptions ke saath account-wide rakho; reporting Project ki instructions mein le jao; report requests ke liye Skill banao; capitals.

**Sawal:** Kaunse DO fixes sahi hain?

**Options ka matlab:**

- **A** — Report requests ke liye Skill banao — "report" par match ho kar fire, emails aur narrative advice se bahar.
- **B** — Table rule reporting Project ki instructions mein le jao — reporting workspace ke andar hamesha on, aur kahin nahi.
- **C** — Account-wide rakho magar "prose ya emails ke waqt nahi" jodo.
- **D** — Account-wide rakho aur capitals mein — emphatic wording sahi wazan deti.

</details>

**Answer:** A, B

- ✅ **A** — A method for one kind of task belongs in a Skill that fires on a description match.
- ✅ **B** — A topic-specific rule belongs in the project; a wrong-scope global instruction damages every chat where it does not apply.
- ❌ **C** — Piling exceptions into a global line grows clutter and still loads the rule into every window.
- ❌ **D** — Emphasis does not fix wrong scope; it makes the damage in non-report chats worse.

**Yaad rakho:** Global field mein sirf har guftagu ka sach; table wali cheez project ya Skill mein.

*Grounded in: What AI Actually Is A.5 (Instructions for Claude: write only what is true for every conversation; wrong-scope and vague instructions; push topic-specific rules into a project) and Skills & Connectors §4*

---

## Domain 7 — Troubleshooting and Optimization (10% — 10 questions)

### Q91.
A team reports four separate problems with the same workspace, each described with its timing, and a trainer asks for the first hypothesis for each (under-specification, context overload, wrong feature or model, stale configuration), knowing that timing tells you where to look first but not what the cause is. P1: the summary of a contract is wrong from the very first answer in a fresh chat. P2: a drafting task began well but by message 45 in the same chat it ignores the rule set in message 1. P3: totals in a commission report are subtly wrong every run, whichever tier is used, from the first answer. P4: a client-summary Skill produced correct output for five months and, in fresh chats, now flags the wrong payments though its file has not changed. Four mappings of P1 to P4 are offered.

**Which mapping of first hypotheses is correct?**

- A. P1 context overload; P2 under-specification; P3 wrong feature; P4 stale configuration.
- B. P1 under-specification; P2 stale configuration; P3 context overload; P4 wrong feature.
- C. P1 under-specification; P2 context overload; P3 wrong feature; P4 stale configuration.
- D. P1 wrong feature; P2 context overload; P3 under-specification; P4 stale configuration.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Team ek workspace ki chaar alag problems unki timing ke saath report karti; trainer har ek ka pehla hypothesis chahta (under-specification, context overload, wrong feature/model, stale configuration) — timing batati pehle kahan dekhna, wajah nahi. P1: fresh chat ke pehle jawab se hi contract summary ghalat. P2: drafting task achha shuru hua magar usi chat ke message 45 tak message 1 ka rule ignore. P3: commission report ke totals har run thode ghalat, koi bhi tier, pehle jawab se. P4: client-summary Skill paanch mahine sahi output deta raha, ab fresh chats mein ghalat payments flag, file nahi badli.

**Sawal:** P1–P4 ke pehle hypotheses ki kaunsi mapping sahi hai?

**Options ka matlab:**

- **A** — P1 context overload; P2 under-specification; P3 wrong feature; P4 stale configuration.
- **B** — P1 under-specification; P2 stale configuration; P3 context overload; P4 wrong feature.
- **C** — P1 under-specification; P2 context overload; P3 wrong feature; P4 stale configuration.
- **D** — P1 wrong feature; P2 context overload; P3 under-specification; P4 stale configuration.

</details>

**Answer:** C

- ✅ **C** — Wrong from the first answer points at the prompt; degrades as the chat grows points at session length; one repeatable error type points at the feature; it used to work points at the setup.
- ❌ **A** — A fresh chat with a wrong first answer rules out context overload, and a rule obeyed at first and lost later is not a thin prompt.
- ❌ **B** — Degradation over a long chat is context overload, and errors that appear from the start and repeat point at the feature.
- ❌ **D** — The first answer wrong in a fresh chat points at the prompt, and subtle numeric errors point at a calculation asked for in prose.

**Yaad rakho:** Pehle jawab se ghalat = prompt; chat lambi hone par bigda = context overload; ek hi kism ki ghalti = feature; pehle chalta tha = purani config.

*Grounded in: Workflow Design §11 (four causes told apart by when the symptom appeared; timing tells you where to look first, not what the cause is)*

---

### Q92.
An operations manager's fresh-chat request for a supplier-contract summary comes back disappointing: it misses the two payment terms she cares about. She feels she should switch to the most capable model and, if that fails, declare the task unfit. Her colleague states five claims about the diagnostic sequence, which runs cheapest first. C1: "Step one is to re-read the prompt against its five parts: role, context, task, constraints, format." C2: "Step two is to check the length of the conversation for overload." C3: "Step three is to check the feature and the model: is it a calculation needing code execution, or a hard task on a speed tier?" C4: "Step four is to check whether the configuration is current: instructions, knowledge and Skills." C5: "Switching to the strongest model is a cheap first move, and questioning whether the task fits should come right after the prompt check, since it saves time."

**Which claim is INCORRECT?**

- A. C3: the third check is the feature and model, for example a calculation asked for in prose or a hard task on a speed tier.
- B. C1: re-reading the prompt against its five parts costs seconds and resolves the most common cause, so it goes first.
- C. C5: the strongest-model switch is a bottom-of-ladder move and task-fit questioning ends the attempt, so both come last.
- D. C4: the fourth check is whether the configuration (instructions, knowledge, Skills) is current, because stale configuration fails silently.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Ops manager ki fresh-chat supplier-contract summary mayoos karti — do aham payment terms miss. Wo sochti sab se capable model lo, fail ho to task unfit declare karo. Colleague diagnostic sequence (sasta pehle) ke paanch claims deta. C1: "Step 1 — prompt ko paanch parts (role, context, task, constraints, format) se dobara parho." C2: "Step 2 — conversation ki length overload ke liye check." C3: "Step 3 — feature aur model: kya yeh calculation hai jise code execution chahiye, ya speed tier par mushkil task?" C4: "Step 4 — configuration current hai: instructions, knowledge, Skills." C5: "Strongest model par jaana sasta pehla qadam hai, aur task fit ka sawal prompt check ke foran baad aana chahiye, waqt bachta."

**Sawal:** Kaunsa claim INCORRECT hai? (Har option ek claim ko uski sahi shakal mein bataata hai — ghalat claim wala option chuno.)

**Options ka matlab:**

- **A** — C3 — teesra check feature aur model, jaise prose mein maangi calculation ya speed tier par mushkil task.
- **B** — C1 — prompt ko paanch parts se parhna seconds leta aur sab se aam wajah hal karta, is liye pehle.
- **C** — C5 — strongest-model switch ladder ke neeche wala move hai aur task-fit ka sawal koshish khatam karta, is liye dono aakhir mein.
- **D** — C4 — chautha check configuration current hai ya nahi, kyunke stale configuration chupke se fail hoti.

</details>

**Answer:** C

- ✅ **C** — The cheapest-first sequence puts the task-fit question last.
- ❌ **A** — This is correct.
- ❌ **B** — This is correct.
- ❌ **D** — This is correct.

**Yaad rakho:** Sasti jaanch pehle: prompt, chat ki lambai, feature/model, config, aakhir mein task-fit.

*Grounded in: Workflow Design §12 (the diagnostic sequence: prompt, session length, feature and model, configuration, then the task; cheapest first)*

---

### Q93.
An analyst asks an assistant to write and run code that totals monthly sales from a merged file. Three problems occur. Day 1: a red error message about a missing column. Day 2: no error, but the total is 8.1 million against the 7.6 million she knows. Day 3: after three attempts each claiming the total is now correct, the assistant returns a different wrong number each time; the chat is long and confused. She has four ways to respond to each day and wants the set that follows the guidance. Guidance she recalls: an error is the computer saying exactly what it needs; for a wrong number with no error give the symptom and the value you expected and ask for row counts and sample rows; after the same fix has failed three times step back and ask for two different approaches, in a clean chat if needed.

**Which set of responses is correct?**

- A. Day 1: paste the full error; Day 2: ask a stronger tier to rerun the same code; Day 3: switch tiers and continue the same chat.
- B. Day 1: paste the full error; Day 2: give the symptom and expected value and ask for row counts; Day 3: restate fresh in a clean chat and ask for two approaches.
- C. Day 1: state the symptom and expected value; Day 2: paste the full error; Day 3: ask for a fourth fix with a firmer instruction to check the total.
- D. Day 1: ask for a different approach; Day 2: paste the last output and ask for diagnosis; Day 3: state the symptom and the expected value.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Analyst AI se merged file ki monthly sales total ka code likhwa kar chalwati. Teen masle. Day 1: missing column ka red error message. Day 2: error nahi, magar total 8.1 million jabke usay 7.6 pata hai. Day 3: teen koshishein, har ek "ab sahi" kehti, har dafa alag ghalat number; chat lambi aur uljhi. Yaad guidance: error computer ka exact batana hai use kya chahiye; bina error ghalat number par symptom aur expected value do aur row counts + sample rows maango; same fix teen dafa fail ho to peeche hato aur do alag approaches maango, zaroorat ho to clean chat mein.

**Sawal:** Responses ka kaunsa set sahi hai?

**Options ka matlab:**

- **A** — Day 1 poora error paste; Day 2 stronger tier se same code rerun; Day 3 tier badal kar same chat jaari.
- **B** — Day 1 poora error paste; Day 2 symptom aur expected value do, row counts maango; Day 3 clean chat mein fresh restate karke do approaches maango.
- **C** — Day 1 symptom aur expected value; Day 2 poora error paste; Day 3 total check karne ki sakht instruction ke saath chautha fix.
- **D** — Day 1 alag approach maango; Day 2 aakhri output paste karke diagnosis; Day 3 symptom aur expected value.

</details>

**Answer:** B

- ✅ **B** — Each symptom has its own smallest fitting move.
- ❌ **A** — A wrong number with no error needs the symptom and row counts, and the long confused chat is part of the problem.
- ❌ **C** — There is an error message on Day 1 and none on Day 2, and a fourth identical attempt continues the loop.
- ❌ **D** — Two approaches are for repeated failure, and Day 3 is a case of three failed fixes, not a first wrong number.

**Yaad rakho:** Error = paste karo; ghalat number = symptom + expected + row counts; teen baar wahi fix = do naye raaste, saaf chat.

*Grounded in: Code You Never Write §7 (errors are dialogue; runs but a number contradicts what you know: symptom and expected value; same fix fails three times: step back and propose two different approaches)*

---

### Q94. *(Select TWO — all-or-nothing)*
A treasury analyst has spent a week trying to get an assistant to forecast next quarter's export sales "to the exact rupee". She kept a log of what was ruled out. Prompt: covers role, context, task, constraints and format. Session length: every attempt in a fresh chat. Feature and model: totals computed by code execution on the historical data; the top tier tried, no change. Configuration: standing instructions and the data source checked and current. Result: the forecast differs from actuals by a different amount each quarter. She wants to try three more years of history and a different tier. A colleague says the diagnostic sequence has a fifth step, expectation mismatch, correct only after the four cheaper causes are ruled out, and that naming it stops an afternoon of tuning toward an output that was never available.

**Which TWO statements are correct?**

- A. The four cheaper causes have been ruled out, so this is an expectation mismatch: an exact future figure is something the tool cannot supply, and more history or another tier will not create it.
- B. The most likely remaining cause is under-specification, so she should restate the request with the exact-rupee requirement in capitals and a longer list of historical constraints.
- C. The fix is to the task: ask for a range with stated assumptions, or an adjustable driver model she can change and re-run.
- D. The most likely remaining cause is a stale data source, so she should rerun with three more years of history and expect the forecast error to fall to zero over time.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Treasury analyst ek hafte se AI se agli quarter ki export sales "exact rupee tak" forecast karwana chahti. Log mein kya rule out hua: Prompt — role, context, task, constraints, format cover. Session length — har koshish fresh chat mein. Feature aur model — totals historical data par code execution se; top tier bhi try, farq nahi. Configuration — standing instructions aur data source check, current. Result: forecast har quarter actual se alag raqam se farq karta. Wo teen saal aur history aur doosra tier try karna chahti. Colleague: diagnostic sequence ka paanchwan step expectation mismatch hai, sirf chaar saste causes rule out hone ke baad sahi.

**Sawal:** Kaunse DO bayan sahi hain?

**Options ka matlab:**

- **A** — Chaar saste causes rule out ho chuke, to yeh expectation mismatch hai: exact future figure tool de hi nahi sakta, aur zyada history ya doosra tier isay paida nahi karega.
- **B** — Baaqi sab se mumkin wajah under-specification — exact-rupee requirement capitals mein aur lambi constraints list.
- **C** — Fix task mein hai: stated assumptions wali range maango, ya adjustable driver model jise wo badal kar dobara chala sake.
- **D** — Baaqi sab se mumkin wajah stale data source — teen saal aur history se error zero tak girega.

</details>

**Answer:** A, C

- ✅ **A** — Step five is right only after the cheaper causes are ruled out, and here they have been.
- ✅ **C** — Reshape the task into one that fits.
- ❌ **B** — The prompt was checked against its five parts, and emphasis cannot make an exact future number available.
- ❌ **D** — The data source was checked and is current, and no amount of history makes a future exact.

**Yaad rakho:** Chaar sasti wajah rule out, aur sawal hi na-mumkin (exact future): expectation mismatch. Range/driver model maango.

*Grounded in: Workflow Design §12 (expectation mismatch; step 5 exists and is sometimes right; reshape the task: a range with stated assumptions or an adjustable driver model)*

---

### Q95.
A finance team's weekly reporting takes each of four analysts about 45 minutes. An audit finds three frictions. F1: each analyst re-pastes the same background paragraph and definitions into three separate prompts each run. F2: each reformats the output by hand into the same layout. F3: different analysts running the same task get different results, seen only by the reviewer. The team also notes the checks each analyst runs before sending, which differ by person. The audit lead says: consolidate steps first, promote what remains second, and sort each remaining friction by the test of rule, reference or procedure. The audit measured a baseline of 45 minutes; after the changes the team expects 25 minutes. One member wants to build a Skill, a Project and standing instructions all at once.

**Which plan follows the guidance?**

- A. Promote the layout to a Skill and the checks to a standing instruction only for the analyst who complained most, and leave the others' habits as they are.
- B. Consolidate the three prompts sharing one background into one; then promote background to knowledge, layout to a Skill, checks to a standing instruction; then measure against the baseline.
- C. Promote everything at once: background to a standing instruction, layout to Project knowledge, checks to a Skill, then consolidate the prompts later if time allows.
- D. Consolidate the prompts; then promote the background to a Skill, the layout to a standing instruction, and the checks to Project knowledge.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Finance team ki weekly reporting chaar analysts ko ~45 minute leti. Audit mein teen frictions: F1 — har analyst har run mein same background paragraph aur definitions teen alag prompts mein paste karta. F2 — har ek output haath se same layout mein reformat karta. F3 — alag analysts ko same task par alag results, sirf reviewer ko dikhte. Team yeh bhi note karti har analyst bhejne se pehle jo checks chalata wo har insaan ke alag. Audit lead: pehle steps consolidate, phir jo bache promote, aur har bachi friction ko rule, reference ya procedure test se baanto. Baseline 45 minute naapa; changes ke baad 25 expected. Ek member sab ek saath banana chahta.

**Sawal:** Kaunsa plan guidance follow karta hai?

**Options ka matlab:**

- **A** — Layout Skill mein aur checks standing instruction mein, sirf us analyst ke liye jisne sab se zyada complain kiya.
- **B** — Ek background share karne wale teen prompts ko ek mein consolidate karo; phir background knowledge mein, layout Skill mein, checks standing instruction mein promote karo; phir baseline se naapo.
- **C** — Sab ek saath promote: background standing instruction, layout Project knowledge, checks Skill; prompts baad mein consolidate.
- **D** — Prompts consolidate; phir background Skill mein, layout standing instruction mein, checks Project knowledge mein.

</details>

**Answer:** B

- ✅ **B** — Consolidation reduces the number of steps and promotion reduces the cost of the steps that remain; do them in that order and sort by rule, reference or procedure.
- ❌ **A** — Variance is fixed by a shared home that every analyst uses, not by fixing one person.
- ❌ **C** — Promoting steps you were about to merge away is wasted work, and the homes are swapped.
- ❌ **D** — A layout is a procedure (Skill), a check a rule (instruction), and background a reference (knowledge).

**Yaad rakho:** Pehle steps jodo, phir promote: background = knowledge, layout = Skill, check = instruction.

*Grounded in: Workflow Design §14-16 (rule, reference or procedure; friction: repetition, correction, variance; consolidate first, then promote; measure the baseline first)*

---

### Q96.
A regional office redesigned its monthly compliance-return workflow with an assistant three months ago. The manager wants to tell head office it "saves a lot of time". The team never timed the old process; three staff recall 60, 90 and 120 minutes. The old process is still documented and could be run again. The return goes to a regulator and an error carries a penalty. A director asks for a defensible statement and for evidence the new way is better on the metric that matters. Five statements are proposed about how to get the evidence. E1: "A baseline cannot be rebuilt afterwards, because estimates of the old way flatter the new one." E2: "Average the three recollections as the baseline of 90 minutes." E3: "Run old and new together for two or three cycles and measure time, revision rounds and manual steps." E4: "For a compliance output the metric to judge is accuracy, not time." E5: "The parallel run buys evidence, a fallback and the agreement of the people whose work changed."

**Which statement is INCORRECT?**

- A. E2: averaging three recollections gives a defensible baseline of 90 minutes, since the people who did the work are the best available witnesses of how long it took.
- B. E4: for a compliance or finance output the metric to optimise and judge is accuracy, since one wrong figure costs more than an hour saved.
- C. E3: running old and new together for two or three cycles and measuring time, revision rounds and manual steps is the right evidence.
- D. E1: a baseline cannot be rebuilt afterwards, since the estimate of the old way will flatter the new one.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Regional office ne teen mahine pehle AI ke saath monthly compliance-return workflow redesign kiya. Manager head office ko "bohat waqt bachta" batana chahta. Purana process kabhi time nahi hua; teen staff ko 60, 90, 120 minute yaad. Purana process documented, dobara chal sakta. Return regulator ko jaata, error par penalty. Director defensible bayan aur us metric par saboot chahta jo matter karta. Paanch bayan: E1 "baseline baad mein dobara nahi banti, kyunke purane tareeqe ke andaaze naye ko achha dikhate." E2 "teen yaadon ka average 90 minute baseline." E3 "do-teen cycles purana aur naya saath chalao, time, revision rounds, manual steps naapo." E4 "compliance output ke liye judge karne wala metric accuracy hai, time nahi." E5 "parallel run evidence, fallback aur jin ka kaam badla unki agreement deta."

**Sawal:** Kaunsa bayan INCORRECT hai?

**Options ka matlab:**

- **A** — E2 — teen yaadon ka average defensible 90-minute baseline, kaam karne wale behtareen gawah.
- **B** — E4 — compliance/finance output ke liye optimise aur judge karne ka metric accuracy, kyunke ek ghalat figure ek ghante ki bachat se mehnga.
- **C** — E3 — do-teen cycles purana aur naya saath chala kar time, revision rounds, manual steps naapna sahi evidence.
- **D** — E1 — baseline baad mein dobara nahi ban sakti, purane tareeqe ka andaaza naye ko achha dikhayega.

</details>

**Answer:** A

- ✅ **A** — Recollections flatter the new process, and a baseline cannot be rebuilt afterwards.
- ❌ **B** — This is correct.
- ❌ **C** — This is correct.
- ❌ **D** — This is correct.

**Yaad rakho:** Yaad se baseline nahi; parallel run karo aur compliance mein accuracy dekho.

*Grounded in: Workflow Design §16 (measure the before; baseline can't be reconstructed; choose the metric that matches why the work mattered; parallel run)*

---

### Q97. *(Select TWO — all-or-nothing)*
A team lead tells reviewers that their "not quite right" reactions must become instructions naming what to change and which part of the setup controls it (the prompt, the instruction, the knowledge, or a saved procedure). She collects five reactions from a week. R1: "It is too generic." R2: "The tone is wrong in every draft." R3: "It is using old data." R4: "It just doesn't feel right." R5: "Something is off with the format again." A colleague says if you cannot name the lever, the critique is still a reaction. The lead asks the team to translate each reaction, and finds that two of the five cannot yet be translated, because nobody has said what would have to be present for the output to be right.

**Which TWO reactions are still reactions?**

- A. R4, 'It just doesn't feel right': it names how the output feels, not what to change, so the next attempt will be a guess that looks like a revision.
- B. R5, 'Something is off with the format again': it names no specific format flaw and no lever, and the word 'again' points to a repeated flaw that should be promoted once named.
- C. R1, 'It is too generic': it translates to naming the audience and the one action wanted, which is a prompt lever, so it is already an instruction in waiting.
- D. R3, 'It is using old data': it translates to replacing the source document in the knowledge base, so the lever is clear and the reaction can be acted on.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Team lead reviewers se kehti unke "not quite right" reactions instructions banein jo batayein kya badalna aur setup ka kaunsa hissa (prompt, instruction, knowledge, saved procedure) isay control karta. Hafte ke paanch reactions: R1 "bohat generic". R2 "har draft mein tone ghalat". R3 "purana data use kar raha". R4 "bas theek nahi lag raha". R5 "format mein phir kuch gadbad". Colleague: agar lever naam nahi kar sakte to critique abhi reaction hai. Lead dekhti paanch mein se do abhi translate nahi ho sakte, kyunke kisi ne nahi bataya output sahi hone ke liye kya maujood hona chahiye.

**Sawal:** Kaunse DO abhi bhi sirf reactions hain?

**Options ka matlab:**

- **A** — R4 "bas theek nahi lag raha" — output kaisa mehsoos hota batata, kya badalna nahi; agli koshish revision jaisi dikhne wali guess hogi.
- **B** — R5 "format mein phir kuch gadbad" — koi specific format flaw ya lever naam nahi karta, aur "phir" dohrati ghalti ki taraf ishara jo naam hone par promote honi chahiye.
- **C** — R1 "bohat generic" — audience aur ek chahiye wala action naam karne mein translate hota (prompt lever), instruction banne ko tayyar.
- **D** — R3 "purana data" — knowledge base mein source document badalne mein translate, lever saaf.

</details>

**Answer:** A, B

- ✅ **A** — If you cannot name the lever, the critique is still a reaction.
- ✅ **B** — It has no lever yet; once the flaw is named, a repeated one belongs in configuration.
- ❌ **C** — It can be turned into an instruction immediately, pulling the prompt lever.
- ❌ **D** — The lever is the knowledge; it can be acted on at once.

**Yaad rakho:** Lever na naam ho to shikayat abhi bhi sirf reaction hai: 'theek nahi lag raha' aur 'format phir ghalat'.

*Grounded in: Workflow Design §13 (turn a reaction into an instruction; what would have to be present, which part of the setup controls it; if you cannot name the lever it is still a reaction) and §14*

---

### Q98.
An analytics lead builds the business case for a redesigned weekly-report workflow. Facts: 4 analysts; each used to spend 50 minutes a week and now spends 20; 48 working weeks a year; a named reviewer spends 15 minutes a week in the gate; the subscription costs PKR 60,000 a year; one analyst hour costs PKR 1,800. A parallel run of two cycles showed accuracy unchanged; the baseline was measured before the change. She wants the statement of net annual value that would survive a budget review, and the hours must be computed: gross saving = 30 x 4 x 48 minutes = 5,760 minutes = 96 hours; gate time = 15 x 48 minutes = 720 minutes = 12 hours. Four statements are offered.

**Which statement is correct?**

- A. Net saving of 84 hours (96 minus 12), about PKR 151,200 less the PKR 60,000 subscription, leaving roughly PKR 91,200, with the surviving risk named.
- B. A 60% reduction in report time, worth about PKR 100,000, presented without hours or cost, since a proportion travels across teams and avoids disputes about hours.
- C. Net saving of 96 hours, worth about PKR 172,800 less the PKR 60,000 subscription, leaving roughly PKR 112,800, with gate time ignored because the reviewer existed before the redesign.
- D. Net saving of 84 hours, worth about PKR 151,200, with no further deduction and no mention of risk, since subscription costs are an overhead paid whether or not the workflow is kept.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Analytics lead redesigned weekly-report workflow ka business case bana raha. Facts: 4 analysts; har ek pehle 50 minute/hafta, ab 20; saal ke 48 working weeks; named reviewer gate mein har hafte 15 minute; subscription PKR 60,000/saal; ek analyst ghanta PKR 1,800. Do cycles ke parallel run mein accuracy same; baseline change se pehle naapa. Hisaab diya hua: gross bachat = 30 × 4 × 48 minute = 5,760 minute = 96 ghante; gate time = 15 × 48 = 720 minute = 12 ghante. Budget review mein tikne wala net annual value bayan chahiye.

**Sawal:** Kaunsa bayan sahi hai?

**Options ka matlab:**

- **A** — Net 84 ghante (96 minus 12), ~PKR 151,200 minus PKR 60,000 subscription = ~PKR 91,200, aur bacha hua risk naam karke.
- **B** — 60% kam report time, ~PKR 100,000, bina ghanton ya cost ke.
- **C** — Net 96 ghante, ~PKR 172,800 minus 60,000 = ~112,800, gate time ignore kyunke reviewer pehle bhi tha.
- **D** — Net 84 ghante, ~PKR 151,200, koi aur deduction nahi aur risk ka zikr nahi — subscription overhead hai.

</details>

**Answer:** A

- ✅ **A** — 84 x 1,800 = 151,200; minus 60,000 = 91,200; cost includes gate time and tool; the surviving risk is stated.
- ❌ **B** — A percentage without volume, cost or risk cannot survive a budget review.
- ❌ **C** — The gate is part of the redesigned workflow's cost.
- ❌ **D** — The tool cost is part of the case, and hiding the residual risk stops it being believed.

**Yaad rakho:** 84 ghante x 1,800 = 151,200; subscription 60,000 ghata kar 91,200; aur bacha hua risk.

*Grounded in: Workflow Design §16 (be able to answer what it costs; saving = baseline x frequency x people; cost includes human time in the kept gates and the tool; name the surviving risk) and §3*

---

### Q99.
A finance team ran a payment-reminder agent twice by hand and both runs looked good. They want to schedule it weekly on a cloud clock and let it send reminders directly to customers without approval. The agent's tools include a cloud connector to the accounts system and a local spreadsheet reached through a desktop bridge. Over the last 12 scheduled runs of a different reporting job, the team's experience is: 11 "completed" and 1 failed loudly; a later audit found that in 3 of the 11 completed runs a section was empty or a figure wrong. A colleague states five principles. G1: "Start with reporting, then graduate carefully." G2: "A schedule is device-independent only when every tool it needs is reachable with your devices off." G3: "A run that finished is not the same as a run that worked." G4: "Grade the rate across many runs, and read which failed before how many." G5: "Two clean manual runs are enough evidence to turn on unattended sending, since sending is a small extension of drafting."

**Which principle is INCORRECT?**

- A. G2: because the local spreadsheet is reached through a bridge, the schedule is device-independent only if that tool is reachable when the devices are off.
- B. G5: two watched runs are the weakest evidence, sending is irreversible, and drafting quality says nothing about an unreviewed send.
- C. G1: start with a report-only mode that a person reviews and graduate to sending only when the runs have earned it.
- D. G4: judge across many runs, reading which items failed and how badly before counting how many, since 3 wrong of 11 completed runs is a serious rate.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Finance team ne payment-reminder agent do dafa haath se chalaya, dono achhe. Ab weekly cloud clock par schedule karke bina approval seedha customers ko reminders bhejna chahte. Tools: accounts system ka cloud connector aur desktop bridge se local spreadsheet. Ek doosre reporting job ke pichle 12 scheduled runs: 11 "completed", 1 zor se fail; baad ke audit mein 11 completed mein se 3 mein ek section khaali ya figure ghalat. Colleague paanch principles: G1 "reporting se shuru, dhyan se graduate." G2 "schedule device-independent tabhi jab har zaroori tool devices band hone par bhi pahunch mein ho." G3 "khatam hua run kaam kiya hua run nahi." G4 "bohat runs par rate grade karo, pehle parho kaunse fail phir kitne." G5 "do clean manual runs unattended sending on karne ke liye kaafi, sending drafting ka chhota izafa."

**Sawal:** Kaunsa principle INCORRECT hai? (Har option principle ko uske sahi matlab ke saath samjhata hai — jo principle ghalat tha wo chuno.)

**Options ka matlab:**

- **A** — G2 — local spreadsheet bridge se aati, to schedule device-independent tabhi jab devices band hone par wo tool pahunch mein ho.
- **B** — G5 — do dekhe hue runs sab se kamzor evidence, sending irreversible, aur drafting quality bina review ke send ke baare mein kuch nahi batati.
- **C** — G1 — insaan ke review wale report-only mode se shuru, sending tak tab graduate jab runs ne haq kamaya.
- **D** — G4 — kai runs par judge karo, pehle parho kaunse items kitne bure fail hue phir gino; 11 mein 3 ghalat serious rate hai.

</details>

**Answer:** B

- ✅ **B** — Demos are the weakest evidence, and the send step is a different, binding step.
- ❌ **A** — This is correct.
- ❌ **C** — This is correct.
- ❌ **D** — This is correct.

**Yaad rakho:** Do achhi runs saboot nahi; pehle sirf report, kai runs par rate dekho, phir bhejne do.

*Grounded in: General Agents on the Web §9 and Appendix E (start with reporting; ran is not worked; grade the rate not the run; read which failed before how many; demos are the weakest evidence)*

---

### Q100.
A team's Project has three problems in a month. Problem 1: every campaign brief comes back without the target segment, and the analyst corrects it by hand each time. Problem 2: reports must always follow a fixed order (cover note, table, exceptions, sign-off) and analysts rebuild the order from memory. Problem 3: quotes use last year's supplier prices, held in the Project's knowledge base. Problem 4: "the company brand voice guide" is attached by hand to each chat. A colleague notes that a fix will be needed again by someone else, so it belongs in configuration, and that the test is whether the fix is a rule (a limit that always applies), a reference (material the work must read) or a procedure (a sequence of steps). The team offers four assignments of Problems 1 to 4 to homes in order, using standing instruction, Skill, and knowledge base.

**Which assignment is correct?**

- A. Problem 1 standing instruction; Problem 2 knowledge base; Problem 3 Skill; Problem 4 standing instruction.
- B. Problem 1 knowledge base; Problem 2 Skill; Problem 3 standing instruction; Problem 4 Skill.
- C. Problem 1 standing instruction; Problem 2 Skill; Problem 3 replace the file in the knowledge base; Problem 4 knowledge base.
- D. Problem 1 Skill; Problem 2 standing instruction; Problem 3 replace the file in the knowledge base; Problem 4 knowledge base.

<details>
<summary>🗣️ <b>Roman Urdu mein samjho</b> (sawal ka matlab — jawab yahan nahi hai)</summary>

**Scenario:** Team ke Project mein mahine mein masle: 1 — har campaign brief target segment ke baghair aata, analyst har dafa haath se theek karta. 2 — reports ko hamesha fixed order (cover note, table, exceptions, sign-off) follow karna, analysts yaad se order banate. 3 — quotes pichle saal ki supplier prices use karte jo Project ki knowledge base mein hain. 4 — "company brand voice guide" har chat mein haath se attach hota. Colleague: jo fix kisi aur ko bhi dobara chahiye wo configuration mein jaata; test: fix rule hai (hamesha lagu hadd), reference (material jo kaam parhe), ya procedure (steps ka sequence). Chaar assignments (standing instruction, Skill, knowledge base).

**Sawal:** Problems 1–4 ki kaunsi assignment sahi hai?

**Options ka matlab:**

- **A** — 1 standing instruction; 2 knowledge base; 3 Skill; 4 standing instruction.
- **B** — 1 knowledge base; 2 Skill; 3 standing instruction; 4 Skill.
- **C** — 1 standing instruction; 2 Skill; 3 knowledge base mein file badlo; 4 knowledge base.
- **D** — 1 Skill; 2 standing instruction; 3 knowledge base mein file badlo; 4 knowledge base.

</details>

**Answer:** C

- ✅ **C** — A rule goes to standing instructions, a procedure to a Skill, and references to the knowledge base.
- ❌ **A** — Stale prices are fixed by replacing the reference, and the brand voice guide is reference material.
- ❌ **B** — A rule is not a reference, prices are references, and a voice guide is reference material rather than a procedure.
- ❌ **D** — The target-segment line is a rule, and a fixed sequence is a procedure; a one-line instruction would lose the order.

**Yaad rakho:** Rule = standing instruction, reference = knowledge (purani file badlo), tarteeb-war qadam = Skill.

*Grounded in: Workflow Design §14 (rule, reference or procedure; promotion; memory is per-user and best-effort) and §13*

---

## Answer Key (jaldi check ke liye)

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
| ---: | :--- | ---: | :--- | ---: | :--- | ---: | :--- | ---: | :--- |
| 1 | D | 21 | D | 41 | B | 61 | B | 81 | D |
| 2 | C | 22 | AC | 42 | A | 62 | CD | 82 | BD |
| 3 | A | 23 | A | 43 | D | 63 | D | 83 | D |
| 4 | B | 24 | C | 44 | AD | 64 | A | 84 | B |
| 5 | AD | 25 | D | 45 | D | 65 | C | 85 | AB |
| 6 | A | 26 | B | 46 | A | 66 | C | 86 | BD |
| 7 | CD | 27 | A | 47 | D | 67 | A | 87 | C |
| 8 | C | 28 | A | 48 | A | 68 | D | 88 | A |
| 9 | C | 29 | A | 49 | C | 69 | C | 89 | A |
| 10 | B | 30 | BC | 50 | BC | 70 | C | 90 | AB |
| 11 | C | 31 | C | 51 | B | 71 | A | 91 | C |
| 12 | D | 32 | B | 52 | C | 72 | C | 92 | C |
| 13 | D | 33 | B | 53 | A | 73 | B | 93 | B |
| 14 | AB | 34 | D | 54 | BC | 74 | B | 94 | AC |
| 15 | B | 35 | A | 55 | D | 75 | AC | 95 | B |
| 16 | BC | 36 | D | 56 | A | 76 | BD | 96 | A |
| 17 | A | 37 | C | 57 | CD | 77 | BD | 97 | AB |
| 18 | B | 38 | D | 58 | AD | 78 | C | 98 | A |
| 19 | AC | 39 | D | 59 | AD | 79 | D | 99 | B |
| 20 | B | 40 | B | 60 | B | 80 | D | 100 | C |

---

## Level 3 Cheat-Sheet — sawal ki shakal aur pivot

| Sawal ki shakal | Kya karna hai |
| --- | --- |
| **"EXCEPT / NOT / INCORRECT / FALSE"** | Teen options course ke mutabiq sahi hain; ek ulta. Har option ko chhote se course-fact se jaancho. |
| **Mapping (S1..S5 -> jagah)** | Har item ki apni jagah (rule/reference/procedure, connector/browser/computer use, Manual/Auto/Skip, tier). Ek hi ghalat item poora option ghalat kar deta hai. |
| **Ordering** | Har qadam sahi hota hai; tarteeb ka usool: eligibility pehle, sasta check pehle, facts likho phir report, source pehle. |
| **Hisaab** | Khud compute karo: 800 x 820 = 656,000; 96 - 12 = 84 ghante; 84 x 1,800 = 151,200. Andaza nahi. |
| **"Kaunsi TWO"** | Dono sahi chunne hain; ek sahi + ek doosre jaisa lagne wala = zero. |

| Jahan Level 3 phansata hai | Pivot |
| --- | --- |
| Known answer sahi lagta hai | Alag zariye se? naye raste (policy badalne ke baad) ko chhooti hai? |
| Do vendors / do runs ka agreement | Same brief aur same file = same omission; checker ko source dikhaya? |
| Total sahi, ranking ghalat | Grouping/inputs (kaunsi file, kaunse naam) reality question se pakdo. |
| "Log mein dikhta hai" | Tool ne kya *event* dikhaya? Hold nahi, ERP call nahi = dawa saboot nahi. |
| Gate ka wording | Kaun (role), kya (khaas risk), kab (sakht hone se pehle); ek bhi kam = gate nahi. |
| Sample plan | Jo reviewer tak pahunchta hai wo kis ne chuna? Approved bhi, threshold ke qareeb bhi. |
| Enterprise / sandbox / incognito | Control ka dhancha, execution ki hadd, memory ki hadd: teeno ijazat nahi. |
| Residual risk / Evidence | Control theek chalne ke baad jo bacha; 'koi nahi' kabhi jawab nahi. |
| Timing | Pehla shak, wajah nahi; 'pehle chalta tha' = config purani ya kaam ki shakal badli. |

---

## Note

Yeh file PCAO-F Panaversity exam ke liye original self-test hai; koi asli exam item shamil nahi. Product-specific baaton
ke liye har course ki "checked on" tareekh (Aug–Sep 2026) dekho aur booking se pehle official CCAO-F guide download karo.

[⬅ PCAO-F Index](README.md) · [`pcaofcombatlevel1.md`](pcaofcombatlevel1.md) · [`pcaofcombatlevel2.md`](pcaofcombatlevel2.md)
