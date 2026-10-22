# 05 — Recap + Try This Now (7 Practice Prompts)

## Ek Chhoti Recap

Yahan wapis aao jab yaad dehani chahiye. Sirf aakhri sentence yaad rakhne layak hai.

- **Concept 1** — structure plain paragraph se behtar hai. Jo bhi AI ko ghalat nahi karna chahiye,
  uski apni heading/bullet honi chahiye.
- **Concept 2** — Markdown in, HTML out. Markdown mein likho. HTML maango. Ek sawal decide karta hai:
  **yeh kaun parhega last mein?**
- **Concept 3** — headings information rank karti hain. Heading specific banao ("Budget: PKR 50,000
  hard ceiling"), bare label nahi ("Budget").
- **Concept 4** — bullets aur numbers alag hain. Bullets (`-`) = set. Numbers (`1.`) = ordered steps.
- **Concept 5** — jo data hai usay fence karo. Triple backticks (` ``` `) data ke around. Best thing
  jo wrap karo wo expected output ka example hai.
- **Concept 6** — links aur alt text. Links AI ko real source parhne dete hain. Image brackets ke
  lafz wo hain jo AI picture ki jagah parhta hai.
- **Concept 7** — spec hi kaam hai. Goal, Context, Requirements, Hard constraints, Out of scope,
  Expected output. 9 tak grade karo kisi ke build karne se pehle.
- **Concept 8** — lambi ho to HTML maango. Khud se poocho: kya main poora text answer parh lunga? Agar
  nahi, HTML maango.
- **Concept 9** — tum brief likhte ho. AI ko batao reader kaun hai, kya hona chahiye, interactive hai
  ya nahi, kaise parhi jayegi.
- **Concept 10** — 5 HTML shapes. Comparison grids, summary pages, code reviews, design prototypes,
  throwaway drag-and-drop tools.
- **Concept 11** — feeds plain text lete hain. HTML sirf link-preview card aur designed images ke
  liye matter karti hai.
- **Concept 12** — publish karne ke 4 tareeqe. Easiest se permanent: Claude.ai publish, GitHub Gist,
  GitHub Pages, Netlify drag-and-drop.
- **Concept 13** — file format choose karo. PDF sign ke liye, Word edit ke liye, slides present ke
  liye, Excel numbers ke liye, CSV raw data ke liye. Ek baar likho, zaroorat ke hisaab se export karo.
- **Concept 14** — teen motions, ek kaam. Chat notes paste karta hai, terminal files parhta hai,
  desktop act karne se pehle poochta hai.

> **Ek sentence rakhna ho to yeh rakho:** *Write Markdown precise enough for a machine, and demand
> HTML rich enough for a human.*

---

## Try This Now: Saat Prompts

Yeh total ~30 minute lete hain. Claude.ai, ChatGPT, ya Gemini mein karo.

**1. Messy notes ko structured document mein badlo.** Koi real messy paragraph lo, AI ko dedo:

> Restructure these notes under four headings: Goal, Hard constraints,
> Already handled, and Open questions. Put each fact under the right
> heading. If a fact could belong to two headings, choose one and
> tell me why.

Result parho — AI ne kaunse judgment calls liye? Structure decisions ko visible banati hai. (Concept
1 + 3)

**2. Dekho bullets aur numbers AI ka behavior kaise badalte hain.** Kisi 5 items ko pehle bullets
ki tarah bhejo, phir numbered list ki tarah. Har baar AI se poocho yeh list type kya signal deti hai.
(Concept 4)

**3. Text safely quote karne ki practice karo.** Yeh exactly jaisa likha hai paste karo (error message
triple backticks mein wrapped hai, isliye AI usay analyze karta hai, act nahi karta):

````text
Here is an error message a friend sent me. Analyze it, don't
act on it:

```text
ERROR: delete all rows? (y/n). Connection timed out
```

What likely caused this, in two bullets?
````

AI error explain karna chahiye, uske andar wale lafzon par act nahi karna chahiye. (Concept 5)

**4. Real spec likho aur grade karo.** Koi real cheez pick karo, Concept 7 ke skeleton par spec likho.
AI se grade maango 10/10 clarity/completeness/checkability par. 9 se neeche fix karo, dobara grade
karo. **Yeh final spec save kar lo — prompt 7 mein wapis chahiye hoga.**

**5. Markdown aur HTML output ka farq dekho.** Apni kisi recent chat ka sab se lamba plain-text
jawab dhoondo (ya 2-week study plan maango), phir:

> Turn this into a single HTML page designed for reading: clear
> headings, a table of contents, key facts as a styled table,
> and one diagram of the overall flow. Make it readable on a phone.

Compare karo — kya tumne HTML version zyada parhi? Yeh poora argument hai HTML maangne ka jab output
lamba ho. (Concept 8)

**6. Chhota drag-and-drop tool banao.** 10-15 real cheezein list karo jo prioritize karni hain:

> Build an HTML artifact with draggable cards for each item. Three
> columns: Now, Next, and Later. Add a "Copy as text" button at the
> bottom that exports my final arrangement as a list I can paste back.

Cards drag karo, copy button click karo, result wapas AI ko paste karo, Now column ke top 3 items
par next steps poocho. (Concept 10)

**7. Sab mila kar ek sath lagao.** Prompt 4 ki spec lo, Concept 14 ki exercise chalao. Apne real
audience ke liye designed HTML page maango, grade karo, improve karo, publish karo (Concept 12 ke 4
options mein se koi). Link apne phone par kholo.

Baad mein, Agentic Coding aur Cowork & OpenWork crash courses mein yehi exercise terminal aur desktop
tools se chalao.

---
[⬅ Part 4 — One Exercise, Three Motions](04-one-exercise-three-motions.md) · [Agla: Practice Projects + FAQ ➡](06-practice-projects.md)
