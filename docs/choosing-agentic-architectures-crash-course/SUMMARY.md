# Choosing Agentic Architectures — Summary

Mode 2 Phase 3, Chapter 8/9. Anchor: Bala Priya C, ML Mastery, May 2026. **22 Concepts, 5 Decisions, 4
tracks.** Core idea: **pattern selection architectural fit hai, capability matching nahi** — simplest
pattern chuno jo task maangta hai, complexity sirf demand hone par add karo.

## 00 — Overview

4 claims course defend karta hai: (1) fit-matching not capability-matching, (2) 5 sawal deterministically
starting pattern decide karte hain, (3) pattern selection deployment/eval ke sath compose hoti hai, (4)
decision tree starting point hai, final answer nahi. 4 learning tracks (Reader ~2-3hrs → Advanced ~4-5
days). 5 sawal: Q1 path known? →Q2. Q2 fixed/stable? →Sequential Workflow. Q3 structure articulable?
→Planning+ReAct / Single Agent+ReAct. Q4 quality>speed+checkable? → +Reflection layer. Q5 specialization/
context/scale bottleneck? → +Multi-Agent. (Q1-Q3 core pattern; Q4-Q5 additive layers.)

## 01 — Pattern-Selection Problem (Concepts 1-3)

1. Build-se-pehle design work — pattern catalogs mature hain (ReAct 2022, Planning from STRIPS,
   Reflection 2023) lekin **choosing** logic missing hai. Failure: impressive-lagne-wala pattern default
   (usually multi-agent) jab simple task ho.
2. **Har pattern ek bet hai** task ke shape ke baare mein — 5 patterns ki bets describe hui (sequential=
   steps known/stable; ReAct=path unknown; Planning+ReAct=stages known content unknown; Reflection=
   quality>speed+checkable; Multi-agent=specialization/context/scale genuine bottleneck).
3. **2 Failure Modes**: Overshooting (elaborate pattern jo zaroorat nahi — famous, visible; e.g. 3-agent
   LinkedIn post) — undo mushkil (rewrite not refactor). Undershooting (simpler than needed — less
   discussed, more dangerous, silently brittle). Dono equally important.

## 02 — Five-Question Decision Tree (Concepts 4-8 + Bridges)

Q1 (path define-able? — "bina LLM ke Python function likh sakte ho?" heuristic), Q2 (fixed/stable? —
known≠stable, "known-on-average" trap), Q3 (structure articulable? — stages not steps; Q2 vs Q3
confusion warning), Q4 (2 conditions: quality>speed AND checkable criteria; critic must differ from
generator), Q5 (3 claims — specialization/context/scale — with quantitative triggers table: tool-
routing errors ~1/3 category, holdout accuracy drop ~10pts 15K→45K tokens, 5+ parallel subtasks+2x
latency, 10x throughput ceiling; evidence hierarchy production-trace>holdout>domain-analysis>"feels
like"). **Bridge 8.5**: SDK primitives per pattern table (`Agent`,`Runner.run`,`@function_tool`,
`handoff()` vs `as_tool()` distinction, guardrails). **Bridge 8.6**: Inngest operational envelope
mapping (`step.run`, `wait_for_event`, concurrency/throttle/priority, fan-out, replay) — 2 failure modes
invisible at diagram level: mid-flight crash cost ($30-600/month waste), coordination-at-scale.

## 03 — Five Patterns In Depth (Concepts 9-13)

Har pattern: SDK shape, deployment topology, eval signals, operational envelope.
9. **Sequential Workflow** — narrow typed Agents, no tools/handoffs; smallest cloud stack (no
   sandbox); step-level correctness evals; Inngest's most direct fit.
10. **Single Agent+ReAct+Tools** — Agent+multiple @function_tools, `max_turns` budget; full cloud
    stack; reasoning-trace evals; 1 step.run wraps whole loop.
11. **Planning+ReAct** — structured-output planner + per-stage ReAct specialists; plan persisted in
    Neon; per-stage step.run (biggest crash-savings of any pattern).
12. **Reflection (additive)** — output_guardrail (lightweight) vs critic-refiner loop; rubber-stamping
    is the hardest failure to detect (measure net-positive not "does it run").
13. **Multi-Agent** — 3 SDK topologies (as_tool coordinator, handoff sequential, parallel+synthesizer);
    3 separate scoreboards (specialist quality×routing×integration = compounding ~68% example);
    quantified Inngest savings (2,000-7,000 hand-rolled lines → 50-200 with Inngest).

## 04 — Failure Signals Aur Pattern Revision (Concepts 14-16.5)

5 signals (loops/revisits, plan-execution divergence, reflection not improving, routing failures,
complex-but-not-better) each with observability tell + likely-cause ranking. **Targeted fixes table**:
try cheapest fix first (prompt/contract) before architectural change. 3 situations where the tree is
wrong (task properties change post-deployment, sub-tasks need different patterns, constraints override
answer). Anti-pattern gallery: 5 overshoot + 3 undershoot examples with correct starting pattern.

## 05 — The Decision Lab (5 Decisions)

Full tree-walks for: Maya's Tier-1 Support (Single Agent+ReAct), Incident Response (Planning+ReAct+
Reflection on remediation), Market Research (Multi-Agent+Planning+Reflection, justified by context
bottleneck not "thoroughness"), Enterprise Onboarding (Sequential Workflow — negative example for
agentic patterns, cheapest deployment), Coding Agent (hardest case — all 4 patterns composed). Each with
deployment topology, eval signals, most-likely-failure+fix, operational envelope. "6th Decision" exercise
for the reader with self-check.

## 06 — Honest Frontiers Aur Closing (Concepts 17-19)

17. Cost/latency are architectural constraints not afterthoughts — cost-per-task multiplier table
    (Sequential 1x → Multi-agent+Reflection 30-60x); 3 options when budget violated (change constraints/
    scope/accept worse fit — document the choice).
18. Pattern composition — hierarchical/sequential/conditional shapes; each layer justified by its own
    5-question walk; test: remove top layer, did output degrade?
19. Connective tissue in the curriculum — bridges agent-building and shipping courses; deployment-cost
    gap example (~$130/mo vs ~$400/mo for same workload from over-elaboration). Quick reference (5Q tree
    ASCII), 5-decisions table, printable Design-Review Template (8 sections), references list (Bala
    Priya C anchor article, ReAct/Voyager/Reflexion papers).
