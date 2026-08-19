# Markdown In, HTML Out — Summary

⚠️ **Chapter incomplete on disk:** README indexes 8 parts (00 Overview → 07 Appendix), but only
`00-overview.md` and `01-two-languages.md` exist in `docs/markdown-html-crash-course/`. Parts 2-4
(Markdown writing language, HTML reading language, One Exercise Three Motions), Recap+7 Practice
Prompts, Practice Projects, and the Appendix still need fetching from Zia Tutor AI before this chapter
can be marked done, per this repo's own critical rule about partial chapters.

Yeh summary sirf jo maujood hai wo cover karta hai.

## Course Ka Core Idea

- Har format decision ek hi sawal se decide hota hai: **yeh cheez aakhir mein kaun parhega?** Insaan
  browser mein parhega → HTML. AI parhega (future chat sameet) → Markdown. Pata nahi → Markdown (insaan
  Markdown kaafi parh leta hai; AI HTML ghalat parhta hai; Markdown kabhi bhi HTML mein render ho sakta
  hai jab chahiye ho).
- One-liner: *"Write Markdown precise enough for a machine; demand HTML rich enough for a human."*

## 00 — Overview: Prove It in Two Minutes

- Flow: aap Markdown likhte ho (spec) → agent HTML deta hai (report, artifact/Canvas) → agent agle agent
  ko Markdown context deta hai.
- 2-minute proof exercise: claude.ai/ChatGPT/Gemini ko ek HTML-artifact request paste karo (tuition-center
  welcome card example) — result ek **artifact** (live document conversation ke sath) hota hai, share/
  publish link ke sath.
- Course map: Part 1 split frame karta hai, Part 2 Markdown (haath se likhi jati hai), Part 3 HTML demand
  karna (kabhi khud nahi likhi jati), Part 4 ek exercise 3 tareeqon se.

## 01 — Part 1: The Two Languages (Concepts 1-2)

- **Concept 1 — Agents ko structure kyun chahiye:** Unstructured prose vs structured Markdown (headings +
  bullets + "Out of scope" section) side-by-side example. Har inference ek jagah hai jahan agent ghalat
  guess kar sakta hai — aur confident lagta hai jab ghalat ho. "Out of scope" likhna almost kabhi prose
  nahi karta, lekin har acchi spec ka aadha hissa hai.
- Markdown = **specification language** kyunki agents heavily Markdown-trained hain (`#` heading = hierarchy
  signal, decoration nahi). Baad ke chapters isay **Intent Layer** kehte hain.
- School Sports Day example: constraint sentence ke beech chhupi thi, draft ne miss kiya; `## Hard
  constraints` heading + bullet mein move karne se agla draft perfectly comply kiya — constraint badla
  nahi, uski **structure mein visibility** badli. Habit: jo cheez galat hona allowed nahi, uski apni
  heading/bullet honi chahiye, kabhi sentence ke andar nahi.
- **Concept 2 — Asymmetry: Markdown In, HTML Out.** Thariq Shihipar (Anthropic, Claude Code team) ka essay:
  Markdown outputs mangna chhora, HTML mangna shuru kiya — 5 wajah: lambi Markdown unreadable (~100 lines
  ke baad log parhna band karte), Markdown ki ceiling low (headings/lists/tables se zyada nahi), HTML ki
  almost no ceiling, HTML shareable (browser-native), Markdown ka killer feature (hand-editability) fade
  ho raha hai kyunki ab log output hand-edit nahi karte, agent ko re-prompt karte hain.
- **Asymmetry table:** Aap→Agent = Markdown (ambiguity-free, fast, natively parhi jati hai). Agent→Aap =
  HTML (rich/readable/shareable/interactive). Agent→Agent = Markdown (compact/precise context passing,
  chahe dono "agents" aap khud se baat kar rahe ho — naye chat ko kuch yaad nahi).
- "HTML out" ki condition: **reader human ho.** AI ke liye HTML noise hai (tags/styling hazaron words
  kharch karte hain jo Markdown 50 mein bolta hai). Sawal: yeh aakhir mein kaun parhega — insaan → HTML,
  AI → Markdown, pata nahi → Markdown.
