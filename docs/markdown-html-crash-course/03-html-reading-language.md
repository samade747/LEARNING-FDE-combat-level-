# 03 — Part 3: HTML, the Reading Language (Concepts 8-13)

Ab tum structured input likhte ho. Doosra hissa structured **output** maangna hai — aur yahan rule
invert ho jata hai. Tumhara kaam hai jaanna **kab** HTML maangni hai, **kya** maangni hai, aur jo wapis
aaye use kaise judge karna hai.

## Concept 8: HTML kyun maango

Kisi bhi lambi Markdown plan/report par try karo. Phir:

> Turn this into a single HTML file designed for reading:
> clear visual hierarchy, a small table of contents, the key
> numbers as a styled table, and one SVG diagram of the overall
> flow. Optimize it for someone reading it once on a phone.

Wapis aati hai wahi information — lekin ab tum isay **actually parhte ho**.

| HTML kya add karti hai | Practically dikhti kaisi hai |
| --- | --- |
| Information density | Tables, color coding, SVG diagrams, annotated code — bullet walls ki jagah |
| Navigability | Tabs, table of contents, collapsible sections — 500-line plan move-through-able |
| Shareability | Browser mein khulti hai, link publish karo, koi bhi click kare, no app/account |
| Interactivity | Sliders, toggles, draggable cards — document instrument ban jata hai |
| Copy-back loop | Button jo tumhari choices text ki tarah export karta hai, wapas agent ko paste karo |

Aakhri row sab se kam obvious aur sab se zyada useful hai. Kuch preferences lafzon mein bayan karna
mushkil hain — ek color, animation speed, 30 items ki priority order. Agent se controls + "copy as
text" button maango, aur "thoda warm karo, nahi, less orange" 30 second ki dragging + ek paste ban
jati hai.

> ⚠️ **Honest caveat:** HTML output zyada **tokens** use karta hai Markdown se — chhoti 3-line answer
> ke liye yeh pure overhead hai. Trade tab worth hai jab output lamba, visual, shared, ya revisit hone
> wala ho. Mobile data ka bhi ek cost hai — heavy artifact (external fonts, bare images, bare
> libraries) kai MB tak barh sakta hai. Jab bandwidth matter kare, kaho: *"Lightweight, single file,
> no external fonts or libraries, keep it under 200 KB."*

## Concept 9: Tum HTML nahi likhte, tum iski demand karte ho

Claude.ai/ChatGPT/Gemini mein "create an HTML artifact" kehna kaafi hai — AI chat ke panel ke bagal
mein ek live page bana deta hai. Terminal tools (Claude Code, OpenCode) ke paas side panel nahi hota —
wo tumhari disk par real files likhte hain, isliye wahan kaho "write this as an HTML file."

Demand karna aasan hissa hai. **Achi** HTML paana skill hai — aur farq trigger word mein nahi, us
**brief** mein hai jo tum uske gird likhte ho. "Make me a page" = "make me food" kehna chef se.

**4 cheezein har HTML request mein shamil karo:**

1. **Kaun parhega.** Ek principal jo phone par sirf ek baar check karegi, ek reference jo tum 10 baar
   khologe se bilkul alag dikhti hai.
2. **Kya hona chahiye.** Diagram of X. Table of Y. 3 key-numbers ki summary strip. Agents named pieces
   banane mein excellent hain, guessing mein poor.
3. **Interactive honi chahiye ya nahi.** Sliders? Copy button? Tabs? Zaroorat nahi to skip karo.
4. **Kaise parhi jayegi.** "Optimize for reading once" = clean linear page. "Optimize as a reference"
   = table of contents + collapsible sections.

```text
Weak:   Make an HTML report about my sales data.

Strong: Read the attached sales CSV. Produce one HTML file for
        my two co-founders, reading once on laptops: a headline
        findings strip on top (3 numbers, large), one SVG chart
        of monthly revenue by product, a table of the 5 fastest
        growers, and a short "what I'd do next" section. No
        scrolling past 3 screens.
```

**Judging result:** grading discipline seedha transfer hoti hai. Kisi bhi HTML artifact ko 10/10 par
grade karo 4 sawalon se: Source ka har fact hai? 10 second mein sab se important cheez mil jati hai?
Phone par parhti hai? Kya tum yeh link forward karoge? 9 se neeche jo bhi ho, gap naam karo aur dobara
poocho.

## Concept 10: 5 HTML Patterns

**Pattern 1 — Plans aur Explorations.** Decision lene ke liye AI se ek jawab mat maango — kai options
side-by-side grid mein lay out karwao, har card apna trade-off dikhaye.

> I'm deciding how to structure [thing]. Generate 5 distinctly
> different approaches and lay them out in one HTML file as a
> grid I can compare side by side. Label each card with the
> trade-off it makes. Don't recommend yet. Let me look first.

**Pattern 2 — Explainers aur Reports.** Ek lambi document/data file/meeting notes ka pile parhna nahi
hai — AI se ek-page HTML summary maango.

**Pattern 3 — Code Review.** Color-coded diffs, annotated code margins mein explanations, flowcharts
— Agentic Coding Crash Course mein poora develop hota hai.

**Pattern 4 — Design Prototypes.** Jab lafzon mein describe karna namumkin ho (kaunsa shade, kitna
rounded corner) — live controls ke sath ek page banwao.

**Pattern 5 — Throwaway Editors (sabse underrated).** Ek-dafa ke chhote tool — 30 tasks prioritize
karna, 20 ideas categorize karna. Drag-and-drop page banwao, 10 minute use karo, copy karo, result
agent ko paste karo, phir kabhi na kholo. **Page disposable hai. Jo text wo export karti hai wo hi
rakhne wali cheez hai.**

Har pattern mein: Markdown/data andar jaati hai, HTML bahar aati hai, aur conversation continue karne
wali cheez text ki tarah wapis aati hai — Concept 2 ki asymmetry, habit ki tarah.

## Concept 11: Jab destination feed hai, browser nahi

"HTML out" rule ka ek bara exception. WhatsApp, LinkedIn, Facebook par post karte ho to app tumhari
formatting ignore kar ke apne design mein dikhati hai. Sawal badal jata hai: **destination asal mein
kya dikhati hai?**

- **WhatsApp** almost saari formatting strip karta hai (`*bold*`, `_italic_` bas) — **plain text**
  maango, short lines, aakhir mein bare link.
- **LinkedIn/Facebook** bhi plain text hi dikhati hain. LinkedIn ki pehli line attention grab karni
  chahiye ("…see more" button baaqi hide karta hai).

Raw HTML post body mein paste karna **hamesha ghalat move hai** — angle-brackets ki wall ban jati hai.

HTML phir bhi 2 jagah matter karti hai:
- **Link preview card:** platform hidden **Open Graph tags** parh ke yeh card banata hai — AI ko kaho
  "include Open Graph meta tags so the link preview looks designed."
- **Designed images:** quote card/stat graphic — HTML page bana kar PNG save karwao, HTML nahi, image
  post karo.

| Post kya hai | Kya maango | Kyun |
| --- | --- | --- |
| WhatsApp message | Plain text, short lines | WhatsApp sab formatting strip karta hai (bold/italic ke ilawa) |
| LinkedIn/Facebook post | Plain text, platform ke liye likha | App tumhari formatting ignore karta hai |
| Link jo post mein share ho | HTML with Open Graph tags | Platform hidden labels parh ke preview card banata hai |
| Image jo post mein attach ho | HTML, phir PNG save | Feeds images ko prominently dikhati hain |

## Concept 12: Publishing — artifact se link tak

**Option 1: Claude.ai built-in publish** (easiest) — artifact panel ka publish button, public link
ek click mein. Link public hai, private cheez publish mat karo; baad mein unpublish kar sakte ho.
**Option 2: GitHub Gist** — file paste karo, link milta hai; designed page ke liye
htmlpreview.github.io se kholo. **Option 3: GitHub Pages** — permanent, free address
(`yourname.github.io/mypage`), ek repository banani hoti hai. **Option 4: Netlify** — free account,
HTML file drag karo, seconds mein live address, no Git.

| Zaroorat | Use karo |
| --- | --- |
| Abhi link chahiye, kuch setup nahi | Claude.ai publish |
| File rakhni/edit karni hai baad mein | GitHub Gist |
| Permanent page, Git use karte ho | GitHub Pages |
| Permanent page, apna address, Git nahi | Netlify |

## Concept 13: Jab destination document hai, browser nahi

Doosra exception: kabhi reader ko ek specific **file format** chahiye, web page nahi. Accountant tax
filing ke liye Claude.ai link submit nahi kar sakta. Sawal thoda badalta hai:

> **Who reads this last, and what will they do with it?**

| Reader isse kya karega | Dedo | Kyun |
| --- | --- | --- |
| Sirf parhna | HTML page ka link | Download/app ki zaroorat nahi |
| Sign/print/file karna record ki tarah | PDF | Hamesha same dikhta hai, accidentally badalta nahi |
| Edit/comment karna | Word (.docx) | Track Changes use karenge |
| Meeting mein present karna | Slides (.pptx) | Click-through karenge |
| Numbers/formulas ke sath kaam | Excel (.xlsx) | Spreadsheet mein kholenge |
| Doosre tool/agent ko data dena | **CSV** | Plain text, commas ke sath, koi tool parh sakta hai |

CSV wahi role play karta hai data ke liye jo Markdown text ke liye karta hai — plain, machine-first.
Excel wahi role play karta hai jo HTML karti hai — formatted, visual, human-ke-liye.

**Pattern underneath:** content ek baar likho plain structured text mein (Markdown words ke liye, CSV
numbers ke liye). Office format aakhri export step hai. Badalna ho to source edit karo, dobara export
karo — Word file ko directly edit mat karo.

**Example:** ek accountant ke 3 readers — audit reviewer ko Excel (formulas recalculate karni hain),
board ko published HTML link (sirf parhte hain), signed engagement letter PDF (file hone ke baad
kabhi badalna nahi chahiye). Ek project, teen readers, teen formats.

---
[⬅ Part 2 — Markdown](02-markdown-writing-language.md) · [Agla: Part 4 — One Exercise, Three Motions ➡](04-one-exercise-three-motions.md)
