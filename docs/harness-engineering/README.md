# Harness Engineering — Notes (Roman Urdu + English)

Ye notes **"Harness Engineering: A Crash Course"** chapter ka easy explainer hain (Loop Engineering ke
turant baad, position #9), Panaversity ke **The AI Agent Factory** book se (Zia Tutor AI connector ke
zariye).

Source: https://agentfactory.panaversity.org/docs/harness-engineering-crash-course

## Index

1. [00 — Overview: Harness Kya Hai](00-overview.md)
2. [01 — Constrain: Agent Ko Rokna](01-constrain.md)
3. [02 — Inform: Agent Ko Batana](02-inform.md)
4. [03 — Verify & Correct: Check Karna Aur Theek Karna](03-verify-correct.md)
5. [04 — Ek Complete Harness (Hardened Morning Triage)](04-complete-harness-example.md)
6. [05 — Staying the Engineer: Insaan Ka Kaam Khatam Nahi Hota](05-staying-the-engineer.md)
7. [06 — Dogfooding: Yeh Kitaab Khud Apni Harness Kaise Use Karti Hai](06-dogfooding.md)
8. [07 — Practice Projects (8 harness builds)](07-practice-projects.md)
9. [08 — Appendix: Hook Pipeline End-to-End (field guide, 3 drills)](08-appendix-hook-pipeline.md)
10. [09 — Sources & Further Reading](09-sources-further-reading.md)
11. [10 — Test Your Understanding (18-question exam assessment)](10-test-your-understanding.md)

## Ek Line Mein Poori Cheez

> **Agent = Model + Harness.** Model intelligence deta hai. Harness us intelligence ko **reliable**
> banata hai — kya allowed hai, agent ko kya pata hai, kaam kaise prove hota hai, aur jab kuch ghalat ho
> to kya hota hai. **Loop Engineering** ne bara cycle sikhaya tha (kab chalta hai, kaise yaad rakhta
> hai). **Harness Engineering** us cycle ke **ek beat ke andar** ka box khol ke dikhata hai.

## Loop Engineering Se Farq (Zaroori)

- **Loop** = kab chalta hai, kya yaad rakhta hai (heartbeat, spine) — [[loop-engineering]]
- **Harness** = **ek beat ke andar** kya allowed hai, agent ko kya pata hai, kaam kaise prove hota hai
  (constrain, inform, verify, correct, escalate)

Ye do alag layers hain aur alag tarah se fail hoti hain: **ek missing deny rule** aur **ek missing
heartbeat** do bilkul alag bugs hain.
