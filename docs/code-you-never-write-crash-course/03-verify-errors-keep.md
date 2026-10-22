# 03 — Part 2: Verify, Errors, Keep the Script (Concepts 6-8)

## Concept 6 — Verifying Work You Cannot Read

Model ke pas apna truth-checker nahi hai (What AI Actually Is, Idea 3). Code ke sath tumhare pass
ek checker hai jo AI ke pass nahi — **tum isay run kar sakte ho.**

Skeptic ka sawal theek hai: _"Agar code parh nahi sakte, correct kaise jaano?"_ Jawab computers se
purana hai: **jis expert ka craft follow nahi kar sakte, uska result check karo.** Accountant ko
check karne ke liye tax law dobara nahi karte — records ke against totals check karte ho.

5 checks, rising effort mein. Pehli 3 zyadatar situations cover karti hain.

**Known-answer test (sabse powerful move):** chhota part jiska answer pehle se pata hai, uspar
code chalao. Mahina close kar chuke ho, uspar script chalao — har answer reproduce ho to confidence
_earned_ hai, hoped-for nahi.

**Reality questions:** jo pehle se pata hai usse output ko pucho. Rows in vs rows out match karte?
"Biggest customer" wo hai jo tum jaante ho? Contradict kare to next prompt: _"Yeh number kaise
compute hua, plain English mein, 3 rows dikhao jo isko support karti hain."_

**Plain-English replay:** AI ka apna account, plain words mein, uske code ne kya kiya. Python parh
nahi sakte, par "maine amount+date 2-din tolerance se match kiya, debits negative treat kiye, 14
rows skip ki" — procedure check kar sakte ho. **Zyadatar real errors procedure errors hote hain,
typing errors nahi** — isliye yeh kaam karta hai.

**Adversarial pass:** AI se apne kaam par attack karwao. _"Yeh analysis kaise galat/misleading ho
sakta hai? Konsa assumption liya? Weakest link kya hai? Har claim ko 1-10 confidence do."_

**Cross-model check:** same brief+data doosri AI (alag company) mein chalao, numbers compare karo.
High-stakes results ke liye. Limit: dono brief parhte hain, ek chhoti rule dono bhool sakte hain.

| Stakes | Minimum verification |
|---|---|
| Personal curiosity | Reality questions |
| Colleague relies on | Known-answer test + plain-English replay |
| Money/grades/health/signed | Sab paanch, human review |

**Pharmacist example:** usne data mein ek fake 10-unit gap plant ki. Script ne wo fake gap pakda
_plus_ 4 real gaps jo usay nahi pata the. Fake catch karne se 4 real par trust bana.

> **Jo kabhi skip nahi karna:** Precision-critical number par act mat karo jise independently
> jaane answer ke against test nahi kiya. **Known-answer test tumhara firewall hai.**

## Concept 7 — Jab Yeh Break Ho: Errors Dialogue Hain, Failure Nahi

Kuch galat hoga. Script stop hogi, red text aayega — ya worse, finish hoke strange dikhega.
**Error project ka fail hona nahi hai — computer bata raha hai bohot precisely usay kya chahiye.**

Red-text errors ki poori skill:

```text
It stopped and showed this error. Diagnose it, fix the code, and
run it again:
[paste the red text, all of it]
```

Tum error interpret nahi karte — **forward karte ho.** AI mechanic ki tarah apna error parhta,
fix karta, chalata hai. Zyadatar errors pehle paste par mar jate hain.

Harder case: **wrong-but-running** (red text nahi, par number galat lagta). "Yeh galat hai, fix
karo" mat bolo — AI ko pata nahi kaunsa part. Symptom report karo doctor ki tarah:

```text
The output shows total sales of 4.2 million, but I know this year
was around 12 million. Investigate: show me the row count you
processed, the date range you found, and the first 5 rows.
```

Specific symptom + expected value + inspect-before-fix request. 9/10 times cause foran dikhta —
Excel ki 3-sheets mein se sirf 1 parhi, ya "1,200" comma ki wajah se text treat hua.

| Symptom | Prompt |
|---|---|
| Red text, stopped | Full error paste karo + "diagnose, fix, rerun" |
| Runs, number contradicts | Symptom + expected value state karo, row counts/sample pehle maango |
| Same fix 3 baar fail | Stop digging — "3 baar try kiya, step back, 2 alag approaches propose karo" |

**Marketer example:** "codec" error, ek word samjhe bina paste kiya — AI ne 40 second mein fix kar
diya. **Errors parhna zaroori nahi — paste karne ki willingness zaroori hai.**

## Concept 8 — Script Keep Karo: Solved Problem Ek Button Ban Jata Hai

Repetition signal ka payoff dusre teen nahi de sakte. **Ek baar likha script forever ka asset
hai.** Teacher ka brief pehli baar effort leta — next assignment par "mera submission-check script
is naye class list par chalao."

3 parts ka habit:

1. **Script ko file ki tarah maango:** _"Isay script file ki tarah save karo, saaf naam ke sath,
   top par plain-English description — yeh kya karta, kaunsi files expect karta, kaunse rules
   follow karta."_
2. **Brief ko script ke sath rakho:** script = how (machines ke liye), brief = what+why (humans +
   future AI sessions ke liye). 6 mahine baad "late-cutoff rule change hui, update karo" bol sako.
   (Pichle course ka **Intent Layer**.)
3. **Dono ko ek folder mein ghar do:** `my-scripts/essay-submissions/` mein brief.md + script +
   sample input — yeh sample tomorrow ka known-answer test hai.

| Bina keep-the-script habit | Isके sath |
|---|---|
| Har mahine memory se re-explain | "Script chalao naye files par" |
| Rule drift (May vs June ka logic alag) | Rules script mein frozen, identical logic har run |
| Sirf tumhari skill help karti | Folder colleague ko do — minutes mein productive |

**Clinic manager example:** March mein no-show script banaya, kept it. August tak "no-show script
is month ke export par chalao" 30-second Friday habit ban gaya. Naya branch khula, manager ko
folder handover kiya — day 1 par bina sawal chala. _Describe once, run forever, hand to anyone._
