# 06 — Where to Run, Aur Kya Rakhein

## Concept 13: Terminal, IDE, Ya Desktop?

**Claude Code:** terminal, VS Code/JetBrains plugin, desktop app (Mac/Windows, parallel sessions ke
liye), web, mobile, cloud-hosted sessions. **OpenCode:** terminal (TUI flagship), desktop app (beta),
VS Code extension, web via SDK, GitHub agent/Slack bot.

**Strong recommendation:** **terminal ya IDE plugin se shuru karo.** Ek dafa samajh ao ke andar kya ho
raha hai (konsi files parhta, konse commands chalata), har doosra interface **transparent wrapper** ban
jata hai. Heavily abstracted UI se shuru karoge to debug karna mushkil hoga.

## Concept 14: Personal Context Library Aahista Banao

Alag alag projects mein wahi cheezein baar baar likhte ho (code style, commit conventions). **Copy-paste
band karo** — shared parts ko home config mein rakho:

```markdown
<!-- ~/.claude/CLAUDE.md — har project mein load hoti hai -->
@~/.claude/style/typescript.md
@~/.claude/style/commits.md
```

```json
// ~/.config/opencode/opencode.json
{ "instructions": ["style/typescript.md", "style/commits.md"] }
```

Same idea skills ke liye — `~/.claude/skills/` (OpenCode bhi parhta hai) mein rakhi skill har jagah
available.

> **Ek saath sab mat banao.** Ek ek kar ke add karo, sirf jab zaroorat pare. Style guide add karo jab AI
> galat style mein likhe. Commit skill add karo jab 3rd dafa wahi instructions type karo.

## Concept 15: Memory, Basics Se Aage

Zyada tar logon ke liye, sessions resume karna aur achi rules file kaafi hai. Agar fresh conversation ke
baad bhi yaad rakhni ho:

- **`notes/` folder** — task khatam hone pe short summary likhwao. Simple, no setup
- **Memory MCP server** — conversations ke darmiyan save/recall karta hai
- **Search across old conversations** — tool ke docs check karo

**2 craft rules jo notes folder ko mahinon baad kaam ka banate hain:**
- **Absolute dates, hamesha** — *"kal humne Redis choose kiya"* 6 hafte mein bekaar hai. *"2026-07-14:
  Redis choose kiya Postgres ke bajaye, kyunke..."* kabhi expire nahi hoti
- **Decisions over narration** — *"auth pe kaam kiya"* kisi kaam ka nahi. *"Auth: token refresh retry
  helper use kare"* agli session ka behavior badalta hai — **yehi test hai ke ek line likhne layak hai
  ya nahi**

**Tools ab khud simple version karte hain:** Claude Code ka **auto memory** apni chhoti notes khud
likhta hai (aapki corrections/preferences), har session shuru mein reload karta hai. Anthropic isay ab
rules file mein manually memory likhne ki purani aadat ki jagah **replace** treat karta hai.

---
[⬅ Complete Worked Example](05-worked-example.md) · [Agla: Composing Tools ➡](07-composing-tools.md)
