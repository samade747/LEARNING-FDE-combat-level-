# Summary — Project 8: Your Own Daily Loop (Capstone)

**Concept:** Sab 6 Parts (heartbeat, worktree, skill, maker-checker, connector, spine)
**Source:** Book ka spec + shape 100% follow karta hai, lekin **koi official starter kit nahi** —
bug, issues, aur code maine khud banaya.

## Kya Sikhata Hai

Poori book ka sab kuch **ek sath** — yehi capstone hai.

## Kyun Zaroori Hai

Har pichli project ek part sikhati hai. Capstone prove karta hai ke aap sab parts ko ek working system
mein jor sakte ho: heartbeat kaam start karta hai, spine yaad rakhti hai, worktree isolation deta hai,
maker-checker safety deta hai, aur **human gate** sabse zaroori decision ko insaan tak bhejta hai.

## Kaise Kaam Karta Hai

`greeter.py` mein ek real bug hai (off-by-one, last name list se gayab ho jata hai). `ISSUES.md` mein
2 candidates: #1 safe fix (yehi bug), #2 **jaan-boojh kar risky** (public-facing string format change).
Loop `progress.md` parhti hai, dono issues dekhti hai, #1 ko fix karke reviewer se PASS leti hai, aur
#2 ko **kabhi khud nahi chhedti** — usay "Open / needs a human" mein likh deti hai.

**Asal lesson:** yeh Human Gate ka poora demo hai. Safe kaam khud ho jata hai; risky kaam insaan tak
jata hai — chahe tests bhi pass ho jayein, reviewer.md issue #2 ko **hamesha** reject karega.

## Maine Kya Test Kiya

`python -m pytest tests/ -v` khud chalaya — bug se **2/3 tests fail** hote hain confirmed
(`test_greet_all_includes_the_last_name`, `test_greet_all_single_name`). `progress.md` ka khaali
template ready hai (Done/In progress/Open sections).

## Real Duniya Mein Wire Karna

[`README.md`](README.md) mein agle steps hain: `ISSUES.md` ki jagah real GitHub issues use karo, aur
isay Routine/cron heartbeat do ([`../07-routines-appendix.md`](../07-routines-appendix.md)).

---
[⬆ Poori Project List](../../README.md#runnable-projects-poore-12-har-ek-ki-real-jagah)
