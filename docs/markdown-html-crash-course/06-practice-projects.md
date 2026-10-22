# 06 — Practice Projects (The Page, The Wheel, The Deck) + FAQ

Saat prompts ne ek-ek move drill ki. Teen projects unko chain karte hain — har ek wahan khatam hoti
hai jahan ek chat window nahi le ja sakti: ek public link jo kisi dost ko text kar sako, ya ek file
jo kisi ko hand kar sako. Har ek 30-60 minute leta hai free account par. Real, runnable scaffolds
(setup + steps + "Done jab" checklist) [`projects/`](projects/README.md) mein hain.

## Pipeline (pehle 2 projects share karte hain)

```text
 the chat builds it          you download it          the internet serves it
┌──────────────────┐        ┌──────────────┐  drag   ┌───────────────────────┐
│ a designed page  │ ─────→ │  index.html  │ ──────→ │ your-site.netlify.app │
│  in the artifact │        │  (one file)  │         │ (a real, public URL)  │
└──────────────────┘        └──────────────┘         └───────────────────────┘
```

Teen projects ek hi skill ke teen jobs sikhate hain:

- **[Project 1 — The Page Someone Opens](projects/the-page-someone-opens/README.md)** (ek direction):
  Markdown spec → finished HTML page → ek insaan parhta hai. Page end of line hai.
- **[Project 2 — Spin the Wheel](projects/spin-the-wheel/README.md)** (do directions): tool banwao,
  operate karo, result text ki tarah wapas AI ko do — agli instruction ban jati hai.
- **[Project 3 — Present It Like You Mean It](projects/present-it-like-you-mean-it/README.md)**
  (browser se bahar): Project 2 ka tool deck mein badal jata hai, phir real PowerPoint file ban jata
  hai.

Project 3 Netlify pipeline use nahi karta — presentation file download + share link ki tarah ship
hoti hai.

## Frequently Asked Questions

<details>
<summary>Do I need to memorize more Markdown than what this course taught?</summary>

Nahi. Headings, lists, fences, links, images — yehi roz-marra ke kaam ke liye kaafi hai. Tables
example se already dekh chuke ho. Kuch fancier chahiye to AI ko likhne do.

</details>

<details>
<summary>Should I learn to write HTML by hand?</summary>

Is workflow ke liye nahi. Yeh course sikhati hai HTML kaise maangi jaye aur judge ki jaye, tags kaise
type karein nahi. Baad ka chapter web fundamentals cover karta hai, wahan AI ka kaam check karte
waqt HTML parhna seekhte ho.

</details>

<details>
<summary>Does asking for HTML waste my usage budget?</summary>

HTML output zyada usage budget use karti hai plain text se. Chhote jawabon ke liye worth nahi. Lekin
jo bhi lambi, visual, ya link ki tarah shared hai, HTML sahi choice hai. Asal waste ek lamba jawab
hai jo koi nahi parhta.

</details>

<details>
<summary>What about PDFs, Word docs, slides, and spreadsheets?</summary>

AI yeh sab bana sakta hai. [Concept 13](03-html-reading-language.md#concept-13-jab-destination-document-hai-browser-nahi)
mein poora jawab hai ready-to-paste prompts ke sath. Format pick karo isse: wo insaan file ke sath
kya **karega**. Sign? PDF. Edit? Word. Present? Slides. Numbers? Excel. Doosre tool ko dena? CSV.

</details>

<details>
<summary>What about code? Is that an output format too?</summary>

Is course ke matlab mein nahi. Markdown, HTML, PDF, waghera containers hain jo tum reader ke hisaab
se choose karte ho. Code container nahi hai — woh banayi ja rahi cheez hai.

Code is course se 2 tareeqon se connect hota hai: (1) spec mein code include karte waqt, fence karo
(Concept 5); (2) AI se code explain karwa sakte ho designed HTML page mein (Pattern 3). Software asal
mein banane ke liye, Agentic Coding Crash Course dekho.

</details>

<details>
<summary>Is there a tool that does this Markdown-in/HTML-out pattern automatically?</summary>

Haan — aur try karna worth hai **baad mein**, iski jagah nahi. Yeh course jo skill banati hai wo
briefing aur khud judge karna hai. Us skill ke bina, tool tumhari jagah sochta hai.

Open-source project [HTML Anything](https://github.com/nexu-io/html-anything) exactly yeh karta hai —
tumhare computer par chalta hai, already-hai AI tools ke sath kaam karta hai, notes/Markdown/CSV ko
ready-made templates ke across finished HTML page mein badal deta hai.

</details>

<details>
<summary>Where does this course lead?</summary>

Teen jagah:

- **Spec-driven development** — [Concept 7](02-markdown-writing-language.md#concept-7-tumhari-pehli-complete-specification)
  ke spec skeleton par banta hai.
- **Agentic Coding Crash Course** — yahan ki HTML-output aur checking habits par banta hai.
- **Problem-Solving Crash Course** — [Concept 14](04-one-exercise-three-motions.md#concept-14-teen-motions)
  ke teen motions assume karta hai.

</details>

Ab tum precisely bol sakte ho kya matlab rakhte ho, aur worth-parhne-wali output maang sakte ho.
Appendix ([07](07-appendix-spec-to-html.md)) poora process end-to-end dikhata hai. Agla sawal hai yeh
skill kahan **point** karni hai — [How to Think in the AI Era](../how-to-think-ai-era/README.md) aur
Problem-Solving Crash Course wahan se shuru hote hain.

---
[⬅ Recap + 7 Prompts](05-recap-and-practice-prompts.md) · [Agla: Appendix ➡](07-appendix-spec-to-html.md)
