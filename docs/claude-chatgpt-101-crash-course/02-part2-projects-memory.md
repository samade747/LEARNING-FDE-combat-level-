# 02 — Part 2: Making the Workspace Yours (Concepts 4-7)

## Concept 4: Projects — ek stream of work ke liye ek room

Kuch hafte AI use karne ke baad, sidebar messy ho jata hai: ek client ke baare mein ek chat, usi
client ke baare mein doosri chat, teesri jahan useful file thi, chauthi jahan wahi background dobara
explain kiya. **Projects** yehi solve karte hain.

Ek **project** ek workspace hai **ek stream of work** ke liye — ek room jahan ek topic ke baare mein
sab kuch sath rehta hai. Normally 3 cheezein hoti hain: **Chats** (us kaam se related), **Knowledge**
(upload ki gayi files), **Instructions** (project ke andar kaam karne ka standing tareeqa).

Is book ki language mein, project ek chhota **[System of Context](../ecosystem-system-of-context/README.md)**
hai.

**Claude aur ChatGPT thoda alag hain:**
- **Claude** growth ko **retrieval** se handle karta hai — jab project knowledge context window se
  bari ho jaye, Claude sab load karne ki jagah usay **search** karna shuru kar deta hai (Anthropic
  kehta hai ~10x capacity expand hoti hai). Yeh automatic hai, paid-plan feature hai.
- **ChatGPT** **project memory** add karta hai: ya to **default memory** (wider memory bhi part le
  sakti hai) ya **project-only memory** (project real boundary ban jata hai, bahar ki memories andar
  nahi aati).

**Project kab banao?** Test: *agar tumne same background 3 baar explain kiya hai ya same file 3 baar
upload ki hai, wo kaam ek project deserve karta hai.* One-off sawalon ko project nahi chahiye.

> **Yaad rakho:** projects un kaamon ke liye hain jo continue hotay hain.

## Concept 5: Memory aur Standing Instructions

Teen features context ko persistent banati hain: **standing instructions**, **memory**, **projects**.
Beginners inko mix kar dete hain — clean separation:

- **Standing instructions** = **stable rules** jo tum ek baar likhte ho aur broadly apply hona
  chahti hain ("Give me the answer before the explanation"). Claude settings/styles mein, ChatGPT
  Custom Instructions mein (Settings → Personalization) rakhta hai.
- **Memory** = **evolving context** jo assistant conversations se khud pick karta hai (preferences,
  recurring goals, facts). Dono products review/edit/delete karne dete hain. Work account par pehle
  check karo yeh on bhi hai ya nahi — Claude individual plans par default on karta hai, Team/Enterprise
  par owner ko enable karna parta hai.
- **Projects** = **scoped work** ke liye context (upar Concept 4).

**Rule of thumb:** *Instructions for stable rules. Memory for evolving context. Projects for scoped
work.* Yehi ek rule zyada tar configuration mistakes rok deta hai.

Dono products ek mode bhi dete hain jo conversation ko normal history/memory se bahar rakhta hai —
Claude **incognito chat**, ChatGPT **temporary chat** kehta hai. Dono vendors phir bhi ek copy ~30 din
tak safety/abuse review ke liye rakhte hain — isay **memory-free samjho, trace-free nahi.**

> ⚠️ **Stored context ek zimmedari hai:** sensitive information hold kar sakta hai, aur stale ho
> sakta hai — stale context **quietly fail** hota hai (koi error nahi, bas confident-lekin-ghalat
> jawab). Monthly review karo (ya jab role/project badle): har item ko **keep, correct, ya delete**
> karo.

> **Yaad rakho:** persistence sirf tab help karti hai jab sahi information sahi jagah ho.

## Concept 6: Artifacts aur Writing Blocks — jo kaam tum le ja sako

Chat conversation ke liye acha hai, **finished work** ke liye kamzor container hai. 2000-word report,
working calculator, diagram, ya chhoti app maango to result **ek alag object** chahiye, scroll mein
ek aur message nahi.

- **Claude: artifacts.** Alag output jo conversation ke bagal khulta hai — document, code, web page,
  diagram, vector image, calculator, dashboard, chhoti interactive app. Baat karte rehte ho jabke
  artifact wahan reh kar build/revise hota hai.
- **ChatGPT: writing blocks aur code blocks.** Purana "canvas" (side-by-side panel) 2026 mein retire
  ho gaya — wahi kaam ab **inline** editable regions ban gaye hain thread ke andar.

Design alag hai. Idea identical hai: **kaam ka product discussion se alag rakhna.**

**Behtar results ke liye:** "a dashboard" mat maango — batao finished cheez kya **karegi**:

> Build a monthly budget tracker. I should be able to enter expenses by
> category, see a pie chart, and get a warning when I go over budget.

Reader kaun hai batao, format batao. Agar jawab **data** hai, **structured output** maango (table/
spreadsheet, paragraph nahi — paragraph sort/filter/paste nahi ho sakta). Agar jawab ek **number** hai
jis par koi act karega, usay **computed** maango — "write and run code, show me the code you ran."
(Anthropic isay **code-executed** kehta hai — chautha output home, inline chat/artifacts/structured
data ke sath). Run exact hai, lekin code agent ne likha hai — **check karo kaunsa column use hua.**

> **Yaad rakho:** chat conversation hai; artifacts/writing blocks/code blocks kaam hold karte hain.
> Data table mein jata hai, number jis par act hoga computed hota hai.

## Concept 7: Skills aur Plugins — packaged ways of working

Projects ek sawal ka jawab dete hain: *right knowledge ko sath kaise rakhoon?* Repetition doosra sawal
uthati hai: *assistant ko har baar same method follow karwaoon kaise?* Yeh **skills** ke liye hai.

**Skill** = ek task karne ka packaged tareeqa (instructions, examples, resources, kabhi code). Matching
task aane par assistant khud load karta hai. Claude aur ChatGPT dono ke paas skills hain.

**Kyun matter karta hai:** dono vendors **Agent Skills open standard** (agentskills.io) par build
karte hain — ek skill Markdown files ka folder hai, koi server/runtime nahi, isliye **travel karta
hai**. Ek product ke liye likhi skill doosre mein install ho sakti hai. **"Discipline constant hai,
tool variable hai."**

**Plugin** broader kaam ke liye capabilities package karta hai — skills + outside apps connections +
kabhi commands/sub-agents, ek installable package mein.

| | |
| --- | --- |
| **Skill** | method sikhati hai |
| **App/connector** | outside system tak access deta hai |
| **Plugin** | inko wrap karta hai |
| **Project** | stream-of-work ka context store karta hai |
| **Custom GPT** (ChatGPT) | ek separately-configured assistant deta hai |

**Line yaad rakhne wali:** *Projects store knowledge. Skills perform tasks.* Ek customer-prep skill
project mein stored customer files use kar sakti hai — project **what** supply karta hai, skill **how**
supply karti hai.

> **Yaad rakho:** jab method repeat ho, method ko package karo.

---
[⬅ Part 1 — The Cockpit](01-part1-cockpit.md) · [Agla: Part 3 — Extending Reach ➡](03-part3-extending-reach.md) · [⬆ Index](README.md)
