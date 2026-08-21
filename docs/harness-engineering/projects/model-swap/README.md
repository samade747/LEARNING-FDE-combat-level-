# Harness Project 8 — The Model Swap (Capstone)

**Concept:** 12 (coupling), sab 5 verbs · **Time:** 2-3 hrs, phir teen raatein · **Difficulty:**
Capstone

Apni hardened loop (Project 7 ka fenced version behtar hai, kyunki poori tarah harnessed hai) ko
teen raaton tak **alag model** par chalao (jaise Claude ki jagah kisi doosre tool/model se, ya Claude
Code ke andar hi `/model` switch kar ke). `HARNESS.md` mein log karo.

## Steps

1. Baseline: apni loop ek raat purane/regular model pe chalao, note karo kitni clean chali.
2. 3 raatein: alag model pe chalao. Jo bhi tootay ya shift ho (token budgets, wordiness, prompt
   habits jo purani model bardasht karti thi) `HARNESS.md` mein log karo.
3. Har failure ko fix karo — lekin **prompt tweak se nahi**, balke contract se: exit codes, JSON
   schema validation (Project 5 ka `typed-reviewer` yahan reuse ho sakta hai), automated tests.
4. Confirm karo loop **dono** models pe clean chalti hai ab.

## Done jab (self-check)

- [ ] Har failure behavior-coupling se contract-coupling mein move hui
- [ ] Loop dono models pe clean chali — yehi proof hai harness **aapki** hai, kisi ek model ki nahi

---
[⬆ Harness Practice Log](../../11-practice-log.md) · [Poori list](../../07-practice-projects.md)
