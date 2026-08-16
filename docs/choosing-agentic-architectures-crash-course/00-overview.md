# 00 — Overview: Yeh Course Kis Baare Mein Hai

*Anchor article: Bala Priya C, "Choosing the Right Agentic Design Pattern: A Decision-Tree Approach,"
Machine Learning Mastery, May 15, 2026. Is course ki decision tree unki hai; yeh course composition
layer add karta hai — har pattern ka aapki deployment topology aur eval suite ke liye kya matlab hai.*

## Plain-English Version (Pehle Yeh Parho)

Aap ne agents banaye hain — Digital FTE course ka Maya ka customer-support Worker, eval-driven course
ka evaluation agent, ya cloud deployment course mein production tak le gaye Tier-1 Support agent. Aap
**ek** agent bana sakte ho. Jo aap principled tarike se nahi kar sakte woh yeh decide karna hai ke
**agli baar kis type ka agent banana hai.**

**Real production failure mode:** engineers usi pattern ki taraf jate hain jo impressive lagta hai —
usually multi-agent — jab task ek sequential workflow maangta hai jise apne 5 steps mein se 3 mein LLM
ki bhi zaroorat nahi. Yeh hafton ka orchestration kaam hai us problem ke liye jo ek well-prompted single
agent 2 tools ke sath ek din mein handle kar leta. **Ulta failure bhi utna hi real hai:** ek lambe
system prompt wale single agent ki taraf jana jab task genuinely specialists mein decomposition
maangta hai, aur agent ko context ke neeche collapse hote dekhna jo ek mental model mein fit nahi hota.

**Yeh course woh design work sikhata hai jo build se pehle ati hai:** agent system ki asal shape kya
honi chahiye. Iska ek principled jawab hai. Apne task ke baare mein 5 sawal pucho, aur jawab ek starting
pattern par map hote hain.

**Discipline "hamesha simplest pattern chuno" nahi hai. Yeh hai: woh simplest pattern chuno jo task
asal mein maangta hai, aur complexity sirf tab add karo jab aap specific task property naam le sako jo
usay demand kare.** Multi-agent sahi jawab hai jab specialization ya scale ek real bottleneck banaye,
na ke jab woh slide par advanced lage.

## 4 Claims Jo Yeh Course Defend Karta Hai

1. **Pattern selection architectural fit hai, capability matching nahi.** Sahi pattern woh hai jiske
   assumptions task ki asal properties se match karein, sabse zyada capability wala nahi
2. **Task ke baare mein 5 sawal architecture decide karte hain**, aur jawab deterministically ek
   starting point par map karte hain
3. **Pattern selection deployment topology aur eval signals ke sath compose hoti hai** — har pattern
   cloud stack ka alag subset use karta hai, apne characteristic failure modes rakhta hai
4. **Decision tree ek starting point hai, final answer nahi** — real systems evolve karte hain

> **Minimum viable path:** Part 1 (problem), Part 2 (decision tree), aur Decision 1 (Maya ka Tier-1
> Support) parho — ~90 minutes, uske baad naya task classify kar sakte ho.

## 4 Learning Tracks

| Track | Waqt | Kya Complete Hota Hai |
| --- | --- | --- |
| **Reader** | ~2-3 ghante | Poora conceptual arc: Problem, Decision Tree, 5 Patterns, Failure Signals, Closing |
| **Beginner** | ~1 din | Reader + Decisions 1-2 (Maya's Tier-1 Support + incident-response agent classify karo) |
| **Intermediate** | ~2-3 din | Beginner + Decisions 3-4 (research agent + enterprise onboarding agent; deployment topology sketch karo) |
| **Advanced** | ~4-5 din | Intermediate + Decision 5 + Parts 6-7 (coding agent — hardest case; pattern composition) |

## 22 Concepts, 5 Decisions — Poori Decision Tree Ek Nazar Mein

**5 sawal jo pattern chunte hain:**
1. **Solution path pehle se define ho sakta hai?** YES → Q2. NO → Q3
2. **Workflow fixed aur stable hai runs ke across?** YES → **Sequential Workflow**
3. **Task structure execution se pehle articulate ho sakti hai?** YES → **Planning + ReAct Execution**.
   NO → **Single Agent + ReAct + Tools**
4. **(Additive layer)** Quality speed se zyada matter karti hai, checkable criteria ke sath? YES →
   **Reflection Layer** upar add karo
5. **(Additive layer)** Specialization, context, ya scale bottleneck hai? YES → **Multi-Agent
   Specialist System** upar add karo

**Yaad rakho:** Q1-Q3 core pattern chunte hain (4 mein se 1). Q4-Q5 additive layers hain jo kisi bhi
core par wrap ho sakti hain — Reflection 5wan peer pattern nahi hai.

---
[⬆ Index](README.md) · [Agla: Pattern Selection Problem ➡](01-pattern-selection-problem.md)
