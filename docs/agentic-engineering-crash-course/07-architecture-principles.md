# 07 — AI-Friendly Codebases Ke Architecture Principles

Workflow aur codebase alag nahi hain: architecture jitni clean hogi, agent **usi ke andar** utna
behtar perform karega. **Architecture ab sirf apna goal nahi — tumhari AI workforce ka input hai.**

## 7.1 Deep Modules Over Shallow Modules

Module **deep** hai jab uska interface chhota ho aur uske peeche bohot behavior ho. **Shallow** hai
jab interface aur implementation roughly same size ke hon.

Agent ke liye farq **decisive** hai. Shallow codebase mein agent kai chhoti files ke beech pairwise
dependencies trace karta hai — signal-to-noise per token degrade hota hai. Deep codebase mein agent
**ek interface parhta hai aur boundary ko trust karta hai.** Tests interface par baithte hain.
Behavior andar add ho sakta hai bina callers disturb kiye.

**Shallow version** (jo agent bina architectural guidance ke likhta hai): `gamification/index.ts` 9
top-level exported functions (`awardPoints`, `totalPoints`, `recordStreakActivity`, `computeLevel`,
`validateAntiCheat`, `backfillHistorical`, ...) — har ek kahin se bhi callable, har ek chup-chaap
doosron par depend karta hai. **Bug jo yahan ho sakta hai:** caller `validateAntiCheat` call karna
bhool sakta hai aur silently system corrupt kar sakta hai.

**Deep version** (§6.4 se): `GamificationService` class, sirf **3 methods**
(`awardLessonCompletion`, `totalPoints`, `currentStreak`). Andar wahi 9 concerns exist karte hain,
lekin **interface nahi hain.** Caller `validateAntiCheat` ko reach hi nahi kar sakta — wo
`awardLessonCompletion` ke andar chhupi hai, automatically call hoti hai. **Sahi cheezein chhupana
hi deep module ka poora kaam hai.**

> **Heuristic:** Agar tumhare IDE ka Outline view ek module ke liye uske public interface se lamba
> hai, module shallow hai. **Deepen karo.**

## 7.2 Test at the Interface

§7.1 ka corollary. **Tests module interfaces par baithte hain, internal functions par nahi.** Internal
function par test implementation ko pin karta hai — refactoring internals test todti hai chahe
externally visible behavior correct ho. Interface par test **behavior** ko pin karta hai — internals
freely badal sakte hain jab tak contract hold karta hai. Yehi `tdd` Skill default enforce karti hai.

## 7.3 Design the Interface, Delegate the Implementation

**Senior engineer ke liye agents ke sath sab se zaroori habit.**

Tum decide karte ho module kya **expose** karta hai (contract, names, invariants) — yeh har caller ko
affect karta hai, architecture shape karta hai, taste+poori system zehan mein chahti hai. Agent decide
karta hai contract **kaise satisfy** hota hai (internal data structures, helper placement) — yeh
sirf ek module ke andar affect karta hai, mistakes recoverable hain.

Yehi **gray box principle** hai. Bahar se module **fully specified** hai (interface visible,
internals invisible-by-design). Andar se agent free hai excellent kaam karne ke liye, sirf interface
contract se constrained. **Senior engineer ek million-line codebase ka architectural map zehan mein
rakh sakta hai kyunke map mein sirf interfaces hoti hain.**

Yehi Failure 5 (brain saturation) ko tractable banata hai. Tum har line nahi parh sakte — wo raasta
burnout tak jata hai. Tum **module map** zehan mein rakh sakte ho aur har interface change carefully
parh sakte ho. Interface change-set chhota hai; module-ke-andar change-set bara hai. **Chhote set par
attention concentrate karna hi scale karta hai.**

## 7.4 The `improve-codebase-architecture` Skill

Codebases time ke sath shallow ki taraf drift karte hain, especially agents ke sath. Fix: **periodic
deepening pass.**

Khud Karpathy, frontier models ke sath kaam karte hue, kehta hai: *"Kabhi kabhi mujhe halka heart
attack sa hota hai kyunke code bohat bloaty hai, copy-paste bohat hai, awkward abstractions brittle
hain. Chalta hai, lekin bohat gross hai."* Yeh deep model ki failure nahi — model "code chalta hai"
wale verifiable circuit ke andar perform kar raha hai, "code well-designed hai" ke corresponding
reward ke bina. **Deepening pass wo reward supply karta hai jo labs ne nahi diya.**

Skill: `improve-codebase-architecture` — codebase walk karta hai, shallow-module candidates dhoondta
hai, numbered list surface karta hai (kaunsi files collapse hongi, naya interface kya hoga [3-5
methods], kya behavior andar move hoga). **Koi change nahi karta** — highest-value candidate ko RFC
issue ki tarah kholta hai, type AFK. Weekly run ek deepening RFC produce karta hai — same Kanban
board mein jata hai, same TDD-on-vertical-slices loop se implement hota hai. **Codebase schedule par
healthy hoti hai, accident se nahi.**

---
[⬅ Pipeline in Practice](06-pipeline-in-practice.md) · [Agla: Working Vocabulary ➡](08-working-vocabulary.md)
