# 00 — Part 1: Foundations (Concepts 1-3)

## Concept 1 — Agent Asal Mein Kya Hai

Farq ek sentence mein: **chat completion aapke sawal ka ek dafa jawab deta hai; agent ek loop chalata
hai jab tak kaam khatam na ho.**

| Pattern | Kya Karta Hai | Kab Use Karo |
| --- | --- | --- |
| **Chat completion** | Ek request → ek response. Stateless | Q&A, single-shot summarization |
| **Function-calling LLM** | Request → tool call → aap execute karo → dobara request... **Aap** loop chalate ho | Ek external lookup |
| **Agent** | SDK loop chalata hai: model → tool calls → results → model → ... → final answer | Jab model ko plan, act, observe, re-plan baar baar karna ho |

Agents SDK teesra pattern hai, packaged. **Agent** = LLM + instructions + tools (plus guardrails,
handoffs). **Runner** loop chalata hai.

## Concept 2 — SDK 3 Primitives Mein

3 naam har agent codebase mein milte hain: `Agent`, `Runner`, `@function_tool`.

1. **`Agent`** — LLM + instructions + tools (naam, model, guardrails, handoffs)
2. **`Runner`** — loop chalata hai. `run_sync` blocks; `run` async; `run_streamed` events deta hai
3. **`@function_tool`** — regular Python function ko decorate karta hai taake agent usay call kar
   sake. Type hints + docstring se JSON schema banta hai jo model parhta hai

```python
@function_tool
def get_weather(city: str) -> str:
    """Return the current weather for a city."""
    return f"It's 22°C and sunny in {city}."

agent = Agent(name="WeatherBot", instructions="...", tools=[get_weather])
result = Runner.run_sync(agent, "What's the weather in Karachi?")
print(result.final_output)
```

**3 cheezein notice karo:** (1) type hints ek contract hain jo model dekhta hai; (2) agar model galat
type bheje, SDK usay pakar leta hai **aapka function chalne se pehle**; (3) `result.final_output` model
ka **wrapped** jawab hai — raw tool return nahi. Model tool call karta hai, result parhta hai, apni
voice mein dobara likhta hai — yeh **2 model calls** hain, ek tool choose karne ke liye, ek answer
compose karne ke liye.

Default model `gpt-5.4-mini` hai — fast aur cheap. `model="gpt-5.5"` pass karo jab frontier chahiye ho.

## Concept 3 — Agent Loop, Concrete Tarike Se

SDK model→tool→model→tool loop chalata hai. Aap `max_turns` se cap karte ho. Zyada tool calls chahiye
hon to `MaxTurnsExceeded` raise hoti hai.

**2 layers jahan loop chalta hai:**

| Layer | Kya Own Karta Hai | Kahan Chalta Hai |
| --- | --- | --- |
| **Harness** | Model calls, tool routing, sessions, approvals | Aapka Python process |
| **Compute** (sandbox only) | Files, shell commands, mounts | Sandbox container |

**Sabse zaroori cheez yaad rakhne wali:** **aap loop mein nahi ho.** Ek dafa `Runner.run` call ho jaye,
model decide karta hai kaunsa tool call karna hai, kya arguments dena hai, kab rukna hai. Aapke control
points upstream hain (instructions, tool surface, guardrails) aur downstream (result parhna).

```python
result = Runner.run_sync(agent, "...", max_turns=3)
```

`max_turns=1` matlab agent sirf "single model call, no tools" kar sakta hai — agar tool chahiye ho,
`MaxTurnsExceeded` turn 1 par hi raise hoti hai (tool result model ko wapis jaane se pehle). **Rule of
thumb:** har tool ke liye ~2 turns budget karo.

```python
from agents.exceptions import MaxTurnsExceeded
try:
    result = await Runner.run(agent, user_input, max_turns=3)
except MaxTurnsExceeded as e:
    print(f"Agent hit the turn cap: {e}")
```

---
[⬆ Index](README.md) · [Agla: Local Chat App ➡](01-chat-app-locally.md)
