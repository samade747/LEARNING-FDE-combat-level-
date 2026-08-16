# 00 — Install Aur Chat (Scenario 1)

## Collaboration Pattern

OpenClaw jaisa hi 5-step rhythm: **1)** ek sentence paste karo **2)** agent `AGENTS.md` consult kar ke
plan proposes karta hai **3)** aap approve karte ho, dekhte ho **4)** agent seam pe rukta hai (browser
login, token paste) **5)** aap done ho jab ek observable cheez hoti hai.

> **Universal recovery move:**
> *"Something didn't work. Run `hermes doctor`, read the gateway log, tell me in plain language what
> you see, and propose a fix I can approve."*

## Naye Hire Ki Tarah Treat Karo, Root Account Nahi

Install se pehle, **4 risks, har ek ka sasta guardrail:**
- **Runaway spend** — free tiers use karo, spending limits pehle se set karo
- **Prompt injection** — least access do, *draft* ko *send* pe tarjeeh do jab tak trust na ho
- **Skills mein supply-chain risk** — har community skill ko executable third-party code samjho, source
  parho, version pin karo
- **Destructive actions + leaks** — secrets `~/.hermes/.env` mein jate hain agent ke command se — **token
  kabhi chat mein paste mat karo**

## Pehla Kaam: Hermes Ki Official Skill Install Karo (~1 min)

```bash
npx -y skills add nousresearch/hermes-agent --skill hermes-agent -a claude-code -a opencode
```

Ye `.agents/skills/hermes-agent/` mein jati hai — **alag store** hai `~/.hermes/skills/` se (jahan
Hermes baad mein apni khud ki skills likhta hai). Installer `✓ Installed 1 skill` line print karta hai
— yehi confirmation hai.

## Scenario 1: Employee Install Aur Chatting (~15 min)

**2 raste:** OpenClaw course kiya hai to **migration path** (settings, memories, skills, keys ek step
mein carry hoti hain). Fresh shuru kar rahe ho to agent free **Google AI Studio (Gemini)** key setup
karta hai.

### 1a: Install Aur Setup

```text
I'd like to get Hermes running and chatting back, using a free
model so I don't have to pay or set up anything complicated.
Before you touch anything, walk me through your plan.
```

Agent official installer chalata hai, Gemini provider non-interactively point karta hai. **Sirf ek
cheez jo agent nahi kar sakta: key khud.**

**Aapka hands-on step:** [aistudio.google.com/apikey](https://aistudio.google.com/apikey) pe key
banao, apne terminal mein ek line se save karo:
```bash
printf 'GEMINI_API_KEY=%s\n' 'your-key-here' >> ~/.hermes/.env
```
> **Key file mein daalo, chat mein kabhi nahi.**

**OpenClaw se migrate ho rahe ho?**
```text
I just finished the OpenClaw crash course. Install Hermes, then
migrate my OpenClaw setup across. Do a dry run first.
```
Underneath: `hermes claw migrate --dry-run` — diff dikhata hai, approval pe real migration.

**1a done jab:** Hermes installed, model configured, Gemini key jagah pe hai.

### 1b: Verify Karo, Terminal UI Kholo

```text
Run `hermes doctor` and tell me it's green. Then launch the modern
terminal UI and give me a first task to type that proves the model
and a tool are both working.
```

> **"Green" ka matlab:** `hermes doctor` kuch yellow warnings dikhata hai chahe setup perfect ho — wo
> theek hain. **Jo line green honi zaroori hai wo hai Gemini ki model + auth line.**

**Done jab:** `hermes doctor` green hai, **aur** TUI mein specific task ka real, sahi jawab mila (tool
ne asal mein fire kiya, training-data guess nahi).

> **Ehtiyat: "Blank Slate" mode is course ke liye avoid karo** — memory capture off kar deta hai, Scenarios
> 3, 4, 5 fire nahi karenge.

---
[⬅ Index](README.md) · [Agla: Phone Aur Hard Task ➡](01-phone-hard-task.md)
