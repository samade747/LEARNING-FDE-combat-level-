# Leaving the Laptop — Notes (Roman Urdu + English)

Ye notes **"Leaving the Laptop: A Runtime Crash Course"** chapter ka easy explainer hain — **General
Agents group ka aakhri chapter (position #12)**, Panaversity ke **The AI Agent Factory** book se (Zia
Tutor AI connector ke zariye).

Source: https://agentfactory.panaversity.org/docs/leaving-the-laptop-crash-course

## Index

1. [00 — Overview: Aakhri Dependency](00-overview.md)
2. [01 — Headless: Har Ghar Ka Pul](01-headless-bridge.md)
3. [02 — Managed Runtime (Home 3)](02-managed-runtime.md)
4. [03 — Move Khud (Suitcase Test)](03-the-move.md)
5. [04 — Ghar Chunna (4 Sawal)](04-choosing-a-home.md)
6. [05 — Staying Honest (Lock-in + Limits)](05-staying-honest.md)
7. [06 — Practice Projects (8 moves)](06-practice-projects.md)

## Ek Line Mein Poori Cheez

> Aapka system mukammal hai, aur **trapped** hai. Loop, harness, evals — sab kuch sahi banaya, lekin sab
> kuch **ruk jata hai** jab aap laptop band karte ho. Ye course **runtime decision** sikhati hai — agent
> **kaha rehta hai** aur **kaun isay zinda rakhta hai**, uska behavior nahi (wo 3 pichli courses ne tay
> kar diya).

## 4 Ghar (Homes)

| Ghar | Control Plane | Execution Plane |
| --- | --- | --- |
| 1. Aapki session | Aap | Aapka laptop |
| 2. Cloud schedule | Aap (scheduler ke zariye) | Cloud runner |
| 3. Managed runtime | Vendor | Vendor (ya self-hosted) |
| 4. Apna process | Aap | Aap |

Ye trilogy — [[loop-engineering]], [[harness-engineering]], [[trusting-the-checker]] — ke upar based hai.
