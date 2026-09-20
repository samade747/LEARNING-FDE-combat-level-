# PCAO-F / CCAO-F — Combat Level 2: 100-Question "Look-Alike Options" Scenario Bank (`pcaofcombatlevel2.md`)

*Yeh **Level 2** hai: [`pcaofcombatlevel1.md`](pcaofcombatlevel1.md) ke baad ek aur dhakka. Level 1 mein galat options
"asli principle, ghalat jagah" the. Level 2 mein **chaaron options ek hi saanche ke hain**: wahi lafz, wahi lambai, wahi
kaam karne wale actions, aur farq sirf ek jagah (kaun / kab / kis order mein / kis scope par). Sawal 100, har ek ke 4
options, blueprint ke weights wahi. Yeh jaan-bujh kar real exam se kaafi mushkil hai (calibrated nahi hai).*

**Source grounding:** Zia Tutor AI MCP ka corpus **generation 75** (retrieved 2026-09-20): PCAO-F page + Governance, AI
Fluency, Workflow Design & Diagnosis, Just Delegate It, What AI Actually Is, ChatGPT & Claude Quick Reference, Skills &
Connectors, AI Prompting in 2026, General Agents on the Web, Code You Never Write. Har sawal ke neeche *Grounded in* line
hai. Sab scenarios original hain; koi asli exam item ya guide ka sample sawal nahi.

## Level 1 se kya badla

| # | Level 2 ki design choice | Yeh kyun mushkil hai |
| ---: | --- | --- |
| 1 | **Look-alike options.** Chaaron options ek jaise jumle hain jo dono principles ka lafz istemal karte hain; sirf ek "pivot" (jaise gate ka *kab*, ya kaunsa source *independent* hai) farq karta hai. | "Sahi lagne wala" option nahi chunna, *deciding fact* dhoondna parta hai. |
| 2 | **Ordering / sequence sawal.** Kai sawalon mein options wahi qadam hain jo alag tarteeb mein rakhe gaye hain (Identify-Trace-Challenge-Decide, first-hour procedure, diagnostic ladder, eligibility→ownership→implementation). | Tarteeb ghalat karna asaan hai, kyunke har qadam khud sahi hai. |
| 3 | **Stacked principles.** Ek sawal mein do ya teen principles milte hain (halo delegation + self-set gate + unstaffed gate; known-answer + independence + naya raasta). | Ek principle pehchan kar jawab nahi milta. |
| 4 | **Ghalat premise wale dawe.** Manager ya colleague ka ek "munasib lagne wala" dawa stem mein hota hai jo course ke khilaf hai (jaise "same brief, do vendors = independent", "sandbox = ijazat"). | Stem ka confident lehja tumhein bhatkata hai. |
| 5 | **Answer key aur lambai balanced.** Single-answer sawalon mein A/B/C/D lagbhag barabar hain, aur correct option ki length wrong options ke qareeb hai (sab se lamba ~58% sawalon mein, aksar sirf 1-6 alfaaz ke farq se; pehli files mein ~95% tha). | Exam-technique se nahi, ilm se jawab do. |
| 6 | **18 "Select TWO — all-or-nothing"** sawal (CCAO-F multiple-response format). | Sirf ek sahi chunna = zero. |
| 7 | **Har option ka apna "kyun galat"** + Roman Urdu "Yaad rakho". | Review se sikhna. |

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

- **Waqt:** ≈ **3 minute per sawal** (stems lambe hain aur options bahut milte-julte). Do baithakon mein 50–50, har baithak ≈ 2.5 ghante.
  Pehle Level 1 kar lo; Level 2 tab jab Level 1 mein raw ≥ 70% ho.
- **Har sawal ka tareeqa:** pehle stem mein se *deciding fact* nikalo (kaun jawabdeh, kab reviewer parhta, kaunsa source
  independent, kya badla), phir dekho chaaron options mein wo fact kahan farq karta hai. Red herrings (tareef, deadline,
  approval rate) ko chhor do.
- **Score (heuristic, official nahi):** yeh bank real exam se zyada mushkil hai. Raw **≥ 60%** = exam level ya upar. **45–60%**
  = qareeb. **< 45%** = *Grounded in* section dobara parho. Official pass **720 / 1000 scaled** (72% nahi), koi per-domain minimum nahi.
- **Har ghalti par:** (1) mera chuna hua option kaunsa principle tha jo maine ghalat jagah lagaya? (2) pivot kya tha? (3) file ke
  aakhir ka "Look-alike traps" cheat-sheet dekho.

---

## Domain 2 — Output Evaluation and Validation (21% — 21 questions)

### Q1.
Nadia, a finance associate at a Lahore textile exporter, has Claude write and run code that totals monthly export rebates from an ERP export. She applies the rule "test on one answer you already know": March's rebate total, which she knows to be PKR 18.42 million, is reproduced to the rupee, and the row counts match (412 in, 412 out). The 18.42 million figure comes from the finance team's March close report, which was produced by exporting the same ERP rebate table to a spreadsheet and summing it with a macro. She also gave the identical brief and file to an assistant from another vendor, and it returned the same total. Head office wants April to June filed unattended on Friday. The rebate policy changed on 1 April: a 2% cap per shipment is now applied, and the ERP export gained a nullable "capped" column that is empty for every March row.

**Which next step best follows the verification method?**

- A. Repeat the March check with a seeded fault placed in the empty capped column, and run April to June unattended if the fault is caught and the March total still matches.
- B. Treat March as verified because two vendors' assistants and one finance report agree, then run April to June unattended with a row-count comparison on each month's output as the safeguard.
- C. Ask the second vendor's assistant to review the first assistant's code line by line for the cap logic, and run April to June unattended if the review finds no defect in the code.
- D. Obtain a total for one closed post-change month from a source not derived from the ERP table, such as the bank's rebate credit statements, and require the code to reproduce it.

**Answer:** D

- ✅ **D** — The known answer must be independent of the data being tested and must exercise the path that changed; the bank statements do both.
- ❌ **A** — March predates the cap, so the seeded test cannot show that a real capped month reproduces, and the known total is still not independent.
- ❌ **B** — The finance total shares its source with the code, and both assistants read the same brief, so agreement adds little independent evidence.
- ❌ **C** — A second reader of the same brief can share its omissions, and no test has yet exercised the capped rows.

**Yaad rakho:** Known answer tabhi kaam ka jab wo *alag zariye* se aaya ho aur naye raste ko chhoo raha ho.

*Grounded in: Code You Never Write §6 (known-answer test; independent knowledge; cross-model limit); Quick Reference §9*

---

### Q2.
A policy analyst at a Karachi think tank receives a 3,000-word AI-written memo on a customs-duty reform for a ministry briefing tomorrow morning. It contains 14 factual claims. Three of them will be quoted verbatim by the minister (a revenue-loss figure, an effective date, and a statement that the reform is "revenue neutral"); the other eleven are background. The memo's citations all resolve to real pages. The analyst has a little under two hours and wants to follow the verification method she was taught, whose four steps are identify, trace, challenge and decide, with the decision being one of accept, correct, investigate or reject. A colleague suggests tracing all 14 claims to their sources first so that nothing is missed, then deciding which to challenge.

**Which sequence follows the method?**

- A. Pick the claims a mistake would hurt most; open the source and find the supporting sentence and its date; ask whether it has been superseded or is second-hand; then choose accept, correct, investigate or reject.
- B. Open the source for all 14 claims and find each supporting sentence and date; pick the three most consequential and ask whether they have been superseded or are second-hand; then choose accept, correct, investigate or reject.
- C. Pick the three claims a mistake would hurt most; ask whether each has been superseded or is second-hand; open the sources to find the supporting sentence and date; then choose accept, correct, investigate or reject.
- D. Pick the three claims a mistake would hurt most; open the sources and find each supporting sentence and date; choose accept, correct, investigate or reject; then ask whether each has been superseded or is second-hand.

**Answer:** A

- ✅ **A** — Identify comes first so that effort follows the stakes; trace and challenge follow for those claims; the four-way decision comes last.
- ❌ **B** — This traces everything before deciding what matters, which spends the limited time where errors cost least.
- ❌ **C** — Challenge before trace: you cannot say a source is superseded or second-hand until you have opened it and read its date.
- ❌ **D** — The decision must follow the challenge, since whether a claim has been superseded is exactly what settles accept versus investigate.

**Yaad rakho:** Pehle chuno kaunse claim ahem (Identify), phir Trace, phir Challenge, aakhir mein Decide.

*Grounded in: Just Delegate It §10 (Identify, Trace, Challenge, Decide; review thresholds)*

---

### Q3.
A bookkeeper at a freight forwarder reconciles a 1,400-row bank export against the ledger. Claude's code reports 23 mismatches and produces a report that covers 1,381 rows. Its plain-English replay says: "I matched on amount and date within two days, treated debits as negative, and skipped rows I could not read." It does not say how many rows were skipped or which. The bank export includes a footer summary line and a "pending" status column. An assistant from another vendor, given the same brief and file, also reports 23 mismatches and covers the same 1,381 rows. The external audit begins in two days, and the bookkeeper's manager says agreement between two vendors settles it.

**What is the best next check?**

- A. Accept the count, because two assistants from different vendors agree on 23 mismatches and on the same 1,381 covered rows, which is independent confirmation of both numbers.
- B. Ask the second assistant to explain in plain English how it handled duplicates and pending rows, and accept if that procedure matches the first assistant's account.
- C. Ask the first assistant to rate its confidence in the 23 mismatches, then rerun with pending rows removed and compare the two mismatch counts.
- D. Ask each assistant to list, by row number, the 19 rows it excluded and the rule that excluded them, then check that none is a real transaction such as a pending item.

**Answer:** D

- ✅ **D** — Rows in against rows out is a reality question; the missing 19 could hide real items, and both tools may share the same skipping rule.
- ❌ **A** — Agreement on a shared brief does not explain the missing rows; both may drop the same footer, pending or unreadable lines.
- ❌ **B** — Matching procedures in words do not show which rows were dropped; the replay omitted exactly that count.
- ❌ **C** — A self-rated confidence is not evidence, and removing pending rows changes the question rather than accounting for the 19 rows.

**Yaad rakho:** 1,400 andar, 1,381 bahar: 19 rows kahan gayeen? Ye reality question hai.

*Grounded in: Code You Never Write §6 (reality questions: rows in versus rows out; plain-English replay; cross-model limit)*

---

### Q4.
A bank's compliance operations team uses an AI screen that pre-reads 400 transactions a day and drafts a one-line "clear" or "escalate". Reviewers click "approve" on each draft. After three months the approval rate is 98.5%, average review time is nine seconds, and no reviewer has rejected a draft in six weeks. Reviewers see the AI's one-line recommendation and its score but not the customer's transaction history, which sits in another system that needs a separate login. Rejecting a draft requires a supervisor's countersignature. The vendor presents the 98.5% as proof of accuracy, and a director proposes fixes: a mandatory review timer, rotating reviewers weekly, or replacing the reviewers with a second AI.

**Which response best fits the framework's view of review quality?**

- A. Give reviewers the source records, authority to reject without countersignature, one specific risk per alert and time sized to volume; then sample edge cases such as near-threshold and escalated alerts.
- B. Add a mandatory 60-second timer and a monthly warning to reviewers whose approval rate exceeds 95%, since slower and monitored review restores diligence on each alert.
- C. Replace the reviewers with a second AI screen that is trained on past rejections, and audit its rejection rate each quarter instead of reviewing individual alerts.
- D. Rotate reviewers weekly and publish approval rates by reviewer, since visibility and fresh eyes stop any one reviewer becoming complacent about the AI's drafts.

**Answer:** A

- ✅ **A** — Good review has the source material, time, a specific risk, authority to reject and a position before the outcome is hard to reverse.
- ❌ **B** — A timer without source access or authority to reject only slows a review that cannot catch anything.
- ❌ **C** — It swaps one unexamined control for another and removes the position before the outcome is hard to reverse.
- ❌ **D** — Rotation and league tables leave the same gaps: no source records, no authority to reject, no specific risk to look for.

**Yaad rakho:** Approval rate reviewer ka rawaiya batati hai, model ki sehat nahi. Gate ko source, waqt, ikhtiyar do.

*Grounded in: Governance A.1 (review quality matters more than volume; sample the edge cases); Workflow Design §7 (unstaffed gate)*

---

### Q5.
The CFO of a Faisalabad chemicals distributor asks Claude to write and run code on an invoice file to compute quarterly late-fee revenue for the board pack. Claude shows the code, which defines rate = 0.018 once and applies it to every overdue invoice, and reports PKR 4.31 million. The CFO recalls that the late-fee schedule rose to 2.1% for invoices issued from 15 February, and that last quarter's figure was PKR 3.9 million. The number "looks the right size". Claude's plain-English replay says it "applies the late-fee rate to overdue balances". The analyst notes that the code was actually run and shown, so the figure is computed, not written, and the board pack goes to print tomorrow.

**What is the right next step?**

- A. Average 1.8% and 2.1% for the quarter and rerun, then compare the result with last quarter's PKR 3.9 million for reasonableness before printing.
- B. Accept the figure, because the code was run and shown, and add a footnote to the board pack stating the flat 1.8% rate assumption so readers can judge it.
- C. Ask Claude to explain the calculation in plain English and accept the figure if the explanation mentions both the old and new rates, since the replay would reveal a wrong rule.
- D. Recompute using the rate effective on each invoice's issue date from the schedule file, showing the rate lookup and per-row counts, then test one closed month against the ledger.

**Answer:** D

- ✅ **D** — The run was exact but used one rate; check the inputs (right rows, right rate), then test against a known answer.
- ❌ **A** — An averaged rate is a new guess, and comparing with last quarter tests plausibility, not correctness.
- ❌ **B** — A footnote discloses a wrong input instead of correcting it; being computed does not make the rate right.
- ❌ **C** — The code applies one rate; a replay that mentions two would describe something the code does not do, so the result must be checked.

**Yaad rakho:** Run exact hai magar rate ek hi lagi. Inputs (kaunsi rate, kaunsi rows) check karo, sirf sum nahi.

*Grounded in: AI Fluency §6.3 (numbers rule; check the inputs, not the sum); Workflow Design §3; Code You Never Write §6*

---

### Q6.
A compliance manager at an insurer wants independence for a Claude-drafted summary of a 90-page reinsurance treaty that the board will rely on. She opens a chat with an assistant from a different company and pastes in Claude's summary with the instruction: "Is this summary accurate and complete? List any errors." The second assistant replies that the summary is "clear, internally consistent and accurate", noting two small wording improvements. It has not been given the treaty. The manager reasons that a different vendor's model does not share the first model's blind spots, so the check is cross-model, and that the score is only a progress signal anyway. The board meets in three days.

**What is the flaw in this verification, and the best correction?**

- A. The checker never saw the source: give it the treaty and criteria, ask for a section-cited list of discrepancies, and have a person verify the claims the board relies on.
- B. The flaw is that only one vendor was used; add a third vendor's assistant that also receives just the summary, and accept if two of the three call it accurate.
- C. The flaw is the wording of the instruction; ask the second assistant to score the summary out of ten on named criteria, and accept it above eight.
- D. The second assistant is from a different company, so the check is sound; the only correction is to run it twice and take the majority answer to smooth out randomness.

**Answer:** A

- ✅ **A** — A different company is the right kind of check only if it compares the summary against the source; consistency with itself proves little.
- ❌ **B** — More checkers of the summary alone still test its coherence, not its fidelity to the treaty.
- ❌ **C** — A named-criteria score is a better prompt but still a score from a checker without the source, not proof.
- ❌ **D** — Repeating a check that never sees the treaty repeats the same blind spot.

**Yaad rakho:** Checker ko source dikhao, sirf summary nahi. Different company + source = asli cross-check.

*Grounded in: AI Prompting 2026 §13 (models checking models: different company; the score is a progress signal); Code You Never Write §6*

---

### Q7.
A junior consultant at a Dubai advisory firm uses Claude to draft client strategy memos. Her manager, pleased that "every memo has come out well", asks whether the workflow is worth keeping. She logs one memo honestly. Writing it herself would take about 35 minutes. With Claude she spends 12 minutes steering across five exchanges, 14 minutes editing the draft, and 6 minutes checking figures and sources against the client file: 32 minutes in total. She notes that she now rewrites more of each draft than she would have written herself, and that the manager reads only the final memo. A colleague suggests writing a longer standing instruction; another suggests a stronger model tier; a third says the result is what counts.

**Which conclusion follows from process discernment?**

- A. The workflow is a clear success, because every memo came out well and the manager's satisfaction with the final result is what discernment is meant to judge.
- B. The process is sound but the model is too weak, so switching to the highest tier should reduce the editing time enough to justify keeping the workflow as designed.
- C. The process is sound but under-described, so a longer standing instruction that specifies audience, tone and structure will bring the 32 minutes down without changing who does what.
- D. Counted honestly it saves about three minutes with heavy rewriting: change the split, so Claude drafts sections while she writes the analysis, or take the memo back.

**Answer:** D

- ✅ **D** — Twenty minutes that saves fifteen is a loss counted as a win; when better description isn't enough, the delegation itself is wrong.
- ❌ **A** — That is product discernment; process discernment asks whether working this way pays off in time and effort.
- ❌ **B** — Escalating the machine is one move, but it does not address that the associate rewrites more than she would have written.
- ❌ **C** — Sometimes better Description is not enough; heavy rewriting suggests the split, not the wording, is the problem.

**Yaad rakho:** Steering + editing + checking ka poora waqt gino. Bachat 3 minute ho to Delegation badlo.

*Grounded in: AI Fluency §5.2 (process discernment: is this way of working paying off; three moves: change the description, change the tool, take the task back)*

---

### Q8.
An FDE at a payroll-software firm asks Claude to write a script that calculates employer pension contributions and a suite of tests for it. All 26 tests pass. Before signing off, she introduces a fault on purpose: she changes the contribution rate constant from 10% to 0% and reruns the suite. All 26 tests still pass. The tests were written by Claude in the same session and mostly assert that the function returns a number, that the number is non-negative, and that the output has two decimal places. Her team lead says that a green suite plus a working demo is the standard for release, and that the fault she introduced was unrealistic. Her team lead adds that the company has released this payroll module to three clients already, that the demo went well, and that the release note is due to the client by Thursday.

**What should she conclude, and do?**

- A. The suite needs more of the same tests, so ask Claude to generate 100 further assertions of the current kind and release once all of them pass on the real rate.
- B. The tests prove almost nothing: a check silent when the code is broken doesn't test the answer, so add hand-worked known-answer cases and confirm the planted fault now fails.
- C. The suite is adequate for release because the planted 0% rate is unrealistic, and the 26 passing assertions cover format, sign and precision, which are the common defects in payroll code.
- D. The suite is fine but the demo is not, so rerun the demo with a wider set of employees and release if every contribution looks plausible to the payroll team.

**Answer:** B

- ✅ **B** — Putting in a fault you know about and seeing whether the check catches it is the test of the test.
- ❌ **A** — More assertions on format and sign add volume, not the ability to catch a wrong rate.
- ❌ **C** — The planted fault is precisely the kind a useful test must catch; format and sign checks cannot see a wrong rate.
- ❌ **D** — Plausibility is not a known answer; a demo does not test the tests.

**Yaad rakho:** Jaan-boojh kar ghalti daalo. Check chup rahe to check kuch bhi verify nahi karta.

*Grounded in: Code You Never Write §6 (put in a fault you know about; mutation-testing idea; never act on a precision-critical number untested)*

---

### Q9.
A legal-aid clinic volunteer asks a search-enabled assistant for the deadline to file an appeal against a rent tribunal order. The assistant answers "30 days from the written order" and quotes a sentence from a government page: "Appeals must be lodged within 30 days of the date of the written order." She opens the link; the sentence is there word for word. The page sits under a heading "Frequently asked questions (archived)", its footer reads "Last updated 2019", and the portal's news section lists a 2025 circular titled "Revised procedure for tribunal orders". The client's intake meeting is in an hour. A colleague says the quote matches exactly, so the claim is verified, and that a citation resolving to the official portal is the gold standard.

**What does the verification method say?**

- A. Accept: the quote matches word for word and the source is the official portal, so the deadline is verified and any later circular would have been surfaced by the search.
- B. Correct: advise the client to file in 30 days as a safe outer limit, since an archived page that gave 30 days is unlikely to have been revised to a longer period.
- C. Investigate: an exact quote shows the page was reported faithfully, not that it is current, so trace to the 2025 circular and current primary text before advising.
- D. Reject: discard the assistant's answer and the search feature for legal deadlines, and advise the client from the volunteer's memory of the usual tribunal timeline.

**Answer:** C

- ✅ **C** — Challenge asks whether the fact changed since the page was written; an archived 2019 page and a 2025 revision mean the evidence is incomplete.
- ❌ **A** — Fidelity to a page is not currency, and search does not guarantee the latest document is the one quoted.
- ❌ **B** — The direction of any change is unknown; guessing it in the client's favour is not verification.
- ❌ **D** — One stale page calls for tracing further, not for abandoning the tool or substituting unverified memory.

**Yaad rakho:** Quote match = page sahi parha gaya. Page abhi bhi durust hai ya nahi, ye alag sawal hai.

*Grounded in: Just Delegate It §10 (a citation is not verification; challenge whether it changed; investigate); AI Prompting 2026 §3 (search drift; quote the sentence)*

---

### Q10.
A university admissions officer asks Claude to draft a scholarship-decision letter, then asks: "Score this letter out of ten and tell me what could be better." Claude proposes a rubric (warmth, clarity, professionalism, brevity), scores the letter 9 out of 10, and suggests two small edits. She applies them and asks again; the score becomes 10. Her supervisor is satisfied that the letter was "independently graded". The letter states a reapplication deadline and the appeals route; neither is on Claude's rubric. The office's actual standard is its decision policy, which the officer has not shared with Claude, and past letters have been challenged over exactly those two items. The officer also mentions that the scholarship panel meets on Monday, that last year's letters were praised for warmth, and that the office has recently changed its email signature.

**Which change most improves the evaluation?**

- A. Ask a fresh Claude chat to re-score the letter on the same four criteria, and average the two scores, since independent runs cancel out the agreeable lean of a single run.
- B. Ask Claude to be harsh and to find fault with the letter, then treat any score below 8 as a failure and above 9 as a pass against the office's policy.
- C. Supply the office's own criteria, including deadline accuracy and the appeals route; score each; ask for the smallest change that would raise each score; allow 'I don't know'.
- D. Keep the rubric but ask for evidence for each score in a sentence, since a justification for each number makes the grade reviewable and therefore independent.

**Answer:** C

- ✅ **C** — A rubric the assistant wrote itself and a bare score invite agreeable answers; named criteria from the real standard do not.
- ❌ **A** — Same model, same self-authored rubric, still no policy criteria; averaging keeps the same blind spot.
- ❌ **B** — Tone instructions change the lean, not the standard; the pass mark is still measured against criteria the office never supplied.
- ❌ **D** — Justifications from the same model are more text to review, not an independent check against the policy.

**Yaad rakho:** Rubric khud AI ka likha ho aur number bina criteria ke: dono khushamad ko dawat dete hain.

*Grounded in: AI Prompting 2026 §6 (score named criteria; the change that would raise each score; 'I don't know' is acceptable); What AI Actually Is Idea 6*

---

### Q11.
An operations lead at a Multan cement company has 80 supplier contracts in a folder. She asks an assistant on its chat interface: "Which of these have a non-standard termination clause?" and attaches the files. The reply lists 9 contracts with a confident paragraph on each, no code block and no row or file counts. She wants the list for a legal review on Thursday, knows from experience that several older contracts use an unusual "notice by registered post only" clause, and worries about missed items. A colleague suggests asking the assistant to "think harder", another to switch to the highest tier, and another to double-check by asking whether it is sure. The contracts are stored in a mix of PDF and scanned formats, and the company's legal adviser is travelling until Wednesday and can only review a shortlist of the flagged contracts.

**What is the best response?**

- A. Ask it to state its method; if it glanced, have it write and run code over all 80 files, list each file's result with counts, and test five contracts she has read.
- B. Switch to the highest tier and repeat the request as written, since a stronger model reads long attachments more thoroughly and is less likely to miss unusual clause wording.
- C. Ask whether it is sure about the list and accept the reply if it confirms, adding a footnote that the list was produced by an assistant for the legal team to review.
- D. Ask it to think harder and re-list, since extended reasoning improves accuracy on long attachments and will surface the missed older contracts without changing the method.

**Answer:** A

- ✅ **A** — Volume, files and precision are code-problem signals; no code block means no code ran.
- ❌ **B** — A stronger model can still glance; the method, not the tier, is the gap.
- ❌ **C** — A confirmation is the same confident voice; a footnote is disclosure, not verification.
- ❌ **D** — Thinking is more prediction; it does not turn a glance into a computation over every file.

**Yaad rakho:** Sirf ek nazar dali ya code chalaya? Volume + files = code problem. Sab 80 files ki list maango.

*Grounded in: Code You Never Write §3-4 (four signals: volume, precision, repetition, files; the tell: no code block, no row counts); §6 (known-answer test)*

---

### Q12.
A property-management firm in Islamabad proves a Claude-based lease-abstraction workflow before rolling it out. The lead follows the proving loop: she picks ten closed leases whose abstracts were done by hand and trusted, asks Claude to reproduce them, and compares. All ten match, including tricky break-clause dates. The firm plans to drop its review sample from 50% to 5%. Later an analyst mentions that three of those ten leases were pasted into the workflow's standing instructions last month as "examples of a good abstract", so that Claude would imitate the format. The other seven were not. The lead says seven of ten is still a strong pass and that the three examples only helped with formatting, and the firm's next intake is commercial leases, which the proving set did not include.

**What does the proving result support?**

- A. An inconclusive result that should be repeated by asking Claude to abstract the same ten leases again, and adopting the 5% sample if the answers are stable across both runs.
- B. Very little yet: three of the ten cases were shown to the assistant with answers, and the clean seven cover only residential leases; re-run on fresh, withheld cases including commercial leases before cutting review.
- C. A strong pass on the seven unseen leases, so cut sampling to 5% for residential work and keep 50% for commercial leases until a similar set has been proved.
- D. A pass on all ten, because the three instruction examples only taught formatting, and an assistant that reproduces break-clause dates has shown the same reliability on any lease.

**Answer:** B

- ✅ **B** — A proving case must be withheld from the assistant, and confidence attaches to similar future work only.
- ❌ **A** — Repeating the same contaminated set tests consistency, not accuracy on new cases.
- ❌ **C** — Seven residential matches are a small set, and the contamination in the other three shows the test setup was not controlled.
- ❌ **D** — Examples with answers in the instructions are exactly what makes a proving case invalid, and reliability does not transfer across lease types.

**Yaad rakho:** Proving case AI se chhupa hona chahiye. Jo example instructions mein daal diya wo test nahi raha.

*Grounded in: Quick Reference §9 (test on old work you already know; passing earns confidence for similar future work; what it does not prove); Governance §8.5*

---

### Q13. *(Select TWO — all-or-nothing)*
A shipping company's legal-operations lead is deciding which of four AI-assisted outputs from this week must have the full verification method and a named person before release. (1) A first-pass tagging of 2,000 incoming vessel emails into five folders, easily moved back, used only by her own team. (2) A draft wire-transfer instruction for a demurrage settlement of USD 480,000 that a finance officer will approve and release on Friday; once the bank executes, the money cannot be recalled. (3) A weekly summary for the executive team of open disputes, read by six executives who can each see the underlying files. (4) A response to a data-protection authority's questionnaire that quotes customer records and will be signed by the general counsel. A colleague argues that item 1 needs the most checking because it has the most volume.

**Which TWO outputs cross a review threshold?**

- A. The executive summary: any content read by six senior people has an audience threshold, so it needs the same named reviewer and four-step check as external documents.
- B. The wire-transfer instruction: irreversible and financially material, so stakes and reversibility are both crossed and a named person must read it before release.
- C. The email tagging: it touches 2,000 items, and volume is a threshold in its own right, so the largest output should get the deepest review before use.
- D. The data-protection response: regulatory exposure and personal data are crossed, and the general counsel's signature makes it a legal communication needing a named reviewer.

**Answer:** B, D

- ✅ **B** — Reversibility and stakes: a payment that cannot be recalled is the classic case for a check before the act.
- ✅ **D** — Regulated or sensitive data and legal communications never go out without a person, however clean the run.
- ❌ **A** — The audience can already see the underlying files and the summary is easily corrected, so no threshold is crossed.
- ❌ **C** — Volume is not one of the four thresholds, and the tagging is reversible, internal and low in stakes.

**Yaad rakho:** Threshold: stakes, reversibility, audience, regulatory exposure. Volume threshold nahi hai.

*Grounded in: Just Delegate It §10 (four review thresholds: stakes, reversibility, audience, regulatory exposure; one is enough; four things that never go out without a person)*

---

### Q14.
A finance team schedules a weekly cloud agent that compiles a supplier-payment exceptions digest. The first run was watched live and looked excellent, and the next eleven all ended with "Completed successfully". A quarterly review of the last six digests finds that two contained a wrong figure: one used last week's exceptions file, one double-counted a supplier merged in the master data. Neither error was visible in the digest's tone or layout. The team lead's plan is to add a second model as a judge that marks each digest PASS or FAIL; in a trial it marks 96% PASS, and the lead proposes treating that as the reliability rate. Another team member argues one demo run plus twelve completions is enough evidence.

**What is the best way to judge reliability here?**

- A. Trust the 96% PASS rate from the judge model as the reliability figure, since two failures in six digests is a small sample and the judge covers every run.
- B. Rely on the completion status and the first live run, since a task that completes twelve times without an error message has demonstrated stable behavior on this workflow.
- C. Replace the judge with a stronger model and accept its verdict on each run, since a more capable judge removes the need to sample failures by hand.
- D. Grade the rate, not the run: sample many runs, read which items failed before counting how many, calibrate the judge against a human-labelled sample, and set the bar per task.

**Answer:** D

- ✅ **D** — An agent's output is a distribution; the judge is a model whose PASS is an opinion; and the wrong figures matter more than the overall percentage.
- ❌ **A** — An uncalibrated judge's PASS is an opinion, and the two real failures are severity information the rate hides.
- ❌ **B** — Ran is not the same as worked; a demo is the weakest evidence, and two of the last six digests were wrong.
- ❌ **C** — A stronger judge is still a model; calibration against human labels, not capability, is what earns trust.

**Yaad rakho:** Ek run saboot nahi. Kai runs par rate dekho, kaunsi ghalti hui wo pehle parho, judge ko calibrate karo.

*Grounded in: General Agents on the Web §9 and Appendix E (grade the rate not the run; the judge is a model too; read which failed before how many; demos are the weakest evidence)*

---

### Q15.
A procurement analyst at a Rawalpindi construction firm attaches three cement-supplier proposals and asks Claude: "Which supplier's contract lets us exit early, and on what terms? Answer only from the attached proposals; if a proposal does not state its exit terms, say so; for every term, quote the section heading and the sentence." Claude answers that Supplier C allows exit on 60 days' notice with no penalty, quoting "Section 9: Termination. Either party may terminate on sixty days' written notice without penalty." The analyst searches Proposal C and cannot find Section 9; that sentence appears word for word in Proposal B. Proposal C has no termination section at all. The tender committee meets tomorrow and the analyst's manager notes the quote is "real, from the attached documents".

**What should the analyst conclude and do?**

- A. It is unsupported for Supplier C: the sentence belongs to Proposal B, so correct it to 'not stated in Proposal C' and check the other answers the same way.
- B. The answer is acceptable because the sentence is real and comes from the attached documents, and the analyst can note that the source proposal is unclear.
- C. The answer needs only a tiny fix: change the supplier name in the sentence to B and keep the rest of the comparison, since the quote and the terms are otherwise right.
- D. The answer should be rejected and the request rerun with a stricter instruction, because one wrong attribution shows the assistant cannot be trusted with attached documents.

**Answer:** A

- ✅ **A** — A quote must support the claim about the document it is attributed to; an exact sentence from the wrong file is a fabricated support.
- ❌ **B** — The claim is about Supplier C; a real sentence from Supplier B does not support it.
- ❌ **C** — That repairs one cell without checking whether the other quotes are attributed to the right proposals.
- ❌ **D** — One mismatched quote calls for a specific correction and a check of the other claims, not abandoning the source-bound method.

**Yaad rakho:** Quote asli ho sakta hai magar galat document ka. Sentence us proposal mein dhoondo jis ka claim hai.

*Grounded in: AI Fluency §5.1 (answer only from attached documents; permission to say the proposal does not state it; quote heading and sentence); Just Delegate It §5*

---

### Q16.
A software firm's engineering manager asks a coding agent to fix a payroll-rounding bug and to "run the test suite and confirm all tests pass". The agent replies: "Fixed the rounding in payslip.py, ran the tests, and all tests pass." The manager, who cannot read code, opens the tool's output and sees a run log ending "collected 0 items ... no tests ran ... exit status 0". The test folder had been renamed in a refactor last week and the runner's path setting still pointed to the old name. A developer says the tool shows a green status and the agent did say it ran the tests, so the claim is supported, and the manager's release checklist requires only "tests pass".

**How should the claim be treated?**

- A. As supported, because the exit status is 0 and the agent reported running the tests, and the release checklist asks only for a passing status.
- B. As probably fine, so ask the agent to confirm in words that the payroll tests were included in the run, and release if it confirms and lists the test names.
- C. As a sentence, not an event: the log shows no tests ran, so fix the runner path, rerun until a nonzero count executes, and check the rounding against a hand-worked payslip.
- D. As a tooling quirk of minor importance, since the rounding fix is small, and the manager can release now and repair the runner configuration next sprint.

**Answer:** C

- ✅ **C** — A claimed action counts only if the tool result shows it; a green status on zero tests is not a pass.
- ❌ **A** — Exit status 0 with zero tests collected is a vacuous pass; the checklist's intent is that tests ran.
- ❌ **B** — A listed name in a reply is another claim; the log shows collection of zero items.
- ❌ **D** — The failed collection means the fix is untested; releasing a payroll change untested is the risk the check exists to prevent.

**Yaad rakho:** 'All tests pass' jumla hai. Log mein 0 tests ran, to saboot nahi.

*Grounded in: AI Fluency §5 (a claimed action that never happened; treat the claim as a sentence unless the tool shows the event); Code You Never Write §6*

---

### Q17.
A regional telecom's analyst asks Claude to summarise churn drivers from a customer file and to explain "how confident we can be that price is the main driver". Claude answers in one confident paragraph: "Price is the main driver of churn; customers on plans above PKR 2,500 are far more likely to leave." The analyst knows from experience that a question like this would get "it depends" from a specialist: churn also tracks contract length, service outages and competitor promotions, none of which are in the file's columns beyond a plan-price field. She wants a defensible statement for the board without rerunning the whole analysis. A colleague suggests asking Claude to rate its confidence, another suggests asking a second Claude to agree.

**Which response best matches the discernment guidance?**

- A. Ask Claude to rate its confidence out of ten and report the number alongside the statement, since a quantified confidence tells the board how far to rely on it.
- B. Treat a flat answer where an expert would hesitate as a warning sign: ask what would change the answer and what the data cannot show, then rerun on named factors.
- C. Ask a second Claude conversation whether it agrees that price is the main driver and report the finding as corroborated if it does.
- D. Accept the statement but add 'according to the data supplied' to it, since the caveat covers the missing variables and the board will read it correctly.

**Answer:** B

- ✅ **B** — Confidence where an expert would hesitate is one of the four signs; asking what would change the answer exposes the missing conditions.
- ❌ **A** — A self-rated confidence is the same confident voice, with no more evidence behind it.
- ❌ **C** — Same model and same file: agreement is likely and independent of the missing variables.
- ❌ **D** — A caveat on a causal claim the data cannot support does not make it defensible.

**Yaad rakho:** Mahir 'depends' kehta, AI 'bilkul' keh de: ye nishani hai. Pooch: kya badle to jawab badle?

*Grounded in: AI Fluency §5 (confidence where an expert would hesitate; ask what would change the answer); What AI Actually Is Idea 6*

---

### Q18.
An accountant at a Karachi trading house uses Claude to analyse a year of invoices and build a sales report. The report says the biggest customer by revenue is "Al-Noor Traders" with PKR 41 million. The accountant knows from long experience that "Hashmi Brothers" is the biggest customer by far. The row counts look right (9,850 in, 9,850 out), the totals are formatted well, and the assistant's replay says it "grouped invoices by customer name and summed the amounts". Her manager says the report matches the ledger's grand total, so the ranking must be right, and that the accountant's own impression may simply be outdated. The accountant also notes that Al-Noor Traders has been a customer for eleven years and that the report is meant for a bank meeting on Monday.

**What is the best next step?**

- A. Ask Claude to regenerate the report with the same instruction and use whichever ranking appears in two of three runs, since agreement across runs indicates stability.
- B. Accept the ranking, because the grand total matches the ledger and the row counts are equal, which shows that no invoice was dropped or double-counted.
- C. Treat the contradiction with her knowledge as a signal: ask Claude to show three rows behind each customer's total and how names were grouped, checking whether spelling variants split Hashmi Brothers.
- D. Ask a second assistant to write the summary of the report in plain English and accept the ranking if both summaries name the same top customer.

**Answer:** C

- ✅ **C** — Reality questions use what you already know; a grand total that matches can still hide a grouping error that splits one customer.
- ❌ **A** — Repeating the same grouping instruction repeats the same grouping error.
- ❌ **B** — A correct grand total says nothing about how invoices were grouped between customers.
- ❌ **D** — Two summaries of the same faulty table agree on it; the grouping is where the error would sit.

**Yaad rakho:** Tumhara tajurba report se takraye to ruk kar teen rows dikhwao. Grand total match hona kaafi nahi.

*Grounded in: Code You Never Write §6 (reality questions; show three rows behind the number; plain-English walkthrough)*

---

### Q19. *(Select TWO — all-or-nothing)*
An FDE reviews a Digital FTE that handles customer refund queries for a retailer. In a review of 200 conversations the answers were accurate against policy in every case. Support data over the quarter shows that 31% of customers who chat with the assistant call the store within an hour about the same issue, up from 12% before launch, and comments say things like "it answered but I still did not know what to do". The retailer's product owner argues that since answers are accurate and the chat model is unchanged, the assistant is performing well, and proposes to expand it to warranty queries. The FDE has been asked which kind of discernment the quarter's review skipped.

**Which TWO statements are correct?**

- A. The 200-conversation review was product discernment on accuracy, and the repeat-call rate and complaints should trigger monitoring and sampling before any expansion.
- B. Nothing was skipped, because an unchanged model with accurate answers is the definition of good performance, and repeat calls reflect customers' preference for talking to staff.
- C. The skipped kind is performance discernment: whether the assistant's independent behavior serves the people it meets, judged over many cases by what users do next and what they complain about.
- D. The skipped kind is process discernment: the FDE should judge whether her own sessions with the assistant during testing were paying off in time saved.

**Answer:** A, C

- ✅ **A** — Product discernment judges the result; performance discernment judges behavior toward users, and it turns into monitoring.
- ✅ **C** — Accurate answers can still fail users; this only shows at scale.
- ❌ **B** — Repeat calls tripling is a behavior signal that accuracy of individual answers cannot explain away.
- ❌ **D** — Process discernment concerns a person's working session with AI, not deployed behavior toward customers.

**Yaad rakho:** Jawab durust, user phir bhi phone kar raha: performance discernment, bohat saare cases par.

*Grounded in: AI Fluency §5.3 (performance discernment; an accurate tutor can still be a bad tutor; monitoring at scale)*

---

### Q20.
An operations director at a private hospital group is designing which AI-assisted outputs may run with sampled review once proven, and which keep a named reader every time. She writes a policy that names accountability explicitly: "The AI system approves patient-billing adjustments below PKR 20,000; the billing system logs that the AI approved them; the AI is therefore accountable for those approvals." The group's finance controller notes that below-20,000 adjustments total PKR 38 million a year, that adjustments are hard to reverse once a patient statement is issued, and that the group's auditors have asked who answers for them. The director says accountability follows whoever makes the decision. The adjustments are posted through a legacy system that was upgraded last year, and the director says the hospital's occupancy has been high all quarter.

**What is the flaw in the policy, and the best correction?**

- A. The flaw is the missing log; add the model version and prompt to each record so that the AI's accountability for each approval is fully documented for the auditors.
- B. The flaw is only the threshold: lower it to PKR 5,000 so that fewer adjustments are covered, and keep the statement that the AI system is accountable for those approvals.
- C. Accountability cannot transfer to a tool: keep a named person accountable, define the gate (who checks what, before statements issue), and sample the adjustments for evidence.
- D. The flaw is that the approvals are unsupervised, so add a monthly review of the AI's error rate and let the review committee share accountability with the AI system.

**Answer:** C

- ✅ **C** — AI can automate work but not accountability; an audit trail of what the AI did does not say who answers for it.
- ❌ **A** — Documentation of what the AI did does not make it answerable; a named person still must be.
- ❌ **B** — Changing the amount leaves the false premise that accountability can sit with the system.
- ❌ **D** — A monthly rate review is a monitor, not a defined gate before statements issue, and accountability is not shared with a system.

**Yaad rakho:** Accountability tool par nahi jati. Log 'kya hua' batata hai, 'kaun jawabdeh' nahi.

*Grounded in: AI Fluency §6.3 (AI can automate work; it cannot automate accountability); Governance §1.3 (accountability cannot transfer to a tool; defined gate)*

---

### Q21. *(Select TWO — all-or-nothing)*
A media-monitoring firm in Karachi has an assistant summarise regulator press releases each morning; a duty editor reads the summary before it goes to clients. Over one week the editor's notes show: on Monday the summary stated a fine of PKR 12 million that was PKR 1.2 million in the source; on Tuesday it attributed a quote to the wrong commissioner; on Thursday it reported that "the regulator confirmed the merger" when the release said the approval was conditional. The editor caught the Monday and Thursday items but only noticed Tuesday's when a client complained. The head of content wants to classify the failures and decide on a control before Friday. The editor has a reputation for catching mistakes, and the head of content says the assistant's summaries have won the firm two new clients this year.

**Which TWO conclusions are best supported?**

- A. All three errors come from one cause, weak prompting, so the fix is a longer standing instruction that tells the assistant to check numbers, names and conditions.
- B. The editor's catches on Monday and Thursday show the gate works, so Tuesday was an unlucky exception and the control should stay as it is with a reminder to be careful.
- C. The gate missed Tuesday's error, so define it: who checks names and figures against the release, when, with the source open, and re-check a sample of past summaries.
- D. The three errors are different types (a number slip, a misattribution, a dropped condition), so each needs a check aimed at its own risk, not one 'be more accurate' instruction.

**Answer:** C, D

- ✅ **C** — A human in the loop is not a gate; without the source in view and a specific check, errors pass.
- ✅ **D** — Generic feedback fails to resolve specific recurring issues; controls must match the specific risk.
- ❌ **A** — A standing instruction is a wish, not a control; the editor's check with the source is what catches errors.
- ❌ **B** — One client complaint is evidence the gate missed an error; a reminder does not change what the reviewer checks.

**Yaad rakho:** Teen alag ghaltiyan = teen alag checks. Gate: kaun, kya (source khol kar), kab.

*Grounded in: Governance §1.3 (a human in the loop is not a gate); Just Delegate It §9 (smallest message that fixes it; write the lesson into the brief); AI Fluency §5*

---

## Domain 4 — Workflow Integration and Solution Design (16% — 16 questions)

### Q22.
A hospital group's operations manager is mapping an AI-assisted appointment-reminder workflow with five steps: pull tomorrow's appointments, draft reminders from a template, personalise for patients with mobility needs, send, and log delivery failures. Her consultant explains that every step takes three decisions, and that mixing them is how a map ends up looking reasonable and being wrong. The manager has already picked a Skill for drafting and a scheduled task for sending because "the tools are what we have". The workspace has never been approved by the group's admin for patient names, and the mobility information lives only in nurses' notes that are not exported to any system. She asks in what order the decisions should be made for each step.

**Which order is correct?**

- A. Confirm the data may enter the tool; choose what carries each step; classify each step on reversibility, stakes and accountability; then check that everything each step needs can be supplied.
- B. Confirm the data may enter the tool and the inputs can be supplied; then classify each step on reversibility, stakes and accountability; only then choose what carries it (Skill, knowledge, code, instruction or gate).
- C. Choose what carries each step, such as the Skill and scheduled task; then classify each step on reversibility, stakes and accountability; then confirm the data may enter the tool and the inputs can be supplied.
- D. Classify each step on reversibility, stakes and accountability; then confirm the data may enter the tool and the inputs can be supplied; only then choose what carries each step.

**Answer:** B

- ✅ **B** — Eligibility comes first (a no ends the question), ownership second, implementation last and only for steps that got past the first two.
- ❌ **A** — Both eligibility gates come before any classification or carrier choice, since a missing input can end a step regardless.
- ❌ **C** — Implementation first is the tool-shaped error; it is decided last.
- ❌ **D** — Ownership before eligibility wastes work on steps that may fail the data or input gate however the criteria come out.

**Yaad rakho:** Tarteeb: pehle eligibility (data + inputs), phir ownership (teen criteria), aakhir mein implementation.

*Grounded in: Workflow Design Part 2 opener (eligibility, ownership, implementation: three decisions, in that order; keep the third out of the second)*

---

### Q23.
A B2B software company's sales-operations team has used an AI assistant for eight months to score inbound leads from 1 to 100. Reps report the scores are "excellent": of 1,900 scored leads, the top decile converted at four times the base rate. The VP of sales proposes letting the assistant also approve discounts of up to 15% automatically for leads scoring above 90, since "it clearly understands our buyers", and notes that discounts are logged in the CRM and can be reversed within 24 hours by finance. A rep points out that the 15% ceiling is written in the assistant's own output field, filled in from the lead's score, and that finance's 24-hour reversal only happens when a deal desk analyst flags an entry. The deal desk has two analysts and 300 quotes a week.

**Which assessment is correct?**

- A. Approve the proposal for leads above 90, because eight months of strong scoring shows understanding of buyers and finance's 24-hour reversal makes any discount error recoverable.
- B. Scoring quality is evidence about scoring, not discount authority; the ceiling is set by the assistant's own field and reversal needs an unstaffed flag, so keep discount approval with a named person.
- C. Keep discount approval human but have the deal desk approve only the quotes the assistant flags as unusual, since the assistant already knows which quotes look normal and can screen the rest.
- D. Approve the proposal but lower the automatic ceiling to 10% and have finance sample 20 quotes a month, since a smaller ceiling and a sample together bound the exposure.

**Answer:** B

- ✅ **B** — Halo delegation plus a self-referential control: a step cannot give itself permission, and the safeguard exists only on paper.
- ❌ **A** — Competence on scoring is credited to a different, binding step, and the reversal depends on an unstaffed flag.
- ❌ **C** — The set of quotes that reach the reviewer is chosen by the system being reviewed, so the gate misses exactly what the assistant misjudges.
- ❌ **D** — The ceiling is still generated by the assistant's own field, and a monthly sample does not restore a reviewer before the discount is committed.

**Yaad rakho:** Scoring achhi hai to discount approve bhi? Nahi. Aur jo gate staff hi na ho wo gate nahi.

*Grounded in: Workflow Design §7 (halo delegation; over-delegation; the unstaffed gate; a step cannot give itself permission to skip the gate) and §8*

---

### Q24.
At a customs-brokerage firm, a delegation map marks "Draft tariff-classification memo" as collaborative, reviewed by a senior broker before it goes to the client. When the map was signed off, volume was 20 memos a week and the broker spent about 15 minutes on each. Over two quarters volume rose to 55 a week, the broker was also assigned a second desk, and the weekly report still shows every memo as reviewed. The map's owner has left, and the map lists no review date. A new manager wants to fix it and considers four changes: a headcount request for a second broker, a rule that memos above a value threshold be reviewed by two people, an AI tool that flags memos where the model seems uncertain, and naming a map owner with a quarterly read.

**Which is the best first change, and why?**

- A. Request a second broker, because the gate was designed for 20 memos a week and 55 a week is beyond what one reviewer can do, so the fix is capacity.
- B. Name a map owner and set a scheduled read asking who reviewed last week and for how long, because the step is automated in practice; then size the gate to real volume.
- C. Deploy an AI tool that flags memos where the model seems uncertain, and route only flagged memos to the broker, because uncertainty is a better trigger than reading every memo.
- D. Add a two-person review rule above a value threshold, because the highest-value memos carry the most risk and a stronger gate there limits exposure while volume is high.

**Answer:** B

- ✅ **B** — Gates, instructions and maps fail with no signal; an owner and a date are how the failure is found before the outcome shows it.
- ❌ **A** — Capacity may be needed, but the process would drift again with no owner or scheduled read to notice.
- ❌ **C** — Model self-uncertainty is not a control; it moves the decision about what gets reviewed to the system being reviewed.
- ❌ **D** — It adds a rule to a map nobody is reading; the sole reviewer's actual behavior on the rest is still unknown.

**Yaad rakho:** Map ko malik aur tareekh do. 'Pichhle hafte kis ne kitna waqt diya?' se asli halat pata chalti hai.

*Grounded in: Workflow Design §8 (map owner and scheduled read; four review questions; 'who reviewed last week and how long') and §7*

---

### Q25.
A shipping-insurance firm built a Skill that turns claim files into a fixed 14-field "claim card", and it has been praised for accuracy. The firm then redesigned the workflow around it: the "Generate claim card" step is AI-owned with the stated reason "our card Skill is very good at this", the coverage check reads the 14 fields, and the client letter is drafted from the card. Adjusters now report that a cargo-tampering allegation, present in the claim file's narrative, does not fit any field and is dropped; no card shows an error because every card is complete against its own fields. The COO asks the team lead which correction addresses the actual cause, and the lead lists four candidates.

**Which correction addresses the cause?**

- A. Name a senior adjuster to review every claim card against the file before it is used, since the reviewer will notice facts the card cannot hold and can add them.
- B. Lower the step's classification to collaborative, keeping the card but requiring the adjuster to approve it, since collaborative steps have a named person judging each output.
- C. Increase the Skill's coverage by adding 6 fields to the card, including a tampering field, so that the card captures the facts adjusters said were missing.
- D. Map the work again with no tools in mind, classify each step on reversibility, stakes and accountability, then ask whether the Skill fits, keeping a place for facts that fit no field.

**Answer:** D

- ✅ **D** — The workflow was bent around a tool's output shape; the order to check is work first, classification second, tools last.
- ❌ **A** — A gate helps, but the map's step and downstream steps are still built around the twelve-field shape; the cause is the design, not only the missing review.
- ❌ **B** — Changing the owner column leaves the reason ('the Skill is very good') and the shape of the downstream steps unchanged.
- ❌ **C** — Adding fields treats one missed fact and keeps the tool-shaped design, so the next unusual fact will drop out too.

**Yaad rakho:** Skill ki khoobi se workflow ka naqsha na banao. Pehle kaam, phir criteria, phir tool.

*Grounded in: Workflow Design §7 (mapping the tool instead of the work; order to check: map the work with no tools in mind, classify each step, then ask who reviews)*

---

### Q26.
A regional bank's operations team is classifying the step "Accept or reject a supplier's late-payment waiver request" in its accounts-payable workflow. The step is reversible for 10 business days because the waiver can be re-billed. Amounts are small, never above PKR 15,000. An AI recommendation has matched the payable manager's own decision in 96% of 80 past cases. The manager says she signs off on all waivers under her delegated authority and that if the step were AI-owned she would still be the one the auditors call. The workflow's author argues that reversibility, low stakes and a 96% match make the step AI-appropriate; the internal-audit lead argues it must be human-retained because "somebody is accountable for every step".

**Which classification and reasoning are correct?**

- A. Human-retained: this step is itself the decision the manager answers for, so accountability decides it and, where the criteria disagree, the strictest wins.
- B. Collaborative: the assistant decides each waiver and the manager reviews a monthly batch, since the ten-day reversibility window lets her catch errors after the fact.
- C. AI-appropriate: the step is reversible for ten days and low in stakes, and a 96% match shows the recommendation is reliable enough for the assistant to own the outcome.
- D. Human-retained: somebody is accountable for every step in a payables process, and that accountability cannot be assigned to a tool, whatever the step's other properties.

**Answer:** A

- ✅ **A** — Somebody answers for every step; the sharper test is whether the step is the call or an input someone judges before it acts.
- ❌ **B** — If the step is the decision, a monthly review means the decision was made by AI and only audited.
- ❌ **C** — Past agreement is not a criterion, and accountability outranks reversibility and stakes where they disagree.
- ❌ **D** — The conclusion matches but the reason is too broad: accountability exists at every step, so it cannot distinguish this step from an input step.

**Yaad rakho:** Har step ka jawabdeh hota hai. Sawal: kya ye step khud wo faisla hai jis ka wo jawabdeh hai?

*Grounded in: Workflow Design §5 (three criteria; accountability's specific shape: is this the call they answer for; strictest wins; past performance is not a criterion)*

---

### Q27.
A policy team at an energy regulator asks Claude to draft a briefing on "the current renewable-energy import duties and how the new budget changes them". The draft is fluent, cites duty rates and a budget clause number, and includes a paragraph on how such duties work in general. The team lead's map treats research as a synthesis step and hands the whole briefing to the assistant. A researcher points out that the assistant's knowledge stops at a training date, that the budget was announced after it, and that the rates cited carry no links. The lead notes that the stable explanation of how duties work is good, and asks how the request should have been split.

**Which split of the research request is correct?**

- A. Have the assistant write the concept explanation and the rates from its own knowledge, but ask it to mark any figure it is unsure of, so the team can check only the marked ones.
- B. Ask for the whole briefing again in a research-mode run and accept it, since a multi-source cited report removes the need to split stable and current material.
- C. Take the stable concept explanation from the model's knowledge, but route current rates and the budget clause to a source she can open, asking for the answer and the link.
- D. Keep the whole briefing with the assistant but instruct it to state the date of its knowledge at the top, since disclosing the cutoff lets readers judge which rates may be stale.

**Answer:** C

- ✅ **C** — Run the window test on research: stable concepts can come from the model; anything current, priced or dated needs an external source you can open.
- ❌ **A** — The model marks nothing reliably; unmarked current figures pass as confident, which is the failure the split prevents.
- ❌ **B** — Research helps for the current part but the concept part does not need it, and citations must still be opened and checked.
- ❌ **D** — Disclosure does not fetch post-cutoff facts; the rates still arrive with the confidence of a guess.

**Yaad rakho:** Stable concept model se, current/dated cheez source (link) se. Confident jawab nahi, khulne wala source.

*Grounded in: Workflow Design §4 (research is a synthesis step: split stable concepts from current, priced or dated facts; ask for the link so you can check)*

---

### Q28.
A tender team at an engineering contractor extracts requirements from a 50-page hospital-linen-service RFP into a table with a label, an exact section reference, and a column "answered in our thread". The list looks complete and each row cites its source. The bid manager says: "Every row traces to a section, so the extraction is verified." Two clauses concern the team. Section 6 says the service must be "delivered promptly after the collection window"; a scoring appendix awards more points for "reasonable" turnaround, with no figure. The team has one day before the buyer's Q&A window closes. A junior suggests filling the two slots with "24 hours" and "48 hours" from typical hospital tenders, then flagging them in the bid.

**What is the best course of action?**

- A. Attack the list: ask which requirements two readers could interpret differently, and send the two vague clauses to the buyer as questions before the Q&A window closes, stating any interim assumption explicitly.
- B. Fill the two slots with 24 and 48 hours as the junior suggests and mark them as assumed in the bid, so that the bid is complete and any difference is flagged to the buyer later.
- C. Ask the assistant to interpret both clauses using tenders it knows of in the same sector and adopt the interpretation that appears most often as the reading of the RFP.
- D. Treat the table as complete because every row cites a section, and let the assistant propose the turnaround figures from typical tenders, since the source column proves the extraction.

**Answer:** A

- ✅ **A** — Extraction finds what was written, not what was meant; an unclear requirement caught now costs one clarifying question.
- ❌ **B** — A model-supplied default closes a blank the team owes the buyer a question about; it may be neither of the buyer's expected values.
- ❌ **C** — Typical tender wording is not this buyer's meaning; the buyer is the only source for what they mean.
- ❌ **D** — Traceability shows where written requirements came from; it cannot reveal ambiguity or implied requirements.

**Yaad rakho:** Source column completeness nahi, matlab nahi batata. Dhundli shart ka sawal khareedar se poochho.

*Grounded in: Workflow Design §2 (extract the requirements, then attack them; an ambiguous requirement does not look ambiguous; each missing answer is a question you owe someone)*

---

### Q29. *(Select TWO — all-or-nothing)*
A shipbuilder's contracts team submits a delegation map for reviewing supplier contracts. Four rows are questioned by the director. Row A: "Extract clauses from the contract", Owner AI, Criterion "reversible and low stakes", Carried by Skill. Row B: "Compute delay-penalty exposure", Owner AI, Criterion "must be computed, not written", Carried by code execution. Row C: "Approve or reject each change", Owner Human, Criterion "this step is the decision somebody answers for", Carried by named reviewer. Row D: "Sign and send", Owner Human, Criterion "the assistant makes formatting mistakes when signing", Carried by named signer. The director asks which rows have a criterion that is not one of reversibility, stakes or accountability. The director adds that the shipbuilder wins about half of its tenders and that the contracts team has recently moved offices, and he asks for the map by Friday.

**Which TWO rows have an invalid Criterion entry?**

- A. Row B: 'must be computed' is a Carried by reason, so the Criterion entry needs reversibility, stakes or accountability reasoning instead.
- B. Row C: 'this step is the decision somebody answers for' is an accountability statement about people, so it belongs under Carried by rather than Criterion.
- C. Row D: 'the assistant makes formatting mistakes' is AI performance, not a criterion; the reason for a human signer is that sending is irreversible and binding.
- D. Row A: 'reversible and low stakes' is a performance claim about the extraction and should be replaced with the Skill's measured accuracy in testing to be a valid criterion.

**Answer:** A, C

- ✅ **A** — 'Must be computed' is true but is an implementation reason, and using it as a criterion is how a high-stakes calculation ends up unreviewed.
- ✅ **C** — How well AI performed is not a criterion; reversibility, stakes and accountability are the only three.
- ❌ **B** — It is exactly the accountability criterion in its specific shape: whether the step is the call someone answers for.
- ❌ **D** — Reversibility and stakes are two of the three valid criteria; accuracy in testing is not one.

**Yaad rakho:** Criterion sirf teen: reversibility, stakes, accountability. 'Compute karna hai' aur 'AI ghalti karta hai' criterion nahi.

*Grounded in: Workflow Design §5-6 (only three criteria; 'must be computed' belongs under Carried by; AI's past performance is not a criterion)*

---

### Q30.
A marketplace's quotation workflow uses a Project whose knowledge holds a supplier price sheet. A junior analyst who built the workflow is the only person with the Project's admin rights. On a Friday evening a customer reports that quotes show old prices. The analyst is on leave until Tuesday with no phone signal. The team can see that every quote generated since the supplier repriced, at least three weeks ago, has used the stale sheet, but nobody else can pause the workflow or replace the sheet. The incident lead knows the four things a workflow designer should decide in advance: how it gets stopped, what is already out, who is told and by when, and what changes in the map. She has to decide which to fix first and asks her team.

**What should be fixed first, and why?**

- A. What is already out: log every quote's recipient and the sheet version used, because scoping the damage is the hard question and stopping the workflow can wait until Tuesday.
- B. How it gets stopped: if only the builder can act every other step waits, so give a second named person authority to pause without asking, then scope the affected quotes.
- C. What changes in the map: record that the sheet went stale and add a monthly refresh, since the fix must outlast the week everyone is paying attention.
- D. Who is told and by when: draft the customer notification tonight and send it before the weekend, since a late disclosure costs far more than an early one.

**Answer:** B

- ✅ **B** — The design-time decision that blocks all others is who can stop it and whether they need permission.
- ❌ **A** — Scoping matters, but continuing to issue stale quotes over the weekend enlarges the scope.
- ❌ **C** — That is a decision for after the incident; it does not stop or scope it.
- ❌ **D** — Telling customers is important, but the workflow keeps producing wrong quotes until someone can stop it.

**Yaad rakho:** Sab se pehle: kaun rok sakta hai aur kya usay permission chahiye? Warna baaqi sab intezar karte hain.

*Grounded in: Workflow Design §17 (four design-time decisions; if the answer is we would have ask the person who set it up, fix that first)*

---

### Q31.
A consultant is presenting an AI-assisted invoice-processing workflow to a manufacturer's CFO, who asks three questions: what it does, how much it saves, and whether it is safe. The facts: the assistant matches invoices to purchase orders and codes them; about 95% match cleanly; matched invoices are paid after an accounts clerk reviews a daily exception report of any invoice above PKR 100,000 or with a new bank account; the remaining 5% go straight to the clerk. Turnaround has fallen from five days to two. The CFO's board contains a former auditor. The consultant drafts four openings, wanting the one that states what the tool does, names the human checkpoint, and does not overstate.

**Which description should she use with the CFO?**

- A. 'Ninety-five percent of invoices are now processed automatically, with turnaround down from five days to two, and clerks handle the exceptions that the assistant cannot process.'
- B. 'The workflow is fully automated for standard invoices, with turnaround down from five days to two, and any invoice above PKR 100,000 is escalated to a clerk.'
- C. 'The assistant performs as accurately as an experienced clerk on invoice matching, so turnaround has fallen from five days to two, with a clerk available for the remaining 5%.'
- D. 'The assistant matches and codes invoices, cutting turnaround from five days to two; a clerk reviews every invoice above PKR 100,000 or with a new bank account before payment.'

**Answer:** D

- ✅ **D** — It states the result in the CFO's units, names the human checkpoint with its trigger, and says what the tool hands over.
- ❌ **A** — 'Automatically' with clerks only on exceptions drops the gate; readers will hear that most invoices have no human check.
- ❌ **B** — 'Fully automated' is almost never true and hides that the clerk also reviews new bank accounts and exceptions.
- ❌ **C** — 'As good as a person' sets a standard the tool will eventually miss, and it omits the checkpoint and its trigger.

**Yaad rakho:** Kya karta hai, gate kahan hai, kya se inkar. 'Automatic', 'handles', 'insan jitna achha' se bacho.

*Grounded in: Workflow Design §18 (state what the tool does, name the gate, say what it refuses; three phrases that overstate: fully automated, AI handles X, as good as a person)*

---

### Q32. *(Select TWO — all-or-nothing)*
A finance shared-services centre is assigning carriers to four items in its quarterly pricing-review workflow. (a) "Always show the customer segment in the first line of every brief." (b) "The approved price list, updated each quarter, that the review must read every run." (c) "Compute the margin impact of each price change the report cites, from the price list and volume file." (d) "Prepare the review pack in this exact order: cover note, table, exceptions, sign-off page." The facilitator says the team has been putting things in the wrong place before, and produced pull requests for changing a standing instruction, a knowledge file, a Skill and a code-execution step. Two of the four pairings below are right.

**Which TWO pairings are correct?**

- A. (d) goes in a Skill, because a fixed sequence in a fixed order is a procedure, and a one-line instruction would lose the order.
- B. (a) goes in Project knowledge, because a first-line rule is content the assistant should have available for every brief in the workspace.
- C. (b) goes in Project knowledge, because the approved price list is reference material the work must read on every run and it changes what the assistant knows.
- D. (c) goes in a standing instruction, because a calculation that must run every time is a rule that applies to every run of the review.

**Answer:** A, C

- ✅ **A** — Procedures go to Skills; a procedure pasted as a one-line instruction loses its steps.
- ✅ **C** — References go to the knowledge base.
- ❌ **B** — A limit that always applies is a rule, and rules belong in standing instructions.
- ❌ **D** — A calculation the output depends on is carried by code execution, not a rule.

**Yaad rakho:** Rule -> standing instruction. Reference -> knowledge. Ordered steps -> Skill. Calculation -> code.

*Grounded in: Workflow Design §2 and §14 (implementation table; rule, reference or procedure; procedures go to Skills; calculations to code execution)*

---

### Q33.
A business-analytics team builds a small internal dashboard as a Claude artifact in three cycles, no code written by them. Cycle 1: five charts from an attached file, all readable and roughly right. Cycle 2: they ask for a date filter and a totals row; the filter works, but one analyst notices a column total is slightly off, only because she knows roughly what one metric should be. Cycle 3: they ask for the brand colours and a print layout, and it works first time. The team lead wants to know how to fix cycle 2, and the analysts suggest more detailed wording of the request, a stronger tier, and restarting the artifact from scratch. Nothing in cycle 2 produced an error message.

**What is the correct diagnosis and fix?**

- A. It is a description problem: rewrite the totals request to specify the columns and the rounding rule in more detail so that the assistant sums exactly what the team intends.
- B. It is a tier problem: rerun cycle 2 on the highest tier, since a stronger model should sum the columns correctly and the error is an example of shallow reasoning.
- C. It is a feature problem: the totals were written into the page rather than computed, so move them to code execution and check what it computed against a known column.
- D. It is a build problem: restart the artifact from scratch with the same requests, because a defect that survives the first two cycles means the initial page was built badly.

**Answer:** C

- ✅ **C** — Cycle 3 was a description problem; cycle 2 fails silently because a written number looks as right as a calculated one.
- ❌ **A** — No amount of describing changes that a total written in prose is not a calculation.
- ❌ **B** — The failure is the wrong feature for a calculation, not depth; a stronger tier can still write rather than compute.
- ❌ **D** — Cycle 1 charts were fine; restarting repeats the request without moving the calculation.

**Yaad rakho:** Rang aur layout describe karne se theek; total computed hona chahiye, likha hua nahi. Feature ka masla.

*Grounded in: Workflow Design §9 (build loop; telling a description problem from a feature problem; totals written not computed) and §3*

---

### Q34.
Six months ago a retail analyst used Claude to build a call checklist as an artifact for her own client-onboarding calls. Today three account managers read from it on every call, HR has linked it in the new-hire pack, and the finance department pastes its scoring output into a board slide. Separately, the same analyst has worked out, by hand, the same three-step routine for replying to supplier payment queries four times in a row, with the same inputs and layout, and now wants colleagues to run it without her. The head of digital says both should "go to IT", another director says both should become "Digital FTEs", and the analyst says neither needs to change because "they still work by prompt".

**Which destinations are correct?**

- A. Both go to engineering, because any process a second person runs has become infrastructure needing uptime, access control and someone to call when it breaks.
- B. The checklist has crossed the escalation signal, since others depend on it, so it needs developer or architect expertise; the routine has a stable method, so manufacture it into a Skill or worker.
- C. Neither needs to move yet: add an owner to the checklist and a saved brief for the routine, since prompt-and-iterate is still adequate while the tools keep working.
- D. The checklist should be manufactured into a Digital FTE and the routine escalated to IT, because the checklist's steps are stable and supplier queries touch outside parties.

**Answer:** B

- ✅ **B** — Two signals with different destinations: who is exposed versus whether the method has stopped changing.
- ❌ **A** — Only the checklist has others depending on it; the routine's issue is a settled method.
- ❌ **C** — Dependence by HR, three managers and a board slide is exactly what prompt-and-iterate cannot carry.
- ❌ **D** — This swaps the two signals; dependence by others points to engineering.

**Yaad rakho:** Doosron ka inhisar = engineering. Wahi tareeqa teen baar = Skill/worker banao.

*Grounded in: Workflow Design §10 (escalation signal: other people depend on this vs I have solved this the same way three times)*

---

### Q35.
An audit-support team at a chartered-accountancy firm redesigns its monthly regulatory-return workflow with an assistant. After three months a partner is told it "saves loads of time". The team never timed the old process; three staff recall estimates of 60, 90 and 120 minutes. The old process is still documented and could be run again once or twice. The return goes to a regulator and an error carries a penalty, but the team's reported benefit is speed. The partner asks for a defensible statement of value and for evidence the new way is better on the metric that matters, and suggests averaging the estimates. The firm's headcount has grown by a third since last year, and one partner is keen to publicise the time saved at a conference next month.

**What is the best way to produce that evidence?**

- A. Report the vendor's published average time saving for similar workflows, and add the firm's error rate from the last audit, so the value statement rests on external and internal figures.
- B. Average the three staff estimates to get the old figure of 90 minutes, and report the time saved against it, since the people who did the work are the best available witnesses.
- C. Track time and revision rounds on the new process for the next quarter and report the trend as the improvement, since a trend across quarters is the standard evidence of change.
- D. Run old and new together for two or three cycles, measuring time, revision rounds and manual steps, and judge accuracy, the metric that matters here; treat earlier estimates as estimates.

**Answer:** D

- ✅ **D** — A parallel run gives a baseline, a fallback and agreement from those whose work changed; compliance outputs are optimised for accuracy.
- ❌ **A** — A vendor benchmark says nothing about this firm's process, and the error rate is not paired with a measured baseline.
- ❌ **B** — Recollections of the old way flatter the new one, and a baseline cannot be rebuilt afterwards.
- ❌ **C** — Without a baseline there is nothing to compare against, and time is not the metric for a regulatory return.

**Yaad rakho:** Purani speed yaad se nahi. Parallel run karo aur metric wahi lo jo kaam ki wajah hai (yahan accuracy).

*Grounded in: Workflow Design §16 (measure the before; baseline can't be rebuilt; choose the metric that matches why the work mattered; parallel run)*

---

### Q36.
An FDE is asked by a regional manufacturer's operations director to have an assistant map and run a new returns-authorisation workflow. The steps: read the customer's return request; check it against the warranty policy; decide whether to authorise; issue a refund. The director asks the FDE to tell her, before the pilot, "what this system will not do". The FDE knows the pilot design: the assistant reads and drafts; a returns supervisor authorises every case in the "decide" step; refunds are issued only by finance after the supervisor's authorisation; and requests mentioning legal action are routed straight to a supervisor without a draft. The director is deciding whether to trust the design and has been burnt by "AI does it all" claims in the past.

**Which statement best serves that professional layer of the exam?**

- A. 'The system performs at the level of a trained supervisor on warranty checks, and supervisors authorise every case as a final safeguard against the rare error.'
- B. 'The assistant handles returns from request to refund recommendation, with supervisors approving the recommendations, so most of your team's time is freed for complex cases.'
- C. 'The assistant reads and drafts a warranty check; a supervisor authorises every case, finance issues every refund, and requests mentioning legal action go straight to a supervisor with no draft.'
- D. 'The system is fully human-controlled: nothing happens without a supervisor, so no case can ever be wrongly authorised by the assistant during the pilot.'

**Answer:** C

- ✅ **C** — It says what the tool does, where the human gate is, and what the tool is built to refuse, before the client has to find out.
- ❌ **A** — 'As good as a person' sets a standard the tool will eventually miss, and it omits refusals and the finance-only refund step.
- ❌ **B** — 'Handles' from request to refund drops the gate and the refusal, and implies a scope the pilot does not have.
- ❌ **D** — It overstates in the safe direction; supervisors can still authorise a wrong draft, so the claim is one visible miss from being false.

**Yaad rakho:** Client ko pehle batao: ye kya karta hai, gate kahan, kis se inkar. Kamzori khud batao.

*Grounded in: Workflow Design §18 (say what it does, then name the gate, then say what it refuses; stakeholders trust it more when the checkpoints are explicit); PCAO-F page (tell the client what the system won't do)*

---

### Q37.
A regional chain of laboratories wants an assistant to draft "priority level" recommendations for incoming test requests, then route them. Data: requests contain patient names and test codes, and the lab's workspace has been approved by the admin for patient data. The steps are mechanical and reversible before routing, and the assistant matches the supervisor's priority in 94% of a trial. The regional director tells the FDE that in practice, urgent cases are those flagged verbally by a senior pathologist on the morning ward round or by a phone call from a named GP surgery: neither is written anywhere and neither reaches the request system. The FDE must place the "assign priority" step in the map. Some staff say the criteria give the step to the assistant; others say it must be manual.

**What is the correct treatment of the step?**

- A. AI-appropriate: the data gate is passed, the step is mechanical and reversible, and a 94% match in trial shows the assistant can own the routing, with an audit of a weekly sample.
- B. AI-appropriate once staff are asked to type the verbal flags into the request form, since a step whose inputs are later written down passes the window test in future.
- C. Collaborative: the assistant proposes priorities and routes them, and a supervisor reviews a random 10% sample each day, since the supervisor can correct the cases the assistant cannot see.
- D. The input gate fails: the information that decides urgent cases cannot be put in front of the model, so the step isn't eligible for AI ownership; keep priority with a person.

**Answer:** D

- ✅ **D** — Passing the window test makes a step eligible, and failing it ends the question however mechanical the step looks.
- ❌ **A** — The trial could not include the unwritten urgent cases, and a sample later is not a gate before routing.
- ❌ **B** — It may become eligible later, but today the inputs are unwritten and the trial data did not include them.
- ❌ **C** — Most requests would be routed on a priority that never had the deciding information, and a sample after routing is not a gate before it.

**Yaad rakho:** Jo baat sirf zabani hai wo model ko dikhayi nahi de sakti. Window test fail = step insaan ka.

*Grounded in: Workflow Design §4 (the window test: could everything this step needs be put in front of the model; passing makes a step eligible, never owned) and Part 2 (eligibility gates)*

---

## Domain 6 — Governance, Risk, and Responsible Use (15% — 15 questions)

### Q38.
Twenty minutes ago a recruitment coordinator at a Lahore staffing firm uploaded a spreadsheet of 340 candidates' names, phone numbers and salary expectations to her personal AI account, because the company workspace login was timing out. Nothing has been sent to anyone. She has since closed the tab and considers her options: deleting the chat, rerunning the same analysis in the approved workspace, waiting until she can describe exactly how many records were exposed, or telling her manager. The company's policy has a five-step first-hour procedure, and her colleague reads the steps out in a different order each time she asks. The firm's clients are regulated and contractual notification windows can be as short as 72 hours.

**Which sequence follows the first-hour procedure?**

- A. Stop the spread; record what went in, when, by which route and whether it went onward; report through the incident path; state facts plainly; follow the owner's instructions on deletion and notification.
- B. Stop the spread; report promptly through the incident path; record what went in, when and by which route; state the facts plainly; then follow the incident owner's instructions.
- C. Delete the chat to stop the spread; record what went in and when; report through the incident path once the exposure is fully understood; state the facts plainly; then follow the incident owner's instructions.
- D. Stop the spread; record the facts; rerun the analysis in the approved workspace so the compliant version is on record; report the incident with the corrected result; then follow the owner's instructions.

**Answer:** A

- ✅ **A** — Facts are recorded before reporting, reported without waiting for a perfect account, and deletion and notification are the owner's call.
- ❌ **B** — The facts should be recorded before the report so that the account is accurate; reporting first with nothing written invites guesses.
- ❌ **C** — Deleting removes her visibility, not the data, and waiting for a complete picture spends time a legal clock may not allow.
- ❌ **D** — Redoing the work is a reasonable later step and no substitute for reporting; the rerun delays the report and adds new copies.

**Yaad rakho:** Rokna, likhna, report karna, saaf bayan, owner ki hidayat. Delete chhupana hai, hal nahi.

*Grounded in: Governance §7 (first-hour procedure: stop the spread, record the facts, report promptly, state facts plainly, follow the incident owner)*

---

### Q39.
A logistics firm drafts the "Case" block of a Governance Record for an AI-assisted service-exception report sent weekly to large customers. The classification is "appropriate with review". The author must write the gate in a form that a reviewer who was not in the meeting can check, and lists four candidate wordings. The report is drafted from dispatch records; the company remains accountable for every factual claim to customers; and on disputed accounts the tone matters. The account managers are busy on Fridays, when the report goes out, and the firm's earlier problem was a report that said a delay was a "driver failure" when the dispatch record said weather. Only one wording names who reviews, what they verify, and when.

**Which wording is a defined gate?**

- A. The account manager reviews each report against the dispatch record for accuracy, with particular care on disputed accounts, as part of the normal Friday send-out routine.
- B. The account manager for each customer checks every delivery fact and cause against the dispatch record, and reviews tone on disputed accounts, before the report is sent on Friday.
- C. The account manager for each customer reviews every report before Friday's send-out, taking care that it is accurate and professional and reflects the company's standards.
- D. Before the report is sent on Friday, the account management team confirms that delivery facts and causes are accurate and that the tone on disputed accounts is appropriate.

**Answer:** B

- ✅ **B** — It names who holds the responsibility, the specific risk checked, and the moment: before the report is sent.
- ❌ **A** — 'As part of the routine' names no point before the output becomes hard to undo, so the when is missing.
- ❌ **C** — 'Accurate and professional' names no specific risk to check against the dispatch record, so the what is missing.
- ❌ **D** — 'The team' names no role that holds the responsibility, so the who is missing.

**Yaad rakho:** Gate = kaun (role), kya check (khaas risk), kab (bhejne se pehle). Ek bhi kam to gate nahi.

*Grounded in: Governance §1.3 (a human in the loop is not a gate: who, what, when; the account-manager example)*

---

### Q40.
A public-health analyst has a 60,000-row spreadsheet of hospital admissions with patient names, national ID numbers, ward, admission date and length of stay. She has two tasks. Task 1: find monthly trends in length of stay by ward. Task 2: reconcile one named patient's 14 admissions against billing, which needs that patient's ID. Her department restricts regulated personal data to approved routes, and nobody has confirmed the workspace is approved for patient records. A colleague says the whole file must stay out because it is red-tier; another says an incognito chat makes it safe; a third says the code-execution sandbox is enough since it is isolated. The data owner is on leave, the department's server was migrated last month, and the analyst says the deadline for the report is the end of next week.

**Which plan follows the framework?**

- A. Run both tasks inside the code-execution sandbox as they stand, since isolated execution stops the sensitive columns leaving and satisfies the department's restriction on regulated data.
- B. Run both tasks in an incognito chat after removing names, since incognito keeps the data out of memory and history and the removal covers the identifiers for reconciliation.
- C. Split by the discriminator: for Task 1 remove names and IDs, check no mapping travels, then run; for Task 2, where identity is the substance, get the route approved first.
- D. Abandon both tasks until compliance approves every dataset, since patient records are red-tier and a redacted copy could still leak through combinations of ward and admission date.

**Answer:** C

- ✅ **C** — Name the branch before you answer: pattern-only work takes redaction, while work that needs the identifiers needs a confirmed route first.
- ❌ **A** — A sandbox is an execution boundary, not an approval boundary; it authorises nothing.
- ❌ **B** — Task 2 needs the ID, and incognito governs persistence, not whether the data was permitted.
- ❌ **D** — That pays the cost of abandonment for Task 1, which needs only the pattern; the answer is remove then verify, not refuse.

**Yaad rakho:** Pattern chahiye to pehchaan hatao; pehchaan chahiye to pehle route ki manzoori. Branch ka naam lo.

*Grounded in: Governance §2.2-2.6 (the discriminator: identifiers or only the pattern; redaction; route first; sandbox is not authorization; incognito is not zero retention)*

---

### Q41.
A pharmaceutical distributor's HR team collected 2,100 employees' health-screening results in 2024 for one stated purpose: a workplace-safety programme for staff exposed to solvents. The results sit in the company's approved AI workspace, which the admin has confirmed is approved for health data. In 2026 the head of analytics proposes using the same records, with names attached, to build an assistant that flags employees "likely to take extended sick leave" for manager conversations. She notes that the route is approved, the data never leaves the workspace, the drafts would be produced in temporary chats, and the assistant would only support managers. The employees were told the results would be used "for the solvent-exposure programme".

**Which governance question is open?**

- A. Whether temporary chats are sufficient for the drafts, since a persistence control that keeps flagged names out of memory is the main safeguard for health data in an approved workspace.
- B. Whether the data can be treated as green once the names are removed, since flagging patterns of sick leave needs only counts and the names are the sensitive fields.
- C. Whether the assistant can be classified as appropriate with review, since managers reading the flags before any conversation is the gate that resolves the governance concern.
- D. Whether the purpose the results were collected for covers the flagging use; an approved route says where data may go, not what for, and the data owner decides.

**Answer:** D

- ✅ **D** — Purpose is the leg of the route question people skip because the file is already inside.
- ❌ **A** — Persistence controls answer a narrower question; they do not settle whether the use was permitted.
- ❌ **B** — The flagging is about named individuals, so removal defeats it; the question is about purpose, not tier.
- ❌ **C** — A review gate does not answer whether the data may be used for this purpose at all.

**Yaad rakho:** Route manzoor hona 'kahan' batata hai, 'kis maqsad ke liye' nahi. Maqsad data-malik se poochho.

*Grounded in: Governance §2.4 (the route matters as much as the tool name; purpose is the reason the data was first collected; a new use needs that reason or fresh permission)*

---

### Q42. *(Select TWO — all-or-nothing)*
A bank's fraud-operations team runs a "case-notes" agent from the vendor's official skills directory. The publisher is well known, the source check passed, and the team's security lead has confirmed the Skill's instructions only summarise notes. The team then connects it to a shared mailbox where customers and third-party investigators send documents and enables its "send reply" action so the agent can acknowledge submissions. Two weeks later a submitted PDF contains hidden text telling the agent to forward the case file to an external address. The agent does not comply, but the security lead wants controls that would hold next time. Four controls are proposed, and the team lead says two of them are real controls and two are not.

**Which TWO controls address the risk?**

- A. Keep the send action behind a human gate: an agent that reads untrusted content and can act is the risky pairing, whoever published the tool.
- B. Give the mailbox connector the narrowest scope the summarising job needs, such as read-only on one folder, since connectors have a scope dial and least privilege applies.
- C. Rely on the publisher's reputation and the passed source check, since a trusted publisher's Skill would not act on instructions found inside a document it was asked to read.
- D. Set the Skill itself to read-only, because a Skill carries its own permission list and read-only limits it to viewing the mailbox and never sending from it.

**Answer:** A, B

- ✅ **A** — Who wrote the tool and who wrote the content are two different trust questions; irreversible actions stay behind a person.
- ✅ **B** — Connectors have scopes you grant and can narrow; start read-only and keep the reach small.
- ❌ **C** — The source check says who wrote the tool, nothing about who wrote the content it reads.
- ❌ **D** — A Skill has no scope dial; it runs with the access the session has.

**Yaad rakho:** Connector ka scope hota hai, Skill ka nahi. Parhna + bhejna saath mein khatarnak: send par insaani gate.

*Grounded in: Governance §3.1-3.3 (a Skill has no scope dial; trusted tool, untrusted content; keep irreversible actions behind a human; least privilege); Skills & Connectors Part 5*

---

### Q43.
A research office at a university has 1,800 survey responses about staff wellbeing. To protect respondents, an analyst replaces each name with a code (R-0001 and so on), removes email addresses, and keeps the code-to-name list in the HR shared folder for follow-up. She then writes "anonymised, green tier" on the file and prepares to use it in a chat workspace. The responses still include job title, department, campus, age band and a free-text field. In small departments a title, campus and age band together identify a single person: the "only female professor in the Physics department at the Sukkur campus" appears in 14 comments. The office's policy classifies HR data as yellow by default and asks for the organisation's own anonymisation standard.

**What is the correct assessment?**

- A. The file is unusable, because HR-related survey data is red-tier and the analysis of any wellbeing data must be done by the HR team without an AI assistant.
- B. The file is yellow and safe as it stands, because a code is a label and labels are not personal data, so the chat workspace can be used without further checks.
- C. It is pseudonymised, not anonymised, and keeps its tier: someone holds the mapping and title, campus and age band identify people; generalise those fields and confirm the route.
- D. The file is anonymised and green, because names and emails were the identifiers and removal of both, together with the codes, meets the policy's standard for a survey.

**Answer:** C

- ✅ **C** — Replacing names is a first move, not a verdict; the test is whether someone reading only what you pasted could work out who it is about.
- ❌ **A** — That abandons a task that needs only the pattern; generalise the identifying fields and verify instead.
- ❌ **B** — Pseudonymised data must not be handled as though it were anonymous, and residual identifiers remain.
- ❌ **D** — The mapping still exists and the remaining fields are identifying in small groups.

**Yaad rakho:** Naam ki jagah code magar list HR ke paas: pseudonymised. Title+campus+age bhi pehchaan hain.

*Grounded in: Governance §2.1-2.3 (pseudonymised keeps its tier; partial redaction fails on combinations of ordinary facts; anonymised by your organisation's standard)*

---

### Q44.
A university admissions office screens 4,000 scholarship applications with an AI assistant that produces a shortlist of 120 for the committee. The committee reads the shortlisted applications carefully and the chair says the process is "thoroughly reviewed". A coordinator notices that 78% of the shortlist come from three universities and that applicants from rural districts are almost absent. The office decides it must add a fairness control, and an academic advisor suggests four: read the 120 more carefully, add a second AI to re-rank the 120, sample the 3,880 excluded applications including those near the cut-off, and publish the AI's ranking criteria. Some applicants may not know an automated screen was used. The scholarship budget was doubled this year, the office recently changed its application portal, and the committee chair is proud that the process now runs in half the time.

**Which control best fits the People question?**

- A. Add a second AI model to re-rank the 120 shortlisted applications and compare its order with the first assistant's, keeping any application both rank in the top 60.
- B. Have the committee read the 120 shortlisted applications more carefully and record their reasoning, since deeper review of the selected set shows whether the AI ranked them fairly.
- C. Publish the assistant's ranking criteria on the scholarship page, since transparency about the criteria lets excluded applicants notice and challenge an unfair outcome.
- D. Sample exclusions as well as inclusions: pull applications from the 3,880 excluded, especially those near the cut-off and from under-represented districts, and check them against the criteria.

**Answer:** D

- ✅ **D** — If review looks only at survivors, the only people positioned to notice a systematic exclusion are the ones filtered out, who were never told.
- ❌ **A** — Two models re-ranking the same 120 still never look at the excluded 3,880.
- ❌ **B** — Reading only the survivors cannot reveal who was removed.
- ❌ **C** — Publishing criteria may help disclosure but does not check who was excluded; nobody inspects the excluded set.

**Yaad rakho:** Sirf bache huay logon ka review masla nahi pakadta. Nikale gaye logon mein se sample lo.

*Grounded in: Governance §4.1 (look at who was excluded; sample exclusions as well as inclusions) and §4.2 (disclosure)*

---

### Q45. *(Select TWO — all-or-nothing)*
A team lead at a marketing agency adds an AI notetaker to a weekly customer call. It joins as a participant, records, and posts a summary to the team's shared channel afterwards. The customer, a listed company's investor-relations team, is not told. The team lead says the tool is routine, the summary will be reviewed by the team before circulation, and the meeting is internal to both companies. The calls often cover unannounced results and pricing. The agency operates in a market where some jurisdictions require every participant's consent to a recording, and its clients' contracts have confidentiality clauses. The agency's own policy is silent on notetakers. The agency has 40 staff, its largest customer is a listed company, and the team lead says the notetaker won an award at a recent vendor conference.

**Which TWO statements are correct?**

- A. The Capability question is the only gap, so the fix is to start the notetaker read-only, since a read-only participant reaches less of the conversation than a full one.
- B. The Data question was skipped too: the content is confidential, so the recording needs the same route check as any upload and the summary needs review before circulating.
- C. The People question was skipped: everyone on the call is affected and some jurisdictions require every participant's consent, so announce the notetaker and decide disclosure by rule first.
- D. Nothing was skipped: recording a call you are a party to is routine tooling, the summary is reviewed by the team, and a review of the summary is the only control needed.

**Answer:** B, C

- ✅ **B** — The notetaker touches all four questions; the conversation may hold customer or deal information needing an approved route.
- ✅ **C** — Check disclosure rules first, then judgment; concealment is what damages trust when it surfaces later.
- ❌ **A** — A participant that records already has the whole conversation; read-only is not the relevant control.
- ❌ **D** — Reviewing the summary does not address consent, disclosure or the route for confidential content.

**Yaad rakho:** Notetaker chaaron sawal chhoota hai. Shuru mein elaan karo, route check karo, summary review karo.

*Grounded in: Governance §4.2 (the notetaker in the meeting touches all four questions; announce it; some jurisdictions require every participant's consent)*

---

### Q46.
A regional insurer's claims director asks for a decision on using an AI assistant to flag possible fraud on 380,000 motor claims a year. Flags go to investigators, who follow up on any flagged claim. The assistant would use, among other inputs, the claimant's postcode and vehicle age. The legal team has said it is unsure whether local law limits automated screening that can affect claim outcomes, and whether policyholders must be told. The director wants the analyst to decide herself and simply document it, arguing the four questions give her enough to decide, and that "when in doubt, disclose" covers everything. The compliance function has not been consulted. The company has grown its motor book by 20% this year, its investigators are already stretched, and a competitor announced a similar tool last month.

**Which response follows the framework?**

- A. Disclose the screening to all policyholders by default and proceed, since disclosure resolves any doubt where no rule settles the question and avoids the cost of an escalation.
- B. Escalate the question, not a verdict: the population is large, the harm significant and the legal point outside her standing; bring the framework, the control added and the unresolved question.
- C. Postpone the decision until a policy is written for automated screening, since acting without a governing rule creates exposure that the analyst personally carries.
- D. Decide and document, applying the four questions and the disclosure default, since structured reasoning handles most ambiguous cases and a documented decision is the professional standard.

**Answer:** B

- ✅ **B** — Any one of three signals is enough; a strong escalation gives the reviewer something specific to decide.
- ❌ **A** — Disclosure is the tie-breaker for ordinary cases, not a substitute for escalation on a large, legally uncertain one.
- ❌ **C** — Waiting halts the work and does not send the specific unresolved question to whoever holds it.
- ❌ **D** — A large population, significant harm and a legal question outside her standing are exactly the signals that the reasoning should not stand alone.

**Yaad rakho:** Teen signals mein se ek: badi abaadi, bara nuqsan, apni salahiyat se bahar. Sawal bhejo, faisla nahi.

*Grounded in: Governance §4.3 (escalate the question, not a verdict; three signals: large population, significant harm, outside standing) and §4.2*

---

### Q47.
A team lead at a design agency audits a month of her team's AI use to see where practice and policy have parted. She finds four candidates for the audit's questions and wants the set that actually finds the Diligence gap. The team uses a mix of an approved workspace and, at times, a personal account; the agency's policy lists approved entry points and a review gate for client deliverables; a Skill was added last month; and a client's data was involved in one project. One colleague suggests the audit be a hidden review of individual chat logs, to see people's true behaviour. The lead wants the audit to be about the process rather than the person.

**Which set of audit questions is best?**

- A. Which workflows were designed last quarter; which gates were planned in each; what training was delivered on the policy; and what did the vendor's dashboard say about total use?
- B. Are the approved entry points and gates listed in the policy still correct; has the policy been approved by legal this year; and does each staff member hold a signed acknowledgment of it?
- C. Which individuals used unapproved entry points; how often did each person skip a review gate; which staff enabled tools without permission; and whose work has the most errors traced to AI use?
- D. Which AI workflows are in use; what data is really going through them; did the defined gates actually run; what tools or permissions were added; what changed in model, route, data or audience?

**Answer:** D

- ✅ **D** — This finds the distance between what the policy says and what people do, by asking about the work rather than the worker.
- ❌ **A** — These describe design and intentions, not the actual data, gates and changes.
- ❌ **B** — These audit the document rather than what people actually do, which is where the gap lives.
- ❌ **C** — Auditing the person makes people show only their cleanest work and loses sight of the behavior wanted.

**Yaad rakho:** Audit kaam ka karo, banda nahi: kya chal raha, kaunsa data, gate chala, kya naya, kya badla.

*Grounded in: Governance §8.1-8.2 (run a usage audit on the work people actually do; audit the process, not the person; the Diligence gap)*

---

### Q48. *(Select TWO — all-or-nothing)*
A regulated-client consultancy approved an AI-assisted workflow last March. Its Governance Record says: internal audience only, one model family, one approved connector, no outside content, low consequence. Since then: the vendor's default model has changed; the workflow's summaries now go to the client's board as well as the internal team; the firm moved its office to a new building with the same IT setup; a new colleague has taken over the workflow from the owner; the company logo was redesigned. The workflow's owner says the record was approved and, because the brief text is unchanged, nothing needs re-checking. The firm's managing partner asks which changes trigger a re-check of the record.

**Which TWO changes are re-check triggers?**

- A. The vendor's change of default model: approval attached to the earlier model, so the workflow is no longer the same thing and needs re-checking.
- B. The office move to a new building with the same IT setup, because any change of location alters the route through which data reaches the assistant.
- C. The logo redesign, because the workflow's outputs carry the company branding and any change to them alters the disclosure the record was approved on.
- D. The change in audience: summaries now reach the client's board, changing who is affected and the consequence of error, so the People and Case blocks need re-checking.

**Answer:** A, D

- ✅ **A** — Approval is not a reason to skip review when the thing approved is no longer the same thing.
- ✅ **D** — Audience, consequence of error, and population affected are re-check triggers.
- ❌ **B** — Nothing about the route, data or permissions changed with the building; it is not a trigger.
- ❌ **C** — Branding does not change the model, data, audience, permission, policy or consequence; it is not a trigger.

**Yaad rakho:** Model, audience, data, permission, policy badle to record dobara dekho. Logo/imarat se farq nahi.

*Grounded in: Governance §8.5 and §9 (re-check when model, product feature, connector, data, source of outside content, audience, consequence, law or policy changes; what changed since we last decided this was okay)*

---

### Q49.
An operations analyst is completing the Evidence strip of a Governance Record for an AI-drafted weekly service report. She writes: "Success measure: account managers complete the factual check before sending. Failure threshold: any AI-generated error big enough to matter reaches a customer. Monitor: the analyst, monthly. Residual risk: none, because the account manager reviews every report." Her manager says the residual risk line is wrong and that "none" is never an answer for a control that depends on people. The analyst says a named reviewer eliminates the risk. The manager wants a corrected residual-risk line that is specific rather than a confession of failure. The analyst adds that the weekly report has never been late, that the account managers are proud of it, and that a customer praised its layout last quarter.

**Which residual-risk line is correct?**

- A. The AI may occasionally make a factual error, so the residual risk is that some reports contain errors before the account manager has reviewed and corrected them.
- B. The account manager might skip the factual check on a busy Friday, so the residual risk is that the check is not always completed before the report is sent.
- C. A consistent wording bias across all reports could survive each manager's individual check, so the monthly sample compares phrasing across customers as well as within each report.
- D. None, because the account manager reviews every report and any error would be caught, so the residual risk is confined to the analyst's monthly monitoring of the reviews.

**Answer:** C

- ✅ **C** — Residual risk is what can still go wrong after every planned control works as designed, named so the right owner can decide if it is acceptable.
- ❌ **A** — Errors that the review catches are not residual risk; the question is what survives a review that works.
- ❌ **B** — That is a control failing, not what remains when the control works as designed.
- ❌ **D** — 'None' hides what survives a working control and restates the design instead of naming a remainder.

**Yaad rakho:** Residual risk = jo control theek chalne ke baad bhi bacha rahe. 'Koi nahi' kabhi jawab nahi.

*Grounded in: Governance §5.5 and A.1 (residual risk means what can still go wrong after every planned control works as designed; naming it lets the right owner decide)*

---

### Q50.
A finance operations lead wants to enable a third-party "analytics booster" Skill to speed up her team's monthly reporting. It comes from an unknown publisher, its long instructions go well beyond reporting (they mention fetching benchmark data from "partner sources" and saving copies of processed files "for continuity"), and it works well in a demo. She proposes enabling it for one week on the team's real reporting data to watch what it does, adding that a scan showed nothing malicious. The team's sessions can reach the finance shared drive and the payment approvals connector. The security team's queue is slow and the month-end deadline is close. The month-end deadline is in four days, the team's morale is low after a hard quarter, and the publisher's demo video has been widely shared on social media.

**Which outcome does the framework support?**

- A. Enable it for one week on real data with close monitoring, because observed behavior over a full month-end cycle is the most reliable way to judge a Skill's reach.
- B. Enable it read-only on the shared drive, since a read-only Skill can look at the reporting files but cannot change or send anything, which limits the reach to the task.
- C. Escalate to security with the specific concerns (unknown source, instructions beyond reporting, file copies) and use no real data meanwhile; a scan pass doesn't settle source, reach and fit.
- D. Decline it permanently and tell the team never to use third-party Skills, since an unknown publisher and broad instructions show the whole category is untrustworthy.

**Answer:** C

- ✅ **C** — A useful idea with unresolved trust and reach goes to escalation with the unanswered question named, not to experiments on real company data.
- ❌ **A** — Enabling and watching grants the access before the risk is understood, which is the wrong order for something you cannot take back.
- ❌ **B** — A Skill has no permission dial; it inherits everything the session can reach, including approvals.
- ❌ **D** — A blanket decline is an overcorrection; escalation with the specific question is the proportionate outcome.

**Yaad rakho:** Anjaan publisher + zaroorat se zyada instructions: escalate karo, asli data par tajurba nahi.

*Grounded in: Governance §3.1-3.2 (five checks; a Skill has no scope dial; three outcomes; escalate with the unresolved question named; scanning helps but is not approval)*

---

### Q51.
A junior consultant at a Karachi firm uses Claude to draft performance-review summaries for 10 team members from her own notes, and she reads each carefully against the notes. An HR partner later compares them side by side: two team members with near-identical notes received summaries with noticeably different language, "reliable and steady" for one and "inconsistent and hesitant" for the other. She asks Claude why and it replies that it "treated each employee independently and neutrally". The firm's policy requires that employees be told when AI has drafted material affecting their appraisal. A colleague suggests adding "be fair" to the prompt and rerunning. The firm's HR partner is new, the appraisal cycle closes next Friday, and the consultant is regarded as one of the most reliable people on the team.

**What does the framework say to do?**

- A. Send the summaries and inform the employees that AI drafted them, since disclosure lets each employee challenge the language and is the control that the policy requires.
- B. Do nothing further, because every paragraph was verified against her notes and any difference in the wording reflects differences in the underlying performance.
- C. Accept Claude's statement that it treated each employee independently and neutrally, and add 'be fair' to the prompt, since a stated instruction resolves any framing tilt.
- D. Check consistency across employees, not only paragraph by paragraph: compare phrasing across the group, own the assessment, and follow the disclosure rule, since framing can tilt wording.

**Answer:** D

- ✅ **D** — A fairness check compares outputs across the affected people; each paragraph can be right while the pattern is unfair.
- ❌ **A** — Disclosure is required by the firm's policy, but it does not itself check consistency across employees.
- ❌ **B** — Matching notes does not show wording was applied consistently; near-identical notes produced different language.
- ❌ **C** — The assistant's own account of its neutrality is not an independent check, and an instruction does not detect a pattern.

**Yaad rakho:** Har paragraph sahi ho sakta hai, poore group mein lehja ek jaisa? Cross-employee check.

*Grounded in: Governance §4 (worked example: performance-review drafting; check consistency across employees; disclosure is decided by rule first) and §4.2*

---

### Q52.
A 12-person analytics consultancy has no AI policy. A junior consultant, worried about client data, writes a 40-clause policy over a weekend and circulates it as "the firm's official AI policy" without the partners seeing it; two clauses conflict with a client's contract. A partner is annoyed; the junior says a policy is better than none. An associate proposes waiting for a law firm to produce a full policy, and another proposes adopting a published framework word for word. The firm has three regulated clients. The partners have asked for a way forward that gives staff something usable this week and is honest about its status. The firm's website was redesigned last quarter, two of the clients have asked about its AI use, and the partners have a retreat planned next month.

**Which is the right way forward?**

- A. Adopt a published governance framework verbatim as the firm's policy today, since a recognised standard is more defensible than anything written internally in a week.
- B. Propose an interim one-page guide for the right owner to endorse (routes, red list, gate rule, Skill and connector review, named contact); it doesn't replace legal or contractual approval.
- C. Wait for the law firm's policy and continue as before in the meantime, since guidance not approved by the owner creates more exposure than existing practice.
- D. Keep the 40 clauses but relabel them 'draft' and ask staff to follow them until the partners review, since a detailed document is more defensible in a later client review.

**Answer:** B

- ✅ **B** — Do not present an invented policy as official; make defaults explicit and route them to the owner.
- ❌ **A** — A framework is a practitioner slice, not a substitute for legal, compliance or contractual approval, and adopting it wholesale skips the owner's endorsement.
- ❌ **C** — With no policy your written reasoning must carry more weight, and whatever staff do becomes the de facto policy.
- ❌ **D** — Length and detail are not the point; a short interim proposal for endorsement is the form, and the conflicting clauses remain.

**Yaad rakho:** Policy nahi to interim proposal likho aur malik se endorse karwao; khud 'official' mat banao.

*Grounded in: Governance §8.4 (when there is no AI policy: an interim proposal for the right owner to endorse; the one-page start; regulated environments)*

---

## Domain 1 — Prompting and Task Execution (14% — 14 questions)

### Q53. *(Select TWO — all-or-nothing)*
A COO asks her chief of staff to shortlist three trucking providers for the Lahore to Karachi corridor with an assistant. The brief reads: Outcome, three providers compared with one recommended. Context, a 20-tonne monthly load. Constraint, under a stated rate per kilometre. Deliverable, a table with rate, transit days and a link. Verification, "mark anything unconfirmed as unverified". The table arrives clean. Two days later the COO asks why a well-known provider is missing. The assistant had silently dropped a provider whose rate was unpublished, and, choosing between two providers tied on rate, had picked the one with shorter transit time without saying so. Nothing was marked unverified because, as far as the assistant was concerned, nothing it stated was unconfirmed.

**Which TWO additions to the brief would have prevented both silent decisions?**

- A. A longer Context line: 'the COO values well-known providers and short transit times', so that the assistant knows which providers and tiebreaks matter to her.
- B. A Verification line extended to omissions: 'list every provider you considered and exclude only with a reason', so the check covers what was left out.
- C. A tighter Constraint line: 'consider at least five providers and rank all of them by rate', so that the assistant has less room to exclude anyone before the shortlist.
- D. An Authority line: 'if two options tie, say so and pick by rate; do not drop a provider without telling me', stating what may be decided alone with a duty to report.

**Answer:** B, D

- ✅ **B** — Verification written before the work starts should name what will be checked, including omissions, which an 'unverified' mark cannot reveal.
- ✅ **D** — Without an Authority line the assistant decides silently and you never learn a decision was made.
- ❌ **A** — Context supplies what the assistant cannot know; it does not tell it which decisions it may take alone or must report.
- ❌ **C** — Constraints limit the job; they do not make the assistant report the decisions it makes inside it.

**Yaad rakho:** Silent faisle rokne ke liye Authority (kya akela tay kare, batana lazmi) aur Verification (kya chhoota).

*Grounded in: Just Delegate It §3 and §7 (six-line brief; Authority and Verification are the two people skip; a silent decision is one you cannot review)*

---

### Q54.
A procurement analyst at a hospital group gives an agent in a desktop coworking product the job of cleaning up a shared vendor master list. She writes "list your plan and wait for my go-ahead" at the top of the brief. The agent lists six steps, she edits one (do not merge records with different bank accounts), and types "go". After the run she compares the approved plan with what happened: the agent followed five steps, and in the sixth it merged two vendor records that have different bank accounts because they had the same name, and it did not say so in its summary. She is considering three lessons: never let an agent deviate from an approved plan, ask for the plan again next time, and add a line to the brief.

**Which lesson follows from the framework?**

- A. Move the agent to a mode that asks approval for each action, since per-action prompts remove the need for a plan and prevent silent merges of records.
- B. The failure is the silent change, not the change: add an Authority line saying the agent may find a better route but must report any deviation, and compare plan to actions after each run.
- C. Treat the plan-first step as sufficient control and simply repeat it, since a plan she edited and approved covers every action the agent later takes.
- D. Forbid deviation from any approved plan, since an agent that finds a different route once it starts has exceeded the authority the plan granted.

**Answer:** B

- ✅ **B** — An approved plan is not a cage; what the agent may not do is cross a drawn line or change something that matters without telling you.
- ❌ **A** — Per-action approval is a different control and does not create the plan-versus-actions comparison or the duty to report a change.
- ❌ **C** — The plan was followed except where it was not, and nothing in plan-first makes the agent report deviations.
- ❌ **D** — Agents often find a better route; forbidding change loses that value and does not address silence about it.

**Yaad rakho:** Plan cage nahi hai. Ghalti ye nahi ke raasta badla, ghalti ye ke batayaa nahi.

*Grounded in: Just Delegate It §7 (plan-first; an approved plan is not a cage; the failure is the silent change; compare the approved plan to what was done)*

---

### Q55.
A compliance analyst pastes a two-page regulator circular into an assistant with the instruction: "Using only the text below, answer three questions. For each answer quote the sentence you used. If the text does not say, write 'not in the source'." The answers arrive with quotes. She checks: the first quote is in the circular word for word; the second is in the circular but two words differ ("thirty" replaced by "sixty"); the third is not in the circular at all. She is under pressure, because the client note is due this afternoon. Her colleague says two of three quotes are at least close, so the answers can be used with small edits, and that the instruction proves the assistant stayed inside the text.

**What should she conclude?**

- A. The second quote changed a figure and the third is invented, so both are unverified: correct them from the circular and rely on a quote only when found word for word.
- B. The answers are usable with small edits, since two of three quotes are in or near the circular and the instruction shows the assistant stayed within the text.
- C. The instruction works, so rerun the request three times and use the majority of the answers, since reruns cancel out the occasional paraphrase.
- D. The instruction failed, so use web search to find the missing sentence and treat the assistant's third answer as correct once the search supports it.

**Answer:** A

- ✅ **A** — A close but not exact quote means the assistant paraphrased and called it a quote; a missing one means it was invented.
- ❌ **B** — A changed figure is an error, not a small edit, and an instruction is not proof of compliance.
- ❌ **C** — Reruns can repeat the same failure, and a majority of unchecked answers is still unchecked.
- ❌ **D** — The task is bounded to the circular; a web source changes the question and may not be the same text.

**Yaad rakho:** Quote lafz ba lafz milna chahiye. Kareeb-kareeb = paraphrase, gayab = ijaad.

*Grounded in: Just Delegate It §5 (using only the text below; quote the sentence; find one quote word for word: exact, paraphrased, or invented); §10*

---

### Q56.
A tender team at an engineering contractor has proposals from three cement suppliers and written criteria: price weighted 40%, delivery reliability 35%, exit terms 25%. They paste everything into one request asking for a recommendation, and get a fluent one with a price that looks wrong. The lead wants to split the work into four steps, so that an early mistake cannot travel unseen. The four steps are: extract the key facts into one table; compare the suppliers using only that table; score them on the weighted criteria; draft the recommendation. The team lead also wants a check after each step. She hears four different orderings from colleagues, each defended with reasons about what "focuses" the assistant. The three suppliers are all long-standing partners, the tender deadline is Friday, and the assistant's earlier extractions for the team have been consistently well formatted.

**Which ordering and check pattern follows the course?**

- A. Score against the weighted criteria first and check the scores; extract the facts the scores used and check the cells; compare using the table; draft the recommendation and check its claims.
- B. Extract facts into one table and check several cells against each proposal; compare using only the table; score and check no criterion was added; draft and check it claims only what the steps support.
- C. Extract the facts and compare the suppliers in one request and check the comparison; score and check the scores; then draft the recommendation and check it against the comparison.
- D. Extract the facts into a table and compare using the table; score; draft the recommendation; then check the table, the comparison, the scores and the draft together at the end.

**Answer:** B

- ✅ **B** — Put the step where a mistake spreads farthest first, check before you continue, and let each later step use only the previous step's output.
- ❌ **A** — Scoring before extraction builds on unchecked facts, so a wrong price flows through.
- ❌ **C** — Merging extraction and comparison removes the check at the step where a wrong price would spread farthest.
- ❌ **D** — One check at the end can only inspect the ending; an early error carried through looks fine by the time it is read.

**Yaad rakho:** Jahan ghalti sab se door tak phailti hai wo step pehle, aur har step ke baad check.

*Grounded in: AI Fluency §4.2 (process description: split by order; extraction goes first; check before you send the next request)*

---

### Q57.
An analyst at a subscription-media business suspects a price rise caused a spike in cancellations. She uploads a customer export and writes: "Confirm that the March price increase caused churn to rise, and show me the evidence." The assistant returns three persuasive charts and a paragraph. Her director notes that a payment-gateway outage and a competitor promotion also fell in March, and the export has no column for either. The analyst wants a rewrite that lets the data speak, including that it may not support her view, and she is offered four rewrites that each mention churn, March and the export. The company also plans a new mobile app next quarter, a competitor recently cut its prices, and the director's own view is that the price increase was the main driver.

**Which rewrite follows the guidance for an analysis ask?**

- A. 'Using the attached export, compute monthly churn by plan for six months either side of March, say what the data shows and cannot show, and list other possible explanations, assuming no cause.'
- B. 'Using the attached export, compute monthly churn by plan around March and give the strongest evidence that the price increase caused the change, with a caveat for other factors.'
- C. 'Analyse churn in the attached export objectively and tell me honestly whether the March price increase was responsible, showing every step of your reasoning.'
- D. 'Using the attached export and your general knowledge of subscription businesses, list the most likely causes of the March churn and rank them by how commonly they occur.'

**Answer:** A

- ✅ **A** — For analysis, tighten the data, definitions and exact question and loosen the conclusion; never state it.
- ❌ **B** — It still presupposes the conclusion and asks for support, with the alternatives reduced to a caveat.
- ❌ **C** — It states the hypothesis as the frame, gives no definitions or window, and asks for honesty in place of a design.
- ❌ **D** — It replaces analysis of the file with general-knowledge ranking, so the data is left out.

**Yaad rakho:** Analysis mein natija mat batao; data, definitions aur sawal kasso, conclusion khula.

*Grounded in: AI Prompting 2026 §7 'One loop, four kinds of ask' (analysis: tighten the data, definitions and exact question; loosen the conclusion; never state it)*

---

### Q58.
A brand team at a beverage company asks an assistant for "a 600-word launch article for our new low-sugar cola" in one request, giving tone, structure and length. The article is polished but says little: it repeats "healthy refreshment" and could describe any cola. The editor has 45 minutes. She asks whether the assistant is weak, and a colleague says a fresh chat with a stronger model would fix it. The team's earlier experience is that a first draft of anything is polished and hollow. The editor wants a process that yields an article worth publishing without a new model, and four colleagues propose their own. The launch is planned for the summer, the product manager loves the bottle design, and the editor has published several successful features on this brand before.

**Which process follows the brainstorm-iterate loop?**

- A. Load the context (audience, claims, competitors, what to avoid); ask for several angles and pick two; outline and grade; expand to bullets; then draft, grade against named criteria and fix.
- B. Ask for the full article three times in fresh chats, choose the best of the three drafts, and then ask the assistant to improve its tone and vocabulary.
- C. Ask for a 200-word summary, then expand it paragraph by paragraph until the article reaches 600 words, checking each paragraph for repetition against the previous one.
- D. Switch to the strongest model and send the same request with more detail on tone and structure, since a stronger model makes fewer generic claims in a first draft.

**Answer:** A

- ✅ **A** — The first draft is slop: polished but empty; the loop spends ten minutes on structure before any drafting.
- ❌ **B** — Three first drafts are three polished, hollow drafts; the fix is structure work before drafting.
- ❌ **C** — It expands a summary with no angle chosen and no criteria graded, so the hollowness spreads.
- ❌ **D** — More detail on tone does not add the context and options the article lacks, and the model is not the constraint.

**Yaad rakho:** Pehla draft khokhla hota hai. Context, options, outline, grade, phir draft.

*Grounded in: AI Prompting 2026 §7 (brainstorm-iterate loop; never take the first answer; load, options, feedback, repeat; the first draft is slop)*

---

### Q59.
A property developer's chief financial officer writes to an assistant: "Help me defend my decision to acquire the Gulberg site. Here is the deal memo." The assistant produces a confident, well-organised defence and no counter-arguments. The CFO's board has two sceptical directors. A colleague says the assistant has simply followed instructions, and that a smarter model would also have offered risks. The CFO wants a prompt that cannot be answered with praise or advocacy, while giving the assistant everything it needs. She lists four rewrites, each of which mentions the memo, the site and the board. The board meets next Thursday, one director previously backed a similar deal, and the CFO has already told the chairman she expects the acquisition to go ahead.

**Which rewrite best neutralises the lean toward agreement?**

- A. 'Here is the deal memo. Score my decision to acquire the Gulberg site from one to ten on financial soundness, and list any risks that a board might raise.'
- B. 'Here is the deal memo. Present the strongest case for acquiring the Gulberg site, briefly list any weaknesses the board might raise, and conclude with a recommendation to the board.'
- C. 'Here is the deal memo and my decision. What is the strongest counter-argument the board should be ready for, and what would change my decision? If the memo doesn't support it, say so.'
- D. 'Here is the deal memo. Be critical and honest about my decision to acquire the Gulberg site, and challenge any assumptions you believe are weak.'

**Answer:** C

- ✅ **C** — It removes the conclusion as a fixed point, asks for the strongest opposing case, and allows a negative answer.
- ❌ **A** — A bare score without named criteria can be as sycophantic as praise, and 'my decision' still frames it as the conclusion.
- ❌ **B** — It leads with advocacy, treats the opposing case as a brief afterthought, and never asks what would change the decision.
- ❌ **D** — Tone instructions change how a lean is expressed, but the decision is still stated as a fixed point and no named criteria are asked for.

**Yaad rakho:** 'Mera faisla defend karo' bait hai. 'Sab se mazboot etiraz kya, aur kya badle to faisla badle?'

*Grounded in: AI Prompting 2026 §6 (sycophancy: 'help me defend my decision' becomes 'what is the strongest counter-argument'); What AI Actually Is Idea 6*

---

### Q60.
A reporter at a business newsletter drafts a 900-word feature with an assistant. Her editor sends back a single general note: "Make it better." She asks the assistant to do a general sweep to improve the draft, and the result is slightly smoother but has introduced two new factual softenings and a shift of tone. She has 30 minutes left. A colleague who edits for a living says to edit in named passes and to ask for more than one draft when the stakes justify it. The reporter's piece is about a regulator's ruling on bank fees, and the two errors she is worried about are a misquoted figure and a headline that overstates the ruling.

**Which approach is best?**

- A. Send the assistant's smoother version to the editor and ask her which paragraphs still feel wrong, then fix only those, since the editor's reading is the check.
- B. Ask for one more general sweep with stricter instructions to keep every fact unchanged, and accept the result if the two softened facts are restored.
- C. Edit in named passes: clarity (does each sentence say one thing), tone for this reader, formatting of headings and length; check figures and the headline separately; ask for two drafts and edit the stronger.
- D. Ask the assistant to rewrite the whole feature in a different structure, then merge the best paragraphs of the old and new versions by hand in the remaining time.

**Answer:** C

- ✅ **C** — Named passes replace a general sweep, and a separate check on figures and the headline covers the two risks the sweep introduced.
- ❌ **A** — It passes the unresolved figure and headline risks to the editor and drops the reporter's own verification.
- ❌ **B** — Another general sweep repeats the mechanism that introduced the drift and does not check the figures and headline.
- ❌ **D** — A structural rewrite adds new text to verify and does not separate the concerns of clarity, tone and format.

**Yaad rakho:** Aam sweep nahi, naam-zad passes: clarity, tone, formatting; aur figures/headline alag check.

*Grounded in: AI Fluency §5 (the loop: edit in named passes; ask for two or three drafts; problem, why it matters, direction) and Just Delegate It §9*

---

### Q61.
A consultancy's practice lead is deciding which of four recurring tasks deserves a Project. Anthropic's own test for the decision asks three questions: does the task come back, is the background the same each time, is the output shape the same each time; two yes answers out of three earn the Project. Task A: a one-off market-entry paper for a single client, with unique background and a unique format. Task B: a weekly client summary with the same client background and a different layout each week. Task C: a monthly board report with the same background and same format every month. Task D: an ad hoc question from a colleague on how to word an email.

**Which tasks earn a Project under the test?**

- A. Task C only: a Project needs all three yes answers, and only the monthly board report has a recurring task, a stable background and a stable format.
- B. Tasks A and C: both have a stable background within their own scope, since a one-off paper also has consistent background for the life of the engagement.
- C. Tasks B, C and D: any task involving a repeated conversation with the same colleagues has the same background, and a Project holds the shared context.
- D. Tasks B and C: B returns weekly and shares its background, and C returns monthly with the same background and format, so each answers yes to at least two questions.

**Answer:** D

- ✅ **D** — Two yes answers out of three earn a Project; a recurring task with a stable background qualifies even when the layout changes.
- ❌ **A** — The test needs two of three, not all three; Task B qualifies.
- ❌ **B** — A one-off paper does not come back and has neither a repeating background nor a repeating format.
- ❌ **C** — Task D is an ad hoc question; it does not come back and has no shared output shape.

**Yaad rakho:** Project ka test: dohrata hai? background wahi? output shakal wahi? Do 'haan' kaafi.

*Grounded in: What AI Actually Is A.5 and Just Delegate It §8 (Anthropic's three-question test for a Project: does it come back, same background, same output shape; two yes answers earn it)*

---

### Q62.
An analyst reviewing an assistant's vendor-comparison table finds Vendor C's price at 1,090 in the table and 1,090 again in the summary paragraph; the source says 1,900. She replies: "Vendor C is 1,900, not 1,090. Fix." The assistant answers: "Corrected: Vendor C is now 1,900" and prints a new summary paragraph with 1,900, but the table is not reprinted. She sees that a third figure, a three-year cost that used 1,090, also exists in the response. She considers replying with a full rewrite of the brief, escalating to a stronger model, or simply accepting because the assistant said it was corrected. She has 20 minutes. The analyst also mentions that the vendor's account manager is a former colleague, that the comparison is for a renewal in the autumn, and that the assistant has been reliable on earlier tables.

**Which is the smallest intervention that works?**

- A. Escalate to the strongest tier and rerun the comparison, since failing to apply a simple correction across three places shows the current tier cannot hold the figure consistently.
- B. Reply 'Now correct the whole table and everything that depends on it', and accept the assistant's confirmation that all dependent figures were corrected in the reply.
- C. Reply naming the error and its replacement everywhere it appears (table, summary, three-year cost) and ask for all three reprinted, then check each in the result, not in the assistant's description.
- D. Rewrite the whole brief with the source price and rerun the job from the start, since a mistake that survived correction shows the original instructions were unclear.

**Answer:** C

- ✅ **C** — The smallest message that fixes it names the error and what should replace it; a claimed fix that did not happen is what the check exists to catch.
- ❌ **A** — Escalation is a later move; the cheaper step is to name the error everywhere and check the result.
- ❌ **B** — It hands the assistant the whole job again and accepts its description of the result as the evidence.
- ❌ **D** — One wrong price and its dependents call for the smallest message, not a rebuild.

**Yaad rakho:** Sab se chhota message: ghalti aur uska badal, har jagah. Phir result mein dekho, dawe mein nahi.

*Grounded in: Just Delegate It §9 (intervene: the smallest message that works; correct = name the error and what replaces it; check the fix in the result, not in AI's description)*

---

### Q63. *(Select TWO — all-or-nothing)*
A strategy analyst at a manufacturing group has four tasks and is deciding which are better with an AI assistant than with a web search engine. (1) Find the official page for the customs tariff schedule; she knows it exists and wants to land on the specific site. (2) Compare three supply-chain risk frameworks and what recent evidence says about each, drawing on several sources. (3) Find where to buy a replacement part for a 2018 forklift model; she wants a product link. (4) Plan a four-day supplier visit across three cities with constraints on budget, travel time and one supplier's holiday closures. A colleague says AI is better for all four because it is "smarter than search".

**Which TWO tasks are better with AI than with a search engine?**

- A. Task 2, comparing three frameworks with recent evidence: an assistant synthesises several sources in one place, where a search engine leaves her reading many tabs.
- B. Task 4, planning the visit: an assistant integrates several constraints at once, where searching means juggling blogs, timetables and reviews by hand.
- C. Task 3, finding a replacement part: an assistant can compare suppliers and prices across the web and choose the best option for her forklift model.
- D. Task 1, finding the official tariff page: an assistant can locate any known site, and it can quote the schedule's rates while explaining how they apply to her goods.

**Answer:** A, B

- ✅ **A** — Synthesis across sources is the strength; the search route is slower.
- ✅ **B** — Planning with multiple constraints is a strength of AI; the search route is slow.
- ❌ **C** — She wants a product link, which a search engine gives directly, and an assistant's product details may be stale.
- ❌ **D** — Landing on a specific known site is better with a search engine; an assistant's quoted rates would need checking.

**Yaad rakho:** Maloom site par jana ho ya product link chahiye: search. Kai sources ka nichor ya kai qaiyd: AI.

*Grounded in: AI Prompting 2026 §3 (when a search engine is better and when AI is better; AI synthesises evidence and integrates constraints)*

---

### Q64. *(Select TWO — all-or-nothing)*
A teacher commissions code from an assistant with a five-part brief (Goal, Input, Output, Rules, Edge cases) to grade 200 students' marks across three spreadsheets. The first script fails in two ways. It crashes on a student with a blank marks cell, and it computes the pass mark for the bilingual students using the wrong weighting because the teacher's school gives extra weight to a practical exam that she did not mention. Her Goal, Input and Output sections were complete and precise. A colleague says beginners most often skip two of the five sections, and each carries something different: one carries what only she knows, the other decides what imperfect data should do. The teacher's school recently changed its report-card design, the results are due on Friday, and two colleagues have already used similar scripts without problems.

**Which TWO sections did she leave out or under-specify?**

- A. Input: the description of the three spreadsheets did not tell the assistant which columns hold the marks, so it failed on the blank cell in one of them.
- B. Edge cases: what a blank marks cell should do is a decision about imperfect data, and leaving it out is why the script crashed on that student.
- C. Output: the report format was not precise enough about the letter grade for bilingual students, so the assistant applied a default weighting.
- D. Rules: the extra weighting for the practical exam is knowledge that only she has, so it had to be stated because the assistant cannot guess it.

**Answer:** B, D

- ✅ **B** — Edge cases decide what imperfect data should do.
- ✅ **D** — Rules carry what only you know.
- ❌ **A** — The Input section was complete; a blank cell is an edge case, not a missing description of the files.
- ❌ **C** — The Output section was complete; the wrong weighting is a rule she did not state.

**Yaad rakho:** Rules = jo sirf tum jaante ho. Edge cases = ghalat/khali data ka kya karna hai.

*Grounded in: Code You Never Write §5 (five-part brief; Rules carry what only you know; Edge cases decide what imperfect data should do; make discovery the first prompt)*

---

### Q65.
An owner of a Multan distribution firm uploads twelve months of expense data and asks an assistant to total fuel costs by month. She receives four different candidate replies in a comparison test her accountant sets up, all quoting the same annual total. She wants to know which reply actually shows that code ran on her file rather than a glance, because the number will be quoted to a lender. Her accountant says the tell is what the reply contains beyond the number. The four replies each contain a table of monthly totals and a sentence about the trend, and their annual figure is PKR 6.41 million. The accountant is retiring next year, the firm has a new bank, and the owner's fleet manager says fuel prices rose sharply in the summer.

**Which reply shows that code was run?**

- A. The reply that shows the code, states it read 2,431 rows and columns date, category and amount, reports monthly totals as computed, and lists the 14 blank-date rows.
- B. The reply that states it is highly confident in the totals, has cross-checked them against typical fuel consumption for a distribution fleet, and reports 6.41 million.
- C. The reply that gives the monthly totals with a short explanation in plain English of how fuel costs are usually summed and reports 6.41 million as the annual figure.
- D. The reply that gives the monthly totals with a note that the analysis covered the full year, that amounts were summed by month, and that the annual total is about 6.41 million.

**Answer:** A

- ✅ **A** — A code block, row counts, column names and a statement of what was computed are the evidence; a reply without them is an opinion about your data.
- ❌ **B** — Confidence and a plausibility comparison are not evidence that a computation ran on this file.
- ❌ **C** — A general explanation of the method is not a record that the method was run on her data.
- ❌ **D** — It describes a method in words but shows no code, row count or column names.

**Yaad rakho:** Code block, row count, column names: ye saboot. Sirf 'confident' aur tarika bayan nahi.

*Grounded in: Code You Never Write §4 (make the AI's hands move; the tell: no code block, no row counts, no 'here is what I computed' is an opinion about your data)*

---

### Q66. *(Select TWO — all-or-nothing)*
An FDE is designing a tutoring agent for a school network and drafts three statements for its specification. Statement 1: "The agent must never give the answer before the student has attempted the problem." Statement 2: "Review the student's working first for correctness, then for method, and last for presentation." Statement 3: "Produce a one-page feedback note with the mark, two strengths and one improvement, in plain language." The FDE knows the framework distinguishes what to do, how to approach the work, and how the agent behaves for people who are not her and will never see the instruction. The specification will be deployed to 3,000 students and must persist across all of their sessions.

**Which TWO classifications are correct?**

- A. Statement 2 is a product description, because it specifies the check the assistant must perform and product description covers all checks that apply to the output.
- B. Statement 1 is a performance description: it defines how the agent behaves toward students on its own, and at system scale it belongs in a permanent instruction such as a system prompt.
- C. Statement 2 is a process description: it defines the order of work, and a reusable, ordered method like this is what a Skill file packages.
- D. Statement 3 is a performance description, because a feedback note is delivered to students and therefore defines how the agent behaves toward them.

**Answer:** B, C

- ✅ **B** — Performance description defines behavior for people you will never meet; at scale it becomes standing behavior.
- ✅ **C** — Process description is how the work is approached: the steps and the order.
- ❌ **A** — It describes how to approach the work in an order, not what output is wanted.
- ❌ **D** — It defines the output: its content, format and length, which is a product description.

**Yaad rakho:** Kya banana hai = product. Kis tarteeb se = process. Doosron ke saath kaisa behave = performance.

*Grounded in: AI Fluency §4 (Description: product, process and performance; performance description at system scale; system prompt and SKILL.md)*

---

## Domain 3 — Product and Model Selection (12% — 12 questions)

### Q67.
A telecom's support-operations manager has three jobs to assign on Claude. Job X: relabel 9,000 short tickets into six fixed categories, high volume and low depth, where speed and cost dominate. Job Y: everyday drafting and summarising of internal updates. Job Z: analyse one 140-page network-sharing agreement whose clauses cross-reference each other, holding the whole structure coherent at once. She knows the ladder from the fast, cheap model through the middle model to the top model, and knows thinking is a separate switch. Her deputy has proposed four allocations that each use every tier once, differing only in which job gets which, and a colleague says Job Z should just use "the Thinking model".

**Which allocation follows the course's selection logic?**

- A. X on the small, fast tier; Y on the mid-tier default; Z on the top tier, with thinking a switch to consider rather than a model name.
- B. X on the small, fast tier; Y on the top tier; Z on the mid tier, with thinking switched on for Y since internal updates go to executives.
- C. X on the top tier; Y on the mid tier; Z on the small, fast tier, with thinking switched on for Z to compensate for the smaller model.
- D. X on the mid tier; Y on the small, fast tier; Z on the top tier, with thinking left off because it costs extra tokens on long documents.

**Answer:** A

- ✅ **A** — Drop down for bulk low-depth work, default to the middle, escalate up for depth.
- ❌ **B** — Routine drafting does not need the top tier, and the depth job is the one that does.
- ❌ **C** — This inverts the ladder; thinking does not make a bulk-tier model hold a large cross-referenced structure coherent.
- ❌ **D** — Bulk relabelling is the small tier's job and the mid tier is the everyday default for drafting.

**Yaad rakho:** Bulk = chhota tez, roz ka = beech wala, gehra = top. Thinking alag switch hai, model ka naam nahi.

*Grounded in: Quick Reference §2 and What AI Actually Is A.3 (the ladder: default to the middle, escalate up for depth, drop down for bulk; thinking is a separate switch)*

---

### Q68.
A policy consultant has kept one Claude chat open for 20 working days while drafting a 200-page report, pasting in each new draft, appendices and dozens of Q&A turns. Her usage allowance is running out earlier each week; replies are slower; and the assistant recently used a different spelling convention from the one she set in her first message. A colleague argues that because the model is stateless, "nothing carries over so cost cannot grow", and another that a newly announced model with a larger context window makes restarting unnecessary. Her manager wants a reasoned recommendation on restarting versus stretching the same chat, expressed in terms of how the model works. The manager also mentions the report was commissioned by a ministry, that its first chapter was well received, and that the consultant has used three different laptops during the drafting.

**Which explanation and recommendation are correct?**

- A. A larger context window removes both the cost growth and the forgetting, so upgrade and continue in the same chat, since the assistant will then hold all 20 days at once.
- B. Every turn re-reads the whole transcript, so cost and dilution grow, and a larger window buys room, not attention: summarise decisions and rules, restart fresh, and put standing material in a project.
- C. Because the model is stateless nothing carries over, so the cost is flat; the drift is random and restarting would lose the report's continuity, so keep stretching the chat.
- D. The assistant stores memory of the chat between turns, so delete the earliest messages to free space and rely on that memory to keep the decisions and spelling rule.

**Answer:** B

- ✅ **B** — Chat history is the transcript replayed each turn; the window is finite and shared, and a fresh chat is an empty window.
- ❌ **A** — A bigger window still replays everything each turn, still shares space, and still dilutes early instructions.
- ❌ **C** — Stateless means the transcript must be re-sent, which is exactly why cost grows.
- ❌ **D** — There is no memory inside the model; the transcript is the memory, and deleting it deletes the decisions.

**Yaad rakho:** Har jawab poori transcript dobara parhta hai. Bara window jagah deta hai, dhyan nahi: summary + naya chat.

*Grounded in: What AI Actually Is Ideas 2 and 5 (stateless; transcript replayed every turn; context window finite and shared; start a fresh chat); Quick Reference §3*

---

### Q69.
A strategy director at a consumer-goods company sends four requests this morning and wants each routed correctly. Request P: today's PKR to USD rate for a note. Request Q: a comparison of three pricing strategies from figures she has already attached, where the difficulty is reasoning across trade-offs. Request R: a thorough, cited investigation of the current cold-chain logistics market, to be given to a board committee. Request S: the latest approved pricing policy, which lives in the company's own document systems. A colleague says research mode should be used for everything so nothing is missed. She has four allocations to choose from, each using all four routes: web search, thinking, research, and connected apps or workplace search.

**Which allocation is correct?**

- A. P to web search; Q to research; R to thinking; S to connected apps or workplace search.
- B. P to research; Q to thinking; R to web search; S to connected apps or workplace search.
- C. P to web search; Q to thinking; R to research; S to connected apps or workplace search.
- D. P to web search; Q to thinking; R to research; S to web search.

**Answer:** C

- ✅ **C** — One current fact is a search; reasoning over supplied figures is thinking; a cited multi-source investigation is research; internal information needs connected apps.
- ❌ **A** — Q is reasoning over supplied figures, not an investigation; R needs many cited sources, not more thinking.
- ❌ **B** — It spends deep research on a single fact and gives a board investigation only a search.
- ❌ **D** — The approved internal policy lives in the organisation's systems, which the open web does not reach.

**Yaad rakho:** Ek fact = search, gehri soch = thinking, cited report = research, apna data = connectors.

*Grounded in: Quick Reference §8 (search, thinking or research: route the question before you send it); What AI Actually Is A.8*

---

### Q70.
A consulting firm wants to capture how it writes board papers (an eight-section structure) and give it to all 60 staff. Staff use Claude in a browser; a few use a coding agent from another vendor; the firm may change chat product next year. It is on a Team plan. Three ideas are on the table: a custom GPT, a Project holding the template, and a Skill. The knowledge partner adds that the Skill should be shared through the organisation's directory, that sharing is off by default and an owner must enable it, and that colleagues will receive view-only copies. A colleague asks what happens when the partner improves the original later and whether the method will travel to the other vendor's agent.

**Which statement is correct?**

- A. Use a Project: each colleague duplicates the Project with the template, edits to the original propagate to every copy, and any product that supports projects applies it the same way.
- B. Package it as a Skill: an owner enables sharing, colleagues get view-only copies that update with the original, and the open-standard SKILL.md travels, though each product's install and permissions need checking.
- C. Package it as a Skill and email the folder to all 60 staff, who each install their own copy, which then updates when the partner edits the original.
- D. Build a custom GPT: colleagues open the same assistant, the partner's edits update it, and the instructions travel to any vendor's tools that read GPT configurations.

**Answer:** B

- ✅ **B** — Shared Skills follow the original's edits; the format is portable while product-specific details are not.
- ❌ **A** — A Project stores knowledge for a stream of work; it does not give a portable, auto-updating method.
- ❌ **C** — Emailed copies are independent; shared, view-only copies through the organisation's directory are what follow the original.
- ❌ **D** — Custom GPTs live only inside ChatGPT.

**Yaad rakho:** Skill: directory se share, view-only copy original ke saath update. Custom GPT ek vendor mein qaid.

*Grounded in: Skills & Connectors §14 and Part 4 (sharing is off by default; shared skills are view-only and update; the Agent Skills open standard); Quick Reference §7*

---

### Q71. *(Select TWO — all-or-nothing)*
An operations lead at a regional bank wants an assistant to pull daily card-dispute counts from the CRM. A supported connector exists but needs an administrator to enable it, which takes a week. She has a quicker idea: use a browser extension that works inside the staff member's logged-in Chrome to open the CRM and copy the numbers. Her colleague adds that "MCP is just USB-C for AI tools, so connecting is routine". The bank's policy requires the narrowest practical access, and the connector's admin will ask four permission questions before enabling it. She wants to know which two of a longer list belong to the four questions. The firm's founder personally wrote the original board-paper template, staff are located in three countries, and the knowledge partner has been with the firm for twelve years.

**Which TWO are among the four questions to ask before connecting a tool?**

- A. What can it read: what data, files and systems the connector could reach where it runs, in the account it is connected to.
- B. Can it write, send, delete or buy: whether it can take consequential, hard-to-reverse actions in another system on the user's behalf.
- C. Is the vendor large enough to be trusted: a well-known publisher removes the need to ask what the connector can read or do in the account.
- D. Does the connector use the standard plug: if it speaks MCP, then its access is the same as any other MCP tool's and needs no separate decision.

**Answer:** A, B

- ✅ **A** — The first question is about reach.
- ✅ **B** — The second question is about actions.
- ❌ **C** — The questions are what it can read, what it can do, whether you trust the source, and whether you are allowed; size is not one.
- ❌ **D** — The plug is standard; the access is not, and connecting is a decision about trust.

**Yaad rakho:** Connect karne se pehle chaar sawal: kya parh sakta, kya kar sakta, source par bharosa, ijazat hai?

*Grounded in: Quick Reference §8 (connections are permission decisions: what can it read, can it act, do I trust the source, am I allowed; the plug is standard, the access is not)*

---

### Q72.
A compliance manager schedules a weekly cloud task compiling a regulator digest from two sources: a cloud drive reached through a connector, and a folder on her office workstation reached through the vendor's desktop bridge. On two Mondays, while she was on leave and the workstation was powered off, the run "completed" but the local section was empty. The vendor page says schedules "run in the cloud". A colleague says the bridge is a convenience, not a custody loophole, and that cloud versus local is a question about where each tool executes. The manager can move the local folder to cloud storage, keep the schedule and add a reminder, or run the task on an always-on machine.

**Which reading and decision are correct?**

- A. Keep the design and add a reminder to switch the workstation on each Sunday, since the bridge then supplies the folder and the cloud schedule is enough.
- B. The runs succeeded, since a completed status means every section was fetched, and the empty local section means the folder had no new material on those Mondays.
- C. The cloud clock ran but the bridged tool went offline with the workstation; schedules are device-independent only if every tool is reachable, so use cloud storage or an always-on local session.
- D. The schedule is broken because cloud tasks cannot use a desktop bridge; reinstall the bridge and reconnect the folder before the next Monday's run.

**Answer:** C

- ✅ **C** — Ask where the loop runs and where each tool executes; a bridge borrows a local tool but does not move the cloud into it.
- ❌ **A** — A reminder makes the schedule depend on a person and a device again, which defeats the point of a device-independent run.
- ❌ **B** — Ran is not the same as worked; an empty section is a symptom to investigate.
- ❌ **D** — Cloud runs can use a bridge while the desktop is online; the problem is what happens when it is not.

**Yaad rakho:** Cloud clock chalta hai, magar bridged local tool band ho to kaam adhoora: har tool cloud-reachable ho.

*Grounded in: General Agents on the Web §2, §9 and Appendix F (cloud-only versus cloud plus bridge versus local; a cloud clock is not enough; ran is not worked)*

---

### Q73.
A finance analyst needs an agent to pull figures from a supplier's web portal that has no connector, and from a page open in her own Chrome, where she is logged in to the company's expenses site. Two tools are available: the vendor's built-in browser, which is part of the desktop app and gets its own browser for delegated work, and a Chrome extension that works inside her existing signed-in browser context. The security team's guidance is to use the most structured tool that can do the job and to grant the smallest scope. She asks which tool suits which page, and what to watch for. The analyst's manager is keen to finish quickly, the company's security team has just published a new policy, and the finance department was recently audited without findings.

**Which choice follows the guidance?**

- A. Use the built-in browser for the portal with no connector, and the Chrome extension only for the page in front of her, remembering it inherits her signed-in session's sensitivity.
- B. Use full computer use for both pages, since it can click any screen and does not depend on the browser's login state or on the presence of a connector.
- C. Use the built-in browser for both, and give it her expenses-site login for the second page, since a single tool is simpler to govern than two.
- D. Use the Chrome extension for both, since it works in her own context and reaches only what she can already see, which makes it the narrowest option for both pages.

**Answer:** A

- ✅ **A** — Choose the browser path by what the work touches; a signed-in session brings its whole reach with it.
- ❌ **B** — Computer use is the highest-risk path; connector before browser, browser before computer use.
- ❌ **C** — Handing a delegated browser her credentials moves the sensitive session into it rather than using the page in front of her.
- ❌ **D** — It inherits the sensitivity of the whole signed-in session, which is broader than a separate delegated browser for the portal.

**Yaad rakho:** Connector, phir browser, phir computer use. Chrome extension tumhari poori signed-in session ki hassasiyat le aata hai.

*Grounded in: General Agents on the Web §6 (reach paths: connector, built-in Cowork browser, Claude in Chrome, computer use; use the most structured tool; smallest scope)*

---

### Q74. *(Select TWO — all-or-nothing)*
A shared-services team is assigning autonomy modes in a desktop coworking product. W1: a brand-new workflow on an unfamiliar vendor portal that includes a form submission which cannot be recalled. W2: a proven, bounded weekly reporting job watched many times, where wrong output is easily corrected and interruptions are costly. W3: an experimental clean-up over a large shared folder, run by someone new to agents. The product offers Manual, Auto and Skip. The team lead notes that Auto's extra safety check consumes more usage, and that Manual does not automatically produce a plan for approval, so plan-first has to be written into the brief. The team also has a quarterly usage limit, its manager has just attended a vendor conference, and the shared-services centre has offices in two cities.

**Which TWO assignments are the best matches?**

- A. W3 in Manual, since a newcomer working across a large shared folder should approve consequential actions, and deletions may skip the recycle bin.
- B. W1 in Auto, since the safety classifier screens each action and will block the irreversible form submission if it is unsafe, without the interruptions of Manual.
- C. W2 in Skip, since a proven job that needs no interruptions gains most from removing every check, and Auto's extra usage cost is avoided.
- D. W1 in Manual, with plan-first written into the brief, since the workflow is new, unfamiliar and includes an irreversible action.

**Answer:** A, D

- ✅ **A** — Manual suits sensitive or hard-to-reverse actions; the beginner's first sessions should be tightly scoped.
- ✅ **D** — Manual suits new workflows and hard-to-reverse actions; plan-first is an instruction, not a guarantee of Manual.
- ❌ **B** — Auto suits proven, bounded workflows; an irreversible action on an unfamiliar site deserves the strictest gate.
- ❌ **C** — Skip removes ordinary approvals and the Auto action check; Auto is for proven, bounded work, and Skip is rarely right for beginners.

**Yaad rakho:** Naya/anjaan/undo-na-hone-wala aur newcomer: Manual. Sabit aur mehdood: Auto. Skip beginners ke liye nahi.

*Grounded in: General Agents on the Web §7-8 (Manual, Auto, Skip; match the gate to blast radius; Manual does not create a plan; plan-first is an instruction) and Prompting 2026 §11*

---

### Q75.
A clinic group's manager wants a coworking agent in the vendor's cloud, with a desktop bridge, to read a folder of patient discharge summaries and draft follow-up letters. She says the group is on an Enterprise plan, that "Enterprise means approved for health data", that the files stay on the clinic's computers because the bridge only reads them, and that Manual mode will make it safe. The clinic's compliance officer has not been asked, and no business associate agreement has been discussed. The letters need patient names attached to diagnoses. A competitor clinic, she adds, already uses the same setup. The clinic group has sixty staff, opened a new branch last year, and its competitor's demo of the same setup was widely praised at a recent industry meeting.

**What is the correct step before any upload?**

- A. Proceed on the Enterprise plan after removing the patient names, since removal ends the health-privacy obligation and the letters can be re-personalised later.
- B. Proceed with Manual mode on, since an approval on each action makes the use compliant and the bridge keeps the files on the clinic's own machines.
- C. Proceed on the strength of the competitor clinic's identical setup, since an industry peer using the product is evidence that the surface is approved for health data.
- D. Stop and get a written compliance answer for this exact surface, including the agreement the vendor must sign; availability isn't permission and a bridge doesn't move the cloud's processing.

**Answer:** D

- ✅ **D** — Regulated work needs the written answer before the upload, not after.
- ❌ **A** — The letters need the names, so redaction breaks the task, and residual details may still identify people.
- ❌ **B** — Approval modes do not substitute for the compliance answer, and a cloud session reading a local file through a bridge still processes it in the cloud.
- ❌ **C** — A peer's use is not an approval for this clinic; availability is not permission.

**Yaad rakho:** Plan ka naam = ijazat nahi. Bridge cloud ki processing nahi rokta. Likhit compliance jawab pehle.

*Grounded in: General Agents on the Web §10 (regulated work: stop and verify; a bridge is not a custody loophole; availability is not permission; HIPAA, PHI, BAA); Governance §2.4*

---

### Q76.
A packaging-firm inventory analyst uploads a photo of a warehouse shelf and asks an assistant to read the 14-character batch codes printed on small labels. It returns confident codes for all 22 labels; a spot check finds four with a swapped or misread character. She then asks the assistant to count how often the letter Z appears across the codes, and the count is off by three. Her manager proposes escalating to the top tier with thinking on, and a colleague notes that pictures are cut into patches that become tokens, just as text becomes tokens, and that exact character-level work is unnatural for the model. The warehouse was recently reorganised, the analyst has ten years' experience with inventory systems, and the manager says the labels were printed by a supplier known for good quality.

**What is the best approach?**

- A. Ask the assistant to report its confidence on each code and manually check only the ones it rates as uncertain, since it knows where small print is hardest to read.
- B. Accept the codes but ask the assistant to spell each one out letter by letter, since spelling out forces the model to see individual characters in the image.
- C. Escalate to the top tier with thinking on and ask it to read each code twice, since reasoning improves accuracy on fine detail and repeated reads will remove the misreads.
- D. Treat character-exact reading and counting as a weak spot at any tier: have codes transcribed and checked against the label, count with code, and verify a sample against the physical labels.

**Answer:** D

- ✅ **D** — A patch is a chunk, so small print inside an image is the strawberry problem again; a number that matters is computed and tested.
- ❌ **A** — Confidence is a learned style with no link to correctness; the four errors were confident.
- ❌ **B** — Spelling out helps text counting, but for an image the characters are still read from patches, and a check against the label is needed.
- ❌ **C** — Thinking is more prediction; it can narrow but not close a gap in exact character reading.

**Yaad rakho:** Chhoti chhapi hui likhayi (image ke patch) mein exact character parhna kamzor. Label se check karo.

*Grounded in: What AI Actually Is Ideas 4 and 7 (tokens; images are patches, small print is the strawberry problem; jagged frontier); Code You Never Write §6*

---

### Q77. *(Select TWO — all-or-nothing)*
A team lead at a consultancy has been using the top tier for all client-facing work and the smallest tier for everything else, on the rule "client-facing means top". Her usage allowance is running out by mid-month. A trainer says the team's habit reflects a common misconception, and that the objective tested on the certification exam is to align model selection with task requirements (cost, speed, quality), not to memorise names, because names rotate every few months. Two of the team's client-facing tasks are: reformatting an agreed set of findings into the client's template, and synthesising four conflicting regulatory sources into one coherent recommendation. The consultancy has offices in three cities, the trainer's session was rated highly by participants, and the company recently switched its email provider.

**Which TWO statements are correct?**

- A. The durable objective is the ladder logic (default to the middle, drop down for bulk, escalate for depth); the model names are labels a later edition would rotate.
- B. The names are what the exam tests, so the team should memorise Haiku, Sonnet and Opus and assume the ranking will stay the same when the ladder is next updated.
- C. The rule is sound, because a client-facing error costs more than an internal one, so the top tier should be used for every task that reaches a client regardless of complexity.
- D. Selection follows task complexity, not audience: the template reformat doesn't need the top tier and the four-source synthesis does, whoever the audience is.

**Answer:** A, D

- ✅ **A** — The logic survives the next rotation; the specific names do not.
- ✅ **D** — 'Client-facing' describes who receives the output, not how hard the task is.
- ❌ **B** — Names rotate; the selection logic is the durable skill, and the ranking moves with each release.
- ❌ **C** — It confuses consequence of error, which a review gate handles, with the capability a task needs.

**Yaad rakho:** Tier task ki pechidgi se chuno, audience se nahi. Naam badalte rehte hain, ladder ka usool nahi.

*Grounded in: What AI Actually Is A.3 (the ladder; two exam objectives: align selection with task requirements versus differentiate model types; the first survives rotation); Quick Reference §2*

---

### Q78.
A pair of associates at an advisory firm evaluate two assistants on a real task from their week: drafting a two-page risk summary from a client file. They run the same request in both and compare outputs, then, as the course suggests, ask each assistant to state in three sentences what additional context would have helped it do the task better. The first assistant's answer to the task is slightly longer and better formatted; the second's list of missing context is sharper. One associate argues they should now pick a "winner" and standardise. The other notes that the exercise is a record of two runs on one day, that models change fast, and that the second comparison usually teaches more.

**Which conclusion follows from the course?**

- A. Pick the assistant that gave the sharper list of missing context, since an assistant that can say what it lacks is the more trustworthy of the two for client work.
- B. Run the same task in a third assistant and pick the one that at least two of the three outputs agree with, since majority agreement is the best test of quality.
- C. Pick the assistant whose output was longer and better formatted as the standard, since a single real-task comparison on the firm's own work is the most reliable ranking available.
- D. Treat it as platform awareness, not a ranking: record what each did and what each said it lacked, use the missing-context lists to improve the brief, and re-run periodically.

**Answer:** D

- ✅ **D** — The comparison shows how a brief travels and where each tool differs; a ranking made today is not true next month.
- ❌ **A** — A confident, sharp self-description is not evidence of better work; the lists are material for improving the brief.
- ❌ **B** — Agreement among outputs from a shared brief does not test correctness, and it turns the exercise back into a ranking.
- ❌ **C** — One run on one day is an observation, not a ranking, and formatting is not the same as correctness.

**Yaad rakho:** Do assistants ki tulna ranking nahi, record hai: kya kiya, kya kami batayi. Brief behtar karo.

*Grounded in: Quick Reference §1 and §9 (platform awareness; run the same task in both; compare what each said it was missing); Just Delegate It §11 (a record, not a ranking)*

---

## Domain 5 — Configuration and Knowledge Management (12% — 12 questions)

### Q79. *(Select TWO — all-or-nothing)*
A finance team built a Skill for month-end client summaries, and it has two symptoms. On requests like "prepare the March summary for DEMO Trading" it never starts. On a request like "quickly total these three numbers" it starts and produces a four-section month-end report nobody wanted. The Skill's description reads "Helps with reports." The author has already added 300 words of rules to the body without effect, and is now considering renaming the folder or moving the Skill into a client Project. A colleague explains that the assistant keeps only the description in view and opens the instructions when a request matches, and that a line can also say when not to use the Skill.

**Which TWO edits fix both symptoms?**

- A. Add more detailed rules to the instruction body describing the four sections, since the assistant reads the whole Skill when deciding whether a request matches it.
- B. Rename the folder to 'month-end-client-summary' and move the Skill into a client Project, since a Project loads it only for the requests where it belongs.
- C. Add a negative trigger to the description, such as 'Do not use for one-off calculations or quick questions', so it stops taking over unrelated requests.
- D. Rewrite the description as what it does, when to use it and the exact phrases people say ('client summary', 'monthly close'), so it fires on the right requests.

**Answer:** C, D

- ✅ **C** — A negative trigger helps when a Skill fires too eagerly.
- ✅ **D** — A sharp description is what makes the right Skill fire at the right moment.
- ❌ **A** — Relevance is judged from the description alone; the body loads only after a match.
- ❌ **B** — The folder name is not the trigger, and a Skill is enabled at the account level rather than scoped to a Project.

**Yaad rakho:** Skill kab chale: sirf description tay karti hai. Kya, kab, alfaaz, aur 'in ke liye nahi'.

*Grounded in: Skills & Connectors §11-13 (the description decides whether a skill fires; what it does, when, exact phrases; negative trigger; progressive disclosure)*

---

### Q80.
A principal at a Karachi advisory firm asks her assistant, as the course suggests, to "show me what you currently remember about me, as a plain list". The list includes: her preference for short answers; a note that she is "negotiating the Clifton lease renewal", a deal that closed in March; a client's confidential acquisition target mentioned once in a chat; and a comment about a former colleague she would not want on a shared screen. Memory is on. The firm is on an organisation plan, and the principal wonders whether to switch it off, use incognito chats for sensitive matters, or just prune. A colleague says memory-off means nothing is retained anywhere. The principal has used the assistant daily for a year, her firm has recently added two new partners, and a client is asking about the firm's data practices.

**Which is the right approach?**

- A. Delete only the two sensitive items and keep the rest, since a stale lease note is harmless, and re-check the memory once a year with the firm's annual policy review.
- B. Decide keep, correct or delete for each item, monthly and when roles change; use incognito for sensitive subjects, remembering it is memory-free not trace-free and organisation retention and exports still apply.
- C. Switch memory off permanently and use ordinary chats for everything, since memory-off means that nothing about the principal or her clients is retained anywhere in the system.
- D. Keep memory and use incognito for everything client-related, since incognito chats are excluded from history and from organisational retention and cannot appear in exports.

**Answer:** B

- ✅ **B** — Stored context goes stale and can embarrass; review it on a schedule, and know what each control does and does not decide.
- ❌ **A** — A stale note quietly shapes answers, and yearly is too slow; each item gets a keep, correct or delete decision on a shorter cycle.
- ❌ **C** — Memory-off stops the profile note, not retention or export of the chats themselves.
- ❌ **D** — Incognito is not deletion; on organisation plans those chats follow retention and appear in standard exports.

**Yaad rakho:** Memory ko schedule par dekho: rakho, theek karo, hatao. Incognito trace-free nahi, sirf memory-free.

*Grounded in: Quick Reference §5 and exercise 4 (audit what is remembered; keep, correct or delete; memory-free is not trace-free); Governance §2.5-2.6*

---

### Q81.
A Project called "Quarterly Board Reporting" holds last quarter's financial model, a style guide and standing instructions on tone. This quarter's deck arrives beautifully formatted and quotes last quarter's revenue and margins throughout. The associate says the assistant "should have noticed" because this quarter's figures were pasted into the chat. The Project owner has not opened the Project for months. A review lists four things that could be the cause: the standing instructions, the style guide, the financial model file, and the chat's context length. The team wants the single most likely cause and the review question that would have found it earliest. The board meets quarterly, the associate has been at the company for two years, and the style guide was praised in a recent internal review.

**Which cause and review question are best?**

- A. The chat's context length is the cause: the pasted figures were pushed out of the window by earlier text, so the review question is how long the conversation had run.
- B. The standing instructions are the cause: they omit a rule to prefer pasted figures, so the review question is whether the instructions cover every source of numbers.
- C. The style guide is the cause: it carries last quarter's example figures, so the review question is whether examples in the guide have been replaced each quarter.
- D. The model file is stale configuration: nothing errors and the assistant can't tell it is old; the question is whether every source the Project reads is still current, checked by reading each date.

**Answer:** D

- ✅ **D** — Stale configuration is the one that fails silently; a scheduled review of the Project's files finds it.
- ❌ **A** — A stale file explains the exact figures quoted; a long chat would show degradation, not last quarter's specific numbers.
- ❌ **B** — An instruction to prefer pasted numbers patches one symptom and leaves the stale file and other outputs using it.
- ❌ **C** — Nothing in the scenario points to the style guide; the file that quotes last quarter's revenue and margins is the model.

**Yaad rakho:** Purani file mein sab kuch theek dikhta hai; koi error nahi. Har source ki tareekh kholkar dekho.

*Grounded in: Quick Reference §5 (stored context goes stale quietly) and Workflow Design §11 (stale configuration fails silently; the twin of the unstaffed gate)*

---

### Q82.
A legal department's Claude Project holds 500 pages of policies as knowledge, plus a short set of project instructions. Users say the assistant sometimes misses a rule that is written in the knowledge files, and, separately, always follows the rule "never cite a case older than 2015" that sits in the instructions. An administrator explains that when a project's knowledge grows past what fits in the context window, the product searches it and fetches relevant parts instead of loading everything. The head of legal wants the missed rules to be reliably followed and asks where each kind of rule belongs. A colleague proposes moving all 500 pages into the instructions. The department has 40 lawyers, three offices, and a policy library that was digitised last year at considerable cost and with a well-received launch.

**Which explanation and change are correct?**

- A. Delete the instructions and keep only the knowledge files, since two sources of rules create conflicts and retrieval treats knowledge files as authoritative.
- B. Instructions load into the window every time while a large knowledge base is retrieved on demand: keep always-apply rules short in the instructions, and point questions at the relevant document.
- C. Move all 500 pages into the instructions, since text in the instructions is always available and the assistant will then apply every rule in the policies consistently.
- D. Leave everything in knowledge and ask the assistant to read all 500 pages before each answer, since retrieval only misses rules when the assistant has not been told to read them.

**Answer:** B

- ✅ **B** — A project is a pre-loaded window with a retrieval fallback; rules that must always apply belong where they always load.
- ❌ **A** — The instructions are why one rule is always followed; removing them loses the always-on layer.
- ❌ **C** — The instructions share the same finite window; loading 500 pages there crowds out the work and dilutes everything.
- ❌ **D** — Retrieval is an automatic choice of relevant parts; an instruction to read everything does not change what fits in the window.

**Yaad rakho:** Instructions har baar window mein; bara knowledge zaroorat par retrieve hota hai. Lazmi rules chhote aur instructions mein.

*Grounded in: Quick Reference §4 (project retrieval when knowledge outgrows the window; instructions versus knowledge); What AI Actually Is A.5 (a project is a pre-loaded window)*

---

### Q83.
An analyst is explaining how the assistant uses a Skill, and draws four statements on a whiteboard for a colleague. Statement 1: the whole SKILL.md, including all instructions, sits in the window at all times, so long Skills slow everything down. Statement 2: only the frontmatter (name and description) is kept in view, the instructions load when a request matches, and detailed reference files are opened only when needed. Statement 3: the assistant reads the instructions of every installed Skill to decide which one is relevant to a request. Statement 4: a Skill's scripts run continuously in the background and keep their results in the window for later requests. She asks which is right and why it lets a team install dozens of Skills.

**Which statement is correct?**

- A. Statement 1: keeping the entire SKILL.md in the window guarantees the assistant applies every instruction consistently, at the cost of slowing down when many Skills are installed.
- B. Statement 3: the assistant reads every installed Skill's instructions to judge relevance, which is why a precise description matters less than the quality of the rules.
- C. Statement 4: Skill scripts run in the background and hold their results in the window, so Skills carry state from one request to the next within a chat.
- D. Statement 2: progressive disclosure keeps a short description of each Skill in view, loads instructions on a match, and opens references only when needed, so dozens of Skills don't slow anything.

**Answer:** D

- ✅ **D** — The frontmatter is the only part always loaded; it decides relevance.
- ❌ **A** — The instructions are not held in the window at all times; that is what progressive disclosure avoids.
- ❌ **B** — Relevance is judged from the description, so a sharp description matters most.
- ❌ **C** — Skills load when a request matches; they do not run continuously or carry state between requests.

**Yaad rakho:** Sirf description hamesha nazar mein; instructions match par; references zaroorat par.

*Grounded in: Skills & Connectors §2 and §11 (progressive disclosure; frontmatter always loaded; instructions on match; references level three); What AI Actually Is Idea 5*

---

### Q84.
A strategy consultant uses one vendor's assistant with its memory feature, project files and a saved set of instructions, and is asked to move to another vendor's product because the client requires it. She worries she will lose what the assistant "knows about her". A colleague tells her the state spine has several layers: session history, projects, semantic memory, standing instructions, and a user-owned context file. She asks which of these she can keep, read, and take with her, and which are held in the vendor's account in the vendor's format. She has three weeks to prepare. The consultant has used the vendor's product for two years, the client is a large multinational, and her manager has praised her for her adaptability.

**What should she do?**

- A. Keep a user-owned, readable context file with her role, audience, limits and standing rules, and export project files to storage she controls; vendor memory and session history stay in the vendor's account.
- B. Rely on the semantic memory, exporting it as a text file when she leaves, since memory is designed to be portable and readable across vendors.
- C. Copy the chat transcripts of her old sessions into the new product, since session history is the assistant's record of what it knows about her and travels with the text.
- D. Recreate her standing instructions from memory in the new product and skip the files, since instructions are the only layer that affects behavior in a new workspace.

**Answer:** A

- ✅ **A** — Persist critical facts in a portable copy you own; put each fact in the narrowest layer and keep a copy of what is critical.
- ❌ **B** — Memory is best-effort, per-vendor and not a reliable portable record; a file she maintains is.
- ❌ **C** — Session history describes one task and is not the same as memory or standing behavior.
- ❌ **D** — Reference files and a context file carry knowledge the instructions do not, and recreating from memory loses items.

**Yaad rakho:** Zaroori cheez apni file mein rakho jo tum parh sako aur le ja sako; vendor ka memory tumhara nahi.

*Grounded in: General Agents on the Web §4 (persistence is a stack; put each fact in the narrowest layer; keep a user-owned portable context file; session history is not memory)*

---

### Q85.
A compliance team's cloud agent drafts monthly vendor-risk memos and saves them into the task's working area and into the vendor's platform storage. The team calls that the record. Their regulator requires seven years' retention in a form the firm controls. A partner argues platform storage is durable, searchable and "safe", so the memos need no other home; a junior notes that the working area is cleared when the task ends. When the regulator asked for a memo from two years ago, only a partial copy in the vendor's own format existed. The team lead is asked to redesign so that finished work exits the platform, and lists four destinations. The regulator has changed its chairman recently, the firm has an excellent record of on-time filings, and the vendor's sales representative described platform storage as best in class.

**Which is the right destination for a finished memo?**

- A. A system the firm controls, such as its records system, drive or repository, with its own retention rules; the task area is scratch and platform storage stays in the vendor's custody.
- B. The vendor's platform storage, with a longer retention setting, since it survives the task and a longer setting satisfies the seven-year requirement without a second copy.
- C. The session history, pinned so that it is not cleared, since session history records each task in full and is searchable when the regulator asks.
- D. The assistant's semantic memory, with an instruction to remember every memo, since memory carries facts across sessions and can reproduce them on request.

**Answer:** A

- ✅ **A** — Three tiers: scratch, vendor custody, and your own system of record; finished work exits the platform.
- ❌ **B** — Platform storage stays in the vendor's custody, format and rules, whatever the retention setting.
- ❌ **C** — Session history describes what happened in one task and is not a system of record.
- ❌ **D** — Memory carries facts and preferences, not compliant records, and is not proof of what was sent.

**Yaad rakho:** Task area scratch, platform storage vendor ka. Tayyar kaam apne system (Tier 3) mein.

*Grounded in: General Agents on the Web §5 (the three file tiers: scratch, platform storage, your own system of record; finished work exits the platform)*

---

### Q86.
A project manager uses a coworking agent and wants four facts to persist across next quarter's sessions. Fact 1: "Invoices under PKR 50,000 count as routine in supplier reports" (applies to one reporting stream). Fact 2: "Write in short sentences and lead with the answer" (applies to everything she does). Fact 3: "What we decided about the Karachi warehouse on Tuesday" (one meeting's outcome, relevant to a live project). Fact 4: "The approved supplier price list for this quarter" (a file the reports must read). The available layers are session history, a Project's instructions or knowledge, account-wide standing instructions, and a user-owned context file. She has four candidate allocations of facts to layers, each looking sensible.

**Which allocation puts each durable fact in the narrowest layer that reliably applies?**

- A. Fact 1 to the Project's knowledge; Fact 2 to account-wide instructions; Fact 3 to account-wide instructions; Fact 4 to the Project's instructions.
- B. Fact 1 to the reporting Project's instructions; Fact 2 to account-wide instructions; Fact 3 to the Project's knowledge or her context file; Fact 4 to the Project's knowledge.
- C. Fact 1 to session history; Fact 2 to the Project's instructions; Fact 3 to the Project's knowledge; Fact 4 to account-wide instructions.
- D. Fact 1 to account-wide instructions; Fact 2 to the Project's instructions; Fact 3 to session history; Fact 4 to the Project's knowledge.

**Answer:** B

- ✅ **B** — Each fact goes in the narrowest reliable layer, and a decision must not rely on one session's history.
- ❌ **A** — A threshold is a rule and a price list is reference material, so those are swapped, and a one-off decision is not an account-wide rule.
- ❌ **C** — A rule for a reporting stream will not survive in session history, and a price list does not belong in account-wide instructions.
- ❌ **D** — A one-stream threshold does not belong account-wide, and a decision left in session history is not reliable in a new session.

**Yaad rakho:** Har fact sab se tang bharosemand layer mein: rule = instructions, file = knowledge, faisla = project/context file.

*Grounded in: General Agents on the Web §4 (persistence is a stack; narrowest reliable layer; session history is not memory); Quick Reference §5*

---

### Q87.
A law firm's managing partner says the firm is on an Enterprise organisation plan, so "everything is approved and controlled": an owner can disable memory for everyone, roles and permissions exist, retention is configurable, exports are available and audit logs run. She wants to roll out a new workflow that puts client matters through the assistant, and says approvals are already covered by the plan. An associate points out that these controls are administrative, that the firm's largest client bans third-party processing of its data without written consent, and that the workflow's data types have not been reviewed. The partner asks what an organisation-managed account does and does not decide. The firm's largest client is in the energy sector, the new workflow was designed by a respected consultant, and the partner says other firms are already doing the same.

**Which statement is correct?**

- A. It approves any data type once memory is disabled for everyone, since memory is the only route by which client information could reach another matter.
- B. It decides nothing useful for approvals, since administrative controls like retention and exports apply only to the vendor's data and never to the firm's own client matters.
- C. It provides roles, retention, exports, audit and organisation-wide controls, but it is not blanket approval for every workflow, data type or audience; the client's consent still needs its own check.
- D. It approves every workflow that is run inside it, since an owner-configured account with audit logs is the firm's evidence that each use has been reviewed and permitted.

**Answer:** C

- ✅ **C** — An organisation-managed account controls the route; it does not decide whether each data type and use is permitted.
- ❌ **A** — Disabling memory addresses one persistence risk, not the client's contractual restriction or the data types in use.
- ❌ **B** — Retention, exports and audit apply to chats in the account and are part of the route assessment.
- ❌ **D** — Audit logs record use; they do not approve it.

**Yaad rakho:** Enterprise plan = control ka dhancha, har workflow ki manzoori nahi. Client ki razamandi alag check.

*Grounded in: Governance §2.5-2.6 (organisation-managed account: roles, retention, exports, audit; not blanket approval for every workflow, data type or audience; an enterprise plan or a security page is not permission)*

---

### Q88.
A finance operations lead has asked the vendor's skill-creator to build a Skill from a workflow description. It produces a tidy SKILL.md and she clicks "Save skill". She announces that the Skill is deployed and will produce the client summary "automatically from now on". Three days later a colleague reports that asking for "the March client summary" yields an ordinary chat answer, and that a request for a quick total triggered the Skill. She lists what to do: test what starts it, test the output on realistic input, test awkward cases such as a client with no income, note when a problem first appeared before changing anything, and bring failures back to skill-creator with a specific instruction.

**Which order follows the build-and-test guidance?**

- A. Announce the Skill as deployed once it is saved; test the output on realistic input; test what starts it only if users complain; then bring specific failures back.
- B. Read the draft for lines two colleagues would read the same; test what starts it and that it doesn't take over unrelated requests; test the output; test awkward cases; then bring specific failures back.
- C. Rewrite the description from scratch immediately; test what starts it; then test the output; skip awkward cases, since the first draft was written by the vendor's own tool.
- D. Test the output on realistic input and awkward cases; announce deployment; test what starts it when the colleague reports; then bring specific failures back to skill-creator.

**Answer:** B

- ✅ **B** — Drafting is not deployment: review, test triggers in both directions, test output, test hard cases, and iterate.
- ❌ **A** — Trigger behavior is the first thing to test, and both directions matter; waiting for complaints is what happened.
- ❌ **C** — Skipping awkward cases and rewriting before noting when it went wrong changes the file blind, and a vendor tool's draft is still a first draft.
- ❌ **D** — Announcing before the trigger tests repeats the failure; a Skill that never fires produces no output to test.

**Yaad rakho:** Draft ko deploy na samjho: parho, trigger dono taraf azmao, output azmao, awkward cases, phir sudharo.

*Grounded in: Skills & Connectors §13-14 (test, then iterate: read the draft, test what starts it, test the output, test awkward cases, bring failures back) and What AI Actually Is A.8*

---

### Q89.
A regional finance lead put "Always answer in Markdown tables" in her account-wide instructions because it helped on her reports. Since then, her team notices that a colleague's chat, sharing her workspace default, produced a table for a short thank-you email, and that a request for a paragraph of narrative advice came back as a three-column table. She also wrote "Be helpful and concise" in the same field. A colleague explains that whatever is written there is placed in the window before the first word of every conversation, and suggests she keep only what is true for every conversation she will ever have. The team lead has been using the tool since it launched, the firm's revenue rose this year, and a colleague says that tables always look more professional in reports.

**What is the right fix?**

- A. Delete the whole account-wide field and rely on the assistant's memory to learn when she wants tables, since memory learns preferences from how she works.
- B. Keep both lines and put the table rule in capitals, since emphatic wording makes the assistant weight the rule correctly when it conflicts with a request for prose.
- C. Move the table rule to the reporting Project or a Skill, delete the vague line, and keep the account-wide field to who she is, her tone and a push-back line.
- D. Keep the table rule account-wide but add 'except when writing prose or emails', since adding exceptions to the global line restores the correct behavior in each case.

**Answer:** C

- ✅ **C** — A wrong-scope instruction damages every conversation where it does not apply, and a vague one constrains nothing.
- ❌ **A** — Memory is best-effort and per-user; it does not replace a scoped rule, and the field is right for what is true everywhere.
- ❌ **B** — Emphasis does not fix wrong scope; it makes the damage in non-report chats worse.
- ❌ **D** — Piling exceptions into a global line grows the clutter and still loads it into every window.

**Yaad rakho:** Global field mein sirf wahi jo har guftagu mein sach ho. Table wali cheez project ya Skill mein.

*Grounded in: What AI Actually Is A.5 (Instructions for Claude: write only what is true for every conversation; push topic-specific rules into a project; vague and wrong-scope instructions)*

---

### Q90. *(Select TWO — all-or-nothing)*
A consultancy's knowledge lead is training new staff on four features and asks them to complete four statements. (a) Account-wide custom instructions touch ... (b) A Skill touches ... (c) A Project loads its files and instructions ... (d) Memory holds ... Staff give varied answers. One says "a Project loads only when you ask for it", another "custom instructions apply only in the project you set them in", another "a Skill is always on everywhere", another "memory is shared across colleagues". The lead wants the statements that are correct under Anthropic's split of the four features. The knowledge lead has run the session five times, the group includes staff from three offices, and one participant has used a competitor's product for years.

**Which TWO statements are correct?**

- A. Custom instructions apply only inside the Project where they were written, so they scope a rule to one body of work without affecting the rest of the account.
- B. A Project is always on inside its own workspace: its files and instructions load when a chat is opened in it, and don't apply outside.
- C. A Skill is enabled at account level and sleeps until a matching request arrives, then works in any chat, touching one kind of task.
- D. Memory holds context about the whole team, so what one colleague teaches the assistant is available to every colleague who uses the same workspace.

**Answer:** B, C

- ✅ **B** — A Project loads its context the moment you open a chat inside it.
- ✅ **C** — A Skill touches one kind of task and fires from a description match.
- ❌ **A** — Custom instructions apply to all of your chats; Project instructions are the scoped ones.
- ❌ **D** — Memory is per-user and best-effort; it is not a shared team configuration.

**Yaad rakho:** Project apne andar hamesha on. Skill account-level, description match par. Custom instructions har chat mein.

*Grounded in: Skills & Connectors §4 (Skill, Connector, Project, custom instructions; a Project is always on in its workspace; a Skill waits for a matching request); Workflow Design §14*

---

## Domain 7 — Troubleshooting and Optimization (10% — 10 questions)

### Q91.
A sales-operations team reports two separate complaints about the same workspace. Complaint 1: "The commission totals in our quarterly summary are subtly wrong, always by small amounts, whichever model tier we use." Complaint 2: "Our account summaries keep missing the points we care about, from the very first answer in a new chat." An engineer proposes one fix for both: switch to a stronger tier. A colleague says the complaints differ and the diagnostic sequence, which runs the cheapest check first, should be run separately for each. The team has four candidate diagnoses and fixes to choose from, each of which names one cause for each complaint. The engineer has been at the company for six years, the sales team is proud of a record quarter, and the commission plan was revised twice last year.

**Which pair of diagnoses and fixes is correct?**

- A. Complaint 1 is under-specification, so state the commission formula in more detail; Complaint 2 is wrong feature, so switch to a stronger tier for the summaries.
- B. Complaint 1 is context overload, so restart the chat and paste a summary; Complaint 2 is under-specification, so name the criteria for a key point in the prompt.
- C. Complaint 1 is a wrong-feature problem, so move it to code execution; Complaint 2 is stale configuration, so update the standing instructions the summaries follow.
- D. Complaint 1 is a wrong-feature problem, so move the calculation to code execution and check what it computed; Complaint 2 is under-specification, so name the criteria for a key point.

**Answer:** D

- ✅ **D** — Subtly wrong numbers are the signature of writing rather than computing; wrong from the first answer points at the prompt.
- ❌ **A** — The totals are a calculation asked for in prose, and missing the points we care about is a prompt gap, not a tier gap.
- ❌ **B** — Errors that appear whichever tier and from the start are not a degradation over a long session.
- ❌ **C** — Stale configuration presents as 'it used to work'; this complaint is wrong from the first answer.

**Yaad rakho:** Numbers halke ghalat = prose mein calculation manga (code chalao). Pehle jawab se kamzor = prompt mein kami.

*Grounded in: Workflow Design §11-12 (four causes; diagnosis table: numbers subtly wrong means wrong feature; summary keeps missing key points means under-specification)*

---

### Q92.
An operations manager's fresh-chat request for a supplier-contract summary comes back disappointing: it misses the two payment terms she cares about. She feels she should switch to the most capable model and, failing that, decide the task cannot be done. Her colleague insists the diagnostic sequence exists to stop exactly this, and runs it cheapest first: re-read the prompt against its five parts; check the length of the conversation; check the feature and model; check whether the configuration is current; and only then question whether the task is a fit at all. The manager has four orderings on a slide, each with the same five checks in a different order. The manager is impatient because the supplier meeting is at noon, her colleague trained on the sequence at a conference, and the contract is nearly eighty pages long.

**Which order is the diagnostic sequence?**

- A. Prompt against its five parts; conversation length; feature and model; whether the configuration is current; then whether the task is a fit.
- B. Conversation length; whether the configuration is current; prompt against its five parts; feature and model; then whether the task is a fit.
- C. Feature and model; prompt against its five parts; conversation length; whether the configuration is current; then whether the task is a fit.
- D. Prompt against its five parts; whether the task is a fit; conversation length; feature and model; then whether the configuration is current.

**Answer:** A

- ✅ **A** — Cheapest first: re-reading the prompt costs seconds and resolves the most common cause; questioning the task ends the attempt, so it is last.
- ❌ **B** — The prompt check is the cheapest and resolves the most common cause, so it goes first, not third.
- ❌ **C** — Switching model or feature is a move from the bottom of the ladder made before the prompt was checked.
- ❌ **D** — Questioning the task early ends the attempt before three cheaper causes have been ruled out.

**Yaad rakho:** Sasti jaanch pehle: prompt, chat ki lambai, feature/model, configuration, aakhir mein 'kya task hi theek hai'.

*Grounded in: Workflow Design §12 (the diagnostic sequence: prompt, session length, feature and model, configuration, then the task; cheapest first)*

---

### Q93.
A reconciliation team's Skill builds bank-reconciliation reports. It worked fine for weeks. Now, in every fresh chat, it mislabels reversed entries as duplicates, even after the author tightened the wording of the instruction three times ("net out reversals before grouping", then in bold, then with an example). The chat is new each time, the description fires correctly, and the reference threshold file was updated last week. A colleague says that when the same mistake recurs after tightening the wording, the step is in the wrong place, because an exact step such as a sum or a threshold check belongs in a small program, since a sentence gets read differently each time. Another suggests a stronger tier.

**What is the best fix?**

- A. Move the exact netting step into a small script inside the Skill, via skill-creator, so it runs the same every time, and bring any needed data in through a connector.
- B. Tighten the wording a fourth time with a worked example of a reversed entry, since specific examples make the rule unambiguous where earlier attempts were too general.
- C. Move to the highest tier and keep the current wording, since a stronger model reads a netting rule more reliably and the failure is a matter of depth.
- D. Start a fresh chat and restate the task, since a repeated failure inside a Skill is usually context overload from earlier turns.

**Answer:** A

- ✅ **A** — The same mistake every run, even after tightening the wording, means the step is in the wrong place: exact steps belong in code.
- ❌ **B** — Three tightenings did not change the outcome; a sentence is read differently each time.
- ❌ **C** — A repeatable error type points at the wrong feature; a stronger tier can still guess at an exact step.
- ❌ **D** — The failure occurs in fresh chats, so context overload is ruled out.

**Yaad rakho:** Wording kasne ke baad bhi wahi ghalti: step ghalat jagah. Exact step chhote program mein.

*Grounded in: Skills & Connectors §13 (the same mistake every run even after you tightened the wording: the step is in the wrong place; exact steps belong in a small program; data through a connector)*

---

### Q94. *(Select TWO — all-or-nothing)*
A CFO's team lists four complaints about their assistant and wants to know which are genuine expectation mismatches (a task asking for something the tool cannot do) rather than problems solved by a prompt, session, feature or configuration change. (a) "It cannot tell us next quarter's export sales to the exact rupee." (b) "Our summaries keep missing the key points." (c) "Its totals are subtly wrong." (d) "It cannot tell us which specific customer will cancel next month, with certainty." A colleague says a real mismatch is step five of the diagnostic ladder, correct only after the cheaper causes are ruled out, and that naming one stops an afternoon of tuning toward an output that was never available.

**Which TWO complaints describe expectation mismatches?**

- A. (c) Subtly wrong totals: this is a mismatch, because arithmetic over many rows is beyond what a language model can do at any tier.
- B. (b) Summaries that miss key points: this is a mismatch, since deciding which points are key is a judgment that the tool cannot make for the team.
- C. (d) A certain prediction of one customer's future cancellation: certainty about an individual future event is beyond the tool, so ask for a ranked risk with reasons.
- D. (a) An exact future sales figure: no prompt, restart, feature or configuration fix produces it; ask for a range with stated assumptions or an adjustable driver model.

**Answer:** C, D

- ✅ **C** — The task asks for something the tool cannot do; reshape it into a task that fits.
- ✅ **D** — The fix is to the task: a range, or a model of the drivers you can adjust and re-run.
- ❌ **A** — This is a wrong-feature problem: move the calculation to code execution.
- ❌ **B** — This is under-specification: name the criteria for what counts as key.

**Yaad rakho:** Aisi cheez maangna jo tool de hi nahi sakta (exact future, yaqeeni ek shakhs): expectation mismatch.

*Grounded in: Workflow Design §12 (expectation mismatch; step 5 exists and is sometimes right; reshape the task into one that fits; diagnoses table)*

---

### Q95.
A due-diligence team's assistant summarised five-page vendor briefs accurately for months. This quarter the team started feeding it 40-page briefs with appendices, and the summaries now drop the second half. A colleague says "it used to work, so it must be stale configuration". The Skill file is unchanged and a new chat gives the same result, so session length is not the issue. An analyst points out that one timing can have more than one cause, that "it used to work" usually means the setup drifted but sometimes means the task changed shape and nobody noticed, and that each signal gives a first guess and a cheap way to test it. The team lead is proud of how quickly the briefs used to be summarised, the vendor recently held a webinar on long documents, and the analyst is new to the team.

**What is the best reading and next step?**

- A. The task changed shape: inputs are eight times longer, so restructure the work (summarise by section, then combine, checking each) rather than editing a Skill that didn't change.
- B. It is stale configuration, so update the Skill's instructions and the reference documents it reads, since nothing else explains a decline after months of reliable summaries.
- C. It is context overload, so restart the chat and paste a summary, since long inputs fill the window the same way that long conversations do.
- D. It is an expectation mismatch, so the task should be declared beyond the tool now that briefs are eight times longer and the summaries have started to fail.

**Answer:** A

- ✅ **A** — 'It used to work' sometimes means the task changed shape; the cheap test is to compare what changed in the inputs.
- ❌ **B** — Nothing in the setup changed; the input did.
- ❌ **C** — A new chat gives the same result, so the length of the conversation is ruled out; the input itself is what changed.
- ❌ **D** — That is step five, concluded only after cheaper causes are ruled out; restructuring the workload is cheaper.

**Yaad rakho:** 'Pehle chalta tha' ka matlab kabhi config purani, kabhi kaam ki shakal badal gayi. Kya badla? pooch.

*Grounded in: Workflow Design §11 (one timing can have more than one cause; 'it used to work' usually means the setup drifted, sometimes the task changed shape)*

---

### Q96.
A team's weekly reporting workflow shows three frictions when audited. Each analyst re-pastes the same background paragraph and definitions into the prompt every run (repetition). Each analyst fixes the same formatting flaw in every output by hand (correction). Different analysts running the same task get different results, and the differences only show up when the reviewer compares them (variance). The audit's lead lists four mappings of friction to fix, each using the same three fixes, and says the variance friction is the one teams miss because no individual feels it. The team's weekly report goes to three directors, the analysts recently changed offices, and the reviewer is well regarded for spotting inconsistencies between people.

**Which mapping of friction to fix is correct?**

- A. Repetition to a shared knowledge base; correction to saved context; variance to a standing instruction that each analyst keeps in their own workspace.
- B. Repetition to saved context or a standing instruction; correction to a configuration change so the flaw stops appearing; variance to a shared Skill or knowledge base all analysts use.
- C. Repetition to a configuration change; correction to a shared Skill or knowledge base; variance to saved context or a standing instruction each analyst keeps.
- D. Repetition to a shared Skill; correction to saved context; variance to a configuration change so the flaw stops appearing in individual outputs.

**Answer:** B

- ✅ **B** — Each friction signal has its own fix, and variance is fixed by making the method shared, not by individual effort.
- ❌ **A** — Personal instructions leave each analyst's results different; variance needs one shared home.
- ❌ **C** — A per-analyst instruction leaves the variance between people in place.
- ❌ **D** — A repeated background is context to save, and variance between people needs a shared method.

**Yaad rakho:** Dohrana = saved context, sudhar = config, farq (variance) = shared Skill/knowledge.

*Grounded in: Workflow Design §15 (find the friction: repetition, correction, variance; the fixes; variance shows at the reviewer)*

---

### Q97.
An operations director is assigning the metric each of four redesigned workflows should be optimised for, before measuring the baseline. W1: an internal first draft of meeting notes that nobody outside the team reads. W2: a customer-facing monthly report whose layouts have varied between staff and eroded trust. W3: a regulatory return where one wrong figure costs a penalty larger than an hour saved. W4: a task done by six people who each get different results. She has four allocations, each using all four metrics (time, consistency, accuracy, variance) once, and notes that naming the metric up front tells you when to stop tuning. The director has a board meeting in a week, the operations team is moving to a new building, and staff morale on the redesign has been high.

**Which allocation is correct?**

- A. W1 to accuracy; W2 to time; W3 to consistency; W4 to variance.
- B. W1 to time; W2 to consistency; W3 to accuracy; W4 to variance.
- C. W1 to time; W2 to variance; W3 to consistency; W4 to accuracy.
- D. W1 to consistency; W2 to accuracy; W3 to time; W4 to variance.

**Answer:** B

- ✅ **B** — Optimise for what the workflow is for: speed on cheap internal drafts, consistency on customer reports, accuracy on compliance outputs, variance where the cost lies between people.
- ❌ **A** — A cheap internal draft is about speed, and a regulatory return is about accuracy, not consistency.
- ❌ **C** — A customer report's problem is inconsistent layouts, and a task done by six people is about variance.
- ❌ **D** — Optimising a penalty-bearing return for time is the wrong trade; accuracy is the metric.

**Yaad rakho:** Metric kaam ki wajah se: internal draft = time, customer report = consistency, compliance = accuracy, kai log = variance.

*Grounded in: Workflow Design §16 (measure the thing you actually care about: internal draft time; customer-facing consistency; compliance accuracy; several people variance)*

---

### Q98.
An analytics lead builds a business case for keeping a redesigned weekly-report workflow. The audit found each of four analysts used to spend 50 minutes a week on the report and now spends 20. The team works 48 weeks a year. The workflow keeps a named reviewer who spends 15 minutes a week in the gate, and the team pays an AI-tool subscription. One colleague proposes stating the saving as "60% less time" without more detail; another proposes leaving out the residual risk "so the case is not confused"; a third does the arithmetic quickly in his head. The lead wants a statement that would survive a budget review, and the hours must be computed, not guessed.

**Which statement of the case is most defensible?**

- A. About 84 hours a year net: 96 hours saved (30 minutes x 4 analysts x 48 weeks) less 12 hours of reviewer time in the gate, against the subscription, with the residual risk named.
- B. About 60% less time on the report, presented as a percentage with no volume or cost, since a proportion travels across teams and avoids arguments about hours.
- C. About 144 hours a year saved, taking the quick estimate and rounding up to allow for consistency benefits, with the gate time and the risk left out.
- D. About 96 hours a year saved (30 minutes x 4 analysts x 48 weeks), with the reviewer's gate time excluded because it is overhead that would exist anyway.

**Answer:** A

- ✅ **A** — Saving is baseline change times frequency times people; cost includes the human time still in the gate; the surviving risk is stated.
- ❌ **B** — A percentage without volume, cost or risk cannot survive a budget review.
- ❌ **C** — 30 x 4 x 48 = 5,760 minutes, which is 96 hours; the quick estimate is wrong, and hiding the risk stops the case being believed.
- ❌ **D** — The gate is part of the redesigned workflow's cost, so the case is overstated.

**Yaad rakho:** Bachat = kitne minute x kitni baar x kitne log; gate ka waqt ghatao; bacha hua risk likho.

*Grounded in: Workflow Design §16 (be able to answer what it costs: saving = baseline x frequency x people; cost includes human time in the kept gates; name the risk that survives) and §3*

---

### Q99.
An analyst asks an assistant to write and run code that totals monthly sales from a merged file. Three separate problems occur on three days. Day 1: the script stops with a red error message about a missing column. Day 2: the script runs but the total is 8.1 million where she knows it should be about 7.6 million; there is no error. Day 3: after three attempts, the assistant's fix, each time claiming the total is now correct, keeps giving a different wrong number. She has three candidate messages, each for one symptom, and four ways to pair messages with days. The analyst uses a laptop with a small screen, the merged file was assembled by a colleague on leave, and the finance director expects the total by the end of the day.

**Which pairing of symptom to message is correct?**

- A. Day 1: paste the full error and say 'diagnose, fix, rerun'. Day 2: give the symptom and expected value and ask for row counts and samples first. Day 3: stop, restate fresh and ask for two different approaches.
- B. Day 1: stop, restate the problem and ask for two approaches. Day 2: state the symptom and expected value. Day 3: paste the full error and say 'diagnose, fix, rerun'.
- C. Day 1: state the symptom and expected value and ask for row counts. Day 2: paste the full error and say 'diagnose, fix, rerun'. Day 3: stop, restate the problem fresh and ask for two different approaches.
- D. Day 1: paste the full error and say 'diagnose, fix, rerun'. Day 2: stop, restate the problem and ask for two approaches. Day 3: state the symptom and expected value and ask for row counts and samples.

**Answer:** A

- ✅ **A** — An error is the computer saying what it needs; a wrong number needs the symptom and expected value; three failed identical fixes mean the approach is wrong.
- ❌ **B** — Day 1 is a plain error to paste back, and Day 3 has no error message to paste.
- ❌ **C** — Day 2 has no error to paste, and Day 1 has one; the messages are swapped.
- ❌ **D** — Two approaches are for repeated failure of the same fix, not for a first wrong number.

**Yaad rakho:** Error aaye to paste karo; ghalat number to symptom + expected value + row counts; teen baar wahi fix fail to naye do raaste.

*Grounded in: Code You Never Write §7 (errors are dialogue; runs but a number contradicts what you know; same fix fails three times: step back and propose two different approaches)*

---

### Q100.
A team lead tells her reviewers that their "not quite right" reactions must become instructions. She writes four reactions on the board and asks what would have to be present for each to be right, and which part of the setup controls it. Reaction 1: "Too generic." Reaction 2: "Wrong tone in every draft." Reaction 3: "It's using old data." Reaction 4: "Missed the point." She lists the levers as the prompt, the instruction, the knowledge, and, for a repeated flaw, a saved procedure. A colleague notes that if you cannot name the lever, the critique is still a reaction. The team lead has run this exercise before, the reviewers are keen to improve, and the last workshop was rated highly by everyone who attended.

**Which set of reaction-to-instruction pairings is correct?**

- A. Too generic: add a tone constraint for every draft (the instruction). Wrong tone: name the audience and the action (the prompt). Old data: state the question up front (the prompt). Missed the point: replace the source document.
- B. Too generic: state the single question up front (the prompt). Wrong tone: replace the source document (the knowledge). Old data: add a tone constraint (the instruction). Missed the point: name the audience and the action.
- C. Too generic: name the audience and action (prompt). Wrong tone: add a tone constraint for every draft (instruction). Old data: replace the source document (knowledge). Missed the point: state the question up front (prompt).
- D. Too generic: replace the source document (the knowledge). Wrong tone: name the audience and the one action wanted (the prompt). Old data: add a tone constraint for every draft (the instruction). Missed the point: state the question up front.

**Answer:** C

- ✅ **C** — Each reaction becomes an instruction naming what to change and the lever that controls it.
- ❌ **A** — A generic answer is fixed by supplying the audience and action; old data by replacing the source.
- ❌ **B** — It scrambles all four pairings; tone is an instruction, old data is knowledge.
- ❌ **D** — The levers are assigned to the wrong reactions; old data is a knowledge problem, tone is an instruction.

**Yaad rakho:** Har shikayat = ek hukm + ek lever: audience/action (prompt), lehja (instruction), purana data (knowledge).

*Grounded in: Workflow Design §13 (turn a reaction into an instruction; what would have to be present, and which part of the setup controls it; if you cannot name the lever it is still a reaction)*

---

## Answer Key (jaldi check ke liye)

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
| ---: | :--- | ---: | :--- | ---: | :--- | ---: | :--- | ---: | :--- |
| 1 | D | 21 | CD | 41 | D | 61 | D | 81 | D |
| 2 | A | 22 | B | 42 | AB | 62 | C | 82 | B |
| 3 | D | 23 | B | 43 | C | 63 | AB | 83 | D |
| 4 | A | 24 | B | 44 | D | 64 | BD | 84 | A |
| 5 | D | 25 | D | 45 | BC | 65 | A | 85 | A |
| 6 | A | 26 | A | 46 | B | 66 | BC | 86 | B |
| 7 | D | 27 | C | 47 | D | 67 | A | 87 | C |
| 8 | B | 28 | A | 48 | AD | 68 | B | 88 | B |
| 9 | C | 29 | AC | 49 | C | 69 | C | 89 | C |
| 10 | C | 30 | B | 50 | C | 70 | B | 90 | BC |
| 11 | A | 31 | D | 51 | D | 71 | AB | 91 | D |
| 12 | B | 32 | AC | 52 | B | 72 | C | 92 | A |
| 13 | BD | 33 | C | 53 | BD | 73 | A | 93 | A |
| 14 | D | 34 | B | 54 | B | 74 | AD | 94 | CD |
| 15 | A | 35 | D | 55 | A | 75 | D | 95 | A |
| 16 | C | 36 | C | 56 | B | 76 | D | 96 | B |
| 17 | B | 37 | D | 57 | A | 77 | AD | 97 | B |
| 18 | C | 38 | A | 58 | A | 78 | D | 98 | A |
| 19 | AC | 39 | B | 59 | C | 79 | CD | 99 | A |
| 20 | C | 40 | C | 60 | C | 80 | B | 100 | C |

---

## Look-Alike Traps — Cheat-Sheet (Level 2 ke pivot)

| Jahan options milte-julte hain | Asal pivot |
| --- | --- |
| **"Known answer" sahi lagta hai** | Kya wo jawab *alag zariye* se aaya (same export/macro nahi) aur kya wo *badle hue raste* ko chhooti hai? |
| **Do vendors ka agreement** | Same brief = same omission. Checker ko *source* dikhaya gaya ya sirf summary? |
| **Gate ka wording** | Teen cheezein: kaun (role), kya (khaas risk, source khol kar), kab (output ke sakht hone se pehle). Ek kam = gate nahi. |
| **Review sample** | Jo reviewer tak pahunchta hai wo *kis ne chuna*? Agar system ne, to gate wahi chhoot jata hai jo system ghalat samjha. |
| **"Ran / completed / green"** | Tool ne kya *dikhaya*? 0 tests, khali section, ghalat rate: chalna ≠ theek chalna. |
| **Order wale sawal** | Har qadam sahi hai; tarteeb ghalat. Sasta/sab se pehle wala kaam (eligibility, prompt check, extraction, identify) pehle. |
| **Halo / self-set gate** | Ek step ki achhai dusre ko de di? Kya permission wahi system de raha hai jis ko review karna hai? |
| **Skill vs connector** | Connector ke scopes; Skill ke nahi (session ki poori pahunch). Parhna + kaam = insaani gate. |
| **Sandbox / incognito / Enterprise** | Execution ki hadd, memory ki hadd, control ka dhancha: teeno *ijazat* nahi. |
| **Independent kaun?** | Doosri company + source + insaan. Same model ka persona, doosra chat, ya khud ki confidence: nahi. |
| **Purana kya, naya kya?** | Config purani (bina error), task ki shakal badli, ya sirf pehli jhalak? Timing pehla shak hai, wajah nahi. |
| **Reach ke raaste** | Connector, phir browser, phir computer use; signed-in session poori hassasiyat le aati hai. |

---

## Note

Yeh file PCAO-F Panaversity exam ke liye original self-test hai; koi asli exam item shamil nahi. Product-specific baaton
ke liye har course ki "checked on" tareekh (Aug–Sep 2026) dekho aur booking se pehle official CCAO-F guide download karo.

[⬅ PCAO-F Index](README.md) · [`pcaofcombatlevel1.md`](pcaofcombatlevel1.md) · [`pcaofexamquizv2.md`](pcaofexamquizv2.md)
