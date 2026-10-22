# 05 — Skills as Encoded Process

Har cure ko reusable, agent-loadable artifact ki tarah encode hona chahiye — wahi artifact **Skill**
hai.

> **Principle vs Instance.** 5 principles pipeline chalate hain: grilling, PRD-synthesis, vertical-
> slicing, TDD, deepening. Har ek ka current best-in-class implementation hai (kisi ka skill pack).
> Implementations evolve hote hain; **principles nahi.** Jab agla behtar `grill-me` aaye, instance
> swap karo — grilling principle nahi badalta.

## 5.1 Skill Kya Hai, Kya Nahi

> **Skill (n.):** ek teachable capability jo ek unit ki tarah bundled hai (instructions+resources),
> environment mein rakhi jati hai, context window mein **sirf relevant hone par** load hoti hai.
> Harness mein progressive disclosure ki unit.

Skill wo hai jo agent **parhta** hai; **Tool** wo hai jo agent **call karta** hai. Skill keh sakti
hai "jab user deploy maange, `bash deploy.sh` chalao" — Skill prose hai, `bash` tool hai.

Skill **on-demand** hai. `AGENTS.md` har turn load hoti hai, har request par token cost deti hai;
Skill sirf tab load hoti hai jab agent decide kare relevant hai. Jo bhi har turn context mein nahi
hona chahiye, Skill mein jana chahiye, AGENTS.md mein nahi.

Skill **portable** hai. Wahi `SKILL.md` Claude Code aur OpenCode dono mein chalta hai bina change ke.

## 5.2 Skills Kahan Rehti Hain

Dono harnesses session start par well-known directories scan karte hain, `SKILL.md` ka YAML
frontmatter parhte hain. `skills` CLI community pack `.agents/skills/` mein install karta hai.

**Claude Code** `.claude/skills/<name>/SKILL.md` scan karta hai (`.agents/skills/` nahi). Pehle
`mkdir -p .claude/skills` chalao, phir `npx skills@latest add mattpocock/skills`. **OpenCode**
`.agents/skills/` directly scan karta hai — extra step nahi chahiye. Ek `SKILL.md` Claude Code ke
liye likhi, kisi bhi location mein drop karo, **bina change ke chalti hai.**

## 5.3 Ek SKILL.md Ki Anatomy

`SKILL.md` ke 2 hisse: YAML frontmatter (metadata jo harness scan karta hai) aur markdown body
(instructions jo agent load par parhta hai).

Matt Pocock ke pack ka most-starred Skill, `grill-me`, poora yahan hai (7 lines body):

```markdown
---
name: grill-me
description: Interview the user relentlessly about a plan or design until reaching shared understanding...
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding.
Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.
For each question, provide your recommended answer.

Ask the questions one at a time.

If a question can be answered by exploring the codebase, explore the codebase instead.
```

Yehi poori Skill hai, aur `grill-me` ek pack mein **sab se zyada use hone wala** skill hai jisne
tens of thousands GitHub stars khinche. **3 observations generalize hoti hain:**

1. **Skills lambi hone se impactful nahi banti.** Yeh ~3 sentences hai aur poori planning conversation
   transform kar deti hai.
2. **Frontmatter real kaam karta hai.** Harness agent ko `description` dikhata hai, body nahi —
   isliye description specific hona zaroori hai ("Use when user wants to stress-test a plan, get
   grilled on their design, or mentions 'grill me'" > "for grilling").
3. **Body agent ko second person mein address karti hai** — "Interview me relentlessly." Direct,
   declarative, no hedging.

**Principle:** process encode karo, jawab encode mat karo.

## 5.4 Panch Daily Principles (Aaj Ke Best Skills)

| Stage | Skill | Kya karti hai |
| --- | --- | --- |
| Idea → Aligned design concept | `grill-me` | Socratic interview jab tak alignment na ho |
| Aligned concept → Destination doc | `to-prd` | Conversation ko PRD mein synthesize karti hai (user stories, implementation decisions, modules list) |
| PRD → Backlog of issues | `to-issues` | PRD ko vertical-slice tickets mein todti hai, explicit blocking relationships ke sath |
| Issue → Implemented slice | `tdd` | Red-green-refactor, ek slice par ek waqt |
| Codebase health, ongoing | `improve-codebase-architecture` | Shallow modules dhoondti hai, deepenings propose karti hai, RFC issue kholti hai |

> ⚠️ **Skill loading tumhare model ki instruction-following par depend karti hai.** Pipeline ka
> architecture model-agnostic hai, **operational reliability nahi.** Frontier-class model
> (Claude Sonnet/Opus, GPT-5-class, Gemini 2.5 Pro) description-match se Skill load karta hai,
> multi-step body order mein execute karta hai. Economy/local model (Haiku-class, Llama-70B) mein
> yeh behaviors degrade hote hain. Cure wahi hai jo §2.3 mein tha: weaker model par **zyada
> scaffold karo** — Skills explicitly naam se invoke karo, bodies short/declarative rakho, model
> kya **nahi** karna chahiye yeh bhi state karo.

**6th Skill:** `grill-with-docs` — same Socratic interview, lekin `CONTEXT.md` aur ADRs inline update
karti hai jaise decisions crystallize hon. Greenfield design ke liye `grill-me`, repo already
`CONTEXT.md`/ADRs rakhti ho to `grill-with-docs`.

> **Apni khud ki Skills pehle banao; doosre ka pack baad mein.** Best Skill wahi hai jo **tumhari**
> team ka process capture kare. Stack own karna (har Skill parh sakna) observability deta hai jab
> kuch ghalat ho.

---
[⬅ End-to-End Workflow](04-end-to-end-workflow.md) · [Agla: Pipeline in Practice (Worked Example) ➡](06-pipeline-in-practice.md)
