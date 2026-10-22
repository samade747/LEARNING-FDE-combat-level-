# 00 — Overview: Pipeline Ek Nazar Mein

## Ek Ghalat Narrative Jo Industry Mein Chal Rahi Hai

Aaj kal ek kahani common hai: AI ek naya paradigm hai, to purani engineering rules apply nahi hoti;
specifications naya source code hain; model compiler hai; diff matter nahi karti jab tak program
behave karta hai. Ye kahani comforting hai — aur ghalat hai.

Is chapter ka thesis, aur is poori book ka throughline, iske ulat hai:

> **Software fundamentals AI ke daur mein pehle se zyada matter karti hain.**

Wajah **mechanical** hai, sentimental nahi. Jo interface aap design karte ho, wahi interface agent
seekhta hai; jo names aap choose karte ho, wahi names agent reuse karta hai; jo boundaries aap
khainchte ho, unhi ko agent respect karta hai. Ek clean, well-tested codebase mein agent kai quality
tiers behtar code deta hai — usi agent ke jo tangled codebase mein kaam kar raha ho, us se. Architecture
ab sirf code ki property nahi hai; ab wo **agent ke liye input** hai. Bad code bad agents deta hai.
Good code aise agents deta hai jo hairatangez competent lagte hain.

## Matt Pocock aur Karpathy Ke Do Jumle

Chapter do epigraphs se shuru hoti hai jo poori baat compress kar dete hain:

> "Code is not cheap. Bad code is the most expensive it has ever been." — **Matt Pocock**

> "Vibe coding is about raising the floor for everyone in terms of what they can do in software.
> Agentic engineering is about preserving the quality bar of what existed before in professional
> software." — **Andrej Karpathy**

## Chapter Kya Sikhati Hai

Chapter ek **seven-stage pipeline** sikhati hai (_idea → grilling → PRD → issues → implementation →
review → QA_), jo chhoti, composable **[Skills](05-skills-as-encoded-process.md)** ke zariye implement
hoti hai — aur ye pipeline **Claude Code** aur **OpenCode** dono mein identically chalti hai. Skills,
specs, aur architectural patterns jo ek tool ke liye likhe jayen, doosre mein bina badlaw ke drop ho
jate hain. **Method constant hai. Tool variable hai.**

Chapter khatam hone tak aap ye kar sakoge:

1. **vibe coding ↔ agentic engineering** spectrum par apni jagah pehchano, aur kaam ke stakes ke
   mutabiq discipline choose karo.
2. AI coding ke **che failure modes** diagnose karo aur har ek ka cure apply karo.
3. Claude Code ya OpenCode mein poora **grill → PRD → vertical-slice issues → AFK implementation** loop
   chalao.
4. `SKILL.md` likho jo agent sirf zaroorat ke waqt load kare, har turn tokens burn na kare.
5. Codebase ko "shallow modules" se "deep modules" mein refactor karo taake AI feedback loops asal mein
   kaam karein.
6. Working vocabulary fluently use karo: **smart zone**, **dumb zone**, **clearing**, **compaction**,
   **handoff**, **AFK**, **tracer bullet**, **design concept**, **grilling**, **jagged intelligence**.

## The Pipeline At a Glance

Yahan wo operating shape hai jo poori chapter sikhati hai — saat stages, panch Skills, ek direction ka
flow. Har baad ki section is table ki ek row ko explain karti hai ya code mein dikhati hai.

| # | Stage | Kya hota hai | Input → Output | Skill | Section |
| --- | --- | --- | --- | --- | --- |
| 1 | Idea → Aligned concept | Agent aap ko Socratically interview karta hai jab tak design shared na ho | wish → design concept | `grill-me` | §6.1 |
| 2 | Concept → Destination | Conversation ko PRD mein synthesise karna | conversation → PRD | `to-prd` | §6.2 |
| 3 | PRD → Backlog | PRD ko vertical-slice tickets mein split karna | PRD → tracer-bullet issues | `to-issues` | §6.3 |
| 4 | Issue → Slice | Ek slice implement karna, test-first | issue → reviewable diff | `tdd` | §6.4 |
| 5 | Slices → Drained backlog | AFK loop backlog ko sandboxes ke andar drain karta hai | issues → PRs | (orchestrator) | §6.5 |
| 6 | Diff → Decision | Insaan diff parhta hai, QA chalata hai | PR → merge ya naya issue | (taste, automated nahi) | §6.6 |
| 7 | Codebase health, ongoing | Shallow modules dhoondo; deepenings propose karo | codebase → RFC | `improve-codebase-architecture` | §7.4 |

Stages 1–3 **day shift** hain: human-in-the-loop. Stages 4–5 **night shift** hain: agent AFK mein
sandbox ke andar chalta hai. Stage 6 wapas day shift. Stage 7 weekly cron par chalta hai aur stage 3
mein naye issues feed karta hai. Poori pipeline Claude Code aur OpenCode mein identically chalti hai.

## Naye Programmer Ke Liye Note

Ye chapter assume karti hai aap ne code likha hai, `git` use kiya hai, test suite chalaya hai, aur pull
request khola hai. Agar ye familiar hai, is note ko skip karo.

Agar nahi — chapter abhi bhi ek **conceptual map** ki tarah readable hai. Milega: workflow ki shape,
vocabulary jo AI-coding conversations samajhne ke liye zaroori hai, common failures ka catalogue, aur
architectural philosophy jo agents ko real codebases mein kaam karne layak banati hai. **Nahi** milega:
abhi example code chalana — iske liye kuch hafte programming foundations pehle chahiye. Honest path:
chapter ek dafa map ke liye parho, prerequisites seekho, phir wapas aa kar code follow karo.

Bare-minimum vocabulary jo conceptual sections follow karne ke liye chahiye:

- **Repo**: project ka code folder, `git` se tracked.
- **Branch**: repo ka parallel version jahan experiment kar sakte ho bina main code chhuye. **Worktree**
  related concept hai — ek branch se attached disk par repo ki copy.
- **Commit**: changes ka saved snapshot, ek short message ke sath.
- **Pull request (PR)**: proposed change jo merge se pehle review ke liye submit hoti hai — chapter ke
  stage 6 mein insaan isi ko review karta hai.
- **Test / test suite**: code jo doosre code ko check karta hai, automatically chalta hai. _"Tests
  pass"_ ka matlab hai saare checks green aaye.
- **Sandbox (container)**: isolated environment, sealed mini-computer jaisa, jahan agent run kar sakta
  hai, files likh sakta hai, aur kuch tor sakta hai baqi system ko chhuye bina.
- **Token**: text ki unit jo language model process karta hai — roughly _3/4 ek word_. 100k-token
  context window ~75,000 words rakhta hai.
- **Terminal / shell / bash**: computer par commands chalane ka text-based tareeqa.

---
[⬆ Index](README.md) · [Agla: Vibe Coding Se Agentic Engineering Tak ➡](01-vibe-coding-to-agentic-engineering.md)
