# Harness Project 2 — The Lint Hook

**Concept:** 8 (hooks) · **Time:** 30-45 min · **Difficulty:** Easy-Medium

`lint_check.py` ek 30-line, dependency-free linter hai (sirf line-length > 79 check karta hai). Do
hooks wired hain `.claude/settings.json` mein — same script, do alag roles:

- **`PostToolUse`** (har Edit/Write ke baad) — **feedback**. Agent ko turant pata chal jata hai file
  mein lint issue hai, lekin jo edit ho chuka woh undo nahi hota.
- **`Stop`** (jab agent kaam khatam samajhta hai) — **gate**. Jab tak lint clean na ho, session "done"
  hi count nahi hota.

## Setup

```bash
cp -r docs/harness-engineering/projects/lint-hook /path/outside/this/repo/lint-hook
cd /path/outside/this/repo/lint-hook
git init && git add -A && git commit -m "start"
claude
```

## Test It

1. **Feedback dekho:** agent se bolo `bad_code.py mein ek naya function add karo jiski ek line 90
   characters se lambi ho`. PostToolUse hook fire hoga, agent ko lint failure dikhega turant.

2. **Gate dekho:** agent se bolo `is task ko "done" mark kar do abhi, lint clean kiye bina`. Stop
   hook usay rokega jab tak `python lint_check.py .` clean na ho.

3. Manually confirm karo: `python lint_check.py .` khud chalao, dekho exit code kya hai.

## Done jab (self-check)

- [ ] Dono behaviors dekhe: feedback (edit khada raha, sirf warn hua) vs gate (session khatam hi
      nahi hua jab tak fix na hui)
- [ ] Ek line mein farq bata sako: feedback batata hai, gate rokta hai

---
[⬆ Harness Practice Log](../../11-practice-log.md) · [Poori list](../../07-practice-projects.md)
