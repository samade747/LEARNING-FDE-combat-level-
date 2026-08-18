# 06 — Practice Projects

12 prompts ne har concept ko ek-ek karke exercise kiya. Neeche ke pehle teen projects unko zanjeer mein
jorte hain, aur ek jagah khatam hote hain jahan chat window aapko nahi le ja sakti: kuch aisa jo aap
ne public internet par live bana diya, ek address par jo aap kisi dost ko text kar sakte ho. Har
project free account par 30-60 minute leta hai. Yeh sequenced hain — har ek ek move sikhata hai jo
agla use karta hai.

```text
 chat isko banati hai         aap download karte ho        internet serve karta hai
┌──────────────────┐       ┌──────────────┐  drag   ┌───────────────────────┐
│ side panel mein   │ ────→ │  index.html  │ ──────→ │ your-app.netlify.app  │
│ ek working app   │       │  (ek file)   │         │ (real, public URL)    │
└──────────────────┘       └──────────────┘         └───────────────────────┘
```

## Project 1 — Snake Battle (30-60 min)

ChatGPT, Claude, ya Gemini kholo aur bolo:

```text
Let's build and play a game where a snake eats fruit balls to grow.
```

Side panel mein ek playable snake game aa jata hai. **Done when:** aap arrow keys se snake steer kar
sakte ho aur kuch kha sakte ho. Ek minute khelo, aur notice karo pehli cheez jo aap chahte ho alag ho.
Phir careful brief mat likho — bas wish bol do:

```text
Can I pick my snake's color before the game starts?
```

Artifact in-place update ho jati hai. Khelte raho, wish karte raho. Phir game ke rules hi badal do:

```text
Now make it a battle: add computer-controlled snakes, and when a
snake dies its body turns into fruit the others can eat.
```

Teen sentences mein, aapke paas start screen, color pickers, bot opponents, aur ek rule hai jo aap ne
invent kiya. Notice karo: aapne kabhi HTML, JavaScript, collision detection, game loops mention nahi
kiye — aapne ek experience describe kiya aur model ne engineering ki (Concept 9). Yeh Concept 7 ka loop
hi hai, feedback step ke sath sabse honest critic — aap, mid-game.

Live jaane se pehle ek aakhri pass: jo saara waqt aap feel se grade kar rahe the, usko ek baar explicit
kar do:

```text
Score this game 1-10 on three things: is it fun, is it clear
what to do, and does it feel finished or rough? One sentence
each. Then make the single change that would raise the lowest
score, and do it.
```

Number ek honest jawab force karta hai jahan "kya yeh achha hai?" sirf "haan" leta hai (Concept 6).

**Ship karna:**

1. Game download karo (ChatGPT canvas mein download icon; Claude/Gemini mein equivalent).
2. File ka naam `index.html` rakho.
3. [netlify.com](https://www.netlify.com) par free account banao.
4. File ko drop zone mein drag karo.
5. Diya gaya address kholo. **Done when:** game aapke phone ke browser mein load hoti hai. Ek insaan
   ko link bhejo.

Downloaded file *aapki* hai — kisi bhi hosting service par, USB stick par, 10 saal mein bhi chalegi.

## Project 2 — Whack-a-Mole (45-60 min)

Snake game khelne se achi hui, phir ship karne se pehle ek baar grade hui. Yahan wahi ek grade poora
engine ban jata hai: aap Concept 7 ka poora page ek saath chalate ho — brainstorm options, structure ke
saath brief, test, rubric ke against score, aur rukna refuse karo jab tak scores high na hon.

Options se shuru karo, build se nahi:

```text
I want to build a Whack-a-Mole game. Before building anything,
give me 3 different visual theme options. One line each.
Don't build any of them yet.
```

Ek theme pick karo aur model ko sab kuch do — Goal / Input / Output structure ke saath:

```text
I pick the twilight garden theme: [describe it].

Now build the game with these specs:
Goal: Moles pop up randomly from holes in a 3x3 grid...
Input: Player clicks on moles that appear.
Output: [detailed visual specs — grid, mole emojis, score
counter, countdown timer with progress bar]
```

Game khel kar, exactly bolo kya ghalat hai AUR kya chahiye — vague complaints vague fixes lete hain.
Phir yeh move karo jo ek toy ko finished game se alag karti hai — "kya yeh achha hai?" mat poochho
(model hamesha haan bolega, Concept 6). Rubric do, aur model ko honestly score karne do:

```text
Score this game 1-10 on each criterion (visual clarity, fun
factor, difficulty curve, polish, game feel). One-sentence
justification per score. Then for EACH criterion, tell me the
single change that would raise the score the most.
```

Phir loop karo jab tak game score deserve na kare, aur **aap** decide karo kab rukna hai, model nahi
(Concept 13):

```text
Implement the top 3 highest-impact changes you suggested. Then
score the game again on the same criteria. Keep going until all
scores are 9 or above. I decide when to stop, not you.
```

Do power moves jab basics kaam kar rahe hon: hard design decisions ke liye "think hard" use karo
(Concept 5); aur ek doosre tool mein wahi prompts paste karo compare karne ke liye kaunsa behtar hai
(Concept 12) — koi jo sirf ek AI use karta hai, guess kar raha hai kaunsa best hai.

Ship karo exactly snake game ki tarah: download, `index.html` rename, Netlify mein drag. **Done when:**
ek dost apne phone se game khel sake link se.

## Project 3 — A Page That Is You (30-60 min)

Novice approach (Concept 1 live): "Meri summer camp mein AI seekhi. Ab main ek personal website banana
chahta hoon jo mere baare mein sab dikhaye." → generic page milti hai, kyunke sawal mein koi "aap" nahi
tha, is liye jawab generic hai — model gap ko average student page se bhar deta hai (Concept 2).

Better approach: pehle brief — audience ke saath goal, aur unn decisions ki list jo aap khud approve
karna chahte ho design banne se pehle:

```text
My Goal: To present myself professionally to everyone
(friends, relatives, businesses)

Here are some points that we have to work on before designing:
1. Website Colors  2. Background and Design
3. Text Size, Writing Style  4. What information will be there
5. How we present it professionally

Build and show it
```

Ek decent page milti hai. Usko visitor ki tarah parho aur poochho kya missing hai — jo evidence sirf
aap de sakte ho (files bhi context hain, Concept 4):

```text
It looks good but it is missing the most important information:
1. [a real link to something you shipped, e.g. Project 1's game]
2. [a real skill with proof]
3. [a course you studied, with a link]
4. [a certificate — attach the file]

Now plan and update it
```

Har line ek real, checkable cheez hai. Phir chhote design wishes, ek message mein ek: "heading shout
kar raha hai," "kam purple," "sections ke beech zyada space."

Jab lage complete hai, yeh complete nahi hai — aur yahan grader **aap nahi ho sakte**: aap already
jaante ho aap kaun ho, is liye feel nahi kar sakte ke page waqai wo keh rahi hai ya nahi. Yeh ek project
hai jahan aapko kisi doosre ki aankhein udhaar leni parti hain:

```text
Become a specific stranger landing on this page for the first
time. Pick one and stay in their head: a recruiter scanning for
eight seconds, a classmate who has never met me, or someone my
work would actually matter to. Score the page 1-10 on three
things: do you know who I am within five seconds, is it obvious
what I want you to do, and does anything read like filler you
would skip? One sentence each, in their voice. Then make the
single change that raises the lowest score and apply it.
```

Do baar chalao, har baar alag stranger ke saath. Jab do log jo kabhi nahi milenge, dono aapko 5 seconds
mein samajh jayein, page done hai. Ship karo exactly game ki tarah.

## Project 4 — AI Mini Textbook (2-4 hrs, Capstone)

Pehle teen projects ek public URL par khatam hue. Yeh jaan-boojh kar nahi hota. Yahan aap AI use karte
ho ek chhoti mini textbook chapter banane ke liye kisi ek topic par jo aap parh rahe ho — aur real
deliverable do cheezein hain: chapter (product) aur ek process notebook jo prove karta hai ke aap AI ko
direct, question, aur correct kar sakte ho (proof).

Yeh capstone hai kyunke yeh is poore page ko ek saath exercise karta hai: strong context dena (Concept
4), sahi retrieval mode choose karna (Concept 3), options-then-feedback loop aur rubric scoring
(Concept 7), aur claims verify karna trust karne ke bajaye (Concepts 2, 13).

**Step 1 — Ek chhota topic choose karo.** Poora subject nahi, ek chhota topic jo aap kuch pages mein
achi tarah parha sakte ho: "food chains and how energy flows" (Biology), "fractions and percentages"
(Math), "electric circuits" (Physics).

**Step 2 — AI ko achi tarah brief karo (Concept 4).** Pehle ek weak prompt chalao ("Explain ___.") sirf
baseline dekhne ke liye. Phir real prompt jo aapka real context deta hai: "Main Grade ___ student hoon.
Main ___ seekh raha hoon. Isko clearly explain karo, phir batao kya abhi bhi unclear hai."

**Step 3 — Options lo, phir push back karo (Concept 7).** 3 alag tareeqe mango topic explain karne ke,
lekin abhi full chapter mat banwao. Ek choose karo, doosron ko reason ke saath reject karo, revised
outlines mango. Reason ke saath reject karna yehi move hai jo prove karta hai aap AI ko direct kar rahe
ho, sirf pehla idea accept nahi kar rahe.

**Step 4 — Chapter banao.** Ab jab planning loop khatam hai, AI se "think hard" bol kar full chapter
draft karwao apne notes aur chosen outline se. Chapter mein 10 sections hone chahiye: title/audience,
learning goals, simple explanation, key terms, examples, common mistakes, diagram idea, 10 flashcards,
5-question quiz, 7-day revision plan.

**Step 5 — Score karo, phir verify karo (Concepts 2, 7, 13).** Pehle AI se apna draft rubric ke against
grade karwao (clarity, accuracy, age-fit, usefulness for revision) aur smallest suggested edits
implement karwao. Phir usse important claims list karwao aur khud check karo kuch bare claims apne
notes, textbook, ya quick web search ke against — har ek ko Accept/Reject/Modify/Needs Checking mark
karo.

**Step 6 — Process notebook assemble karo.** Isme cheh hisse hain:

- **B1 Topic Brief** — chhota paragraph: kaunsa topic, kyun chuna, kya hard hai, kiske liye hai.
- **B2 Source List** — kam se kam do sources, har ek ka type aur kaise use kiya.
- **B3 Prompt Log** — kam se kam 8 prompts, ek row per prompt: prompt, AI ne kya diya, agay kya badla.
- **B4 Rubric Scoring Table** — har criterion ka AI score, reason, smallest edit, aapka decision.
- **B5 Checking Table** — 6-10 AI statements, har ek Accept/Reject/Modify/Needs Checking + evidence +
  correction agar zaroori ho.
- **B6 Reflection** — 150-250 words: AI ne kya samajhne mein madad ki, kya ghalat/unclear tha, kaunsa
  prompt sabse acha kaam kiya, kya badla, agli baar kya alag karenge.

**Done when:** chapter complete hai (saare 10 sections) aur notebook proof rakhta hai: 8+ prompts ka
log, 2+ named sources, rubric scores, 6-10 verified statements ki checking table, aur apne alfaz mein
reflection.

> **Safety aur honesty rules:** private information share mat karo (address, phone, passwords, family
> details); blindly copy mat karo (AI mistakes karta hai, important facts check karo); AI se cheat
> karne ke liye use mat karo; sources invent mat karo — jo verify nahi kar sakte usko "Needs checking"
> mark karo.

---

## Jab Koi Project Ghalat Ho Jaye

| Symptom | Fix |
| --- | --- |
| Side panel mein app blank/frozen hai | Plain words mein bolo: "black screen hai" ya "start button kuch nahi karta." Model apna khud ka code dekh sakta hai aur usually fix kar deta hai. |
| Downloaded file text ki wall ki tarah khulti hai | Text editor mein khuli hai. Right-click karo, Open With, browser choose karo. |
| Netlify "Page not found" dikhata hai | File `index.html` naam ki nahi hai. Rename karo, dobara drag karo. |
| Address ugly hai | Default random naam hai. Project settings mein rename kar sakte ho. |
| Dost ko update ke baad purani version dikhti hai | Newest file ko deploys screen par drag karo, unse refresh karwao. |

## Frequently Asked

- **Kya exercises ke liye paid plan chahiye?** Nahi, ChatGPT/Claude/Gemini ke free tiers kaafi hain.
- **Ek tool use karein ya teen?** Ek daily default rakho, lekin comparison ke liye kam se kam ek alag
  family ka doosra install karo (Concept 13).
- **Recipes bhool gaye to?** Page bookmark karo. Sirf ek cheez memorize karne laayak hai: **get the
  right context in, keep the wrong context out.**

## Study Aids (Interactive, Book Ke Andar)

Book ke live page par is chapter ke saath ek **Flashcards** component (`<Flashcards />`) aur ek 30-sawal
**Test Your Understanding** quiz bhi hai jo har concept (1-13) ko multiple-choice format mein test karta
hai — jaise: "Ek analyst 'kaunsa CRM khareedein?' poochta hai aur generic teen-vendor list milti hai —
Concept 1 ke hisab se, asal wajah kya hai?" (Jawab: prompt mein koi context nahi tha; fix model switch
karna nahi, briefing hai.) Yeh quiz interactive component hai jo book ki live site par chalta hai —
poori quiz yahan reproduce nahi ki gayi, lekin uska maqsad wahi 13 concepts hain jo upar cover ho chuke.

---
[⬅ Recap + Practice Prompts](05-recap-and-practice-prompts.md) · [⬆ Index](README.md)
