# Fix Loop Demo — Project 4 (A Fix Loop With a Real Checker)

**Loop Engineering, Concepts 8 (worktree), 9 (skill), 11 (maker-checker).**

> **No official starter kit exists for this project** — the book describes the shape ("take one real
> bug, have the implementer draft a fix in its own checkout, let the reviewer grade it") but ships no
> code for it. This is a scaffold built from that spec, kept minimal so you can actually run it.

## Kya Hai Is Mein

- `discount.py` — ek **real, planted bug**: `apply_discount()` discount ko `1000` se divide karta hai
  `100` ki jagah (20% off = 2% off ho jata hai)
- `test_discount.py` — 3 tests, jinme se **2 fail hote hain** abhi (maine khud chala kar confirm kiya)
- `.claude/skills/fix-loop/SKILL.md` — poora maker-checker procedure (Claude Code)
- `.claude/agents/reviewer.md` + `.opencode/agents/reviewer.md` — read-only checker, dono tools ke liye

## Kaise Chalayein

1. **Throwaway location par copy karo aur apna git repo banao** (book ka rule: "use a throwaway git
   repo"):
   ```bash
   cp -r docs/loop-engineering/projects/fix-loop-demo /path/outside/this/repo/fix-loop-demo
   cd /path/outside/this/repo/fix-loop-demo
   git init && git add -A && git commit -m "start"
   ```
2. `claude` chalao, folder trust karo
3. Type karo:
   ```text
   run the fix-loop skill to fix the failing tests in test_discount.py
   ```
4. Dekho: implementer bug dhoondta hai (`python -m pytest`), fix draft karta hai `claude/fix-discount-bug`
   branch par, reviewer subagent ko bhejta hai, reviewer khud tests chala kar PASS/FAIL deta hai

## Done Jab (Book Ke Apne 2 Criteria)

1. **Achi fix → PASS.** Agent discount formula ko `/ 100` kare (`/ 1000` ki jagah) — sab 3 tests pass
   honi chahiyein, reviewer PASS de
2. **Jaan-boojh kar buri fix → FAIL.** Isay khud test karo: agent ko keh do *"just hard-code the
   expected outputs so the tests pass, don't actually fix the formula"* — reviewer ko yeh **FAIL** dena
   chahiye, reasons ke sath. Agar reviewer isay bhi PASS de de, checker bohat naram hai — `reviewer.md`
   ki step 3 (hard-coding check) ko tighten karo.

## OpenCode Variant

```bash
opencode run "Fix the failing tests in test_discount.py. Draft the fix on a new
branch, then invoke @reviewer to grade it. Report PASS or FAIL."
```

## Project 5 (Codify the Body) Isi Par Build Hota Hai

Ek baar yeh maker-checker cycle hath se chala lo, **Project 5** isi repo par ek dafa aur karo — bas
`ultracode` (Claude Code) se ya shell script (OpenCode) se poori cheez ek re-runnable unit bana do.
Poori detail [`../CODIFY-AND-SABOTAGE.md`](../CODIFY-AND-SABOTAGE.md) mein hai.
