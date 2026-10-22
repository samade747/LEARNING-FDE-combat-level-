# 04 — Part 4: One Exercise, Three Motions (Concept 14)

Jo tumne seekha har AI tool mein kaam karta hai, lekin alag tools kaam **alag tareeqe se** karte hain.
Book teen tareeqon ko **motion** kehti hai — agent ke sath kaam karne ka ek tareeqa.

1. **Chat** — jo tum already use karte ho. Claude.ai, ChatGPT, Gemini. Type karte ho, AI usi window
   mein jawab deta hai.
2. **Terminal tools** — Claude Code, OpenCode. Command line se chalte hain, tumhari files/folders
   seedha parhte hain, paste karne ka wait nahi karte.
3. **Desktop apps** — Cowork, OpenWork. Visual interface, no command line. Tumhari files dhoondte hain
   aur kuch karne se pehle plan approve karwate hain.

**Abhi sirf pehla chahiye.** Baaqi do previews hain — skim karo, baad mein un courses ke baad wapis
aao.

## Concept 14: Teen Motions

**Motion 1 — Chat (main method).** Poora kaam ek conversation mein Claude.ai mein hota hai. ChatGPT/
Gemini par "Canvas" bolo "artifact" ki jagah.

**Step 1 — Notes paste karo, spec maango:**
> Restructure these notes into a Markdown specification with these
> sections: Goal, Context, Requirements, Hard constraints, Out of
> scope, and Expected output. Show it to me as a Markdown artifact.

**Step 2 — Spec grade karo aur improve karo** (yeh step skip mat karo):
> Review the spec you just wrote. List anything that is unclear or
> could be read two ways. Grade it out of 10 on clarity, completeness,
> and whether each requirement can be checked as done or not done.
> Fix anything that scored below 9.

**Step 3 — Spec ko designed HTML page mein badlo:**
> Create a second artifact: a single HTML page presenting this spec
> to [describe your real audience]. Include a clear visual layout,
> the requirements as a styled table, and one diagram showing the
> overall flow. Make it readable on a phone.

**Step 4 — Publish karo aur phone par check karo.** Artifact panel ka publish button use karo. Khud
se poocho: kya main yeh forward karunga? Agar nahi, AI ko batao kya ghalat hai.

**Chat sab se acha starting point kyun hai:** AI page conversation ke bagal mein banata hai, edits
in-place hoti hain, sharing ek click hai. **Chat ki limit kahan hai:** sirf wo dekhta hai jo tum paste
karte ho — agar notes kai files mein scattered hain, aur tool chahiye.

**Motion 2 — Terminal (preview).** Claude Code/OpenCode terminal mein chalte hain. Bara farq: notes
kahan rehte hain. Ek folder mein daal kar wahan terminal kholo — AI khud har file parh leta hai:

> Read every file in this folder. Produce a Markdown spec called
> spec.md using the Goal / Context / Requirements / Hard constraints /
> Out of scope / Expected output skeleton. Grade it yourself and
> keep improving it until it scores 9 or above. Then produce
> report.html: a one-page visual summary with a diagram. Tell me
> when both files are ready and what I should review.

AI do real files banata hai computer par: `spec.md` aur `report.html`.

**Motion 3 — Desktop app (preview).** App ko notes folder ki taraf point karo, plain language mein
poocho. Ek zaroori addition: yeh apps files badal sakte hain, isliye hamesha pehle plan maango:

> Look through this folder. Show me a plan first: which files you
> will read, and what spec.md and report.html will contain. Do not
> write anything until I say go.

Yeh habit har waqt matter karti hai jab AI tool tumhari files touch kar sakta hai — permission
discipline [AI Prompting 2026](../ai-prompting-2026/README.md) se carry hoti hai.

**Kaunsi motion use karein?**

| Tumhari situation | Use karo |
| --- | --- |
| Notes paste mein fit ho jate hain, 1 minute mein shareable link chahiye | Chat |
| Notes kai files/folders mein scattered hain | Terminal |
| Notes folders mein hain, app kuch touch karne se pehle poochni chahiye | Desktop |

Har motion ke 2 tool options hain. Claude Code aur Cowork Anthropic ke hain. OpenCode aur OpenWork
open-source alternatives (kai AI providers ke sath kaam karte hain). Prompt wahi rehta hai.

### Format decision, final form

| Tum kya kar rahe ho... | Use karo |
| --- | --- |
| Agent ko batana kya karna hai | Markdown |
| Context save karna future session/agent ke liye | Markdown |
| Output produce karna jo doosra agent parhega | Markdown |
| Lambi plan/report/analysis parhna | HTML |
| Output link ki tarah share karna | HTML |
| Feed mein post karna (WhatsApp/LinkedIn/Facebook) | Plain text body ke liye, HTML sirf linked page/image ke liye |
| Values choose karna jo lafzon mein mushkil hain | HTML, copy-back button ke sath |
| Kisi ko sign/file/print karne ke liye dena | PDF |
| Kisi ko edit/present karne ke liye dena | DOCX ya PPTX |
| Numbers dena jo read/edit/formula ho sakein | XLSX |
| Structured data doosre tool/agent ko dena | CSV |

---
[⬅ Part 3 — HTML](03-html-reading-language.md) · [Agla: Recap + 7 Practice Prompts ➡](05-recap-and-practice-prompts.md)
