# 02 — Rules Aur Instructions

## Concept 7: Global, Folder, Aur Session Instructions

**3 layers, kitni door tak apply hoti hain:**
- **Global instructions** — har session pe apply — role, default tone, output formats
- **Folder/project instructions** — jab wo folder scope mein ho — client terminology, matter structure
- **Session prompts** — abhi wale task ka goal

**Sab se common ghalti:** sab kuch global mein daalna — 3,000-token system prompt jo har turn cost
karta hai aur galat rules se agent confuse karta hai.

> **Sahi model:** **global sparse ho, folder specific ho, session goal ho.**

```text
Global:
I'm a marketing analyst at a mid-size SaaS company. I write in
concise, direct prose. Default to markdown for documents.

Folder (Q1-campaign-analysis/):
This folder contains weekly campaign reports from Jan-Mar 2026.
Conversions in column G, spend in column H.

Session prompt:
Compare conversion rates across the 12 reports. Identify the top
3 weeks and what they had in common. One-page summary.
```

Global mein **nahi** hai: matter-specific naming, is filing ki citation form, folder layout — wo
matter ke sath rehte hain.

## Concept 8: "Execute Karne Se Pehle Sawal Poocho" Pattern

Anthropic ke apne best-practices se: task state karne aur ummeed karne ki bajaye, **"start karne se
pehle 1-2 clarifying questions poocho"** kaho.

Non-trivial tasks ke liye, ye unstated assumptions surface karta hai jo warna bugs ban jate: *"Kya
cancelled subscriptions count mein shamil karoon?"* — 2 sawal, 90 second, kaafi behtar deliverable.

**Multi-source tasks ke liye ek aur instruction:** *"agar sources ek dusre se contradict karein, flag
karo; chup chaap ek mat chuno."* Bina explicit instruction ke, model conflicts ko **smooth** kar deta
hai, confident-sounding output deta hai jo ek jawab chun leta hai. **Lawyer/auditor ke liye, yehi wo
failure mode hai jo malpractice banata hai.**

```text
If any sources contradict each other on a material point, flag
the contradiction explicitly in the deliverable; do not silently
pick one.
```

---
[⬅ Context, Sessions, Projects](01-context-sessions.md) · [Agla: Extending the Tool ➡](03-extending-tool.md)
