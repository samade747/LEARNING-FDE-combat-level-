# 09 — Test Your Understanding (20-Question Assessment)

Book ke apne `<Quiz>` block se verbatim (English, precision ke liye). Har sawal ke sath explanation +
source section diya gaya hai.

1. **Q:** A ledger and a Vertical System of Record are both authoritative. Over what, respectively?
   **A: The ledger over state, the Vertical SoR over rules and method.** *(Two kinds of record, and the layer above them)*
2. **Q:** QuickBooks is asked whether a lease should have been classified as a finance lease. What is the correct account of its silence?
   **A: It is authoritative about what was recorded, and silent about whether it should have been.** *(QuickBooks holds the data)*
3. **Q:** Why does this book avoid the phrase 'a traditional System of Record only stores data'?
   **A: Because it undersells controls the business depends on, and will cost you the meeting.** *(One word of caution)*
4. **Q:** What is the risk when a context packet is compressed to fit a token budget?
   **A: Provenance is stripped, turning evidence into text.** *(What the layer assembles: the context packet)*
5. **Q:** Why can a language model not serve as the source of truth, even when its answer is correct?
   **A: Because it has no register row, cannot be versioned, and cannot be corrected in place.** *(The model is not a source either)*
6. **Q:** Which of these is NOT one of the three quiet ways a model becomes the source?
   **A: The typed query, where an exact value is fetched from the system that owns it.** *(Three places the model quietly becomes the source)*
7. **Q:** What is the model actually for, in this architecture?
   **A: The middle eighty: applying the reflex, calculating, spotting conflicts, and drafting.** *(What the model is actually for)*
8. **Q:** What is the one law of the System of Context?
   **A: It carries authority, and never holds it.** *(The one law: authority never moves)*
9. **Q:** In what sense does the System of Context sit above the Systems of Record?
   **A: It sees across them, for access.** *(Three layers, three jobs)*
10. **Q:** A customer runs an accounting Vertical SoR and a sales Vertical SoR. Sales says the deal closed in June, accounting says the revenue is not recognisable yet. What is the correct handling?
    **A: Resolve by scope: both are right about their own question.** *(Authority is scoped across many records)*
11. **Q:** You build one vertical, but the customer may run several. What does authority routing then require?
    **A: Routing that resolves the profession first, before which source inside it governs.** *(Authority is scoped across many records)*
12. **Q:** A buyer asks for a twenty percent discount with the revenue recognised this quarter. How should the layer handle it?
    **A: Decompose it, route each part to the record that governs it, and assemble one packet.** *(Authority is scoped across many records)*
13. **Q:** What is the difference between discovery and confirmation?
    **A: Discovery asks where information might be, confirmation asks which source is officially applicable.** *(What may be indexed, and what must be asked)*
14. **Q:** May a Vertical System of Record's governed pages be synchronized into a search index?
    **A: Yes, for discovery, provided every item keeps its canonical identity and is confirmed before it is relied on.** *(What may be indexed, and what must be asked)*
15. **Q:** Why is chunking the place governance disappears?
    **A: Because twelve controls travel with a governed entry and a generic pipeline keeps only the sentence.** *(Why chunking is where governance disappears)*
16. **Q:** Why is there no single global source hierarchy across all connected systems?
    **A: Because different sources govern different questions.** *(Authority is scoped across many records)*
17. **Q:** A Worker asks for the current balance in an account. Which path answers it?
    **A: A typed query over MCP against the system that owns the number.** *(The three questions, and the three paths)*
18. **Q:** What is a context packet?
    **A: A temporary cited bundle for one actor, case, and moment.** *(What the layer assembles: the context packet)*
19. **Q:** When must information be fetched live rather than read from an index?
    **A: When a stale value could change the conclusion, permission, payment, filing, or action.** *(What may be indexed, and what must be asked)*
20. **Q:** Why must permission be enforced before the model, not after?
    **A: Forbidden content must never enter the model context at all.** *(Permission comes before the model)*

<details>
<summary>Questions 21-29 (full explanations)</summary>

21. **Q:** In a law-governed profession, why is a permission failure worse than a privacy problem?
    **A: Because it grants effective access outside the entitlement model the access review certifies.**
    *Explanation:* Segregation of duties is about combinations of ability (creating a journal entry and also approving it), not visibility — read access alone is usually not an SoD conflict. The real exposure is one layer lower: access control is the foundation the rest of the control environment stands on, so a layer that hands a user content their entitlements never granted leaves the periodic access review certifying a picture that is not true. *(Permission comes before the model)*
22. **Q:** What should happen when two relevant sources disagree?
    **A: Preserve the conflict, resolve authority, or escalate.**
    *Explanation:* The layer keeps sources separate, preserves provenance, tests authority and scope, then resolves or escalates. A conflict has exactly three outcomes: resolved by scope, resolved by authority, or unresolved-and-escalated with evidence already organized. *(Conflict is a result, not a retrieval failure)*
23. **Q:** A three-year-old internal email says 'we always capitalise these.' How may a Worker use it?
    **A: As supporting context: read it, attribute it, never cite it as the requirement.**
    *Explanation:* The correct answer routes the requirement to the standard in the governed record and flags the email against it if they disagree — an accounting error repeated for twelve months remains an error. *(Provenance travels with every item)*
24. **Q:** Where should an executed action be recorded?
    **A: In the source system that owns the result.**
    *Explanation:* The Worker acts through governed tools, and the system that owns the record records the result; the conclusion and evidence enter the governed case record. The context layer must never become a shadow transaction system. *(Read, reason, act, and record)*
25. **Q:** Which layer of the FDE AF Model holds the reusable part of a System of Context?
    **A: Layer 3, which holds the pattern: authority maps, packet schemas, connector templates, and evaluations.**
    *Explanation:* Layer 3 holds assets generic to the profession with no customer data. Layer 4 binds the customer's actual applications, identities, and records — that is where the layer becomes real. The Layer 3 pattern is the asset you carry; Layer 4 fitting is the work you perform. *(Where it sits in the FDE AF Model)*
26. **Q:** Does this page contradict the book's 'consolidate by default' stance?
    **A: No: consolidation holds when one set of invariants governs all the data.**
    *Explanation:* Specialization is correct when two sets of invariants pull in opposite directions — the record needs exactness/versioning/audit trail, the customer's world needs breadth/freshness/permission fidelity from systems you don't control. Forcing them together makes both worse. This is the clearest example of the word "deliberately," not an exception to it. *(Consolidate by default, specialize deliberately)*
27. **Q:** Which product is this book's open reference implementation of a System of Context?
    **A: Onyx.**
    *Explanation:* Onyx is chosen because the architecture is inspectable — a student can connect sources, trace one request end to end, test a conflict, and replace a component. Glean is the commercial reference point. *(The open reference implementation)*
28. **Q:** Which four interfaces must stay open so the context layer remains replaceable?
    **A: MCP, OpenAPI, connectors and ingestion APIs, and source-owned identifiers and citations.**
    *Explanation:* MCP carries agent-facing knowledge/tools, OpenAPI carries governed application capabilities, connectors/ingestion APIs carry synchronized content, and source-owned identifiers/citations mean the layer can be swapped without losing the record. *(The open reference implementation)*
29. **Q:** When should a vertical build a System of Context?
    **A: Only when the answer to 'why was it done this way' lives outside every governed system.**
    *Explanation:* A single MCP connection to the system that owns the numbers is a tool, not a System of Context. The hard gate: the thin slice must be finished and a Worker must already cite it — a connecting layer with nothing governed to connect to is a search box with ambitions. *(When you do not need one)*

</details>

30. **Q:** What does Ayesha test before she tests any professional answer?
    **A: Permissions, by asking as a junior a question whose correct answer is nothing.** *(Ayesha connects her first customer)*
31. **Q:** Six weeks in, Ayesha's Worker finds that the firm's 2023 memo disagrees with the current standard. What is the correct behaviour?
    **A: Report both, name the authority test applied, and escalate to the partner.** *(Ayesha connects her first customer)*
32. **Q:** Which failure mode describes a long prompt that tells the model how to interpret ten systems, while the connections and checks are never implemented?
    **A: The prompt as integration layer.** *(The failure modes)*
33. **Q:** What must the evaluation set contain beyond successful searches?
    **A: Retired policies, wrong jurisdictions, missing permissions, conflicts, and source outages.** *(The definition of done)*

---
[⬅ Appendix + Recap](08-appendix-and-recap.md) · [⬆ Index](README.md)
