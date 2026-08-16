# 01 — Phone Se Reach Aur Hard Task (Scenarios 2-3)

## Scenario 2: Phone Se Reach Karo (~15 min)

**Zaroori farq:** OpenClaw aapke laptop pe **design se** rehta hai. Hermes **ulta** bana hai: *"runs
anywhere, lives where you do."* Gateway ek agent, ek memory, **20+ platforms** se reachable.

```text
I'd like to talk to Hermes from my phone. Set up the messaging
gateway with Telegram (my preference), or fall back to Discord or
Signal.
```

Telegram ke liye **@BotFather** se token — chat mein nahi, agent ke bataye tareeqe se paste karo.

**Done jab:** phone se message bhejo, real reply ata hai — **wahi memory, alag surface.**

> **Ehtiyat:** Kuch regions mein Telegram throttled/blocked hai (`api.telegram.org connection failed`
> log mein). Ye delivery problem hai, setup mistake nahi — Signal ya Discord pe switch karo.

> **Asal ghar laptop nahi hai:** Laptop so jata hai; AI Employee ko nahi sona chahiye. Asal ghar ek
> **sasta always-on computer** hai jo aapke phone se reach ho.

## Scenario 3: Hard Task Do, Khud Ki Skill Likhte Dekho (~15 min)

**Zaroori:** Ye scenario OpenClaw mein equivalent nahi rakhta. Hermes ek **closed learning loop** chalata
hai — substantial task ke baad, decide karta hai kya jo hua wo rakhne layak hai — **memory ki tarah, ya
ek skill jo agent khud likhta hai.**

> **Expectation set karo:** Hermes khud skills likhta hai, lekin ye judgment call hai — **pehli dafa
> khud kar hi le, ye zaroori nahi.** Sab se reliable tareeqa: **loop ko steer karo** — task karo, result
> ek dafa fix karo, agent ko batao ye tareeqa save karo.

```text
Let's prove the part that makes Hermes different. I want to give
it a real, slightly fiddly task, the kind I'd have to redo the
same way next week. Tail the Hermes log live.
```

**Achhe first tasks:**
- *"Messy changelog ko clean weekly update mein badlo: theme se group karo, noise hatao, user-facing
  changes se shuru karo."*
- *"Repo ke open issues cluster karo area se, top 5 rank karo agar ignore ho jayein to kitna nuksan
  hoga."*

**Log mein 2 phases dekho:** Pehle, ordinary agent loop (message → model → tool calls → answer). **Phir,
naya hissa:** agent apne kaam ko review karta hai, aur jab worth-keeping lage, `~/.hermes/skills/` mein
ek **skill likhta hai.**

**Confirm karo:**
```text
Did you just save a skill from that? List what's in
~/.hermes/skills/ and show me the new one: its name and the short
description.
```

**Done jab:** Ek skill exist karti hai jo Scenario 3 se pehle nahi thi, aur aap samajhte ho **description**
(install nahi) hi decide karti hai wo agli dafa fire hogi ya nahi.

> **Agar skill nahi bani, ye broken feature nahi hai.** Deterministic lever: task dobara chalao, output
> ek dafa fix karo, agent ko kaho *"save that as the way you want this done every time."* Log dekho —
> ab wo `SKILL.md` khud likhega.

**Skill kaisi dikhti hai:**
```markdown
---
name: weekly-update-from-changelog
description: Turn a raw or messy changelog into a clean weekly
  update grouped by theme, leading with user-facing changes. Use
  when asked for a weekly update, release notes, or "what changed."
---
## When to Use
When asked for a weekly update...
## Procedure
1. Group entries by theme...
## Verification
The summary leads with user-facing changes...
```
> **Zaroori line: `description`.** Vague ho to skill kabhi fire nahi hoti; sharp ho to AI Employee usi
> task pe tezi se behtar hota jata hai bina dobara sikhaye.

---
[⬅ Install Aur Chat](00-install-chat.md) · [Agla: Memory Aur Model-Swap ➡](02-memory-model-swap.md)
