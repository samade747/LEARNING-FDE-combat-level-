# 00 — Collaboration Pattern + Install (Scenario 1)

## Poora Course Kaise Kaam Karta Hai

Aap ek chhota folder download karte ho, apne general agent (Claude Code, OpenCode, Cowork, OpenCowork)
ko dete ho, aur 6 scenarios se guzarte ho. Agent folder parhta hai, OpenClaw install/chalata hai, aapka
phone connect karta hai, naye skills uthata hai, apna "brain" customize karta hai, aur ek task schedule
karta hai jo bina aapke chale.

**3 actors:** aap, general agent, OpenClaw. Har scenario **5-step rhythm** use karta hai:

1. **Aap ek sentence paste karte ho** — brief hai, script nahi
2. **Agent `AGENTS.md` consult karta hai** aur plan propose karta hai — konse commands chalayega,
   kaunse decision points hain
3. **Aap approve karte ho aur dekhte ho** — agent install/config/restart karta hai, live log dikhata hai
4. **Agent seam pe rukta hai** — sirf aap kar sakte ho: Gemini key lena, phone se QR scan karna, Google
   OAuth click karna
5. **Aap "done" ho jab ek observable cheez hoti hai** — real reply, message ka jawab, ek file disk pe

> **Universal recovery move:** Kuch bhi galat ho, ye paste karo:
> *"Something didn't work. Read the gateway log, tell me in plain language what you see, and propose a
> fix I can approve."*

**Download:** `openclaw-with-general-agents.zip` — sirf 2 files: `AGENTS.md` (~600-line operational
reference) aur `CLAUDE.md` (1 line: `@AGENTS.md`). Unzip karo, terminal kholo, `claude` ya `opencode`
chalao.

**Confirm karo brief load hui:** *"What can you do for OpenClaw?"* Agar specific OpenClaw work (install
probes, channels, brain files) naam le, loaded ho. Generic AI capability baat kare to relaunch karo.

## Scenario 1: Employee Install Aur Chatting (~15 min)

**Goal:** OpenClaw laptop pe chal raha ho, Gemini free tier pe setup ho, dashboard mein "hi" ka reply
mile.

**Prompt 1 — plan mango:**
```text
I'd like to get OpenClaw running on my laptop and chatting back
through Gemini's free tier. Before you touch anything, walk me
through your plan in plain language.
```
Agent 2 jagah aapko chahiye ga: [aistudio.google.com](https://aistudio.google.com/app/api-keys) se free
Gemini key lena, aur system changes se pehle confirmation.

**Prompt 2 — approve karo:**
```text
Plan looks good. Go ahead step by step, and tell me what you see
at each step. When you need my Gemini key, pause and tell me how
to give it to you safely.
```

**Prompt 3 — verify karo:**
```text
Now do your own end-to-end check first, then open the dashboard
for me so I can try it from the browser too.
```

**Done jab:** Agent ki apni CLI check real reply de, **aur** browser dashboard bhi `hi` type karne pe
reply de. Dashboard footer `google/gemini-3.5-flash` dikhaye (agar `pro-preview` dikhaye, agent ko batao
— free tier pe wapas switch karega).

**Underneath, ~5 commands hain** (aap khud kabhi type nahi karte):
```bash
npm install -g openclaw@latest
openclaw onboard --install-daemon
openclaw gateway status
openclaw dashboard
openclaw doctor
```
Sab kuch `~/.openclaw/` mein rehta hai: config `openclaw.json` mein, Gemini key `credentials/` mein,
brain `workspace/` mein.

---
[⬅ Index](README.md) · [Agla: Channel Aur Delegate ➡](01-channel-delegate.md)
