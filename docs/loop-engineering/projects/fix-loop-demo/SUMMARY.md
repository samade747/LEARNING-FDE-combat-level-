# Summary — Project 4: A Fix Loop With a Real Checker

**Concept:** 8 (worktree), 9 (skill), 11 (maker-checker)
**Source:** Book ka spec + shape 100% follow karta hai, lekin **koi official starter kit nahi** —
bug aur code maine khud banaya.

## Kya Sikhata Hai

**Maker-checker split** — jo agent kaam banata hai, wahi khud grade nahi karta. Poore course ka
**sabse important choice.**

## Kyun Zaroori Hai

Ek model jo apna khud kaam check kare, usay bohat asaani se approve kar deta hai. Ek dusra agent
(alag instructions, kabhi alag model) woh galtiyan pakarta hai jo pehle ne miss ki. Isi separation se
ek unattended loop safe banti hai.

## Kaise Kaam Karta Hai

`discount.py` mein ek real bug hai (discount `÷1000` se calculate hota hai, `÷100` hona chahiye).
Implementer bug dhoondta hai (`pytest` chala kar), alag branch/worktree mein fix draft karta hai,
phir **reviewer subagent** ko bhejta hai — jo khud tests chala kar PASS/FAIL deta hai. Sirf PASS pe
kaam "ready" mana jata hai.

**Done jab 2 cheezein sach hon:** achi fix → PASS. Jaan-boojh kar buri fix (jaise hard-coded expected
values) → **FAIL + reasons**. Agar reviewer buri fix bhi pass kar de, checker naram hai.

## Maine Kya Test Kiya

`python -m pytest test_discount.py -v` khud chalaya — bug se **2/3 tests fail** hote hain confirmed
(`test_twenty_percent_off` aur `test_multiple_prices`), 1 pass hota hai (`test_no_discount_is_a_no_op`
— jahan 0% discount hai, ÷1000 vs ÷100 ka farq zero output deta hai). Checker sahi kaam kar raha hai.

## Isi Par Project 5 Build Hoti Hai

[`../CODIFY-AND-SABOTAGE.md`](../CODIFY-AND-SABOTAGE.md) mein poori tarah likha hai — isi cycle ko
ek re-runnable "workflow" mein badalna.

---
[⬆ Poori Project List](../../README.md#runnable-projects-poore-12-har-ek-ki-real-jagah)
