# 01 — Part 2: Khule Mein Kaam Karna (Concepts 4-5)

## Concept 4 — Agar Likha Nahi Hai, Woh Exist Hi Nahi Karta

Agent apni samajh **poori tarah** us cheez se banata hai jo team **searchable** banati hai: channels,
code, docs, notes. Private messages, hallway conversations, restricted files usay nahi milte. **Agent
ke liye, likha na hua invisible hai.**

Pehli practice cultural hai, technical baad mein: **public mein kaam karo.** Decisions channels aur
docs mein land karti hain, DMs aur bina-notes meetings mein nahi.

**Payoff real hai:** Agent jo team ke decisions parh sakta hai, aisa kaam propose nahi karega jo aap
pehle hi mar chuke ho. Doosri team ke specs parh sakta hai to woh pattern reuse karega jo kaam kar
chuka. Aur agent insan se bohat tez parhta hai, isliye relevant kaam surface kar deta hai jo log miss
kar dete.

**Doosra payoff, ulti taraf se:** Log dekh kar seekhte hain agent kaise achhe se use hua. Public channels
mein sab dekhte hain expert users agent ko kaise direct karte hain — phrasing, scoping, verification —
aur yeh patterns apne kaam mein le jate hain. **Single-player AI skill private windows mein locked
rehti thi; multiplayer AI skill khud phailti hai.**

## Concept 5 — Boundaries Workspace Par, Document Par Nahi

**Ghalat tareeqa:** ek document, ek channel ek waqt mein decide karna — decision fatigue, insan aur
agent dono ke liye.

**Sahi tareeqa:** **kuch clear security boundaries** **workspace** level par khinchi hui (boundary =
information ke around ek deewar, andar kaun hai uska rule). Ek boundary ke andar, context har teammate
tak flow karta hai. **Kam, clear lines zyada, soft lines se behtar hain.**

Yehi wajah hai aapka system of record kaam ata hai — boundary deewar hai; AI Searchable Context wala
searchable store deewar ke andar azaad flow karta hai.

**Exception saaf batao:** Kuch kaam sensitive hai — ek insan, ek agent ke beech. Yeh direct message hai,
ya private apps (claude.ai, Cowork). **Default open, exception ke liye ek narrow lane rakho.**

**Draft karo:**
```text
Draft a working agreement for my team. State what is public by
default. List the few security boundaries we need (no more than a
handful) and who is inside each. List what stays private.
```

**Check karo:** Kya har boundary ek sentence mein bata sakte ho? Nahi to bohat zyada hain.

---
[⬅ Ek Worker Se Team Tak](00-from-one-worker-to-team.md) · [⬆ Index](README.md) · [Agla: Roster Aur Roles ➡](02-roster-and-roles.md)
