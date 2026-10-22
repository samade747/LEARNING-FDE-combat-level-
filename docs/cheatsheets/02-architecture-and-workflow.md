# 02 — The 4-Layer Architecture & Daily Workflow (Panels 8-9)

Yahan cheatsheet zoom-out karti hai: pehle poori architecture ek diagram ki tarah dikhati hai, phir
ek typical din ka workflow pattern.

## Panel 8: 🏗️ The 4-Layer Architecture

Panels 2-7 mein jo pieces alag-alag dekhe (CLAUDE.md, Skills, Hooks, Agents), wo asal mein ek **stack**
hain — char layers, neeche se oopar:

- **L1 — CLAUDE.md** — persistent context aur rules (sab se neeche, foundation)
- **L2 — Skills** — auto-invoked knowledge packs
- **L3 — Hooks** — safety gates aur automation
- **L4 — Agents** — subagents jinki apni context hoti hai

**Important note:** har layer apne neeche wali layer **par** banti hai. Isliye shuruaat hamesha L1
(CLAUDE.md) se karo, aur jab actual patterns emerge hon (jab bar-bar wahi masla dikhe) tab aagay ki
layers add karo — pehle se hi char layers set karne ki koshish mat karo.

## Panel 9: 🔄 Daily Workflow Pattern

Yeh ek typical session ka 8-step loop hai:

1. `cd project && claude` — session shuru karo
2. **Shift+Tab** → Plan Mode mein jao
3. Feature ka intent describe karo (kya chahiye, kyun chahiye)
4. **Shift+Tab** → Auto Accept mode mein switch karo
5. `! git status` — inline bash (`!` prefix se seedha shell command chalao, Claude se nikal ke)
6. `/compact` — jab context lamba ho jaye, compress karo
7. **Ctrl+B** — current task ko background mein bhej do
8. **Esc Esc** — zaroorat pare to last turn rewind karo

Yeh pattern roz ka "rhythm" hai: plan karo, execute karo, inline check karo, context manage karo,
parallel kaam background mein chalao, aur ghalti pe wapas jao.

---
[⬅ Prev](01-skills-hooks-permissions.md) · [Next ➡](03-models-ci-mcp.md)
