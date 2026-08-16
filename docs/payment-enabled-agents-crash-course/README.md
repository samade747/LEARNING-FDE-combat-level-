# Payment-Enabled Agents

*Source: The AI Agent Factory — "Payment-Enabled Agents: ACP, AP2, x402, and MPP in Production" (Panaversity)*
*URL: https://agentfactory.panaversity.org/docs/payment-enabled-agents-crash-course*
*Group: Mode 2 — Manufacturing, Phase 3 · Scale the Workforce (Chapter 9 of 9 — Aakhri Chapter)*

---

## Yeh Course Kis Baare Mein Hai

Yeh course un 4 protocols par hai jo OpenAI Agents SDK systems ko paisa spend karne dete hain:
merchants par, APIs ke against, doosre agents ke sath, poori open economy mein. **Poora course jispar
khara hai:** **4 protocols rivals nahi hain. Layers hain.** Real system 2026 mein ek sath kai use karti
hai, kyunki har ek same problem ki alag layer solve karta hai. **Aapka kaam use case parhna hai aur har
layer par sahi protocol stack karna hai.** 19 concepts, 5 worked decisions, 4 learning tracks.

## Parts

1. [Overview: 4 Protocols, 4 Layers](00-overview.md)
2. [Part 1 — Agent Commerce Ko Naye Protocols Kyun Chahiye (Concepts 1-3)](01-why-new-protocols.md)
3. [Part 2 — The Four Layers In Depth (Concepts 4-7)](02-four-layers.md)
4. [Part 3 — The Four Protocols In Depth (Concepts 8-11)](03-four-protocols.md)
5. [Part 4 — Composition Rules (Concepts 12-14)](04-composition-rules.md)
6. [Part 5 — The Decision Lab (5 Worked Examples)](05-decision-lab.md)
7. [Part 6 — Production Concerns (Concepts 15-18)](06-production-concerns.md)
8. [Part 7 — Closing (Concept 19) + Cheat Sheet + References](07-closing.md)

---

## 4 Layers, Ek Nazar Mein

```
Layer 1: DISCOVERY      → "Kya khareedne ke liye available hai?"      (MCP, A2A, directories)
Layer 2: AUTHORIZATION  → "Kya main yeh spend karne ka allowed hoon?" (AP2, ACP SPT, TAP, ERC-8004)
Layer 3: COMMERCE       → "Poori purchase lifecycle kya hai?"         (ACP, UCP, ya none)
Layer 4: SETTLEMENT     → "Paisa asal mein kahan move hota hai?"      (x402, MPP, card rails)
```

**Discipline ek sentence mein:** use case parho, usay 4 layers mein tor do, har layer par sahi protocol
chuno. Ek layer ke andar, ek protocol chuno. Layers ke across, kai compose karo.

---

*Yeh AI Agent Factory book ke Mode 2 — Manufacturing group ka aakhri chapter hai. Isi ke sath poora
Mode 2 (18/18 chapters) aur poori "yes Mode 2 bhi kar do" instruction complete hoti hai.*

*Yeh summary poore course (Naye Protocols Kyun + 4 Layers + 4 Protocols + Composition + Decision Lab +
Production Concerns + Closing) ka overview hai.*
