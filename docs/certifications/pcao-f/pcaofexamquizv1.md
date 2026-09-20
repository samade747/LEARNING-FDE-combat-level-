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
- A. Keep a human checkpoint despite the benchmark: a known-answer test earns confidence for similar future cases, not a transfer of accountability for a hard-to-reverse fraud freeze.
- B. Retire manual review only for the 38 case types the model got right, keeping humans on the other 2 case types
- C. Raise the benchmark threshold to 99% before considering retiring manual review
- D. Retire manual review — the model has now been rigorously benchmarked and measurably outperforms the human baseline

**Answer:** A — Beating a human accuracy baseline on a known test set is genuine, useful evidence, but it answers a *capability* question, not the separate *accountability* question. A consequential, hard-to-reverse action (freezing an account on a fraud call) still needs a human checkpoint regardless of how favorable the benchmark looks — accuracy numbers, however good, don't transfer responsibility to the tool. (A trap in this question: the 95%-vs-91% comparison is real and relevant to trust in the model's *capability*, but it is being used to justify the wrong conclusion — removing accountability rather than earning it for similar work.)

---

### Q2.
An urban-planning associate asks Claude why a proposed transit line will increase ridership more than a proposed bus-rapid-transit corridor, framed exactly that way, and gets a confident, well-cited case. A colleague, working on the competing option, asks why the bus corridor will increase ridership more than the transit line, and gets an equally confident, well-cited case with different citations. Both cite real-sounding but different studies.
**Options**
- A. This is normal model variability and no further action is needed
- B. This is hallucination: the model invented the studies cited in at least one of the two answers
- C. This is context contamination: the second associate's chat inherited framing from the first
- D. It is sycophancy from leading framing: each question presupposed its answer, so the real test is whether the cited studies themselves check out.

**Answer:** D — The core pattern is leading-question sycophancy, but the harder distinction here is that this doesn't yet prove hallucination (B) — the studies could be real but selectively chosen. The correct next step implied by D is to verify the underlying citations independently, not just diagnose the sycophancy pattern and stop.

---

### Q3.
An asset-management analyst asks Claude to summarize a fund's Q3 performance letter for a client memo. The summary states a "6.2% net return, outperforming the benchmark by 140 basis points," phrased confidently, and separately restates the return once more later in the same summary as "6.2% net return, 110 basis points ahead of benchmark."
**Options**
- A. Use whichever basis-point figure appears first in the summary, since first mentions are usually most reliable
- B. Treat the 140 vs 110 bps contradiction as a hallucination signal and verify both figures against the original letter before using either.
- C. Use the 6.2% figure, since both restatements agree on the headline return number
- D. Average the two basis-point figures (125 bps) as a reasonable compromise

**Answer:** B — Two different figures for the *same underlying comparison*, restated within one document, is a specific and reliable hallucination signal — the fact that the headline return agrees doesn't resolve the contradiction in the derived comparison. Averaging or picking one arbitrarily are exactly the wrong instincts; the source must be checked.

---

### Q4.
A national retailer runs an AI-assisted returns-fraud flagging system across 5,000 weekly returns, auto-approving refunds for the ~4,200 not flagged and routing the ~800 flagged ones to a specialist team. The specialist team, reviewing all 800 flagged cases carefully each week for a month, finds the flagging consistently accurate — false-positive rate under 3%.
**Options**
- A. This four-week track record is sufficient; the flagging logic can now run with lighter specialist review going forward
- B. Ask the assistant to self-report its estimated false-negative rate and adjust routing based on that figure
- C. Increase the flagging threshold so more cases get routed to the specialist team, improving overall safety
- D. Also sample the much larger unreviewed auto-approved group: a low false-positive rate on the flagged side says nothing about false negatives among the unflagged.

**Answer:** D — A well-verified flagged subset can coexist with a badly-performing unflagged majority; the false-positive rate measured on the reviewed side gives no information about the false-negative rate on the unreviewed side. This is the systemic-triage-risk pattern in its harder form: the flagged side looking clean is precisely what makes the unflagged side easy to overlook.

---

### Q5.
A corporate-law associate asks Claude to extract every indemnification obligation from a 90-page acquisition agreement, and the output lists nine obligations, each with a clause citation and a one-line quote. The associate opens three citations at random; all three quotes match the cited clauses exactly.
**Options**
- A. Re-run the extraction once more and accept the list only if the second run also produces nine obligations
- B. Ask Claude whether the list of nine is complete, and accept its answer if confident
- C. Confirm the remaining six citations too: a verified partial sample doesn't rule out fabrication in the unchecked portion of a hard-to-reverse extraction.
- D. The matching sample of three is sufficient confirmation for a document of this length and stakes

**Answer:** C — Three correct citations build confidence in *those three*, not in the remaining six or in the completeness of the list overall (a tenth, unlisted obligation is exactly the kind of omission that spot-checking existing entries cannot catch). For a high-stakes legal extraction, full verification — not partial sampling or self-report — is warranted.

---

### Q6.
A manufacturing quality team has Claude draft a root-cause analysis for a defect batch, then, in the same conversation, asks Claude to "review this analysis as a skeptical outside auditor would." Claude's "auditor" pass raises two additional concerns and revises its confidence downward.
**Options**
- A. This is unnecessary, since the auditor persona already found two concerns, proving the check worked
- B. It shares the same model and context: a persona reframes the self-check without making it independent; a separate human or data check is still needed.
- C. This satisfies independent verification, since Claude explicitly adopted an adversarial, skeptical persona
- D. This satisfies independent verification only if the persona pass happens in a new chat

**Answer:** B — An adversarial persona prompt improves the *thoroughness* of a self-review but does not create genuine independence — same model, same blind spots, same training data. It can surface some issues (as it did here) while still missing others systematically shared with the original pass.

---

### Q7.
A construction-supplies distributor's finance team receives a Claude-built margin-analysis spreadsheet built from raw invoice exports. Every product line shows a margin percentage; the formulas are visible in the cells and check out correctly for the ten rows the associate spot-checked. The spreadsheet will set which product lines get discontinued.
**Options**
- A. Recompute all totals manually as a full duplicate check, since a business-critical decision warrants full manual redundancy regardless of how the first pass was built
- B. Ask Claude to re-verify its own formulas and confirm no line was missed
- C. Since the visible formulas check out for the sampled rows and the computation was done via code/formulas rather than prose, no further check is needed before the discontinuation decision
- D. Confirm which source rows and invoice ranges fed the unsampled lines' totals: a wrong reference range is a distinct failure that spot-checking formulas misses.

**Answer:** D — This is a harder, more specific version of the "verify computation" principle: the formulas themselves being correct doesn't guarantee they were applied to the *correct source range* for every line — a wrong reference is a separate error mode from a wrong formula, and spot-checking the formula doesn't catch a wrong range on an unsampled row. A over-corrects into unnecessary full duplication once code/formulas are already being checked appropriately.

---

### Q8.
An executive search firm asks Claude and a second AI tool to independently score the same six finalist candidates for a CFO role against an identical rubric. The two tools agree closely on five candidates and diverge sharply on the sixth — one rates the candidate as the strongest overall, the other as the weakest.
**Options**
- A. Treat the sixth-candidate disagreement as the signal identifying which candidate needs deeper human evaluation; the five-candidate agreement is reassuring but non-decisive.
- B. Since five of six agree, treat the sixth divergence as noise and default to whichever tool has generally been more reliable historically
- C. Remove the sixth candidate from consideration entirely, since AI disagreement suggests unresolvable uncertainty
- D. Ask both tools to re-score the sixth candidate together in one shared conversation until they converge

**Answer:** A — The harder distinction here: agreement on most candidates doesn't validate the disagreement away, and it especially doesn't justify defaulting to "the historically more reliable tool" for the one case where they disagree — that's exactly the case needing independent human judgment, not a tie-break by track record.

---

### Q9.
A city government's records office asks Claude to confirm the current statutory retention period for a specific category of tax records. Claude cites "Revenue Code §14.3(b)" and states a seven-year period, matching what the associate already believed to be true from memory.
**Options**
- A. Ask a colleague whether seven years "sounds right" as an additional check
- B. Accept the figure, since statutory retention periods rarely change
- C. Since the cited figure matches the associate's own prior understanding, this corroboration is sufficient confirmation
- D. Confirm the citation against current statute text anyway: a result matching what you expected is where under-checking is most tempting, and confirmation adds no independent evidence.

**Answer:** D — Matching prior belief feels like corroboration but is not independent evidence — it's actually a moment of elevated risk, because the natural inclination to skip verification is strongest exactly when a claim confirms what's already assumed. The citation still needs to be checked against the actual current source.

---

### Q10.
A wholesale distributor's operations team has Claude reconcile 18 months of warehouse-scan data against supplier invoices in a single request, producing a discrepancy report. Weeks later, an auditor finds that a systematic unit-conversion error (cases vs. individual units) in one supplier's data caused every discrepancy involving that supplier to be miscalculated, and the error passed cleanly through the report's totals and flagged-exceptions list alike.
**Options**
- A. Decompose the process: profile each supplier's format and confirm units, verify that normalization independently, then run reconciliation and exception flagging on confirmed-consistent units.
- B. The fix is to have Claude flag any numbers that "look unusual" as a final review step
- C. The fix is to re-run the same single-pass request on a more capable model, since a stronger model would catch a unit mismatch
- D. The fix is simply to add "double-check unit conversions" to the same single-pass prompt for future runs

**Answer:** A — The systemic error occurred at an early, unverified step (unit normalization) and then propagated invisibly through everything built on top of it. Verifying that specific intermediate step before building the exception report on top of it is what prevents this — added carefulness wording, a bigger model, or a vague "flag anything unusual" instruction don't address the structural gap.

---

### Q11.
An environmental consultancy has Claude summarize a 250-page site-remediation report for a client briefing. The summary is fluent, well-structured, cites specific page numbers for each claim, and every citation the associate spot-checks (4 of 15 claims) matches the source page correctly.
**Options**
- A. Spot-check the remaining 11 claims as well, which fully resolves the concern
- B. This sampling result is sufficient given the citation-matching discipline shown
- C. Ask Claude to rate its own summary's technical accuracy on a 1–10 scale and treat a high score as sufficient
- D. Have someone with remediation expertise judge whether the summary's characterization of the findings is credible; a fluent, accurately cited summary can still mischaracterize severity.

**Answer:** D — This is the harder version of the "fluency isn't accuracy" principle: even with citations that check out (ruling out simple hallucination), a technically fluent summary can still misrepresent severity, risk, or context in ways that only a domain expert — not more citation-checking, and not a self-rating — would catch.

---

### Q12.
A national grocery chain's category team has Claude and a competing AI tool each independently forecast next quarter's demand for a seasonal product line, using identical historical data. Both forecasts land within 2% of each other.
**Options**
- A. Close agreement is only meaningful if the two tools are from genuinely unrelated vendors, which cannot be confirmed
- B. Close agreement should be treated as full proof, since two independently-built systems converging on the same figure is definitionally reliable
- C. Close agreement between independent tools is stronger than either one's self-reported confidence, but still no substitute for validating against a known-outcome period before high-stakes commitments.
- D. Close agreement between two AI tools using the same input data is not meaningfully different from one tool's self-reported confidence, since both tools may share the same blind spot in the historical data itself

**Answer:** C — The harder distinction: cross-model agreement using the *same input data* is weaker evidence than cross-model agreement built from independently gathered evidence (since both models could share a blind spot baked into that shared data) — but it is still meaningfully stronger than a single model's self-report, because two independent reasoning processes converging on the same output is not nothing. It remains a progress signal, not proof, ahead of a real financial commitment.

---

### Q13.
An ad agency's media-buying associate frames a request as: "This campaign's underperformance is clearly due to a weak creative — confirm that for the client report." Claude returns a confident analysis attributing underperformance to creative weakness, citing engagement metrics.
**Options**
- A. The framing presupposes the conclusion, and the cited metrics may have been picked to fit; ask instead for the strongest evidence for and against several causes.
- B. This is acceptable because engagement metrics are objective and cannot be selectively framed
- C. This is acceptable as long as the associate independently verifies the specific engagement numbers cited
- D. This is an acceptable evaluative process since real engagement metrics were cited in support

**Answer:** A — This is a harder version of the leading-question trap: real, verifiable metrics were cited, which makes the sycophancy less obvious than a purely fabricated claim, but the fundamental issue remains — the question told the model which conclusion to build a case for, and metrics can be true while still being cherry-picked to fit a presupposed answer.

---

### Q14.
A telehealth platform runs a Claude-assisted symptom-triage layer that has correctly matched licensed-nurse triage decisions in 970 of 1,000 audited historical cases (97%). Leadership proposes removing the nurse-review step for the lowest-acuity triage category specifically, which accounts for 60% of volume and had zero mismatches in the audit.
**Options**
- A. Approve a partial removal — a licensed nurse spot-checks 10% of the low-acuity category going forward instead of reviewing all of it
- B. Keep the nurse-review checkpoint for live triage: a clean retrospective audit doesn't remove a patient-safety checkpoint, and zero mismatches in one sample isn't zero risk.
- C. Approve the removal — zero mismatches in that specific high-volume category, within an already-strong overall audit, is sufficient justification
- D. Approve the removal only after the audit sample size doubles

**Answer:** B — This intentionally offers a very tempting "clean subgroup" (60% volume, zero mismatches) to test whether the test-taker still applies the underlying principle: patient-safety accountability doesn't transfer based on a favorable retrospective slice, no matter how clean that slice looks, and no matter how large the volume behind it is.

---

### Q15.
A commercial insurer's underwriting team has Claude flag policy applications for manual underwriter review based on risk indicators. Of 3,000 applications, 340 are flagged; the underwriting team reviews all 340 and finds the flagging judgment sound in every case. Separately, the team notices flagged applications disproportionately come from two specific ZIP codes relative to their share of total applicants.
**Options**
- A. Since every flagged case held up under review, the ZIP-code pattern is incidental and needs no further attention
- B. Quietly adjust the flagging criteria to reduce the ZIP-code concentration before anyone else notices
- C. Escalate the ZIP-code concentration to the compliance owner for fairness review: accurate individual flags can still form a disparate-impact pattern beyond the associate's call.
- D. Ask Claude whether its own flagging criteria are biased by ZIP code and rely on its answer

**Answer:** C — Individual-case accuracy and aggregate fairness are separate questions; a flagging system can get every single case "right" on its own terms while still producing a concentration pattern that deserves review by whoever owns fairness/compliance obligations — not a unilateral quiet fix, not a dismissal because case-level review passed, and not the model's own self-assessment.

---

### Q16.
A private equity associate has Claude build a comparable-companies valuation table from ten public filings. Every individual multiple (P/E, EV/EBITDA) that the associate spot-checks against the filings is correct. The table's *median* EV/EBITDA multiple, which will anchor a client-facing valuation range, is computed by Claude in the same response as prose ("the median across the ten comparables is 8.4x").
**Options**
- A. Accept the 8.4x median since the underlying individual multiples were confirmed correct
- B. Spot-check two more individual multiples for extra assurance before accepting the median
- C. Have the median and any other aggregate feeding the range computed by executable calculation shown against the confirmed multiples; correct inputs don't guarantee correct aggregation.
- D. Ask Claude to recompute the median and confirm it matches

**Answer:** C — This is the aggregation-error pattern at its most consequential: confirmed-correct individual inputs still don't guarantee a correctly computed aggregate (a median is easy to miscompute silently, e.g., averaging instead of taking the true middle value with an even count) — the aggregation step itself needs to be shown and verified, not inferred from correct inputs.

---

### Q17.
A media company's ad-sales associate needs Claude to help decide whether an underperforming campaign should continue. Which single request best supports an honest evaluation rather than a persuasive case for a predetermined conclusion?
**Options**
- A. "Rate this campaign's performance from 1–10 and explain the score."
- B. "Lay out the strongest case for continuing the campaign unchanged and the strongest case for pausing it, based only on the attached performance data, before any recommendation."
- C. "This campaign seems to be struggling — walk me through why."
- D. "Give me the strongest argument that this campaign should continue as-is."

**Answer:** B — Asking for both sides explicitly, grounded in the data, before any recommendation is what avoids presupposing an answer. D asks for one-sided advocacy; C's framing ("seems to be struggling") leads toward a negative conclusion; A invites a plausible-sounding score without necessarily surfacing the actual tradeoffs on both sides.

---

### Q18. *(Select TWO — all-or-nothing)*
A biotech company's regulatory-affairs associate is deciding which of five upcoming Claude-assisted tasks need a second, independent verification path beyond the associate's own read-through. Which **TWO** most clearly require it?
**Options**
- A. Calculating a dosage-conversion table that will be used directly in a patient-facing dosing chart
- B. Drafting a thank-you note template for conference attendees
- C. Summarizing a competitor's public press release for an internal slide
- D. Extracting adverse-event thresholds from a clinical protocol that will determine a trial's stopping rules
- E. Drafting talking points for an internal town hall about a recent product launch

**Answer:** A, D — Both feed directly into consequential, hard-to-reverse, safety/regulatory-relevant outcomes (trial stopping rules; patient dosing) where an error compounds badly and a second independent check is warranted. B, C, and E are low-stakes, easily-correctable internal or informational content.

---

### Q19.
A national law firm's e-discovery team has Claude review 40,000 documents and tag 1,100 as "privileged — withhold." Outside counsel reviews a random sample of 150 of the 1,100 tagged documents and confirms all 150 were correctly tagged privileged.
**Options**
- A. Ask Claude to re-scan the untagged documents and self-report its confidence that none were missed
- B. Increase the sample size on the withheld side to 300 for extra confidence, which resolves the concern
- C. This sample confirms the tagging system overall; proceed to withhold all 1,100 without further review
- D. The sample only confirms precision on the withheld side; sample the untagged 38,900 too before certifying the production complete and privilege-safe.

**Answer:** D — This is the systemic-triage-risk pattern applied to its highest-stakes form (privilege waiver risk in litigation): validating the flagged/withheld side, however thoroughly, says nothing about false negatives in the much larger unflagged side, which is exactly where an inadvertent privilege waiver would hide.

---

### Q20.
A regional airline's revenue-management team asks Claude to explain a fare-optimization recommendation. Claude's explanation is detailed, well-structured, and internally consistent, describing a chain of reasoning about competitor pricing and demand elasticity. The recommended fare change, if wrong, would be reversible within 24 hours by resetting fares.
**Options**
- A. Detailed, consistent-sounding reasoning must always be independently verified against real elasticity data before any action, regardless of reversibility
- B. No fare change should ever be made without first replicating the analysis on a second AI model, regardless of reversibility
- C. Because the action is reversible within 24 hours, implement the change now and monitor actual bookings as the check; low cost of error lowers the verification needed.
- D. The explanation's internal consistency is itself sufficient verification, regardless of reversibility

**Answer:** C — This question tests whether the test-taker over-applies verification rigor uniformly regardless of stakes/reversibility: for a low-cost-of-error, quickly-reversible action, real-world monitoring *is* a legitimate, proportionate verification path — the earlier, harder questions in this set involve irreversible or high-stakes actions specifically because that's where heavier verification is warranted, not as a universal rule for every AI-assisted decision.

---

### Q21.
A hospital's clinical-informatics team wants to validate a new Claude-assisted chart-summarization tool before wider rollout. Which validation approach most rigorously tests whether the tool can be trusted, as opposed to merely appearing trustworthy?
**Options**
- A. Run the tool twice on the same new chart and check whether the two outputs are consistent with each other
- B. Run the tool on past charts with known, physician-verified summaries withheld from it, and compare its output with that ground truth.
- C. Ask the tool to explain its own summarization methodology and have an informaticist judge whether the explanation sounds sound
- D. Have ten clinicians read a week's worth of new summaries and rate them "looks accurate" or "looks off"

**Answer:** B — This is the known-answer test at its clearest: comparing against an already-established, verified ground truth is fundamentally different from (and stronger than) a plausibility rating (D), a self-explained methodology (C), or self-consistency across repeated runs (A), any of which could be consistently wrong or consistently plausible-sounding without being correct.

---

## Domain 4 — Workflow Integration and Solution Design (16% — Q22–Q37)

### Q22.
A multinational manufacturer's plant-operations director says: "We want Claude handling our safety-incident intake so reports get filed faster." The director adds that "faster" is the main goal, since delayed filing has been the recurring complaint.
**Options**
- A. Ask the director to pick the AI tooling first, since the goal is already clear
- B. Still settle the other four task-definition elements: what is produced, for whom, from what data, in what format; a stated goal alone doesn't define the output.
- C. Since the goal (speed) is already stated, proceed directly to building a faster intake process around that stated goal
- D. Proceed directly, treating "reduce filing delay" as sufficient specification for a safety-critical workflow

**Answer:** B — This is a harder version of the task-definition trap: a stated *goal* (speed) is not the same as a full task definition. Four of the five settled-answers slots are still open, and for a safety-critical intake process, resolving them before building matters more than the presence of a clear-sounding goal.

---

### Q23.
A pharmaceutical distributor's cold-chain compliance workflow has Claude flag shipment temperature-log anomalies for a compliance officer, who then decides whether to quarantine the batch. A proposal suggests removing the compliance officer's decision step for anomalies below a certain severity threshold, "since Claude's severity scoring, based on code-executed threshold comparisons, is mathematically precise and has never been wrong in six months."
**Options**
- A. Keep the step, but let it be satisfied by an automatically generated confirmation email rather than an actual review
- B. Approve the removal below the threshold, since the severity math is both code-executed (removing computation risk) and has a clean six-month track record
- C. Keep the compliance officer's decision even below the threshold: quarantine is consequential and hard to reverse, and accountability doesn't transfer to a scoring formula.
- D. Remove the step only for the lowest 25% of severity scores, as a middle-ground compromise

**Answer:** C — This question specifically combines two tempting-but-insufficient justifications (code-executed precision AND a clean track record) to see whether the test-taker still separates the *computation-accuracy* question from the *accountability/reversibility* question — both being favorable doesn't change who is accountable for a quarantine decision.

---

### Q24.
A logistics company's proposal for an AI-assisted freight-routing tool states: "Routes will be optimized by the assistant, and a dispatcher reviews any route through a designated high-risk corridor before departure." A colleague argues this wording is already a complete, well-defined control.
**Options**
- A. The wording is incomplete because it doesn't name a specific dispatcher by name
- B. The wording is complete: it names the trigger condition (high-risk corridor) and implies a reviewer (dispatcher)
- C. The wording is complete and additionally should specify which AI model performs the routing
- D. It omits what the dispatcher checks (WHAT) and confirmation the review precedes departure (WHEN); naming a role and trigger isn't enough for a defined gate.

**Answer:** D — This is a harder application of the WHO/WHAT/WHEN gate test: the wording here already does more than the classic vague "a person will review" example (it names a trigger and a role), which makes it tempting to call complete — but it still hasn't specified the *specific risk* being checked for, which is what a truly audit-proof gate requires.

---

### Q25.
A five-branch credit union is redesigning its loan-document intake around Claude. Two changes are planned: consolidating four separate document-request emails into one, and moving repeated compliance-language requirements into a Project's standing instructions. Leadership wants a "processing time reduced by X%" figure for the board within two weeks, and the team is tempted to estimate the improvement now to hit that deadline.
**Options**
- A. Report the combined, undifferentiated impact of both changes together as a single figure, without needing a pre-change baseline, since board members care about the end result
- B. Provide a reasoned estimate now to meet the board deadline, and correct it later once real data comes in
- C. Make the two planned changes immediately, then measure only the new process, comparing it against last year's informal recollection of typical processing time
- D. Measure the unchanged process for a short window to get a real baseline, even if the figure arrives late, rather than presenting an estimate as measured.

**Answer:** D — This raises the stakes on the baseline-before-optimizing principle by adding real organizational pressure (a board deadline) as a reason to skip it — the correct answer holds that measuring first is still right even when it conflicts with a deadline, rather than substituting an estimate or an undocumented "last year, roughly" comparison.

---

### Q26.
A national insurer connected its claims-document folder to Claude in read-only mode to summarize incoming claims. A new initiative wants Claude to also tag each claim folder with a standardized status label (e.g., "pending," "closed") directly in the folder system, visible to all claims staff.
**Options**
- A. This should be solved by building a Skill that defines the tagging logic, since read access plus clear logic is sufficient
- B. This is achievable today since read access lets Claude see and reason about folder structure and status
- C. Applying a status tag is a write action: it must be granted deliberately, after confirming the connector supports it, separate from the read-only summarization access.
- D. This requires no connector change, since folder tags are metadata rather than file content

**Answer:** C — This question specifically tests whether "just a label/tag" (which sounds lighter than moving or deleting files) is still correctly recognized as a write action requiring deliberate, confirmed permission — the answer is yes, regardless of how minor the specific write operation seems.

---

### Q27.
A hospital system's discharge-summary workflow has five steps. Step 3 (drafting the summary) and Step 4 (a physician co-signing it) are both currently classified as "collaborative." A quality-improvement lead proposes reclassifying Step 3 alone as "AI-appropriate" (no collaborative flag) since Step 4's physician co-sign already exists as a downstream safeguard.
**Options**
- A. Approve the reclassification only if Step 4's co-sign becomes mandatory rather than optional
- B. Do not approve: Step 3 should be classified on its own reversibility, stakes and accountability, not because a later gate exists that may be removed or rushed.
- C. Approve the reclassification — Step 4's existing safeguard makes Step 3's own collaborative flag redundant
- D. Approve the reclassification, but only for low-complexity discharge cases

**Answer:** B — This tests a subtler version of the delegation-map principle: each step's classification should stand on its own reversibility/stakes/accountability analysis; using a *different* step's safeguard to justify loosening this step's classification creates a fragile dependency where a later change to Step 4 silently removes the only remaining check on Step 3.

---

### Q28.
An investment bank's associate describes an AI-assisted trade-reconciliation workflow in three versions. The version for the trading desk head says: "Claude flags mismatched trades daily; a reconciliation analyst confirms and resolves each flag before end-of-day close." The version for the audit committee omits the phrase "before end-of-day close" but otherwise matches.
**Options**
- A. This omission is acceptable because audit committees focus on outcomes, not process timing
- B. It drops the detail an audit-facing description most needs, WHEN (before an irreversible cutoff), since auditors care whether the control operates before risk crystallizes.
- C. This omission is only a problem if the actual process timing ever changes
- D. This omission is acceptable, since the audit committee version still mentions the analyst confirming and resolving each flag

**Answer:** B — This is a harder version of "don't drop the human checkpoint" — here the human role (analyst) is still mentioned; what's silently dropped is the *timing* element (before close) that turns "a human checks it" into an actual pre-crystallization control, which matters most to exactly the audience (audit) being shown this version.

---

### Q29. *(Select TWO — all-or-nothing)*
A regional airline is expanding an AI-assisted crew-scheduling exception workflow. Which **TWO** of the following five proposed changes would leave the system with more authority than its risk profile allows?
**Options**
- A. Let Claude draft the rationale for each rest-period exception request, with a named crew-scheduling manager required to approve or reject before it takes effect
- B. Let Claude auto-approve crew rest-period exceptions below a regulatory minimum threshold when historical approval rates for similar requests exceed 98%, without human sign-off
- C. Have a scheduling coordinator approve 40 daily exceptions by glancing at Claude's one-line summaries, without opening any case, to meet a same-day cutoff.
- D. Move the rest-period regulatory-threshold lookup into a Skill so it's applied consistently across all schedulers
- E. Use Claude to compute optimal crew rotations via code execution, with the existing scheduling-manager approval gate unchanged and immediately following

**Answer:** B, C — B directly automates a regulatory, safety-relevant exception based on a historical approval rate rather than an actual case-by-case decision (the approval rate does not make an individual exception automatically safe). C keeps a human "in the loop" in name only — approving 40 cases from one-line summaries without opening any case file is a rubber stamp, not a real review. A, D, and E all preserve substantive human decision-making at the point that matters.

---

### Q30.
A city's public-works department drafts a single internal memo explaining why a road-resurfacing project ran over budget. The memo needs to reach the city council (who approve the next budget cycle) and the resurfacing crew (whose work-order process is changing as a result).
**Options**
- A. Ask Claude to produce a "balanced, general-audience" version suitable for both, to save review time
- B. Produce one rewrite per audience, each organized around what that specific audience needs to decide or do next, rather than adapting tone alone on a single shared draft
- C. Keep one memo but add a short "for council" and "for crew" heading to each relevant section within it
- D. Send the identical memo to both audiences, since the underlying facts (why it ran over budget) don't change between audiences

**Answer:** B — Even though C looks like a reasonable middle ground (headers separating audience-relevant sections within one document), it still doesn't restructure the content around what each specific audience needs to *decide or do* — a council needs budget-cycle-relevant framing to approve funding; a crew needs operational, work-order-relevant framing to change practice. A genuinely separate rewrite per audience, not a labeled single document, is what the harder version of this principle requires.

---

### Q31.
A specialty pharmacy chain has Claude extract every controlled-substance handling requirement from a new state regulation and an internal compliance memo. The output is a clean list of 24 requirements. Before pharmacists begin retraining based on this list, which single next request best protects against a missed obligation?
**Options**
- A. Ask Claude to cross-check the 24 requirements against a general industry best-practices summary for completeness
- B. Have Claude summarize the state regulation and the internal memo separately, and manually compare the two summaries side by side
- C. Ask for the list reorganized by urgency, so the pharmacy team tackles the most time-sensitive requirements first
- D. For each of the 24 requirements, add its exact source, whether the two sources agree, and whether it's ambiguous enough for a compliance question, surfacing hidden conflicts.

**Answer:** D — This is a harder version of the traceability principle: with *two* source documents involved, the highest-value addition is surfacing whether they actually agree with each other on each requirement (not just tracing each item to *a* source), since a silent conflict between the regulation and the internal memo is exactly the kind of gap reorganizing by urgency (C) or a general industry comparison (A) would not surface.

---

### Q32.
A national moving company's operations associate delegates: build a truck-loading sequence plan for a specific multi-stop route, given stated stop order, weight limits per stop, and a stated instruction that Claude may reorder stops for efficiency but must flag any such reordering. In the output, Claude reorders two stops for efficiency and clearly flags the change — but also silently substitutes a different, unstated weight-distribution method than the company's standard practice, without flagging that substitution.
**Options**
- A. It anticipated one kind of discretion but not another (weighting method); broaden 'flag when you decide' to any meaningful methodological choice.
- B. This is a context-overload issue, since the request had multiple constraints
- C. This is a hallucination, since the weight-distribution method wasn't in the source data
- D. The original instruction was sufficient, since the reordering (the anticipated type of discretion) was correctly flagged

**Answer:** A — This is a harder version of the "say when you decide" principle: the instruction worked exactly as designed for the anticipated discretion (reordering) but didn't generalize to an unanticipated category of silent choice (methodology substitution) — the fix broadens the flagging instruction's scope rather than concluding the original instruction failed outright.

---

### Q33.
A university's research-data office has consent-based access to sensitive survey data collected for a specific longitudinal health study. A separate research team, studying an unrelated topic, requests that the same dataset (already sitting in an approved Claude workspace for the original study team) be analyzed for their unrelated project, arguing "it's already inside the approved system, so no new access step is needed."
**Options**
- A. Approve the request only if the second team's project is also health-related
- B. Approve the request, but only if the second team anonymizes all identifiers first
- C. Take it to the data or consent owner: consent for one study doesn't cover an unrelated project just because the data sits in an approved environment.
- D. Approve the request, since the data is already inside an approved, secured workspace regardless of which team or project uses it

**Answer:** C — Being inside an approved workspace addresses data security, not purpose limitation; consent for a specific study's use does not automatically extend to a different project, however secure the storage, however anonymized the eventual output, or however topically adjacent the new project seems.

---

### Q34.
An AI-assisted vendor-risk scoring tool at a manufacturing conglomerate appears to consistently score vendors headquartered in one particular country higher-risk than vendors with comparable financials headquartered elsewhere. The procurement associate who noticed this does not own vendor-risk policy, but does own the day-to-day scoring workflow.
**Options**
- A. Since the associate owns the workflow, quietly adjust the scoring inputs to remove the apparent geographic skew before anyone else notices
- B. Ask the tool directly whether its scoring is geographically biased, and act only if it confirms bias
- C. Work through who is affected and what could go wrong, then escalate to the vendor-risk policy owner; running the workflow isn't authority to redefine its criteria.
- D. Since it's outside the associate's ownership entirely, take no action and let the pattern continue until someone else notices

**Answer:** C — Owning the day-to-day operation of a workflow is distinct from owning the authority to change its underlying risk criteria — a harder distinction than the more general "escalate fairness concerns" pattern, since it specifically separates *operational* ownership from *policy* ownership, and the associate has the former but not the latter.

---

### Q35.
A regional hospital network wants to establish whether a new Claude-assisted nurse-staffing recommendation tool can be trusted before wider rollout across its 12 facilities. The tool has performed well in a 3-week pilot at the single facility that helped design it.
**Options**
- A. This pilot result establishes sufficient trust for network-wide rollout, since it was a real, multi-week test with real staffing decisions
- B. Roll out network-wide immediately, monitoring closely for the first month as the real-world check
- C. Extend the pilot at the same single facility for another 3 weeks before deciding
- D. Test against known-answer staffing decisions from other facilities, not only the design site, before treating the pilot as evidence it generalizes.

**Answer:** D — This is a harder version of the known-answer test: a favorable pilot at the facility that helped *design* the tool doesn't establish that the tool generalizes to other facilities with different patient populations, staffing patterns, or shift structures — the correct next validation step tests against a *different* known-answer context, not just a longer test in the same one.

---

### Q36.
A specialty foods distributor redesigns its supplier-onboarding workflow around Claude. Six months in, an audit finds the redesigned process is measurably faster (a 45% reduction in onboarding time) but that two suppliers were onboarded despite missing a required food-safety certification, which the workflow's document-checklist step should have caught.
**Options**
- A. Add a note to the two affected supplier files acknowledging the gap, and continue monitoring without further workflow changes
- B. Re-examine the checklist step for a structural gap, such as checking document presence but not validity, rather than treating two missed certifications as unrelated one-offs.
- C. Since the overall time-reduction goal was met, treat the two missed certifications as isolated errors to be corrected individually, with no workflow change needed
- D. Revert the entire redesigned workflow back to the original manual process, since any compliance miss invalidates the redesign

**Answer:** B — When speed was gained but a compliance-critical check specifically failed, the right move is investigating whether that specific step has a structural gap (not whether the redesign overall succeeded) — the earlier baseline-first principle established that outcomes should be measured before optimizing; this question extends it: when a *specific* compliance-relevant metric fails despite overall success, that specific step needs re-examination, not a blanket revert or two isolated corrections.

---

### Q37.
A logistics-software company writes three descriptions of an AI-assisted invoice-matching workflow — for the engineering team, for the CFO, and for a prospective enterprise client's procurement team. The client-facing version states: "Our AI-assisted system reconciles 95% of invoices automatically, with the remainder routed to a trained specialist for review before payment release."
**Options**
- A. This version is fine, since specialist review of the remainder is the only checkpoint that legally needs disclosing
- B. It doesn't say what 'automatically' means for the 95%: whether lighter verification still applies before payment, since a client may read it as no verification at all.
- C. This version is appropriately pitched for a prospective client and correctly preserves the human checkpoint
- D. This version should be simplified further for a sales audience by removing the 95%/remainder breakdown entirely

**Answer:** B — This is a harder version of "don't let the audience believe there's no gate": the human checkpoint is disclosed, but the boundary of what counts as "automatic" (does the 95% get *any* verification, or none) is left genuinely ambiguous in a way a client evaluating risk would reasonably want clarified — technically true statements can still create a misleading impression through what they leave undefined.

---

## Domain 6 — Governance, Risk, and Responsible Use (15% — Q38–Q52)

### Q38.
A multinational retailer's e-commerce team wants Claude to auto-generate personalized discount offers based on a customer's purchase history and a predicted "price sensitivity" score. The predicted score uses a customer's shipping ZIP code as one of several inputs, alongside purchase frequency and average order value.
**Options**
- A. This is inappropriate for any AI involvement, since any use of geographic data in pricing is impermissible
- B. This is appropriate-with-review, but only because of the purchase-history component, not the ZIP code
- C. Appropriate with review because ZIP code can proxy protected characteristics; the review must check for disparate impact in who gets better offers, not just effectiveness.
- D. This is fully appropriate with no review needed, since discount personalization is a routine marketing function

**Answer:** C — The harder distinction: ZIP code is a commonly-used, seemingly neutral input that carries real proxy-discrimination risk in pricing/offer contexts — the review needs to specifically examine *that* input's disparate-impact potential, not treat the workflow as routine (D), ban geography outright (A, an overcorrection), or focus review only on the more obviously "personal" input while ignoring the riskier one (B).

---

### Q39.
A national law firm's associate can't determine from firm policy whether client conflict-check summaries generated with AI assistance need to be logged as "AI-assisted" in the firm's conflicts database, given that the firm recently onboarded a new practice group with different internal conventions. The associate escalates to the firm's general counsel.
**Options**
- A. The process, the specific ambiguity about the new practice group's logging requirement, and the one open question, without a recommendation the associate lacks authority to make.
- B. A request to pause using AI assistance for conflict checks in the new practice group until the question is resolved, without further detail
- C. "I've reviewed the situation and my recommendation is to log all future conflict summaries as AI-assisted going forward — please approve."
- D. A description of the general benefits of AI transparency in legal practice, with a request for general guidance

**Answer:** A — This is a harder version of the escalation-quality principle: C looks helpful (a specific recommendation) but oversteps — the associate doesn't have the standing or full context to decide firm-wide logging policy, and a baked-in recommendation can anchor the general counsel's decision inappropriately. The correct escalation gives facts and the specific open question, without pre-deciding it.

---

### Q40.
A boutique wealth-management firm's compliance officer reviews a proposal to let Claude draft — but never send without human approval — personalized client-portfolio commentary that references specific holdings performance. After 18 months of clean operation with 100% human sign-off maintained throughout, a partner proposes: "Given the perfect track record, let's remove the requirement that the compliance officer specifically checks for any forward-looking performance language, since the reviewing advisor already reads the whole thing anyway."
**Options**
- A. Approve the change, but require the compliance officer to spot-check 20% of commentary going forward instead
- B. Approve the change — an 18-month clean record plus an existing general reviewer (the advisor) makes the additional compliance-specific check redundant
- C. Do not approve: dropping the specific forward-looking-language check because a general reviewer exists conflates two kinds of review that aren't substitutes.
- D. Approve the change, but only for clients below a certain account size

**Answer:** C — This question layers two tempting justifications (a long clean track record AND an existing general reviewer) to test whether the test-taker still recognizes that a *specific, named* risk check (forward-looking language, a known regulatory issue) is not satisfied by a *general* review happening for other reasons — the two checks serve different purposes even when performed by different people reading the same document.

---

### Q41.
A consumer-electronics company's employees have started using a personal, consumer-grade AI voice-transcription app during customer-support calls to draft call summaries, because the approved support platform's built-in summarization feature frequently times out on longer calls. Call summaries reference customers' names, purchase details, and sometimes partial payment information mentioned during troubleshooting.
**Options**
- A. Approve continued use of the consumer app for now, since it solves a real, currently-unaddressed problem
- B. Report the timeout gap to the policy owner and work around the approved tool's limit, keeping the consumer app off calls with payment or personal data.
- C. Ban all call summarization, AI-assisted or otherwise, until a long-term platform fix is implemented
- D. Immediately discipline any employee found using the unapproved app, since customer payment information is involved

**Answer:** B — This is a harder version of the capability-gap pattern specifically because it involves payment information (higher stakes than the earlier photograph-based example), which makes both extremes (ignoring the gap by disciplining, or accepting the workaround by approving it) clearly wrong — the correct answer still centers on fixing the actual gap while closing the risky workaround for the highest-risk call types immediately.

---

### Q42.
A regional nonprofit's development team uses an AI assistant's incognito/temporary-chat mode for all donor-prospect research conversations "to avoid cluttering our shared account's history." Separately, they've been told an upcoming grant-compliance audit will require records of what tools and data sources were used to identify major-gift prospects.
**Options**
- A. Incognito/temporary mode is irrelevant to the audit either way, since audits only examine data sources, not AI tool usage patterns
- B. Incognito/temporary mode fully satisfies data-minimization best practice and also happens to solve the audit-readiness question
- C. Incognito is reasonable: it affects only the tool's history and memory, not the organization's record-keeping obligations, which its own process must meet.
- D. Incognito/temporary mode should be avoided entirely for donor research, since it prevents the audit from ever being satisfied

**Answer:** C — This is a harder, more nuanced application of the incognito/temporary-mode principle from the earlier "nothing on record" scenario type: here, unlike a plan to *evade* an audit, the team's goal is legitimate (tidiness), and the correct answer recognizes that private-chat modes affecting the *tool's own* history/memory is a separate question from the *organization's* own obligation to keep independent records for compliance — the audit-readiness gap, if any, isn't created or solved by the chat mode itself.

---

### Q43.
A property-insurance carrier's claims department wants Claude to draft an initial coverage determination (approve/deny/investigate further) for straightforward, low-dollar-value claims (under a defined small threshold), with a licensed adjuster required to countersign every determination before it's communicated to the policyholder.
**Options**
- A. Appropriate with review: WHO (licensed adjuster), WHAT (the coverage determination) and WHEN (before the policyholder is told) are defined; keep the low-dollar limit absent fresh review.
- B. Fully appropriate with no review needed, given the low-dollar threshold already limits exposure
- C. Appropriate-with-review, but the adjuster's countersign should be replaced by a second AI review pass for efficiency, given the low-dollar threshold
- D. Inappropriate for any AI drafting involvement, since coverage determinations are inherently high-stakes regardless of dollar value

**Answer:** A — This question is designed so that A initially looks like a simple "yes, this satisfies the WHO/WHAT/WHEN gate" answer, but the harder, complete version of the correct answer also flags that the dollar-threshold scope is load-bearing — if that threshold silently expands later without a fresh review of the gate's adequacy at higher stakes, the original appropriate-with-review classification would no longer hold.

---

### Q44.
A staffing agency's AI-assisted candidate-matching tool has operated for two years with strong placement-success metrics. A new client asks the agency to also use the tool to auto-reject candidates who don't meet a client-specified "cultural fit" criterion, described only as "someone who'll mesh well with our fast-paced, high-energy team."
**Options**
- A. Decline 'cultural fit' as a vague auto-reject criterion: it risks proxying protected characteristics, so escalate to compliance for fairness review and a concrete definition first.
- B. Proceed, but only auto-reject candidates who fail the criterion by a wide margin, using a numeric confidence threshold
- C. Proceed, but require a recruiter to review only the candidates who were auto-rejected, not those who passed
- D. Proceed, since the underlying matching tool already has a strong two-year track record

**Answer:** A — The tool's general track record on unrelated matching criteria doesn't validate a *new*, vague, and specifically risky criterion — "cultural fit" phrased this way is a well-known proxy-discrimination risk pattern in hiring, and it needs its own compliance review and concrete redefinition, not a numeric confidence threshold (B) or partial review (C), neither of which addresses the vagueness/proxy risk itself.

---

### Q45.
A hospital's IT governance committee is reviewing an AI vendor's claim that its clinical-documentation assistant "has been validated as safe and effective" based on the vendor's own internal testing, with no independent third-party validation performed. A committee member argues that since the vendor is a reputable, established company, the validation claim can be accepted as-is.
**Options**
- A. Accept the claim only if the vendor provides a written summary of its testing methodology
- B. Reject the vendor outright, since any company claiming its own product is "safe and effective" should be presumed to be overstating
- C. Treat the vendor's testing as informative but not independent: like a model's self-report, a vendor's self-report needs an independent validation path before clinical deployment.
- D. Accept the claim, since reputable vendors have strong incentives to be truthful about safety validation

**Answer:** C — This extends the independent-verification principle from model outputs to vendor claims about their own products: a vendor's reputation doesn't substitute for independent validation, and a written methodology summary (A) is still the vendor's own self-report, just in more detail — neither resolves the lack of independent verification, though outright rejection (B) also overcorrects past what the situation calls for.

---

### Q46.
A national grocery chain's loss-prevention team deploys an AI system that flags in-store customers for closer staff attention based on behavior-pattern analysis from security footage. After three months, an internal review finds flagged customers are disproportionately from one demographic group relative to store foot traffic, though the loss-prevention outcomes (actual theft caught) show no statistically significant demographic skew.
**Options**
- A. Escalate the flagging disparity to the fairness owner despite equal theft-catch rates: closer scrutiny is itself a disparate customer experience, separate from accuracy.
- B. Since actual theft-catch outcomes show no skew, the flagging pattern itself is not a problem worth escalating
- C. Discontinue the system entirely, since any demographic disparity in flagging is disqualifying regardless of context
- D. Adjust the system to equalize flagging rates exactly across demographic groups, regardless of underlying behavior-pattern data

**Answer:** A — This is a harder fairness question because the "outcome" metric (theft actually caught) looks clean, which makes it tempting to conclude there's no real problem — but the disparity in who experiences *being flagged and scrutinized* is itself a harm worth escalating, independent of whether flagged individuals turn out to be guilty at equal rates.

---

### Q47.
A community bank's small-business lending team uses Claude to draft loan-denial explanation letters required under fair-lending disclosure rules. The letters must state specific, accurate reasons for denial. An efficiency-focused branch manager proposes using a rotating set of five pre-approved, generic denial reasons "so the letters go out faster and more consistently."
**Options**
- A. Approve the approach, but require a compliance review of the five generic reasons once, when first created
- B. Approve the rotating generic-reasons approach, since consistency in letter format reduces legal risk
- C. Do not approve: fair-lending disclosure requires each applicant's actual, specific denial reason, and trading that accuracy for speed defeats the requirement's purpose.
- D. Approve the approach only for denials below a certain loan-amount threshold

**Answer:** C — This scenario intentionally frames the shortcut around desirable-sounding goals (speed, consistency) to see whether the test-taker still recognizes that some outputs (like a legally-required, applicant-specific disclosure) have accuracy as their entire point — no threshold (D) or one-time review (A) fixes a design that structurally can't produce applicant-specific accurate reasons.

---

### Q48.
A logistics company's compliance team is deciding whether an AI-assisted customs-classification tool needs to disclose AI involvement to the customs broker who ultimately files declarations based on its suggested classifications. The tool's suggestions are always reviewed and can be overridden by a licensed customs specialist before filing.
**Options**
- A. Disclosure is unnecessary, since customs brokers don't need to know internal tooling used by their suppliers
- B. Disclosure is needed only if the specialist overrides the AI's suggestion, to explain the discrepancy
- C. No disclosure is needed, since a licensed specialist reviews every suggestion before it's used
- D. Disclosure to the broker is still appropriate: they rely on the output without knowing AI shaped it, and transparency is reasonable even when a human can override.

**Answer:** D — Human review/override capability addresses the accuracy-safeguard question but doesn't resolve the separate transparency question: whether someone relying on the output (the broker) has a reasonable interest in knowing AI was involved in shaping it, even when a human retained final judgment.

---

### Q49.
A regional healthcare system's telehealth platform proposes retaining full video-call recordings (not just AI-generated summaries) indefinitely "in case the AI summary is ever challenged and we need to verify against the original." The platform's current retention policy for the summaries themselves is 7 years, matching medical-record requirements; no policy currently addresses the underlying recordings.
**Options**
- A. Delete all recordings immediately after summary generation, since only the summary has an established retention policy
- B. Approve retention matching the 7-year summary policy, applied automatically to the recordings as well
- C. Escalate the retention question to the privacy policy owner first: indefinite retention of sensitive health video is a higher exposure than a 7-year text summary.
- D. Approve indefinite recording retention, since having the original available to verify a challenged summary is a reasonable, low-risk safeguard

**Answer:** C — The verification rationale (having the original if a summary is challenged) is reasonable, but "indefinite" retention of sensitive video recordings is a much bigger privacy decision than the stated rationale requires, and it's being proposed without any deliberate retention-period decision at all — this needs its own policy escalation rather than defaulting to indefinite, defaulting to matching an unrelated document's retention period (B), or the opposite overcorrection of immediate deletion (A) which would defeat the legitimate verification purpose entirely.

---

### Q50.
A national retailer's return-fraud model, which incorporates a customer's return frequency and total return value among other factors, has operated for a year with strong fraud-catch rates. A new analyst proposes adding "average time between purchase and return" as an additional input, noting that legitimate returns (e.g., gift returns after holidays) often have longer gaps than fraudulent ones.
**Options**
- A. Add the input, but only review it if fraud-catch rates change significantly after deployment
- B. Run the same disparate-impact check used for any new scoring input: a neutral-looking metric can correlate with protected characteristics or penalize legitimate return patterns.
- C. Add the input without further review, since it's a behavioral metric unrelated to any protected characteristic and the model already has a strong track record
- D. Skip review since return-frequency and return-value (the existing inputs) were presumably already reviewed, and this is a similar type of behavioral metric

**Answer:** B — This tests whether the test-taker recognizes that "facially neutral, behavioral, not obviously protected-characteristic-related" (as this new input genuinely is) doesn't exempt an input from the same fairness-review discipline applied to any new scoring factor — assuming neutrality from a plausible-sounding rationale, or from analogy to previously-reviewed inputs (D), skips the actual check.

---

### Q51.
A national law firm allows attorneys to use Claude for legal research, with a written policy requiring that all case citations be independently verified against a legal database before inclusion in any filing. An attorney reports that they always follow this policy, but describes their verification step as: "I ask Claude to confirm each citation is accurate before I use it."
**Options**
- A. This satisfies the policy only if Claude's confirmation includes a direct quote from the case
- B. It misses the policy's intent: asking the model that produced a citation to confirm it isn't independent verification against a legal database.
- C. This satisfies the firm's verification policy, since the attorney is actively checking each citation as required
- D. This satisfies the policy as long as the attorney has never personally encountered a fabricated citation before

**Answer:** B — This is a harder, applied version of the independent-verification principle specifically targeting a well-known real failure mode (fabricated legal citations): an attorney can sincerely believe they're complying with a verification policy while actually performing a self-report check that doesn't meet the policy's substantive requirement of independent, database-based verification.

---

### Q52.
A manufacturing company's HR team uses an AI tool to draft performance-improvement-plan (PIP) language for underperforming employees, with a manager required to review and personalize each draft before delivery. An employee later grieves their PIP, alleging the language was "generic and dehumanizing, clearly written by AI with no real consideration of my situation." HR responds that a manager did review and approve the PIP before delivery, satisfying the required checkpoint.
**Options**
- A. HR's response is insufficient because AI should never be used to draft PIP language under any circumstances
- B. HR showed the gate was followed, not that it functioned: a superficial manager approval leaves the complaint that no real judgment was applied unanswered.
- C. HR's response is insufficient only if the manager cannot produce evidence of specific edits made to the draft
- D. HR's response is sufficient, since the defined review checkpoint (manager review before delivery) was followed as designed

**Answer:** B — This is a harder governance question because it distinguishes between a checkpoint *existing and being followed procedurally* versus that checkpoint *functioning substantively* — the earlier principle that "a person will review" needs WHO/WHAT/WHEN to be a real gate extends further here: even a well-specified gate can fail in practice if the review itself is superficial, which is a legitimate concern separate from whether the documented process was technically followed.

---

## Domain 1 — Prompting and Task Execution (14% — Q53–Q66)

### Q53.
A commercial real-estate associate attaches a 12-page lease abstract and asks Claude to "summarize the key terms for the investment committee." The committee needs exactly five things: rent escalation schedule, renewal options, termination rights, any tenant improvement allowances, and co-tenancy clauses — nothing else. The first draft is a well-organized eight-section summary covering the whole lease.
**Options**
- A. Make the prompt substantially longer, describing the property and lease history in more detail, so Claude better understands the context
- B. Specify the exact five items the committee needs and what to exclude, rather than relying on 'key terms' meaning the same to both parties.
- C. Attach the lease as a file instead of pasting excerpts, expecting a more targeted read
- D. Ask Claude to shorten the eight-section summary by half, keeping the same structure

**Answer:** B — "Key terms" was interpreted reasonably by the model, just not in the way the associate specifically meant; naming the exact five required items (and what to leave out) resolves the ambiguity directly, rather than adding unrelated context, shortening a still-wrong structure, or changing the attachment format.

---

### Q54.
A benefits consultant's first draft request to Claude is: "Compare our three proposed health-plan options for the employee newsletter." The result is a dense, actuarial-style comparison table using terms like "coinsurance" and "out-of-pocket maximum" without explanation — technically accurate, but not right for a general-employee newsletter audience.
**Options**
- A. Rewrite the original prompt from scratch with a much longer, highly detailed specification and try a more capable model.
- B. "Simplify this."
- C. "The audience is general employees, not specialists: keep the three options but explain each term plainly, with everyday framing instead of insurance jargon."
- D. "This is too technical. Try again with a totally different approach."

**Answer:** C — Specific, targeted feedback (name the actual audience gap and what "simpler" concretely means here) produces a better second draft than a vague "too technical, try again" (D), a full prompt-and-model overhaul (A) for what was actually a targeted, fixable gap, or an underspecified "simplify" (B) that doesn't say what changes.

---

### Q55.
A university department chair's first draft request reads: "Give me ideas for improving student engagement in our intro course." **(Select TWO — all-or-nothing)** Which **TWO** follow-up refinements best preserve this as a genuinely divergent, options-generating task while still improving its usefulness?
**Options**
- A. "Include a mix of ideas other departments have used, and ones I haven't seen suggested before."
- B. "Rank the ideas from best to worst and only show me the top 3."
- C. "Only give me ideas that fit our existing 50-minute lecture format, use no additional TA hours, and follow our current syllabus template exactly."
- D. "Give me 15 varied ideas, spanning low-effort/quick-win options through bigger structural changes, without filtering any out yet — I'll evaluate them after."
- E. "Format each idea as a two-sentence bullet point in a table with columns for effort and impact."

**Answer:** A, D — Both widen the range of what's generated (explicitly asking for volume and variety, spanning familiar and novel) without pre-filtering, which is what a genuinely divergent brainstorming request needs. C constrains the response too tightly for a brainstorm (locking in format/resource assumptions before ideas are even generated), and B and E both prematurely convergent-ize the task (ranking/cutting to 3, or locking a rigid output format) before divergent value has been captured.

---

### Q56.
A city library system's associate needs to reconcile a decade of digitized catalog records against a newer standardized format, and has only sampled a handful of the oldest records so far, which a colleague warns are "inconsistently formatted, some by hand originally." The associate's instinct is to write one comprehensive prompt covering every formatting inconsistency they can imagine, then have Claude write and run the full conversion in one pass.
**Options**
- A. First have Claude profile a representative sample across the full decade and report the actual range of formatting inconsistencies before any conversion rules are written.
- B. Write the comprehensive rule set now, covering every imaginable inconsistency, to avoid multiple rounds of rework
- C. Run the conversion now on the assumption that unexpected issues can be fixed as they surface in the output
- D. Ask for the conversion code in a specific language so the associate can inspect the logic before running it on the full decade of records

**Answer:** A — This is a harder version of the profile-before-rules principle, specifically because it adds a subtler trap: the associate has only sampled the *oldest* records, but the profiling step needs to cover the *full* decade's range of formats, not just extend the sample within the subset already known to be messy — a colleague's warning about one subset shouldn't narrow the scope of the diagnostic step.

---

### Q57.
A nonprofit's grant-writing associate needs a full grant-narrative draft for a specific foundation, and their instinct is to request the complete narrative immediately, in one detailed prompt covering the foundation's stated priorities.
**Options**
- A. Ask Claude to grade a rough outline the associate writes first, before any narrative drafting begins
- B. Request the complete narrative now, since including the foundation's stated priorities upfront should be enough specification for a strong first draft
- C. Request three different narrative drafts in different tones and select the strongest as the base
- D. First ask Claude to map what is known: past successful grant narratives, this foundation's funding history and priorities, and prior applications, before generating narrative text.

**Answer:** D — Even with the foundation's priorities included in the prompt, jumping straight to narrative generation skips grounding the draft in the organization's own track record and this specific foundation's history — mapping what's known first (a decomposition step for an open-ended writing task) produces a better-grounded narrative than three stylistic variants (C) or grading an outline in isolation (A).

---

### Q58.
A regional airline's associate, in a brand-new chat with no prior conversation history, asks Claude to draft a flight-delay compensation notice for affected passengers. The first draft correctly follows the required regulatory disclosure format but uses the wrong currency symbol for one of the three markets the notice needs to cover.
**Options**
- A. Start an entirely new chat and resend the identical prompt, in case something in the first chat caused the error
- B. Check whether a stored account instruction or knowledge file about currency formatting has gone stale
- C. Switch to a more capable model immediately, expecting it to handle multi-market currency correctly
- D. Treat it as under-specification: the request likely never said which currency applies to which market, so re-check it and add that explicitly.

**Answer:** D — With no conversation history to overload (ruling out A as the mechanism) and no prior working version to compare against for staleness (ruling out B), a first-attempt error on an unstated multi-market requirement (which currency for which market) is a specification gap to close directly, not a model-capability issue.

---

### Q59.
A hotel-group associate's fully-specified delegation (reader, purpose, budget, format, and what Claude may decide alone) still results in Claude silently omitting one of the four requested comparison criteria from the final table, without noting the omission anywhere.
**Options**
- A. It needed a closing instruction to confirm every requested item is present or flag omissions by name; 'flag when you decide' doesn't catch a silent omission.
- B. The request needed more background detail about why each criterion matters
- C. The request needed the table reformatted as a spreadsheet instead
- D. The request needed a stricter budget constraint

**Answer:** A — This is a harder distinction from the earlier "flag when you decide" pattern: an outright silent omission of an explicitly requested item is a different failure than exercising unflagged discretion on an ambiguous choice (like a tie-break) — the fix here is a specific completeness-confirmation instruction, not simply more background detail or a different output format.

---

### Q60.
A market-research firm's analyst pastes 25 open-ended customer-interview transcripts into one request, asking for theme identification, a frequency count per theme, and a client-ready insight memo, all at once — but this time, includes an instruction: "Before counting or writing anything, first show me your theme definitions and a table mapping each transcript to its assigned theme, and wait for my confirmation before proceeding."
**Options**
- A. This instruction is unnecessary as long as the analyst reviews the final memo carefully
- B. This instruction doesn't meaningfully change the risk of a downstream error, since the underlying single large request remains
- C. It substantially reduces the decomposition risk, since the mapping table and wait-for-confirmation gate work as a checkpoint like staged requests.
- D. This instruction should also specify a maximum number of themes, or it won't work as intended

**Answer:** C — This tests whether the test-taker recognizes that the *structural* protection (verify the intermediate coding step before building on it) can be achieved within a single, well-constructed request via an explicit checkpoint-and-wait instruction — it isn't strictly about how many separate messages are sent, but about whether verification happens before downstream steps build on unverified intermediate output.

---

### Q61.
A management consultant is preparing a client workshop and asks Claude for "10 icebreaker activity ideas" for a group of senior executives who are described, in the same prompt, as "notoriously skeptical of anything that feels like a typical corporate team-building exercise." The results returned are 10 fairly conventional icebreaker ideas (two-truths-and-a-lie, speed networking, etc.).
**Options**
- A. Icebreaker requests are inherently unsuited to AI assistance for skeptical audiences, and should be brainstormed manually instead
- B. The ideas were never checked against the named audience constraint; a targeted iteration asking which avoid feeling corporate, plus five alternatives, beats restarting.
- C. The prompt was already well-specified (audience described, quantity given); the model simply produced a weak result, so try a different, more capable model on the identical prompt
- D. The prompt should have specified a stricter format (e.g., "each idea in one sentence") to force more creative constraint-following

**Answer:** B — The audience constraint was stated but the model's divergent output wasn't yet filtered or iterated against that specific constraint — a targeted, specific follow-up (naming exactly what "still feels typical" means, in the direction the ideas should move) is the efficient iteration move, rather than switching models on the same prompt, declaring the task unsuited, or adding an unrelated formatting constraint.

---

### Q62.
An operations manager delegates a data-cleaning task on a 5,000-row customer export, providing clear rules for handling duplicates and missing fields, and separately noting: "If you encounter a data pattern not covered by these rules, stop and describe it to me rather than guessing how to handle it." Claude encounters an unanticipated pattern (a batch of rows with a foreign-format phone number), stops, and describes it clearly, without attempting a fix.
**Options**
- A. This is a prompting failure, since a well-specified request shouldn't encounter any unanticipated patterns at all
- B. This is the request behaving as intended: an explicit 'don't guess, ask' instruction produced the right behavior when an unanticipated pattern arose.
- C. This is a sign the task needed a more capable model to handle the unanticipated pattern autonomously
- D. This is a context-overload issue, since 5,000 rows is a large dataset

**Answer:** B — This is included as a "correctly designed prompt working as intended" recognition question: an explicit, well-placed "flag rather than guess" instruction for genuinely out-of-scope cases is good task design, and the model encountering *and correctly flagging* an edge case is the system working, not a fault to diagnose.

---

### Q63.
A corporate-communications associate needs the same underlying announcement (a policy change) delivered as: a two-line push notification, a one-paragraph email summary, and a detailed FAQ document. The associate's plan is to ask for all three in one prompt: "Give me a push notification, an email summary, and an FAQ for this policy change."
**Options**
- A. Request all three in one prompt, but ask for extended thinking to be turned on to handle the combined complexity
- B. Decompose by output format: request the push notification, email summary and FAQ separately, each with its own length and purpose constraint, since one prompt risks blending them.
- C. Request only the FAQ first, then ask Claude to extract the push notification and email summary from it afterward
- D. This single combined prompt is well-suited to the situation, since all three outputs describe the same underlying policy change and benefit from being drafted together for consistency

**Answer:** B — Even though the three outputs share the same underlying content (making D tempting, since consistency does matter), their format constraints are different enough (a two-line notification has essentially opposite constraints from a detailed FAQ) that a single combined prompt risks a "one-size-fits-none" result — this is task decomposition applied by *output format/constraint type*, not just by topic or section.

---

### Q64.
A regional theater company's marketing associate needs to know this week's local weather forecast for an outdoor-event contingency plan, needs a cited, multi-source comparison of five ticketing-platform vendors' fee structures for a board decision, and needs a one-line reminder of what "will call" means for a new box-office volunteer. **(Select THREE — all-or-nothing)** Which **THREE** correctly match each need to the most fitting way of answering it?
**Options**
- A. The "will call" definition → an inline conversational reply, not a formal document
- B. The ticketing-platform fee comparison → a deeper, cited research-style pass gathering and comparing multiple vendor sources
- C. The weather forecast → a cited, multi-source research pass, to ensure meteorological accuracy for an outdoor event
- D. The ticketing-platform fee comparison → a quick current-facts lookup, since fee structures are simple, published numbers
- E. The weather forecast → a quick, current-facts lookup, not a deep multi-source research pass

**Answer:** A, B, E — A live, simple current fact (weather) fits a quick lookup, not heavy research (ruling out C); a multi-vendor, board-facing comparison needing citations across several sources fits a deeper research pass, not a single quick lookup (ruling out D); and a one-line definition for a volunteer fits a short conversational answer, not a formal document.

---

### Q65.
A junior policy analyst with no prior housing-policy background drafts a public-facing explainer on a proposed zoning change, using Claude, based on the actual proposed ordinance text and a staff briefing document provided as sources. The explainer accurately reflects both source documents and addresses every point requested in the brief.
**Options**
- A. Ask Claude to rate the explainer's own accuracy and revise any section scoring below a set threshold
- B. A colleague with housing-policy or zoning expertise should judge whether the explainer is credible; matching sources and covering the points doesn't show it captures policy nuance.
- C. A grammar-and-clarity proofread by a colleague is the missing check before publication
- D. Run the explainer through a formatting pass so it reads as polished as one written by an experienced policy writer

**Answer:** B — As in the customs-briefing pattern, internal accuracy against provided sources doesn't confirm subject-matter credibility from a domain expert's perspective — the specific gap (a junior analyst's inexperience) is closed only by genuine subject-matter review, not proofreading, self-rating, or polish.

---

### Q66.
A independent bookstore's owner asks Claude to "write a description for our new staff-picks display" and receives a single, generic paragraph. The owner then asks: "Actually, give me three different versions: one punchy and short for the front window sign, one warmer and more detailed for the store's email newsletter, and one that could work as an Instagram caption with relevant hashtags — each should describe the same staff-picks concept but fit its own format."
**Options**
- A. It is a well-constructed decomposition: distinctly specified formats, each with its own tone and length, instead of one generic version or three unconstrained variants.
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
- B. Split each document into five separate chats and cross-reference them manually afterward
- C. Switch to the fastest, lightest tier to process both documents more quickly and reduce the chance of losing track
- D. Turn off any extended reasoning mode, on the theory that additional reasoning steps are diluting attention to the source text

**Answer:** A — This is the same "escalate for depth on a large, coherent, cross-referencing structure" pattern, made harder by involving *two* separate long documents that must be held in relation to each other — exactly the kind of task the top capability tier is suited for, not a faster/lighter tier, reduced reasoning, or fragmenting the documents (which would break the very cross-referencing the task requires).

---

### Q68.
A customer-support operations lead runs every routine, single-sentence ticket-tagging task through the top-capability model tier with extended thinking enabled, "to be safe," while running an annual, high-stakes staffing-model rebuild (balancing seasonality, overtime rules, and multi-site constraints) on the fastest, lightest tier "since it just needs to produce a spreadsheet."
**Options**
- A. Both are mismatched in opposite directions: routine tagging needs neither the top tier nor extended reasoning, while a high-stakes multi-constraint rebuild does, whatever its output format.
- B. Neither choice is a problem, since model tier is primarily a cost lever and quality differences are marginal for both task types
- C. Only the staffing-rebuild choice is a problem; the ticket-tagging default is a safe, low-risk choice even if costly
- D. Only the ticket-tagging choice is a problem; the staffing rebuild is fine on the lightest tier as long as the spreadsheet formulas are reviewed afterward

**Answer:** A — The staffing rebuild's *output format* (a spreadsheet) is a red herring — what determines tier/reasoning-depth needs is the task's underlying complexity (multi-constraint optimization with real consequences), which is high regardless of how simple the deliverable format looks; meanwhile the tagging task's low complexity doesn't justify its expensive default either.

---

### Q69.
A specialty retailer's pricing team runs a heavy, multi-source research-mode pass every time they need to check a competitor's current advertised price for a specific product, "to be thorough," and separately relies on a single quick chat message (no research mode) to synthesize a nuanced comparison of long-term supplier-contract terms across three multi-year agreements with materially different renewal and penalty clauses.
**Options**
- A. Only the competitor-price lookup is mismatched; the contract comparison is appropriately handled with a quick chat since it's "just reading three documents"
- B. Only the contract comparison is mismatched; the competitor-price research-mode pass is appropriately thorough given pricing is business-critical
- C. Both choices are reasonable, since research mode is generally the more thorough option and a quick chat is generally the more efficient one
- D. Both are mismatched: a single current price doesn't need heavy multi-source research, while comparing multi-factor terms across three agreements benefits from deeper reasoning.

**Answer:** D — This inverts the more obvious pairing to test the underlying principle rather than surface impressions: a simple current-fact lookup doesn't need heavy research tooling regardless of business importance, and a genuinely multi-factor reasoning task (comparing clauses with different structures across three contracts) needs reasoning depth regardless of how simple "just reading documents" sounds.

---

### Q70. *(Select TWO — all-or-nothing)*
A corporate-events team is deciding, for five upcoming requests, whether extended thinking is worth its added time/cost. Which **TWO** are genuinely worth it?
**Options**
- A. Generating eight quick tagline options for a save-the-date email, to be narrowed down casually later
- B. Sequencing a multi-city product-launch tour across six cities under simultaneous constraints of venue availability, staff travel limits, and a fixed total budget
- C. Deciding the optimal seating-chart arrangement across 40 tables balancing known interpersonal conflicts, sponsorship-visibility requirements, and dietary-accommodation groupings simultaneously
- D. Looking up the venue's posted maximum occupancy limit from an attached venue-specs sheet
- E. Converting a finalized run-of-show document into a simple printable schedule handout

**Answer:** B, C — Both are genuine multi-constraint optimization problems where several competing factors must be weighed against each other simultaneously, which is exactly where deeper reasoning adds real value. A, D, and E are simple, low-stakes, largely single-step tasks where extended reasoning adds cost without meaningfully improving the result.

---

### Q71.
A boutique law firm's associate is three hours into a single long conversation drafting and revising a complex contract with Claude, and response quality has visibly degraded over the last 30 minutes — Claude has started contradicting an earlier-agreed defined term and has forgotten a formatting convention established at the start of the session.
**Options**
- A. Switch immediately to a more capable model tier within the same long conversation, since a stronger model would maintain the defined term and formatting convention regardless of conversation length
- B. This is a sign the contract-drafting task itself is unsuited to AI assistance and should move to manual drafting from this point forward
- C. Most likely context overload from length, not capability: summarize the agreed terms and conventions, correct any drift, and continue in a fresh session seeded with that summary.
- D. Continue in the same conversation, simply repeating the defined term and formatting convention at the top of every subsequent message

**Answer:** C — The pattern (strong performance for a long stretch, followed by drift/contradiction specifically after a lengthy session) is the classic context-overload signature, best addressed by summarizing and restarting rather than upgrading model tier (which doesn't fix an overloaded context window), manually repeating information every message (a workaround, not a fix), or abandoning AI assistance for the task entirely.

---

### Q72.
A management consultancy's internal AI-strategy lead states as firm policy: "For any client-facing analytical deliverable, always use our most capable model tier with extended thinking enabled, regardless of the specific task, because our clients expect and are paying for our best work."
**Options**
- A. It reflects poor task-fit judgment: 'client-facing' describes the audience, not complexity, so a simple reformatting task doesn't need the top tier and extended reasoning.
- B. This is sound, defensible policy, since client-facing work should never risk being under-resourced
- C. This is sound policy as long as the firm can absorb the additional cost
- D. This is sound policy specifically for consultancies, even if it wouldn't be sound for other industries

**Answer:** A — This is a harder version of the "always use the best" trap because it's dressed up as a client-service rationale (clients expect our best work) rather than a lazy habit — but the underlying judgment failure is the same: model-tier/reasoning-depth decisions should track task complexity, not who the audience happens to be.

---

### Q73.
A financial-services support team needs to: quickly verify today's published overnight interbank lending rate for a client call in five minutes, conduct a comprehensive, multi-source comparison of five competing custodial-services providers for a board presentation next month (with citations), and determine, given a client's specific and unusual combination of account types, which of three internal fee schedules applies (a determination requiring careful, multi-step reasoning through the firm's internal fee-schedule rules).
**Options**
- A. Rate lookup: quick current-facts check; provider comparison: deeper cited multi-source research; fee-schedule determination: extended thinking for the multi-step rule application.
- B. Rate lookup → extended thinking, since interest rates are financially significant; provider comparison → a quick lookup, since providers are well-known; fee-schedule determination → a quick lookup, since it's an internal document
- C. All three → a deeper, cited multi-source research pass, since thoroughness is always the safer choice
- D. All three → extended thinking, since financial-services contexts always warrant deeper reasoning regardless of task type

**Answer:** A — Each task fits a different tool for a specific structural reason: a single current published rate needs a fast factual check, not deep research; a multi-source, citation-needing comparison needs an actual research pass; and a multi-step internal-rule application (not a lookup at all) benefits from deeper, careful reasoning — collapsing all three into "always thorough" or "always deep reasoning" ignores what each task structurally requires.

---

### Q74.
A regional theater's box-office system produces a "recommended ticket price" for an upcoming show that's noticeably higher than any comparable past show, with no obvious explanation in the current season's data. The associate's first instinct is to assume the pricing model hallucinated the figure and re-run the request with "use only this season's actual sales data."
**Options**
- A. Switch to a more capable model tier, on the theory that a stronger model is less likely to fabricate a pricing figure
- B. Re-prompt with the stricter wording and regenerate the full recommendation
- C. Ask the tool to rate its own confidence in the recommended price and only accept figures above a high confidence threshold
- D. Before assuming hallucination, check whether Project knowledge holds an outdated 'premium pricing' document from a past special event that may still influence the recommendation.

- **Answer:** D — As with the earlier stale-rate-card pattern, an unusual, unexplained figure is often better explained by a stale or mismatched knowledge source still feeding the workflow than by outright fabrication — checking the actual configuration first is more diagnostic than re-prompting, upgrading the model, or relying on a self-reported confidence score.

---

### Q75.
A specialty coffee roaster's wholesale team has iterated five times with Claude on a bulk-order discount-tier calculator embedded in a client-facing quote template. Formatting, tier boundaries, and client-facing language are all now correct, but the final discounted-total figure is still subtly wrong on every attempt, despite five rounds of increasingly precise wording about how discounts should stack.
**Options**
- A. It is a feature mismatch: the stacking discount should be computed by executable code, not generated as prose, however precisely the rule is worded.
- B. This is a context-overload problem, since five rounds of iteration have accumulated in one conversation
- C. This is a description problem requiring one more, even more precise attempt at wording the stacking rule
- D. This is a model-capability problem requiring the top-capability tier

**Answer:** A — Five rounds of increasingly precise wording still producing subtly wrong arithmetic is a strong, repeated signal that this is a prose-vs-computation feature mismatch, not a wording, model-capability, or context-length problem — the calculation needs to move into actual executable computation.

---

### Q76.
A university's IT helpdesk wants a single AI-assisted intake system to both instantly triage routine password-reset requests (extremely high volume, essentially no ambiguity) and also help resolve a smaller number of complex, multi-factor account-access disputes involving conflicting departmental permissions across multiple systems.
**Options**
- A. Use the lightest tier for both, since IT helpdesk work is generally routine
- B. Use one uniform model configuration (same tier, same reasoning setting) for both request types, to keep the system simple to maintain
- C. Use the highest-capability tier with extended thinking for both, since account-access issues are always security-sensitive
- D. Use a fast, lightweight tier for high-volume password-reset triage and deeper reasoning, perhaps a higher tier, for complex permission disputes; different request types warrant different judgments.

**Answer:** D — This tests whether the test-taker recognizes that a single system serving structurally different task types should apply the underlying tier/reasoning-depth judgment *per request type*, not adopt one uniform setting for administrative simplicity (B), blanket caution (C), or blanket cost-minimization (A) — the "match tool to task" principle applies within one workflow just as much as across separate ones.

---

### Q77.
An urban-planning associate needs Claude to draft a public meeting notice (simple, templated, low-stakes) and, in the same working session, needs it to reconcile conflicting numeric traffic-count data from three different consulting reports commissioned over the years, where the reports used different methodologies and the discrepancy needs careful, multi-step reasoning to explain and resolve for a technical appendix.
**Options**
- A. Enable extended thinking for both tasks, since the associate is working on both in the same general session
- B. Keep notice drafting on a standard configuration and enable extended thinking for the traffic-count reconciliation, a genuine multi-step task, accepting the small friction of switching.
- C. Use the lightest tier for the meeting notice and the lightest tier plus extended thinking for the traffic-count reconciliation, since a lighter tier plus deeper reasoning is more cost-effective than a heavier tier
- D. Use the same default configuration for both tasks in the same session, since switching settings mid-session adds friction

**Answer:** B — The two tasks are genuinely different in kind (templated low-stakes drafting vs. multi-source numeric reconciliation requiring careful reasoning), and the correct judgment is to configure each task appropriately even within one working session — session-level convenience (D) or applying one setting to both (A) doesn't override task-level fit, and C's "lighter tier plus reasoning" substitution doesn't necessarily suit a task that may also benefit from a higher capability tier, not tier substitution alone.

---

### Q78.
A regional hospital's clinical-documentation team has been told that "extended thinking" and "the flagship model" are the same feature under different names by a well-meaning but mistaken vendor trainer, and has been avoiding extended thinking on cost-sensitive routine tasks specifically because they believe it always requires the (expensive) flagship tier.
**Options**
- A. It's a misconception: extended thinking and model tier are independent settings, so cost-driven avoidance rests on a wrong premise, and some tiers support thinking without flagship cost.
- B. The trainer's claim is correct, and the team's cost-avoidance behavior is appropriately cautious
- C. The distinction doesn't matter in practice, since both settings should generally be minimized for cost reasons regardless of task
- D. The trainer's claim is correct for some vendors but not others, so the team should verify per-vendor before deciding

**Answer:** A — This directly tests the same independent-switches distinction from earlier in this domain, framed as a correction of a specific, plausible-sounding misconception (that reasoning depth and model tier are bundled) — correcting the premise matters because it changes the team's actual available options for balancing cost against reasoning depth on different tasks.

---

## Domain 5 — Configuration and Knowledge Management (12% — Q79–Q90)

### Q79.
A regional accounting firm's associate handles work for two clients, "Client A" (a construction company) and "Client B" (a restaurant group), currently in two separate Claude Projects, each correctly scoped with its own knowledge files and instructions. The associate now also needs to draft the firm's own internal year-end newsletter, unrelated to either client.
**Options**
- A. Draft it in a plain chat or a separate firm-wide Project, not inside either client Project, since neither client's material applies and using one risks cross-contamination.
- B. Draft the newsletter using the firm-wide account-level instructions alone, since a one-off task doesn't need Project scoping
- C. Draft the newsletter inside whichever client Project was most recently used, for convenience
- D. Create a fresh Project for the newsletter, and import both clients' knowledge files into it in case any client data is referenced

**Answer:** A — This tests the harder edge case of Project scoping discipline: a one-off, unrelated internal task shouldn't be drafted inside an existing client-scoped Project (risking that Project's client-specific instructions/knowledge bleeding into unrelated work) — plain chat or a genuinely appropriate internal-work Project is the right scope, and there's no reason to import client knowledge files (D) into unrelated work.

---

### Q80.
An associate's account-level instructions include: "When I ask for a summary, always structure it as: Overview, Key Risks, Recommendation." This has worked well for the associate's typical risk-assessment work, but the associate has just started a new role requiring frequent short customer-service response summaries, where this three-part structure is now consistently unhelpful and out of place.
**Options**
- A. Keep the account-level instruction as-is, since it has a strong track record from the previous role
- B. Delete the account-level instruction entirely and rely on Claude to infer the right structure for each request going forward
- C. An instruction true everywhere in one role can stop fitting as work changes: update it or scope it to a Project for the work it still suits.
- D. Leave the instruction in place, and manually override it by writing "ignore your standard structure" at the top of every customer-service summary request

**Answer:** C — This is a harder version of the account-level-scoping principle because the instruction was genuinely well-scoped *at the time it was written* (given the associate's prior role) — the lesson is that "true everywhere" instructions need to be revisited as the actual scope of "everywhere" (the associate's own work) changes, rather than assuming a once-correct global instruction stays correct indefinitely, patching around it per-request (D), or removing structure guidance altogether (B).

---

### Q81.
A high school's two AP History teachers share one Claude Project for "AP History Resources," containing both teachers' respective rubrics, sample essays, and pacing guides, because "it's all AP History content." One teacher's students have started receiving feedback referencing grading language from the other teacher's rubric.
**Options**
- A. This is acceptable as long as students are told feedback may reference either teacher's rubric
- B. It is a scoping error: each teacher's rubric language belongs in its own Project, since 'same subject' doesn't mean interchangeable materials, and sharing causes contamination.
- C. This can be fixed by asking Claude, in each request, to "use the correct teacher's rubric," without changing the Project structure
- D. This is expected and acceptable, since both teachers teach the same subject and course level

**Answer:** B — "Same subject" is a more tempting-sounding justification for shared scoping than the earlier wholesale/retail example, but the underlying issue is identical: two genuinely distinct rule-sets (each teacher's own rubric) are getting cross-applied because they share one always-on knowledge pool — a per-request reminder (C) is a workaround, not a structural fix.

---

### Q82.
A consultant connected a project-management platform's connector three months ago and has used it daily without issue. Today, in a new chat, a request referencing a specific project's task list returns an error stating the connector cannot be reached, though the consultant confirms (by checking the platform directly) that the platform itself is fully operational.
**Options**
- A. Check narrower causes first: whether the connector is enabled for this chat, a token or permission issue, and whether it can access the referenced project, before a full reconnect.
- B. Switch to manually copy-pasting task list data into chat going forward, to avoid connector reliability issues entirely
- C. Assume the connector has permanently expired after three months and needs to be fully reconnected from scratch immediately
- D. Assume the issue is a temporary platform-side outage, despite having confirmed the platform is operational, and simply try again later

**Answer:** A — Even though this associate has months of reliable use (unlike the newer-connector example), the correct diagnostic instinct is still to check the narrower, more common causes (per-conversation enablement, specific project access, token issues) before concluding a full reconnection is needed — jumping to the most disruptive fix, abandoning the connector for manual workarounds, or ignoring already-confirmed platform status are all less efficient responses.

---

### Q83.
A boutique investment firm's Claude Project for a specific client contains that client's portfolio holdings as a knowledge file, refreshed monthly by an operations associate. A portfolio manager, preparing for a client call, notices the AI-generated portfolio summary references a holding the client sold three weeks ago.
**Options**
- A. This means the AI is hallucinating a holding not actually in the current portfolio
- B. This means the portfolio manager should switch to a different model, which may have more current training data
- C. This means the Project should be deleted and recreated to clear any corrupted cached data
- D. Most likely a stale knowledge source: with monthly refreshes a three-week-old sale may be missing, so confirm the file's last-refresh date and update it before the call.

**Answer:** D — A monthly refresh cycle creates a predictable staleness window, and a sale three weeks ago falls plausibly within that window — checking the actual file's currency (a configuration/maintenance question) is the right first step, rather than assuming hallucination, corruption requiring a rebuild, or a model-training-data issue (irrelevant, since the holding came from the uploaded file, not general training knowledge).

---

### Q84.
An associate wants a rule that should apply only when working on a specific quarterly board-deck project, should include several standing reference documents (last quarter's deck, the current financial data extract, the board's stated format preferences), and should not affect any other work the associate does.
**Options**
- A. Memory, since it will persist the board's format preferences over time automatically
- B. A Skill, since it defines "how" to build a board deck on demand whenever requested
- C. A Project: the need is scoped to one quarterly deliverable, always-on within it, and shouldn't leak into other work, unlike a Skill or account-level instructions.
- D. Account-level custom instructions, since board-deck quality matters enough to apply broadly

**Answer:** C — This question is harder because a Skill (B) is genuinely plausible for "how to build a board deck," but the requirement that specific reference *files* stay attached and that the scope explicitly exclude other work points to a Project's combination of always-on files plus instructions within a bounded scope, which a Skill alone (on-demand logic, not necessarily bundled with specific persistent files) doesn't fully provide.

---

### Q85.
A mid-sized law firm is piloting a Claude connector to its document-management system for the first time, to support a new AI-assisted contract-review workflow. The pilot plan calls for connecting the system with full read/write access immediately, "so we don't have to reconfigure permissions later once the pilot proves successful."
**Options**
- A. Approve full read/write access from the start, since anticipating future needs avoids a later reconfiguration step
- B. Approve full read/write access, but only for the specific pilot user's individual account rea, rather than the firm's shared account
- C. Start read-only and grant write access later, once the workflow is validated and a real write use case is confirmed; don't provision it 'just in case'.
- D. Approve write-only access, since the review workflow's main function is producing analysis, not reading original documents

**Answer:** C — "Avoiding reconfiguration later" is a tempting operational-convenience argument, but it inverts the correct sequencing: access (especially write access) should be scoped to actual, confirmed current need, with broader access deliberately added later once a real use case exists — provisioning broad access upfront "just in case" is the pattern this principle specifically cautions against.

---

### Q86.
A freelance grant-writer's Claude account has developed a memory note, generated over several past conversations, stating a specific client "prefers a very formal, traditional tone." A new project for that same client explicitly requests "a much more casual, conversational voice for this particular campaign, different from our usual style."
**Options**
- A. Claude will correctly override the memory note automatically once the new, explicit in-conversation instruction is given, so no action is needed regarding the memory note itself
- B. Delete the memory note immediately, since it has now been contradicted once
- C. This situation requires no attention at all, since memory notes are only suggestions and never actually influence output
- D. Though the explicit instruction wins here, update or qualify the memory note ('usually formal, except [campaign type]') so future conversations don't default to an incomplete generalization.

**Answer:** D — This is a harder, more realistic memory-management scenario than a simply "wrong" memory note: the note isn't incorrect, just incomplete (it doesn't capture a legitimate exception) — the associate should consider refining it for future accuracy rather than assuming automatic override handles it (A, which may or may not hold every time) or overreacting by deleting a generally-accurate note (B) over one legitimate exception.

---

### Q87.
A community health clinic wants to connect Claude to its patient-scheduling system to help draft appointment-reminder messages, its first-ever connector integration touching any patient data. The IT lead proposes testing the integration using a full, real, de-identified export of last month's actual appointment data, reasoning that "de-identified real data is safer than synthetic data and more realistic for testing."
**Options**
- A. Prefer genuinely synthetic data for the first pilot: de-identified real data can retain re-identification risk, especially in a small clinic, which synthetic data avoids.
- B. Skip both synthetic and de-identified testing, and go straight to a small, closely-monitored live pilot with real patient data
- C. Approve this approach, but only if the de-identification is performed by a different team than the one building the integration
- D. Approve this approach — de-identified real data is a reasonable, safer alternative to synthetic data for a first-time regulated-data integration test

**Answer:** A — This is a harder test of the synthetic-data-first principle because de-identified real data is a genuinely more sophisticated, more tempting alternative than obviously-risky raw real data — but de-identification carries its own residual risk (especially in a small dataset where unusual patterns can still be identifying), which is exactly why the standing practice specifically prefers synthetic data over de-identified real data for a first-time regulated pilot, not just "some form of anonymization."

---

### Q88.
An operations team at a mid-size manufacturer has built a useful, reusable Skill for formatting weekly production reports. A new hire, unfamiliar with the Skill, manually recreates the same formatting logic from scratch in their own individual prompts each week, producing slightly inconsistent results compared to the team's Skill-based output.
**Options**
- A. This is a memory problem, since the system should have "remembered" to tell the new hire about the Skill automatically
- B. This is a Project-scoping problem, since the Skill should have been built as a Project instead
- C. This is a Skill-design problem — the Skill itself needs to be simplified so new hires can discover and use it more easily
- D. It is an onboarding or awareness gap, not a design flaw: the Skill is correctly built but the new hire doesn't know it exists.

**Answer:** D — This distinguishes a genuine configuration-design flaw from a simpler awareness/onboarding gap: the Skill working correctly for the rest of the team, with the new inconsistency traceable specifically to one person not knowing it exists, points to an onboarding fix, not a redesign of the Skill, a memory mechanism, or a wholesale change from Skill to Project.

---

### Q89.
A city government's public-records office has a Claude Project for handling records-request intake, with standing instructions that say: "Always redact personal identifying information before summarizing a request for the public log." The office has just started receiving a new category of request (business-license records) where the requester's business name is itself the relevant subject and generally should NOT be redacted, unlike prior request types.
**Options**
- A. Remove the redaction instruction entirely, since it no longer applies cleanly to every request category
- B. Keep the blanket redaction instruction unchanged, since "always redact personal identifying information" is a safe default that should simply be manually overridden per-request as needed for the new category
- C. Update the Project's standing instructions to distinguish the new category: redact individuals' personal identifiers, but business names in business-license requests are the subject and stay.
- D. Move the new request category into a completely separate Project so the original instruction never has to change

**Answer:** C — As the actual scope of work handled by a Project evolves (a new request category with genuinely different needs), the Project's standing instructions should be updated to reflect that nuance directly, rather than left as an over-broad rule requiring manual correction each time (B), split off into a separate Project to avoid updating the original (D, unnecessary fragmentation for a rule that could simply be made more precise), or removed altogether (A, which loses the still-valid protection for the original request types).

---

### Q90.
A regional airline's crew-training department built a Skill several years ago that formats training-completion certificates according to a specific regulatory template. The regulator has since updated the required template format, but the Skill still produces certificates in the old format, and several recently issued certificates have gone out non-compliant before anyone noticed.
**Options**
- A. This is stale configuration: the Skill's template wasn't updated for the regulator's change, and a Skill's instructions don't self-update when the real-world standard changes.
- B. This is primarily a model-capability issue; a more capable model would have recognized the regulatory template had changed and adapted automatically
- C. This is a context-length issue, since the Skill has been used many times over several years
- D. This is a connector issue, since the certificate template should be pulled from a live regulatory source instead

**Answer:** A — This is a harder, higher-stakes version of the earlier stale-Skill pattern (with real regulatory-compliance consequences already realized): a Skill's instructions are fixed text that must be manually maintained as the real-world requirement they encode changes — no model upgrade compensates for genuinely outdated instructions, and while a live connector to a regulatory source (D) might be a good future improvement, it doesn't change that the *immediate* root cause is the Skill's static, unmaintained instructions.

---

## Domain 7 — Troubleshooting and Optimization (10% — Q91–Q100)

### Q91.
A regional water utility's scheduled weekly agent task, which compiles a compliance-monitoring report and emails it to three regulators, has now failed silently two weeks in a row, after months of reliable operation. The team's instinct is to immediately rewrite the underlying prompt with more detail, assuming the task's instructions have become inadequate.
**Options**
- A. Before touching the prompt, check for a paused run, usage limits, changed permissions or connector access, and a valid destination; two failures after months of reliability suggest plumbing.
- B. Recreate the entire task from scratch on a different automation platform, since repeated failure suggests the current platform is unreliable
- C. Manually compile and send the report for the next few weeks while waiting to see if the automated task starts working again on its own
- D. Rewrite the prompt with more detail immediately and re-run, since two consecutive failures after months of success suggests the instructions need reinforcement

**Answer:** A — A sudden failure after a long, stable track record is a stronger signal of an environmental change (permissions, limits, connector, destination) than of the original instructions suddenly becoming inadequate — the systematic plumbing check should come before prompt-rewriting, platform migration, or simply waiting.

---

### Q92.
A corporate-communications team notices that Claude-drafted press statements have, over the past month, started requiring significantly more editing rounds before approval than they did six months ago, even though the prompt template used has not changed. Which combination of questions should be asked first, before proposing a fix?
**Options**
- A. "Are we using the correct file format for the press statement output?" and "Is the formatting consistent with brand guidelines?"
- B. "Is the current model tier still the newest one available?" and "Is extended thinking turned on?"
- C. Has the type of statement shifted? Has the session pattern changed, such as one long-running chat? Has reference material gone stale without configuration being updated?
- D. "Should we switch to a different AI vendor?" and "Should we hire an additional writer?"

**Answer:** C — With the prompt template itself unchanged, the diagnostic questions should probe the other likely causes: a shift in task complexity/type, a change in session/context patterns, or staleness in supporting reference material — not jump to vendor-switching or additional hiring (D), assume a model/reasoning-setting issue without evidence (B), or focus on formatting concerns unrelated to the reported symptom (editing rounds, not formatting complaints) (A).

---

### Q93.
A hospital's clinical-education team has, for the past two years, defaulted to the top-capability model tier for every task "since patient-adjacent education content should always get our best effort," including routine tasks like reformatting an already-finalized training module into a printable handout.
**Options**
- A. This is a connector problem, since the training module needs to be pulled from a document-management system
- B. "Patient-adjacent" content justifies the top-tier default regardless of the specific task's actual complexity
- C. This is appropriate as long as the cost is within the department's budget
- D. It is a tier-mismatch habit: 'patient-adjacent' describes the subject, not task complexity, so reformatting a finalized document doesn't need the top tier.

**Answer:** D — This intentionally uses "patient-adjacent" as a plausible-sounding justification, similar to "client-facing" in an earlier question, to test whether the test-taker distinguishes subject-matter sensitivity in general from the actual complexity of a specific task — reformatting an already-finalized document is low-complexity regardless of the broader subject's sensitivity.

---

### Q94.
A nonprofit's grant-reporting associate says, "Every week I re-explain our organization's mission statement, our fiscal year dates, and our standard reporting disclaimers to Claude before I can start drafting anything." What is the correct symptom-to-concept mapping and fix?
**Options**
- A. This is a configuration gap: always-true information like mission statement, fiscal year and disclaimers belongs in a Project's instructions or files, not retyped weekly.
- B. This indicates the underlying grant-reporting task doesn't fit AI assistance well and should move to a manual template instead
- C. This indicates the associate should switch to a different AI tool with better memory by default
- D. This indicates extended thinking should be enabled so Claude can infer this context automatically each time

**Answer:** A — "Same background information, every time, for this recurring task" is the textbook signal for moving that content into a persistent configuration layer — not a tool-switching problem, a task-fit problem, or something a reasoning-depth setting would address.

---

### Q95.
A regional airline's pricing-operations team notices that a Claude-assisted fare-adjustment recommendation task, which has run smoothly for over a year, suddenly began giving noticeably different-quality recommendations three days ago — coinciding, the team later realizes, with an unrelated IT migration of the shared drive where the Project's reference fare-rules document lives.
**Options**
- A. This is a task-fit problem; fare-adjustment recommendations should not have been delegated to AI assistance in the first place
- B. This is most likely a coincidental model-quality fluctuation unrelated to the IT migration, and should be monitored for another week before investigating further
- C. This is a context-overload problem, since the Project has been used for over a year
- D. Check first whether the Project's reference to the fare-rules document survived the migration (broken link, old duplicate, permissions); a broken reference explains a precisely timed drop.

**Answer:** D — A sudden quality change that precisely coincides with an unrelated infrastructure event (the migration) is a strong, specific clue pointing to a broken or altered configuration reference, not a random model fluctuation (B, which ignores a highly relevant coincidence), general context overload (C, which doesn't explain the sudden onset tied to a specific event), or a task-fit conclusion contradicted by over a year of prior smooth operation (A).

---

### Q96.
A specialty printing company notices that routine, simple print-job description tasks (essentially, converting a customer's order form into a one-line job ticket) have quietly become one of the largest line items in their monthly AI usage costs, despite no increase in order volume.
**Options**
- A. This means extended thinking must be enabled to make the process more cost-efficient over time
- B. Likely a tier mismatch: check whether this simple, high-volume task runs on a pricier tier or reasoning setting than it needs before blaming volume or pricing.
- C. This means the task should be abandoned and reverted to fully manual job-ticket creation
- D. This means the AI provider must have changed its pricing structure without adequate notice

**Answer:** B — Rising cost specifically on a simple, high-volume, unchanged-volume task points directly to a tier/configuration mismatch as the first thing to check, before assuming external pricing changes (D), abandoning the workflow (C), or — notably — assuming that *enabling* extended thinking (A, which typically increases rather than decreases cost) would somehow improve cost efficiency.

---

### Q97.
An enterprise-software company's technical-writing team has iterated six times over two weeks on a Claude-assisted API-documentation-generation workflow, with each round's feedback being some version of "this is close, just needs to be a bit more accurate about the parameter descriptions." Accuracy issues persist each round despite this repeated feedback.
**Options**
- A. This means a seventh round of the same style of feedback ("be more accurate") is likely to finally succeed, given how close previous rounds have been
- B. This means the team should switch to manually writing documentation for parameter descriptions specifically, while keeping AI assistance for the rest of the document
- C. Six rounds of vague 'be more accurate' feedback failed; make it concrete by pointing to the exact source of truth, such as the API schema, and requiring sourcing from it.
- D. This means the underlying task (API documentation generation) is fundamentally unsuited to AI assistance

**Answer:** C — This extends the "vague iteration feedback is itself under-specified" principle to a repeated-failure pattern: six rounds of the same non-specific feedback category is a signal to make the *next* feedback concrete and sourced (e.g., point directly at the schema file), rather than expect a seventh vague repetition to somehow succeed (A), or conclude the whole task type is unsuited (D) or needs manual carve-out (B) without first trying genuinely specific feedback.

---

### Q98.
A national retailer's loyalty-program team optimized their AI-assisted personalized-offer generation workflow primarily for "offers generated per hour," successfully tripling output volume. Three months later, redemption rates for AI-generated offers are measurably lower than for the smaller volume of offers the team previously generated manually.
**Options**
- A. Abandon AI assistance for offer generation entirely and revert fully to the manual process
- B. Continue optimizing for volume, since a threefold volume increase is a clear, demonstrable success regardless of redemption rate
- C. Continue optimizing for volume, since the redemption-rate decline may simply reflect market conditions unrelated to the workflow change
- D. Reconsider the optimization target: maximizing volume for a redemption-driven workflow may have traded away the metric that mattered, so re-optimize toward relevance and redemption rate.

**Answer:** D — This is a harder version of "optimize for the metric that actually matters": raw volume was successfully optimized, but it wasn't the metric that mattered for the workflow's actual business purpose (driving redemptions) — the fix is re-targeting the optimization, not assuming external causes (C), declaring volume success sufficient regardless of the business outcome (B), or overcorrecting to full abandonment (A).

---

### Q99.
A metropolitan transit agency's service-alert drafting workflow has used the identical prompt template for two years without issue. This month, several drafted alerts have contained outdated route numbers that were renumbered in a system-wide route overhaul four months ago.
**Options**
- A. Since the prompt template is unchanged, this must be a sudden and unexplained model-capability regression
- B. This means the prompt template needs to be rewritten to explicitly mention the new route numbers each time
- C. This means the drafting task should be moved to a more capable model tier immediately
- D. Check whether the route-number reference was updated after the overhaul: an unchanged prompt plus a real-world data change points to a stale reference source.

**Answer:** D — An unchanged prompt ruling out prompt-based causes, combined with a specific, dateable real-world change (the route overhaul) that precedes the errors, points clearly to a stale knowledge/reference source that was never updated after that change — not a sudden model regression (A), a capability issue (C), or a prompt rewrite (B) that would need constant manual updating rather than fixing the actual stale source once.

---

### Q100.
A specialty food distributor's finance team has a Claude-assisted monthly rebate-calculation workflow that computes rebate amounts owed to retail partners via code execution, with a finance analyst reviewing and approving the computed rebate file before payments are released. A new efficiency proposal suggests removing the analyst's review step specifically for retail partners whose rebate calculation has matched the prior month's amount within 1%, "since a near-identical result to last month is itself evidence of correctness."
**Options**
- A. Approve the proposal — a near-identical result to a previously-approved, correct calculation is meaningful corroborating evidence that this month's calculation is also likely correct
- B. Do not approve: a rebate close to last month's is consistent with correctness but equally with silently stale inputs; similarity isn't independent verification, so keep the review.
- C. Approve the proposal, but only reinstate the review step if the match tolerance is tightened from 1% to 0.1%
- D. Approve the proposal, but require a lighter-touch review (a quick glance rather than full verification) for the matching partners instead of removing review entirely

**Answer:** B — This is a deliberately tricky closing question because "matches last month" sounds like a form of the known-answer verification principle, but it's actually the opposite: it's an untested assumption that stability implies correctness, when stability could just as easily result from a silent input error (e.g., accidentally reusing last month's sales figures) — reversibility/accountability at the payment-release point is what the review step actually protects, independent of how similar results happen to look, and neither a tighter tolerance (C) nor a lighter-touch review (D) addresses that the similarity itself proves nothing about correctness.

---
[⬅ PCAO-F Index](README.md) · [Companion set: `pcaofexamquiz.md`](pcaofexamquiz.md)
