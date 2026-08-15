# 02 — Rules File: CLAUDE.md / AGENTS.md

## Concept 8: CLAUDE.md / AGENTS.md, Sahi Tareeqe Se

Ek file jo AI **har conversation ke shuru mein** parhta hai — project ke liye permanent instructions.

- **Claude Code:** `CLAUDE.md`
- **OpenCode:** `AGENTS.md` (agar `CLAUDE.md` bhi ho aur `AGENTS.md` na ho, OpenCode `CLAUDE.md` parh
  leta hai)

`/init` chalao, AI project scan kar ke file banata hai — **wo bohat lambi hogi. Aapka kaam: jo zaroorat
nahi wo delete karna.**

**Sab se badi ghalti:** Isay poora manual samajhna — architecture, coding rules, sab kuch. **AI ye file
har single message pe parhta hai.** Bari file slow karti hai, conversation space waste karti hai.

**Chhota rakho.** Sirf wo likho jo AI files dekh kar khud pata nahi laga sakta:

```markdown
# Project: my-app

## Stack
Next.js 14, TypeScript, Postgres, Drizzle ORM.

## Critical rules
- Never edit files in `src/generated/`. They're rebuilt by codegen.
- See @docs/conventions.md for naming and folder rules.
```

> **Claude Code:** `@filename` reference hone pe **automatically** load hota hai. **OpenCode:** ye
> automatic nahi — ya to AGENTS.md mein likho "jab zaroorat ho tab load karo", ya `opencode.json` mein
> `instructions` array mein list karo.

**Ye sirf code ke liye nahi.** Writing/research/blog projects ke liye bhi wahi structure kaam karta hai.

**Har line ka test:** *"Agar ye line hata doon, kya AI galti karega?"* Nahi to delete karo. Aapko batana
nahi parega project Python use karta hai (files `.py` mein khatam hoti hain, AI dekh sakta hai). Lekin
batana **parta** hai "published/ folder kabhi edit mat karna" — AI ko ye kabhi khud pata nahi chalega.

**Ghalti hone pe rule add karo, pehle se nahi.** Anthropic ka apna team yahi karta hai — Boris Cherny
(Claude Code creator) ka file **~2,500 tokens** hai, saal bhar baad bhi. **Chhoti file, har ghalti se ek
earned line.**

### Doosri Aadhi Method — Prune Karo

Sirf lines add karna kaafi nahi — **contradictory rules jama ho jati hain**. July 2026 mein Claude Code
team ne apne system prompt ka **80%+ hataya**, koi performance loss ke bagair. Rule jo **forbid** karti
thi, usay rule jo **standard describe** kare se replace kiya:

| Purani Rule | Nayi Rule |
| --- | --- |
| "Kabhi comments mat likho. Multi-paragraph docstrings kabhi nahi." | "Surrounding code jaisa likho: uski comment density match karo." |

> **2 aadatein, ek nahi:** Ghalti earn kare to line add karo, **aur** model ko ab zaroorat na ho to line
> delete karo. Har chand mahine, poori file dobara Concept 8 test se guzaro.

**Model ki capability ke hisaab se constrain karo:** Frontier model — thin, trust-heavy rules file.
Cheap/local model (OpenCode) — deleted lines wapas add karni parti hain. **Constrain jitna karo, model
ki capability ke ulta.**

**`/doctor`** (Claude Code) — file ko review kar ke batata hai kya cut karna hai. OpenCode mein
equivalent nahi — manual review.

---
[⬅ Context Management](01-context-management.md) · [Agla: Personalizing ➡](03-personalizing.md)
