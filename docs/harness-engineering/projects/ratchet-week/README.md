# Harness Project 6 — The Ratchet Week

**Concept:** 10 (failure classes, ratchet) · **Time:** 1 hafta, ~15 min/din · **Difficulty:** Medium

Koi naya scaffold nahi — **kisi bhi apni existing loop** (jaise
[`daily-triage-demo`](../../../loop-engineering/projects/daily-triage-demo/) ya
[`fix-loop-demo`](../../../loop-engineering/projects/fix-loop-demo/)) ko roz chalao, aur har mistake ko
`HARNESS.md` mein log karo — 4 failure classes mein classify kar ke.

## Steps

1. `HARNESS.md` (isi folder mein) ko apni loop-wali repo mein copy karo.
2. 7 din, roz kam se kam ek beat chalao. Jo bhi galti dikhe, usi din ki table mein ek row daalo:
   mistake, class (1-4), fix.
3. Har fix ko **surface** par likho — deny rule mein? doc/skill instruction mein? hook mein?
   escalation path mein? (Concept 10 ki language mein: constraint / information / verification /
   recovery)
4. Hafta khatam hone par "Week Verdict" section fill karo.

## Done jab (self-check)

- [ ] 7 din ka per-class count mil gaya, pata hai harness kahan sab se patli thi
- [ ] Same-shape 2 failures pehli ke baad namumkin ho gayin (fix genuinely stuck)

---
[⬆ Harness Practice Log](../../11-practice-log.md) · [Poori list](../../07-practice-projects.md)
