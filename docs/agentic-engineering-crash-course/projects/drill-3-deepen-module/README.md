# Drill 3 — Deepen a Module

**Time:** 30 min - 2 hours · **Tool:** Claude Code or OpenCode, `improve-codebase-architecture` Skill

## Steps

1. `improve-codebase-architecture` ek codebase par chalao jo tum achhi tarah jaante ho.
2. Highest-value candidate pick karo.
3. **Implement mat karo abhi** — paper par naya interface sketch karo (3-5 method signatures, zyada
   nahi).
4. Naye interface ki surface area compare karo purane se (public symbols sum, un files ke jo
   collapse hongi).

## Done Jab ("What Good Looks Like")

- [ ] Genuine deepening typically **5-15 chhoti modules** ko **ek deep module** mein collapse karti
  hai
- [ ] Public-symbol ratio (old:new) **3:1 ya zyada** hai (agar 1:1 ke qareeb hai, candidate asal
  mein shallow nahi tha — doosra pick karo)
