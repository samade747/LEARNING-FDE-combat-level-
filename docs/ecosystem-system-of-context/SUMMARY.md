# The System of Context — Summary

Vertical SoR + customer's real applications/identities ke beech ka connecting layer. Fetched: Zia
Tutor AI generation 82, 2 windows (complete), 2026-10-22.

## 00 — Overview

- Core line: "A System of Record decides what is true. A System of Context decides what arrives."
- 2 record kisam (traditional SoR = state, governed knowledge record = rules/method) + layer jo
  koi apni truth nahi rakhti.
- 3 layers, 3 jobs: Systems of Record (what's officially true) → System of Context (what's relevant
  now) → Worker (reason+act).

## 01 — One Law + Model Not a Source

- **The System of Context carries authority. It never holds it.**
- Model source nahi ban sakta: no register row, plausibility ≠ provenance, release dated ho sakta
  hai propositions nahi, permission enforcement point nahi ho sakta.
- 3 quiet leaks: gap fill, drifting paraphrase, unmanaged persistent model memory.

## 02 — Authority Scoped + Three Paths

- Federated — many records, har ek apni authority, koi merge nahi. 8 routing questions, profession
  pehle route hoti hai.
- 3 questions/paths: rule (retrieval, governed) / number (typed query, live) / case-talk (retrieval,
  ungoverned, supporting context only).

## 03 — Context Packet + Indexing Rules

- 7 operations: connect, identify, retrieve, filter, rank, assemble, deliver. Packet = 8
  compartments, temporary, inherits authority+permissions, expires.
- "Index working context. Discover governed knowledge. Query current truth live." Chunking 12
  controls kho deti hai, sentence bachti hai.

## 04 — Permission, Provenance, Conflict

- Permission model se pehle enforce honi chahiye (safe order vs unsafe order). SoD visibility nahi,
  combinations ka masla hai — real exposure access-review-invalidation hai.
- Provenance = 9 fields per item. Conflict = resolved-by-scope / resolved-by-authority / escalate.

## 05 — Read-Reason-Act + 8 Invariants + Placement

- 5 jobs order mein: layer finds, Worker reasons, record validates, tool acts, owner records.
- **8 Invariants** (authority/relevance/permission/freshness/provenance/conflict/promotion/
  discovery-vs-confirmation).
- FDE AF Model: Layer 3 (pattern, no customer data) + Layer 4 (customer binding). "Consolidate by
  default, specialize deliberately."

## 06 — Reference Implementation + Ayesha

- Onyx = open reference implementation; Glean = commercial reference. 4 interfaces must stay open
  (MCP, OpenAPI, connectors, source-owned IDs).
- Build it only when institutional memory is part of the deliverable — not automatically.
- Ayesha's Chicago engagement: routes authority before connecting, tests permissions (junior →
  "nothing") before testing answers, writes a one-line design-record rule.

## 07 — 11 Failure Modes + 4 Templates + Definition of Done

- 11 named failure modes (flat index, flattened portfolio, reliance on the copy, stale answer,
  retrieve-first-hide-later, model as quiet source, prompt as integration layer, citations without
  provenance, blended conflict, shadow record, product-shaped doctrine).
- 4 templates: connected source register, authority routing map, boundary contract, permission test
  set (must include a "nothing" test).
- ~20-item definition of done.

## 08 — Appendix + Recap

- Full 8-step worked example (20% discount + June revenue, resolved by scope).
- One-sentence architecture compression + "where to go from here" + one-poster summary.

## 09 — Test Your Understanding

- Book's own 33-question `<Quiz>` block (English, verbatim) with explanations.

No `projects/` folder — this is architectural/conceptual; the hands-on build lives in its own
chapter ([Building the Context Layer](../context-layer-crash-course/README.md)). The 4 templates in
file 07 are the practical scaffolds for a real engagement.
