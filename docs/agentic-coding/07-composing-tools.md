# 07 — Composing Claude Code Aur OpenCode

Ek dafa basics comfortable ho jayein, **dono tools ek project pe saath** use kar sakte ho. Har tool ki
apni strength hai.

## Safety Pehle: Git Worktrees

2 sessions same file edit karein to ek doosre ka kaam overwrite kar deta hai. **Git worktree** = project
folder ki smart copy — har ek apni independent workspace mein.

```bash
git worktree add -b my-branch-1 ../myproject-copy1
git worktree add -b my-branch-2 ../myproject-copy2

cd ../myproject-copy1 && claude       # ek terminal mein
cd ../myproject-copy2 && opencode     # doosre terminal mein

cd ../myproject
git merge my-branch-1
git merge my-branch-2
git worktree remove ../myproject-copy1
git worktree remove ../myproject-copy2
```

**File-edit rule:**

| Pattern | Verdict |
| --- | --- |
| 2 sessions ek hi file ek saath edit karein | **Bura** — last write jeetta hai |
| 2 sessions alag directories edit karein | **Acha** — koi conflict nahi |
| Ek session edit-commit kare, doosre ko handoff kare | **Theek** — commit handoff artifact hai |

> **Rule of thumb:** Ek session se shuru karo. Doosri sirf tab add karo jab clearly pata ho kaunsi files
> kis session ki hain.

> Claude Code ke creator khud terminal mein **~5 sessions** chalate hain (har ek apni git checkout mein)
> + 5-10 browser mein — aur **10-20% sessions abandon** kar dete hain. Dono numbers zaroori hain:
> parallelism real leverage hai, dead-end sessions phenkna iski normal cost hai.

## Pattern 1: Plan / Execute Split

1. **Claude Code** plan mode mein — detailed plan banao
2. Plan `docs/plans/my-feature.md` mein save karo
3. **OpenCode** alag worktree mein, cheaper model se: *"read docs/plans/my-feature.md and implement it"*
4. OpenCode plan follow karta hai: edit, tests, formatting
5. (Optional) Claude Code se review karo merge karne se pehle

> **Plan file contract hai** — session loss se bachti hai, architectural decisions encode karti hai, aur
> cheap session ko expensive thinking dobara karne se bachati hai.

## Pattern 2: Cross-Model Review

**Kyun kaam karta hai:** Jis AI ne code likha, wahi review ke liye sab se bura hai — usi ke same blind
spots hain jinhon ne mistakes banayin. **Alag** AI (alag company, alag training data) wo cheezein
notice karega jo pehla miss kar gaya.

1. **Tool A** apni worktree mein code likhta hai
2. **Tool B** (alag model) changes parhta hai, review `docs/reviews/my-feature.md` mein likhta hai — code
   edit nahi karta
3. **Tool A** review parhta hai, decide karta hai kya follow karna hai

**Best results providers mix karne se milte hain.** Claude apna khud ka code review karega to wahi blind
spots miss karega. **GPT Claude ka code review kare (ya ulta)** — alag types ki galtiyan pakarta hai.

## Kab Single Tool Kaafi Hai

Do tools setup extra kaam hai (2 configs, 2 permission lists). **Chhote tasks ke liye, ek tool ek session
mein zyada tez hai.**

**2 tools kab use karo:** Task itni bari ho ke planning/building clearly alag steps hon. Cheap model se
paisa bachana ho. Merge se pehle independent review chahiye ho.

**Baaki sab ke liye, ek tool kaafi hai.**

---
[⬅ Where to Run](06-where-to-run.md) · [⬆ Index](README.md)
