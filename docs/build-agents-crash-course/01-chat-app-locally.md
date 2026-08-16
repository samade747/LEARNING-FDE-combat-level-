# 01 — Part 2: Local Chat App Banana (Concepts 4-9)

## Concept 4 — Project Setup `uv` Se

`uv` ko Python ka `npm`/`Cargo` socho — Python khud install karta hai, virtual environment banata hai,
dependencies lock karta hai. **Sirf woh install karo jo abhi chahiye** — `openai-agents` aur
`python-dotenv`.

## Concept 5 — Chat Loop, Aur Uska Bug

Obvious chat loop 3 lines ka hai: input parho, agent chalao, jawab print karo, repeat. Turn 1 par kaam
karta hai, turn 2 par toot jata hai. **Wajah: `Runner.run_sync` stateless hai** — har call independent
hai, kuch bhi turns ke beech carry nahi hota. Agent ne turn 1 **bhoola** nahi — usay turn 1 mila hi
nahi. **Yeh classic state bug hai.**

```python
agent = Agent(name="Chatty", instructions="...")
while True:
    user_input = input("You: ").strip()
    result = Runner.run_sync(agent, user_input)
    print(f"Assistant: {result.final_output}\n")
```

## Concept 6 — Sessions, Bug Fix Karna

**Sessions state add karte hain:** ek object jo `Runner.run` ko pass karte ho, SDK conversation history
har turn ke through thread karta hai.

```python
session = SQLiteSession("chat-cli")   # default: in-memory
result = Runner.run_sync(agent, user_input, session=session)
```

Persistence ke liye file path do: `SQLiteSession("chat-cli", "conversations.db")`.

> **Cost consequence real hai:** Turn 2 **poori history** bhejta hai, sirf naya sawal nahi. Har turn
> pichle sab turns ko dobara bill karta hai.

Lambe conversations ke liye: `OpenAIResponsesCompactionSession` — purane turns ko auto-summarize karta
hai jab threshold cross ho.

## Concept 7 — Streaming Responses

`Runner.run_sync` block karta hai jab tak agent khatam na ho — multi-tool turn mein 10+ second. Chat UI
mein yeh broken lagta hai. `Runner.run_streamed` fix hai — events batate hain kya ho raha hai:
token-by-token text, `tool_called`, `tool_output`.

```python
result = Runner.run_streamed(agent, user_input, session=session)
async for event in result.stream_events():
    if isinstance(event, RawResponsesStreamEvent):
        delta = getattr(event.data, "delta", None)
        if delta: print(delta, end="", flush=True)
```

> **Trade-off:** Streaming live-feeling UI deta hai, debugging mehngi karta hai. Synchronous run fail
> ho to ek clean stack trace milta hai; stream beech mein fail ho to aadha-print jawab milta hai. Pehle
> plain version chalao, phir streaming add karo.

## Concept 8 — Function Tools, Stub Se Aage

Model ko `book_meeting(duration_minutes=45)` call karne se kya rokta hai jab calendar sirf 15/30/60
allow kare? **Type hints.** `@function_tool` Python type hints aur docstring ko JSON schema mein badalta
hai jo model dekhta hai. Model galat argument bheje to SDK validation error wapis deti hai — aapka
function kabhi galat types ke sath nahi chalta.

```python
@function_tool
def book_meeting(
    attendee_email: str,
    duration_minutes: Literal[15, 30, 60],
    topic: str,
) -> str:
    """Schedule a meeting. Use only after user confirms time and attendee.
    Do not call this to check availability — use check_availability."""
    return f"Booked {duration_minutes} min with {attendee_email}: '{topic}' Tue 2pm."
```

**3 practical rules:**
1. **Type hints model ke liye documentation hain** — `Literal[...]` exact values force karta hai
2. **Docstring hi tool description hai** — kab **na** call karo woh bhi likho
3. **Tools strings ya chote JSON-encodable types return karein** — bara data summarize karo ya key
   likho

Structured return chahiye to Pydantic model use karo — SDK JSON-encode kar deta hai.

## Concept 9 — Handoffs Specialist Agents Ko

**Handoff** ek agent se doosre agent ko conversation control transfer karta hai. Use karo jab
instructions ya tool sets **genuinely alag** hon.

```python
billing_agent = Agent(name="BillingSpecialist", instructions="...", tools=[get_billing_invoice])
calendar_agent = Agent(name="CalendarSpecialist", instructions="...", tools=[check_availability, book_meeting])
triage_agent = Agent(
    name="Triage",
    instructions="For billing, hand off to BillingSpecialist. For scheduling, hand off to CalendarSpecialist.",
    handoffs=[billing_agent, calendar_agent],
)
```

**Handoff jab worth hai:** instructions/tool surfaces genuinely diverge karte hon. **Worth nahi:** jab
aap sirf ek agent ko halka sa vary kar rahe ho — 90% identical instructions wale 2 agents overhead hain.

**Decision table:**

| Signal | Sahi Shape |
| --- | --- |
| 2 roles ke alag system prompts jo merge nahi ho sakte | Handoff |
| 2 roles ko alag tool surfaces chahiye (auth, scope) | Handoff |
| Target ka pehla action "conversation ab tak parho" hai | Shayad tool, agent nahi |
| Pehla agent function call kar ke continue kar sakta hai | Single agent + tool |

**Cost:** Har handoff kam az kam ek extra model call hai. Ek billing sawal ka typical trace: (1) Triage
decide karta hai handoff karna hai, (2) BillingSpecialist tool call karta hai, (3) BillingSpecialist
result parh ke jawab likhta hai — **3 model calls versus single-agent design ke 1.**

---
[⬅ Foundations](00-foundations.md) · [⬆ Index](README.md) · [Agla: Safety, Observability, Routing ➡](02-safety-observability-routing.md)
