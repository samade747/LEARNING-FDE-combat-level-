# 05 — Part 6: Cost Discipline + How to Get Good At This

## Har Turn Poori Duniya Ko Re-Bill Karta Hai

Single insight jo affordability ko constraint se discipline mein badalta hai: **har turn poori session
history model ko bhejta hai.** 20 turns wali conversation mein 50K tokens accumulated context ho to,
aap already ek million tokens input ka pay kar chuke hain.

**3 numbers yaad rakho:**
1. **Output tokens input se zyada costly hain** — typically 2-5x. Model jo "loud thinking" karta hai
   full output rates pay karta hai
2. **Cache hits almost free hain** — stable prefixes (system prompt, rules file) 80-90% discount pate
   hain. Isliye tight, stable rules file cheap hai; churning bloated file har turn full price par
   re-bill hoti hai
3. **Subagents aur guardrails token-multipliers hain** — guardrail classifier ek **aur** model call hai
   har turn

**Meter parhna:** Local CLI mein `print(result.context_wrapper.usage)`. Trace dashboard mein har span
tokens dikhata hai.

> **Rule of thumb:** Session shuru mein meter dekho, 10 turns baad dobara. Doosra number pehle se 4x
> zyada ho, to context bloat ho chuka hai — `/reset` ya compaction overdue hai.

## 2-Tier Routing Decision

**Frontier tier** (`gpt-5.5`, `deepseek-v4-pro`): real architectural judgment, economy model already
fail ho chuka, subtle debugging, ghalat jawab discover karna mehnga.

**Economy tier** (`gpt-5.4-mini`, `deepseek-v4-flash`): mechanical kaam (greeting, clarification), tight
plan/prompt template, high volume.

**2 Routing Patterns:**
1. **Plan on frontier, implement on economy** — ek agent `gpt-5.5` par plan banaye, doosra
   `deepseek-v4-flash` par implement kare
2. **Default economy; visible failure par escalate karo** — Flash default; model ghalat jawab de to
   frontier switch karo, hard part khatam hone par wapis switch karo

## 5 Cost-Failure Modes

```
Symptom: monthly bill 3x expected
  → Wajah: default gpt-5.5 chal raha
  → Fix: triage/guardrails ko flash_model par switch karo

Symptom: bill kisi din spike ho
  → Wajah: user ne agent ko loop mein rakhne ka tareeqa dhoond liya
  → Fix: max_turns kam rakho, session compaction add karo

Symptom: har turn pichle se mehnga
  → Wajah: context unbounded barh raha
  → Fix: OpenAIResponsesCompactionSession threshold ke sath

Symptom: model over-explaining kar raha
  → Wajah: instructions mein "explain your reasoning" jaisi phrases
  → Fix: "Reply in ≤2 sentences unless asked" — output tokens 60-80% kam

Symptom: cache hits 70% se 10% girein
  → Wajah: rules file/instructions ki structure badli
  → Fix: context ke shuru mein jo hai usay stable rakho, variable content aakhir mein
```

## 3 DeepSeek Gotchas

1. **Streaming + `@function_tool` fail hota hai** — non-streaming `Runner.run` use karo, `result.new_items`
   se markers lo
2. **Strict JSON schema HTTP 400 deta hai** — `output_type=` drop karo, prose mein JSON mangwao, manually
   parse karo
3. **Tracing exports reject hote hain** — per-run `RunConfig(tracing_disabled=True)`, global disable
   nahi

## Realistic Cost Expectation

Moderate user (90-minute session/day, 5 din/hafta, reasonable context discipline): low-single-digit
dollars/month cheap-tier turns par, plus kabhi kabhi frontier escalations. Heavy user: $15-30.

## How to Actually Get Good At This

Build kar ke seekhte ho. Har addition ek failure mode reveal karta hai jo concept se map hota hai:

- "Agent bhool gaya kya baat hui" → Sessions
- "Agent 80 turns tak circles mein raha" → `max_turns` + clearer tool outputs
- "Din 1 par $40 kharch hua" → galat model defaults — triage ko Flash par le jao
- "User ko ghalat jawab mila aur pata nahi kyun" → Tracing
- "Aisi phone number di jo nahi deni chahiye thi" → Output guardrail
- "Agent ne refund kar diya jo maine sanction nahi kiya" → Human approval
- "Agent ne `rm -rf` chalaya kyunki kisi ne clever prompt paste kiya" → Sandboxing

**Safety primitives problem hit hone par add karo, pehle nahi.** Exception: tracing — din 1 se on karo,
kyunki bina uske debugging hopeless hai.

**Kya aap sath le jate ho:** Almost kuch bhi OpenAI-specific nahi hai. Model swap karo (DeepSeek, Claude,
Gemini via LiteLLM). Sandbox provider swap karo. R2 ko S3 se swap karo. **Yeh shape** (agent loops,
tools, sessions, guardrails, approvals, tracing, sandboxes) hi asal seekh hai.

Aur jab agent misbehave kare, yaad rakho jahan se shuru kiya: **har agent bug state bug hai ya trust
bug** — aap 16 concepts debug nahi kar rahe, sirf poochte ho in do sawalon mein se kaunsa fail hua.

---
[⬅ Worked Example](04-worked-example.md) · [⬆ Index](README.md)
