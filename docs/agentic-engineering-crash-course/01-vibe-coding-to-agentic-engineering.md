# 01 — Vibe Coding Se Agentic Engineering Tak

## 1.1 Software 3.0: A New Computing Paradigm

Karpathy software ko **3 eras** mein describe karta hai: **1.0** = explicit code (CPU execute karta
hai). **2.0** = learned weights (dataset curate karo, neural network train karo). **3.0** = ab ka
daur — **prompting se programming**, LLM ek programmable computer hai, context window hi lever hai.

Era badalne se **artifact** badalta hai jo tum produce karte ho. 3.0 mein artifact increasingly **ek
text hai jo agent ke liye bana hai.** OpenCode apna installer bash script ki tarah ship nahi karta —
natural-language paragraph ship karta hai jo coding agent mein paste hota hai. Installer ab program
nahi, **ek Skill hai.** Yeh generalize hota hai: human docs agent docs ban jati hain, UI sirf
interface nahi rehti — **agent har system ka second-class user ban jata hai.** **Agent-native
infrastructure** (APIs/docs/tooling/deployment agent-first design ki) agla platform layer hai.

## 1.2 Vibe Coding Floor Raise Karti Hai; Agentic Engineering Ceiling Preserve Karti Hai

**Vibe coding** = agent ko code likhne do, output bina diff parhe accept karo, judge karo "chalta hai
ya nahi" se. Real, useful, aur yahin rehne wala hai — ek non-programmer ek weekend mein useful tool
ship kar sakta hai. Vibe coding **floor raise karti hai** jo ek individual bana sakta hai.

Ek doosra discipline is par **banta hai**: **agentic engineering** — jahan vibe coding floor raise
karti hai, yeh **ceiling preserve karti hai** (professional software ka quality bar). Agent zyada tar
typing karta hai; tum security/data-integrity/maintainability/UX ke zimmedar rehte ho. **Vibe coding
vulnerabilities introduce nahi karti — careless engineer karta hai.**

| | Vibe coding | Agentic engineering |
| --- | --- | --- |
| **Goal** | Floor raise karna | Ceiling preserve karna |
| **Reviewer** | Often koi nahi — "chalta hai" se judge | Insaan diff parhta hai + automated review |
| **Architecture** | Jo agent de de | Engineer design karta, agent implement karta |
| **Tests** | Optional | Non-negotiable, critical-path par TDD |
| **Codebase health** | Drift accept hota hai | Schedule par refactor, modules deepen hote hain |
| **Right setting** | Side projects, prototypes | Production, regulated work, multi-user kuch bhi |

Jab tum **Digital FTE** banate ho jo organization payroll/customer-escalations/financial-reconciliation
mein trust karegi, **vibe coding malpractice hai.** Floor **aur** ceiling dono chahiye — raised
throughput aur preserved quality.

> Karpathy: *"10× speed-up jo tum gain karte ho wo nahi hai. Jo log is mein genuinely acche hain,
> abhi 10× se bohot zyada peak karte hain."* Yehi gap is chapter ka kaam hai.

---
[⬅ Overview](00-overview.md) · [Agla: Three Constraints ➡](02-three-constraints.md)
