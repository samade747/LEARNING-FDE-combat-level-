# 04 — End-to-End Workflow

Baaqi sab is skeleton se hang hota hai — poori pipeline ki shape, Skills+code mein descend karne se
pehle zehan mein fix karo.

## 4.1 Day Shift / Night Shift Model

2 kism ka kaam. **Human-in-the-loop** kaam ko keyboard par insaan chahiye (alignment, design, taste,
QA). **AFK** ("away from keyboard") kaam sandbox mein unattended chalta hai, subah diff dikhata hai
(implementation, refactors, test fills).

Pipeline alternate karti hai:

```
DAY SHIFT (human-in-the-loop): Idea → Grill → PRD → Issues (vertical slices) → backlog
NIGHT SHIFT (AFK, sandboxed): Implementation Loop (TDD per slice) → Automated Review → review-ready PRs
DAY SHIFT (back to human): Human Review (diff parho) → QA → Merge
                            (QA se naye issues backlog mein wapis ja sakte hain)
```

Har transition ek **handoff** hai. Har handoff ek chhota, durable artifact se mediated hota hai
(CONTEXT.md, PRD, ticket, diff) — **lambi session se nahi**. **Lambi sessions dumb zone mein mar
jati hain; durable artifacts hamesha survive karte hain.** Yehi architectural insight hai jo baaqi
sab kaam karati hai.

## 4.2 Specs-to-Code Ki Limits

Specs useful hain. PRDs specs hain. Issues mini-specs hain. `CONTEXT.md` ek spec hai. Yahan argument
narrow hai: specs ko **poori** workflow ki tarah treat karna — likho, agent se compile karo, code
ignore karo, kuch ghalat ho to spec edit karo dobara compile karo — yeh **tootjata hai**, do wajahon
se:

**Code hi battleground hai.** Code ke andar wo constraints chhupe hain jo spec ne anticipate nahi
kiye — existing module jisse feature integrate hona hai, data shape jo database asal mein return
karta hai. Spec jo respond nahi karti, reality se aur door jati hai har recompilation mein — aur har
round **worse** code deta hai (agent ko longer history of unrooted suggestions inherit hoti hai).

**Specs decay hoti hain.** March mein likhi `gamification-prd.md` July tak ek system ke baare mein
document hai jo exist nahi karta — names badal gaye, boundaries move ho gayi, requirements evolve ho
gayi.

**Sahi model:** specs **handoff artifacts** hain ek stage par, poori system ka source of truth nahi.
Ek-do sessions guide karti hain, phir retire ho jati hain. **Code, tests, aur CONTEXT.md persist
karte hain.**

## 4.3 Vertical Slices Aur Tracer Bullets

§4.1 ka sab se zaroori shape decision: PRD ko issues mein kaise split karo. Temptation **horizontal**
slicing hai (database ek issue, API ek, UI ek) — **yeh ghalat hai**. Horizontal slicing mein, agent
ko koi end-to-end feedback nahi milti jab tak teesra issue na lande; bugs seams par accumulate hote
hain; ek issue baaqi sab ko stall kar sakta hai.

Sahi shape **vertical slice** hai, ek **tracer bullet** (Pragmatic Programmer ki analogy — glowing
rounds jo gunner ko dikhati hain fire kahan ja raha hai). Har issue **har layer** se thinly cut karta
hai jo feature touch karta hai.

```
Horizontal (bad):  Frontend(phase3) -.- API(phase2) -.- Database(phase1)
                    ⇒ phase 3 tak koi integrated feedback nahi

Vertical (good):   Slice1(F→A→D) ~ Slice2(F→A→D) ~ Slice3(F→A→D) ~ Slice4(F→A→D)
                    ⇒ har issue end-to-end path ship karta hai
```

Section 06 (Pipeline in Practice) worked example par vertical slicing dikhata hai, including kaise
slices ke beech dependency graph parallel execution allow karta hai.

---
[⬅ Six Failure Modes](03-six-failure-modes.md) · [Agla: Skills as Encoded Process ➡](05-skills-as-encoded-process.md)
