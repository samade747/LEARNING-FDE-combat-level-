# Project 2 — Diagnose a Real Failure

**Time:** ~15 min · **Tool:** any free AI assistant

Koi real output socho jo recently disappoint kiya. Hypothetical nahi, real wala use karo.

## Steps

1. **Kya hua:** kya mangi thi, kya mili, aur sabse zaroori — **kab** galat hui: pehli response se
   galat thi, lambi session mein degrade hui, ek repeatable error-type hai, ya pehle kaam karti
   thi ab nahi?
2. **Diagnosis:** 4 causes (under-specification/context overload/wrong feature-or-model/stale
   configuration) mein se kaunsa, aur timing mein kya usay batata (baqi 3 nahi)?
3. **Fix:** us specific cause ke liye specific fix. "Better prompt likho" jawab ho, to check karo
   kya under-specification hi actually diagnosis thi.

## Jo Yeh Catch Karta Hai

- Diagnosis timing se follow karta hai, ya timing jo support nahi karti wo cause choose kiya?
  (Jaise: fresh-chat-pehli-response-galat ke liye context-overload diagnose karna.)
- "Task fit nahi karta" ya "behtar model switch karo" par jump kiya bina cheaper causes rule-out
  kiye? Yeh exercise exactly isi jump ko catch karne ke liye bani hai.

## Done

- [ ] Diagnosis timing se match karta
- [ ] Cheaper causes (prompt/context/feature) rule-out kiye gaye diagnosis se pehle
- [ ] Fix diagnosed cause ke mutabiq hai, generic "better prompt" nahi
