# Project 1 — Money Detective

**Time:** ~45 min · **Tool:** any free AI assistant

"Paisa gayab ho jata hai, pata nahi kahan" — budgeting app yeh **aage** ke liye answer karta hai.
Yeh opposite move hai: **peeche** apni real history mein wo leak hunt karna jo sirf tum pehchan
sakte ho.

## Step 1 — Rehearse (apna export na ho to)

Yeh sample wallet paste karo (student ki wallet, kuch mahine, `+` = paisa aaya, `-` = gaya):

```text
Date,What,Amount
2025-06-01,Pocket money,+5000
2025-06-04,PrimeVideo subscription,-199
2025-06-05,Spotify,-299
2025-06-07,Foodpanda,-650
2025-06-09,Careem ride,-300
2025-06-15,Tutoring received,+1500
2025-06-18,Foodpanda,-700
2025-06-28,Bank service fee,-50
2025-07-01,Pocket money,+5000
2025-07-04,PrimeVideo subscription,-199
2025-07-05,Spotify,-299
2025-07-08,Foodpanda,-650
2025-07-08,Foodpanda,-650
2025-07-14,Careem ride,-300
2025-07-28,Bank service fee,-50
2025-08-01,Pocket money,+5000
2025-08-04,PrimeVideo subscription,-199
2025-08-05,Spotify,-299
2025-08-10,Foodpanda,-700
2025-08-16,Careem ride,-350
2025-08-20,Tutoring received,+1500
2025-08-28,Bank service fee,-50
2025-09-01,Pocket money,+5000
2025-09-04,PrimeVideo subscription,-199
2025-09-05,Spotify,-299
2025-09-12,Foodpanda,-700
2025-09-17,Careem ride,-300
2025-09-28,Bank service fee,-50
```

## Step 2 — Brief

```text
Here's a few months of my wallet (a plus is money in, a minus is money
out). Money keeps disappearing and I can't see where. Be my money
detective: write and run code, and show me it ran, to find where it
actually goes, anything that keeps charging me every month, and any
charge billed twice on the same day. Then tell me what I'll have left
by my next pocket money.
```

## Step 3 — Earn Trust Backstage (known-answer test)

Khud check karo: total money in = **23,000** (4x 5,000 pocket money + 2x 1,500 tutoring).
PrimeVideo har mahine appear hona chahiye, **796** so far (199×4). Code yeh reproduce kare to
baqi par trust karo.

## Step 4 — Plain-English Replay

```text
Now explain it like I can't read code. Which language did you use, and
how did you actually get these numbers, especially how you decided
something was a duplicate?
```

## Step 5 — Catch

Sample par milta: PrimeVideo subscription (796 so far, bhool gaye the), Foodpanda 2x same-day
charge (8 July — dispute kar sakte ho), real leak: food delivery ~4,050 (sab subscriptions se
zyada).

**Ek sentence jo real insaan ko bolna hai:** "AI ne ek subscription dhoondi jo mai bhool gaya tha,
796 gaye so far, plus ek double charge jo dispute kar sakta hoon."

## Step 6 — Apna Real Data Chalao

Same brief apne bank export par chalao. Higher stakes ho (refund chase karna) to [cross-model
check](../troubleshooting.md) karo — dusri AI mein same brief chalao, numbers compare karo.

## Keep the Tool

```text
Save this as a script with a plain-English header, named "my monthly
money check". Next month I'll paste a fresh export and say "run this".
```

## Done

- [ ] Code ne 23,000 (total in) aur 796 (PrimeVideo) reproduce kiya
- [ ] Kam az kam 1 true cheez catch ki jo pehle nahi pata thi aur act kar sakte ho
- [ ] Script save ki jo next month rerun ho sakti
