# Project 3 — The Books Don't Match

**Time:** ~45 min · **Tool:** any free AI assistant

Bookkeeper ka problem jo course khola, chhoti scale par. Class trip/club/group gift ke liye paisa
collect kiya — **count** kiya kitna aaya, yeh tumhara known answer hai, koi app yeh nahi de sakta
kyunke koi app room mein nahi tha.

## Step 1 — Rehearse (apna collection na ho to)

```text
Everyone owes 500 for the class trip. Eight people: Ali, Omar, Sara,
Bilal, Hina, Zoya, Ayesha, Usman. So the books should show 4,000.

Digital record (JazzCash), exactly as it came in, messy memos and all:
Date,From,Amount,Memo
2025-09-02,Ali,1000,trip me + my brother Omar
2025-09-02,Sara,500,trip dues
2025-09-03,Bilal,500,
2025-09-03,Hina,500,class trip
2025-09-05,0300-unknown,500,
2025-09-05,Usman,300,pizza
2025-09-06,Zoya,500,dues
2025-09-08,Ayesha,500,trip

What only I know (the rules):
- Ali's 1,000 covers Ali AND his brother Omar. Count it for both.
- Usman's 300 with "pizza" is NOT dues; he was paying me back. Ignore it.
- The 500 from "0300-unknown" has no name I recognize. Do not assume; flag it.
```

## Step 2 — Brief

```text
Here's what everyone owes, the messy payment record, and the rules only
I know. Write and run code, and show me it ran, to reconcile them:
who's paid, who still owes, and how much is unaccounted for. List any
payment you can't match to a person, and don't guess. My counted total
is [your number]. Show me how the code's total compares with mine.
```

## Step 3 — Earn Trust Backstage (known-answer test)

Tumhara counted figure (4,000 sample mein) is job ka known answer hai — code ka expected total
yehi aana chahiye, catch dekhne se pehle.

## Step 4 — Catch

Sample: books 500 short. 7 log covered (Ali+Omar 1,000 se, +Sara/Bilal/Hina/Zoya/Ayesha). Usman ka
sirf payment pizza thi — abhi bhi owes. Ek mystery 500 jo place nahi ho sakta. **Ek sentence group
chat ke liye:** "Sab accounted hain Usman ke siwa, aur ek mystery 500 hai, Usman ko message karunga."

## Keep the Tool

```text
Save it as my reconciliation script. Next trip/gift/collection — naya
record + dues list paste karo.
```

## Done

- [ ] Code ka total tumhare counted number se match karta
- [ ] Ek specific naam chase karne ko mila, ya ek specific payment place karne ko
