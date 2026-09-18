# PCAO-F / CCAO-F — 100-Question Max-Hard Scenario Bank (`pcaofexamquizv1.md`)

*The "harder companion set" to [`pcaofexamquiz.md`](pcaofexamquiz.md) — same relationship as
[`../ccao-f/quiz100.md`](../ccao-f/quiz100.md) → [`../ccao-f/hardquiz.md`](../ccao-f/hardquiz.md).
100 **entirely new, original** scenarios (no overlap with `pcaofexamquiz.md`), written one notch
above real-exam difficulty on purpose: longer stems with an embedded red-herring detail, options
that are each individually defensible so the "most appropriate" one has to be argued for, and a
higher share of "Select TWO/THREE — all-or-nothing" items. Domain-weighted identically to the
published blueprint (grounded in [`../ccao-f/01-domain-blueprint.md`](../ccao-f/01-domain-blueprint.md)):*

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

Every option here is written to sound reasonable — read the whole stem twice before choosing. Answer
+ explanation follow each question; cover them for a clean self-test pass.

---

## Domain 2 — Output Evaluation and Validation (21% — Q1–Q21)

### Q1.
A regional bank's fraud team built a Claude-assisted alert-scoring model. Against a batch of 40 historical cases whose true fraud/no-fraud status is already confirmed, the model scores 38 correctly — a 95% match, higher than the analyst's own historical accuracy of 91%. The team lead proposes retiring manual review of new alerts entirely, citing the model's superior measured accuracy.
**Options**
- A. Retire manual review — the model has now been rigorously benchmarked and measurably outperforms the human baseline
- B. Keep a human checkpoint regardless of the favorable benchmark: a known-answer test earns confidence for *similar* future cases, not a permanent transfer of accountability for a consequential, hard-to-reverse action like a fraud freeze
- C. Retire manual review only for the 38 case types the model got right, keeping humans on the other 2 case types
- D. Raise the benchmark threshold to 99% before considering retiring manual review

**Answer:** B — Beating a human accuracy baseline on a known test set is genuine, useful evidence, but it answers a *capability* question, not the separate *accountability* question. A consequential, hard-to-reverse action (freezing an account on a fraud call) still needs a human checkpoint regardless of how favorable the benchmark looks — accuracy numbers, however good, don't transfer responsibility to the tool. (A trap in this question: the 95%-vs-91% comparison is real and relevant to trust in the model's *capability*, but it is being used to justify the wrong conclusion — removing accountability rather than earning it for similar work.)

---

### Q2.
An urban-planning associate asks Claude why a proposed transit line will increase ridership more than a proposed bus-rapid-transit corridor, framed exactly that way, and gets a confident, well-cited case. A colleague, working on the competing option, asks why the bus corridor will increase ridership more than the transit line, and gets an equally confident, well-cited case with different citations. Both cite real-sounding but different studies.
**Options**
- A. This is hallucination: the model invented the studies cited in at least one of the two answers
- B. This is context contamination: the second associate's chat inherited framing from the first
- C. This is sycophancy from leading framing — each question presupposed its own answer, and the model built a persuasive case toward whichever conclusion each question implied; the real test here is whether the *cited studies themselves* check out, independent of which framing produced them
- D. This is normal model variability and no further action is needed

**Answer:** C — The core pattern is leading-question sycophancy, but the harder distinction here is that this doesn't yet prove hallucination (A) — the studies could be real but selectively chosen. The correct next step implied by C is to verify the underlying citations independently, not just diagnose the sycophancy pattern and stop.

---

### Q3.
An asset-management analyst asks Claude to summarize a fund's Q3 performance letter for a client memo. The summary states a "6.2% net return, outperforming the benchmark by 140 basis points," phrased confidently, and separately restates the return once more later in the same summary as "6.2% net return, 110 basis points ahead of benchmark."
**Options**
- A. Use the 6.2% figure, since both restatements agree on the headline return number
- B. Use whichever basis-point figure appears first in the summary, since first mentions are usually most reliable
- C. Treat the internal contradiction (140 bps vs. 110 bps for the same comparison) as a specific hallucination signal and verify both the return and the benchmark spread against the original letter before either figure is used
- D. Average the two basis-point figures (125 bps) as a reasonable compromise

**Answer:** C — Two different figures for the *same underlying comparison*, restated within one document, is a specific and reliable hallucination signal — the fact that the headline return agrees doesn't resolve the contradiction in the derived comparison. Averaging or picking one arbitrarily are exactly the wrong instincts; the source must be checked.

---

### Q4.
A national retailer runs an AI-assisted returns-fraud flagging system across 5,000 weekly returns, auto-approving refunds for the ~4,200 not flagged and routing the ~800 flagged ones to a specialist team. The specialist team, reviewing all 800 flagged cases carefully each week for a month, finds the flagging consistently accurate — false-positive rate under 3%.
**Options**
- A. This four-week track record is sufficient; the flagging logic can now run with lighter specialist review going forward
- B. Also periodically sample the auto-approved population (the much larger, unreviewed ~4,200) to check whether a category of genuinely fraudulent returns is being systematically waved through, since a low false-positive rate on the flagged side says nothing about the false-negative rate on the unflagged side
- C. Increase the flagging threshold so more cases get routed to the specialist team, improving overall safety
- D. Ask the assistant to self-report its estimated false-negative rate and adjust routing based on that figure

**Answer:** B — A well-verified flagged subset can coexist with a badly-performing unflagged majority; the false-positive rate measured on the reviewed side gives no information about the false-negative rate on the unreviewed side. This is the systemic-triage-risk pattern in its harder form: the flagged side looking clean is precisely what makes the unflagged side easy to overlook.

---

### Q5.
A corporate-law associate asks Claude to extract every indemnification obligation from a 90-page acquisition agreement, and the output lists nine obligations, each with a clause citation and a one-line quote. The associate opens three citations at random; all three quotes match the cited clauses exactly.
**Options**
- A. The matching sample of three is sufficient confirmation for a document of this length and stakes
- B. Confirm the remaining six citations as well before relying on the list, since a partial verified sample doesn't rule out fabrication or omission in the unchecked portion of a hard-to-reverse, high-stakes extraction
- C. Ask Claude whether the list of nine is complete, and accept its answer if confident
- D. Re-run the extraction once more and accept the list only if the second run also produces nine obligations

**Answer:** B — Three correct citations build confidence in *those three*, not in the remaining six or in the completeness of the list overall (a tenth, unlisted obligation is exactly the kind of omission that spot-checking existing entries cannot catch). For a high-stakes legal extraction, full verification — not partial sampling or self-report — is warranted.

---

### Q6.
A manufacturing quality team has Claude draft a root-cause analysis for a defect batch, then, in the same conversation, asks Claude to "review this analysis as a skeptical outside auditor would." Claude's "auditor" pass raises two additional concerns and revises its confidence downward.
**Options**
- A. This satisfies independent verification, since Claude explicitly adopted an adversarial, skeptical persona
- B. This still shares the same underlying model and conversational context as the original analysis — a persona instruction changes the *framing* of the self-check, not its independence; a genuinely separate path (a different model, a human quality engineer, or the actual defect data) is still needed for a batch-quality decision
- C. This satisfies independent verification only if the persona pass happens in a new chat
- D. This is unnecessary, since the auditor persona already found two concerns, proving the check worked

**Answer:** B — An adversarial persona prompt improves the *thoroughness* of a self-review but does not create genuine independence — same model, same blind spots, same training data. It can surface some issues (as it did here) while still missing others systematically shared with the original pass.

---

### Q7.
A construction-supplies distributor's finance team receives a Claude-built margin-analysis spreadsheet built from raw invoice exports. Every product line shows a margin percentage; the formulas are visible in the cells and check out correctly for the ten rows the associate spot-checked. The spreadsheet will set which product lines get discontinued.
**Options**
- A. Since the visible formulas check out for the sampled rows and the computation was done via code/formulas rather than prose, no further check is needed before the discontinuation decision
- B. Even with correct, visible formulas, confirm which specific source rows and invoice ranges fed the *unsampled* product lines' totals, since a wrong reference range (not a wrong formula) is a distinct failure mode that spot-checking formulas alone won't catch
- C. Ask Claude to re-verify its own formulas and confirm no line was missed
- D. Recompute all totals manually as a full duplicate check, since a business-critical decision warrants full manual redundancy regardless of how the first pass was built

**Answer:** B — This is a harder, more specific version of the "verify computation" principle: the formulas themselves being correct doesn't guarantee they were applied to the *correct source range* for every line — a wrong reference is a separate error mode from a wrong formula, and spot-checking the formula doesn't catch a wrong range on an unsampled row. D over-corrects into unnecessary full duplication once code/formulas are already being checked appropriately.

---

### Q8.
An executive search firm asks Claude and a second AI tool to independently score the same six finalist candidates for a CFO role against an identical rubric. The two tools agree closely on five candidates and diverge sharply on the sixth — one rates the candidate as the strongest overall, the other as the weakest.
**Options**
- A. Since five of six agree, treat the sixth divergence as noise and default to whichever tool has generally been more reliable historically
- B. Treat the disagreement on the sixth candidate as the specific, actionable signal — it identifies exactly which candidate needs deeper human evaluation, while the five-candidate agreement is a separate, reassuring but non-decisive signal about general alignment
- C. Remove the sixth candidate from consideration entirely, since AI disagreement suggests unresolvable uncertainty
- D. Ask both tools to re-score the sixth candidate together in one shared conversation until they converge

**Answer:** B — The harder distinction here: agreement on most candidates doesn't validate the disagreement away, and it especially doesn't justify defaulting to "the historically more reliable tool" for the one case where they disagree — that's exactly the case needing independent human judgment, not a tie-break by track record.

---

### Q9.
A city government's records office asks Claude to confirm the current statutory retention period for a specific category of tax records. Claude cites "Revenue Code §14.3(b)" and states a seven-year period, matching what the associate already believed to be true from memory.
**Options**
- A. Since the cited figure matches the associate's own prior understanding, this corroboration is sufficient confirmation
- B. Confirm the citation against the actual current statute text regardless of whether it matches prior belief — a citation that happens to confirm what you already expected is exactly the case where under-checking is most tempting and most risky, since confirmation bias adds no real independent evidence
- C. Ask a colleague whether seven years "sounds right" as an additional check
- D. Accept the figure, since statutory retention periods rarely change

**Answer:** B — Matching prior belief feels like corroboration but is not independent evidence — it's actually a moment of elevated risk, because the natural inclination to skip verification is strongest exactly when a claim confirms what's already assumed. The citation still needs to be checked against the actual current source.

---

### Q10.
A wholesale distributor's operations team has Claude reconcile 18 months of warehouse-scan data against supplier invoices in a single request, producing a discrepancy report. Weeks later, an auditor finds that a systematic unit-conversion error (cases vs. individual units) in one supplier's data caused every discrepancy involving that supplier to be miscalculated, and the error passed cleanly through the report's totals and flagged-exceptions list alike.
**Options**
- A. The fix is simply to add "double-check unit conversions" to the same single-pass prompt for future runs
- B. The fix is to decompose the process — first profile each supplier's data format and confirm units explicitly, verify that normalization step independently, and only then run the reconciliation and exception-flagging on top of confirmed-consistent units
- C. The fix is to re-run the same single-pass request on a more capable model, since a stronger model would catch a unit mismatch
- D. The fix is to have Claude flag any numbers that "look unusual" as a final review step

**Answer:** B — The systemic error occurred at an early, unverified step (unit normalization) and then propagated invisibly through everything built on top of it. Verifying that specific intermediate step before building the exception report on top of it is what prevents this — added carefulness wording, a bigger model, or a vague "flag anything unusual" instruction don't address the structural gap.

---

### Q11.
An environmental consultancy has Claude summarize a 250-page site-remediation report for a client briefing. The summary is fluent, well-structured, cites specific page numbers for each claim, and every citation the associate spot-checks (4 of 15 claims) matches the source page correctly.
**Options**
- A. This sampling result is sufficient given the citation-matching discipline shown
- B. Have someone with environmental-remediation expertise assess whether the summary's *characterization* of the findings (not just the citation accuracy) is credible by the field's own standards — a fluent, accurately-cited summary can still subtly mischaracterize technical severity or omit context in ways only a subject-matter expert would catch
- C. Spot-check the remaining 11 claims as well, which fully resolves the concern
- D. Ask Claude to rate its own summary's technical accuracy on a 1–10 scale and treat a high score as sufficient

**Answer:** B — This is the harder version of the "fluency isn't accuracy" principle: even with citations that check out (ruling out simple hallucination), a technically fluent summary can still misrepresent severity, risk, or context in ways that only a domain expert — not more citation-checking, and not a self-rating — would catch.

---

### Q12.
A national grocery chain's category team has Claude and a competing AI tool each independently forecast next quarter's demand for a seasonal product line, using identical historical data. Both forecasts land within 2% of each other.
**Options**
- A. Close agreement between two independent tools is strong evidence the forecast is directionally sound, and is meaningfully stronger evidence than either tool's self-reported confidence would be — though it is still not a substitute for validating against an actual known-outcome period before high-stakes inventory commitments are made
- B. Close agreement between two AI tools using the same input data is not meaningfully different from one tool's self-reported confidence, since both tools may share the same blind spot in the historical data itself
- C. Close agreement is only meaningful if the two tools are from genuinely unrelated vendors, which cannot be confirmed
- D. Close agreement should be treated as full proof, since two independently-built systems converging on the same figure is definitionally reliable

**Answer:** A — The harder distinction: cross-model agreement using the *same input data* is weaker evidence than cross-model agreement built from independently gathered evidence (since both models could share a blind spot baked into that shared data) — but it is still meaningfully stronger than a single model's self-report, because two independent reasoning processes converging on the same output is not nothing. It remains a progress signal, not proof, ahead of a real financial commitment.

---

### Q13.
An ad agency's media-buying associate frames a request as: "This campaign's underperformance is clearly due to a weak creative — confirm that for the client report." Claude returns a confident analysis attributing underperformance to creative weakness, citing engagement metrics.
**Options**
- A. This is an acceptable evaluative process since real engagement metrics were cited in support
- B. The framing presupposes the conclusion (leading question), and even though real metrics were cited, they may have been selectively chosen to support the presupposed cause; a better prompt asks for the strongest evidence *for and against several possible causes* (creative, targeting, timing, budget) without presupposing which one is correct
- C. This is acceptable as long as the associate independently verifies the specific engagement numbers cited
- D. This is acceptable because engagement metrics are objective and cannot be selectively framed

**Answer:** B — This is a harder version of the leading-question trap: real, verifiable metrics were cited, which makes the sycophancy less obvious than a purely fabricated claim, but the fundamental issue remains — the question told the model which conclusion to build a case for, and metrics can be true while still being cherry-picked to fit a presupposed answer.

---

### Q14.
A telehealth platform runs a Claude-assisted symptom-triage layer that has correctly matched licensed-nurse triage decisions in 970 of 1,000 audited historical cases (97%). Leadership proposes removing the nurse-review step for the lowest-acuity triage category specifically, which accounts for 60% of volume and had zero mismatches in the audit.
**Options**
- A. Approve the removal — zero mismatches in that specific high-volume category, within an already-strong overall audit, is sufficient justification
- B. Do not remove the nurse-review checkpoint for any live patient-facing triage category based on a retrospective audit alone, regardless of how clean that category's historical numbers look — patient-safety decisions retain a human checkpoint independent of measured accuracy, and a category with zero mismatches in one audit sample is not the same as zero risk going forward
- C. Approve the removal only after the audit sample size doubles
- D. Approve a partial removal — a licensed nurse spot-checks 10% of the low-acuity category going forward instead of reviewing all of it

**Answer:** B — This intentionally offers a very tempting "clean subgroup" (60% volume, zero mismatches) to test whether the test-taker still applies the underlying principle: patient-safety accountability doesn't transfer based on a favorable retrospective slice, no matter how clean that slice looks, and no matter how large the volume behind it is.

---

### Q15.
A commercial insurer's underwriting team has Claude flag policy applications for manual underwriter review based on risk indicators. Of 3,000 applications, 340 are flagged; the underwriting team reviews all 340 and finds the flagging judgment sound in every case. Separately, the team notices flagged applications disproportionately come from two specific ZIP codes relative to their share of total applicants.
**Options**
- A. Since every flagged case held up under review, the ZIP-code pattern is incidental and needs no further attention
- B. Escalate the ZIP-code concentration pattern to the policy/compliance owner for a fairness review, even though every individual flagged case was substantively correct — a flagging system can be accurate case-by-case while still producing a disparate-impact pattern worth a fairness check, and this determination is not the reviewing associate's to make alone
- C. Quietly adjust the flagging criteria to reduce the ZIP-code concentration before anyone else notices
- D. Ask Claude whether its own flagging criteria are biased by ZIP code and rely on its answer

**Answer:** B — Individual-case accuracy and aggregate fairness are separate questions; a flagging system can get every single case "right" on its own terms while still producing a concentration pattern that deserves review by whoever owns fairness/compliance obligations — not a unilateral quiet fix, not a dismissal because case-level review passed, and not the model's own self-assessment.

---

### Q16.
A private equity associate has Claude build a comparable-companies valuation table from ten public filings. Every individual multiple (P/E, EV/EBITDA) that the associate spot-checks against the filings is correct. The table's *median* EV/EBITDA multiple, which will anchor a client-facing valuation range, is computed by Claude in the same response as prose ("the median across the ten comparables is 8.4x").
**Options**
- A. Accept the 8.4x median since the underlying individual multiples were confirmed correct
- B. Have the median (and any other aggregate statistic feeding the valuation range) computed via executable calculation shown against the ten confirmed multiples, rather than accepted as a prose-stated aggregate — correct inputs do not guarantee a correct aggregation step
- C. Ask Claude to recompute the median and confirm it matches
- D. Spot-check two more individual multiples for extra assurance before accepting the median

**Answer:** B — This is the aggregation-error pattern at its most consequential: confirmed-correct individual inputs still don't guarantee a correctly computed aggregate (a median is easy to miscompute silently, e.g., averaging instead of taking the true middle value with an even count) — the aggregation step itself needs to be shown and verified, not inferred from correct inputs.

---

### Q17.
A media company's ad-sales associate needs Claude to help decide whether an underperforming campaign should continue. Which single request best supports an honest evaluation rather than a persuasive case for a predetermined conclusion?
**Options**
- A. "Give me the strongest argument that this campaign should continue as-is."
- B. "Rate this campaign's performance from 1–10 and explain the score."
- C. "Lay out the strongest case for continuing the campaign unchanged and the strongest case for pausing it, based only on the attached performance data, before any recommendation."
- D. "This campaign seems to be struggling — walk me through why."

**Answer:** C — Asking for both sides explicitly, grounded in the data, before any recommendation is what avoids presupposing an answer. A asks for one-sided advocacy; D's framing ("seems to be struggling") leads toward a negative conclusion; B invites a plausible-sounding score without necessarily surfacing the actual tradeoffs on both sides.

---

### Q18. *(Select TWO — all-or-nothing)*
A biotech company's regulatory-affairs associate is deciding which of five upcoming Claude-assisted tasks need a second, independent verification path beyond the associate's own read-through. Which **TWO** most clearly require it?
**Options**
- A. Drafting talking points for an internal town hall about a recent product launch
- B. Extracting adverse-event thresholds from a clinical protocol that will determine a trial's stopping rules
- C. Summarizing a competitor's public press release for an internal slide
- D. Calculating a dosage-conversion table that will be used directly in a patient-facing dosing chart
- E. Drafting a thank-you note template for conference attendees

**Answer:** B, D — Both feed directly into consequential, hard-to-reverse, safety/regulatory-relevant outcomes (trial stopping rules; patient dosing) where an error compounds badly and a second independent check is warranted. A, C, and E are low-stakes, easily-correctable internal or informational content.

---

### Q19.
A national law firm's e-discovery team has Claude review 40,000 documents and tag 1,100 as "privileged — withhold." Outside counsel reviews a random sample of 150 of the 1,100 tagged documents and confirms all 150 were correctly tagged privileged.
**Options**
- A. This sample confirms the tagging system overall; proceed to withhold all 1,100 without further review
- B. This sample only confirms precision on the *withheld* side; it says nothing about documents that should have been tagged privileged but weren't — sample the untagged 38,900 as well (or a defensible portion of them) before certifying the production is complete and privilege-safe
- C. Increase the sample size on the withheld side to 300 for extra confidence, which resolves the concern
- D. Ask Claude to re-scan the untagged documents and self-report its confidence that none were missed

**Answer:** B — This is the systemic-triage-risk pattern applied to its highest-stakes form (privilege waiver risk in litigation): validating the flagged/withheld side, however thoroughly, says nothing about false negatives in the much larger unflagged side, which is exactly where an inadvertent privilege waiver would hide.

---

### Q20.
A regional airline's revenue-management team asks Claude to explain a fare-optimization recommendation. Claude's explanation is detailed, well-structured, and internally consistent, describing a chain of reasoning about competitor pricing and demand elasticity. The recommended fare change, if wrong, would be reversible within 24 hours by resetting fares.
**Options**
- A. Because the reasoning is detailed and internally consistent, and the action is reversible within 24 hours, it is reasonable to implement the fare change now while monitoring actual bookings as the real-world check — this is a case where the low cost of being wrong changes how much verification is warranted before acting
- B. Detailed, consistent-sounding reasoning must always be independently verified against real elasticity data before any action, regardless of reversibility
- C. The explanation's internal consistency is itself sufficient verification, regardless of reversibility
- D. No fare change should ever be made without first replicating the analysis on a second AI model, regardless of reversibility

**Answer:** A — This question tests whether the test-taker over-applies verification rigor uniformly regardless of stakes/reversibility: for a low-cost-of-error, quickly-reversible action, real-world monitoring *is* a legitimate, proportionate verification path — the earlier, harder questions in this set involve irreversible or high-stakes actions specifically because that's where heavier verification is warranted, not as a universal rule for every AI-assisted decision.

---

### Q21.
A hospital's clinical-informatics team wants to validate a new Claude-assisted chart-summarization tool before wider rollout. Which validation approach most rigorously tests whether the tool can be trusted, as opposed to merely appearing trustworthy?
**Options**
- A. Have ten clinicians read a week's worth of new summaries and rate them "looks accurate" or "looks off"
- B. Run the tool on a set of past patient charts whose correct, physician-verified summary is already known and withheld from the tool, and compare the tool's output against that established ground truth
- C. Ask the tool to explain its own summarization methodology and have an informaticist judge whether the explanation sounds sound
- D. Run the tool twice on the same new chart and check whether the two outputs are consistent with each other

**Answer:** B — This is the known-answer test at its clearest: comparing against an already-established, verified ground truth is fundamentally different from (and stronger than) a plausibility rating (A), a self-explained methodology (C), or self-consistency across repeated runs (D), any of which could be consistently wrong or consistently plausible-sounding without being correct.

---

## Domain 4 — Workflow Integration and Solution Design (16% — Q22–Q37)

### Q22.
A multinational manufacturer's plant-operations director says: "We want Claude handling our safety-incident intake so reports get filed faster." The director adds that "faster" is the main goal, since delayed filing has been the recurring complaint.
**Options**
- A. Since the goal (speed) is already stated, proceed directly to building a faster intake process around that stated goal
- B. Before building anything, still settle the other four task-definition elements even though the goal is stated: exactly what should be produced, for whom, from what data/inputs, and in what format — a stated goal alone doesn't resolve what "faster filing" should actually output, to whom, or from which source records
- C. Ask the director to pick the AI tooling first, since the goal is already clear
- D. Proceed directly, treating "reduce filing delay" as sufficient specification for a safety-critical workflow

**Answer:** B — This is a harder version of the task-definition trap: a stated *goal* (speed) is not the same as a full task definition. Four of the five settled-answers slots are still open, and for a safety-critical intake process, resolving them before building matters more than the presence of a clear-sounding goal.

---

### Q23.
A pharmaceutical distributor's cold-chain compliance workflow has Claude flag shipment temperature-log anomalies for a compliance officer, who then decides whether to quarantine the batch. A proposal suggests removing the compliance officer's decision step for anomalies below a certain severity threshold, "since Claude's severity scoring, based on code-executed threshold comparisons, is mathematically precise and has never been wrong in six months."
**Options**
- A. Approve the removal below the threshold, since the severity math is both code-executed (removing computation risk) and has a clean six-month track record
- B. Keep the compliance officer's decision step even below the severity threshold: quarantine/non-quarantine is a consequential, not-easily-reversible decision (product may already be distributed before a missed anomaly surfaces), and accountability for that call does not transfer to a scoring formula regardless of its computational accuracy or track record
- C. Remove the step only for the lowest 25% of severity scores, as a middle-ground compromise
- D. Keep the step, but let it be satisfied by an automatically generated confirmation email rather than an actual review

**Answer:** B — This question specifically combines two tempting-but-insufficient justifications (code-executed precision AND a clean track record) to see whether the test-taker still separates the *computation-accuracy* question from the *accountability/reversibility* question — both being favorable doesn't change who is accountable for a quarantine decision.

---

### Q24.
A logistics company's proposal for an AI-assisted freight-routing tool states: "Routes will be optimized by the assistant, and a dispatcher reviews any route through a designated high-risk corridor before departure." A colleague argues this wording is already a complete, well-defined control.
**Options**
- A. The wording is complete: it names the trigger condition (high-risk corridor) and implies a reviewer (dispatcher)
- B. The wording is incomplete in one specific way even though it looks well-defined at first glance: it doesn't state *what* the dispatcher is checking for (WHAT) or confirm the review happens *before* departure is finalized rather than logged after the fact (WHEN is implied but not explicit) — naming a trigger and a role is necessary but not sufficient for a defined gate
- C. The wording is incomplete because it doesn't name a specific dispatcher by name
- D. The wording is complete and additionally should specify which AI model performs the routing

**Answer:** B — This is a harder application of the WHO/WHAT/WHEN gate test: the wording here already does more than the classic vague "a person will review" example (it names a trigger and a role), which makes it tempting to call complete — but it still hasn't specified the *specific risk* being checked for, which is what a truly audit-proof gate requires.

---

### Q25.
A five-branch credit union is redesigning its loan-document intake around Claude. Two changes are planned: consolidating four separate document-request emails into one, and moving repeated compliance-language requirements into a Project's standing instructions. Leadership wants a "processing time reduced by X%" figure for the board within two weeks, and the team is tempted to estimate the improvement now to hit that deadline.
**Options**
- A. Provide a reasoned estimate now to meet the board deadline, and correct it later once real data comes in
- B. Run the current, unchanged process for a short measurement window first to establish a real baseline (time, revision rounds, manual steps), even if that means the board figure arrives after the two-week request, rather than reporting an estimated number as if it were measured
- C. Make the two planned changes immediately, then measure only the new process, comparing it against last year's informal recollection of typical processing time
- D. Report the combined, undifferentiated impact of both changes together as a single figure, without needing a pre-change baseline, since board members care about the end result

**Answer:** B — This raises the stakes on the baseline-before-optimizing principle by adding real organizational pressure (a board deadline) as a reason to skip it — the correct answer holds that measuring first is still right even when it conflicts with a deadline, rather than substituting an estimate or an undocumented "last year, roughly" comparison.

---

### Q26.
A national insurer connected its claims-document folder to Claude in read-only mode to summarize incoming claims. A new initiative wants Claude to also tag each claim folder with a standardized status label (e.g., "pending," "closed") directly in the folder system, visible to all claims staff.
**Options**
- A. This is achievable today since read access lets Claude see and reason about folder structure and status
- B. Applying a visible status tag to files/folders is a write action; it must be deliberately granted (confirming the connector even supports this kind of write capability) separately from the existing read-only summarization access, regardless of how simple "just adding a label" sounds
- C. This should be solved by building a Skill that defines the tagging logic, since read access plus clear logic is sufficient
- D. This requires no connector change, since folder tags are metadata rather than file content

**Answer:** B — This question specifically tests whether "just a label/tag" (which sounds lighter than moving or deleting files) is still correctly recognized as a write action requiring deliberate, confirmed permission — the answer is yes, regardless of how minor the specific write operation seems.

---

### Q27.
A hospital system's discharge-summary workflow has five steps. Step 3 (drafting the summary) and Step 4 (a physician co-signing it) are both currently classified as "collaborative." A quality-improvement lead proposes reclassifying Step 3 alone as "AI-appropriate" (no collaborative flag) since Step 4's physician co-sign already exists as a downstream safeguard.
**Options**
- A. Approve the reclassification — Step 4's existing safeguard makes Step 3's own collaborative flag redundant
- B. Do not approve: Step 3's classification should be based on its own reversibility/stakes/accountability profile, not on whether a downstream step also exists — collapsing an upstream collaborative step because a later gate exists risks weakening the overall workflow if the downstream gate is ever removed, changed, or under time pressure, later, for reasons unrelated to Step 3
- C. Approve the reclassification only if Step 4's co-sign becomes mandatory rather than optional
- D. Approve the reclassification, but only for low-complexity discharge cases

**Answer:** B — This tests a subtler version of the delegation-map principle: each step's classification should stand on its own reversibility/stakes/accountability analysis; using a *different* step's safeguard to justify loosening this step's classification creates a fragile dependency where a later change to Step 4 silently removes the only remaining check on Step 3.

---

### Q28.
An investment bank's associate describes an AI-assisted trade-reconciliation workflow in three versions. The version for the trading desk head says: "Claude flags mismatched trades daily; a reconciliation analyst confirms and resolves each flag before end-of-day close." The version for the audit committee omits the phrase "before end-of-day close" but otherwise matches.
**Options**
- A. This omission is acceptable, since the audit committee version still mentions the analyst confirming and resolving each flag
- B. This omission removes exactly the detail (WHEN — before an irreversible cutoff) that an audit-facing description most needs, since audit interest centers on whether the control operates before risk crystallizes, not just on whether a human is generally involved
- C. This omission is acceptable because audit committees focus on outcomes, not process timing
- D. This omission is only a problem if the actual process timing ever changes

**Answer:** B — This is a harder version of "don't drop the human checkpoint" — here the human role (analyst) is still mentioned; what's silently dropped is the *timing* element (before close) that turns "a human checks it" into an actual pre-crystallization control, which matters most to exactly the audience (audit) being shown this version.

---

### Q29. *(Select TWO — all-or-nothing)*
A regional airline is expanding an AI-assisted crew-scheduling exception workflow. Which **TWO** of the following five proposed changes would leave the system with more authority than its risk profile allows?
**Options**
- A. Let Claude auto-approve crew rest-period exceptions below a regulatory minimum threshold when historical approval rates for similar requests exceed 98%, without human sign-off
- B. Let Claude draft the rationale for each rest-period exception request, with a named crew-scheduling manager required to approve or reject before it takes effect
- C. Have a scheduling coordinator approve a batch of 40 daily exception requests by glancing only at Claude's one-line summary for each, without opening any individual case, to meet a same-day cutoff
- D. Use Claude to compute optimal crew rotations via code execution, with the existing scheduling-manager approval gate unchanged and immediately following
- E. Move the rest-period regulatory-threshold lookup into a Skill so it's applied consistently across all schedulers

**Answer:** A, C — A directly automates a regulatory, safety-relevant exception based on a historical approval rate rather than an actual case-by-case decision (the approval rate does not make an individual exception automatically safe). C keeps a human "in the loop" in name only — approving 40 cases from one-line summaries without opening any case file is a rubber stamp, not a real review. B, D, and E all preserve substantive human decision-making at the point that matters.

---

### Q30.
A city's public-works department drafts a single internal memo explaining why a road-resurfacing project ran over budget. The memo needs to reach the city council (who approve the next budget cycle) and the resurfacing crew (whose work-order process is changing as a result).
**Options**
- A. Produce one rewrite per audience, each organized around what that specific audience needs to decide or do next, rather than adapting tone alone on a single shared draft
- B. Keep one memo but add a short "for council" and "for crew" heading to each relevant section within it
- C. Send the identical memo to both audiences, since the underlying facts (why it ran over budget) don't change between audiences
- D. Ask Claude to produce a "balanced, general-audience" version suitable for both, to save review time

**Answer:** A — Even though B looks like a reasonable middle ground (headers separating audience-relevant sections within one document), it still doesn't restructure the content around what each specific audience needs to *decide or do* — a council needs budget-cycle-relevant framing to approve funding; a crew needs operational, work-order-relevant framing to change practice. A genuinely separate rewrite per audience, not a labeled single document, is what the harder version of this principle requires.

---

### Q31.
A specialty pharmacy chain has Claude extract every controlled-substance handling requirement from a new state regulation and an internal compliance memo. The output is a clean list of 24 requirements. Before pharmacists begin retraining based on this list, which single next request best protects against a missed obligation?
**Options**
- A. Ask for the list reorganized by urgency, so the pharmacy team tackles the most time-sensitive requirements first
- B. For each of the 24 requirements, add its exact source (regulation section or memo line), whether the two sources agree or conflict on it, and whether it is ambiguous enough to warrant a compliance-officer question — surfacing hidden conflicts between the two source documents, not just tracing to one source
- C. Ask Claude to cross-check the 24 requirements against a general industry best-practices summary for completeness
- D. Have Claude summarize the state regulation and the internal memo separately, and manually compare the two summaries side by side

**Answer:** B — This is a harder version of the traceability principle: with *two* source documents involved, the highest-value addition is surfacing whether they actually agree with each other on each requirement (not just tracing each item to *a* source), since a silent conflict between the regulation and the internal memo is exactly the kind of gap reorganizing by urgency (A) or a general industry comparison (C) would not surface.

---

### Q32.
A national moving company's operations associate delegates: build a truck-loading sequence plan for a specific multi-stop route, given stated stop order, weight limits per stop, and a stated instruction that Claude may reorder stops for efficiency but must flag any such reordering. In the output, Claude reorders two stops for efficiency and clearly flags the change — but also silently substitutes a different, unstated weight-distribution method than the company's standard practice, without flagging that substitution.
**Options**
- A. The original instruction was sufficient, since the reordering (the anticipated type of discretion) was correctly flagged
- B. The instruction correctly anticipated *one* category of discretion (stop reordering) but didn't cover a second, unanticipated one (choice of weight-distribution method); the fix is to broaden the "flag when you decide" instruction to cover *any* meaningful methodological choice, not just the one type of discretion originally named
- C. This is a hallucination, since the weight-distribution method wasn't in the source data
- D. This is a context-overload issue, since the request had multiple constraints

**Answer:** B — This is a harder version of the "say when you decide" principle: the instruction worked exactly as designed for the anticipated discretion (reordering) but didn't generalize to an unanticipated category of silent choice (methodology substitution) — the fix broadens the flagging instruction's scope rather than concluding the original instruction failed outright.

---

### Q33.
A university's research-data office has consent-based access to sensitive survey data collected for a specific longitudinal health study. A separate research team, studying an unrelated topic, requests that the same dataset (already sitting in an approved Claude workspace for the original study team) be analyzed for their unrelated project, arguing "it's already inside the approved system, so no new access step is needed."
**Options**
- A. Approve the request, since the data is already inside an approved, secured workspace regardless of which team or project uses it
- B. Take this to the data/consent owner: data collected under consent for one specific study cannot be repurposed for an unrelated project just because it happens to sit in an already-approved technical environment — approved *storage* location and approved *use* are separate questions
- C. Approve the request, but only if the second team anonymizes all identifiers first
- D. Approve the request only if the second team's project is also health-related

**Answer:** B — Being inside an approved workspace addresses data security, not purpose limitation; consent for a specific study's use does not automatically extend to a different project, however secure the storage, however anonymized the eventual output, or however topically adjacent the new project seems.

---

### Q34.
An AI-assisted vendor-risk scoring tool at a manufacturing conglomerate appears to consistently score vendors headquartered in one particular country higher-risk than vendors with comparable financials headquartered elsewhere. The procurement associate who noticed this does not own vendor-risk policy, but does own the day-to-day scoring workflow.
**Options**
- A. Since the associate owns the workflow, quietly adjust the scoring inputs to remove the apparent geographic skew before anyone else notices
- B. Work through who is affected (which vendors, and how) and what could go wrong (unfair competitive disadvantage, potential trade/discrimination exposure) and escalate the pattern with that reasoning to whoever owns vendor-risk policy — owning the workflow's operation is not the same as owning the authority to redefine its risk criteria
- C. Since it's outside the associate's ownership entirely, take no action and let the pattern continue until someone else notices
- D. Ask the tool directly whether its scoring is geographically biased, and act only if it confirms bias

**Answer:** B — Owning the day-to-day operation of a workflow is distinct from owning the authority to change its underlying risk criteria — a harder distinction than the more general "escalate fairness concerns" pattern, since it specifically separates *operational* ownership from *policy* ownership, and the associate has the former but not the latter.

---

### Q35.
A regional hospital network wants to establish whether a new Claude-assisted nurse-staffing recommendation tool can be trusted before wider rollout across its 12 facilities. The tool has performed well in a 3-week pilot at the single facility that helped design it.
**Options**
- A. This pilot result establishes sufficient trust for network-wide rollout, since it was a real, multi-week test with real staffing decisions
- B. Test the tool against known-answer staffing decisions from at least one or two *other* facilities in the network — not just the facility that helped design the tool — before treating the pilot's success as evidence the tool generalizes; a pilot at the design facility may reflect a good fit to that facility's specific patterns rather than genuine tool reliability network-wide
- C. Roll out network-wide immediately, monitoring closely for the first month as the real-world check
- D. Extend the pilot at the same single facility for another 3 weeks before deciding

**Answer:** B — This is a harder version of the known-answer test: a favorable pilot at the facility that helped *design* the tool doesn't establish that the tool generalizes to other facilities with different patient populations, staffing patterns, or shift structures — the correct next validation step tests against a *different* known-answer context, not just a longer test in the same one.

---

### Q36.
A specialty foods distributor redesigns its supplier-onboarding workflow around Claude. Six months in, an audit finds the redesigned process is measurably faster (a 45% reduction in onboarding time) but that two suppliers were onboarded despite missing a required food-safety certification, which the workflow's document-checklist step should have caught.
**Options**
- A. Since the overall time-reduction goal was met, treat the two missed certifications as isolated errors to be corrected individually, with no workflow change needed
- B. Re-examine the specific checklist-verification step for a structural gap (was it verifying document *presence* without verifying document *validity/currency*, for example) rather than treating two missed certifications as unrelated one-off mistakes, since a food-safety compliance miss is exactly the kind of error the workflow's redesign should have been optimized to prevent, not just sped up around
- C. Revert the entire redesigned workflow back to the original manual process, since any compliance miss invalidates the redesign
- D. Add a note to the two affected supplier files acknowledging the gap, and continue monitoring without further workflow changes

**Answer:** B — When speed was gained but a compliance-critical check specifically failed, the right move is investigating whether that specific step has a structural gap (not whether the redesign overall succeeded) — the earlier baseline-first principle established that outcomes should be measured before optimizing; this question extends it: when a *specific* compliance-relevant metric fails despite overall success, that specific step needs re-examination, not a blanket revert or two isolated corrections.

---

### Q37.
A logistics-software company writes three descriptions of an AI-assisted invoice-matching workflow — for the engineering team, for the CFO, and for a prospective enterprise client's procurement team. The client-facing version states: "Our AI-assisted system reconciles 95% of invoices automatically, with the remainder routed to a trained specialist for review before payment release."
**Options**
- A. This version is appropriately pitched for a prospective client and correctly preserves the human checkpoint
- B. This version, while naming a human checkpoint, states the 95% figure without qualifying what "automatically" means for that 95% — specifically whether a lighter form of verification (e.g., automated matching-confidence checks) still applies before payment release even for the "automatic" cases, since a prospective client may reasonably read "automatically" as "no verification at all" for 95% of their invoice volume
- C. This version is fine, since specialist review of the remainder is the only checkpoint that legally needs disclosing
- D. This version should be simplified further for a sales audience by removing the 95%/remainder breakdown entirely

**Answer:** B — This is a harder version of "don't let the audience believe there's no gate": the human checkpoint is disclosed, but the boundary of what counts as "automatic" (does the 95% get *any* verification, or none) is left genuinely ambiguous in a way a client evaluating risk would reasonably want clarified — technically true statements can still create a misleading impression through what they leave undefined.

---

## Domain 6 — Governance, Risk, and Responsible Use (15% — Q38–Q52)

### Q38.
A multinational retailer's e-commerce team wants Claude to auto-generate personalized discount offers based on a customer's purchase history and a predicted "price sensitivity" score. The predicted score uses a customer's shipping ZIP code as one of several inputs, alongside purchase frequency and average order value.
**Options**
- A. This is fully appropriate with no review needed, since discount personalization is a routine marketing function
- B. This is appropriate-with-review specifically because ZIP code, a proxy correlated with protected characteristics like income and race in many markets, is one of the scoring inputs — the review should include whether the ZIP-code input introduces a disparate-impact risk in who receives better or worse offers, not just whether the offers are commercially effective
- C. This is inappropriate for any AI involvement, since any use of geographic data in pricing is impermissible
- D. This is appropriate-with-review, but only because of the purchase-history component, not the ZIP code

**Answer:** B — The harder distinction: ZIP code is a commonly-used, seemingly neutral input that carries real proxy-discrimination risk in pricing/offer contexts — the review needs to specifically examine *that* input's disparate-impact potential, not treat the workflow as routine (A), ban geography outright (C, an overcorrection), or focus review only on the more obviously "personal" input while ignoring the riskier one (D).

---

### Q39.
A national law firm's associate can't determine from firm policy whether client conflict-check summaries generated with AI assistance need to be logged as "AI-assisted" in the firm's conflicts database, given that the firm recently onboarded a new practice group with different internal conventions. The associate escalates to the firm's general counsel.
**Options**
- A. "I've reviewed the situation and my recommendation is to log all future conflict summaries as AI-assisted going forward — please approve."
- B. The specific process (conflict-check summaries), the specific ambiguity (whether the new practice group's conventions require this logging, which existing policy doesn't clearly address), and the one open question policy leaves unresolved — without a baked-in recommendation, since the associate does not have the authority or full context to make this determination
- C. A description of the general benefits of AI transparency in legal practice, with a request for general guidance
- D. A request to pause using AI assistance for conflict checks in the new practice group until the question is resolved, without further detail

**Answer:** B — This is a harder version of the escalation-quality principle: A looks helpful (a specific recommendation) but oversteps — the associate doesn't have the standing or full context to decide firm-wide logging policy, and a baked-in recommendation can anchor the general counsel's decision inappropriately. The correct escalation gives facts and the specific open question, without pre-deciding it.

---

### Q40.
A boutique wealth-management firm's compliance officer reviews a proposal to let Claude draft — but never send without human approval — personalized client-portfolio commentary that references specific holdings performance. After 18 months of clean operation with 100% human sign-off maintained throughout, a partner proposes: "Given the perfect track record, let's remove the requirement that the compliance officer specifically checks for any forward-looking performance language, since the reviewing advisor already reads the whole thing anyway."
**Options**
- A. Approve the change — an 18-month clean record plus an existing general reviewer (the advisor) makes the additional compliance-specific check redundant
- B. Do not approve: removing the *specific* check for forward-looking language (a specific regulatory risk in wealth management) because a *general* reviewer already exists conflates two different kinds of review — a general advisor read-through and a compliance-specific regulatory check are not substitutes for each other, regardless of track record length
- C. Approve the change, but only for clients below a certain account size
- D. Approve the change, but require the compliance officer to spot-check 20% of commentary going forward instead

**Answer:** B — This question layers two tempting justifications (a long clean track record AND an existing general reviewer) to test whether the test-taker still recognizes that a *specific, named* risk check (forward-looking language, a known regulatory issue) is not satisfied by a *general* review happening for other reasons — the two checks serve different purposes even when performed by different people reading the same document.

---

### Q41.
A consumer-electronics company's employees have started using a personal, consumer-grade AI voice-transcription app during customer-support calls to draft call summaries, because the approved support platform's built-in summarization feature frequently times out on longer calls. Call summaries reference customers' names, purchase details, and sometimes partial payment information mentioned during troubleshooting.
**Options**
- A. Immediately discipline any employee found using the unapproved app, since customer payment information is involved
- B. Report the capability gap (timeout failures on longer calls) to the platform/policy owner and fix or work around the approved tool's limitation, while keeping the consumer app closed to any call involving customer payment or personal information in the meantime — the pattern (a real capability gap driving a well-intentioned workaround) matters more here than punishing the workaround
- C. Approve continued use of the consumer app for now, since it solves a real, currently-unaddressed problem
- D. Ban all call summarization, AI-assisted or otherwise, until a long-term platform fix is implemented

**Answer:** B — This is a harder version of the capability-gap pattern specifically because it involves payment information (higher stakes than the earlier photograph-based example), which makes both extremes (ignoring the gap by disciplining, or accepting the workaround by approving it) clearly wrong — the correct answer still centers on fixing the actual gap while closing the risky workaround for the highest-risk call types immediately.

---

### Q42.
A regional nonprofit's development team uses an AI assistant's incognito/temporary-chat mode for all donor-prospect research conversations "to avoid cluttering our shared account's history." Separately, they've been told an upcoming grant-compliance audit will require records of what tools and data sources were used to identify major-gift prospects.
**Options**
- A. Incognito/temporary mode is a reasonable choice here, since it only affects what's visible in the tool's own history and memory, not the organization's separate record-keeping obligations — the audit-readiness question should be addressed by the org's own process/record-keeping practices regardless of which chat mode is used
- B. Incognito/temporary mode should be avoided entirely for donor research, since it prevents the audit from ever being satisfied
- C. Incognito/temporary mode fully satisfies data-minimization best practice and also happens to solve the audit-readiness question
- D. Incognito/temporary mode is irrelevant to the audit either way, since audits only examine data sources, not AI tool usage patterns

**Answer:** A — This is a harder, more nuanced application of the incognito/temporary-mode principle from the earlier "nothing on record" scenario type: here, unlike a plan to *evade* an audit, the team's goal is legitimate (tidiness), and the correct answer recognizes that private-chat modes affecting the *tool's own* history/memory is a separate question from the *organization's* own obligation to keep independent records for compliance — the audit-readiness gap, if any, isn't created or solved by the chat mode itself.

---

### Q43.
A property-insurance carrier's claims department wants Claude to draft an initial coverage determination (approve/deny/investigate further) for straightforward, low-dollar-value claims (under a defined small threshold), with a licensed adjuster required to countersign every determination before it's communicated to the policyholder.
**Options**
- A. Appropriate-with-review: this defines WHO (licensed adjuster), WHAT (the coverage determination itself), and WHEN (before communication to the policyholder) — but the threshold-based scope limitation (low-dollar-value only) is also a meaningful part of what makes this appropriate, and should be explicitly preserved rather than later expanded without a fresh review
- B. Fully appropriate with no review needed, given the low-dollar threshold already limits exposure
- C. Inappropriate for any AI drafting involvement, since coverage determinations are inherently high-stakes regardless of dollar value
- D. Appropriate-with-review, but the adjuster's countersign should be replaced by a second AI review pass for efficiency, given the low-dollar threshold

**Answer:** A — This question is designed so that A initially looks like a simple "yes, this satisfies the WHO/WHAT/WHEN gate" answer, but the harder, complete version of the correct answer also flags that the dollar-threshold scope is load-bearing — if that threshold silently expands later without a fresh review of the gate's adequacy at higher stakes, the original appropriate-with-review classification would no longer hold.

---

### Q44.
A staffing agency's AI-assisted candidate-matching tool has operated for two years with strong placement-success metrics. A new client asks the agency to also use the tool to auto-reject candidates who don't meet a client-specified "cultural fit" criterion, described only as "someone who'll mesh well with our fast-paced, high-energy team."
**Options**
- A. Proceed, since the underlying matching tool already has a strong two-year track record
- B. Decline to implement "cultural fit" as an auto-reject criterion in its current vague form: an ill-defined, subjective criterion like this carries meaningful risk of proxying for protected characteristics, and should be escalated to the agency's own compliance/legal function for a fairness review and a much more concrete definition before any automated filtering is built around it, regardless of the tool's unrelated track record
- C. Proceed, but only auto-reject candidates who fail the criterion by a wide margin, using a numeric confidence threshold
- D. Proceed, but require a recruiter to review only the candidates who were auto-rejected, not those who passed

**Answer:** B — The tool's general track record on unrelated matching criteria doesn't validate a *new*, vague, and specifically risky criterion — "cultural fit" phrased this way is a well-known proxy-discrimination risk pattern in hiring, and it needs its own compliance review and concrete redefinition, not a numeric confidence threshold (C) or partial review (D), neither of which addresses the vagueness/proxy risk itself.

---

### Q45.
A hospital's IT governance committee is reviewing an AI vendor's claim that its clinical-documentation assistant "has been validated as safe and effective" based on the vendor's own internal testing, with no independent third-party validation performed. A committee member argues that since the vendor is a reputable, established company, the validation claim can be accepted as-is.
**Options**
- A. Accept the claim, since reputable vendors have strong incentives to be truthful about safety validation
- B. Treat the vendor's own internal testing as informative but not equivalent to independent verification — the same principle that a model's self-report isn't independent evidence extends to a vendor's self-report about its own product, regardless of the vendor's general reputation, and an independent validation path is still warranted before clinical deployment
- C. Accept the claim only if the vendor provides a written summary of its testing methodology
- D. Reject the vendor outright, since any company claiming its own product is "safe and effective" should be presumed to be overstating

**Answer:** B — This extends the independent-verification principle from model outputs to vendor claims about their own products: a vendor's reputation doesn't substitute for independent validation, and a written methodology summary (C) is still the vendor's own self-report, just in more detail — neither resolves the lack of independent verification, though outright rejection (D) also overcorrects past what the situation calls for.

---

### Q46.
A national grocery chain's loss-prevention team deploys an AI system that flags in-store customers for closer staff attention based on behavior-pattern analysis from security footage. After three months, an internal review finds flagged customers are disproportionately from one demographic group relative to store foot traffic, though the loss-prevention outcomes (actual theft caught) show no statistically significant demographic skew.
**Options**
- A. Since actual theft-catch outcomes show no skew, the flagging pattern itself is not a problem worth escalating
- B. Escalate the flagging-pattern disparity to the policy/fairness owner regardless of the theft-catch outcome parity: being subjected to closer staff scrutiny is itself a real, disparate experience for customers even when it doesn't ultimately result in a theft finding, and that experiential harm is a separate question from catch-rate accuracy
- C. Adjust the system to equalize flagging rates exactly across demographic groups, regardless of underlying behavior-pattern data
- D. Discontinue the system entirely, since any demographic disparity in flagging is disqualifying regardless of context

**Answer:** B — This is a harder fairness question because the "outcome" metric (theft actually caught) looks clean, which makes it tempting to conclude there's no real problem — but the disparity in who experiences *being flagged and scrutinized* is itself a harm worth escalating, independent of whether flagged individuals turn out to be guilty at equal rates.

---

### Q47.
A community bank's small-business lending team uses Claude to draft loan-denial explanation letters required under fair-lending disclosure rules. The letters must state specific, accurate reasons for denial. An efficiency-focused branch manager proposes using a rotating set of five pre-approved, generic denial reasons "so the letters go out faster and more consistently."
**Options**
- A. Approve the rotating generic-reasons approach, since consistency in letter format reduces legal risk
- B. Do not approve: fair-lending disclosure requirements are specifically about giving each applicant the *actual, specific* reason for their denial — substituting speed/consistency for accuracy on this particular output defeats the legal and ethical purpose of the disclosure requirement itself, regardless of how much faster or more consistent it makes the process
- C. Approve the approach, but require a compliance review of the five generic reasons once, when first created
- D. Approve the approach only for denials below a certain loan-amount threshold

**Answer:** B — This scenario intentionally frames the shortcut around desirable-sounding goals (speed, consistency) to see whether the test-taker still recognizes that some outputs (like a legally-required, applicant-specific disclosure) have accuracy as their entire point — no threshold (D) or one-time review (C) fixes a design that structurally can't produce applicant-specific accurate reasons.

---

### Q48.
A logistics company's compliance team is deciding whether an AI-assisted customs-classification tool needs to disclose AI involvement to the customs broker who ultimately files declarations based on its suggested classifications. The tool's suggestions are always reviewed and can be overridden by a licensed customs specialist before filing.
**Options**
- A. No disclosure is needed, since a licensed specialist reviews every suggestion before it's used
- B. Disclosure to the customs broker is still appropriate: the broker is relying on the specialist's output without necessarily knowing an AI tool shaped the underlying suggestion, and disclosure of AI involvement in a regulatory-filing-adjacent process is a reasonable transparency practice even when a qualified human reviews and can override it
- C. Disclosure is needed only if the specialist overrides the AI's suggestion, to explain the discrepancy
- D. Disclosure is unnecessary, since customs brokers don't need to know internal tooling used by their suppliers

**Answer:** B — Human review/override capability addresses the accuracy-safeguard question but doesn't resolve the separate transparency question: whether someone relying on the output (the broker) has a reasonable interest in knowing AI was involved in shaping it, even when a human retained final judgment.

---

### Q49.
A regional healthcare system's telehealth platform proposes retaining full video-call recordings (not just AI-generated summaries) indefinitely "in case the AI summary is ever challenged and we need to verify against the original." The platform's current retention policy for the summaries themselves is 7 years, matching medical-record requirements; no policy currently addresses the underlying recordings.
**Options**
- A. Approve indefinite recording retention, since having the original available to verify a challenged summary is a reasonable, low-risk safeguard
- B. Escalate the retention-period question for the underlying recordings to whoever owns data-retention/privacy policy before implementing indefinite retention — "indefinite" retention of sensitive video health data is a substantively different, and higher, privacy exposure than retaining a text summary for a defined 7-year period, and shouldn't be adopted as a byproduct of verification convenience without its own deliberate policy decision
- C. Approve retention matching the 7-year summary policy, applied automatically to the recordings as well
- D. Delete all recordings immediately after summary generation, since only the summary has an established retention policy

**Answer:** B — The verification rationale (having the original if a summary is challenged) is reasonable, but "indefinite" retention of sensitive video recordings is a much bigger privacy decision than the stated rationale requires, and it's being proposed without any deliberate retention-period decision at all — this needs its own policy escalation rather than defaulting to indefinite, defaulting to matching an unrelated document's retention period (C), or the opposite overcorrection of immediate deletion (D) which would defeat the legitimate verification purpose entirely.

---

### Q50.
A national retailer's return-fraud model, which incorporates a customer's return frequency and total return value among other factors, has operated for a year with strong fraud-catch rates. A new analyst proposes adding "average time between purchase and return" as an additional input, noting that legitimate returns (e.g., gift returns after holidays) often have longer gaps than fraudulent ones.
**Options**
- A. Add the input without further review, since it's a behavioral metric unrelated to any protected characteristic and the model already has a strong track record
- B. Even for a facially neutral behavioral input like this, run the same disparate-impact consideration applied to any new scoring input before deployment — a facially neutral metric can still correlate with protected characteristics or disadvantage particular legitimate-return patterns (e.g., holiday gift-giving customs that vary by community) in ways worth checking before adoption, not just assuming neutrality from the input's description
- C. Skip review since return-frequency and return-value (the existing inputs) were presumably already reviewed, and this is a similar type of behavioral metric
- D. Add the input, but only review it if fraud-catch rates change significantly after deployment

**Answer:** B — This tests whether the test-taker recognizes that "facially neutral, behavioral, not obviously protected-characteristic-related" (as this new input genuinely is) doesn't exempt an input from the same fairness-review discipline applied to any new scoring factor — assuming neutrality from a plausible-sounding rationale, or from analogy to previously-reviewed inputs (C), skips the actual check.

---

### Q51.
A national law firm allows attorneys to use Claude for legal research, with a written policy requiring that all case citations be independently verified against a legal database before inclusion in any filing. An attorney reports that they always follow this policy, but describes their verification step as: "I ask Claude to confirm each citation is accurate before I use it."
**Options**
- A. This satisfies the firm's verification policy, since the attorney is actively checking each citation as required
- B. This does not satisfy the policy's actual intent: asking the same model that generated a citation to confirm its own accuracy is not independent verification against a legal database — the attorney is following the letter of "I verify citations" while missing the substance of what independent verification requires
- C. This satisfies the policy only if Claude's confirmation includes a direct quote from the case
- D. This satisfies the policy as long as the attorney has never personally encountered a fabricated citation before

**Answer:** B — This is a harder, applied version of the independent-verification principle specifically targeting a well-known real failure mode (fabricated legal citations): an attorney can sincerely believe they're complying with a verification policy while actually performing a self-report check that doesn't meet the policy's substantive requirement of independent, database-based verification.

---

### Q52.
A manufacturing company's HR team uses an AI tool to draft performance-improvement-plan (PIP) language for underperforming employees, with a manager required to review and personalize each draft before delivery. An employee later grieves their PIP, alleging the language was "generic and dehumanizing, clearly written by AI with no real consideration of my situation." HR responds that a manager did review and approve the PIP before delivery, satisfying the required checkpoint.
**Options**
- A. HR's response is sufficient, since the defined review checkpoint (manager review before delivery) was followed as designed
- B. HR's response addresses whether the *process gate* was followed, but not whether that gate actually functioned as intended in substance — if the manager's review was itself superficial (a quick approval rather than genuine personalization), the named checkpoint existing on paper doesn't resolve the employee's substantive complaint that no real human judgment was meaningfully applied to their specific situation
- C. HR's response is insufficient only if the manager cannot produce evidence of specific edits made to the draft
- D. HR's response is insufficient because AI should never be used to draft PIP language under any circumstances

**Answer:** B — This is a harder governance question because it distinguishes between a checkpoint *existing and being followed procedurally* versus that checkpoint *functioning substantively* — the earlier principle that "a person will review" needs WHO/WHAT/WHEN to be a real gate extends further here: even a well-specified gate can fail in practice if the review itself is superficial, which is a legitimate concern separate from whether the documented process was technically followed.

---

## Domain 1 — Prompting and Task Execution (14% — Q53–Q66)

### Q53.
A commercial real-estate associate attaches a 12-page lease abstract and asks Claude to "summarize the key terms for the investment committee." The committee needs exactly five things: rent escalation schedule, renewal options, termination rights, any tenant improvement allowances, and co-tenancy clauses — nothing else. The first draft is a well-organized eight-section summary covering the whole lease.
**Options**
- A. Make the prompt substantially longer, describing the property and lease history in more detail, so Claude better understands the context
- B. Specify the exact five items the committee needs and explicitly what to exclude (the other three sections), rather than relying on "key terms" to be interpreted the same way the associate means it
- C. Ask Claude to shorten the eight-section summary by half, keeping the same structure
- D. Attach the lease as a file instead of pasting excerpts, expecting a more targeted read

**Answer:** B — "Key terms" was interpreted reasonably by the model, just not in the way the associate specifically meant; naming the exact five required items (and what to leave out) resolves the ambiguity directly, rather than adding unrelated context, shortening a still-wrong structure, or changing the attachment format.

---

### Q54.
A benefits consultant's first draft request to Claude is: "Compare our three proposed health-plan options for the employee newsletter." The result is a dense, actuarial-style comparison table using terms like "coinsurance" and "out-of-pocket maximum" without explanation — technically accurate, but not right for a general-employee newsletter audience.
**Options**
- A. "This is too technical. Try again with a totally different approach."
- B. "The audience is general employees, not benefits specialists — keep the three options, but explain each term in plain language and use everyday framing (e.g., 'what you pay if...') instead of insurance jargon."
- C. Rewrite the original prompt from scratch with a much longer, highly detailed specification and try a more capable model.
- D. "Simplify this."

**Answer:** B — Specific, targeted feedback (name the actual audience gap and what "simpler" concretely means here) produces a better second draft than a vague "too technical, try again" (A), a full prompt-and-model overhaul (C) for what was actually a targeted, fixable gap, or an underspecified "simplify" (D) that doesn't say what changes.

---

### Q55.
A university department chair's first draft request reads: "Give me ideas for improving student engagement in our intro course." **(Select TWO — all-or-nothing)** Which **TWO** follow-up refinements best preserve this as a genuinely divergent, options-generating task while still improving its usefulness?
**Options**
- A. "Give me 15 varied ideas, spanning low-effort/quick-win options through bigger structural changes, without filtering any out yet — I'll evaluate them after."
- B. "Only give me ideas that fit our existing 50-minute lecture format, use no additional TA hours, and follow our current syllabus template exactly."
- C. "Include a mix of ideas other departments have used, and ones I haven't seen suggested before."
- D. "Rank the ideas from best to worst and only show me the top 3."
- E. "Format each idea as a two-sentence bullet point in a table with columns for effort and impact."

**Answer:** A, C — Both widen the range of what's generated (explicitly asking for volume and variety, spanning familiar and novel) without pre-filtering, which is what a genuinely divergent brainstorming request needs. B constrains the response too tightly for a brainstorm (locking in format/resource assumptions before ideas are even generated), and D and E both prematurely convergent-ize the task (ranking/cutting to 3, or locking a rigid output format) before divergent value has been captured.

---

### Q56.
A city library system's associate needs to reconcile a decade of digitized catalog records against a newer standardized format, and has only sampled a handful of the oldest records so far, which a colleague warns are "inconsistently formatted, some by hand originally." The associate's instinct is to write one comprehensive prompt covering every formatting inconsistency they can imagine, then have Claude write and run the full conversion in one pass.
**Options**
- A. Write the comprehensive rule set now, covering every imaginable inconsistency, to avoid multiple rounds of rework
- B. First request that Claude profile a representative sample across the full decade (not just the oldest records) and report the actual range of formatting inconsistencies found, before any conversion rules are written
- C. Run the conversion now on the assumption that unexpected issues can be fixed as they surface in the output
- D. Ask for the conversion code in a specific language so the associate can inspect the logic before running it on the full decade of records

**Answer:** B — This is a harder version of the profile-before-rules principle, specifically because it adds a subtler trap: the associate has only sampled the *oldest* records, but the profiling step needs to cover the *full* decade's range of formats, not just extend the sample within the subset already known to be messy — a colleague's warning about one subset shouldn't narrow the scope of the diagnostic step.

---

### Q57.
A nonprofit's grant-writing associate needs a full grant-narrative draft for a specific foundation, and their instinct is to request the complete narrative immediately, in one detailed prompt covering the foundation's stated priorities.
**Options**
- A. Request the complete narrative now, since including the foundation's stated priorities upfront should be enough specification for a strong first draft
- B. First ask Claude to map what's already known and available — the organization's past successful grant narratives, this foundation's funding history and stated priorities, and any prior (even unsuccessful) applications to this same foundation — before generating new narrative text
- C. Request three different narrative drafts in different tones and select the strongest as the base
- D. Ask Claude to grade a rough outline the associate writes first, before any narrative drafting begins

**Answer:** B — Even with the foundation's priorities included in the prompt, jumping straight to narrative generation skips grounding the draft in the organization's own track record and this specific foundation's history — mapping what's known first (a decomposition step for an open-ended writing task) produces a better-grounded narrative than three stylistic variants (C) or grading an outline in isolation (D).

---

### Q58.
A regional airline's associate, in a brand-new chat with no prior conversation history, asks Claude to draft a flight-delay compensation notice for affected passengers. The first draft correctly follows the required regulatory disclosure format but uses the wrong currency symbol for one of the three markets the notice needs to cover.
**Options**
- A. Switch to a more capable model immediately, expecting it to handle multi-market currency correctly
- B. Treat this as under-specification: the request likely didn't explicitly state which currency applies to which market, so re-check the original request against that specific unstated requirement and add it explicitly
- C. Start an entirely new chat and resend the identical prompt, in case something in the first chat caused the error
- D. Check whether a stored account instruction or knowledge file about currency formatting has gone stale

**Answer:** B — With no conversation history to overload (ruling out C as the mechanism) and no prior working version to compare against for staleness (ruling out D), a first-attempt error on an unstated multi-market requirement (which currency for which market) is a specification gap to close directly, not a model-capability issue.

---

### Q59.
A hotel-group associate's fully-specified delegation (reader, purpose, budget, format, and what Claude may decide alone) still results in Claude silently omitting one of the four requested comparison criteria from the final table, without noting the omission anywhere.
**Options**
- A. The request needed more background detail about why each criterion matters
- B. The request needed an explicit closing instruction requiring Claude to confirm, after finishing, that every originally requested item is present in the output, or to flag any omission by name — a "you may decide/must flag when you decide" instruction addresses discretionary choices, but a specific silent *omission* of a directly requested item is a distinct failure this instruction alone may not catch
- C. The request needed a stricter budget constraint
- D. The request needed the table reformatted as a spreadsheet instead

**Answer:** B — This is a harder distinction from the earlier "flag when you decide" pattern: an outright silent omission of an explicitly requested item is a different failure than exercising unflagged discretion on an ambiguous choice (like a tie-break) — the fix here is a specific completeness-confirmation instruction, not simply more background detail or a different output format.

---

### Q60.
A market-research firm's analyst pastes 25 open-ended customer-interview transcripts into one request, asking for theme identification, a frequency count per theme, and a client-ready insight memo, all at once — but this time, includes an instruction: "Before counting or writing anything, first show me your theme definitions and a table mapping each transcript to its assigned theme, and wait for my confirmation before proceeding."
**Options**
- A. This instruction doesn't meaningfully change the risk of a downstream error, since the underlying single large request remains
- B. This instruction substantially reduces the earlier decomposition risk even within a single message, because it explicitly inserts a verification checkpoint (the mapping table) and a wait-for-confirmation gate between the coding step and the downstream counting/writing steps, functionally achieving the same protection as separate staged requests
- C. This instruction is unnecessary as long as the analyst reviews the final memo carefully
- D. This instruction should also specify a maximum number of themes, or it won't work as intended

**Answer:** B — This tests whether the test-taker recognizes that the *structural* protection (verify the intermediate coding step before building on it) can be achieved within a single, well-constructed request via an explicit checkpoint-and-wait instruction — it isn't strictly about how many separate messages are sent, but about whether verification happens before downstream steps build on unverified intermediate output.

---

### Q61.
A management consultant is preparing a client workshop and asks Claude for "10 icebreaker activity ideas" for a group of senior executives who are described, in the same prompt, as "notoriously skeptical of anything that feels like a typical corporate team-building exercise." The results returned are 10 fairly conventional icebreaker ideas (two-truths-and-a-lie, speed networking, etc.).
**Options**
- A. The prompt was already well-specified (audience described, quantity given); the model simply produced a weak result, so try a different, more capable model on the identical prompt
- B. The prompt named the audience constraint ("skeptical of typical exercises") but the actual generated ideas weren't explicitly checked against that specific constraint; a targeted iteration ("of these 10, which specifically avoid feeling like a typical corporate exercise, and give me 5 alternatives that lean further away from that pattern") more directly addresses the gap than starting over
- C. Icebreaker requests are inherently unsuited to AI assistance for skeptical audiences, and should be brainstormed manually instead
- D. The prompt should have specified a stricter format (e.g., "each idea in one sentence") to force more creative constraint-following

**Answer:** B — The audience constraint was stated but the model's divergent output wasn't yet filtered or iterated against that specific constraint — a targeted, specific follow-up (naming exactly what "still feels typical" means, in the direction the ideas should move) is the efficient iteration move, rather than switching models on the same prompt, declaring the task unsuited, or adding an unrelated formatting constraint.

---

### Q62.
An operations manager delegates a data-cleaning task on a 5,000-row customer export, providing clear rules for handling duplicates and missing fields, and separately noting: "If you encounter a data pattern not covered by these rules, stop and describe it to me rather than guessing how to handle it." Claude encounters an unanticipated pattern (a batch of rows with a foreign-format phone number), stops, and describes it clearly, without attempting a fix.
**Options**
- A. This is the request behaving exactly as intended: an explicit "don't guess, ask" instruction for out-of-scope cases produced the correct behavior when a genuinely unanticipated pattern arose
- B. This is a prompting failure, since a well-specified request shouldn't encounter any unanticipated patterns at all
- C. This is a context-overload issue, since 5,000 rows is a large dataset
- D. This is a sign the task needed a more capable model to handle the unanticipated pattern autonomously

**Answer:** A — This is included as a "correctly designed prompt working as intended" recognition question: an explicit, well-placed "flag rather than guess" instruction for genuinely out-of-scope cases is good task design, and the model encountering *and correctly flagging* an edge case is the system working, not a fault to diagnose.

---

### Q63.
A corporate-communications associate needs the same underlying announcement (a policy change) delivered as: a two-line push notification, a one-paragraph email summary, and a detailed FAQ document. The associate's plan is to ask for all three in one prompt: "Give me a push notification, an email summary, and an FAQ for this policy change."
**Options**
- A. This single combined prompt is well-suited to the situation, since all three outputs describe the same underlying policy change and benefit from being drafted together for consistency
- B. Decompose the request by output format instead, requesting the push notification, email summary, and FAQ as separate, sequential requests, each with its own length/format/purpose constraint, since the three formats have very different constraints (extreme brevity vs. structured depth) that a single combined prompt risks blending or under-serving for at least one of the three
- C. Request only the FAQ first, then ask Claude to extract the push notification and email summary from it afterward
- D. Request all three in one prompt, but ask for extended thinking to be turned on to handle the combined complexity

**Answer:** B — Even though the three outputs share the same underlying content (making A tempting, since consistency does matter), their format constraints are different enough (a two-line notification has essentially opposite constraints from a detailed FAQ) that a single combined prompt risks a "one-size-fits-none" result — this is task decomposition applied by *output format/constraint type*, not just by topic or section.

---

### Q64.
A regional theater company's marketing associate needs to know this week's local weather forecast for an outdoor-event contingency plan, needs a cited, multi-source comparison of five ticketing-platform vendors' fee structures for a board decision, and needs a one-line reminder of what "will call" means for a new box-office volunteer. **(Select THREE — all-or-nothing)** Which **THREE** correctly match each need to the most fitting way of answering it?
**Options**
- A. The weather forecast → a quick, current-facts lookup, not a deep multi-source research pass
- B. The ticketing-platform fee comparison → a deeper, cited research-style pass gathering and comparing multiple vendor sources
- C. The "will call" definition → an inline conversational reply, not a formal document
- D. The ticketing-platform fee comparison → a quick current-facts lookup, since fee structures are simple, published numbers
- E. The weather forecast → a cited, multi-source research pass, to ensure meteorological accuracy for an outdoor event

**Answer:** A, B, C — A live, simple current fact (weather) fits a quick lookup, not heavy research (ruling out E); a multi-vendor, board-facing comparison needing citations across several sources fits a deeper research pass, not a single quick lookup (ruling out D); and a one-line definition for a volunteer fits a short conversational answer, not a formal document.

---

### Q65.
A junior policy analyst with no prior housing-policy background drafts a public-facing explainer on a proposed zoning change, using Claude, based on the actual proposed ordinance text and a staff briefing document provided as sources. The explainer accurately reflects both source documents and addresses every point requested in the brief.
**Options**
- A. A grammar-and-clarity proofread by a colleague is the missing check before publication
- B. A colleague with genuine housing-policy or zoning expertise should assess whether the explainer is substantively credible and non-misleading by the field's own standards — accurately reflecting the provided sources and covering the requested points doesn't confirm the explainer captures policy nuances, common misunderstandings, or implications that only domain expertise would surface
- C. Ask Claude to rate the explainer's own accuracy and revise any section scoring below a set threshold
- D. Run the explainer through a formatting pass so it reads as polished as one written by an experienced policy writer

**Answer:** B — As in the customs-briefing pattern, internal accuracy against provided sources doesn't confirm subject-matter credibility from a domain expert's perspective — the specific gap (a junior analyst's inexperience) is closed only by genuine subject-matter review, not proofreading, self-rating, or polish.

---

### Q66.
A independent bookstore's owner asks Claude to "write a description for our new staff-picks display" and receives a single, generic paragraph. The owner then asks: "Actually, give me three different versions: one punchy and short for the front window sign, one warmer and more detailed for the store's email newsletter, and one that could work as an Instagram caption with relevant hashtags — each should describe the same staff-picks concept but fit its own format."
**Options**
- A. This second request is a well-constructed decomposition: it separates the same underlying content into distinctly specified formats, each with its own tone and length constraint, rather than asking for one generic version or three unconstrained variants
- B. This second request is over-engineered for a simple task and should have simply asked for "3 versions" without further detail
- C. This second request needed extended thinking enabled, given it asks for three simultaneous outputs
- D. This second request should have been split into three fully separate conversations rather than one combined request

**Answer:** A — This is another "recognize good prompting" question: explicitly naming each output's format, audience, and tone within one request is exactly the kind of decomposition-by-format that produces well-differentiated results — it doesn't need to be split into separate conversations (D, unnecessary overhead) or generalized into a vaguer "3 versions" ask (B), and it isn't a reasoning-depth problem needing extended thinking (C).

---

## Domain 3 — Product and Model Selection (12% — Q67–Q78)

### Q67.
A regional engineering firm's associate uses a mid-tier model to analyze a 150-page infrastructure inspection report, cross-referencing structural findings against a 40-page code-compliance checklist, and the output misses several cross-references between the two documents despite a clear, well-specified prompt that worked on a similar 30-page report previously.
**Options**
- A. Move to the top-capability tier, suited to holding a large, complex cross-referencing structure coherent across two lengthy source documents at once
- B. Switch to the fastest, lightest tier to process both documents more quickly and reduce the chance of losing track
- C. Turn off any extended reasoning mode, on the theory that additional reasoning steps are diluting attention to the source text
- D. Split each document into five separate chats and cross-reference them manually afterward

**Answer:** A — This is the same "escalate for depth on a large, coherent, cross-referencing structure" pattern, made harder by involving *two* separate long documents that must be held in relation to each other — exactly the kind of task the top capability tier is suited for, not a faster/lighter tier, reduced reasoning, or fragmenting the documents (which would break the very cross-referencing the task requires).

---

### Q68.
A customer-support operations lead runs every routine, single-sentence ticket-tagging task through the top-capability model tier with extended thinking enabled, "to be safe," while running an annual, high-stakes staffing-model rebuild (balancing seasonality, overtime rules, and multi-site constraints) on the fastest, lightest tier "since it just needs to produce a spreadsheet."
**Options**
- A. Only the staffing-rebuild choice is a problem; the ticket-tagging default is a safe, low-risk choice even if costly
- B. Both choices are mismatched, in opposite directions: routine single-sentence tagging needs neither the top tier nor extended reasoning, while a genuinely multi-constraint, high-stakes annual rebuild is exactly the kind of task that benefits from deeper reasoning and capability, regardless of the fact that its output format happens to be "just a spreadsheet"
- C. Neither choice is a problem, since model tier is primarily a cost lever and quality differences are marginal for both task types
- D. Only the ticket-tagging choice is a problem; the staffing rebuild is fine on the lightest tier as long as the spreadsheet formulas are reviewed afterward

**Answer:** B — The staffing rebuild's *output format* (a spreadsheet) is a red herring — what determines tier/reasoning-depth needs is the task's underlying complexity (multi-constraint optimization with real consequences), which is high regardless of how simple the deliverable format looks; meanwhile the tagging task's low complexity doesn't justify its expensive default either.

---

### Q69.
A specialty retailer's pricing team runs a heavy, multi-source research-mode pass every time they need to check a competitor's current advertised price for a specific product, "to be thorough," and separately relies on a single quick chat message (no research mode) to synthesize a nuanced comparison of long-term supplier-contract terms across three multi-year agreements with materially different renewal and penalty clauses.
**Options**
- A. Both choices are reasonable, since research mode is generally the more thorough option and a quick chat is generally the more efficient one
- B. Both choices are mismatched: a specific, current, single-fact lookup (a competitor's advertised price right now) doesn't need a heavy multi-source research pass, while comparing nuanced, multi-factor contract terms across three agreements is exactly the kind of task that benefits from deeper reasoning (e.g., extended thinking) rather than a single quick, unstructured pass
- C. Only the competitor-price lookup is mismatched; the contract comparison is appropriately handled with a quick chat since it's "just reading three documents"
- D. Only the contract comparison is mismatched; the competitor-price research-mode pass is appropriately thorough given pricing is business-critical

**Answer:** B — This inverts the more obvious pairing to test the underlying principle rather than surface impressions: a simple current-fact lookup doesn't need heavy research tooling regardless of business importance, and a genuinely multi-factor reasoning task (comparing clauses with different structures across three contracts) needs reasoning depth regardless of how simple "just reading documents" sounds.

---

### Q70. *(Select TWO — all-or-nothing)*
A corporate-events team is deciding, for five upcoming requests, whether extended thinking is worth its added time/cost. Which **TWO** are genuinely worth it?
**Options**
- A. Converting a finalized run-of-show document into a simple printable schedule handout
- B. Deciding the optimal seating-chart arrangement across 40 tables balancing known interpersonal conflicts, sponsorship-visibility requirements, and dietary-accommodation groupings simultaneously
- C. Looking up the venue's posted maximum occupancy limit from an attached venue-specs sheet
- D. Sequencing a multi-city product-launch tour across six cities under simultaneous constraints of venue availability, staff travel limits, and a fixed total budget
- E. Generating eight quick tagline options for a save-the-date email, to be narrowed down casually later

**Answer:** B, D — Both are genuine multi-constraint optimization problems where several competing factors must be weighed against each other simultaneously, which is exactly where deeper reasoning adds real value. A, C, and E are simple, low-stakes, largely single-step tasks where extended reasoning adds cost without meaningfully improving the result.

---

### Q71.
A boutique law firm's associate is three hours into a single long conversation drafting and revising a complex contract with Claude, and response quality has visibly degraded over the last 30 minutes — Claude has started contradicting an earlier-agreed defined term and has forgotten a formatting convention established at the start of the session.
**Options**
- A. Since quality was strong for the first 2.5 hours, this is most likely context overload from conversation length rather than a model-capability issue; the associate should summarize the agreed defined terms and formatting conventions, correct anything already drifted, and continue in a fresh session seeded with that summary
- B. Switch immediately to a more capable model tier within the same long conversation, since a stronger model would maintain the defined term and formatting convention regardless of conversation length
- C. Continue in the same conversation, simply repeating the defined term and formatting convention at the top of every subsequent message
- D. This is a sign the contract-drafting task itself is unsuited to AI assistance and should move to manual drafting from this point forward

**Answer:** A — The pattern (strong performance for a long stretch, followed by drift/contradiction specifically after a lengthy session) is the classic context-overload signature, best addressed by summarizing and restarting rather than upgrading model tier (which doesn't fix an overloaded context window), manually repeating information every message (a workaround, not a fix), or abandoning AI assistance for the task entirely.

---

### Q72.
A management consultancy's internal AI-strategy lead states as firm policy: "For any client-facing analytical deliverable, always use our most capable model tier with extended thinking enabled, regardless of the specific task, because our clients expect and are paying for our best work."
**Options**
- A. This is sound, defensible policy, since client-facing work should never risk being under-resourced
- B. This statement reflects a lack of task-fit judgment: "client-facing" describes who receives the output, not the task's actual complexity — a client-facing but genuinely simple task (e.g., reformatting an agreed set of findings into the client's template) doesn't need the top tier and extended reasoning any more than an equivalent internal task would, and applying a blanket rule based on audience rather than task complexity is exactly the pattern the credential's judgment framework tests against
- C. This is sound policy specifically for consultancies, even if it wouldn't be sound for other industries
- D. This is sound policy as long as the firm can absorb the additional cost

**Answer:** B — This is a harder version of the "always use the best" trap because it's dressed up as a client-service rationale (clients expect our best work) rather than a lazy habit — but the underlying judgment failure is the same: model-tier/reasoning-depth decisions should track task complexity, not who the audience happens to be.

---

### Q73.
A financial-services support team needs to: quickly verify today's published overnight interbank lending rate for a client call in five minutes, conduct a comprehensive, multi-source comparison of five competing custodial-services providers for a board presentation next month (with citations), and determine, given a client's specific and unusual combination of account types, which of three internal fee schedules applies (a determination requiring careful, multi-step reasoning through the firm's internal fee-schedule rules).
**Options**
- A. Rate lookup → a quick current-facts check; provider comparison → a deeper, cited multi-source research pass; fee-schedule determination → extended thinking to work through the multi-step internal rule application carefully
- B. All three → a deeper, cited multi-source research pass, since thoroughness is always the safer choice
- C. Rate lookup → extended thinking, since interest rates are financially significant; provider comparison → a quick lookup, since providers are well-known; fee-schedule determination → a quick lookup, since it's an internal document
- D. All three → extended thinking, since financial-services contexts always warrant deeper reasoning regardless of task type

**Answer:** A — Each task fits a different tool for a specific structural reason: a single current published rate needs a fast factual check, not deep research; a multi-source, citation-needing comparison needs an actual research pass; and a multi-step internal-rule application (not a lookup at all) benefits from deeper, careful reasoning — collapsing all three into "always thorough" or "always deep reasoning" ignores what each task structurally requires.

---

### Q74.
A regional theater's box-office system produces a "recommended ticket price" for an upcoming show that's noticeably higher than any comparable past show, with no obvious explanation in the current season's data. The associate's first instinct is to assume the pricing model hallucinated the figure and re-run the request with "use only this season's actual sales data."
**Options**
- A. Re-prompt with the stricter wording and regenerate the full recommendation
- B. Before assuming hallucination, check whether the pricing tool's Project knowledge contains an outdated general "premium pricing" reference document from a prior special event that may still be influencing the recommendation, and correct or remove it if so
- C. Switch to a more capable model tier, on the theory that a stronger model is less likely to fabricate a pricing figure
- D. Ask the tool to rate its own confidence in the recommended price and only accept figures above a high confidence threshold

- **Answer:** B — As with the earlier stale-rate-card pattern, an unusual, unexplained figure is often better explained by a stale or mismatched knowledge source still feeding the workflow than by outright fabrication — checking the actual configuration first is more diagnostic than re-prompting, upgrading the model, or relying on a self-reported confidence score.

---

### Q75.
A specialty coffee roaster's wholesale team has iterated five times with Claude on a bulk-order discount-tier calculator embedded in a client-facing quote template. Formatting, tier boundaries, and client-facing language are all now correct, but the final discounted-total figure is still subtly wrong on every attempt, despite five rounds of increasingly precise wording about how discounts should stack.
**Options**
- A. This is a feature mismatch: the stacking discount calculation should be performed via executable code rather than generated as prose text, regardless of how precisely the stacking rule is worded
- B. This is a description problem requiring one more, even more precise attempt at wording the stacking rule
- C. This is a model-capability problem requiring the top-capability tier
- D. This is a context-overload problem, since five rounds of iteration have accumulated in one conversation

**Answer:** A — Five rounds of increasingly precise wording still producing subtly wrong arithmetic is a strong, repeated signal that this is a prose-vs-computation feature mismatch, not a wording, model-capability, or context-length problem — the calculation needs to move into actual executable computation.

---

### Q76.
A university's IT helpdesk wants a single AI-assisted intake system to both instantly triage routine password-reset requests (extremely high volume, essentially no ambiguity) and also help resolve a smaller number of complex, multi-factor account-access disputes involving conflicting departmental permissions across multiple systems.
**Options**
- A. Use one uniform model configuration (same tier, same reasoning setting) for both request types, to keep the system simple to maintain
- B. Use a fast, lightweight tier configuration for the high-volume, low-ambiguity password-reset triage, and route the complex, multi-factor permission disputes to a configuration with deeper reasoning enabled (and potentially a higher capability tier) — the same underlying system can, and often should, apply different model-tier/reasoning judgments to structurally different request types it handles
- C. Use the highest-capability tier with extended thinking for both, since account-access issues are always security-sensitive
- D. Use the lightest tier for both, since IT helpdesk work is generally routine

**Answer:** B — This tests whether the test-taker recognizes that a single system serving structurally different task types should apply the underlying tier/reasoning-depth judgment *per request type*, not adopt one uniform setting for administrative simplicity (A), blanket caution (C), or blanket cost-minimization (D) — the "match tool to task" principle applies within one workflow just as much as across separate ones.

---

### Q77.
An urban-planning associate needs Claude to draft a public meeting notice (simple, templated, low-stakes) and, in the same working session, needs it to reconcile conflicting numeric traffic-count data from three different consulting reports commissioned over the years, where the reports used different methodologies and the discrepancy needs careful, multi-step reasoning to explain and resolve for a technical appendix.
**Options**
- A. Use the same default configuration for both tasks in the same session, since switching settings mid-session adds friction
- B. Keep the meeting-notice drafting on a standard default configuration, and specifically enable extended thinking for the traffic-count reconciliation, since resolving conflicting multi-source numeric data via different methodologies is a genuine multi-step reasoning task distinct in kind from the templated notice — switching configuration mid-session, when the two tasks are this different, is the correct judgment call even though it adds a small amount of friction
- C. Enable extended thinking for both tasks, since the associate is working on both in the same general session
- D. Use the lightest tier for the meeting notice and the lightest tier plus extended thinking for the traffic-count reconciliation, since a lighter tier plus deeper reasoning is more cost-effective than a heavier tier

**Answer:** B — The two tasks are genuinely different in kind (templated low-stakes drafting vs. multi-source numeric reconciliation requiring careful reasoning), and the correct judgment is to configure each task appropriately even within one working session — session-level convenience (A) or applying one setting to both (C) doesn't override task-level fit, and D's "lighter tier plus reasoning" substitution doesn't necessarily suit a task that may also benefit from a higher capability tier, not tier substitution alone.

---

### Q78.
A regional hospital's clinical-documentation team has been told that "extended thinking" and "the flagship model" are the same feature under different names by a well-meaning but mistaken vendor trainer, and has been avoiding extended thinking on cost-sensitive routine tasks specifically because they believe it always requires the (expensive) flagship tier.
**Options**
- A. The trainer's claim is correct, and the team's cost-avoidance behavior is appropriately cautious
- B. The trainer's claim is a specific, common misconception: extended thinking (a reasoning-depth toggle) and model tier (fast/thinking-capable/flagship) are independent settings, and the team's avoidance behavior, while cost-conscious in intent, is based on an incorrect premise that should be corrected — some tiers support extended thinking without requiring the flagship tier's cost
- C. The trainer's claim is correct for some vendors but not others, so the team should verify per-vendor before deciding
- D. The distinction doesn't matter in practice, since both settings should generally be minimized for cost reasons regardless of task

**Answer:** B — This directly tests the same independent-switches distinction from earlier in this domain, framed as a correction of a specific, plausible-sounding misconception (that reasoning depth and model tier are bundled) — correcting the premise matters because it changes the team's actual available options for balancing cost against reasoning depth on different tasks.

---

## Domain 5 — Configuration and Knowledge Management (12% — Q79–Q90)

### Q79.
A regional accounting firm's associate handles work for two clients, "Client A" (a construction company) and "Client B" (a restaurant group), currently in two separate Claude Projects, each correctly scoped with its own knowledge files and instructions. The associate now also needs to draft the firm's own internal year-end newsletter, unrelated to either client.
**Options**
- A. Draft the newsletter inside whichever client Project was most recently used, for convenience
- B. Draft the newsletter in a plain chat (or a separate, appropriately-scoped Project if the firm has one for internal/firm-wide work), rather than inside either client-scoped Project, since neither client's instructions or knowledge files are relevant to an internal firm newsletter and using one risks unintended cross-contamination of context
- C. Create a fresh Project for the newsletter, and import both clients' knowledge files into it in case any client data is referenced
- D. Draft the newsletter using the firm-wide account-level instructions alone, since a one-off task doesn't need Project scoping

**Answer:** B — This tests the harder edge case of Project scoping discipline: a one-off, unrelated internal task shouldn't be drafted inside an existing client-scoped Project (risking that Project's client-specific instructions/knowledge bleeding into unrelated work) — plain chat or a genuinely appropriate internal-work Project is the right scope, and there's no reason to import client knowledge files (C) into unrelated work.

---

### Q80.
An associate's account-level instructions include: "When I ask for a summary, always structure it as: Overview, Key Risks, Recommendation." This has worked well for the associate's typical risk-assessment work, but the associate has just started a new role requiring frequent short customer-service response summaries, where this three-part structure is now consistently unhelpful and out of place.
**Options**
- A. Keep the account-level instruction as-is, since it has a strong track record from the previous role
- B. Recognize that an instruction genuinely useful as "true everywhere" in one role may stop being appropriate as the associate's actual work changes, and either update the account-level instruction to reflect the new, more varied context, or move the three-part structure into a Project scoped specifically to the risk-assessment-type work it still suits, rather than leaving a now-mismatched global default in place
- C. Leave the instruction in place, and manually override it by writing "ignore your standard structure" at the top of every customer-service summary request
- D. Delete the account-level instruction entirely and rely on Claude to infer the right structure for each request going forward

**Answer:** B — This is a harder version of the account-level-scoping principle because the instruction was genuinely well-scoped *at the time it was written* (given the associate's prior role) — the lesson is that "true everywhere" instructions need to be revisited as the actual scope of "everywhere" (the associate's own work) changes, rather than assuming a once-correct global instruction stays correct indefinitely, patching around it per-request (C), or removing structure guidance altogether (D).

---

### Q81.
A high school's two AP History teachers share one Claude Project for "AP History Resources," containing both teachers' respective rubrics, sample essays, and pacing guides, because "it's all AP History content." One teacher's students have started receiving feedback referencing grading language from the other teacher's rubric.
**Options**
- A. This is expected and acceptable, since both teachers teach the same subject and course level
- B. This is a scoping error similar to mixing two business units' pricing files: even within the same general subject, each teacher's specific rubric/grading language should live in its own Project (or a clearly separated section with explicit per-request specification), since "same subject" doesn't mean "interchangeable materials," and the shared Project is causing exactly the cross-contamination this kind of scoping is meant to prevent
- C. This is acceptable as long as students are told feedback may reference either teacher's rubric
- D. This can be fixed by asking Claude, in each request, to "use the correct teacher's rubric," without changing the Project structure

**Answer:** B — "Same subject" is a more tempting-sounding justification for shared scoping than the earlier wholesale/retail example, but the underlying issue is identical: two genuinely distinct rule-sets (each teacher's own rubric) are getting cross-applied because they share one always-on knowledge pool — a per-request reminder (D) is a workaround, not a structural fix.

---

### Q82.
A consultant connected a project-management platform's connector three months ago and has used it daily without issue. Today, in a new chat, a request referencing a specific project's task list returns an error stating the connector cannot be reached, though the consultant confirms (by checking the platform directly) that the platform itself is fully operational.
**Options**
- A. Assume the connector has permanently expired after three months and needs to be fully reconnected from scratch immediately
- B. Before assuming full reconnection is needed, check narrower possibilities first: whether the connector is enabled for this specific new chat, whether a temporary permission or token issue exists, and whether the specific project referenced is one the connector actually has access to — a full "reconnect from scratch" response may be more disruptive than necessary if the actual cause is narrower
- C. Switch to manually copy-pasting task list data into chat going forward, to avoid connector reliability issues entirely
- D. Assume the issue is a temporary platform-side outage, despite having confirmed the platform is operational, and simply try again later

**Answer:** B — Even though this associate has months of reliable use (unlike the newer-connector example), the correct diagnostic instinct is still to check the narrower, more common causes (per-conversation enablement, specific project access, token issues) before concluding a full reconnection is needed — jumping to the most disruptive fix, abandoning the connector for manual workarounds, or ignoring already-confirmed platform status are all less efficient responses.

---

### Q83.
A boutique investment firm's Claude Project for a specific client contains that client's portfolio holdings as a knowledge file, refreshed monthly by an operations associate. A portfolio manager, preparing for a client call, notices the AI-generated portfolio summary references a holding the client sold three weeks ago.
**Options**
- A. This means the AI is hallucinating a holding not actually in the current portfolio
- B. This is most likely a stale-knowledge-source issue: the monthly refresh cycle means a sale from three weeks ago may not yet be reflected in the uploaded file, and the portfolio manager should confirm the file's actual last-refresh date and update it (or push the refresh cadence to match the call's needs) before relying on the summary for the client call
- C. This means the Project should be deleted and recreated to clear any corrupted cached data
- D. This means the portfolio manager should switch to a different model, which may have more current training data

**Answer:** B — A monthly refresh cycle creates a predictable staleness window, and a sale three weeks ago falls plausibly within that window — checking the actual file's currency (a configuration/maintenance question) is the right first step, rather than assuming hallucination, corruption requiring a rebuild, or a model-training-data issue (irrelevant, since the holding came from the uploaded file, not general training knowledge).

---

### Q84.
An associate wants a rule that should apply only when working on a specific quarterly board-deck project, should include several standing reference documents (last quarter's deck, the current financial data extract, the board's stated format preferences), and should not affect any other work the associate does.
**Options**
- A. A Skill, since it defines "how" to build a board deck on demand whenever requested
- B. A Project, since this need is genuinely scoped (one specific quarterly deliverable), always-on within that scope (reference documents and format preferences apply throughout the work), and explicitly should not leak into unrelated work — exactly the profile a Project is designed for, as opposed to a Skill (on-demand, not necessarily tied to specific reference files) or account-level instructions (global, which would incorrectly affect unrelated work)
- C. Account-level custom instructions, since board-deck quality matters enough to apply broadly
- D. Memory, since it will persist the board's format preferences over time automatically

**Answer:** B — This question is harder because a Skill (A) is genuinely plausible for "how to build a board deck," but the requirement that specific reference *files* stay attached and that the scope explicitly exclude other work points to a Project's combination of always-on files plus instructions within a bounded scope, which a Skill alone (on-demand logic, not necessarily bundled with specific persistent files) doesn't fully provide.

---

### Q85.
A mid-sized law firm is piloting a Claude connector to its document-management system for the first time, to support a new AI-assisted contract-review workflow. The pilot plan calls for connecting the system with full read/write access immediately, "so we don't have to reconfigure permissions later once the pilot proves successful."
**Options**
- A. Approve full read/write access from the start, since anticipating future needs avoids a later reconfiguration step
- B. Start with read-only access for the pilot, and deliberately grant write access later, specifically once the workflow has been validated and a genuine write use case (e.g., filing a reviewed document back into the system) is confirmed and scoped — granting broader access than the current pilot actually needs, based on anticipated future convenience, works against the principle that write access should be deliberately granted once actually needed and confirmed available, not provisioned in advance "just in case"
- C. Approve write-only access, since the review workflow's main function is producing analysis, not reading original documents
- D. Approve full read/write access, but only for the specific pilot user's individual account rea, rather than the firm's shared account

**Answer:** B — "Avoiding reconfiguration later" is a tempting operational-convenience argument, but it inverts the correct sequencing: access (especially write access) should be scoped to actual, confirmed current need, with broader access deliberately added later once a real use case exists — provisioning broad access upfront "just in case" is the pattern this principle specifically cautions against.

---

### Q86.
A freelance grant-writer's Claude account has developed a memory note, generated over several past conversations, stating a specific client "prefers a very formal, traditional tone." A new project for that same client explicitly requests "a much more casual, conversational voice for this particular campaign, different from our usual style."
**Options**
- A. Claude will correctly override the memory note automatically once the new, explicit in-conversation instruction is given, so no action is needed regarding the memory note itself
- B. Even if the explicit in-conversation instruction takes precedence for this specific project, the grant-writer should consider whether the memory note itself needs updating or qualifying (e.g., "usually prefers formal tone, except for [specific campaign type]") so that future conversations about this client don't default back to an now-incomplete generalization
- C. Delete the memory note immediately, since it has now been contradicted once
- D. This situation requires no attention at all, since memory notes are only suggestions and never actually influence output

**Answer:** B — This is a harder, more realistic memory-management scenario than a simply "wrong" memory note: the note isn't incorrect, just incomplete (it doesn't capture a legitimate exception) — the associate should consider refining it for future accuracy rather than assuming automatic override handles it (A, which may or may not hold every time) or overreacting by deleting a generally-accurate note (C) over one legitimate exception.

---

### Q87.
A community health clinic wants to connect Claude to its patient-scheduling system to help draft appointment-reminder messages, its first-ever connector integration touching any patient data. The IT lead proposes testing the integration using a full, real, de-identified export of last month's actual appointment data, reasoning that "de-identified real data is safer than synthetic data and more realistic for testing."
**Options**
- A. Approve this approach — de-identified real data is a reasonable, safer alternative to synthetic data for a first-time regulated-data integration test
- B. Prefer genuinely synthetic/invented data for this first-time pilot regardless of de-identification: de-identification of a real dataset can be imperfect (residual re-identification risk, especially in a small local clinic's data where a handful of unusual appointment patterns could be identifying) in ways synthetic data structurally avoids, and the standing practice specifically favors synthetic data for a first-time regulated-data workflow test
- C. Approve this approach, but only if the de-identification is performed by a different team than the one building the integration
- D. Skip both synthetic and de-identified testing, and go straight to a small, closely-monitored live pilot with real patient data

**Answer:** B — This is a harder test of the synthetic-data-first principle because de-identified real data is a genuinely more sophisticated, more tempting alternative than obviously-risky raw real data — but de-identification carries its own residual risk (especially in a small dataset where unusual patterns can still be identifying), which is exactly why the standing practice specifically prefers synthetic data over de-identified real data for a first-time regulated pilot, not just "some form of anonymization."

---

### Q88.
An operations team at a mid-size manufacturer has built a useful, reusable Skill for formatting weekly production reports. A new hire, unfamiliar with the Skill, manually recreates the same formatting logic from scratch in their own individual prompts each week, producing slightly inconsistent results compared to the team's Skill-based output.
**Options**
- A. This is a Skill-design problem — the Skill itself needs to be simplified so new hires can discover and use it more easily
- B. This is an onboarding/awareness gap rather than a configuration-design flaw: the Skill itself is correctly built and scoped, but the new hire simply doesn't know it exists or how to invoke it — the fix is surfacing/teaching the existing Skill to the new hire, not necessarily changing the Skill's design
- C. This is a memory problem, since the system should have "remembered" to tell the new hire about the Skill automatically
- D. This is a Project-scoping problem, since the Skill should have been built as a Project instead

**Answer:** B — This distinguishes a genuine configuration-design flaw from a simpler awareness/onboarding gap: the Skill working correctly for the rest of the team, with the new inconsistency traceable specifically to one person not knowing it exists, points to an onboarding fix, not a redesign of the Skill, a memory mechanism, or a wholesale change from Skill to Project.

---

### Q89.
A city government's public-records office has a Claude Project for handling records-request intake, with standing instructions that say: "Always redact personal identifying information before summarizing a request for the public log." The office has just started receiving a new category of request (business-license records) where the requester's business name is itself the relevant subject and generally should NOT be redacted, unlike prior request types.
**Options**
- A. Keep the blanket redaction instruction unchanged, since "always redact personal identifying information" is a safe default that should simply be manually overridden per-request as needed for the new category
- B. Update the Project's standing instructions to explicitly distinguish the new category's different redaction needs (e.g., "redact personal identifying information for individual requesters; business names for business-license requests are the subject of the request and should not be redacted unless a specific business owner's personal details also appear"), rather than leaving a now-imprecise blanket rule in place to be manually corrected each time
- C. Move the new request category into a completely separate Project so the original instruction never has to change
- D. Remove the redaction instruction entirely, since it no longer applies cleanly to every request category

**Answer:** B — As the actual scope of work handled by a Project evolves (a new request category with genuinely different needs), the Project's standing instructions should be updated to reflect that nuance directly, rather than left as an over-broad rule requiring manual correction each time (A), split off into a separate Project to avoid updating the original (C, unnecessary fragmentation for a rule that could simply be made more precise), or removed altogether (D, which loses the still-valid protection for the original request types).

---

### Q90.
A regional airline's crew-training department built a Skill several years ago that formats training-completion certificates according to a specific regulatory template. The regulator has since updated the required template format, but the Skill still produces certificates in the old format, and several recently issued certificates have gone out non-compliant before anyone noticed.
**Options**
- A. This is primarily a model-capability issue; a more capable model would have recognized the regulatory template had changed and adapted automatically
- B. This is a stale-configuration issue: the Skill's instructions describe a fixed, specific template that hasn't been updated to reflect the regulator's change, and it needs to be manually revised to match the current requirement — a Skill's instructions are static and don't self-update when the real-world standard they describe changes, regardless of model capability
- C. This is a context-length issue, since the Skill has been used many times over several years
- D. This is a connector issue, since the certificate template should be pulled from a live regulatory source instead

**Answer:** B — This is a harder, higher-stakes version of the earlier stale-Skill pattern (with real regulatory-compliance consequences already realized): a Skill's instructions are fixed text that must be manually maintained as the real-world requirement they encode changes — no model upgrade compensates for genuinely outdated instructions, and while a live connector to a regulatory source (D) might be a good future improvement, it doesn't change that the *immediate* root cause is the Skill's static, unmaintained instructions.

---

## Domain 7 — Troubleshooting and Optimization (10% — Q91–Q100)

### Q91.
A regional water utility's scheduled weekly agent task, which compiles a compliance-monitoring report and emails it to three regulators, has now failed silently two weeks in a row, after months of reliable operation. The team's instinct is to immediately rewrite the underlying prompt with more detail, assuming the task's instructions have become inadequate.
**Options**
- A. Rewrite the prompt with more detail immediately and re-run, since two consecutive failures after months of success suggests the instructions need reinforcement
- B. Before touching the prompt, check systematically whether the run is paused pending approval, whether usage limits were hit, whether required permissions or connector access changed, and whether the destination (the regulators' email addresses or a delivery system) is still valid — two failures after a long period of reliable operation is more consistent with an environmental/plumbing change than a sudden inadequacy in instructions that had worked for months
- C. Recreate the entire task from scratch on a different automation platform, since repeated failure suggests the current platform is unreliable
- D. Manually compile and send the report for the next few weeks while waiting to see if the automated task starts working again on its own

**Answer:** B — A sudden failure after a long, stable track record is a stronger signal of an environmental change (permissions, limits, connector, destination) than of the original instructions suddenly becoming inadequate — the systematic plumbing check should come before prompt-rewriting, platform migration, or simply waiting.

---

### Q92.
A corporate-communications team notices that Claude-drafted press statements have, over the past month, started requiring significantly more editing rounds before approval than they did six months ago, even though the prompt template used has not changed. Which combination of questions should be asked first, before proposing a fix?
**Options**
- A. "Should we switch to a different AI vendor?" and "Should we hire an additional writer?"
- B. Has anything about the *type* of statements being requested shifted (e.g., more sensitive/complex topics recently)? Has the conversation/session pattern changed (e.g., now reusing one long-running chat rather than fresh sessions)? Has any reference material or style guide used to inform drafts gone stale or been replaced without updating the associated configuration?
- C. "Is the current model tier still the newest one available?" and "Is extended thinking turned on?"
- D. "Are we using the correct file format for the press statement output?" and "Is the formatting consistent with brand guidelines?"

**Answer:** B — With the prompt template itself unchanged, the diagnostic questions should probe the other likely causes: a shift in task complexity/type, a change in session/context patterns, or staleness in supporting reference material — not jump to vendor-switching or additional hiring (A), assume a model/reasoning-setting issue without evidence (C), or focus on formatting concerns unrelated to the reported symptom (editing rounds, not formatting complaints) (D).

---

### Q93.
A hospital's clinical-education team has, for the past two years, defaulted to the top-capability model tier for every task "since patient-adjacent education content should always get our best effort," including routine tasks like reformatting an already-finalized training module into a printable handout.
**Options**
- A. "Patient-adjacent" content justifies the top-tier default regardless of the specific task's actual complexity
- B. This is a tier-mismatch habit, not a task-fit judgment: "patient-adjacent" describes the general subject area, not the complexity of a specific task like reformatting an already-finalized document — the top tier should be reserved for tasks that actually need its capability (e.g., synthesizing complex new clinical content), and this specific reformatting task doesn't require it regardless of the broader subject area's sensitivity
- C. This is appropriate as long as the cost is within the department's budget
- D. This is a connector problem, since the training module needs to be pulled from a document-management system

**Answer:** B — This intentionally uses "patient-adjacent" as a plausible-sounding justification, similar to "client-facing" in an earlier question, to test whether the test-taker distinguishes subject-matter sensitivity in general from the actual complexity of a specific task — reformatting an already-finalized document is low-complexity regardless of the broader subject's sensitivity.

---

### Q94.
A nonprofit's grant-reporting associate says, "Every week I re-explain our organization's mission statement, our fiscal year dates, and our standard reporting disclaimers to Claude before I can start drafting anything." What is the correct symptom-to-concept mapping and fix?
**Options**
- A. This indicates the associate should switch to a different AI tool with better memory by default
- B. This is a configuration gap: this recurring, always-true-for-this-work information (mission statement, fiscal year, standard disclaimers) belongs in a Project's standing instructions or knowledge files (or account-level instructions, if genuinely true across all the associate's work, not just this reporting task), not re-typed weekly
- C. This indicates the underlying grant-reporting task doesn't fit AI assistance well and should move to a manual template instead
- D. This indicates extended thinking should be enabled so Claude can infer this context automatically each time

**Answer:** B — "Same background information, every time, for this recurring task" is the textbook signal for moving that content into a persistent configuration layer — not a tool-switching problem, a task-fit problem, or something a reasoning-depth setting would address.

---

### Q95.
A regional airline's pricing-operations team notices that a Claude-assisted fare-adjustment recommendation task, which has run smoothly for over a year, suddenly began giving noticeably different-quality recommendations three days ago — coinciding, the team later realizes, with an unrelated IT migration of the shared drive where the Project's reference fare-rules document lives.
**Options**
- A. This is most likely a coincidental model-quality fluctuation unrelated to the IT migration, and should be monitored for another week before investigating further
- B. Given the precise timing coincidence with the IT migration, check first whether the Project's connector/reference to the fare-rules document survived the migration correctly (e.g., a broken file link, a duplicated old version, or a permissions change) — a stale or broken configuration reference is a far more likely explanation for a sudden, precisely-timed quality drop than an unrelated model fluctuation
- C. This is a context-overload problem, since the Project has been used for over a year
- D. This is a task-fit problem; fare-adjustment recommendations should not have been delegated to AI assistance in the first place

**Answer:** B — A sudden quality change that precisely coincides with an unrelated infrastructure event (the migration) is a strong, specific clue pointing to a broken or altered configuration reference, not a random model fluctuation (A, which ignores a highly relevant coincidence), general context overload (C, which doesn't explain the sudden onset tied to a specific event), or a task-fit conclusion contradicted by over a year of prior smooth operation (D).

---

### Q96.
A specialty printing company notices that routine, simple print-job description tasks (essentially, converting a customer's order form into a one-line job ticket) have quietly become one of the largest line items in their monthly AI usage costs, despite no increase in order volume.
**Options**
- A. This is likely a tier-mismatch: check whether this simple, high-volume, low-complexity task is being run on a more expensive tier or with reasoning settings enabled that it doesn't need, before assuming volume, pricing changes, or task-suitability are the cause
- B. This means the AI provider must have changed its pricing structure without adequate notice
- C. This means the task should be abandoned and reverted to fully manual job-ticket creation
- D. This means extended thinking must be enabled to make the process more cost-efficient over time

**Answer:** A — Rising cost specifically on a simple, high-volume, unchanged-volume task points directly to a tier/configuration mismatch as the first thing to check, before assuming external pricing changes (B), abandoning the workflow (C), or — notably — assuming that *enabling* extended thinking (D, which typically increases rather than decreases cost) would somehow improve cost efficiency.

---

### Q97.
An enterprise-software company's technical-writing team has iterated six times over two weeks on a Claude-assisted API-documentation-generation workflow, with each round's feedback being some version of "this is close, just needs to be a bit more accurate about the parameter descriptions." Accuracy issues persist each round despite this repeated feedback.
**Options**
- A. This means a seventh round of the same style of feedback ("be more accurate") is likely to finally succeed, given how close previous rounds have been
- B. Six rounds of the same category of vague feedback ("be more accurate") failing to resolve a specific, recurring issue (parameter-description accuracy) suggests the feedback itself needs to become concrete and specific (e.g., pointing to the exact source-of-truth for parameter definitions, such as the actual API schema file, and requiring direct sourcing from it) rather than repeating the same general directive
- C. This means the underlying task (API documentation generation) is fundamentally unsuited to AI assistance
- D. This means the team should switch to manually writing documentation for parameter descriptions specifically, while keeping AI assistance for the rest of the document

**Answer:** B — This extends the "vague iteration feedback is itself under-specified" principle to a repeated-failure pattern: six rounds of the same non-specific feedback category is a signal to make the *next* feedback concrete and sourced (e.g., point directly at the schema file), rather than expect a seventh vague repetition to somehow succeed (A), or conclude the whole task type is unsuited (C) or needs manual carve-out (D) without first trying genuinely specific feedback.

---

### Q98.
A national retailer's loyalty-program team optimized their AI-assisted personalized-offer generation workflow primarily for "offers generated per hour," successfully tripling output volume. Three months later, redemption rates for AI-generated offers are measurably lower than for the smaller volume of offers the team previously generated manually.
**Options**
- A. Continue optimizing for volume, since the redemption-rate decline may simply reflect market conditions unrelated to the workflow change
- B. Reconsider the optimization target: for a workflow whose actual business purpose is driving redemptions (not merely producing offers), optimizing for raw generation volume without regard to redemption quality may have traded away the metric that actually mattered — the workflow should likely be re-optimized toward offer relevance/redemption rate, even if that means somewhat lower raw volume
- C. Continue optimizing for volume, since a threefold volume increase is a clear, demonstrable success regardless of redemption rate
- D. Abandon AI assistance for offer generation entirely and revert fully to the manual process

**Answer:** B — This is a harder version of "optimize for the metric that actually matters": raw volume was successfully optimized, but it wasn't the metric that mattered for the workflow's actual business purpose (driving redemptions) — the fix is re-targeting the optimization, not assuming external causes (A), declaring volume success sufficient regardless of the business outcome (C), or overcorrecting to full abandonment (D).

---

### Q99.
A metropolitan transit agency's service-alert drafting workflow has used the identical prompt template for two years without issue. This month, several drafted alerts have contained outdated route numbers that were renumbered in a system-wide route overhaul four months ago.
**Options**
- A. Since the prompt template is unchanged, this must be a sudden and unexplained model-capability regression
- B. Check whether a reference document or knowledge source listing route numbers (used to inform the drafting workflow) was updated to reflect the four-month-old route overhaul — an unchanged prompt combined with a real-world data change (the overhaul) four months ago, only now surfacing as errors, points to a stale reference source rather than the prompt or the model itself
- C. This means the drafting task should be moved to a more capable model tier immediately
- D. This means the prompt template needs to be rewritten to explicitly mention the new route numbers each time

**Answer:** B — An unchanged prompt ruling out prompt-based causes, combined with a specific, dateable real-world change (the route overhaul) that precedes the errors, points clearly to a stale knowledge/reference source that was never updated after that change — not a sudden model regression (A), a capability issue (C), or a prompt rewrite (D) that would need constant manual updating rather than fixing the actual stale source once.

---

### Q100.
A specialty food distributor's finance team has a Claude-assisted monthly rebate-calculation workflow that computes rebate amounts owed to retail partners via code execution, with a finance analyst reviewing and approving the computed rebate file before payments are released. A new efficiency proposal suggests removing the analyst's review step specifically for retail partners whose rebate calculation has matched the prior month's amount within 1%, "since a near-identical result to last month is itself evidence of correctness."
**Options**
- A. Approve the proposal — a near-identical result to a previously-approved, correct calculation is meaningful corroborating evidence that this month's calculation is also likely correct
- B. Do not approve: a rebate amount matching the prior month closely is consistent with correctness, but it is equally consistent with the calculation having silently used stale prior-month inputs (e.g., an outdated sales-volume figure) rather than genuinely correct current-month data — similarity to a prior result is not the same kind of evidence as independent verification against current source data, and the review step (and the reversibility/accountability it provides before payment) should be retained regardless of how closely results happen to track month to month
- C. Approve the proposal, but only reinstate the review step if the match tolerance is tightened from 1% to 0.1%
- D. Approve the proposal, but require a lighter-touch review (a quick glance rather than full verification) for the matching partners instead of removing review entirely

**Answer:** B — This is a deliberately tricky closing question because "matches last month" sounds like a form of the known-answer verification principle, but it's actually the opposite: it's an untested assumption that stability implies correctness, when stability could just as easily result from a silent input error (e.g., accidentally reusing last month's sales figures) — reversibility/accountability at the payment-release point is what the review step actually protects, independent of how similar results happen to look, and neither a tighter tolerance (C) nor a lighter-touch review (D) addresses that the similarity itself proves nothing about correctness.

---
[⬅ PCAO-F Index](README.md) · [Companion set: `pcaofexamquiz.md`](pcaofexamquiz.md)
