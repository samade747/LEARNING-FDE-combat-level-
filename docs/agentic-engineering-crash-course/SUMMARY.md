# Agentic Engineering Fundamentals — Summary

"8 Concepts, 80% of Real Use." Thesis: software fundamentals matter MORE in the AI era, not less —
agent's interface/names/boundaries become its inputs. Fetched: Zia Tutor AI generation 82, 2 windows
+ quiz block (complete), 2026-10-22.

## 00 — Overview

- 7-stage pipeline (idea → grilling → PRD → issues → implementation → review → QA), 5 Skills,
  Claude Code + OpenCode identically.
- Prerequisite: Agentic Coding Crash Course (tools); this page teaches discipline.

## 01 — Vibe Coding → Agentic Engineering

- Software 1.0 (code) → 2.0 (weights) → 3.0 (prompting, artifact = text for an agent).
- Vibe coding raises the floor; agentic engineering preserves the ceiling. Payroll/regulated/
  multi-user work = vibe coding is malpractice.

## 02 — Three Constraints

- **Smart zone/dumb zone:** attention budget dilutes as session fills, ~100k token practical
  waterline regardless of advertised window.
- **Memento problem:** stateless models, clearing > compaction (compaction carries dumb-zone
  reasoning forward).
- **Jagged intelligence:** peaks where RL-verifiable (code/math), valleys elsewhere. 4 implications
  incl. "choose on-distribution stacks."

## 03 — Six Failure Modes

- Misalignment (cure: `grill-me`), verbose agent/no shared language (cure: `CONTEXT.md`), weak
  feedback loops (cure: `tdd`), ball of mud/shallow modules (cure: `improve-codebase-architecture`),
  brain saturation (cure: gray-box), review bottleneck (cure: automated+human review split).

## 04 — End-to-End Workflow

- Day shift (human-in-loop) / Night shift (AFK, sandboxed) alternation, mediated by durable
  handoff artifacts.
- Specs are handoff artifacts, not the whole workflow — they decay.
- Vertical slices (tracer bullets) > horizontal slicing.

## 05 — Skills as Encoded Process

- Skill = agent reads (on-demand); Tool = agent calls. Portable across Claude Code/OpenCode.
- 5 principles × current best Skills: `grill-me`, `to-prd`, `to-issues`, `tdd`,
  `improve-codebase-architecture`. 6th: `grill-with-docs`.

## 06 — Pipeline in Practice (Gamification Worked Example)

- Full worked walkthrough: grilling → PRD → vertical-slice issue board → TDD slice (Python
  `GamificationService`) → sequential/parallel/persistent AFK loops → human review+QA (found a
  null-check bug the agent's tests missed, became a new issue).

## 07 — Architecture Principles

- Deep modules (small interface, large hidden implementation) vs shallow (9-function gamification
  example). Test at the interface. Gray-box: design interface, delegate implementation.
  `improve-codebase-architecture` Skill for periodic deepening.

## 08 — Working Vocabulary

- 18 terms: Model, Harness, Agent, Context window, Smart/dumb zone, Hallucination, Clearing,
  Compaction, Handoff, AFK, Skill, Tracer bullet, Deep module, Design concept, Grilling, Vibe
  coding, Agentic engineering, Jagged intelligence, On distribution, Loop/Routine.

## 09 — Practical Drills

- 3 drills with concrete "what good looks like" benchmarks (15-40 questions for grilling, <1
  session per slice, 3:1+ symbol-ratio for deepening). Real scaffolds in `projects/`.

## 10 — Closing: The Strategic Programmer

- Agent = tactical (sergeant); human = strategic (which hill, design concept, map). "You can
  outsource your thinking, but you can't outsource your understanding" (Karpathy). Printing-press
  analogy (Boris Cherny): domain experts will write their own software.

## 11 — Test Your Understanding

- Book's own 18-question `<Quiz>` block (English, verbatim) with explanations.
