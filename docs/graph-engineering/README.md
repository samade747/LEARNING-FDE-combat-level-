# Graph Engineering — Notes (Roman Urdu + English)

Ye notes **"Graph Engineering: A Crash Course"** chapter ka easy explainer hain (Loop → Harness → Graph
Engineering, position #10), Panaversity ke **The AI Agent Factory** book se (Zia Tutor AI connector ke
zariye).

Source: https://agentfactory.panaversity.org/docs/graph-engineering-crash-course

## Index

1. [00 — Overview: Memory Problem](00-overview.md)
2. [01 — DAG of Work (Karpathy ka Rasta)](01-dag-of-work.md)
3. [02 — Graph of Facts (Anthropic ka Rasta)](02-graph-of-facts.md)
4. [03 — Graph Se Kaam Lena (Subgraph + Grounded Checker)](03-working-from-graph.md)
5. [04 — Graph of Loops (Governance Layer)](04-graph-of-loops.md)
6. [05 — Ek Complete Graph (Morning Triage Upgrade)](05-complete-graph-example.md)
7. [06 — Staying Grounded (Kab Nahi Banani)](06-staying-grounded.md)
8. [07 — Practice Projects (8 graph builds)](07-practice-projects.md)

## Ek Line Mein Poori Cheez

> **"The agent forgets, the graph does not."** Ek loop ki memory (`progress.md`) sirf **usi ek loop**
> ke liye kaam karti hai. Jab do loops facts share karein, ya 20 agents ek saath kaam karein, transcript
> kaam nahi karti. **Graph engineering** sikhati hai ke agents jo seekhein wo **typed, connected
> records** (nodes + edges) ki tarah likhein, taake koi bhi baad wala agent query kar sake.

## 2 (+1) Graphs

- **Commit DAG** — **kaam** yaad rakhta hai (kya try hua, kya kisi se descend hua) — [[loop-engineering]]
  ka Git history
- **Knowledge graph** — **facts** yaad rakhte hain (kya exist karta hai, kaise connected hai, kaunsa
  source proof hai)
- **Governance graph** — **loops khud** nodes ban jate hain — kaun kisay check karta hai, kaun kis ka
  target owns karta hai

Ye Loop Engineering aur Harness Engineering dono pe based hai — pehle wo do chapters parhna zaroori hai.
