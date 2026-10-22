# Drill 1 — Install & Run `grill-me`

**Time:** 30-90 min · **Tool:** Claude Code or OpenCode

## Setup

1. Ek clean repo mein (Claude Code readers): `mkdir -p .claude/skills` pehle, phir
   `npx skills@latest add mattpocock/skills`.
2. OpenCode readers: `.agents/skills/` directly scan hota hai, extra step nahi — seedha
   `npx skills@latest add mattpocock/skills`.

## Steps

1. Ek feature pick karo jo tum scope karne se taal rahe ho (real, non-trivial).
2. `claude` ya `opencode` kholo, `/grill-me` (ya "use the grill-me skill") invoke karo.
3. Sawalon ka jawab do jab tak agent stop na kare. **Shortcut mat lo.**
4. Questions count karo. Note karo kaunse decisions tumne khud surface nahi kiye hote.

## Done Jab ("What Good Looks Like")

- [ ] Session **15-40 questions** aur **30-90 minute** mein chali (10 se kam = idea chhota tha ya
  tum zyada generously jawab de rahe the; 60 se zyada = agent fishing kar rahi hai, interrupt karo)
- [ ] Tum kam az kam **3 decisions** paraphrase kar sakte ho jo emerge hue jo tumne pehle consider
  nahi kiye the
- [ ] Diagnostic ratio: roughly **1 in 5 questions** ne ek decision surface kiya jo pre-resolved
  nahi tha
