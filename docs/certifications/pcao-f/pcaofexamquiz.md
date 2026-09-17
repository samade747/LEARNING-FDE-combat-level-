# PCAO-F / CCAO-F — 100-Question Hard Scenario Bank (`pcaofexamquiz.md`)

*100 **original** long-form scenario questions, written to match the complexity of the real exam
(modelled on the style/difficulty of a genuine PCAO-F/CCAO-F sample paper reviewed for this repo —
`docs/certifications/exam.docx` — but none of these scenarios are copied from it). Distributed across
the 7 blueprint domains **in proportion to their published exam weight** (grounded in
[`../ccao-f/01-domain-blueprint.md`](../ccao-f/01-domain-blueprint.md) and
[`../ccao-f/08-teaching-walkthrough.md`](../ccao-f/08-teaching-walkthrough.md)):*

| Domain | Weight | Questions Here |
| --- | ---: | ---: |
| 2 — Output Evaluation and Validation | 21% | 21 |
| 4 — Workflow Integration and Solution Design | 16% | 16 |
| 6 — Governance, Risk, and Responsible Use | 15% | 15 |
| 1 — Prompting and Task Execution | 14% | 14 |
| 3 — Product and Model Selection | 12% | 12 |
| 5 — Configuration and Knowledge Management | 12% | 12 |
| 7 — Troubleshooting and Optimization | 10% | 10 |
| **Total** | **100%** | **100** |

Most items are single-answer. Items marked **(Select TWO — all-or-nothing)** or **(Select THREE —
all-or-nothing)** match the real exam's multiple-response format: partial credit is not given, all
correct options must be chosen and no incorrect one. Answer + explanation follow every question —
cover them before reading if you want a clean self-test pass.

---

## Domain 2 — Output Evaluation and Validation (21% — Q1–Q21)

### Q1.
A hospital-billing associate has Claude reconcile insurance-remittance files against submitted claims each week. This week's reconciliation matches a prior week whose correct result the associate already verified by hand. The associate now wants to stop checking future weeks by hand entirely.
**Options**
- A. Correct — one matched verification proves the process is reliable going forward, for any future week
- B. Keep spot-checking a sample of line items each week; a single matched case earns confidence for *similar* weeks, not a permanent guarantee
- C. Verification is no longer needed once Claude itself confirms the totals balance
- D. Switch to a flagship model instead, which removes the need for ongoing checks

**Answer:** B — A known-answer match earns *earned confidence for similar future work*, not a permanent pass. Reconciliations can still hit new edge cases (a new insurer format, a new denial code), so periodic sampling stays part of the process. Self-confirmation by the same tool (C) isn't independent verification, and model choice (D) doesn't substitute for checking.

---

### Q2.
A university admissions office uses Claude to draft rejection-reason summaries for an appeals committee. An associate asks Claude, "Are you confident these summaries are fair and accurate?" and Claude replies with a detailed, confident "yes." The associate files the summaries without further review.
**Options**
- A. This is sufficient — Claude's own confidence statement is a valid quality signal
- B. Self-reported confidence from the same model that produced the output is not independent verification; an alternate path (human review, a second model, a rubric) is needed
- C. Sufficient only because it's an internal, non-published document
- D. Sufficient, since appeals committees always re-check everything anyway

**Answer:** B — The generating model is its own weakest verifier: whatever bias or gap shaped the output will also shape its self-assessment. A model's stated confidence is not evidence.

---

### Q3.
A pharma-company associate asks Claude to summarize a set of clinical-trial abstracts for an internal slide. The summary quotes a "38.4% reduction in adverse events," phrased with high confidence and no source line.
**Options**
- A. Use the figure as stated — the phrasing was confident, and precision (one decimal place) suggests care
- B. Treat the precise, unsourced figure as a fabrication risk and trace it back to the specific abstract and page before using it
- C. Round the number to make it sound less exact and use it as an estimate
- D. Ask Claude to rate its own confidence in the figure and use it if the rating is above 90%

**Answer:** B — A precise-looking statistic with no attached source is a classic hallucination signature, not a sign of accuracy. It must be traced to its origin before it goes on a slide with clinical implications.

---

### Q4.
A logistics coordinator has Claude review 600 delivery-exception tickets and auto-close the 80 it classifies as "duplicate, no action needed." The coordinator personally reviews all 80 closed tickets and confirms they were correctly duplicates.
**Options**
- A. That review is complete; the closed tickets were the only risk
- B. Also sample the 520 tickets that were *not* closed, to check whether a category of real exceptions is being systematically left open or mis-routed
- C. Re-run the classification with a stricter prompt and close only tickets appearing in both runs
- D. Add a note to each closed ticket that AI performed the first pass, and stop there

**Answer:** B — Checking only the acted-upon subset misses systemic misrouting in the untouched majority. The real risk in a screening/triage system often hides in what wasn't flagged, not in what was.

---

### Q5.
A litigation paralegal asks Claude to extract every deadline from a 40-page case-management order. The output lists twelve deadlines, each with a page reference. The paralegal is drafting the firm's calendar from this list directly.
**Options**
- A. Enter all twelve into the calendar; page references make the list self-verifying
- B. Spot-check a couple of entries by opening those pages, and treat the full list as final without opening the rest
- C. Independently confirm each deadline against the source document before calendar entry, since a missed court deadline is high-stakes and hard to reverse
- D. Ask Claude to confirm its own list is complete and accurate before proceeding

**Answer:** C — A page citation reduces search effort but is not proof of correctness — the citation itself can be wrong. Given the irreversibility (a missed deadline), full independent confirmation against the source is warranted, not sampling or self-confirmation.

---

### Q6.
A city-planning department has Claude draft a zoning-variance impact summary that will go to the same model, in a fresh chat, for a "second opinion" self-check before it reaches the planning board.
**Options**
- A. This satisfies the independent-verification principle, since it's a separate conversation
- B. It does not — a fresh chat with the same model still shares the same underlying blind spots; a genuinely independent path (a different model family, a human domain expert, or a hard rule) is needed for a board-facing document
- C. It satisfies the principle only if the second chat uses a different account
- D. It's unnecessary either way, since zoning summaries are low-stakes

**Answer:** B — "Independent" means a different source of judgment, not a different chat window. Same model, same blind spots, regardless of session boundaries.

---

### Q7.
A retail chain's finance team gets a Claude-built spreadsheet of quarterly markdowns from raw POS exports. Every cell holds a number; none are labeled with their formula or source range, and the team is using the sheet to decide next quarter's pricing.
**Options**
- A. Accept the numbers since the totals look plausible at a glance
- B. Have the calculations done via code Claude runs and shows (not prose arithmetic), and check the rows/ranges it actually used before relying on the totals
- C. Ask Claude to re-verify its own arithmetic and confirm the totals are correct
- D. Spot-check three cells; if they're right, trust the rest

**Answer:** B — Numeric work that will drive a real decision should be produced and shown via executable computation, not prose-generated arithmetic, and the associate should confirm which data the computation actually drew from — not merely spot-check outputs that look reasonable.

---

### Q8.
An HR analyst asks two different AI assistants (Claude and a competitor) to independently rate the same finalist shortlist for a director role against the same rubric. The two tools disagree sharply on two of five candidates.
**Options**
- A. Average the two scores and move forward with the blended ranking
- B. Discard both AI opinions since they disagree, and decide entirely without them
- C. Treat the disagreement itself as the signal — it flags exactly which two candidates need deeper human review before a decision is made
- D. Re-run both tools until they agree, then use that consensus

**Answer:** C — Cross-model disagreement is diagnostic, not noise: it points precisely at the cases needing human judgment, rather than being something to average away or force into artificial agreement.

---

### Q9.
An energy-utility associate asks Claude for the current regulatory threshold for reporting a minor gas leak. Claude cites a trade-association newsletter from 2022 and states a figure. The associate opens the newsletter and confirms it does say that figure.
**Options**
- A. Use the figure — the citation was checked and it supports the claim
- B. Trace the figure to the regulator's own current publication and cite that instead, since a 2022 secondary source may be outdated or non-authoritative
- C. Ask Claude for two more secondary sources and use the figure if they agree
- D. Discard the figure entirely, since no secondary source can ever be trusted

**Answer:** B — Confirming a secondary source *exists and says X* is not the same as confirming *X is still true*. For a regulatory threshold, the regulator's own current text is the authority to check against.

---

### Q10.
A market-research associate pastes 60 open-ended survey responses into one message and asks Claude to code each by theme, tally the themes, rank them, and write the executive summary — all in a single pass. Weeks later, someone discovers 9 responses were mis-coded into the wrong theme, and the error is baked into the tally, the ranking, and the summary.
**Options**
- A. Add "work carefully and double-check" to the same single-pass prompt next time
- B. Split the work into stages — code the themes first, verify the coding table against the raw responses, then tally, rank, and summarize
- C. Re-run the identical single-pass prompt on a more capable model
- D. Split the 60 responses into six batches of 10 and repeat the same single-pass approach on each batch

**Answer:** B — Errors made early in an unverified single pass propagate silently through every downstream step. Verifying the intermediate coding table before building on it is what catches this, not more careful wording or smaller batches of the same unverified pattern.

---

### Q11.
A construction-firm associate has Claude draft a subcontractor's scope-of-work compliance check against the master contract. Claude lists four compliance gaps, fluently and confidently. Three are genuinely in the contract; the fourth — a specific insurance-certificate requirement — is not in this contract but is standard practice industrywide.
**Options**
- A. Turn on web search so Claude can cross-reference industry norms as well as the contract text
- B. Instruct Claude to answer strictly from the pasted contract text only, quote the clause behind each claim, and say "not in the source" rather than supplying industry-standard fill-ins
- C. Add "please be accurate and don't make anything up" and re-run the same request
- D. Attach the contract as a file instead of pasting the text, expecting more careful reading

**Answer:** B — The model filled a real gap in the contract with a plausible, common industry norm — exactly the "sounds right, isn't sourced" failure mode. Constraining the model to the provided source and requiring an explicit "not found" response is what prevents silent invention.

---

### Q12.
A nonprofit's grants officer has Claude summarize a 300-line donation ledger by campaign, to decide which campaigns to renew. The prose summary's totals look reasonable, and every individual line item Claude quotes checks out correctly.
**Options**
- A. Accept the campaign totals — since the individual line items are correct, the aggregated totals must be too
- B. Ask Claude to re-check its own arithmetic and confirm the totals
- C. Have the totals computed by code the assistant runs and displays, and verify which rows and campaign labels fed each total
- D. Spot-check five line items; if they match, trust the totals

**Answer:** C — Correct individual facts don't guarantee correct aggregation — a wrong grouping or summation step can sit invisibly between accurate line items and a wrong total. Decision-driving totals need a shown, checkable computation.

---

### Q13.
An airline's customer-relations team has Claude pre-screen 1,200 compensation claims and fast-track 150 for expedited payout. The team lead carefully reviews all 150 fast-tracked claims and finds them sound.
**Options**
- A. That review is sufficient; approve the 150 payouts
- B. Sample the 1,050 non-fast-tracked claims to check whether a group of legitimate claims (e.g., from a particular route or fare class) is being systematically routed away from fast-track
- C. Re-run the screening with a stricter prompt and only pay claims appearing in both runs
- D. Disclose to all 1,200 claimants that AI performed initial screening, and stop there

**Answer:** B — As with any triage/screening system, the larger risk usually sits in what was *not* selected. Checking only the selected subset can miss systematic exclusion of a valid group.

---

### Q14.
A museum's development office asks Claude to draft a donor-impact report. It reads well and cites "a 22% increase in program reach," a figure the assistant says it "calculated from the attached files." No formula, cell reference, or calculation is shown.
**Options**
- A. Use the figure — the assistant stated where it came from
- B. Ask for the actual calculation to be shown (ideally via executable computation against the attached data) before the figure goes into a donor-facing report
- C. Round the number down slightly to be conservative, then use it
- D. Ask Claude to rate its own confidence and use the figure if confidence is high

**Answer:** B — A claim of having calculated something is not the calculation itself. A stated source without a shown method is still unverified, especially for a number going to external donors.

---

### Q15.
A biotech-startup associate has Claude and a second AI model independently review the same 15-page safety-data summary for internal consistency issues. Both tools flag the same three inconsistencies and find nothing else.
**Options**
- A. Treat the agreement as sufficient and finalize the summary — for a safety document, tool agreement should still be treated as a progress signal, and a qualified human reviewer should still sign off before anything safety-related ships
- B. Treat agreement between two AI tools as full proof of correctness on a safety document, with no further human review needed
- C. Since both tools missed the same things, add a third AI tool and stop only once three agree
- D. Discard both reviews since AI cannot be trusted with safety content at all

**Answer:** A — Cross-model agreement raises confidence and is useful progress evidence, but for legal/medical/safety-adjacent claims it is never a substitute for a qualified human's final sign-off — multiple tools can share the same blind spot.

---

### Q16.
A media company's ad-sales associate asks Claude to justify why a client's underperforming campaign is "on track," framing the question as "explain why this campaign is actually doing well."
**Options**
- A. This produces a genuinely evaluative answer, since Claude will correct a wrong premise
- B. This is a leading question — the framing signals the desired conclusion. A better prompt asks for the strongest case for *and against* the campaign being on track, without presupposing the answer
- C. This is fine as long as the associate double-checks any numbers cited afterward
- D. This is fine because Claude has no incentive to agree with a client-facing associate

**Answer:** B — Framing a question to presuppose its answer invites a persuasive case for that answer rather than an honest evaluation — the same failure pattern as asking two differently-leading questions and getting two confident, contradictory answers.

---

### Q17.
An accounting-firm associate discovers that a client's quarterly figures, drafted with Claude's help, contained a wrong number that the regulator flagged. The workflow had reported a 55% time saving versus the old manual process.
**Options**
- A. Keep optimizing for time saved, since speed was the redesign's stated goal and errors are cheap to fix after the fact
- B. Re-optimize the workflow around accuracy — for a compliance-facing output, one wrong figure costs far more than the time that was saved
- C. Optimize for consistency of formatting instead, since that is what regulators usually flag
- D. Treat this as a one-off and change nothing, since the time savings are still real

**Answer:** B — When a workflow's output feeds a compliance/regulatory decision, the correctness of that output matters more than the speed of producing it — an efficient process that ships an error is a worse outcome than a slower, correct one.

---

### Q18. *(Select TWO — all-or-nothing)*
A supply-chain analyst has five reactions to Claude's outputs this week. Which **TWO** reflect a genuine independent-verification failure rather than a simple preference or formatting issue?
**Options**
- A. "It quoted a supplier lead-time that isn't in any of our files and gave no source for it"
- B. "It used bullet points when I wanted a paragraph"
- C. "It told me itself that the reorder-quantity math was correct, and I used that as my only check before submitting the purchase order"
- D. "It used British spelling instead of American spelling"
- E. "It picked a slightly different shade of formatting than last week's report"

**Answer:** A, C — A is an unsourced, unverifiable claim (hallucination risk); C is relying on the same model's self-report as the *only* check on a numeric decision that drives a real purchase order. B, D, and E are stylistic preferences, not evaluation failures.

---

### Q19.
A telecom's fraud-analytics associate has Claude flag suspicious account changes. Of 2,000 accounts scored, 40 are flagged as high-risk and immediately frozen without further review, since "the model has been accurate on past audits."
**Options**
- A. This is fine — a strong past track record justifies acting on the score alone going forward
- B. Freezing an account is a consequential, hard-to-reverse action for the customer; a defined human review step (naming who checks what, before the freeze takes effect) is still needed regardless of past accuracy
- C. This is fine as long as customers are notified after the freeze
- D. This is fine only if the model used code execution to compute the risk score

**Answer:** B — A track record earns the model similar future work, but it does not transfer accountability, and a customer-impacting, hard-to-reverse action still needs a defined human checkpoint before it takes effect — not just retrospective notice.

---

### Q20.
A public-health department's associate asks Claude to summarize a peer-reviewed study for a citizen-facing FAQ. The summary is fluent, well-organized, and consistent with the abstract — but the associate has no epidemiology background and cannot judge if the summary is misleading in a way that reads perfectly well.
**Options**
- A. A formatting/clarity proofread by a colleague is the missing check
- B. Ask Claude to rate its own accuracy and revise until the score is high
- C. Have someone with relevant subject-matter expertise assess whether the summary is credible by the field's own standards — fluency and internal consistency don't confirm subject-matter accuracy
- D. Run a plagiarism check against the original abstract

**Answer:** C — A summary can be fluent, well-structured, and internally consistent while still misrepresenting the underlying science in ways only a subject-matter expert would catch. That is the specific gap a general proofread or self-rating cannot close.

---

### Q21.
A national retailer's category manager has Claude re-verify a Claude-generated demand forecast by asking the same model, "Are you sure this forecast is right?" in the same conversation.
**Options**
- A. This counts as sufficient verification since the model reconsidered the question
- B. This is not independent verification — same model, same conversation, same blind spots; a genuinely separate check (holdout data, a different model, a domain expert) is needed for a forecast that will drive inventory decisions
- C. This is sufficient only if the model's second answer differs from its first
- D. This is unnecessary, since demand forecasts are inherently uncertain anyway

**Answer:** B — Re-asking the same source in the same context for reassurance produces confidence, not verification.

---

## Domain 4 — Workflow Integration and Solution Design (16% — Q22–Q37)

### Q22.
A regional bank's operations lead says only, "Get Claude to handle our loan-document intake." Nothing else is specified.
**Options**
- A. Start building immediately with sensible defaults, and adjust based on feedback
- B. Before building anything, settle five things: what exactly should be produced, for whom, how often, from what data/documents, and in what output format
- C. Ask the bank's IT department to pick the tooling first
- D. Pick the most capable model available and let it infer the requirements from the document types

**Answer:** B — "Handle our intake" is a wish, not a specification. Task definition — what/for whom/how often/from what/in what format — must be settled first; unresolved items are clarifying questions for a person, not gaps for the model to guess.

---

### Q23.
A six-step vendor-payment approval workflow is being redesigned. One step: an AI-drafted early-payment discount calculation, followed by a supervisor who releases or holds the payment. A team member proposes removing the supervisor's release step "since the math is computed by code and is always correct."
**Options**
- A. Agree — a correctly computed number needs no further human check
- B. Keep the release step: the computation itself is safe to delegate specifically *because* an error can still be caught and reversed before the payment goes out, and a named person still decides
- C. Replace the supervisor with a second AI pass that recomputes independently
- D. Move the whole calculation back to manual, since anything payment-related should stay fully human

**Answer:** B — Correct computation reduces one risk (arithmetic error) but doesn't eliminate the need for a reversibility/accountability checkpoint before an irreversible payment goes out — the release step is what keeps the action correctable, not the arithmetic.

---

### Q24.
A property-management firm's proposal for AI-drafted tenant maintenance replies states, "All replies will be reviewed by a person before sending." A colleague says this is fine because it "clearly keeps a human in the loop."
**Options**
- A. Change it to "light human review" to reduce reviewer workload once the drafts prove reliable
- B. Add a note that 10% of replies will be sampled after sending
- C. Name the specific role that reviews, the specific risk the review is checking for, and confirm review happens before the reply is sent — a vague "a person will review" is an intention, not a defined gate
- D. Remove the review requirement, since an unenforceable rule is worse than no rule

**Answer:** C — A real governance gate names WHO reviews, WHAT they're checking for, and WHEN (before an action is taken/hard to undo). "A person will review" alone commits to nothing specific and can't be audited or challenged.

---

### Q25.
A five-person consulting team is redesigning its monthly client-status-report workflow around Claude. They've planned two changes: consolidating three separate prompts into one, and moving repeated formatting rules into standing instructions. They want to report a time-savings figure to leadership.
**Options**
- A. Move the formatting rules into configuration first, so every later run already benefits before measuring
- B. Consolidate the prompts first, since removing steps is the biggest expected saving
- C. Pick "time saved" up front as the figure to report, so the improvement is easy to communicate
- D. Run the current, unchanged process once and record its time, revision rounds, and manual steps — establish the baseline before changing anything

**Answer:** D — Without a measured baseline, any "improvement" figure reported afterward is unverifiable. Establishing the starting point comes before making changes or picking which metric to showcase.

---

### Q26.
A logistics firm connected its shipment-tracking folder to Claude with read-only access, to summarize incoming manifests. A new request: have Claude also move completed manifests into an archive folder.
**Options**
- A. This is already possible, since a connector inherits everything the associate's account can do
- B. This requires enabling a Skill that teaches Claude how to identify completed manifests
- C. This requires a second, separate connector, since read and write access cannot share one connection
- D. Moving files is a write action, and it must be deliberately granted once the connector's settings are checked to confirm it can even offer write access

**Answer:** D — Read access does not imply write access. A write capability (moving/deleting files) must be deliberately enabled and confirmed available — not assumed from account permissions or solved with a Skill alone.

---

### Q27.
A hospital's discharge-planning team wants an AI assistant to draft patient discharge instructions. The team is deciding, for five parts of the workflow, whether each step is AI-appropriate, human-retained, or collaborative.
**Options**
- A. Base the classification only on how technically difficult each step is for the model
- B. Base the classification on reversibility (can an error be caught and undone?), stakes (worst-case cost of an error?), and accountability (who is responsible, and can they meaningfully review?)
- C. Make every step collaborative by default, since healthcare is always high-stakes
- D. Base the classification on which step takes the most staff time currently

**Answer:** B — Delegation decisions are driven by reversibility, stakes, and accountability together, not by task difficulty, blanket caution, or current time cost.

---

### Q28.
A team lead describes an AI-assisted invoice-dispute triage workflow in three versions: one for the operations manager, one for the CFO, and one for the external auditor. The CFO version reads: "AI clears the disputes, cutting the backlog from ten days to two, measured against last quarter's baseline."
**Options**
- A. The figure has no published source, so the CFO cannot verify the claim
- B. The sentence drops the human checkpoint entirely, leaving the CFO believing there is no review gate at all
- C. It's too brief for a CFO, who needs the underlying mechanism and failure modes in full
- D. There's no problem — executives want outcomes, and oversight detail belongs only in the auditor's version

**Answer:** B — Omitting the human checkpoint from an executive summary isn't appropriate brevity — it actively misleads the reader into believing the process is fully automated when it isn't. The gate should always be named, even briefly, regardless of audience.

---

### Q29.
A customer-onboarding workflow using Claude has run smoothly for four months. Five changes are proposed. **(Select TWO — all-or-nothing)** Which **TWO** would leave Claude with more authority than the step's actual risk allows?
**Options**
- A. Let Claude approve identity-verification exceptions directly — a binding decision that is hard to unwind — because its summaries have been accurate for months
- B. Have the compliance analyst sign off on the day's exceptions straight from the AI-written summary line, without opening the underlying case file, to meet a service-level deadline
- C. Move document-field extraction into a reusable Skill so it behaves consistently for everyone on the desk
- D. Compute risk scores via code execution and keep the analyst's approval gate immediately after that step
- E. Add a named reviewer and a defined checkpoint for the step that drafts the rationale behind each exception

**Answer:** A, B — A gives Claude the actual binding, hard-to-reverse decision. B keeps a human "in the loop" only in name — signing off without opening the case file is a rubber stamp, not real review. C, D, and E all correctly keep human judgment substantively in the loop.

---

### Q30.
A marketing associate attaches two years of event data and asks Claude for next year's calendar with a budget allocation per event. The plan is detailed and confidently allocates last year's total budget across twelve events. Unknown to the associate, leadership halved the events budget in a meeting last week, and that decision exists in no document anywhere.
**Options**
- A. The prompt was under-specified; more detail would have made the model hedge about the budget
- B. The wrong model tier was used; a more capable model would have flagged the budget uncertainty
- C. A required input (the leadership decision) was never available to the model at all, so it confidently filled the gap with the only figure it had
- D. The attached data was too large, so the budget-cut information was dropped from context

**Answer:** C — This isn't a prompting or model-tier failure; it's a case where a fact the plan depended on simply never entered the system. No amount of specification or model capability compensates for an input that was never provided.

---

### Q31.
A facilities associate has Claude extract every operating requirement from a new franchise agreement and onboarding emails. The output is a tidy list of 37 requirements, each with a short label. Before the team starts planning around it, what request most reduces the risk of missing an obligation?
**Options**
- A. For each requirement, add its source clause, whether the emails already resolve it, and whether it's ambiguous enough to need a question
- B. Draft the opening-day plan immediately and flag any requirement it can't meet
- C. Group the 37 requirements by theme and rank them by cost-of-error
- D. Summarize the agreement into two pages so the list can be checked against that summary instead

**Answer:** A — Adding traceability (source clause), resolution status, and an explicit ambiguity flag to each item is what surfaces gaps before planning starts — grouping, ranking, or re-summarizing doesn't add that missing verification layer.

---

### Q32.
A hotel-group associate delegates: shortlist three conference venues with on-site AV for a 120-person event in the second week of March, in a table with links, under a stated budget — including the audience/purpose, budget, AV need, table format, and which two figures the associate will personally verify. In the result, two venues tied on price; Claude picked one and silently dropped the other, and it quietly widened the date range to "late March" to find a third option.
**Options**
- A. Add an instruction to show the plan of steps before starting, for approval
- B. Add more detail about the event's audience and purpose
- C. Add a requirement that Claude list every assumption it made, after finishing
- D. Add a line stating explicitly what Claude may decide on its own, and that it must flag it whenever it does

**Answer:** D — The failure here is silent decision-making on choices that mattered (a tie-break, a scope change to the date range) — not missing detail or missing an after-the-fact assumptions list. An explicit "decide freely, but say when you did" instruction is what prevents silent scope changes.

---

### Q33.
A support team records customer calls with consent for quality assurance, and the transcripts already sit inside an approved Claude workspace. The product team now asks an associate to mine those same transcripts for upsell opportunities to hand to sales.
**Options**
- A. Proceed — the transcripts are already inside an approved workspace, so no new upload is needed
- B. Strip customer names first, then run the upsell analysis inside the approved workspace
- C. Run it in an incognito chat so the upsell analysis leaves no trace
- D. Take it to the data owner first — the transcripts were collected under consent for one specific purpose (QA), and using them for a new purpose (sales upsell) needs fresh authorization

**Answer:** D — Data collected under consent for a specific stated purpose can't be silently repurposed for a different one, even if it's technically already inside an approved system. That's a purpose-limitation question for the data owner, not a technical-access question.

---

### Q34.
An AI-prioritized complaints queue appears to consistently rank complaints from corporate accounts above older, still-unresolved complaints from individual customers. The associate who noticed this doesn't own the complaints policy and isn't sure whether the pattern is actually a problem.
**Options**
- A. Proceed with the queue as-is; corporate accounts plausibly do carry more at stake
- B. Work through who is affected, what could go wrong for them, and what disclosure might be owed, then escalate to the policy owner with that reasoning
- C. Re-run the prioritization with the account-type field removed and adopt whichever ordering looks fairer
- D. Ask the assistant whether its own ranking is biased, and keep the queue if it says no

**Answer:** B — This is a fairness/People-impact question outside the associate's ownership. The right move is to reason through impact and disclosure obligations, then escalate to whoever owns the policy — not to unilaterally re-engineer the ranking or trust the model's self-assessment of its own bias.

---

### Q35.
A procurement lead wants Claude to take over the monthly supplier-scorecard process. Which approach best establishes whether it can actually be trusted with the work?
**Options**
- A. Feed it this month's new data, review the output carefully, and adopt it if the scores look reasonable
- B. Ask Claude to explain its intended method first, and judge that explanation before running anything
- C. Run this month's data through Claude twice and adopt the result if both runs agree
- D. Give it a past month whose scorecard the team already signed off on, withhold that known answer, and compare its output to the verified result

**Answer:** D — This is the known-answer test: comparing output against a case whose correct answer is already established is what actually earns trust, rather than a plausibility check, a stated-method review, or self-consistency across repeated runs (which can be consistently wrong).

---

### Q36.
An associate writes three descriptions of the same AI-assisted workflow — one for a technical lead, one for an executive, one for a risk/compliance team. Which description pairing correctly matches audience to content?
**Options**
- A. Technical lead gets the mechanism (rules/thresholds and what triggers human review); executive gets the outcome plus a named checkpoint; risk team gets the specific control and audit trail
- B. All three get the identical description, since the underlying facts don't change
- C. Only the risk team needs to know a human checkpoint exists; the others can be told it's "fully automated" for simplicity
- D. The executive gets the mechanism in full detail, since executives approve budgets and need the most technical depth

**Answer:** A — Detail level should shift by audience, but the human checkpoint itself must appear in every version, worded for what each audience needs to act on — never omitted for simplicity.

---

### Q37.
A retail chain's reporting team has Claude draft one document explaining why a product launch missed its sign-up target. The same finding must now reach both the executive committee and the store-floor staff whose process is changing as a result.
**Options**
- A. Produce one rewrite per audience, each shaped around what that reader needs to decide or do next, edited in separate passes
- B. Ask Claude to make the draft "more professional" and send that single version to both audiences
- C. Send the identical document to both audiences with a different cover note for each
- D. Generate three drafts in different styles, pick the strongest, and send that one version to both audiences

**Answer:** A — Different audiences need different framing built around their own decisions/actions, not a single polished draft, a cosmetic cover note, or a single "best" style applied universally.

---

## Domain 6 — Governance, Risk, and Responsible Use (15% — Q38–Q52)

### Q38.
A field-engineering team at a utility company has been photographing site-inspection reports (which include customer site details) and sending the photos to a consumer chatbot app on personal phones, because the company's approved connector cannot process images. No one acted with bad intent.
**Options**
- A. Report the capability gap to the policy owner and fix the approved path, while keeping the consumer app closed to customer data
- B. Block the consumer app on company phones and circulate a reminder that unapproved tools are prohibited
- C. Relax the policy to permit the consumer app for site reports, since the engineers will keep using it regardless
- D. Open disciplinary proceedings against the engineers to deter further violations

**Answer:** A — The root cause is a genuine capability gap in the approved tool, not misconduct. Fixing the approved path (so there's a legitimate way to do the job) addresses the actual cause; blocking or disciplining without fixing the gap just pushes the same workaround elsewhere, and loosening policy accepts the risk instead of closing it.

---

### Q39.
A lettings firm's proposal has Claude issue final decisions on tenant deposit forfeiture directly from the tenancy agreement and inspection file. The firm argues any accuracy concern disappears if they simply use the most capable model available.
**Options**
- A. Appropriate with light human review, since a capable model's error rate is low enough for spot-checks to catch the rest
- B. Fully appropriate, since the source files contain everything needed and errors can be corrected once noticed
- C. Inappropriate for any involvement at all, including summarizing the inspection file, since the subject is legal
- D. Inappropriate as the final decision-maker: accountability cannot transfer to a tool regardless of model capability — a better model changes the error rate, not who is accountable

**Answer:** D — This is a classification question about accountability, not accuracy. No model capability upgrade changes who is responsible for a binding legal-financial decision affecting a third party; the decision-maker role itself is inappropriate for full delegation, even if summarization support (a lesser role) might be fine.

---

### Q40.
A team lead can't tell from written policy whether recording customer calls for AI summaries requires per-customer consent in a jurisdiction the company just entered. The question must go to the legal owner. Which escalation gives that owner the most useful basis for a decision?
**Options**
- A. The workflow itself, who it reaches, the control already in place, and the one specific question policy leaves open
- B. A completed ten-criterion risk matrix with a total score and a recommendation to approve
- C. "I think this is probably fine — can you approve it today so we can start recording tomorrow morning?"
- D. A request to pause all recording until the AI policy is rewritten to explicitly cover consent

**Answer:** A — A useful escalation gives the decision-maker concrete facts (the workflow, its reach, existing controls) and one clearly bounded open question — not a pre-baked recommendation disguised as a score, pressure for a same-day approval, or a demand to halt everything before the actual question is even answered.

---

### Q41.
An associate proposes running all supplier-pricing discussions in Claude's incognito chat, and, for colleagues on a competing AI tool, in that tool's temporary-chat mode, "so there's nothing on record if the audit team asks."
**Options**
- A. Both modes discard the conversation entirely and instantly — neither vendor retains anything
- B. Both modes keep the chat out of the assistant's own history/memory, but each vendor may still retain a copy for a period, and company records/legal holds can still capture it
- C. Claude's incognito leaves no trace at all, but the competing tool's temporary mode is fully retained, so the plan only works for Claude users
- D. Neither private mode changes anything of substance — both are stored in ordinary history regardless

**Answer:** B — Private/incognito modes affect what the *assistant's own interface* shows you (history, memory) — they are not a guarantee against vendor-side retention or an organization's own records/legal-hold obligations. Treating them as "nothing on record" is a governance misunderstanding, not a safe practice.

---

### Q42.
After twelve consecutive clean runs of an AI-drafted monthly client analysis, a vendor proposes the outputs be labeled "AI-generated" going forward with no named human owner attached, arguing the track record proves reliability.
**Options**
- A. A track record earns the assistant similar future work, but each output still needs a named person attached who answers for it
- B. After enough clean runs, accountability shifts to the vendor whose model produced the analysis each month
- C. Labeling the output "AI-generated" satisfies the accountability requirement, since readers are told its origin
- D. A named owner is only needed if a client actually challenges an output — otherwise the label alone is enough

**Answer:** A — Accountability doesn't erode with a good track record and doesn't transfer to the tool or vendor, and a disclosure label is not a substitute for a specific person who owns and answers for the result.

---

### Q43.
A facilities analyst wants to find building-usage patterns across a year of badge-swipe records. Policy restricts sharing regulated personal data. The analyst replaced every badge number with a coded value — but the workbook's second tab still holds the lookup table mapping each code back to a real employee.
**Options**
- A. Proceed as planned — coding the badge numbers already anonymizes the data
- B. Upload it as-is, but only in an incognito chat, so the lookup tab isn't retained afterward
- C. Remove the lookup tab and any other identifying fields, confirm no mapping travels with the file, then run the analysis
- D. Abandon the analysis entirely, since the data can't be made safe without destroying the pattern it needs

**Answer:** C — Coding is not anonymization if the re-identification key travels alongside it. Removing the lookup table (and confirming nothing else identifies individuals) preserves the useful pattern while actually removing the regulated-data risk — incognito mode doesn't fix a data-content problem.

---

### Q44.
An accounts-payable desk computes each invoice's early-payment discount via code execution; a supervisor then releases or holds each payment. A team member proposes dropping the supervisor step "because the arithmetic is code, and code is always right, so the supervisor is just re-reading the same numbers."
**Options**
- A. Agree — a correctly computed figure doesn't need a human check
- B. Keep the step: delegating the computation is safe specifically because a wrong figure can still be caught and reversed before release, and a person still makes that call
- C. Replace the supervisor with a second, independent AI pass that recomputes and flags differences
- D. Move the calculation back to fully manual work, since payment-adjacent steps should stay human-owned

**Answer:** B — "The math is code" addresses correctness of computation, not the separate question of who is accountable for releasing an irreversible payment. Reversibility and accountability are why the checkpoint exists, independent of how reliable the math is.

---

### Q45.
A hiring team asks Claude to "organize applications for reading" by summarizing each candidate's resume. This seems like a low-risk administrative task.
**Options**
- A. This is fully AI-appropriate with no review needed, since summarizing text isn't a hiring decision
- B. This is appropriate-with-review: a selective or subtly biased summary can influence which candidates get a fair look, even though summarization itself sounds administrative — a named reviewer should check the summaries before any rejection decision
- C. This is inappropriate for any AI involvement, since it touches hiring
- D. This requires disclosure to every candidate before summarization can begin

**Answer:** B — The classification isn't about how the task sounds ("just organizing") but about its downstream effect: a biased summary can shape a hiring outcome. That makes it appropriate-with-review, not fully hands-off or fully forbidden.

---

### Q46.
A manager tells a client, "The AI drafted this, so any mistake in it is the AI's fault, not ours."
**Options**
- A. This is accurate — the entity that generated the content bears responsibility for its errors
- B. This is inaccurate — accountability for a delivered output stays with the person/company that used the tool and sent the work out, regardless of how much of the draft the AI produced
- C. This is accurate only if the client was told AI was used
- D. This is accurate only for low-stakes deliverables

**Answer:** B — Accountability never transfers to the tool. Whoever reviewed, approved, and sent the work remains responsible for it, regardless of authorship split between human and AI.

---

### Q47.
A governance review finds that a customer-complaints workflow discloses "an AI tool assists with initial triage" to customers whose complaints were fast-tracked, but says nothing to the much larger group whose complaints were not fast-tracked, even though the same AI tool made that routing decision too.
**Options**
- A. This is fine, since only the fast-tracked group experienced a visible outcome from the AI's involvement
- B. Disclosure should apply based on whether AI meaningfully affected someone's outcome, not whether that effect was a "positive" one — the non-fast-tracked group was also affected by the same AI decision and the disclosure gap should be corrected
- C. No disclosure is needed either way, since triage is an internal operational process
- D. Disclosure is needed only if a customer specifically asks whether AI was involved

**Answer:** B — Being routed *away* from expedited handling is still an AI-driven outcome affecting the customer, just as much as being fast-tracked. Disclosure obligations track actual impact on the person, not whether the impact happens to look favorable.

---

### Q48.
A regulated-industry team wants to connect a new client's real case files to Claude for the first time, to test a proposed AI-assisted intake workflow.
**Options**
- A. Connect real client files immediately, since testing on real data gives the most accurate signal
- B. Build and test the workflow first against synthetic or invented data resembling the real files, and only move to approved real accounts once the workflow is validated
- C. Use a competitor's AI tool for the first test instead, to avoid exposing data to a new tool
- D. Skip testing altogether and go straight to production with close monitoring

**Answer:** B — For regulated data (healthcare, legal, financial, student records, etc.), the standing practice is to validate a new workflow against synthetic data first, and only use real, approved accounts once the approach is proven — not to expose real regulated data to an unvalidated process.

---

### Q49.
A finance associate is deciding how to classify an upcoming task: "have Claude draft the wording of a customer refund-policy exception, to be issued after a named supervisor's sign-off." Which single factor is the clearest "deciding factor" that makes this appropriate-with-review rather than fully AI-appropriate?
**Options**
- A. The task involves writing text, which is always appropriate with review
- B. Accountability: the company remains responsible for what actually goes out to the customer, and a named supervisor must be the one who can meaningfully check it before it's issued
- C. The task is time-consuming, so review helps quality
- D. Refund policy exceptions are always inappropriate for any AI involvement

**Answer:** B — The deciding factor is accountability plus a real reviewer who can meaningfully check the output before it's issued — not the format of the task (writing text) or its time cost, and not a blanket ban on the subject matter.

---

### Q50.
A school district's IT team enabled a community-published Claude skill, after only a quick glance at its description, on a shared drive connection set to write mode. Separately, they run a full security-style review before every use of the assistant's own built-in spreadsheet skill on internal data.
**Options**
- A. Apply the same full review to both, for consistency, and keep the current settings otherwise
- B. Drop the built-in-skill review since it hasn't caused problems; keep the community skill as-is
- C. Disable the community skill until it has actually been reviewed, return its drive connection to read-only in the meantime, and keep the review discipline already applied to the built-in skill
- D. Remove all skills entirely until an approved list exists

**Answer:** C — An unreviewed, third-party skill with write access to a shared drive is a materially higher-risk configuration than a vetted, built-in one — it needs to be disabled and downgraded to read-only until actually reviewed, not simply added to a uniform review checklist after the fact.

---

### Q51.
A team wants to reuse call-center transcripts (recorded with consent for quality-assurance purposes) to train a customer-sentiment classifier that will inform staff bonuses.
**Options**
- A. Proceed, since the transcripts are already lawfully collected and stored
- B. Take this to the data owner: using QA-consented data to build a bonus-affecting classifier is a new purpose beyond the original consent, and needs its own review/authorization
- C. Proceed, but only using transcripts older than one year
- D. Proceed, but anonymize speaker names in the transcripts first, which resolves the concern fully

**Answer:** B — The issue is purpose limitation, not data age or anonymization — data given for one stated purpose (QA) being repurposed for something with real consequences for staff (bonuses) needs fresh authorization from whoever owns that data, regardless of how well it's otherwise handled.

---

### Q52.
A manufacturing plant's safety officer asks whether an AI tool can be allowed to draft (not finalize) incident-investigation reports following workplace injuries, with a named safety engineer reviewing and signing every report before it's filed.
**Options**
- A. Inappropriate for any involvement — safety incidents are too sensitive for AI to touch at all
- B. Appropriate-with-review: drafting support is reasonable given a defined reviewer (named engineer), a specific check (accuracy and completeness against the incident record), and a clear "before filing" checkpoint
- C. Fully appropriate with no review needed, since a human reported the incident originally
- D. Appropriate only if the AI tool itself carries professional liability insurance

**Answer:** B — This is a textbook appropriate-with-review case once WHO (named engineer), WHAT (accuracy/completeness check), and WHEN (before filing) are all defined — a defined gate, not a blanket ban or a no-review default.

---

## Domain 1 — Prompting and Task Execution (14% — Q53–Q66)

### Q53.
A facilities associate attaches warehouse site-inspection notes and asks Claude to "write up the inspection." The result is a tidy, general narrative — useless for its real purpose, since the insurer's loss adjuster only needs the three open defects, each with a date found and photo reference. A colleague suggests the fix is simply a much longer prompt.
**Options**
- A. State the reader, the purpose, the required length, exactly what items to cover, and what to leave out
- B. Make the prompt much longer by describing the warehouse and inspection day in exhaustive detail
- C. Re-run the request with extended thinking turned on so the model infers what the reader needs
- D. Attach last year's internal narrative report so the structure gets copied exactly

**Answer:** A — The problem was missing specification (reader, purpose, scope), not insufficient length or reasoning depth. Naming exactly who reads it and what they need is what turns a generic narrative into a usable defect list.

---

### Q54.
An insurance-claims associate gets a first draft letter to a delayed policyholder: 700 words against a 200-word limit, addressed generically to "the customer," with the required action buried at the end.
**Options**
- A. "Score this draft out of ten and keep improving whatever scores lowest until it's a nine."
- B. "This isn't right. Try a completely different approach to the whole letter."
- C. Rewrite the original prompt from scratch with much more detail and try it on a stronger model.
- D. "The length broke, the reader is one worried policyholder, and the ask is buried — keep everything else and fix those three things."

**Answer:** D — Effective iteration targets the *specific* things that broke (length, tone/addressing, buried ask) rather than triggering a full rewrite, a vague quality score, or a fresh prompt-and-model combination that discards a draft that was mostly fine.

---

### Q55.
A procurement manager's first draft request reads, "Tell me this shortlist is defensible." **(Select TWO — all-or-nothing)** Which **TWO** rewrites are most likely to produce an honest evaluation rather than a persuasive defense?
**Options**
- A. "Rate the shortlist 1–10 on coverage, cost realism, and risk, with the one change that would most improve it."
- B. "Defend the shortlist against the objections that finance is likely to raise about it."
- C. "Give the strongest case for and against sending this shortlist to the committee exactly as it stands."
- D. "Isn't this shortlist good enough for the committee? Just point out anything minor to tidy up."
- E. "Rate your confidence, as a percentage, that this shortlist survives the committee unchanged."

**Answer:** A, C — A asks for a genuine rubric-based critique with an actionable change; C explicitly asks for both sides, avoiding a one-sided defense. B, D, and E all presuppose or lead toward the conclusion that the shortlist is fine.

---

### Q56.
An operations lead at a solar installer must reconcile fourteen months of "messy" technician-shift exports against sign-in sheets. Only one of the fourteen files has been opened so far. The plan is to write an exhaustive rule for every irregularity imaginable, then have an assistant write and run the reconciliation code.
**Options**
- A. Write the full rule set for every imaginable irregularity before any code is written
- B. Request the reconciliation now, and fix data problems as they surface in the output
- C. Ask the assistant to first profile the files and list anything ambiguous or irregular, before any rule is written
- D. Ask for the code in a named language so the logic can be read before it runs on real files

**Answer:** C — Writing exhaustive rules for problems that haven't been observed yet (only one of fourteen files has even been opened) is guessing. Profiling the actual data first is what task-decomposition looks like here — rules should follow from what's actually found, not precede it.

---

### Q57.
A learning-and-development associate asks Claude for five different *formats* for launching a leadership program. The request also fixes a specific slide template, two mandatory sections, a 60-word limit per idea, and the house tone. All five "formats" come back as minor variants of the same single workshop structure.
**Options**
- A. The response's shape was pinned too tightly for a genuinely divergent, options-generating request; keep the situation details, but loosen the format constraints, and tighten again once a direction is picked
- B. The model lacked context; add more detail about the audience, goals, and last year's participation figures
- C. The model needs an example to imitate; attach a competitor's launch campaign
- D. The task needs deeper reasoning; turn on extended thinking

**Answer:** A — This is a divergent (brainstorming) task that was constrained like a convergent (drafting) one — a fixed template, mandatory sections, and a strict word limit collapse the variation a "give me five different formats" request is supposed to produce. Loosening the format constraints, not adding more context or reasoning depth, is the fix.

---

### Q58.
In a fresh chat with no prior history, an associate asks Claude to draft a tariff-change notice for customers. The first reply omits the required legal footer and states amounts in the wrong currency. This is the first such notice the associate has ever drafted with Claude.
**Options**
- A. Switch to a more capable model immediately, since a stronger model wouldn't drop the footer or the currency
- B. Start another fresh chat and resend the identical request, in case the first chat was already overloaded
- C. Treat it as under-specification: re-read the original request against its actual required parts (footer, currency, amounts) and add what was missing
- D. Check whether a stored instruction or knowledge file has gone stale since the last notice

**Answer:** C — With no conversation history to overload and no prior working version to compare against, a first-attempt miss on unstated requirements (footer, currency) is a specification gap, not a model-capability or context/staleness issue.

---

### Q59.
A hotel-group associate's delegated request already states the reader, purpose, budget, AV requirement, table format, and which two figures will be manually verified. Despite this, Claude silently dropped a tied venue option and quietly widened the date range to find a third option.
**Options**
- A. The request needed even more background detail about the event
- B. The request needed an instruction on what Claude may decide on its own, and a requirement that it flag whenever it exercises that discretion
- C. The request needed to specify the output format more precisely
- D. The request needed a stricter budget constraint

**Answer:** B — The request was already well-specified on content; what was missing was a boundary on autonomous decision-making itself — permission to decide combined with a requirement to disclose when a decision (like a tie-break or scope change) was made.

---

### Q60.
A customer-insights associate pastes forty interview transcripts into a single message and asks for theme-coding, tallying, ranking, and a final memo — all in one pass. An error in coding eight transcripts later turns out to have propagated into the final memo's conclusions.
**Options**
- A. Keep the single-pass request but add "work carefully and re-check your work"
- B. Send one request per stage — code the themes first, verify the coding against the transcripts, then tally, rank, and write the memo
- C. Run the identical single-pass request on a more capable model
- D. Split the forty transcripts into four batches of ten, still running the full single-pass pipeline on each batch

**Answer:** B — Multi-stage decomposition with a verification step between coding and downstream aggregation is what catches an error before it propagates — not more careful wording, a stronger model on the same flawed pipeline, or smaller batches of the same unverified single-pass approach.

---

### Q61.
A strategy associate needs a proposal to redesign a company's returns process. Their instinct is to ask for the complete proposal immediately, with extended thinking on.
**Options**
- A. Ask for the complete proposal now, with extended thinking on, and iterate as structure emerges
- B. First ask Claude to map what's already known — existing approaches, what other firms have tried, prior internal attempts — before anything gets produced
- C. Ask for three complete proposals in different styles, then pick the strongest as the base
- D. Ask Claude to grade the associate's own outline out of ten, with reasons, before any writing begins

**Answer:** B — Mapping the known landscape first is task decomposition applied to an open-ended strategy problem: it grounds the eventual proposal in what's already known, rather than generating a confident, ungrounded first draft (or three) to fix up afterward.

---

### Q62.
An HR associate's first prompt reads: "Write something about our new benefits package." The result is generic and unusable.
**Options**
- A. "Write something better about our new benefits package."
- B. "Write a 150-word all-staff email announcing the new benefits package, warm and clear tone, ending with where to enroll."
- C. Repeat "write about our benefits package" two more times
- D. "You are the most experienced HR communicator in the world — write something truly outstanding about our benefits."

**Answer:** B — Concrete specification (length, audience/channel, tone, required closing action) is what fixes a vague request — not a vaguer "better" instruction, repetition, or an elaborate persona with no actual content constraints.

---

### Q63.
An operations lead needs a quarterly review covering budget variance, project status, staffing, and next-quarter risks, and sends this as one single prompt. The result covers all four topics shallowly and unevenly.
**Options**
- A. Ask for the same document again but double the requested word count
- B. Tell Claude to "try harder on the weak sections"
- C. Switch the output to bullet points so shallow sections are less noticeable
- D. Decompose it: request each section separately, review each, then request a combined, consistent final draft

**Answer:** D — A single mega-prompt covering four distinct topics splits the model's attention unevenly; decomposing into per-section requests (then combining) is what produces even, adequate coverage — the other options mask the symptom rather than fixing the underlying complexity.

---

### Q64.
A support-operations associate needs to know the current VAT rate for a customs declaration, needs a cited multi-source comparison of cold-chain logistics providers in East Africa (with funding and key customers), and needs to know what a shipping term ("demurrage") means for a colleague. **(Select THREE — all-or-nothing)** Which **THREE** correctly pair each request with the most fitting way to answer it?
**Options**
- A. The VAT-rate lookup → a quick, current-facts check (e.g., web search), not a long research pass
- B. The multi-source, cited comparison with funding/customer detail → a deeper research-style pass that gathers and cites multiple sources
- C. The "what does demurrage mean" question → an inline conversational reply, not a formal document
- D. The VAT-rate lookup → a long multi-source research pass, to be thorough
- E. The definition question → a document artifact, since any technical term deserves its own file

**Answer:** A, B, C — A quick current-fact lookup doesn't need heavy multi-source research (ruling out D); a broad, cited, multi-source comparison is exactly what a deeper research pass is for; a one-line definition fits naturally as a short conversational reply rather than a standalone document (ruling out E).

---

### Q65.
A junior analyst with no customs background uses Claude to draft a customs-compliance briefing the operations team will follow when clearing shipments. It addresses every requirement in the request and is fully consistent with the uploaded regulation extract.
**Options**
- A. Ask a colleague to proofread the briefing for tone, clarity, and consistency
- B. Ask a colleague with actual customs experience whether the briefing is credible by the field's own professional standards
- C. Ask Claude to rate the briefing's own accuracy and revise any section scoring below a nine
- D. Run a formatting pass so the briefing reads as polished as an expert-written one

**Answer:** B — Internal consistency and full requirement coverage don't confirm subject-matter credibility. The specific gap here — a junior analyst's lack of domain background — is only closed by a genuine subject-matter expert's judgment, not proofreading, polish, or self-rated accuracy.

---

### Q66.
A facilities associate pastes a lift-maintenance contract and asks for the contractor's response-time obligations. Claude lists four obligations fluently; three are genuinely in the contract, and the fourth (a two-hour emergency call-out) is not in this contract, though it's common industry practice.
**Options**
- A. Turn on web search so Claude can also check industry-standard response times
- B. Attach the contract as a file instead of pasting the text, expecting more careful reading
- C. Instruct Claude to answer strictly from the pasted text, quote the sentence behind each claim, and state "not in the source" where nothing supports an answer
- D. Add "be accurate and don't make anything up" and re-run the identical request

**Answer:** C — The model filled a real gap with a plausible industry norm not actually present in this contract — a source-boundedness instruction requiring quotes (or an explicit "not found") is what prevents that specific failure, not attachment format, added web search, or a generic accuracy plea.

---

## Domain 3 — Product and Model Selection (12% — Q67–Q78)

### Q67.
A legal-operations associate, using a mid-tier model with extended thinking already on, analyzes a 180-page master services agreement for cross-referencing obligations. The same prompt worked well on a 20-page contract. On the 180-page document, the answer is fluent but shallow, missing obligations spread across multiple sections.
**Options**
- A. Move to the flagship-tier model, which is built to hold a long, complex structure coherent across the whole document at once
- B. Switch to the fastest, lightest-tier model to process the document more quickly
- C. Turn extended thinking off, since the extra reasoning may be diluting attention to the text
- D. Split the agreement into ten separate chats so each section is analyzed alone

**Answer:** A — This is the classic "escalate for depth" case: a task requiring one large, complex structure to stay coherent across 180 pages is exactly what the top model tier is suited for, not a lighter/faster model, not disabling reasoning depth, and not fragmenting the document so cross-section references get lost between chats.

---

### Q68.
A sales associate runs a research-mode / heavy web-lookup pass every time a pricing question comes up, "so Claude looks it up thoroughly." Answers take minutes and consistently miss the firm's own discount rules, which live in an internal policy document, not the open web.
**Options**
- A. Keep research mode, but add "use our internal pricing policy" to each request
- B. Switch to the flagship model for pricing questions, since it has "read more" pricing material
- C. Put the internal policy into a Project's knowledge and ask pricing questions in chat inside that Project
- D. Paste the policy document into every new chat before asking

**Answer:** C — The actual problem is a feature/configuration mismatch: research mode searches external sources, while the needed information is internal and static. Putting it into a Project's always-on knowledge is the fix — not repeating an instruction to a feature that searches the wrong place, upgrading the model, or manually re-pasting the same document every time.

---

### Q69.
Five tasks are under consideration for turning on extended (slower, more resource-intensive) thinking. **(Select TWO — all-or-nothing)** For which **TWO** is the extra cost worth it?
**Options**
- A. Converting a bulleted meeting agenda into a calendar invite for a weekly team meeting
- B. Choosing a rollout sequence across four warehouses under staffing, downtime, and budget constraints simultaneously
- C. Finding the expansion of an acronym in an attached glossary for a routine email
- D. A staffing decision across three sites with real consequences, seasonality effects, and overtime rules to balance
- E. Producing ten quick, casual name ideas for a new internal chat channel

**Answer:** B, D — Both are genuine multi-constraint reasoning problems (competing constraints that must be balanced against each other) where deeper reasoning materially changes quality. A, C, and E are simple, low-stakes, single-step tasks where extended thinking adds cost without adding value.

---

### Q70.
A support team runs every routine meeting-notes tidy-up through the flagship model with extended thinking on, and runs its once-a-year, high-stakes pricing-model rebuild on the lightest, fastest model tier "to save budget." A new team lead feels both choices are wrong.
**Options**
- A. Only the pricing-model choice is wrong; the flagship-plus-thinking default for tidy-ups is a safe choice even if slower
- B. Neither choice is wrong; model tier is purely a cost decision, and quality differences between tiers are marginal
- C. Only the tidy-up choice is wrong; the rebuild simply needs extended thinking turned on, regardless of model
- D. Both are wrong, in opposite directions: the flagship-plus-thinking setup spends budget on work that needs neither, while the lightest tier under-serves the one task that actually needs depth

**Answer:** D — Routine, low-complexity tidy-ups don't need the top tier or extended reasoning, while a high-stakes, complex annual rebuild is exactly the kind of task that benefits from more capability, not less. Both defaults are mismatched to their tasks, in opposite directions.

---

### Q71.
A marketing associate runs 50 short product-description generations daily on the flagship model, saying "I want the best quality every time."
**Options**
- A. This is the correct default, since quality should never be compromised
- B. This wastes cost/latency on high-volume, low-depth work; a faster, lower-cost tier is well-suited to short, straightforward descriptions at this volume
- C. This is correct only if the descriptions are for a premium product line
- D. This is correct as long as the associate reviews all 50 outputs afterward

**Answer:** B — High-volume, low-complexity work is exactly where a lighter/faster tier is the right default — reserving the flagship tier for tasks that actually need deep, coherent reasoning, not for routine bulk generation.

---

### Q72.
A financial analyst is three hours into one long conversation getting coding help from Claude, and the quality of responses has noticeably degraded.
**Options**
- A. Immediately switch to a different, more capable model
- B. First check whether context has become overloaded (the conversation is very long); then decide to restart fresh, summarize and carry forward the key points, or persist key context into a Project — model tier isn't the first thing to change if the model was working fine earlier
- C. Repeat the exact same request again in the same chat
- D. Add "please pay closer attention" to the next message

**Answer:** B — Since quality was fine earlier in the same conversation, the likely cause is accumulated context length, not a model-capability gap. The judgment call is restart/summarize/persist, not jumping straight to a different model or repeating/pleading with the same overloaded context.

---

### Q73.
A consultant tells a client, "We always use the most capable model available for everything, so quality is never a concern."
**Options**
- A. This is a strong, defensible practice that should be adopted broadly
- B. This statement reflects a lack of task-fit judgment — CCAO-F/PCAO-F judgment is about matching model tier to the task's actual complexity and stakes, not defaulting to maximum capability regardless of task
- C. This is only a weak statement if the client asks about cost
- D. This is a strong practice specifically for regulated industries

**Answer:** B — "Always use the biggest model" is a marketing claim, not a judgment demonstration — the tested skill is choosing the tier that fits each task, escalating for genuine complexity and dropping tier for high-volume simple work.

---

### Q74.
A team needs Claude to answer "what did the port authority announce this morning about a berth closure," pull an approved rate card from a shared drive, and assess "which of two leases is riskier to exit early, given their break clauses." **(Select THREE is not applicable here — pick the single best-matched trio statement)** Which set of feature choices is correctly matched?
**Options**
- A. Berth-closure announcement → a quick current-facts web lookup; rate card retrieval → a connector to the shared drive, not web search; lease-risk comparison → extended thinking, since it requires weighing multiple contract terms against each other
- B. All three → web search, since web search can access everything given enough retries
- C. All three → extended thinking, since every business question benefits from deeper reasoning
- D. Berth-closure announcement → extended thinking; rate card retrieval → web search; lease-risk comparison → a quick lookup

**Answer:** A — Each task fits a different feature for a specific reason: a live public announcement needs current web information; an internal file needs a connector to where it actually lives (not the open web); and comparing risk across contract clauses is a multi-factor reasoning task suited to extended thinking.

---

### Q75.
A pricing Project produces a customer quote listing unit prices, to the cent, that nobody on the team currently recognizes. The associate assumes Claude hallucinated the figures and plans to re-prompt with "use only current prices."
**Options**
- A. Re-prompt with stricter wording about using only current prices, and regenerate the whole quote
- B. Check the Project's knowledge files for a superseded rate card that's still sitting there, replace it if so, and set a review date for the file
- C. Switch the Project to the flagship model, which is less prone to fabricating figures across long documents
- D. Ask Claude to rate its confidence in each price and keep only prices rated above 90%

**Answer:** B — This isn't necessarily hallucination — a stale, superseded document sitting in the Project's always-on knowledge would produce exactly this symptom (confident, precise, but outdated prices). Checking the actual knowledge source is the correct first step, not assuming fabrication and re-prompting or upgrading the model.

---

### Q76.
An operations director insists that turning on extended thinking always requires switching to the flagship model too, "since deeper reasoning needs the biggest model." A routine, one-step formatting task gets both extended thinking and the flagship tier turned on together.
**Options**
- A. Correct as stated — extended thinking and model tier must always move together
- B. Extended thinking is a separate switch from model tier; a routine, single-step task needs neither the flagship tier nor extended thinking, regardless of this stated rule
- C. Extended thinking is only available on the flagship tier, so the pairing is required by design
- D. Model tier only affects cost, so pairing them this way causes no real harm either way

**Answer:** B — Model tier (fast / thinking-capable / flagship) and extended thinking (a reasoning-depth toggle) are independent choices. A routine, low-complexity task needs neither turned up, and treating them as permanently bound together produces needless cost on simple work.

---

### Q77.
A support-operations lead has three tasks this hour: quickly classifying 500 incoming tickets by category, resolving a nuanced dispute over which of two overlapping SLA clauses applies to a customer, and staying coherent through a two-hour live troubleshooting session with that same customer.
**Options**
- A. Use the flagship model with extended thinking for all three, since customer-facing work always deserves the top tier
- B. Use a fast/lightweight tier for the 500-ticket classification, extended thinking for the nuanced SLA comparison, and manage the long session primarily through context judgment (summarizing or restarting as needed) rather than model tier alone
- C. Use the lightest tier for all three, since support work is inherently low-stakes
- D. Use extended thinking only for the 500-ticket classification, since sheer volume alone justifies deeper reasoning

**Answer:** B — Each task calls for a different lever: high-volume, simple classification suits a fast tier; a nuanced multi-clause comparison benefits from deeper reasoning; and a long live session's quality is primarily a context-management question, not simply a model-tier one.

---

### Q78.
A procurement associate has iterated four times with Claude on a supplier-scorecard table in chat. Columns, formatting, and filters are now correct, but the weighted-score column is still subtly wrong each round, despite increasingly precise wording about how weights should apply.
**Options**
- A. A feature mismatch: the weighted scores are being generated as prose by the model and belong in code execution instead
- B. A description problem: the wording about weights is still ambiguous and needs one more precise attempt
- C. A model problem: this needs the flagship model instead of the one currently producing the table
- D. A context problem: four rounds have overloaded the chat, so earlier weight instructions no longer hold

**Answer:** A — Four rounds of increasingly precise wording that still produce subtly wrong arithmetic is a strong signal this is a computation task being done as prose generation rather than actual calculation — moving the weighted-score math into code execution addresses the real cause, not further wording refinement, a bigger model, or context management.

---

## Domain 5 — Configuration and Knowledge Management (12% — Q79–Q90)

### Q79.
A consultant sets up Claude for ongoing work with one client. **(Select THREE — all-or-nothing)** Which **THREE** placements are correct?
**Options**
- A. A firm-wide writing-tone rule that should apply to every chat, for every client → account-level instructions
- B. The client's recurring reference files and past deliverables → that client's Project knowledge
- C. "This client's negotiation is paused until the end of the month" → account-level instructions
- D. "Treat any figure absent from the client's files as unconfirmed" → the client Project's instructions
- E. A one-off question about a colleague's unrelated internal memo → its own new Project

**Answer:** A, B, D — A firm-wide rule true across every chat belongs at the account level; client-specific reference material belongs in that Project's knowledge; a client-specific handling rule belongs in that Project's instructions. C is wrong (a temporary, client-specific fact doesn't belong in global account instructions), and E is wrong (a one-off unrelated question doesn't need a dedicated Project).

---

### Q80.
An associate added "always open with a three-line executive summary" and "use the Meridian account's tone guide" to their personal account-level instructions. Now every chat — including unrelated quick questions — opens with an executive summary in the Meridian voice.
**Options**
- A. Delete the account-level instructions entirely, since no single rule fits every conversation
- B. Keep both rules, but add exceptions to the account-level text for every kind of chat where they shouldn't apply
- C. Remove both rules and rely on memory to eventually learn when the summary/tone should apply
- D. Move both rules into the Meridian Project's instructions, and keep the account-level text limited to what's true everywhere

**Answer:** D — Both rules are scoped to one specific account/context, not to every conversation — they belong in that Project's scoped instructions, not the global account-level layer. Deleting everything, patching exceptions onto a global rule, or hoping memory infers scope are all worse fixes than placing the rule at its correct scope.

---

### Q81.
A teacher creates a separate Project for each course (syllabus, rubric, sample work included as knowledge), but still repeats the same instructions manually at the start of every chat.
**Options**
- A. Nothing is missing; repeating instructions is a normal part of using Projects
- B. The teacher isn't actually leveraging what a Project provides — a Project's files and instructions are meant to be always-on within that workspace, which should eliminate the need to repeat them each time
- C. The fix is to move the instructions into account-level settings instead
- D. The fix is to enable a connector for each course

**Answer:** B — A Project's whole purpose is to keep its instructions and knowledge always loaded for that workspace — repeating them manually each chat means the Project isn't being used as intended, not that something else needs to be configured.

---

### Q82.
A consultant connected a Gmail-style connector three weeks ago. Today's chat can't see the inbox at all.
**Options**
- A. The connector must have expired after three weeks and needs to be reconnected from scratch
- B. Check first whether the connector was actually enabled *for this specific conversation* — connecting an app and enabling it per-conversation are two separate steps, and forgetting the second is the most common cause
- C. Switch to a different AI tool that has native email integration
- D. The account must have hit a usage limit

**Answer:** B — The most common connector failure is exactly this: connecting an app is a one-time step, but many connectors still need to be turned on inside each individual conversation — checking that first, before assuming expiry or usage limits, is the efficient diagnostic order.

---

### Q83.
A team's internal policy document, uploaded as a Project knowledge file, was updated to a new version by the policy owner weeks ago. The old version is still sitting in the Project.
**Options**
- A. Nothing needs to happen — Claude will detect and fetch the newer version automatically
- B. The Project's knowledge source needs to be manually updated — replacing or removing the outdated file — since a static upload doesn't self-update
- C. Add an instruction telling Claude to "always follow the latest policy" instead
- D. Create an entirely new Project every time the policy changes

**Answer:** B — A Project's uploaded knowledge file is a static snapshot (unless it's a live connector); it doesn't fetch newer versions on its own, and an instruction to "follow the latest" is meaningless if the actual latest text was never provided. The physical file must be maintained.

---

### Q84.
An associate wants a single rule to apply automatically to every future conversation, without re-typing it, regardless of topic or project.
**Options**
- A. A Skill, since Skills apply automatically to every request
- B. Account-level custom instructions, since these are the layer meant to hold what should be true globally, in every conversation
- C. A Project's instructions, since Projects are always-on
- D. Chat history/search, since it retrieves relevant past context automatically

**Answer:** B — The one-line test: "I want this true always, everywhere" is exactly what account-level custom instructions are for — a Skill is on-demand (only activates when a request matches), a Project is scoped to its own workspace (not global), and history/search retrieves past content rather than applying a standing rule.

---

### Q85.
A retail consultant, for convenience, put both the wholesale and retail pricing files for one client into a single Claude Project. In a chat drafting a retail customer's quote, Claude applied the wholesale unit's volume discounts by mistake.
**Options**
- A. Add "unit: retail" at the top of every prompt, so Claude knows which files apply
- B. Create one Project per business unit, each with its own instructions and knowledge files, and move the files across accordingly
- C. Use incognito chats for retail quotes so nothing from the shared Project carries over
- D. Delete the wholesale files after each retail chat, and re-upload them whenever wholesale work comes up

**Answer:** B — Mixing two distinct rule-sets (wholesale vs. retail pricing) inside one always-on Project is a scoping error; separating them into their own Projects removes the ambiguity structurally, rather than relying on per-prompt reminders, incognito mode, or constant manual file shuffling.

---

### Q86.
In every new chat, Claude addresses an associate as the lead of a project that actually closed months ago, framing every answer around that stale context. The associate has been manually correcting this in every new prompt since.
**Options**
- A. Keep adding the correction each time, since it's cheap and has worked so far
- B. Switch to incognito chats permanently, so the wrong assumption is never loaded
- C. Switch models for all new chats, since a different model won't carry the closed project forward
- D. Find and read the stored memory note causing this, correct or delete it, then start a fresh chat

**Answer:** D — This is a stale-memory problem; memory is meant to be user-controlled (you decide what's remembered or forgotten). Reading and fixing the actual note is the direct fix — a per-prompt patch, permanent incognito use, or a model switch all work around the symptom without addressing the stored, incorrect memory.

---

### Q87.
An associate connected a shared drive to Claude in read-only mode to summarize incoming documents. A new task now requires Claude to also rename and reorganize files in that same drive.
**Options**
- A. This is already covered, since summarizing and reorganizing are both "reading" the drive in a broad sense
- B. This needs a Skill that teaches Claude the reorganization logic; access isn't the concern
- C. Reorganizing/renaming is a write action, and needs to be deliberately granted (upgrading the connector's permission) once confirmed the connector supports it — separate from adding logic via a Skill
- D. This is impossible with any connector and needs a custom integration to be built

**Answer:** C — Renaming/moving files is a write action, structurally different from read-only summarization, and needs its own deliberate permission grant — a Skill can add the logic for *how* to do it, but doesn't substitute for actually having write access.

---

### Q88.
An associate wants Claude to always answer using the same client's brand tone, pull that client's saved reference documents automatically, and never need those documents re-uploaded chat to chat — but only for conversations related to that one client.
**Options**
- A. This is best achieved with a Skill, since Skills define "how" to do something on demand
- B. This is best achieved with account-level instructions, since they apply everywhere
- C. This is best achieved with a Project: scoped, always-on files and instructions for that one client's workspace, distinct from other work
- D. This requires a new connector to be built specifically for that client

**Answer:** C — "Always on, but only for this one workspace" is precisely what a Project is designed for — a Skill is on-demand rather than always-on, account-level instructions would incorrectly apply this client's specific tone/files everywhere, and no connector is needed for content that's simply being stored and reused.

---

### Q89.
A hospital compliance officer wants to pilot a new connector to a patient-scheduling system, which would touch regulated health data, for the very first time.
**Options**
- A. Connect it directly to the live scheduling system and monitor closely for the first week
- B. Build and validate the pilot against synthetic/invented patient-scheduling data first, only moving to the real, approved system once the workflow is proven
- C. Skip the connector and have staff manually paste scheduling data into chat instead, which avoids the connector risk entirely
- D. Connect it, but only enable it for one staff member initially, as a way of limiting exposure

**Answer:** B — For regulated data, the standing practice is validating against synthetic data first, regardless of how limited the initial rollout is — manual paste-in isn't materially safer, and limiting to one user doesn't substitute for testing the workflow itself before real regulated data touches it.

---

### Q90.
A team's Skill (for formatting weekly reports) hasn't been updated even though the report template changed two months ago. Reports keep coming out in the old format.
**Options**
- A. This is a model problem — a more capable model would infer the new template automatically
- B. This is a stale-configuration problem — the Skill's instructions describe an outdated template and need to be manually updated to match the current one
- C. This is a context problem — the chat has simply gotten too long
- D. This is a connector problem — the report source needs to be reconnected

**Answer:** B — A Skill's instructions are static text describing "how" to do something; if the underlying process (the template) changes, the Skill itself must be edited to match — no model upgrade, context management, or connector fix addresses outdated instructions sitting in the Skill itself.

---

## Domain 7 — Troubleshooting and Optimization (10% — Q91–Q100)

### Q91.
A scheduled weekly agent task that compiles a branch stock-level report and writes it to a shared folder produced nothing this Monday.
**Options**
- A. Rewrite the prompt with clearer instructions and run the task again immediately
- B. Recreate the task on a different vendor's platform, since this one has now proven unreliable
- C. Check, in order, whether the run is paused waiting on approval, then usage limits, permissions, connector availability, and the destination folder itself
- D. Reschedule the task for an hour later and see if it runs, before changing anything

**Answer:** C — A silent automation failure has several plumbing-level causes (paused state, limits, permissions, connector status, destination) that should be checked systematically before assuming the prompt is wrong, switching platforms, or just waiting and hoping.

---

### Q92.
An associate complains, "Claude's output has gotten worse lately; it used to be fine." Before suggesting any fix, which three questions should be asked first?
**Options**
- A. "Which model are you on?" / "How much does your plan cost?" / "How long have you used Claude?"
- B. Has the task or prompt itself changed recently? How long has the current conversation run (context overload)? Has any stored instruction or knowledge source gone stale?
- C. "Have you tried turning off extended thinking?" / "Have you tried a different browser?" / "Have you cleared your cache?"
- D. "Do you prefer bullet points or prose?" / "What tone do you want?" / "What's your deadline?"

**Answer:** B — These three questions map directly onto the most common diagnoses (under-specification via a changed task, context overload, and stale configuration) — the diagnostic step comes before any specific fix is proposed, and shouldn't default to unrelated technical or stylistic questions.

---

### Q93.
A team uses the flagship model for every new project "because it worked last time." A weekly report's prompt hasn't changed in two months, but output quality has recently dropped.
**Options**
- A. "Last time it worked" is a habit, not a diagnosis — model tier should be chosen per project's actual complexity/stakes, not by default; and since the report prompt is unchanged, check for stale underlying data/knowledge or a new format/volume requirement, not the prompt wording itself
- B. Switch to an even more capable model, since quality dropped
- C. Rewrite the prompt from scratch, since two months without changes is suspicious
- D. Assume this is normal model drift and nothing can be done

**Answer:** A — Two separate issues are combined here: defaulting to the flagship tier from habit (not task-fit), and diagnosing a quality drop on an *unchanged* prompt, which points toward stale data/config or a shifted requirement — not the wording itself, a bigger model, or shrugging it off as unavoidable drift.

---

### Q94.
An associate says, "I keep typing the same three formatting instructions every single week for this report." What is the correct symptom-to-concept mapping?
**Options**
- A. This means the model needs extended thinking turned on
- B. This is a configuration gap — this recurring instruction belongs in a Skill or a Project's standing instructions, not retyped each time
- C. This means the associate should switch to a different model
- D. This means the report task itself doesn't fit AI assistance

**Answer:** B — "Same instructions, every time" is the textbook signal for moving something into a persistent configuration layer (Skill/Project), not a model or reasoning-depth issue, and certainly not evidence the task is unsuited to AI help.

---

### Q95.
An hour into a long chat, an analyst notices response quality steadily declining, though it was strong at the start.
**Options**
- A. This means the model itself has gotten worse and should be swapped out
- B. This is a likely context-overload symptom; starting a fresh session, summarizing key decisions forward, or persisting stable material into a Project are the relevant fixes — not a model swap
- C. This means the task was never suited to AI assistance
- D. This means a stored instruction has gone stale

**Answer:** B — Quality degrading specifically *within* a single long-running conversation, after starting strong, is the classic context-overload pattern — the fix is managing the conversation/context, not assuming the model itself changed or that the task is unsuited.

---

### Q96.
A team notices its routine, simple internal-memo tasks are now costing noticeably more per use than before.
**Options**
- A. This means the model provider raised prices unfairly
- B. This likely means the wrong (too capable/expensive) model tier is now being used for simple, high-volume work — check tier assignment before assuming a pricing problem
- C. This means the task should be abandoned
- D. This means extended thinking must be turned on for cost efficiency

**Answer:** B — Rising cost on routine, simple tasks maps directly to a tier-mismatch (Domain 3) diagnosis — checking which tier is actually assigned to that workflow comes before assuming external pricing changes or unrelated fixes.

---

### Q97.
A procurement associate has iterated on a supplier-scorecard's weighted-score column four times with increasingly precise wording, but the numbers are still subtly wrong every round. What should the associate check *before* trying a fifth wording refinement?
**Options**
- A. Whether the weighted-score computation should actually be done via code execution rather than as prose text generation
- B. Whether the chat window's color theme is affecting readability of the numbers
- C. Whether a fifth attempt at rewording will finally succeed, given the pattern of the last four
- D. Whether the associate's account has hit its usage limit for the day

**Answer:** A — Four rounds of wording refinement failing to fix consistent arithmetic errors is a strong signal this is a feature mismatch (prose-generated math) rather than a wording problem — checking that before a fifth attempt at more precise language is the efficient diagnostic order.

---

### Q98.
A compliance-report workflow redesigned around Claude reports a 60% time saving in month one. In month two, a regulator queries a specific figure in the submitted report.
**Options**
- A. This means the redesign should be reverted entirely back to the fully manual process
- B. This means the workflow's optimization target should shift toward accuracy/verification for this output, since a flagged compliance figure costs far more than the time saved — the process, not necessarily the tool, needs a stronger verification step
- C. This means the associate running the workflow should be replaced
- D. This means nothing needs to change, since one regulator query is a normal cost of doing business

**Answer:** B — A queried figure in a compliance submission is a signal to strengthen verification around the output that matters most (accuracy), not to abandon the redesign, blame the individual running it, or dismiss the incident as routine.

---

### Q99.
A team lead notices their weekly "ask Claude to fix whatever's wrong with this draft" habit rarely produces a clearly better second draft, regardless of which draft is involved.
**Options**
- A. This means the model is generally unreliable for editing tasks
- B. This is likely under-specification at the iteration step itself — vague feedback ("fix what's wrong") doesn't tell the model which specific things to change; naming the concrete problems (as in a targeted iteration) is the fix
- C. This means extended thinking should be enabled for every editing pass
- D. This means the team should stop using AI for editing entirely

**Answer:** B — This is the same principle as Domain 1's iteration guidance applied at the troubleshooting level: vague, non-specific feedback is itself a form of under-specification, and it's fixable by naming concrete issues rather than concluding the tool or task is fundamentally unsuited.

---

### Q100.
A finance associate uploads a 300-row expense export and asks Claude to summarize spending by category in prose; the totals will directly decide next quarter's budget cuts. Every individual line item Claude quotes checks out correctly against the export.
**Options**
- A. Accept the category totals, since every individual line item cited was correct
- B. Ask Claude to double-check its own arithmetic and confirm the totals
- C. Spot-check ten line items against the export, and accept the totals if all ten match
- D. Have the totals computed via code Claude runs and shows, then verify which rows and categories actually fed each total

**Answer:** D — Correct individual facts don't guarantee correct aggregation; for a budget-deciding total, the computation itself needs to be shown and its inputs verified — not inferred from correct line items, a self-check by the same model, or a partial spot-check of inputs that were already confirmed accurate individually.

---
[⬅ PCAO-F Index](README.md) · [Domain-level teaching walkthrough](../ccao-f/08-teaching-walkthrough.md)
