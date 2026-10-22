# 02 — Part 2: Hands Move Karna + Brief the Problem (Concepts 4-5)

## Concept 4 — Automatic vs. Explicit: AI Ke Hath Move Karna

Modern AI tools decide karte hain prompt ki sound se ke code likhna hai ya nahi. Spreadsheet
upload karke "kaunsa product fastest grow kiya" poochoge, zyadatar compute karenge. Par jo
glance-se-answerable lage, AI code skip kar ke **estimate** kar sakta — estimate exactly
computation jaisa dikhta, same confident tone, same tidy numbers. **Failure silent hai** — screen
par kuch nahi batata kaunsa mila.

**Ek habit yeh hata deti hai: Precision signal fire karne wali kisi bhi cheez par decision AI par
mat chhodo.** Words bolo.

Teen lines, desk ke upar pin karne layak:

```text
Write and run code to answer this.
Show me the code you ran.
Before analyzing anything, tell me the exact row count, the column
names, and the date range of the file.
```

Line 1 computation force karti. Line 2 proof deti — code block na aaye to code nahi chala, jo bhi
words claim karein. Line 3 sabse cheap lie detector hai — AI real mein file parh raha hai to row
count/column names exactly right honge; bana raha hai to round number aur sahi-lagne-wale-ghalat
column names milenge.

**Note: lines "code" bolti hain, "Python" nahi.** AI ko tell karo compute karo — kaunsi language
mein kabhi mat bolo. "In Python" add karna AI ka hath ek guess par force karta hai jo tum equipped
nahi ho karne ke liye.

| Tumhari phrasing | Usually kya hota | Risk |
|---|---|---|
| "What does this data show?" | Glance-based summary, shayad code | Estimates facts ki tarah dressed |
| "Roughly costs kaise trend hue?" | Almost hamesha glance | Fine _sirf_ agar tumhe truly care nahi |
| "Write and run code to compute..." | Code, har baar | Minimal |
| "Running code ya estimating ho?" | AI method naam karta, phir compute karta | Best move jab glance ka shaq ho |

**Opposite bhi matter karta hai: answer problems ke liye code demand mat karo** — "write and run
code to tell me if my essay is persuasive" tool waste karta hai.

> **The tell:** data ke baare mein reply bina code block/row counts/"yahan maine compute kiya" ke —
> yeh **data ke baare mein opinion hai, analysis nahi.**

## Concept 5 — Brief the Problem, Not the Program

**Best code briefs mein koi technical language nahi hoti.** Loops, libraries, file handling, ya
language ka naam na lo. Jo good outcome dikhta hai usay describe karo — jaise human assistant ke
liye. **Jo half-programming jaante hain wo aksar total beginners se worse briefs likhte hain** —
wo "how" ko over-manage karte, "what" ko under-describe karte.

5 sections (prompting course se 3 pehle se jaante: Goal, Input, Output; code problems 2 naye add
karte hain):

- **Rules** — stranger ko na pata limits (school year August se start hota)
- **Edge cases** — imperfect data ko kya karna chahiye, pehle se decide

```text
# Brief: [name the task]

## Goal
What problem is solved when this works?

## Input
What am I giving you? (files, their format, roughly how many rows/items)

## Output
What exactly do I want back? (a number, a table, a chart, a cleaned
file, an HTML report)

## Rules
The constraints a stranger wouldn't know. (The school year starts in
August. "Pending" means not yet submitted. Ignore rows before 2024.)

## Edge cases
What should happen when the data is imperfect? (blank rows, duplicates,
a date in the wrong format, an amount with a currency symbol)
```

Yeh ek Markdown spec hai (Markdown In, HTML Out course ne sikhaya). Har heading ek aur cheez hai jo
AI ko guess nahi karni.

**Rules** — tumhari professional knowledge yahan rehti hai. AI Python jaanta hai, par nahi jaanta
ke tumhare system mein "Pending" ka matlab "abhi tak submit nahi hui" hai. **School administrator
ka missed-partial-payments** ek missing rule se aaya: "koi bhi unpaid balance = behind."

**Edge cases** — imperfect data ke liye pehle se decide. _"Jo row parh nahi sakte, guess mat karo —
skip karo, end mein list karo."_ Silent damage ko visible report mein badalta hai.

**Teacher-edition worked brief** — Rules+Edge cases ke bina chalao, mess wapas aa jata hai.

> **Edge cases nahi pata? Pucho.** Pehla prompt discovery ho: _"Files examine karo, batao kya
> unclear/inconsistent/surprising hai."_ AI wapas aata "14 rows blank dates, 2 currency formats
> hain, kya karoon?" — **ab** Edge cases knowledge se likho, imagination se nahi. **Inspect, ask,
> then brief.**
