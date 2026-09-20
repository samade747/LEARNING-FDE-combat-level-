# PCAO-F / CCAO-F — 100-Question Max-Difficulty Scenario Bank (`pcaofexamquizv2.md`)

*Third tier in this folder's difficulty ladder: [`pcaofexamquiz.md`](pcaofexamquiz.md) (100-Q, real-exam
hard) → [`pcaofexamquizv1.md`](pcaofexamquizv1.md) (100-Q, one notch harder) → this file (100-Q,
**maximum difficulty**). Same relationship as `../ccao-f/quiz100.md` → `../ccao-f/hardquiz.md` →
`../ccao-f/`'s own extreme tier. Every scenario here is new (no reuse from the two companion files).
What makes this tier harder: longer vignettes carrying at least one deliberate red-herring detail;
wrong options that are each a *correct application of a different, real CCAO-F/PCAO-F principle*,
just misapplied to this specific scenario (so pattern-matching "which principle is this" is not
enough — you must identify which principle is the *deciding* one here); and a higher share of
multi-select items. Domain-weighted identically to the published blueprint:*

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

Read every stem twice. Answer + explanation follow each question — cover them for a clean self-test pass.

---

## Domain 2 — Output Evaluation and Validation (21% — Q1–Q21)

### Q1.
A regional dairy cooperative's quality-assurance lead has Claude reconcile monthly milk-fat testing results across 40 member farms against lab-reported values. This month's reconciliation matches a prior month whose correct result was hand-verified, and separately, the cooperative just adopted a new lab-testing vendor two weeks ago whose report format differs slightly from the old vendor's. The QA lead wants to stop hand-checking future months.
**Options**
- A. Keep hand-verifying for a few months: the new vendor's format change means the earlier match, verified under the old format, doesn't yet establish reliability.
- B. Hand-check only the farms whose fat content changed by more than 0.5% this month, treating stable farms as pre-verified
- C. Ask Claude to flag any reconciliation result that looks inconsistent with the new vendor's typical reporting patterns, and rely on that flag instead of hand-checking
- D. Stop hand-checking — the matched prior month is sufficient, ongoing proof of reliability

**Answer:** A — This is a harder version of the known-answer-test principle specifically because the "match" evidence (real and legitimate) predates a relevant environmental change (the new vendor format) that the associate must notice matters — earned confidence from a prior period doesn't automatically transfer across a change in the underlying data source, even when the match itself was genuine.

---

### Q2.
A marine-cargo insurer's claims associate asks Claude, in one chat, "Why do cargo claims from Port A get approved faster than from Port B?" and receives a confident, well-cited operational explanation. Days later, in a fresh chat, a colleague asks "Why do cargo claims from Port B get approved faster than from Port A?" — using the same historical claims dataset attached both times — and also receives a confident, well-cited explanation, with different citations from the same dataset.
**Options**
- A. This is context overload, since the second chat inherited assumptions from the first colleague's earlier discussion of the topic
- B. This is run-to-run randomness, and re-running the identical question a third time would likely resolve which port is actually faster
- C. This proves the dataset is corrupted, since it produced two contradictory conclusions
- D. It is sycophancy from leading framing, but both answers used the same dataset, so first check whether the data supports either directional claim.

**Answer:** D — The scenario is designed so the sycophancy pattern is present (correctly identified in D) but incomplete as a full answer — since both chats used the *same* source data, the real next step is checking the data itself for what it actually supports, rather than stopping at "the framing was leading" or assuming corruption (C) or randomness (B) without checking.

---

### Q3.
A specialty pharmaceutical distributor's regulatory associate asks Claude to summarize stability-testing data for a temperature-sensitive product. The summary states "the product remains stable for 18 months at 2–8°C, per the attached study," and separately, in a different paragraph of the same summary, states "stability data supports a 24-month shelf life under refrigerated conditions."
**Options**
- A. Average the two durations (21 months) as a defensible compromise figure
- B. Use the more generous figure (24 months) only if the client specifically requests a longer shelf life
- C. Use the more conservative figure (18 months) as the safer choice between the two, without further checking
- D. Treat the two stability durations for the same condition as a hallucination signal and trace both figures to the attached study before any regulatory use.

**Answer:** D — Two different numeric claims about what should be the same underlying fact (shelf life under refrigeration) is a specific, reliable hallucination signature — picking the "safer-sounding" one (C), a compromise (A), or a business-driven pick (B) all skip actually resolving which, if either, the source study supports.

---

### Q4.
A metropolitan waste-management authority runs an AI-assisted illegal-dumping detection system across sensor and camera data from 200 collection routes, flagging 25 routes weekly for enforcement follow-up. The enforcement team investigates all 25 flagged routes each week for two months and confirms genuine dumping activity in the large majority of cases, calling the system "highly accurate."
**Options**
- A. This two-month track record on the flagged routes is sufficient to certify the system's overall accuracy
- B. Ask the system to self-report a confidence score for the unflagged routes and treat a low aggregate score as reassurance
- C. Increase the number of routes flagged weekly to improve overall coverage
- D. Also sample the 175 unflagged routes: precision on flagged routes says nothing about recall, and dumping in sensor blind spots is a separate unaddressed question.

**Answer:** D — This is the systemic-triage-risk pattern again, but the harder distractor here (B) offers a *plausible-sounding* alternative to human sampling (a self-reported confidence score) that is still fundamentally a self-report from the same system being evaluated, not independent verification.

---

### Q5.
A commercial aviation MRO (maintenance, repair, overhaul) facility's associate asks Claude to extract every torque-specification value from a 60-page maintenance manual for a specific aircraft component. The output lists 14 torque specs, each with a page and paragraph citation. The associate opens 4 of the 14 citations at random; all 4 match exactly.
**Options**
- A. Cross-check the 14 values against a second AI tool's independent extraction, and accept the list if the two tools agree on all 14
- B. Confirm the remaining 10 citations too: for safety-critical torque values a matching partial sample doesn't rule out error in the unchecked majority.
- C. A 4-of-14 matching sample is proportionally sufficient confirmation, given the manual's length
- D. Ask Claude whether the list of 14 is complete and accurate, and accept a confident answer

**Answer:** B — This intentionally offers A as a tempting, genuinely-independent-sounding alternative (a second AI tool), but for a safety-critical extraction where a single wrong torque value has severe consequences, full verification against the actual source document is the standard the stakes call for — cross-model agreement remains a progress signal, not a substitute for confirming safety-critical values directly.

---

### Q6.
A municipal water-treatment plant's compliance officer has Claude draft a chemical-dosing incident summary for a regulatory filing, then asks Claude, in the same conversation, to "now review this summary as an independent EPA auditor would, and flag any issues." The auditor-persona pass identifies two additional concerns and revises the summary's risk characterization downward.
**Options**
- A. Still not independent: same model and context whatever the persona, so a regulatory filing needs a separate check such as the incident logs or a qualified reviewer.
- B. This satisfies independent verification for a regulatory filing, since an adversarial persona was explicitly used
- C. This satisfies independent verification only because the persona pass found *additional* concerns, proving it added real scrutiny
- D. This is unnecessary additional verification, since compliance officers are already domain experts

**Answer:** A — The persona pass genuinely improved thoroughness (as reflected in finding two new concerns), which is what makes C tempting — but improved thoroughness from the same model in the same context is not independence, and a regulatory filing's stakes call for a genuinely separate verification path.

---

### Q7.
A theme-park operations team receives a Claude-built staffing-cost spreadsheet built from raw shift-log exports, to be used for next season's budget. Every visible formula in the spreadsheet is correct for the twelve rows the finance associate spot-checks, and the computation was done via executable formulas rather than prose. Separately, the associate notices the spreadsheet's total headcount figure is slightly higher than the plant's actual current headcount roster.
**Options**
- A. Ask Claude to explain the headcount discrepancy and accept its explanation if it identifies a specific cause
- B. Since the sampled formulas are correct and the computation method (executable formulas) is sound, the headcount discrepancy is likely just a rounding artifact and can be safely ignored
- C. Re-verify the sampled twelve rows a second time, which would resolve the discrepancy if a formula error existed
- D. Investigate the headcount gap as possible stale or duplicate source records; correct spot-checked formulas don't rule out a wrong source range.

**Answer:** D — This is a harder version of the "correct formula, wrong data range" pattern: a real, observable anomaly (headcount mismatch) is present, and the correct move is to investigate the *source data* behind an otherwise well-built computation, not dismiss it as rounding (B), re-check already-verified rows again (C, which wouldn't reveal a source-data issue), or accept a self-generated explanation (A) without confirming it against the actual roster.

---

### Q8.
A professional sports league's front office asks Claude and a second AI tool to independently project which of eight draft prospects will have the best rookie-season performance, using the same scouting-report inputs for both tools. The two tools agree on the top 3 prospects but rank prospects 4 through 8 in nearly opposite order.
**Options**
- A. Since the tools agree on the most important ranking (top 3), the disagreement on the remaining five is immaterial and can be ignored
- B. Have both tools re-run the ranking together in one shared session until prospects 4–8 converge
- C. Discard both AI rankings entirely for prospects 4–8, since disagreement there suggests the tools are unreliable overall
- D. Treat the disagreement on prospects 4-8 as the signal for deeper human scouting there; the top-3 agreement, from the same inputs, is comfort, not proof.

**Answer:** D — The harder distinction here is recognizing that agreement built from *identical* input data is weaker evidence than independently-sourced agreement (echoing the demand-forecast principle), while the *disagreement* zone is still the correctly actionable signal — neither dismissing it (A) nor overreacting to discard everything (C) nor forcing artificial convergence (B) is right.

---

### Q9.
A state historical-preservation office asks Claude to confirm the current statutory threshold (in square footage) above which a renovation project triggers mandatory historical review. Claude cites "Preservation Code §9.2(c)" and states 5,000 square feet — a figure that happens to exactly match a training reference the associate recalls from a preservation-law course taken years ago.
**Options**
- A. Since the figure matches independent prior training knowledge (not just the associate's assumption), this constitutes sufficient corroboration
- B. Ask a colleague whether 5,000 square feet "sounds right" as a tie-breaking check
- C. Accept the figure, since two independent recollections (the citation and the associate's training) now agree
- D. Still confirm the citation against current statute text: matching prior training, whose currency is unknown, is reassuring but not verification.

**Answer:** D — This is a harder version of the confirmation-bias trap: unlike simply matching the associate's own unverified assumption, this scenario offers a more sophisticated-sounding corroboration (independent prior *training*) to test whether the test-taker still recognizes that neither source's *current* accuracy has actually been checked against the live statute — training knowledge has its own unknown currency date and doesn't substitute for checking the current source.

---

### Q10.
An agricultural cooperative's operations team has Claude reconcile 24 months of grain-silo intake weights against member-farmer delivery receipts in one request, producing a payment-discrepancy report. An auditor later discovers a systematic error: one silo's scale was recalibrated eight months ago, and the reconciliation silently applied the *old* calibration factor to all 24 months, including the 16 months after recalibration, because the calibration factor was embedded once at the top of the associate's original prompt rather than tracked as a time-varying input.
**Options**
- A. Decompose the process: profile and confirm time-varying inputs, such as a mid-period recalibration, as their own verified step before reconciliation.
- B. The fix is adding "make sure to double check calibration factors" to the same single-pass prompt for future runs
- C. The fix is re-running the same single-pass request on a more capable model, expecting it to infer the recalibration event on its own
- D. The fix is shortening the reconciliation window to 8 months at a time, repeating the same single-value-embedding approach four times

**Answer:** A — This is a genuinely novel failure mode (a time-varying input treated as static) beyond simple unit-conversion errors — the fix requires explicitly surfacing and confirming whether any input changed *during* the period being analyzed, which added carefulness wording (B), a bigger model (C), or merely shortening the window while repeating the same flawed static-input approach (D) would not reliably catch.

---

### Q11.
A wildlife-conservation nonprofit has Claude summarize a 180-page ecological impact assessment for a donor briefing. The summary is fluent, well-cited, and the associate confirms 5 of 20 citations match their source pages exactly. Separately, the summary characterizes the assessment's overall conclusion as "strongly supportive of the proposed conservation corridor," while the actual assessment's executive summary (which the associate has not read) uses more qualified language.
**Options**
- A. Confirm the remaining 15 citations as well, which would resolve the characterization concern
- B. Ask Claude to quote the assessment's exact conclusion language and treat a direct quote as sufficient confirmation of the characterization
- C. Have someone with ecological-assessment expertise verify the overall characterization, not just citations: accurate citations can still overstate or understate the source's qualified conclusion.
- D. Since the sampled citations check out, the overall characterization is likely accurate too

**Answer:** C — This is a harder version of the "fluency and citation-accuracy aren't the same as characterization accuracy" principle: even checking all remaining citations (A) wouldn't verify the *overall tone/strength* the summary attributes to the source, which requires either reading the source's own conclusion directly or expert judgment — not further citation-level checking.

---

### Q12.
A national pension-fund administrator has Claude and a competing AI tool independently project a fund's required contribution rate for the coming year, using the same actuarial input dataset. The two projections land within 0.3 percentage points of each other, and separately, both projections use a mortality-assumption table that was current five years ago but has since been updated by the actuarial standards board.
**Options**
- A. The close agreement between the two tools is strong, sufficient evidence the projection is sound, given both used the same rigorous actuarial dataset
- B. The close agreement is irrelevant, since the fund's actual contribution rate is set by regulation regardless of any projection
- C. The close agreement should be treated as full proof, since two independently-built systems converging this closely is inherently reliable
- D. Agreement is only moderately reassuring: both tools may share an outdated mortality table in the input data, so confirm the current table first.

**Answer:** D — This is a harder version of the "shared input data limits the value of cross-model agreement" principle, now with a specific, identifiable shared flaw (an outdated mortality table) that both tools inherited — the close numeric agreement is real but doesn't detect a flaw common to both, which is exactly the scenario where cross-model agreement is weakest as evidence.

---

### Q13.
A film-production company's marketing associate frames a request as: "Our test-audience scores were disappointing — confirm that this is because the trailer's pacing was too slow, so we can justify a re-edit to the studio." Claude returns a detailed analysis attributing the low scores to pacing, citing specific test-audience comment excerpts.
**Options**
- A. This is acceptable as long as the associate personally reads the full set of test-audience comments afterward, not just the cited excerpts
- B. The framing presupposes the cause and the goal, and real comments can be selectively surfaced; ask instead for the strongest evidence across several causes.
- C. This is acceptable because test-audience comments are direct customer feedback and cannot be manipulated by framing
- D. This is an acceptable evaluative process, since specific, real audience comments were cited in support of the conclusion

**Answer:** B — This raises the stakes on the leading-question pattern by presupposing *two* things at once (the cause and the desired remedy), which makes the eventual "evidence" doubly likely to be selectively assembled — reading the full comment set (A) helps but doesn't substitute for asking an unbiased, multi-cause question in the first place.

---

### Q14.
A veterinary-hospital chain's AI-assisted triage-support tool has matched licensed-veterinarian triage decisions in 990 of 1,000 audited historical emergency cases (99%). Leadership proposes removing the veterinarian-confirmation step specifically for the lowest-severity triage category, which represents 70% of case volume and showed zero mismatches in the audit, while keeping the confirmation step for all higher-severity categories.
**Options**
- A. Approve the removal, but require the audit to be repeated with double the sample size first
- B. Approve the removal for the low-severity category — a 70%-volume category with zero mismatches, sitting within an already-excellent 99% overall audit, meets a reasonable bar for automation
- C. Keep the veterinarian checkpoint: animals can't report symptoms, low-severity misclassifications can deteriorate quickly, and accountability doesn't transfer on a favorable historical slice.
- D. Approve a partial removal — a veterinarian reviews only 15% of low-severity cases going forward, selected at random

**Answer:** C — This deliberately maximizes the temptation (99% overall, 70% volume, zero mismatches in that specific slice) to test whether the underlying principle — that safety-relevant checkpoints don't get removed based on retrospective favorable numbers, regardless of how favorable — still holds; larger samples (A) or partial spot-review (D) don't change the underlying accountability logic.

---

### Q15.
A commercial fishing-fleet insurer's underwriting team has Claude flag vessel-insurance applications for manual underwriter review based on risk indicators including vessel age, captain's safety record, and home port. Every one of the 210 flagged applications this quarter, reviewed by underwriters, is confirmed as a genuinely appropriate flag. Separately, flagged applications are noticeably concentrated among vessels whose home port is a specific small fishing community historically associated with a particular ethnic-minority fishing tradition.
**Options**
- A. Quietly remove home port as an input factor going forward, without escalating, since the correlation is now apparent
- B. Escalate the home-port concentration to the fairness owner despite justified individual flags: an input correlated with a marginalized community can create disparate impact.
- C. Since every individual flagged case held up under underwriter review, the home-port concentration is incidental and doesn't need further attention
- D. Continue as-is, since insurance risk factors are generally exempt from fairness review when actuarially justified

**Answer:** B — As with the earlier ZIP-code-pricing and complaints-queue patterns, individual-case accuracy doesn't resolve a separate aggregate-fairness question, and this scenario adds a layer (an actuarially-plausible-sounding justification, D) that a test-taker might use to wave off the concern entirely — actuarial plausibility doesn't substitute for the compliance owner's own fairness review, and unilaterally changing the model without escalation (A) also bypasses that owner's authority.

---

### Q16.
A private-equity due-diligence associate has Claude build a working-capital adjustment schedule from a target company's trailing-twelve-month financials. Every individual line item the associate spot-checks against source financials is correct, and the schedule's final adjustment figure — which will directly reduce the purchase price in the deal — is described by Claude as "calculated by summing the quarterly net working capital changes shown above."
**Options**
- A. Have the final summation performed and shown via executable calculation against the confirmed quarterly figures, not accepted as a prose sum.
- B. Accept the final adjustment figure, since the individual quarterly line items were all confirmed correct
- C. Spot-check one additional quarterly line item for extra assurance before accepting the final sum
- D. Ask Claude to recompute the sum and confirm it matches its own original figure

**Answer:** A — This is the aggregation-error principle at its highest stakes (a purchase-price-determining figure): confirmed-correct individual quarters still don't guarantee a correctly executed final sum, which needs to be shown as an actual computation, not inferred from correct inputs or re-confirmed by the same source that stated it (D).

---

### Q17.
An orchestra's development office needs Claude's help deciding whether a lapsed major donor is likely to re-engage if approached this season. Which single request best supports an honest assessment rather than a case for a predetermined approach?
**Options**
- A. "Rate this donor's re-engagement likelihood from 1–10 and explain your reasoning."
- B. "Based only on the donor's giving history and past engagement notes, lay out the strongest case for approaching this donor this season and the strongest case for waiting, before recommending either."
- C. "This donor has been quiet for a while — is now a good time to reach out?"
- D. "This donor seems like a good re-engagement candidate — build the case for approaching them this season."

**Answer:** B — As with the earlier campaign-continuation example, explicitly requesting both sides grounded in the actual data, before any recommendation, avoids presupposing a conclusion — C and D both lead toward one direction, and A's single-number rating can sound rigorous while still reflecting an unstated, unexamined lean.

---

### Q18. *(Select TWO — all-or-nothing)*
A regional trauma center's clinical-informatics associate is deciding which of five upcoming Claude-assisted tasks need a second, independent verification path beyond their own read-through. Which **TWO** most clearly require it?
**Options**
- A. Extracting drug-interaction contraindication thresholds from a pharmacology reference that will populate an automated prescribing-alert system
- B. Summarizing a hospital department's monthly all-staff newsletter content
- C. Calculating a pediatric weight-based medication dosing table that feeds directly into a nurse's dosing calculation without an independent pharmacist check before administration
- D. Drafting talking points for a hospital's annual volunteer-appreciation event
- E. Drafting a general patient-education handout about post-surgical wound care, reviewed and approved by a nurse before distribution

**Answer:** A, C — Both feed directly into consequential, safety-relevant systems (an automated prescribing-alert system; a pediatric dosing calculation without an independent pharmacist check) where an error compounds badly and no adequate independent check currently exists downstream. E already has a nurse review built in for a lower-stakes handout; B and D are low-stakes informational content.

---

### Q19.
A federal contractor's export-control compliance team has Claude review 15,000 technical documents and tag 620 as "potentially export-controlled — hold for legal review." Outside counsel reviews a random sample of 80 of the 620 tagged documents and confirms all 80 were correctly tagged as potentially controlled.
**Options**
- A. Ask Claude to re-scan the untagged documents and self-report a confidence level that none were missed, accepting a high self-reported confidence as sufficient
- B. The sample validates only the flagged side; sample the 14,380 untagged documents defensibly before release, since a missed export-controlled document has severe legal consequences.
- C. This sample sufficiently validates the tagging system; proceed to hold all 620 for legal review and release the rest
- D. Increase the sample size on the flagged side to 150 for extra confidence, which resolves the concern

**Answer:** B — This is the systemic-triage-risk pattern at its highest-stakes form in this bank (federal export-control violations), and as with the privileged-document scenario, checking the flagged side thoroughly (however large the sample) says nothing about false negatives in the much larger unflagged population.

---

### Q20.
A commercial airline's flight-operations team asks Claude to explain a proposed fuel-load optimization recommendation for a specific route. The explanation is detailed, internally consistent, and describes a chain of reasoning about historical wind patterns and aircraft weight. The recommendation, if wrong in the conservative direction (loading slightly more fuel than optimal), costs a small, easily-absorbed efficiency loss; if wrong in the other direction (loading less), it raises a safety margin concern requiring standard regulatory fuel-reserve minimums to still be independently confirmed regardless.
**Options**
- A. No fuel-load recommendation should ever be optimized by AI assistance in an aviation context under any circumstances
- B. A separate mandatory control protects the fuel-reserve floor and the guarded error is low-cost, so the efficiency reasoning can be acted on without independent verification.
- C. The explanation's internal consistency is itself sufficient verification, regardless of what other controls exist or don't
- D. Detailed, consistent-sounding reasoning about fuel loads must always be independently verified against actual wind and weight data before any adjustment, given aviation's inherent safety stakes, regardless of what other controls exist

**Answer:** B — This is a harder version of the "match verification rigor to actual stakes and reversibility" principle from the earlier fare-recommendation question, now deliberately set in a superficially high-stakes domain (aviation) to test whether the test-taker over-applies maximum verification regardless of context — the key detail is that the safety-critical floor (regulatory minimums) is protected by a separate, mandatory, independent control either way, which changes how much additional verification the *efficiency-optimization* layer specifically needs.

---

### Q21.
A university's institutional-research office wants to validate a new Claude-assisted graduation-risk prediction tool before using it to allocate limited academic-advising resources. Which validation approach most rigorously tests whether the tool can be trusted, as opposed to merely appearing trustworthy?
**Options**
- A. Have five advisors review a semester's worth of the tool's risk flags and rate each as "seems right" or "seems off," aggregating their impressions
- B. Ask the tool to explain its prediction methodology and have an institutional researcher judge whether the explanation sounds statistically sound
- C. Run the tool on several past cohorts' known, withheld outcomes across more than one program, checking whether accuracy holds by program or group.
- D. Run the tool twice on the same cohort's current students and check whether the two outputs are consistent

**Answer:** C — This is a harder version of the known-answer test, specifically requiring *multiple* known-answer comparisons across *different* populations (not just one matched cohort, as a simpler version of this question might accept) — resource-allocation decisions affecting real students demand checking whether accuracy is consistent across the different groups it will be applied to, not just validated once.

---

## Domain 4 — Workflow Integration and Solution Design (16% — Q22–Q37)

### Q22.
A national semiconductor manufacturer's fab-operations director says: "We want Claude handling our equipment-downtime incident reports so they get filed faster and more consistently — that's really the whole ask." The director considers this a complete brief since both the goal (speed and consistency) and the workflow (incident reports) are named.
**Options**
- A. Ask the fab-operations team to select the AI tooling first, since the goal and workflow are already clear
- B. Still settle the other elements: report fields and format, recipient and system, trigger and source data; 'faster and more consistently' describes properties, not content.
- C. Since both a goal and a named workflow are provided, this is sufficient specification to begin building
- D. Proceed directly, treating "faster, more consistent incident reports" as sufficient specification for a safety-relevant reporting workflow

**Answer:** B — This is a harder version of the task-definition trap because *two* things are given (a stated goal and a named workflow), which makes it more tempting to treat the brief as complete — but neither actually resolves the concrete "what/for whom/how triggered/from what data" questions that still need settling before building, especially for a safety-relevant equipment-downtime process.

---

### Q23.
A regional dialysis-clinic chain's clinical-operations team has Claude flag treatment-session anomalies (e.g., unusual fluid-removal-rate patterns) for a charge nurse's review before the next scheduled session for that patient. A proposal suggests letting Claude auto-adjust the flagged patient's *next* session parameters directly, without nurse review, specifically for anomalies the system scores as "low severity," arguing the severity scoring is code-executed and has shown zero clinically significant misses in six months of shadow-mode operation.
**Options**
- A. Approve auto-adjustment, but require the charge nurse to review a written summary after the adjustment is already made
- B. Approve auto-adjustment only for the lowest 10% of severity scores, as a narrower compromise
- C. Do not approve: adjusting a live patient's treatment is consequential and hard to reverse, accountability doesn't transfer, and shadow-mode success isn't live authority.
- D. Approve auto-adjustment for low-severity flags — six months of shadow-mode data with zero misses, combined with code-executed (not prose-generated) scoring, meets a reasonable evidence bar

**Answer:** C — This combines several tempting justifications (code-executed precision, a clean track record, *and* a specific evidentiary detail — shadow-mode operation, meaning the system watched but never actually acted) to test whether the test-taker also catches that shadow-mode success is not equivalent evidence to live decision-making performance, on top of the underlying accountability-doesn't-transfer principle.

---

### Q24.
A container-shipping line's proposal for an AI-assisted cargo-manifest discrepancy workflow states: "Claude flags manifest discrepancies above a 2% weight variance; a cargo compliance officer confirms the flagged discrepancy's cause and clears or holds the container before it's loaded." A reviewer argues this wording is already a complete, well-defined control, since it names the trigger (2% variance), the role (compliance officer), the specific check (confirming the cause), and the timing (before loading).
**Options**
- A. It doesn't address discrepancies below the 2% threshold that may warrant attention with other factors; a defined gate at one threshold doesn't show it's calibrated.
- B. The wording is genuinely complete — it satisfies WHO, WHAT, and WHEN explicitly, and no further refinement is needed
- C. The wording is incomplete because it doesn't specify which AI model performs the flagging
- D. The wording is incomplete because it doesn't name the specific compliance officer by name

**Answer:** A — This is designed so that B is highly tempting (the WHO/WHAT/WHEN elements genuinely are all present, unlike the earlier freight-routing example), which tests whether the test-taker can identify a *different* kind of gap — not a missing gate element, but an unexamined boundary condition (the threshold itself, and near-threshold cases) that a well-specified gate can still have.

---

### Q25.
A twelve-branch credit union is redesigning its mortgage-document intake around Claude. Two changes are planned: consolidating five separate document-request emails into one, and moving repeated regulatory-disclosure language into a Project's standing instructions. Leadership wants an ROI figure for a board vote next week, and separately, three of the twelve branches have significantly different document intake volumes and complexity than the other nine due to differing regional loan-product mixes.
**Options**
- A. Establish a baseline by measuring the current, unchanged process at a single representative branch, then apply that baseline's implied improvement across all twelve branches for the board figure
- B. Report a range instead of a single ROI figure, based on the planned changes' theoretical maximum and minimum impact, without measuring any actual baseline
- C. Make the two planned changes at all twelve branches immediately, then measure the new process only, comparing against branch managers' general recollection of typical past processing time
- D. Baseline each distinct branch group first: one branch may not represent the other's time, revision rounds or manual steps, though any real baseline beats an estimate.

**Answer:** D — This is a harder version of the baseline-before-optimizing principle: measuring *a* baseline (as in A) is real progress over not measuring at all, but the added complexity here (meaningfully different branch types) means a single branch's baseline may not generalize, and the correct answer requires recognizing that heterogeneity, not just accepting any single measured baseline as sufficient.

---

### Q26.
A large logistics company connected its customs-documentation folder to Claude with read-only access to summarize incoming import declarations. A new initiative wants Claude to also automatically generate and save a standardized cover-sheet PDF into that same folder for each declaration, without modifying or moving any existing files.
**Options**
- A. This should be solved with a Skill that defines the cover-sheet template and generation logic, since read access plus clear logic is sufficient for creating new content
- B. This is achievable today since generating and adding a *new* file, without touching existing ones, is a lesser action than the write actions (moving, renaming, deleting) that clearly require deliberate permission
- C. This requires no connector change, since the new PDF is unrelated to the existing declaration files already being read
- D. Saving a new file is still a write action: adding versus modifying doesn't change that write access must be deliberately granted and confirmed, separate from read-only access.

**Answer:** D — This tests a specific, tempting distraction: the intuition that *adding* a new file is somehow lower-risk or different in kind from *modifying* existing ones, and therefore might not need the same deliberate write-access step — but both are write actions to the destination, and the distinction doesn't change the underlying permission requirement.

---

### Q27.
A children's hospital's medication-reconciliation workflow has five steps. Step 2 (comparing a patient's home medication list against newly prescribed hospital medications to flag potential duplications or interactions) is classified as "collaborative," with a pharmacist reviewing every flag. A proposal suggests reclassifying Step 2 as "AI-appropriate" specifically for patients on fewer than three total medications, arguing the complexity (and thus error risk) of reconciliation scales with medication count, so a low count represents a genuinely lower-stakes case.
**Options**
- A. Approve the narrower reclassification — medication count is a defensible, task-relevant complexity proxy, and lower complexity genuinely can mean lower stakes for this specific kind of task
- B. Approve the reclassification, but require the pharmacist to review a monthly summary of the reclassified cases retroactively instead of reviewing prospectively
- C. Do not approve: a missed interaction is equally harmful for a child on fewer medications, so the step's own accountability and reversibility profile governs its class.
- D. Approve the reclassification, but only for patients under a specific age threshold rather than medication count

**Answer:** C — This is a genuinely harder question than the earlier discharge-summary example because the proposed proxy (medication count correlating with task complexity) is actually reasonable as a complexity signal — the key distinction the correct answer draws is that *stakes* (harm severity if an error occurs) doesn't scale down the same way *complexity* does, so a complexity-based proxy doesn't appropriately govern a stakes-driven classification.

---

### Q28.
A cargo-airline's associate describes an AI-assisted load-planning workflow in three versions. The version for the flight-operations team states: "Claude proposes cargo load distributions; a certified load planner verifies weight and balance calculations and signs off before the load plan is finalized, per standard load-planning certification requirements." The version for a prospective corporate client states the same thing, verbatim.
**Options**
- A. The identical wording is a problem because it should be simplified for the client audience by removing the certification-requirement detail entirely
- B. The identical wording is a problem because a prospective client needs additional context the flight-operations team doesn't (why a certified load planner's involvement matters, and what "load-planning certification requirements" means as a credible standard) — audience-appropriate framing is always required, even when the control itself doesn't differ
- C. Identical wording for both audiences is appropriate, since the process and control don't change and the description already names WHO, WHAT and WHEN clearly.
- D. The identical wording is a problem only if the client is unfamiliar with aviation terminology

**Answer:** C — This is a deliberately counter-intuitive correct answer testing whether the test-taker over-applies "always rewrite per audience" mechanically: unlike the earlier CFO/technical-lead/risk-team example (where different audiences genuinely needed different framing to act on), this description already contains the full WHO/WHAT/WHEN gate in accurate, audience-neutral terms, and reusing accurate, complete wording verbatim across two audiences is not itself a flaw when the underlying control and the reader's actual need for information happen to be the same — the principle is "match content to audience need," not "always produce a different version."

---

### Q29. *(Select TWO — all-or-nothing)*
A regional dialysis-clinic chain is expanding an AI-assisted treatment-scheduling exception workflow. Which **TWO** of the following five proposed changes would leave the system with more authority than its risk profile allows?
**Options**
- A. Let Claude auto-approve minor session-time adjustments (within a 30-minute window) based on patient-reported scheduling conflicts, with a scheduling coordinator notified after the fact rather than approving beforehand
- B. Let Claude draft a clinical rationale for treatment-frequency exception requests, with a named nephrology charge nurse required to approve or reject before it takes effect
- C. Use Claude to flag potential fluid-overload risk patterns via code-executed threshold comparisons against lab values, with the existing nephrologist approval gate unchanged and immediately following
- D. Move routine appointment-reminder drafting into a reusable Skill so it runs the same way for every scheduling coordinator
- E. Have a charge nurse approve 25 daily treatment-parameter exceptions by glancing at Claude's one-line summaries, without opening any chart, to meet a shift-change deadline.

**Answer:** A, E — A grants auto-approval authority (notification-after-the-fact is not approval-before-action) for a scheduling change that, while framed as "minor," still affects a dialysis patient's treatment timing without a human decision point beforehand. E keeps a human "in the loop" in name only — approving 25 clinical exceptions from one-line summaries without opening any chart is a rubber stamp, not real review. B, C, and D all preserve substantive human decision-making at the point that matters.

---

### Q30.
A metropolitan symphony orchestra's operations team drafts a single internal report explaining why a subscription-renewal campaign underperformed its target. The report needs to reach the board's finance committee (who approve next season's marketing budget) and the box-office staff (whose subscriber-outreach call scripts are changing as a result), and separately, both groups will be in the same room for a joint meeting where the report will be presented once.
**Options**
- A. Prepare two written versions, but structure the joint presentation around one narrative signalling which points matter for which group, since a live setting changes the mechanics.
- B. Send the identical report to both groups ahead of time, since a shared meeting means both need the same information anyway
- C. Produce one combined report, using headers to separate "for finance committee" and "for box office" sections
- D. Ask Claude to produce one "balanced, general-audience" version suitable for the joint meeting, to save preparation time

**Answer:** A — This is a harder version of the multi-audience principle specifically because the *shared live setting* is a genuinely different constraint than the earlier separate-email scenario — the underlying principle (organize content around what each audience needs to decide or do) still applies, but its correct implementation adapts to a joint delivery context rather than mechanically producing fully separate, separately-delivered documents as if the audiences would never be in the same room.

---

### Q31.
A specialty coffee importer has Claude extract every quality-certification requirement from a new direct-trade farm agreement and a separate industry-standard certification body's requirements document. The output is a clean list of 19 requirements. Before the sourcing team begins farm audits based on this list, which single next request best protects against a missed obligation, given that the two source documents cover overlapping but not identical certification schemes?
**Options**
- A. Ask for the list reorganized by which farm-visit phase (pre-harvest, harvest, post-harvest) each requirement applies to, for audit-planning efficiency
- B. Add each requirement's exact source and flag any appearing in only one of the two documents, which risk being overlooked if the schemes are assumed redundant.
- C. Ask Claude to cross-check the 19 requirements against general industry best practices for completeness
- D. Have Claude summarize each source document separately and manually compare the two summaries side by side

**Answer:** B — This is a harder version of the two-source traceability principle: rather than just flagging general conflicts (as in the earlier franchise-agreement example), the specific risk here is a requirement appearing in only *one* of two overlapping-but-different certification schemes being treated as redundant/optional when it isn't — surfacing that specific asymmetry is the highest-value addition, more targeted than reorganizing by phase (A) or a general best-practices cross-check (C).

---

### Q32.
A specialty auction house's associate delegates: research and produce a provenance summary for a specific antique item going to auction, given a stated instruction that Claude may note gaps in the provenance record but must not speculate about ownership during any gap period, and must flag explicitly wherever it exercises judgment about how confident a given provenance claim is. In the output, Claude correctly flags one confidence judgment as instructed — but also silently omits a decades-long gap in the provenance record entirely, rather than noting it as a gap (which was explicitly permitted and arguably expected).
**Options**
- A. The original instruction was sufficient, since the one confidence judgment that was made was correctly flagged as instructed
- B. It got the confidence case right but silently omitted the decades-long gap it asked Claude to note, needing a direct completeness check, not just broader flagging.
- C. This is a hallucination, since the provenance gap wasn't in the source materials
- D. This is a context-overload issue, since provenance research often involves lengthy historical records

**Answer:** B — This is designed to be more serious than the earlier "unflagged silent choice" pattern: here, the *exact category* of information the instruction explicitly invited (gaps) was the very thing omitted — worse than an unanticipated discretion category, because it was anticipated and still missed, calling for a direct completeness-verification step rather than simply broadening the flagging instruction's scope.

---

### Q33.
A university's cognitive-neuroscience lab has consent-based access to fMRI scan data collected for a specific study on memory formation, currently sitting in an approved Claude workspace for that study's team. A different lab within the same department, studying an unrelated question about visual attention, requests access to the same dataset, noting that both labs are part of the same IRB-approved department-wide data-sharing agreement that permits "internal departmental research use" of collected neuroimaging data.
**Options**
- A. Deny the request outright, since the data was originally collected for a specific, different study
- B. Approve the request, but only after all identifying information is stripped from the fMRI data
- C. Confirm with the IRB or data-governance owner whether 'internal departmental use' covers a materially different research question than participants consented to; broad-sounding agreements may have scope limits.
- D. Approve the request without further review, since the department-wide data-sharing agreement already permits internal departmental research use, which explicitly covers this situation

**Answer:** C — This is harder than the earlier unrelated-topic data-reuse example because a genuine, broader sharing agreement actually exists here (unlike the earlier case where no such agreement was mentioned) — but the correct answer recognizes that even a real sharing agreement's scope can be ambiguous for a specific new use, and that ambiguity should go to the actual governance owner to interpret, rather than being assumed to clearly cover the new use (D) or dismissed as clearly not covering it (A) by the requesting associate.

---

### Q34.
An AI-assisted patient-appointment no-show prediction tool at a large multi-specialty clinic network appears to assign higher no-show-risk scores to patients using a public transit-dependent commute pattern (inferred from appointment-time clustering and clinic location data) relative to patients with similar appointment histories but car-dependent commute patterns. The clinic operations analyst who noticed this pattern owns the scheduling workflow that uses these scores to decide overbooking levels, but does not own the underlying prediction model's design.
**Options**
- A. Escalate the pattern, with who is affected and what could go wrong, to the owner of model design and equity policy; using outputs isn't authority over inputs.
- B. Take no action, since the analyst doesn't own the model design and the pattern falls outside their explicit responsibilities
- C. Since the analyst owns the scheduling workflow that *uses* the scores, adjust the overbooking formula directly to compensate for the apparent pattern, without escalating to the model's owners
- D. Ask the prediction tool directly whether its scoring is biased by commute pattern, and act only if it confirms bias

**Answer:** A — This sharpens the operational-vs-policy-ownership distinction from the earlier vendor-risk-scoring example: the analyst has real authority over how scores are *used* (overbooking formula) but not over whether the underlying model's *inputs* are appropriate — the correct answer keeps the analyst from either overstepping into model redesign (C) or under-acting by treating this as entirely outside their concern (B).

---

### Q35.
A specialty-crop agricultural cooperative wants to establish whether a new Claude-assisted crop-disease identification tool (using photos submitted by member farmers) can be trusted before wider rollout across its 40-member network. The tool performed well in a 6-week pilot involving photos submitted by the 5 founding member farms that helped design the photo-submission format and disease taxonomy used.
**Options**
- A. Extend the pilot with the same 5 founding farms for an additional 6 weeks before deciding
- B. Roll out network-wide immediately, since 5 farms already provides meaningfully more diversity than a single-site pilot
- C. Test against known-answer cases from farms outside the five that shaped the taxonomy, ideally with different crops or regions, before claiming the pilot generalizes.
- D. This pilot result establishes sufficient trust for network-wide rollout, since it was a real, multi-week test with real farmer-submitted photos across multiple farms (not just one)

**Answer:** C — This is a harder version of the founding-facility-bias pattern because the pilot already involves multiple farms (5, not 1), which makes it more tempting to treat as sufficiently diverse (as in B) — but all 5 still share the specific bias of having helped design the tool's own format and taxonomy, which is a different and more specific concern than simple site-count diversity.

---

### Q36.
A specialty medical-device distributor redesigns its product-complaint intake workflow around Claude. Eight months in, an audit finds the redesigned process is measurably faster (a 50% reduction in intake-to-triage time) but that two complaints involving a specific device malfunction pattern were triaged as "low priority — customer education issue" when they should have been flagged as a potential reportable adverse event requiring regulatory notification.
**Options**
- A. Add training for the specific two customers' complaint handlers, and continue monitoring without further workflow changes
- B. Since the overall speed goal was met and only two complaints out of many were affected, treat these as isolated triage errors to be corrected individually, with no workflow change needed
- C. Re-examine the triage step for a structural gap in separating customer-education issues from reportable malfunctions, rather than treating two same-type misses as one-offs.
- D. Revert the entire redesigned workflow back to the fully manual process, since any regulatory-reportability miss invalidates the redesign

**Answer:** C — As with the food-safety-certification example, when a compliance-critical classification specifically fails (and here, *twice*, for the *same type* of underlying issue — a device malfunction pattern), the structural classification logic itself needs re-examination, not individual-case correction (A, B) or a full revert (D) disproportionate to a specific, identifiable, fixable gap.

---

### Q37.
A precision-agriculture technology company writes three descriptions of an AI-assisted crop-yield prediction product — for its engineering team, for its board, and for a prospective institutional-investor client performing due diligence. The investor-facing version states: "Our AI-assisted platform predicts yield within a 92% accuracy range across our current customer base, validated against three full growing seasons of historical outcomes."
**Options**
- A. It doesn't say whether the 92% holds across crop types and regions or masks weaker subsets, a breakdown a sophisticated investor would want.
- B. This version is fine, since three growing seasons is a sufmpiciently long validation window regardless of breakdown by subgroup
- C. This version should remove the specific percentage entirely for an investor audience, replacing it with qualitative language about "strong predictive performance"
- D. This version is appropriately rigorous for an investor due-diligence audience and needs no further refinement

**Answer:** A — This is a harder version of the "technically true but incomplete disclosure" principle than the earlier invoice-matching example: here the claim already includes real methodological rigor (a specific validation approach, three seasons), which makes the remaining gap (aggregate figure potentially masking subgroup variation) subtler and easy to miss if the test-taker is satisfied by the presence of *some* methodological detail.

---

## Domain 6 — Governance, Risk, and Responsible Use (15% — Q38–Q52)

### Q38.
A large home-insurance carrier wants Claude to auto-generate personalized policy-renewal pricing adjustments based on a customer's claims history, home age, and a predicted "renewal likelihood" score. The renewal-likelihood score incorporates, among other inputs, the customer's historical responsiveness to past communications (measured by email open rates and response speed).
**Options**
- A. Appropriate with review, because responsiveness metrics like open rates can correlate with age, disability or digital access; review this input for disparate impact in renewal pricing.
- B. This is fully appropriate with no review needed, since renewal-pricing personalization is a routine, established insurance practice
- C. This is appropriate-with-review, but only because of the home-age component, not the communication-responsiveness score
- D. This is inappropriate for any AI involvement, since any personalization of insurance pricing is impermissible

**Answer:** A — This is a harder version of the ZIP-code proxy-risk pattern because the risky input here (communication responsiveness) is even less obviously connected to demographic proxies than ZIP code is — which is exactly why it requires deliberate scrutiny rather than being assumed neutral just because it doesn't superficially resemble a classic proxy variable like geography.

---

### Q39.
A large accounting firm's associate can't determine from firm policy whether an AI-assisted preliminary materiality assessment (used internally to help scope an audit) needs to be disclosed to the audit client, given that the client operates in a jurisdiction whose regulator recently issued informal guidance (not yet a binding rule) suggesting AI-assisted audit procedures should be disclosed. The associate escalates to the firm's audit-quality partner.
**Options**
- A. A request to disclose immediately to this one client only, without describing the broader policy question the regulatory guidance raises
- B. A general summary of industry disclosure trends for AI-assisted audit work, with a request for the partner's general thoughts
- C. The procedure, its scoping purpose, the non-binding new guidance, and the single open question of whether it changes disclosure practice, without a firm-wide recommendation the associate can't authorize.
- D. "Given the new informal regulatory guidance, my recommendation is that we should now disclose AI-assisted procedures to this client and all similar clients going forward — please confirm."

**Answer:** C — This is a harder escalation question than the recording-consent example because the correct answer must also recognize a subtler distinction: the guidance is *informal and non-binding*, and the associate's escalation should surface that status accurately rather than either overstating it into a firm-wide recommendation (D) or acting unilaterally on just this one client (A) without surfacing the broader policy question it raises.

---

### Q40.
A boutique architecture firm's principal reviews a proposal to let Claude draft — but never send without human approval — preliminary structural-load calculations for early-stage design concepts, always followed by a licensed structural engineer's independent calculation before any concept advances to permitting. After three years of this workflow operating with zero discrepancies found between Claude's draft calculations and the engineer's independent ones, a project manager proposes: "Given three years of perfect agreement, let's have the engineer simply co-sign Claude's calculations directly for early-stage concepts, rather than independently recalculating from scratch each time — it would save significant engineering hours."
**Options**
- A. Approve the change, but require the engineer to independently recalculate 25% of early-stage concepts at random going forward instead of all of them
- B. Approve the change, but only for early-stage concepts below a certain building size
- C. Do not approve: replacing an independent calculation with a co-sign of the AI's figure changes the check; only a separate path catches errors its method is prone to.
- D. Approve the change — three years of perfect agreement is compelling evidence that independent recalculation is now redundant effort

**Answer:** C — This is a harder version of the "verification method matters, not just track record" principle: unlike the earlier lettings-firm or dialysis examples (which asked whether to remove a checkpoint entirely), this question specifically distinguishes *between two different kinds of check* (independent recalculation vs. co-signing) — a long track record of agreement between the two methods doesn't establish that the weaker method (co-signing) would have caught everything the stronger one (independent calculation) could.

---

### Q41.
A regional pharmacy chain's pharmacists have started using a personal, consumer-grade AI photo-identification app to help identify pills brought in by patients for reconciliation, because the pharmacy's approved clinical system's pill-identification database is frequently out of date for newer generic formulations. Patient information is not directly entered into the consumer app — pharmacists only photograph the pill itself, without any patient-identifying context in the photo or accompanying text.
**Options**
- A. Ban use of the consumer app immediately and provide no interim guidance, since any unapproved clinical tool use should stop immediately regardless of the underlying gap
- B. Report the outdated pill-identification database to the policy owner and supplement the approved tool: lower privacy exposure doesn't remove the gap, and the unapproved app's accuracy is unverified.
- C. This is acceptable as-is, since no patient-identifying information is being entered into the unapproved app
- D. Approve continued use of the consumer app indefinitely, since the specific privacy concern that applied to the earlier photographed-site-report scenario doesn't apply here

**Answer:** B — This is a harder version of the capability-gap pattern specifically because the most obvious risk from the earlier example (patient data exposure) is genuinely absent here, which might tempt a test-taker to conclude there's no real problem (as in D) — but the correct answer identifies a *different* risk (unverified clinical accuracy of an unapproved identification tool) that the absence of a privacy concern doesn't resolve, while still recognizing the underlying capability-gap-first-then-close-the-workaround pattern.

---

### Q42.
A boutique executive-search firm uses an AI assistant's incognito/temporary-chat mode for all compensation-benchmarking research done on behalf of clients, "to keep client-specific salary data out of our shared team history for confidentiality." Separately, the firm's engagement contracts with clients require the firm to retain records of the research methodology used for each search, for a defined period, as a contractual deliverable if requested.
**Options**
- A. Incognito/temporary mode is irrelevant either way, since contractual retention requirements only apply to final deliverables, not research methodology
- B. Incognito/temporary mode should be avoided entirely for this work, since it may prevent the firm from meeting its contractual record-retention obligation to clients
- C. Incognito/temporary mode fully satisfies both the confidentiality goal and the contractual retention requirement simultaneously, since keeping the research out of shared history is itself a form of methodology documentation
- D. Incognito is reasonable and sufficient here: it keeps data out of shared team history without addressing the firm's separate record-retention obligation, which its own process must meet.

**Answer:** D — Similar to the donor-research example, this tests whether the test-taker correctly separates what a private-chat mode does (affects the tool's own history/memory) from a separate organizational obligation (contractual record retention) — the firm needs its own independent process to satisfy the contractual requirement regardless of chat mode, but the chat mode choice itself is not inherently in conflict with that requirement, contrary to B's overcorrection or C's conflation of the two.

---

### Q43.
A regional auto-insurance carrier wants Claude to draft an initial total-loss determination (whether a damaged vehicle's repair cost exceeds a state-defined percentage of its value, triggering a total-loss classification) for claims where the estimated repair cost is unambiguous and comes from a single, already-verified body-shop estimate, with a licensed claims adjuster required to countersign every determination before it's communicated to the policyholder, regardless of how unambiguous the underlying math appears.
**Options**
- A. Fully appropriate with no review needed for the unambiguous cases specifically, since a single verified estimate leaves little room for calculation error
- B. Appropriate with review: WHO, WHAT and WHEN are defined, and the countersign is kept even for clear cases, avoiding 'review only the hard ones' scope creep.
- C. Inappropriate for any AI drafting involvement, since total-loss determinations always require full independent recalculation by the adjuster from source repair estimates
- D. Appropriate-with-review, but the adjuster's review should be replaced by an automated cross-check against a second AI-generated determination for efficiency

**Answer:** B — This question is designed to test recognition of *good* design specifically resisting a tempting scope-creep failure mode (carving out "easy" cases from review, as A proposes) — the correct answer identifies that retaining the countersign requirement uniformly, even for seemingly unambiguous cases, is precisely what prevents the gate from eroding over time as more cases get labeled "unambiguous enough to skip."

---

### Q44.
A staffing agency's AI-assisted candidate-matching tool has operated for three years with strong placement-success metrics, entirely for administrative/clerical roles. A new client asks the agency to apply the *same, unmodified* matching tool and criteria to executive-level searches, arguing "the tool has three years of proven success, so it should transfer directly."
**Options**
- A. Proceed with the same tool and criteria for executive searches, since a three-year track record is substantial evidence of reliability
- B. Decline to reuse the tool and criteria for a different role category without validating it there; a track record on one role type doesn't show the logic suits another.
- C. Proceed with the same tool, but only for executive roles at client companies where the tool has separately been used successfully for administrative roles
- D. Proceed with the same tool, but require a recruiter to review only the top 3 executive matches rather than the full slate

**Answer:** B — This is a harder version of the track-record-doesn't-automatically-transfer principle than the vague "cultural fit" example: here the tool's track record is genuinely strong and real, but for a *different task category* — the correct answer requires recognizing that validated performance on one role type doesn't establish validity for a materially different one, regardless of how proven the original track record is.

---

### Q45.
A children's hospital's IT governance committee is reviewing an AI vendor's claim that its pediatric-dosing-support tool has been "validated through peer-reviewed publication," and the committee finds the cited peer-reviewed study, confirms it's real, and confirms it does describe validation of an earlier version of the tool — but the vendor's current production version includes several substantive algorithm changes made after that study was published, which the vendor's marketing materials don't distinguish from the studied version.
**Options**
- A. Accept the claim, but only after confirming the peer-reviewed journal's general reputation and impact factor
- B. Treat the study as validating the earlier studied version only, not the current one with undocumented changes; the vendor's version blur needs clarification and ideally new validation.
- C. Accept the peer-reviewed validation claim, since the study is real, genuinely peer-reviewed, and genuinely describes the tool
- D. Reject the vendor's claim entirely, treating the version discrepancy as evidence of bad faith

**Answer:** B — This is a genuinely harder version of the vendor-validation-claim question than the earlier internal-testing-only example, because here real, credible, independent (peer-reviewed) validation *does* exist — the harder distinction is recognizing that validation of a specific studied version doesn't automatically extend to a materially changed current version, which the vendor's marketing has obscured rather than clarified.

---

### Q46.
A large grocery chain's self-checkout system uses an AI-assisted "receipt verification" flagging tool that selects a subset of self-checkout transactions for staff receipt-checking at the exit, based on behavior-pattern and item-value analysis. An internal review finds flagged transactions are disproportionately associated with the store's self-checkout lanes located nearest to the store's public-transit-accessible entrance, relative to lanes nearest the parking-garage entrance, though item-theft-recovery rates at the exit check show no significant difference between the two flagged groups.
**Options**
- A. Escalate the entrance-proximity disparity to the fairness owner despite equal recovery outcomes: the entrance may correlate with a demographic, so scrutiny can fall unevenly.
- B. Adjust the flagging system to exactly equalize flagging rates across the two entrance groups, regardless of underlying behavior-pattern data
- C. Discontinue the receipt-verification system entirely, since any entrance-based disparity in flagging is disqualifying regardless of context
- D. Since theft-recovery outcomes show no difference between the two groups, the entrance-proximity pattern is not a problem worth escalating

**Answer:** A — This is a harder version of the experiential-harm principle because the correlated input here (lane/entrance location) doesn't sound like a demographic proxy at all on its surface, unlike ZIP code or home port in earlier questions — the correct answer requires independently reasoning through *why* this seemingly neutral input might still correlate with a demographic pattern worth escalating, rather than relying on the input already sounding suspicious.

---

### Q47.
A regional credit union's small-business lending team uses Claude to draft loan-denial explanation letters required under fair-lending disclosure rules, providing specific, applicant-particular reasons each time (not generic reasons, unlike the earlier rotating-reasons example). A compliance officer separately notices that the specific reasons cited across a batch of recent denials cluster heavily around a single factor ("insufficient time in business") even though the credit union's underwriting criteria include several other factors that could independently justify denial in some of these cases.
**Options**
- A. Investigate the clustering only if an applicant specifically challenges their denial letter
- B. Adjust the underwriting criteria to reduce reliance on "insufficient time in business" as a factor, without investigating the letters themselves
- C. Investigate whether the clustering reflects each denial's actual primary reason or Claude defaulting to an easy factor; a true-sounding reason isn't necessarily the determinative one.
- D. Since each individual letter provides a specific, applicant-particular reason (satisfying the disclosure requirement's literal text), the clustering pattern itself needs no further attention

**Answer:** C — This is a harder version of the fair-lending disclosure principle than the earlier rotating-generic-reasons example: here the letters already avoid the more obvious flaw (generic, non-specific reasons), which makes it easy to assume the requirement is satisfied — but the subtler concern is whether the cited *specific* reason is actually each applicant's true primary reason, not just *a* true and specific-sounding one.

---

### Q48.
A pharmaceutical distributor's compliance team is deciding whether an AI-assisted lot-recall-risk scoring tool needs to disclose its AI involvement to the retail pharmacy customers who receive automated recall-priority notifications generated using the tool's risk scores. A pharmacist at one retail customer, upon learning of the tool's existence during an unrelated conversation, says: "I assumed a person reviewed and prioritized these recall notices — knowing it's AI-scored actually makes me want to double-check the ones marked lower-priority myself."
**Options**
- A. Disclosure is unnecessary, since retail pharmacy customers are sophisticated professional recipients who don't need transparency about internal tooling
- B. Disclosure is needed only for notifications marked lower-priority, since those are the ones the pharmacist specifically said they'd want to double-check
- C. No disclosure is needed, since the notifications themselves are accurate regardless of how priority was determined
- D. The pharmacist's reaction shows why disclosure matters: knowing AI shaped the prioritization changes how a downstream professional allocates verification effort, and withholding removes that ability.

**Answer:** D — This is a harder, more concrete version of the customs-broker disclosure question: rather than reasoning abstractly about a "reasonable interest in knowing," this scenario shows a *specific, real behavioral change* a recipient makes once informed, which makes the transparency argument more concrete — and the correct answer generalizes that reasoning to the disclosure policy overall (B incorrectly tries to limit disclosure to only the specific sub-case one pharmacist mentioned, rather than recognizing the general principle it illustrates).

---

### Q49.
A large telehealth platform proposes retaining anonymized *audio* (not video) recordings of therapy sessions indefinitely, after removing identifying information, specifically to train and improve its own AI-assisted session-summarization feature over time, arguing that anonymization resolves the primary privacy concern, and that indefinite retention of anonymized data is a lower-risk category than the earlier indefinite-video-retention proposal.
**Options**
- A. Approve indefinite retention, since the stated purpose (improving the summarization feature) is a legitimate, beneficial business use
- B. Approve indefinite retention of the anonymized audio, since removing identifying information substantively changes the privacy calculus compared to retaining identified data
- C. Deny the proposal outright, since voice data can never be adequately anonymized under any circumstances
- D. Escalate retention and anonymization adequacy to the privacy policy owner first: voice and therapy content can re-identify people, and indefinite retention for training deserves its own review.

**Answer:** D — This is a harder version of the earlier indefinite-video-retention question: here, anonymization is genuinely attempted (unlike the earlier proposal), and the comparison to a "riskier" alternative (video) is used to make the audio proposal seem safe by contrast — but voice and conversational content carry their own specific re-identification risks that structured data doesn't, and "lower risk than an even worse alternative" doesn't substitute for the retention-period and anonymization-adequacy policy review this still deserves on its own terms.

---

### Q50.
A national retailer's dynamic-pricing model, which adjusts online prices in real time based on demand signals, browsing behavior, and inventory levels, has operated successfully for two years. A new analyst proposes adding "device type" (e.g., a specific premium smartphone model vs. a budget model) as an additional input, reasoning that device type correlates with willingness-to-pay and could improve pricing optimization, similar to how other behavioral signals are already used.
**Options**
- A. Add the input, but only review it if a regulator or consumer group raises a complaint after deployment
- B. Run the same disparate-impact review used for any new pricing input: willingness-to-pay by device type is a documented income proxy with a foreseeable price-discrimination concern.
- C. Add the input without further review, since device type is a behavioral/technical signal, not a demographic category, and is analogous to inputs already in use
- D. Skip review, since this is analogous to previously-reviewed behavioral inputs and doesn't need a fresh check

**Answer:** B — This is a harder, higher-stakes version of the previous facially-neutral-input question because device-type-based pricing (sometimes called "device discrimination" in pricing) is a specifically well-documented, previously-litigated pattern in consumer-protection contexts, not just a hypothetically-neutral-sounding metric — the correct answer requires recognizing that this particular input carries a foreseeable, known risk that should trigger review proactively, not just generic caution about "any new input."

---

### Q51.
A national law firm allows attorneys to use Claude for legal research, with a written policy requiring independent database verification of all citations before filing. A senior partner, reviewing a junior associate's brief, finds all citations verified correctly per policy — but also notices the brief's central legal argument relies on characterizing a precedent case's holding in a way that, while not factually false about any specific citation, subtly overstates how squarely that precedent applies to the current case's facts.
**Options**
- A. Since every citation was independently verified per policy, the brief satisfies the firm's AI-use verification requirements
- B. Citation verification is narrower than checking that the legal argument's characterization is sound; genuine citations can support a strained argument, so substantive legal review is still needed.
- C. This is acceptable as long as the partner cannot find any single individually false statement in the brief
- D. This is unacceptable and should be treated as identical in severity to a fabricated-citation violation

**Answer:** B — This is a harder version of the citation-verification principle: the firm's policy correctly addresses the well-known fabricated-citation risk, but this scenario shows a different failure mode (genuine citations, strained application) that citation-verification alone doesn't catch — requiring the test-taker to recognize that satisfying one specific, named safeguard doesn't mean all relevant risks for the output have been addressed.

---

### Q52.
A manufacturing company's HR team uses an AI tool to draft performance-improvement-plan (PIP) language, with a manager required to review and personalize each draft before delivery, and separately, HR has begun tracking a compliance metric: "percentage of PIPs where the reviewing manager made at least one substantive edit to the AI draft," reasoning this metric provides evidence that real review is occurring. A manager under review for consistently showing 0% substantive edits argues, "I make zero edits because the drafts are already excellent, not because I'm not reviewing them properly."
**Options**
- A. The edit-rate metric can't distinguish careful review needing no changes from superficial approval; treat it as a signal to investigate, not a conclusion.
- B. Discontinue the substantive-edit-rate metric entirely, since this case shows it can be misleading
- C. Treat the 0% edit rate as conclusive proof of superficial review, regardless of the manager's explanation, and require immediate retraining
- D. Accept the manager's explanation at face value, since draft quality is a plausible reason for consistently making no edits

**Answer:** A — This is a harder version of the "does the checkpoint function substantively" question than the earlier PIP-grievance example: here, HR has already tried to operationalize substantive review into a measurable metric (a reasonable, good-faith attempt), but the correct answer recognizes that metric itself has a specific blind spot (it can't distinguish genuine no-edit-needed review from rubber-stamping) and needs supplementing with a more direct assessment, rather than being trusted uncritically (D) or abandoned as useless just because of this one ambiguous case (B).

---

## Domain 1 — Prompting and Task Execution (14% — Q53–Q66)

### Q53.
A commercial-fishing-fleet operator attaches a 20-page vessel-inspection report and asks Claude to "summarize the findings for the insurance renewal." The insurer specifically needs only safety-equipment deficiencies and their remediation status — nothing about engine performance or crew accommodations, which are covered separately. The first draft is a well-organized, comprehensive summary of the entire report, including engine and crew-accommodation sections.
**Options**
- A. Make the prompt substantially longer, describing the vessel and inspection context in more detail
- B. Attach the report as a file instead of pasting excerpts, expecting a more targeted read
- C. Specify the exact scope the insurer needs (safety-equipment deficiencies and remediation status) and what to exclude, since 'summarize the findings' was reasonably read as the whole report.
- D. Ask Claude to shorten the comprehensive summary by half, keeping the same section structure

**Answer:** C — As with the lease-abstract example, the model's interpretation of "the findings" was reasonable on its own terms; naming the exact required scope and explicit exclusions resolves the ambiguity directly, rather than adding unrelated detail, shortening a still-wrongly-scoped structure, or changing the attachment format.

---

### Q54.
A specialty-foods importer's regulatory associate gets a first draft of a customs-compliance summary: technically thorough and well-organized, but written using dense customs terminology the associate's non-specialist warehouse team (who will action the summary's checklist items) won't understand, and separately, the draft correctly includes a required disclaimer paragraph the associate hadn't thought to request.
**Options**
- A. Rewrite the original prompt from scratch with a much longer, highly detailed specification and try a more capable model
- B. "This is too technical. Try again with a completely different structure."
- C. "Simplify this for a general audience."
- D. "The audience is the warehouse team, not customs specialists: keep the checklist structure and disclaimer as-is, but rewrite the explanations in plain terms."

**Answer:** D — Specific, targeted feedback naming exactly what changes (plain-language explanations) and exactly what to preserve (structure and the correctly-included disclaimer) produces a better second draft than a vague "too technical" (B) or "simplify" (C) request, or an unnecessary full prompt-and-model overhaul (A) for what is a targeted, easily fixable gap.

---

### Q55.
A regional theater company's artistic director's first draft request reads: "Give me ideas for next season's play selection." **(Select TWO — all-or-nothing)** Which **TWO** follow-up refinements best preserve this as a genuinely divergent, options-generating task while still improving its usefulness?
**Options**
- A. "Format each suggestion as a one-paragraph pitch in a table with columns for genre, cast size, and estimated royalty cost."
- B. "Give me 20 varied options spanning classics, contemporary works and lesser-known pieces, without filtering for budget or cast size yet; I'll narrow down after."
- C. "Include a mix of plays that have been commercially successful elsewhere and ones that are more artistically ambitious or unconventional."
- D. "Rank the options from most to least likely to sell well, and only show me the top 5."
- E. "Only suggest plays with a cast of 6 or fewer, a public-domain script (no royalty fees), and a running time under 90 minutes."

**Answer:** B, C — Both widen the range generated (explicit volume and variety, spanning commercial-success and artistic-ambition dimensions) without pre-filtering by constraints. E constrains the brainstorm too tightly upfront (locking in cast size, cost, and length before ideas are generated), and A and D both prematurely convergent-ize the task (ranking/cutting to 5, or a rigid structured output format) before divergent value has been captured.

---

### Q56.
A specialty-chemical manufacturer's EHS (environmental health and safety) associate must reconcile five years of incident-report logs against a newer standardized severity-classification system, and has sampled reports only from the most recent year, which a colleague notes were already "mostly filed under the newer system already, unlike the older years." The associate's instinct is to write a comprehensive mapping rule covering every classification discrepancy they can imagine, based on this recent-year sample, then have Claude apply it across all five years at once.
**Options**
- A. Ask for the mapping code in a specific language so the associate can inspect the logic before running it on all five years
- B. Run the mapping now on the assumption that unexpected issues in older years can be fixed as they surface in the output
- C. First have Claude profile a sample from the older, old-system years her sample missed and report the discrepancy range there before finalizing any mapping rule.
- D. Write the comprehensive mapping rule now, based on the recent-year sample, to avoid multiple rounds of rework

**Answer:** C — This is a harder version of the profile-before-rules principle than the solar-installer example: the associate did sample data, but specifically the *wrong, easier* subset (the year already mostly using the new system) rather than the harder conversion cases (older years) the rule actually needs to handle — the fix isn't just "profile before writing rules," but "profile the population that's actually representative of the hard cases."

---

### Q57.
A boutique architecture firm's business-development associate needs a capabilities statement for a specific municipal RFP response, and their instinct is to request the complete statement immediately, providing the RFP's stated evaluation criteria in the prompt.
**Options**
- A. First ask Claude to map what is known: the firm's past municipal projects, prior responses to this municipality's RFPs, and evaluation-criteria language matching its strengths.
- B. Request the complete statement now, since including the RFP's stated evaluation criteria upfront should be enough specification for a strong first draft
- C. Ask Claude to grade a rough outline the associate writes first, before any statement drafting begins
- D. Request three different versions of the statement in different tones and select the strongest as a base

**Answer:** A — Even with the RFP's evaluation criteria included in the prompt, jumping straight to generating statement text skips grounding the draft in the firm's own actual portfolio and RFP-history — mapping what's known and available first produces a better-grounded, more specifically competitive statement than generating stylistic variants (D) or grading an isolated outline (C).

---

### Q58.
A specialty-insurance underwriter, in a brand-new chat with no prior conversation history, asks Claude to draft a binder confirmation letter for a marine-cargo policy. The first draft correctly follows the required policy-language structure but states the wrong currency for the policy limit, which should match the cargo's origin-country currency per the underlying request's stated terms.
**Options**
- A. Check whether a stored account instruction or knowledge file about currency formatting has gone stale
- B. Start an entirely new chat and resend the identical prompt, in case something in the first chat caused the error
- C. Switch to a more capable model immediately, expecting it to handle currency matching correctly
- D. Treat it as under-specification: the request probably never stated which currency applies, so re-check it against that unstated requirement and state it explicitly.

**Answer:** D — With no conversation history to overload (ruling out B) and no prior working version to compare against for staleness (ruling out A), a first-attempt error on a requirement that was implied by context but not explicitly and unambiguously stated is a specification gap to close directly — this is a harder version of the pattern because the requirement was arguably inferable, which makes "the model should have figured it out" a tempting but ultimately still under-specification-pointing conclusion.

---

### Q59.
A boutique auction house's associate's fully-specified delegation (item, target buyer profile, format, and explicit instruction on what Claude may decide alone) results in a provenance research summary that correctly flags every discretionary judgment call as instructed — but uses a specific technical term ("deaccessioned") in a way that, while not factually wrong, differs subtly from how this particular auction house's own internal style guide defines and uses that term, a style guide that exists but was not attached to this specific request.
**Options**
- A. The request needed more background detail about why provenance terminology matters for this specific item
- B. This is a knowledge gap, not a prompting gap: the house style guide was never available to the request, so attach it as Project knowledge.
- C. This is a silent-discretion problem requiring a broader "flag when you decide" instruction, similar to the earlier tie-break and weight-distribution-method examples
- D. The request needed an explicit closing instruction requiring Claude to confirm every originally requested item is present in the output

**Answer:** B — This is designed to look like a Domain 1 prompting issue (similar to C's silent-discretion pattern) but is actually a Domain 5 configuration/knowledge-availability issue in disguise: no prompting refinement can fix a definitional mismatch against a reference document that was simply never provided to the request — recognizing when a "prompting-shaped" symptom actually has a configuration-layer cause is the harder skill being tested.

---

### Q60.
A specialty-foods co-op's member-services associate pastes 35 member-satisfaction survey responses into one request, asking for theme coding, frequency counts, and a board-ready insight memo — but structures the request as: "First, propose your theme categories and get my sign-off. Then, once I confirm, code all 35 responses into a table against those categories, and stop again for my review of the table before writing any counts or memo." The associate follows through, reviewing and confirming at each stated checkpoint.
**Options**
- A. This approach doesn't meaningfully reduce the risk, since all the underlying analysis still originates from the same initial message
- B. This approach is unnecessary if the final memo is reviewed carefully regardless of how it was produced
- C. The staged approach substantially reduces the propagation risk by verifying category definitions and the coding table before counting or memo-writing, much like separate requests.
- D. This approach should also specify a maximum number of themes in advance, or the staging won't provide real protection

**Answer:** C — This is a "recognize good task decomposition" question testing whether the test-taker credits a well-structured staged process (explicit checkpoints for category definitions AND the coding table, both before downstream aggregation) as functionally equivalent to fully separate requests — the protection comes from verifying intermediate steps before building on them, not from how many distinct messages are used to achieve that.

---

### Q61.
A regional public-radio station's development associate asks Claude for "10 fundraising-drive slogan ideas" for a specific membership campaign, describing the campaign's theme and target donor segment in detail, and separately notes: "Our last three drives all used some variation of 'the sound of community' — we specifically want to move away from that exact framing this time." The 10 results returned include two slogans that are close paraphrases of "the sound of community."
**Options**
- A. The ideas were never checked against the named exclusion; a targeted iteration asking which are too close to it, plus replacements, beats starting over.
- B. The prompt should have specified a stricter format (e.g., a maximum word count) to force more differentiated results
- C. The prompt was well-specified overall; try a different, more capable model on the identical prompt to get better-differentiated results
- D. Slogan-brainstorming requests are inherently unsuited to AI assistance when a specific past framing needs to be avoided, and should be done manually instead

**Answer:** A — The exclusion was stated but the divergent output wasn't yet filtered or iterated against that specific constraint — a targeted, specific follow-up naming exactly which results still violate the exclusion is the efficient iteration move, rather than switching models, declaring the task unsuited, or adding an unrelated formatting constraint.

---

### Q62.
A regional health department's outreach coordinator delegates a data-cleaning task on a 3,000-row community-survey export, providing clear rules for standard cases, and separately: "If you find a response that seems to contradict a rule I've given you in a way I haven't anticipated, apply your best judgment silently rather than stopping to ask, since I want this done without back-and-forth." Claude encounters an ambiguous, unanticipated pattern and, following the instruction, resolves it silently using its own judgment without flagging it.
**Options**
- A. This is a prompting failure, since a well-specified request shouldn't encounter unanticipated patterns at all
- B. This is a context-overload issue, given the dataset's size
- C. The request behaved as instructed: she asked for silent judgment calls, so faithful execution isn't the flaw, though she should reconsider that choice for ambiguous data.
- D. This is a sign a more capable model was needed to resolve the ambiguity correctly rather than merely silently

**Answer:** C — This is a harder, inverted version of the earlier "flag rather than guess" recognition question: here the coordinator explicitly requested the *opposite* behavior (silent judgment, no back-and-forth), so Claude complying with that explicit instruction is the system working as instructed — even if, separately, that instruction itself might be worth reconsidering for data-quality reasons, that's a different question from whether the request was executed as specified.

---

### Q63.
A specialty outdoor-gear retailer's e-commerce associate needs the same underlying seasonal-sale announcement delivered as: a two-line push notification, a detailed email with product category breakdowns, and a set of five short product-tagged social media captions. The associate's plan is a single combined prompt requesting all three, but adds: "Treat the push notification and email as needing to share consistent sale dates and discount percentages, but the social captions can vary more loosely in tone from each other."
**Options**
- A. This is well-suited, but only if extended thinking is enabled to manage the combined complexity
- B. This is still poorly suited; decompose fully into three fully separate, sequential requests, since combining any outputs with different format constraints in one prompt is always the wrong approach regardless of the specific consistency requirements named
- C. This prompt manages the one thing needing cross-format consistency (dates and discounts) while allowing looser variation elsewhere, instead of uniform consistency or independence.
- D. This should also specify a maximum word count for each of the three formats, or the consistency instruction won't work as intended

**Answer:** C — This is a harder, "recognize good prompting" version of the earlier multi-format decomposition question: rather than mechanically requiring full separation of every differently-formatted output (as B claims), this prompt correctly identifies which specific dimension (dates/discounts) genuinely needs cross-format consistency and explicitly permits appropriate variation elsewhere — sophisticated, well-reasoned constraint-setting within one request, not a violation of the decomposition principle.

---

### Q64.
A community land trust's outreach associate needs the current local zoning-hearing schedule for this week (a simple published fact), needs a cited, multi-source comparison of affordable-housing financing models used by five peer land trusts nationally for a board strategy session, and needs a one-line explanation of what "community land trust" means for a new volunteer orientation packet. **(Select THREE — all-or-nothing)** Which **THREE** correctly match each need to the most fitting way of answering it?
**Options**
- A. The zoning-hearing schedule → a cited, multi-source research pass, to ensure the schedule information is authoritative
- B. The "what is a community land trust" explanation → a short inline conversational reply, appropriate for an orientation packet excerpt, not a lengthy standalone document
- C. The peer-land-trust financing-model comparison → a quick current-facts lookup, since land trust structures are generally well-established and simple
- D. The peer-land-trust financing-model comparison → a deeper, cited research-style pass gathering and comparing multiple organizations' approaches
- E. The zoning-hearing schedule → a quick, current-facts lookup, not a deep multi-source research pass

**Answer:** B, D, E — A live, simple, current published fact fits a quick lookup, not heavy research (ruling out A); a multi-organization, board-facing comparison needing citations across several sources fits a genuine research pass, not a quick lookup (ruling out C); and a short definitional explanation for an orientation excerpt fits a brief conversational-style answer rather than a formal document.

---

### Q65.
A regional land-trust's newly-hired conservation easement coordinator, with a real-estate background but no prior conservation-easement-specific experience, drafts a public-facing explainer on how a proposed easement would affect nearby property owners, using Claude, based on the actual easement terms and a staff legal memo provided as sources. The explainer accurately reflects both source documents and addresses every point the coordinator's supervisor requested.
**Options**
- A. A colleague with conservation-easement expertise, not just general real-estate experience, should check whether the explainer captures easement-specific nuances and common owner misconceptions.
- B. Run the explainer through a formatting pass so it reads as polished as one written by an experienced conservation professional
- C. A grammar-and-clarity proofread by a colleague is the missing check before publication
- D. Ask Claude to rate the explainer's own accuracy and revise any section scoring below a set threshold

**Answer:** A — This is a harder version of the domain-expertise-gap principle because the coordinator isn't a complete novice (they have real-estate background, a genuinely relevant adjacent field) — the correct answer requires recognizing that adjacent-domain competence doesn't substitute for the specific domain expertise (conservation easements specifically) needed to catch nuances a general real-estate background wouldn't surface.

---

### Q66.
An independent brewery's taproom manager asks Claude to "write something for our new seasonal beer release" and gets a single generic paragraph. The manager then asks: "Give me three versions: one short and punchy for a chalkboard menu, one with more flavor-profile detail for our website's beer list, and one conversational one for bartenders to say out loud to customers who ask about it — same beer, same key facts, but each suited to how and where it'll actually be used."
**Options**
- A. This second request should have been split into three fully separate conversations rather than one combined request
- B. This second request needed extended thinking enabled, given it asks for three simultaneous outputs
- C. This second request is over-engineered for a simple task and should have simply asked for "3 versions" without further detail
- D. It is a well-constructed decomposition: distinctly specified formats, each with its own context of use, length and tone, and it names why each differs.

**Answer:** D — This is another "recognize good prompting" question, one notch beyond the bookstore staff-picks example: not only does it name each format, audience, and tone, it also grounds each in its actual context of use (chalkboard, website, spoken by bartenders), which is exactly the kind of decomposition-by-real-world-use-case that produces well-differentiated, genuinely fit-for-purpose results — no need for separate conversations (A) or extended thinking (B), and vaguer instructions (C) would produce a weaker result, not an equally good one achieved more efficiently.

---

## Domain 3 — Product and Model Selection (12% — Q67–Q78)

### Q67.
A regional engineering firm's associate uses a mid-tier model to cross-reference a 200-page bridge-inspection report against a 60-page structural-code checklist, and the output misses several cross-references despite a clear, well-specified prompt that worked well on a similar 35-page report previously. Separately, the associate notices the 200-page report contains several scanned, lower-quality image pages that the model may be processing less reliably than the surrounding text pages.
**Options**
- A. Split each document into five separate chats and cross-reference them manually afterward
- B. Move to the top tier to hold the cross-referencing structure across both documents, and separately fix image quality with a cleaner scan or OCR.
- C. Switch to the fastest, lightest tier to process both documents more quickly
- D. Turn off any extended reasoning mode, on the theory that additional reasoning is diluting attention to the source text

**Answer:** B — This is a harder version of the escalate-for-depth pattern because it layers in a *second*, genuinely distinct issue (input quality on scanned pages) that a model-tier change alone doesn't fix — the correct answer requires recognizing that tier selection addresses the complexity/coherence problem while a separate, non-tier-related fix (better image quality/OCR) is needed for the degraded-input problem, rather than assuming one fix (tier change) resolves both issues.

---

### Q68.
A hospital system's clinical-education team runs annual, high-stakes accreditation self-study documentation (balancing multiple regulatory standards, historical compliance data, and multi-year trend analysis) on the fastest, lightest model tier "since it just needs to compile information we already have," while running routine, single-sentence patient-satisfaction-survey-response tagging on the top-capability tier with extended thinking enabled "to be thorough with anything patient-related."
**Options**
- A. Only the survey-tagging choice is a problem; the accreditation documentation is fine on the lightest tier as long as a human reviews the final compiled document
- B. Only the accreditation-documentation choice is a problem; the survey-tagging default is a safe, low-risk choice even if costly
- C. Both are mismatched in opposite directions: 'compiling what we have' undersells multi-standard, multi-year synthesis, while routine single-sentence tagging needs neither the top tier nor extended reasoning.
- D. Neither choice is a problem, since model tier is primarily a cost lever and quality differences are marginal for both task types

**Answer:** C — The accreditation task's *framing* ("just compiling information we already have") is a red herring that undersells its actual complexity (multi-standard, multi-year synthesis), while the survey-tagging task's *subject* ("anything patient-related") is a red herring that overstates its actual complexity (simple, routine tagging) — both tier choices are wrong because they were driven by surface framing rather than genuine task complexity, in opposite directions.

---

### Q69.
A specialty-textile importer's compliance team runs a heavy, multi-source research-mode pass every time they need to check whether a specific, named foreign supplier currently appears on a public sanctions list (a simple, binary, current-facts check), and separately relies on a single quick chat message to synthesize a nuanced assessment of which of four possible alternative sourcing countries best balances tariff exposure, labor-standards risk, and shipping-lead-time variability for a major sourcing decision.
**Options**
- A. Only the sanctions-list check is mismatched; the sourcing-country assessment is appropriately handled with a quick chat since it's "just comparing four options"
- B. Only the sourcing-country assessment is mismatched; the sanctions-list research-mode pass is appropriately thorough given compliance stakes are high
- C. Both choices are reasonable, since research mode is generally more thorough and a quick chat is generally more efficient
- D. Both are mismatched: a current binary sanctions check doesn't need heavy multi-source research, while a multi-factor sourcing decision across four countries benefits from deeper reasoning.

**Answer:** D — As with the earlier competitor-price/contract-comparison pairing, this inverts the more intuitive pairing (treating the high-stakes-sounding compliance check as needing more, and the "just comparing four options" sourcing decision as needing less) to test the underlying principle: a simple current-fact check doesn't need heavy research tooling regardless of compliance stakes, and a genuine multi-factor tradeoff decision needs reasoning depth regardless of how simple "comparing four options" sounds.

---

### Q70. *(Select TWO — all-or-nothing)*
A regional performing-arts venue's operations team is deciding, for five upcoming requests, whether extended thinking is worth its added time/cost. Which **TWO** are genuinely worth it?
**Options**
- A. Sequencing a multi-venue touring schedule across eight cities under simultaneous constraints of venue availability, load-in/load-out timing, and a fixed total transportation budget
- B. Converting a finalized show-run sheet into a simple printable schedule for ushers
- C. Determining the seating hold-release schedule across a multi-show subscription season, balancing renewals, single-ticket demand and a fixed capacity constraint simultaneously.
- D. Generating six quick name options for a new subscriber-loyalty program, to be narrowed down casually later
- E. Looking up a specific performer's stated technical-rider requirement from an attached rider document

**Answer:** A, C — Both are genuine multi-constraint optimization problems requiring several competing factors to be weighed simultaneously, which is where deeper reasoning adds real value. B, D, and E are simple, low-stakes, largely single-step tasks where extended reasoning adds cost without meaningfully improving the result.

---

### Q71.
A boutique law firm's associate is two hours into a single long conversation drafting a complex trust document with Claude, and separately, has also been pasting in increasingly long excerpts from a 40-page trust-law treatise for reference throughout the conversation, rather than attaching it once at the start. Response quality has visibly degraded over the last 20 minutes.
**Options**
- A. Switch immediately to a more capable model tier within the same long conversation
- B. Continue in the same conversation, but stop pasting treatise excerpts going forward, without addressing the context already accumulated
- C. This is a sign the trust-drafting task itself is unsuited to AI assistance and should move to manual drafting from this point forward
- D. Most likely context overload from accumulated length, including repeatedly pasted excerpts: summarize the agreed terms and restart fresh with one treatise attachment.

**Answer:** D — This is a harder version of the context-overload pattern because it specifically identifies a compounding cause (repeatedly pasting excerpts rather than attaching once) alongside the general conversation length — the correct answer addresses both the *existing* accumulated context (summarize/restart) and the *going-forward* habit (attach once rather than repeatedly paste), which B only partially addresses by stopping the habit without cleaning up what's already accumulated.

---

### Q72.
A national parks conservancy's development director states as organizational policy: "For any donor-facing document, always use our AI tool's most capable setting with extended reasoning enabled, because our major donors deserve our very best effort on everything we send them."
**Options**
- A. It shows poor task-fit judgment: 'donor-facing' describes the audience, not complexity, so a simple templated acknowledgment doesn't need the top tier and extended reasoning.
- B. This is sound policy as long as the conservancy can absorb the additional cost
- C. This is sound, defensible policy, since donor-facing work should never risk being under-resourced
- D. This is sound policy specifically for donor relations, even if it wouldn't be sound in other departments

**Answer:** A — This is the same "audience-based blanket rule" trap as the earlier consultancy and hospital examples, now dressed in donor-stewardship language — the underlying judgment failure is identical: tier/reasoning-depth decisions should track task complexity, not who ultimately receives the output.

---

### Q73.
A regional credit union's member-services team needs to: quickly verify today's published federal funds rate for a member inquiry in the next two minutes; conduct a comprehensive, multi-source comparison of six competing core-banking software vendors for a board presentation next quarter (with citations); and determine, given a specific member's unusual combination of account types opened across three different mergers the credit union has been through, which of several legacy fee-schedule versions still technically applies (a determination requiring careful, multi-step reasoning through historical merger-integration documentation).
**Options**
- A. Rate lookup → extended thinking, since interest rates are financially significant; vendor comparison → a quick lookup, since vendors are well-known; fee-schedule determination → a quick lookup, since it's an internal document
- B. Rate lookup: quick current-facts check; vendor comparison: cited multi-source research; legacy fee-schedule determination: extended thinking for the multi-step documentation.
- C. All three → a deeper, cited multi-source research pass, since thoroughness is always the safer choice
- D. All three → extended thinking, since financial-services contexts always warrant deeper reasoning

**Answer:** B — Each task fits a different tool for a specific structural reason: a single current published rate needs a fast factual check; a multi-vendor, citation-needing comparison needs genuine research; and a multi-step reasoning task through historical, non-obvious documentation (not a simple lookup, despite being "an internal document") benefits from deeper, careful reasoning.

---

### Q74.
A specialty-cheese cooperative's inventory system produces a "recommended wholesale price" for a specific aged-cheese batch that is noticeably higher than any comparable past batch, with no obvious explanation in the current season's aging-cost data. The associate's first instinct is to assume the pricing tool hallucinated the figure and re-run the request with "use only this season's actual cost data."
**Options**
- A. Re-prompt with the stricter wording and regenerate the full recommendation
- B. Before assuming hallucination, check whether Project knowledge holds an outdated reference, such as a premium guideline for a prior specialty batch, still influencing the recommendation.
- C. Switch to a more capable model tier, on the theory that a stronger model is less likely to fabricate a pricing figure
- D. Ask the tool to rate its own confidence in the recommended price and only accept figures above a high confidence threshold

**Answer:** B — As with the theater and pricing-project examples, an unusual, unexplained figure is often better explained by a stale or mismatched knowledge source still feeding the workflow than by outright fabrication — checking the actual configuration first is more diagnostic than re-prompting, upgrading the model, or relying on self-reported confidence.

---

### Q75.
A specialty printing company's wholesale team has iterated six times with Claude on a bulk-order discount-tier calculator embedded in a client-facing quote template. Formatting, tier boundaries, and client-facing language are all now correct, but the final discounted-total figure is still subtly wrong on every attempt, despite six rounds of increasingly precise wording about how discounts should stack — and the team has also, across these six rounds, been alternating between two different model tiers, hoping a change in tier would eventually resolve the issue.
**Options**
- A. This is a context-overload problem, since six rounds of iteration have accumulated in one conversation
- B. It is a feature mismatch: the stacking discount should be computed by code, not prose, whatever the wording or tier; six rounds of alternating tiers confirm it.
- C. This is a model-capability problem, and the team should commit to the single most capable tier going forward rather than continuing to alternate
- D. This is a description problem requiring one more, even more precise attempt at wording the stacking rule

**Answer:** B — This is a harder version of the prose-vs-computation pattern because it explicitly builds in a tier-alternation red herring: the fact that changing tiers across six rounds *didn't* fix a consistent arithmetic error is itself diagnostic evidence pointing away from a tier/capability explanation (ruling out C) and toward a feature mismatch, on top of the wording-precision evidence already present in the simpler version of this pattern.

---

### Q76.
A metropolitan opera company's IT team wants a single AI-assisted patron-services intake system to both instantly handle high-volume, low-ambiguity requests (e.g., "what time does the show start") and also help resolve a smaller number of complex, multi-factor subscription-transfer disputes involving conflicting records across a recent ticketing-system migration.
**Options**
- A. Use the lightest tier for both, since patron-services work is generally routine
- B. Use one uniform model configuration for both request types, to keep the system simple to maintain
- C. Use the highest-capability tier with extended thinking for both, since patron account issues are always sensitive
- D. Use a fast, lightweight tier for high-volume, low-ambiguity requests and deeper reasoning for complex disputes, especially those complicated by migration inconsistencies.

**Answer:** D — This extends the per-request-type tier judgment principle by adding a specific complicating factor (the system migration) that reinforces, rather than merely restates, why the dispute category needs deeper reasoning — recognizing that added layer of justification (not just "disputes are generally complex") is what makes this harder than a simpler version of the same underlying principle.

---

### Q77.
A regional history museum's exhibits team needs Claude to draft a simple, templated donor-plaque acknowledgment (low-stakes, routine) and, in the same working session, needs it to reconcile conflicting artifact-provenance dates across three different historical catalogs compiled decades apart using different dating conventions, where resolving the discrepancy requires careful, multi-step reasoning for a scholarly exhibit label.
**Options**
- A. Use the same default configuration for both tasks in the same session, since switching settings mid-session adds friction
- B. Use the lightest tier for the plaque and the lightest tier plus extended thinking for the provenance reconciliation, since a lighter tier plus deeper reasoning is more cost-effective than a heavier tier
- C. Keep plaque drafting on a standard configuration and enable extended thinking for the provenance-date reconciliation, a genuine multi-step task, accepting the friction of switching.
- D. Enable extended thinking for both tasks, since the associate is working on both in the same general session

**Answer:** C — The two tasks are genuinely different in kind, and the correct judgment is to configure each task appropriately even within one working session — session-level convenience (A) or applying one setting to both (D) doesn't override task-level fit, and B's tier-substitution assumption doesn't necessarily suit a task that may also benefit from higher capability, not reasoning depth alone.

---

### Q78.
A regional blood-donation center's IT-support team has been told by a well-meaning colleague that "research mode" and "extended thinking" are simply two names for the same underlying feature, and has been avoiding research mode for routine internal-policy lookups specifically because they believe it always triggers the slower, more expensive extended-reasoning process regardless of what's actually being asked.
**Options**
- A. The colleague's claim is correct for some AI platforms but not others, so the team should verify per-platform before deciding
- B. The distinction doesn't matter in practice, since both features should generally be minimized for cost reasons regardless of task
- C. The colleague's claim is correct, and the team's avoidance behavior is appropriately cautious
- D. It's a misconception: research mode and extended thinking are separate capabilities, so avoiding one because of the other rests on a false premise.

**Answer:** D — This is a harder variant of the earlier "extended thinking ≠ flagship model" misconception because it conflates two *different* pairs of features (research mode and extended thinking) rather than model tier and reasoning depth — the underlying lesson is the same (independent settings shouldn't be treated as bundled), but the specific features being confused are different, requiring the test-taker to recognize the pattern in a new pairing rather than recall a memorized fact about one specific pair.

---

## Domain 5 — Configuration and Knowledge Management (12% — Q79–Q90)

### Q79.
A regional accounting firm's associate handles work for three clients in three separate, correctly-scoped Claude Projects. The firm has also just adopted a new, firm-wide standard client-communication disclaimer that must appear at the bottom of every client-facing email, regardless of which client it's for, and separately, each client Project already has its own client-specific email signature block that should continue to appear as well.
**Options**
- A. Add the disclaimer to account-level instructions since it is true for every client, and leave each client's signature block in its own Project.
- B. Add the new disclaimer to each of the three client Projects' instructions individually, alongside each Project's existing signature block
- C. Add the disclaimer to all three client Projects' knowledge files (not instructions), reasoning that a disclaimer is reference material rather than an instruction
- D. Create a new, fourth "firm-wide disclaimers" Project containing just the disclaimer, and reference it manually from each client conversation

**Answer:** A — This is a harder version of the account-level-vs-Project-scoping principle because it involves *updating* an existing multi-Project setup with a new global rule, rather than initially setting up scoping from scratch — the correct answer recognizes that a genuinely global addition belongs at the account level (added once, applying everywhere) without needing to duplicate it into every existing Project (B) or invent an unnecessary fourth Project (D) or miscategorize it as passive knowledge rather than an active instruction (C).

---

### Q80.
An associate's account-level instructions include: "When drafting any client proposal, always include a 'Why Us' section highlighting our team's credentials." This served the associate well when proposal-writing was their primary work. The associate has since taken on additional responsibilities drafting internal process documentation, where this instruction is now irrelevant, and separately, a new junior colleague has started sharing the same Claude account for a probationary period and has begun encountering the same irrelevant "Why Us" section appearing in their own internal-documentation drafts.
**Options**
- A. Keep the account-level instruction as-is, since it still serves its original purpose for actual proposal work
- B. Leave the instruction in place, and have the junior colleague manually override it by writing "skip the Why Us section" at the top of every internal-documentation request
- C. A shared account means a badly scoped global instruction burdens a second person's unrelated work, strengthening the case to scope it into a proposal Project.
- D. Delete the account-level instruction entirely, since it's now causing problems for at least one user

**Answer:** C — This is a harder version of the evolving-scope principle than the customer-service-summary example specifically because a *second person* (the junior colleague) is now affected by the same scoping mismatch through a shared account — recognizing that a shared-account context changes the stakes and urgency of fixing a poorly-scoped global instruction (beyond just the original author's own convenience) is the added layer of judgment here.

---

### Q81.
A small independent publishing house's two imprint editors (one for literary fiction, one for genre fiction) share one Claude Project called "Editorial Resources," containing both imprints' respective style guides, author-voice notes, and submission-response templates, because "it's all editorial work for the same company." One imprint's rejection letters have started referencing style preferences that belong to the other imprint.
**Options**
- A. It is a scoping error: each imprint's style guide belongs in its own Project, since 'same company' doesn't mean interchangeable standards, and sharing causes contamination.
- B. This is acceptable as long as authors are told their rejection letter may reference either imprint's style
- C. This is expected and acceptable, since both editors work for the same publishing house
- D. This can be fixed by asking Claude, in each request, to "use the correct imprint's style," without changing the Project structure

**Answer:** A — "Same company" is an even more tempting-sounding justification for shared scoping than "same subject" (the AP History example) or "same client" (a hypothetical version of the wholesale/retail example), precisely because company-level identity feels like it should unify standards — but the underlying issue (two genuinely distinct rule-sets cross-applying because they share one always-on knowledge pool) is identical, and a per-request reminder (D) remains a workaround, not a structural fix.

---

### Q82.
A freelance court-reporting professional connected a legal-transcript-management platform's connector eight months ago and has relied on it daily. Today, a request referencing a specific case's transcript returns an error stating the connector cannot access that particular case folder, though other case folders connected through the same platform work normally, and the professional confirms (by checking the platform directly) that this specific case folder's permissions were recently changed by the law firm that owns it, unrelated to the connector itself.
**Options**
- A. Work with the case-owning firm to restore that one folder's permissions: the confirmed cause is a permissions change, and the connector works for every other folder.
- B. Reconnect the connector for this specific case folder only, assuming a folder-level connection can independently expire while others remain active
- C. Switch to manually requesting transcript exports from the firm going forward, to avoid connector issues entirely
- D. Assume the entire connector has become unreliable after eight months and reconnect it fully from scratch

**Answer:** A — This is a harder diagnostic question because it already provides strong, specific evidence pointing away from the connector itself (other folders work fine; the professional already confirmed a permissions change at the source) — the correct answer requires recognizing that the diagnostic work is essentially already done and points to an external cause, rather than still defaulting to connector-focused troubleshooting (B, D) or abandoning the tool (C) despite evidence it isn't the actual problem.

---

### Q83.
A boutique wealth-management firm's Claude Project for a specific high-net-worth client contains that client's portfolio holdings as a knowledge file, refreshed monthly, and separately contains a set of "client communication preferences" notes (e.g., "prefers concise, non-technical summaries") that were accurate when originally written two years ago but have never been revisited, during which time the client has become considerably more financially sophisticated through ongoing engagement with the firm.
**Options**
- A. Preference notes can go stale like factual sources: a client's sophistication evolves, so a two-year-old, never-revisited note should be reviewed periodically.
- B. This should be resolved by deleting the preference notes entirely and asking about communication preferences fresh in every conversation
- C. This is not a real configuration problem, since communication-preference notes are inherently subjective and don't go "stale" the way factual data like portfolio holdings does
- D. This should be resolved by moving the preference notes into account-level instructions instead, so they apply more broadly

**Answer:** A — This is a harder version of the stale-configuration principle because it applies the concept to a *qualitative, preference-based* knowledge item rather than a clearly factual one (like a rate card or portfolio holding) — the correct answer requires recognizing that "soft" configuration content needs the same maintenance discipline as "hard" factual content, just reviewed on its own appropriate cadence, rather than assuming subjective content is exempt from staleness (C) or over-correcting into a different scoping layer (D) or removing structure entirely (B).

---

### Q84.
An associate wants a rule that should apply only when working on a specific ongoing litigation matter, should include several standing reference documents (the complaint, key deposition excerpts, a chronology of events), should not affect any other matter the associate works on, and — new to this scenario — needs different team members (the lead associate, a paralegal, and an outside co-counsel with limited access) to have different levels of visibility into the underlying materials.
**Options**
- A. A Skill, since Skills can be configured with different permission levels for different users
- B. This requirement cannot be met with any current configuration layer and requires a custom integration
- C. Account-level instructions, since they can be selectively shared with specific team members
- D. A single Project, since its scoped, always-on files meet the first three requirements; differentiated access needs platform sharing controls layered on top, not rejecting the Project.

**Answer:** D — This is a harder version of the Project-fit question because it introduces a genuinely separate concern (differentiated user access) that a Project's core file/instruction scoping doesn't natively address — the correct answer recognizes that a Project is still the right foundational tool for the scoping requirements it does solve, while the access-differentiation requirement needs a different, complementary mechanism, rather than concluding the wrong tool was chosen entirely (B) or misattributing access-control capability to Skills (A) or account instructions (C), neither of which are designed for per-user permission differentiation.

---

### Q85.
A mid-sized architecture firm is piloting a Claude connector to its building-information-modeling (BIM) file repository, to support an AI-assisted code-compliance pre-check workflow. The pilot plan calls for read-only access initially, which the team agrees with — but separately proposes testing the pilot using the firm's actual current in-progress projects' real BIM files, reasoning that "these files aren't regulated personal data like patient or financial records, so the synthetic-data-first practice doesn't apply here."
**Options**
- A. The team's reasoning is correct — the synthetic-data-first practice is specifically about regulated personal data, and BIM files for building projects don't fall into that category, so testing with real current project files is acceptable here
- B. The gap is narrower: BIM files aren't personal data but may carry client confidentiality obligations, so synthetic or non-live test files are worth considering.
- C. The team's reasoning is correct, and additionally read-only access alone is sufficient protection regardless of what test data is used
- D. The team's reasoning is entirely wrong, and synthetic data must be used for any connector pilot regardless of data type

**Answer:** B — This is a harder question because it correctly identifies that the *literal* synthetic-data-first rule (aimed at regulated personal data) technically doesn't apply to BIM files, which makes A tempting and technically defensible on narrow grounds — but the correct, more complete answer recognizes that the *underlying reason* for that practice (caution with sensitive, real data during unvalidated pilots) extends to other categories of sensitive information, like client-confidential design files, even when the specific rule's literal scope doesn't cover them.

---

### Q86.
A regional real-estate brokerage's Claude account has developed a memory note, generated over past conversations, stating that a specific listing agent "always wants property descriptions under 100 words." A new listing for this same agent is a luxury property where the agent explicitly requests: "For this one, I want a much longer, more narrative description — really sell the lifestyle, not just the specs."
**Options**
- A. Though the explicit instruction wins here, update the memory note to record that the preference varies, for example 'usually under 100 words, except luxury listings'.
- B. Delete the memory note immediately, since it has now been contradicted
- C. This situation requires no attention at all, since memory notes never actually influence output
- D. Claude will correctly follow the new, explicit in-conversation instruction for this listing, so no action regarding the memory note is needed at all, now or later

**Answer:** A — This is essentially the same category of judgment as the earlier grant-writer/client-tone example (memory note correct-but-incomplete, not wrong) applied in a new context — testing whether the test-taker recognizes the *same underlying pattern* (refine an incomplete-but-accurate memory note rather than assume automatic handling or overreact by deleting it) when it appears in a different, unrelated scenario rather than a directly analogous one.

---

### Q87.
A small rural health clinic wants to connect Claude to its patient-scheduling system for the first time to help draft appointment-reminder messages. The IT lead, having learned from a prior mistake, proposes testing with genuinely synthetic data — but proposes generating that synthetic data by taking the clinic's real patient roster and randomly shuffling which appointment times are associated with which (real) patient names, reasoning "this way the data patterns are realistic, but no name is linked to its real actual appointment anymore."
**Options**
- A. This approach is acceptable as a first step, to be followed by fully synthetic data testing in a second phase
- B. This approach is an acceptable form of synthetic data, since shuffling breaks the real name-to-appointment linkage, which was the sensitive connection
- C. It isn't genuine synthetic data: it reuses real names, now tied to fabricated appointments; genuine synthetic data uses fabricated names and patterns entirely.
- D. This approach is acceptable only if the shuffling is done by a different team than the one building the integration

**Answer:** C — This is a harder test of what "synthetic data" actually means: the IT lead's approach sounds sophisticated (preserving realistic patterns while breaking a specific sensitive link) and represents genuine improvement in reasoning over naive de-identification, but it still uses real identifying information (patient names) and additionally creates a new, distinct problem — real people incorrectly associated with fabricated appointment records — that fully synthetic (fabricated names and patterns) data would avoid entirely.

---

### Q88.
A regional manufacturing company's quality team built a useful, reusable Skill for formatting non-conformance reports according to their ISO-certification documentation standard. A new quality engineer, hired specifically because of prior experience at a company with a very similar but not identical ISO-documentation format, assumes their prior employer's format is close enough and doesn't investigate whether this company has its own Skill, manually recreating a format from memory that turns out to differ in several required fields from this company's actual certified standard.
**Options**
- A. This is a memory problem, since the system should have automatically flagged the discrepancy
- B. This is a Skill-design problem — the Skill needs to be made more prominent so it's harder for a new hire to miss
- C. Mainly an onboarding gap compounded by misplaced confidence: experience with a similar format made the engineer assume no company check was needed; similar isn't identical.
- D. This is a Project-scoping problem, since the Skill should have been built as a Project instead

**Answer:** C — This is a harder version of the onboarding-gap pattern because it adds a specific psychological mechanism (transferable-experience overconfidence) rather than simple unfamiliarity — recognizing that "I've done something similar before" can be a more insidious version of "I didn't know this existed," especially in a compliance context where near-identical isn't sufficient, is the added layer of judgment here.

---

### Q89.
A county elections office has a Claude Project for handling public-records requests related to voter registration data, with standing instructions stating: "Always redact individual voters' personal identifying information before summarizing a request for the public log, except aggregate statistics (e.g., total registered voters by precinct) which should be reported in full." The office has just started receiving a new category of request specifically asking for candidate campaign-finance filings, which are public by law and do include the filer's name as the relevant subject, similar in structure to the earlier business-license-records example but in a different domain.
**Options**
- A. Apply the existing instruction as written, redacting the campaign-finance filer's name since it's "personal identifying information" under the current instruction's literal wording
- B. Remove the redaction instruction entirely, since it no longer applies cleanly to every request category
- C. Move the new request category into a completely separate Project so the original instruction never has to change
- D. Update the standing instructions with a campaign-finance carve-out: filers' names are the public, legally required subject of that request type, unlike voters' registration details.

**Answer:** D — This is a direct application of the same underlying principle as the business-license-records example (an instruction written for one context needs explicit updating, not blanket application or removal, when a genuinely different request category with different disclosure rules emerges) — testing whether the test-taker recognizes the *same pattern* in a new domain (elections/campaign-finance) rather than a directly repeated scenario.

---

### Q90.
A regional airline's flight-dispatch department built a Skill several years ago that formats weather-briefing summaries according to a specific internal template referencing aviation weather codes current at the time. The relevant international standards body has since updated several weather-code definitions, and separately, one experienced dispatcher has been manually correcting the Skill's outdated codes in every briefing without ever reporting this to anyone, considering it "just part of the job now."
**Options**
- A. This is a connector issue, since weather codes should be pulled from a live aviation-weather data source instead
- B. It is still stale configuration: update the Skill to the current weather-code standard, since one dispatcher's quiet manual fix leaves others exposed and masks the source.
- C. This is a training issue; other dispatchers should be taught the same manual-correction habit the experienced dispatcher developed
- D. Since one dispatcher has been successfully correcting the issue manually, the outdated Skill is a minor, already-mitigated problem

**Answer:** B — This combines the stale-Skill pattern with the capability-gap-driving-a-quiet-workaround pattern from Domain 6, testing whether the test-taker recognizes both at once: the Skill genuinely needs updating (not just tolerated because one person compensates for it), and formalizing the workaround as standard practice (C) would perpetuate an undocumented, inconsistent fix rather than correcting the actual source of the problem.

---

## Domain 7 — Troubleshooting and Optimization (10% — Q91–Q100)

### Q91.
A regional water utility's scheduled weekly agent task, which compiles a compliance-monitoring report and emails it to three regulators, has failed silently two weeks in a row after months of reliable operation. The team checks systematically and finds no paused state, no usage-limit issue, no permissions change, and no connector problem — everything appears configured correctly, yet the task still isn't running.
**Options**
- A. Since the systematic plumbing check found nothing, the team should now conclude the issue is unfixable through configuration and revert to fully manual compilation permanently
- B. Recreate the task from scratch on a different automation platform, since the current one has now failed unexplained twice
- C. Rewrite the underlying prompt with significantly more detail, since the plumbing checks came back clean
- D. Widen the systematic check to the scheduling trigger, such as a time-zone or platform-update shift, and to whether the regulators' email systems filter the report.

**Answer:** D — This is a harder version of the systematic-diagnosis principle specifically because the *first-pass* checklist (paused/limits/permissions/connector) came back clean, which could tempt a test-taker to abandon the systematic approach (A, B) or pivot to an unrelated fix (C, prompt rewriting, when the reported symptom was total silence, not poor content) — the correct response is widening the systematic search to less obvious causes, not concluding the diagnostic method itself has failed.

---

### Q92.
A corporate-communications team notices that Claude-drafted press statements have required significantly more editing rounds over the past month than six months ago. Investigation reveals the prompt template is unchanged, no session/context pattern has changed (fresh sessions are still used each time), and the team's style-guide reference document was actually *updated and improved* three weeks ago to reflect newer brand guidelines.
**Options**
- A. Since the style guide was updated (not gone stale), configuration staleness can be ruled out as a cause, and the team should look elsewhere for the explanation
- B. Investigate whether the updated style guide introduced new ambiguity or conflicts with the prompt template; a recent update can add problems as easily as age.
- C. This must mean the underlying task no longer fits AI assistance, given multiple potential causes have been ruled out
- D. This must be a model-capability regression, since every other explanation has been controlled for

**Answer:** B — This is a harder version of the stale-configuration diagnostic pattern because it inverts the usual signal: the reference material was recently *improved*, not neglected, which could tempt a test-taker to rule out configuration as a cause entirely (A) — but a recent change can introduce new problems (ambiguity, internal inconsistency) just as staleness can cause old ones, so "recently updated" should redirect the investigation, not close it off.

---

### Q93.
A hospital's clinical-education team has finally moved away from defaulting to the top-capability model tier for every task, after recognizing the earlier "patient-adjacent content deserves our best effort" pattern was a mismatch for simple tasks. Six months later, a new complaint arises: a genuinely complex task — synthesizing a new multi-source clinical-guideline update into training material spanning several interacting recommendations — was run on the team's new default lighter tier and produced a shallow, incomplete synthesis.
**Options**
- A. The team over-corrected: the principle is matching tier to task complexity, so a genuinely complex multi-source synthesis does warrant the higher tier despite the new lighter default.
- B. This means the team's correction (moving away from a blanket top-tier default) was itself a mistake, and they should return to always using the top tier for anything patient-adjacent
- C. This means extended thinking, not tier, is the only lever that matters, and tier should be set to the lightest option universally
- D. This means model tier doesn't actually matter for synthesis tasks, and the shallow result must have another cause entirely

**Answer:** A — This is a harder, "correcting the correction" question: having internalized one lesson (don't blanket-default to the top tier), the team swung to a new blanket default (always lighter tier) that is just as much a task-fit failure as the original mistake, in the opposite direction — the underlying principle was never "which single tier is right," but "match tier to each task's actual complexity," which this new failure illustrates just as clearly as the original one did.

---

### Q94.
A large nonprofit's grant-reporting associate no longer has to re-explain their organization's mission statement, fiscal year, and standard disclaimers each week (having fixed that recurring-instruction problem by moving it into a Project). A new, different complaint has now emerged: reports drafted within that same Project have started including a specific outdated grant-amount figure from two funding cycles ago, apparently drawn from an old grant-summary document still sitting in the Project's knowledge files alongside newer ones.
**Options**
- A. This means the Project itself was a mistake and the associate should go back to re-explaining context in every chat, since Projects introduce their own new problems
- B. This means extended thinking should be enabled so Claude can infer which grant-amount figure is current
- C. It's a different issue: a superseded knowledge file sitting beside current information lets Claude draw from either, so clean up or date the files rather than adding instructions.
- D. This is the same configuration gap as before (recurring instructions), and the fix is the same: move more content into the Project

**Answer:** C — This tests whether the test-taker distinguishes between two different configuration problems that can occur within the same Project: a missing standing instruction (the earlier problem, now fixed) versus an accumulation of stale, unremoved knowledge files (a new, different problem) — both are "configuration" issues in a general sense, but they call for different specific fixes, and recognizing that the earlier fix (moving content into the Project) doesn't automatically prevent this different failure mode is the harder judgment here.

---

### Q95.
A regional airline's pricing-operations team, having previously traced a sudden fare-recommendation quality drop to a broken reference-document link following an IT migration (and having fixed it), now experiences a second, distinct quality drop three months later. This time, no IT migration or similar infrastructure event has occurred, and the team's first instinct is to assume it must be the same type of broken-reference-link issue as before.
**Options**
- A. Checking the link is reasonable, but don't assume the same cause: no triggering event this time is a meaningful difference, so consider the fuller range of causes.
- B. This must be pure model-quality fluctuation, since the previously-identified cause (a migration-related broken link) is absent this time
- C. Since the previous incident was caused by a broken reference link after a migration, and this is a new quality drop, the team should assume the same cause and immediately check reference-document links first, before anything else
- D. Since the same team experienced a similar-sounding problem before, this confirms a recurring, unfixable weakness in how the Project is configured, and the workflow should be rebuilt from scratch

**Answer:** A — This is a harder version of the diagnostic-order principle testing whether past experience is applied as a reasonable starting hypothesis (worth a quick check) versus an anchoring bias that skips the fuller diagnostic process — the key clue (no triggering event this time, unlike the clearly-dated migration coincidence before) should prevent the team from assuming the same specific cause applies again without evidence, while still not being irrational to check first, cheaply, given it's a known possible cause.

---

### Q96.
A specialty printing company, having previously identified and fixed a tier-mismatch problem (an expensive tier being used for simple print-job descriptions), now sees overall AI usage costs rising again three months later — but this time, order volume has also genuinely increased by 40% in the same period, and the per-job cost (cost divided by number of jobs) has actually decreased slightly.
**Options**
- A. This is the same tier-mismatch problem recurring, and the team should immediately re-audit tier assignments across all task types
- B. This isn't a new tier or configuration problem: total cost rising with 40% more volume while per-job cost falls is healthy scaling.
- C. This means extended thinking must have been inadvertently enabled again and needs to be disabled
- D. This means the previous tier-mismatch fix didn't actually work and should be reverted

**Answer:** B — This is a "recognize when there is no problem" question, testing the same diagnostic discipline in reverse: rising total cost looks like a red flag matching a previously-diagnosed pattern, but checking the *right* metric (per-job cost, which improved) reveals this is likely healthy scaling, not a recurrence of the earlier tier-mismatch issue — correctly diagnosing "no new problem here" is as much a troubleshooting skill as correctly diagnosing a real one.

---

### Q97.
An enterprise-software company's technical-writing team, after correctly diagnosing an earlier vague-feedback problem and switching to specific, source-grounded feedback (point directly at the API schema file), still finds that two specific parameter descriptions remain persistently wrong across several rounds of this improved, specific feedback — even though every other parameter description is now consistently correct.
**Options**
- A. Since specific, sourced feedback has worked for every other parameter, the team should simply repeat the same specific feedback approach for these two remaining parameters, expecting eventual success
- B. This means the model tier needs to be upgraded specifically for these two parameters
- C. This means the task fundamentally doesn't fit AI assistance for at least these two parameters, and they should always be written manually going forward
- D. Investigate what is structurally different about those two parameters in the schema, such as inherited or aliased definitions the general instruction handles less directly.

**Answer:** D — This is a harder, "the general fix didn't fully generalize" version of the troubleshooting principle: rather than a single fix resolving everything (as the simpler version of this pattern might suggest), a persistent, narrower failure surviving an otherwise-successful fix points to something specifically different about the remaining cases — investigating that structural difference is the right move, not simply repeating the general fix harder (A) or concluding total task-unsuitability (C) for what may be a narrow, explainable edge case.

---

### Q98.
A national retailer's loyalty-program team, having previously over-corrected toward "offers generated per hour" as an optimization target (and having since re-optimized toward redemption rate instead), now finds that redemption rates have improved substantially, but a new concern has emerged: the offers achieving the highest redemption rates are disproportionately steep discounts that are eroding profit margins more than the previous, lower-redemption-rate offers did.
**Options**
- A. Redemption rate alone is incomplete: offers can hit it while hurting profitability, so the workflow likely needs a combined objective, such as redemptions weighed against margin.
- B. Since redemption rate was correctly identified as the metric that actually mattered, and it has now improved substantially, this is a clear success with no further optimization needed
- C. This means the team should revert to optimizing for raw volume instead, since both redemption rate and volume have now shown problems
- D. This means AI assistance should be removed from the offer-generation workflow entirely, since two different optimization targets have each caused problems

**Answer:** A — This is a harder, second-order version of the optimize-for-the-right-metric principle: having already corrected one single-metric-optimization mistake (volume), the team discovers that its replacement single metric (redemption rate) has its own blind spot (profitability) — the lesson generalizes further than either individual fix: a single proxy metric, whichever one is chosen, can still be gamed or over-optimized in a way that misses the actual underlying business purpose, which usually requires a combined or balanced objective, not a search for the one "correct" single metric.

---

### Q99.
A metropolitan transit agency, having previously fixed a stale-route-number problem in its service-alert drafting workflow (by updating the reference document after a system-wide route overhaul), now encounters a new complaint: alerts have started using an old, discontinued fare-payment method name that was phased out four months ago, in a completely different part of the same alert template than where the route-number issue was.
**Options**
- A. Since the team already knows the general category of past cause (a stale reference document), they should assume the fare-payment-method reference document has also gone stale in the same general knowledge-source location as the route-number document, and check there first
- B. This means the whole alert-drafting Project should be rebuilt from scratch, since stale content keeps recurring in different forms
- C. Verify which reference source actually feeds the fare-payment language rather than assuming it is the route-number document; a different template part may use a different source.
- D. This must be an entirely new type of problem unrelated to configuration, since the team already fixed the configuration issue once

**Answer:** C — This is a harder version of "recognize the general pattern without over-anchoring on the specific prior instance": the general diagnostic category (stale reference content) is likely correct and worth checking first, but the correct answer specifically cautions against assuming it's the *same* document/location without verifying, since a genuinely different part of the template may draw from a genuinely different, separately-maintained reference source.

---

### Q100.
A specialty food distributor's finance team, having previously declined to remove analyst review from rebate calculations that closely matched the prior month (recognizing that similarity to a prior result doesn't prove correctness), now proposes a different, more targeted safeguard: automatically flagging for extra scrutiny any month-over-month rebate calculation that matches the prior month within 1% *and* where the underlying sales-volume input also happens to be nearly identical to the prior month's — reasoning that this specific combination is the actual scenario most likely to indicate a stale-input error, rather than treating all close matches with equal suspicion.
**Options**
- A. It is a genuine refinement: flagging a close output match with a suspiciously identical input targets the real signature of a stale-input error, while keeping human review.
- B. This refined approach is still fundamentally flawed for the same reason as before: any near-match, however specifically characterized, should never receive different treatment than any other output, and this refinement doesn't change the core issue
- C. This refined approach is flawed because it still requires human review at all, when a sufficiently specific automated check should be trusted to resolve the concern without any review step
- D. This refined approach is unnecessary, since the original full-review policy the team already retained makes any additional flagging logic redundant

**Answer:** A — This is a deliberately sophisticated closing question testing whether the test-taker can distinguish a *genuine refinement* of a previously-correct judgment from a backslide into the original flawed reasoning: the team isn't proposing to remove review based on similarity (the original error) — they're proposing a more precise way to *prioritize* review effort by identifying the specific mechanism (matched output plus suspiciously matched input) that actually signals elevated risk, while still keeping review itself in place, which is a legitimate, more sophisticated application of judgment rather than either the original mistake (C takes it too far by removing review; B wrongly treats any refinement as impermissible) or mere redundancy (D, which misses that even a retained safeguard can be usefully prioritized).

---
[⬅ PCAO-F Index](README.md) · [Companion sets: `pcaofexamquiz.md`](pcaofexamquiz.md) · [`pcaofexamquizv1.md`](pcaofexamquizv1.md)
