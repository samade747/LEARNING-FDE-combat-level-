# 09 — Worked Example + Capstone

## Ek Real-Looking Task Par Poora Loop

**Task family:** Ek complex incoming artifact review karo, jo important hai woh identify karo, verified
claims ke sath structured response banao.

- *Engineer track:* Contractor se PR aayi hai. Diff review karo, risks flag karo, response likho.
- *Domain-expert track:* Vendor se MSA (master services agreement) aaya hai. Firm ke redline standard
  se deviations flag karo.

Alag domains, **identical workflow shape.**

## Chaar Phases, Chaar Prompts

**Phase 1 — Explore (P1, P7).** Read-only:

```text
Don't make any edits yet. Read the PR diff... Summarize:
  - What this PR is changing
  - Which files are touched
  - Any obvious risks (max 5)
Save the summary to reviews/pr-explore.md. No code edits.
```

**Phase 2 — Plan (P2, P5).** Structured artifact, save karo, approve hone tak ruko:

```text
Read reviews/pr-explore.md. Produce a review plan:
  ## Review plan
  - Files to inspect in depth (max 5)
  - Tests to run
  - Concerns to flag (severity: HIGH / MED / LOW)
  - Questions for the contractor
Save to reviews/pr-plan.md. Pause for my approval before continuing.
```

**Phase 3 — Implement (P4, P3).** Ek item ek waqt, har claim grounded:

```text
Execute the plan one item at a time. After each item:
  1. Produce the output
  2. Verify it against the source, quote specific lines
  3. Save a numbered version (e.g., step3.md)
  4. Wait for my OK before the next item.
If you can't ground a claim, flag it instead of fabricating.
```

**Phase 4 — Commit (P6, P7).** Final verification, assemble:

```text
Final verification pass:
  - Every cited claim is grounded in a source location
  - The structure matches the plan
  - The tone matches CLAUDE.md / AGENTS.md
Then assemble the final deliverable with executive summary, numbered
findings, review checklist, and "Rules-file proposals" section.
```

**Result:** Har phase apni file deta hai — explore, plan, numbered steps, final. Plan audit trail hai;
numbered steps kaam hain; final file woh hai jo ship hoti hai. **Slower pehli baar clock-time mein;
hamesha ke liye faster trust-time mein**, us ek prompt ke muqable jo sab kuch ek block mein deta hai
bina kisi checkpoint ke.

## Capstone — Apne Kaam Par Poora Loop

Hello-world curated example par tha. Capstone open-ended hai: same loop, aapka kaam, aapki stakes. Ek
real task chalao chaaron phases se, **consciously naam lo** har step kaunsa principle invoke karta hai —
naming hi long-term memory mein wire karta hai.

**Setup:** Ek recurring task chuno jo 60+ minute leta ho (privilege log, variance commentary, campaign
report, hiring brief, code-review-merge cycle). Jitna lamba aur recurring, utna acha — jo rules file
banegi woh har future run par wapis dega.

| Phase | Kya Karna Hai | Principle |
| --- | --- | --- |
| Explore | Relevant inputs parho, structured summary file banao. Koi writes nahi. | P1, P7 |
| Plan | Structured plan mango. Save karo. Parho. Edit karo. Approve karo. | P2, P5 |
| Implement | Ek step ek waqt execute karo, verification check har ek ke baad. | P4, P3 |
| Commit | Final verification, summary, rules file update karo. | P6, P7 |

**5 Sawal Journal Karne Ke Liye:**
1. Manual baseline ke muqable total time?
2. Kaunsa principle sabse mushkil laga apply karna? Kyun?
3. Rules file mein kya add hua?
4. Kaunsi constraint tighten ki?
5. Kaunsa failure pattern dikha (Drift/Confident Wrong/Big Bang/Scope Creep/Black Box)?

**Compounding step:** Agle hafte wahi task, isi rules file ke sath dobara chalao. Doosri run usually
40-60% tez hoti hai. Teesri run par rules file barhna band ho jata hai aur discipline invisible ban jata
hai — **yehi threshold hai jahan "principles seekhna" se "principles use karna" cross hota hai.**

## Get Good At This

Course parhna aapko agents direct karne mein acha nahi banata — **use karna** banata hai. Aap manual se
shuru hote ho, friction mehsoos karte ho, har friction ek principle ki taraf ishara karta hai:

- "Agent sirf chat kyun kar raha hai?" → P1
- "Output baar baar subtly ghalat kyun?" → P2
- "Yeh confident jawab ghalat kyun nikla?" → P3
- "Ek prompt ne aadha kaam kyun nuke kar diya?" → P4
- "Agent baar baar wahi context kyun poochta hai?" → P5
- "Agent aisi folder kyun chhui jo mention nahi ki?" → P6
- "Mujhe pata kyun nahi agent ne kya kiya?" → P7

**Response har friction par banao, pehle se nahi.** Rules file 10 lines se shuru ho, phir 12, phir 20 —
har line ek galti se seekhi hui. Speculative-likhi rules file documentation hai; friction se ugi hui
rules file **memory** hai — sirf yehi agli session mein zinda rehti hai.

> **Course complete hone ki nishani:** (1) Chatbot prompt ko action-with-artifact mein reframe kar sako,
> (2) content se pehle output shape likh sako, (3) do independent verification paths naam le sako aur
> ek use kar sako, (4) kaam ko checkpoint ke sath atomic units mein todo sako, (5) rules file line-by-line
> maintain kar sako aur kisi bhi session ka behavior uske execution trace se explain kar sako.

---
[⬅ Four-Phase Workflow](08-four-phase-workflow.md) · [⬆ Index](README.md) · [Agla: Quick Reference ➡](10-quick-reference.md)
