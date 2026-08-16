# 02 — Voice Aur Memory Customize Karna (Scenario 4)

AI Employee ka behavior `~/.openclaw/workspace/` mein markdown files se ata hai:

- **SOUL.md** — personality/tone (kaise baat karta hai)
- **IDENTITY.md** — apna naam/role (kaise introduce karta hai)
- **USER.md** — aapke baare mein kya jaanta hai
- **MEMORY.md** — durable facts jo channels ke aar-paar commit hote hain

> **Ehtiyat:** Har file **lean rakho** — har line context cost hai jo agent har turn pe pay karta hai.
> Aur baad mein **churn mat karo** — ye har reply ki shape banate hain.

> **Zaroori:** Kisi bhi workspace file edit karne ke baad, **`/reset`** bhejo (paired channel se, ya
> dashboard se) — nahi to running session purani cached system prompt use karta rehta hai.

## 4a: SOUL.md — Voice Badlo

```text
Take a look at SOUL.md and suggest three small changes that would
make replies more direct and less hedgy. Show me the diff first.
```
Edit ke baad `/reset`, phir *"How are you today?"* poocho. **Done jab:** tone visibly alag ho.

## 4b: IDENTITY.md — Naam Do

```text
Give it a name and a role. I'd like it to introduce itself as
"Atlas, my research assistant" (or pick whatever feels right).
```
`/reset`, phir *"Who are you?"* poocho. **Done jab:** naya naam/role bataye.

## 4c: USER.md — Aapke Baare Mein Sikhao

```text
Teach it about me. Add my full name, my role, my timezone, and
the three topics I most often need help with.
```
`/reset`, phir *"What should I prioritize this afternoon?"* poocho. **Done jab:** timezone/topics factor
mein ayein, generic advice nahi.

## 4d: MEMORY.md — Channels Ke Aar-Paar Commit Karo

Pehli 3 files voice shape karti hain. **MEMORY.md alag hai** — sirf main session mein load hoti hai,
isliye jo channels ke aar-paar chahiye wo **deliberately commit** karna padta hai.

**4 steps (real, in-flight cheez use karo — "name" jaisi stable fact nahi):**

1. **Paired channel se:** *"Quick context: main [real project] Friday tak finish kar raha hoon. Hold
   onto this."* Phir turant: *"Main Friday tak kya finish kar raha hoon?"* — jawab milta hai (session +
   channel memory, automatic)
2. **Dashboard chat se** (alag session): wahi sawal — **usay pata nahi.** Ye **wall hai:** channel
   memory per-channel hai, shared nahi
3. **Wapas paired channel se:** *"Commit my Friday goal to your long-term memory."* Agent `MEMORY.md`
   banata hai (pehli commit tak exist nahi karti)
4. **Dashboard se dobara** (`/reset` pehle): wahi sawal — **ab pata hai.** Deliberate commit ne wall
   cross kar li

**Done jab:** Step 4 succeed ho. AI Employee ab aapki tarah bolta hai, sahi naam se introduce karta hai,
aapke context ko jaanta hai, aur channels ke aar-paar yaad rakhta hai kyunke kuch **deliberately commit**
hua tha, sirf cache nahi.

## 4e: Identity Backup Karo

Workspace **hi** aapka AI Employee hai. Laptop mar jaye to sab kho jayega — isay dotfiles ki tarah treat
karo.

```text
Back up my agent's workspace at ~/.openclaw/workspace/ to a
private GitHub repo so I don't lose it if my laptop dies.
```

**Done jab:** Private repo GitHub pe hai, workspace pushed hai, aur aapke paas recovery one-liner save
hai (note app/password manager mein). **Ab identity ek laptop wipe survive kar sakti hai.**

---
[⬅ Channel Aur Delegate](01-channel-delegate.md) · [Agla: Skill Aur Tool Se Extend Karna ➡](03-extend-skill-tool.md)
