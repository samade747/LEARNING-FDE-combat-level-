# Designing the Vertical System of Record from First Principles

*Source: The AI Agent Factory — "The Ecosystem" group, lesson `ecosystem-designing-the-vertical-sor`,
poora `mcp__claude_ai_Zia_Tutor_AI__read_agent_factory_lesson` se fetch kiya (2026-08-27, teen windows,
`next: null` tak) — pehle yeh chapter galat source (KSoR SDK GitHub README + PDF) se bana tha, ab book
ke apne lesson se rebuild hua hai (AGENTS.md rule 3).*
*Group: The Ecosystem*

## Yeh Chapter Kis Baare Mein Hai

Aapne apna vertical choose kar liya ([Choosing Your Vertical](../ecosystem-choosing-your-vertical/README.md)),
expert sign ho chuka hai, sources ka rights-basis likhit mein hai — koi customer abhi nahi bika. Ab
sawal: **is System of Record ke andar jaata kya hai?**

Tempting jawab galat hai: profession ke current workflows collect kar ke searchable bana do. Woh
workflows agentic-AI-era se pehle bane thay — insaani limits aur purani technology ke around design
hue. Is page ka method: **first-principles, legacy-informed redesign**. Purane kaam se sachaiyan nikalo,
phir un sachaiyon se dobara banao — AI Workers ke liye, na ke insanon ke liye.

**Nau shabd jo yeh page use karta hai:** Corpus (governed source docs jo agent cite karta hai), Map
(index jo bataye kya knowledge exist karti hai aur kab parhni hai), Outcome (complete professional
result jo value banata hai), Slice (ek outcome, poora covered), Invariant (rule jo har case mein sach
rahe), Evidence, Judgment (professional decision jo simple rule mein reduce nahi hoti), Reflex (complete
procedure jo Worker load kar ke whole follow kare), Workflow archaeology (purane kaam ko study karna
uske real rules/controls/reasons dhoondne ke liye).

## Index

1. [00 — First Principles: Kyun Purana Workflow Blueprint Nahi Hai](00-first-principles-and-old-workflow.md)
2. [01 — Outcome Se Shuru Karo, Phir Workflow Archaeology](01-outcome-and-archaeology.md)
3. [02 — Three-Bin Sort Aur Source Hierarchy](02-three-bin-sort-and-hierarchy.md)
4. [03 — Do Content Classes: Authority Vs Orientation](03-authority-vs-orientation.md)
5. [04 — Decisions, Rules/Judgment/Permissions, Exceptions, Rebuild Reflexes](04-decisions-rules-exceptions-reflexes.md)
6. [05 — 8 Failure Modes + Ayesha Ka Worked Example](05-failure-modes-and-ayesha.md)
7. [06 — 7 Templates + Definition of Done](06-templates.md)
8. [07 — Appendix A: Sales System of Record (End to End)](07-appendix-sales-sor.md)
9. [08 — Appendix B: General Ledger System of Record (End to End)](08-appendix-ledger-sor.md)
10. [09 — Dono Appendices Ka Contrast, Poster, Aage Kya](09-appendices-contrasted-and-next-steps.md)
11. [10 — Test Your Understanding (Scenario-Based)](10-test-your-understanding.md)
12. [Quiz — Book Ka Apna 59-Question Assessment](quiz.md)

## Ek Line Mein Poori Cheez

> Purane workflow ka har step khud profession nahi hai — zyada tar steps insaani limits (attention,
> scattered info, department handoffs) ya purani technology ka workaround hain. **Bin 1** (law/trust)
> ko rakho, **Bin 2** (human limits) ko Worker capability + checker mein rebuild karo, **Bin 3** (purani
> tech) ko delete karo. Ek complete, proven **thin slice** — ek outcome, poora covered, governance day
> one se — hi woh credential hai jo sponsor conversation kamati hai.

## Practice Projects

[`projects/fill-the-templates/`](projects/fill-the-templates/README.md) — worksheet-style project
(jaisa harness-engineering ka `tool-diet`/`ratchet-week`): apna vertical choose karo, 7 templates ko
apne outcome par fill karo, Ayesha ka worked example reference-solution ki tarah use karo. Koi code
nahi, structured exercise hai.

## Is Repo Ke Baaqi SoR Content Se Rishta

- [Agent Factory System of Record](../ecosystem-system-of-record/README.md) — is book ki apni SoR;
  yeh chapter usi pattern ko kisi bhi vertical ke liye generalize karta hai
- [The FDE AF Model](../ecosystem-fde-af-model/README.md) — "ek component, kai corpora" framing, SoR
  Layer 1
- [Choosing Your Vertical](../ecosystem-choosing-your-vertical/README.md) — is page se pehle aata hai
  (4 gates, sponsor conversation)
- [`docs/ksor/`](../ksor/README.md) — `panaversity/ksor` open-source SDK ka **standalone reference**
  (naam similar hai, lekin alag cheez: yeh chapter method/methodology hai, `docs/ksor` ek concrete
  tooling implementation ka reference)
- [Graph Engineering](../graph-engineering/README.md) — provenance/claims idea overlap karta hai

---
[⬅ The Ecosystem](../ecosystem-overview/README.md)
