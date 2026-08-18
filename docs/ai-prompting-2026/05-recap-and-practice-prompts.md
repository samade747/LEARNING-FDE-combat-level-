# 05 — Recap + Try This Now (12 Practice Prompts)

## Short Recap — 13 Concepts, Ek-Ek Line

- **Concept 1.** Novice aur power-user prompt ke darmiyan gap chand habits hain: AI ko smart new
  colleague ki tarah brief karo — context, constraints, clear ask ke saath.
- **Concept 2.** AI internet ke ek snapshot se cheezein jaanta hai — duniya ke baare mein *text parh*
  kar seekha, *experience* kar ke nahi — is liye common topics par strong, obscure/recent par weak.
- **Concept 3.** Teen retrieval modes: pretrained, web search, deep research. Aapki wording decide
  karti hai kaunsa fire hota hai.
- **Concept 4.** Model ki apni koi memory nahi; context window is response ke liye uski working memory
  hai. Answer quality ka sabse bara determinant yeh hai ke aap window mein kya rakhte ho — aur projects
  aapko yeh ek baar front-load karne dete hain, har baar nahi. Tools ki apni memory features chhata
  layer add karte hain jo aapne likha nahi — parho aur prune karo.
- **Concept 5.** Modern models seconds ya minutes tak hard think kar sakte hain agar aap mango.
- **Concept 6.** Models agreement ki taraf biased hain. Neutral framing aur rubrics zyada tar bias
  neutralize karte hain; har criterion ke liye 1-10 score force karna, aur woh change jo score barhaye,
  baaqi neutralize karta hai.
- **Concept 7.** Explicit-feedback wala iterate loop is page ka sabse high-leverage habit hai. Har
  stage 10 mein se grade karo aur re-iterate karo jab tak score plateau na ho.
- **Concepts 8-9.** AI images dekh sakta hai, audio dono directions mein handle kar sakta hai, aur
  chhoti apps bana sakta hai — chalti hui app ek *artifact* hai jise aap iterate, share, embed kar
  sakte ho.
- **Concept 10.** AI code bhi likh aur chala sakta hai aapke data par, lekin yeh automatically hamesha
  nahi karta. Explicitly poochho, aur verify karo ke code actually chala.
- **Concept 11.** File-aware desktop apps ka naya category hai (Cowork, OpenWork). Permissions tight
  scope karo jab tak safely use na kar liya ho.
- **Concept 12.** Sahi tool har kuch mahino mein badalta hai. Distinct families jaano (Claude, ChatGPT,
  Gemini, Grok, Meta AI, DeepSeek), sab ke free tiers, aur Arena ko monthly check karo.
- **Concept 13.** Jab koi human expert room mein na ho, models ko ek doosre se — **alag families ke
  across** — grade karwana quality ka sabse objective signal hai jo maujood hai.

> Underneath sab kuch ek move hai, dus disguises mein: **sahi context andar lao, ghalat context bahar
> rakho.** Agar is page se ek hi cheez yaad rahe, aap phir bhi top quartile users mein honge.

## Try This Now — 12 Prompts (~28 Minutes)

Parhna trying ka placeholder hai. Claude, ChatGPT, ya Gemini kisi doosre tab mein kholo. Yeh 12 prompts
order mein chalao.

**1. Web-search trigger.**

```text
What major news happened today in [your country]? Cite each claim
with a source link. Flag any claim you can't support with a citation
as "unverified".
```

**2. Pretrained-only question.**

```text
Why do cats stare at walls? Two-paragraph answer.
```

**3. Context-rich personal prompt.**

```text
Plan a 15-minute home workout for me. Constraints: I have stairs
in my home, a bad knee (no squats), I cannot stick to plans for
more than three days, and I want to feel slightly silly while
doing it. Give me 3 options, no commentary.
```

**4. Neutral-framing rewrite.**

```text
The question I want to ask is: "Don't you think four-day work
weeks are obviously better for everyone?" Rewrite this as a
neutral question that doesn't signal what answer I want.
Then answer the rewritten version.
```

**5. Three-options brainstorm with iteration.**

```text
Round 1: I want to start a small side project that takes about
3 hours per week and might make money in a year. I'm a [your
profession] who likes [your hobby]. Give me 5 different ideas,
one line each. Don't expand any of them.

(Read the 5. Pick what you like and don't like. Then, in the
SAME conversation:)

Round 2: I reject options [N] and [N] because [reason]. I like
the [keyword] idea but I want it to use less [thing]. Give me
5 new options that incorporate this feedback.
```

**6. Outline-first writing.**

```text
I want to write a 600-word post about [a topic you care about].
Don't write it yet. Give me 3 different outline options, each
with 4-6 headings. One line per heading.
```

**7. Think-hard reasoning prompt.**

```text
I'm choosing between [Option A] and [Option B] for [real personal
decision in your life]. Here's the relevant context: [a paragraph
of context]. Think hard before answering. Tell me:
1. The 3 trade-offs that actually matter.
2. Which you'd choose and why.
3. Under what conditions your recommendation would flip.
```

**8. Grade-and-improve critique.**

```text
I'm pasting in something I wrote: [paste anything 100-300 words].

Critique it using these 4 criteria, each scored 1-10 with a
one-sentence justification:
- Does it have a clear central claim?
- Is each paragraph in the right order?
- Are there any sentences that could be cut without loss?
- Does the ending earn the time the reader spent getting there?

Then, for each criterion, tell me the change that would raise
its score the most. There is always a next level — even a 9
has a path to 9.5.
```

**9. Image-input task.**

```text
[Upload any handwritten note, receipt, or whiteboard photo]

Transcribe what's written. Then summarize what it's about in
3 bullets. Flag anything you couldn't read with confidence.
```

**10. Small-app prompt.**

```text
Build me a Pomodoro timer.
Goal: 25-minute work sessions, 5-minute breaks.
Input: I press start.
Output: Visible timer counting down, a satisfying click when
each cycle ends, a yellow theme. Show me the working version.
```

**11. Data analysis — silent failure mode expose karo.** Do rounds mein.

```text
Round 1, the trap: In a fresh conversation, paste this prompt
exactly as written. Do NOT mention code.

  "Here are 18 numbers: 47, 52, 89, 91, 23, 67, 78, 12, 95,
  44, 88, 71, 33, 56, 99, 18, 64, 82. What is the median,
  the average, and which numbers are outliers? Be specific."

Look at the response carefully. Did the AI show you a code
block that it ran? Or did it write a paragraph with numbers
in it and no visible computation? Note your answer.

Round 2, the fix: In the same conversation, paste this:

  "Now run that calculation again — but this time write and
  run code to do it, and show me the code you ran."

Compare the two answers. Correct answers: median 65.5, average
~61.6, no clear outliers (numbers roughly evenly spread).
```

**12. Cross-model review.** Do alag-family AI tools chahiye.

```text
Take any 200-300 word draft you wrote recently (an email, a memo,
or a paragraph from one of these exercises).

Step 1: In your primary AI tool, paste the draft and ask: "Score
this 1-10 on clarity, structure, evidence, and what's missing.
One-sentence justification per score."

Step 2: Open a second AI tool from a different family (if your
primary is Claude, use ChatGPT or Gemini or Meta AI — not another
Anthropic model). Paste the same draft, ask the same question.

Step 3: Compare the two scores and the two critiques side by
side. Note any point only one of them caught. Those are the
points the cross-model loop pays for.
```

---
[⬅ Part 4 — Working Safely and Choosing Tools](04-working-safely-and-choosing-tools.md) · [⬆ Index](README.md) · [Agla: Practice Projects ➡](06-practice-projects.md)
