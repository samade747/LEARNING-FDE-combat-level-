# Project 2 — What's My Grade, Really

**Time:** ~30-45 min · **Tool:** any free AI assistant

Koi gradebook app nahi jaanta ke tumhara teacher 2 lowest homeworks drop karta, best 8/10 quizzes
count karta, strong final weak midterm replace kar sakta. Yeh exact rules sirf ek syllabus par
exist karte — sirf **tumhari likhi brief** yeh carry kar sakti.

## Step 1 — Rehearse (apne scores handy na hon to)

```text
My homework scores: 60, 92, 88, 45, 90, 85
My quiz scores (best 8 of 10 count): 70, 95, 88, 100, 0, 91, 84, 77, 93, 80
Midterm: 72
Final: 86

My teacher's exact rules:
- Homework is 20% of the grade. Drop my two lowest homework scores,
  average the rest.
- Quizzes are 20%. Only my best 8 of 10 count (a 0 means I missed one).
- Midterm is 25%.
- Final is 35%. If my final percentage is higher than my midterm, the
  final replaces the midterm too.
```

## Step 2 — Brief

```text
Here are my scores and my teacher's exact grading rules. Write and run
code, and show me it ran, to work out my real grade right now following
every rule, and show each part's subtotal so I can check one by hand.
Then tell me what I need on the final to reach 90 percent.
```

## Step 3 — Earn Trust Backstage (known-answer test)

Khud 2 lowest homeworks drop karo (45, 60), baqi (92,88,90,85) average karo = **88.75**. Code ka
homework subtotal yehi aana chahiye.

## Step 4 — Catch

Jo number aata hai wo almost kabhi wo nahi jo tumhare zehan mein tha — real figure, plan ke sath.
"Main actually 79 par hoon, 85 nahi jo assume kiya, final mein 88 chahiye A ke liye."

## Keep the Tool

```text
Save this as a "what do I need on the final" script. Run it again every
time a grade posts.
```

## Done

- [ ] Code ka homework subtotal 88.75 (ya apna-check-kiya category) match karta
- [ ] Real grade mil gaya jo pehle nahi pata tha, plus final ke liye exact score chahiye
