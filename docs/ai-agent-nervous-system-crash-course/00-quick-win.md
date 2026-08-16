# 00 — 15-Minute Quick Win

Setup ek dafa karo — Quick Win aur Part 4 dono isi base par chalte hain.

## Kya Banega

- Base khula, skills/tools setup
- Fresh Neon database (`customers`, `audit_log` tables)
- Chota worker chalta hua, dashboard ke sath
- Ek run jo **wait karte waqt zero compute** use kare
- Ek run jo jaan-boojh kar todo, phir retry dekho — **jo kaam ho chuka woh dobara nahi hota, sirf jo
  toota woh dobara chalta hai**
- Wahi function, ab ek **real agent** greeting likhta hua

## Setup Steps

**1. Base download karo, kholo.**

**2. Base prep karo (~3 min):**
```text
Read AGENTS.md, then get this base ready: install the Skills it lists,
copy .env.example to .env, tell me what you need to bring Neon and
Context7 MCP servers online.
```

**3. Inngest dev server chalao, gate confirm karo (~2 min):**
```bash
npx inngest-cli@latest dev
```
Dashboard `http://127.0.0.1:8288` par ata hai. Agent restart karo, phir:
```text
List the Neon tools and the inngest-dev tools you can see.
```

**4. Store banao, connection string lo (~3 min):**
```text
On a fresh Neon project, create two tables: customers (id, email,
tier) and audit_log. Write the connection string into .env as
DATABASE_URL.
```

**5. Pehla durable function banao (~3 min):**
```text
Write one tiny Inngest durable function (greet-customer, triggered by
demo/greet event) that composes a greeting in one step.run, sleeps 15
seconds with step.sleep, then composes a farewell in a second
step.run. Serve from FastAPI on port 8000 with auto-reload.
```

**6. Trigger karo, sleep step ko zero-compute par dekho:**
```text
Send a demo/greet event with name Sara using inngest-dev send_event.
```
15 second tak, code mein kuch nahi chalta — dev server resume time hold karta hai. **Yehi durable wait
ka poora point hai: zero compute.**

**7. Step todo, retry dekho memoization ke sath (payoff):**
```text
Make the farewell step raise an error on purpose.
```
Dashboard mein: greeting step **1 attempt** par khara, farewell step **kai attempts** climb karta hai
backoff ke sath. **Complete hui greeting ek dafa pay hui, har retry par nahi.**

**8. Fix karo, real agent se badlo:**
```text
Replace the hardcoded greeting with a one-line call to a minimal
hello-world agent built on the OpenAI Agents SDK, still inside the
same step.run.
```

**Done jab:** Run complete ho aur greeting agent se aayi ho, hardcoded string se nahi. **Yeh poora course
ek sentence mein hai:** AI agent, event se jagaya, nervous system ke andar durably chalta, crash se
survive karta.

## Common Problems

1. Dev server function host tak nahi pahunch pata — port 8000 confirm karo
2. Client Cloud mode mein hai — `.env` mein `INNGEST_DEV=1` chahiye
3. Function dashboard mein missing — host reload nahi hua, restart karo
4. Run hang ho — host aur dev server dono restart karo, ek host ek dev server

---
[⬆ Index](README.md) · [Agla: The Senses ➡](01-the-senses.md)
