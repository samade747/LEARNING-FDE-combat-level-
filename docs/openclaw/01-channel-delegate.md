# 01 — Channel Pair Aur Delegate (Scenarios 2-3)

## Scenario 2: Phone Se Channel Pair Karo (~15 min)

**Goal:** Phone se "hi" bhejo, AI Employee se reply wapas ao.

```text
The model answers in the dashboard. Now I'd like to talk to my AI
Employee from my phone. Walk me through pairing WhatsApp
(preferred), or fall back to Telegram or Discord.
```

**WhatsApp ke liye:** **doosra number + WhatsApp Business** use karo, apna personal account nahi
(underlying library unofficial hai, Meta personal accounts ban kar sakta hai). Telegram → BotFather.
Discord → Developer Portal + 3 privacy intents.

> **Ek cheez jo agent nahi kar sakta:** Login step ka QR code/token prompt terminal-based UI use karta
> hai jo agent ke shell tool se render nahi hoti. Agent ruk kar aapko naya terminal window kholne ko
> kahega — QR scan karo (WhatsApp Business → Settings → Linked Devices) ya bot token paste karo. Agent
> ko *"linked"* batao.

**Done jab:** Phone se `hi` bhejne pe real reply ata hai.

> **Scenario 3 ke liye carry-forward:** Aapka phone ab ek **authenticated path** hai OpenClaw service
> tak — real trust jo aapke phone ne di. Isay credential ki tarah treat karo, share mat karo.

## Scenario 3: Real Kaam Delegate Karo, Loop Dekho (~10 min)

**Concept:** "AI Employee" ko chatbot se alag karta hai **agent loop**: real task ata hai, agent decide
karta hai kaunse tools chahiyen, call karta hai, result parhta hai, jawab banata hai.

```text
The channel works. Let's prove this is more than a chatbot. I'd
like to send a task from my phone that needs the agent to actually
go do something. Set up a live view of the gateway log.
```

**Real task ka example (apni zindagi se, tutorial demo nahi):**
- *"Competitor X apna entry plan ka kya charge karta hai? Ek paragraph summary + source URL do."*
- *"Ye article URL parho, mere industry ke liye 3 sab se zaroori claims batao"*

**Log stream mein 6 lines scroll karti hain:**
1. Inbound message channel pe arrive hoti hai
2. Model call — agent loop Gemini ko message bhejta hai
3. Tool call — agent jo tool zaroori ho invoke karta hai
4. Tool result wapas ata hai
5. Doosri model call — result summarize karne ke liye
6. Outbound message — reply channel pe wapas

**Done jab:** Aap ne ye 6-line shape scroll hote dekhi ho aur reply phone pe aya ho. **Yehi loop hai.**
Agli scenarios mein jo bhi add karoge (skill, tool, scheduled task) — sab isi loop mein aur tools/triggers
add karte hain.

---
[⬅ Install](00-collaboration-install.md) · [Agla: Identity Customize Karna ➡](02-customize-identity.md)
