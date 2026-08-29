# Week 2, Hour 1 — The Agentic Loop by Hand (Concepts)

*Required course: **The Loop by Hand**. Exam mapping: **Task 1.1**; `tool_choice` concepts used in
Tasks 2.3 aur 4.3. Domain 1 (Agentic Architecture & Orchestration, 27%).*

## Central rule

> **Protocol ke control signals se pata karo ke turn khatam hua — prose parh kar nahi, aur yeh dekh
> kar nahi ke response mein text hai ya nahi.**

## 1. Messages API is stateless

- Server aapki conversation **yaad nahi rakhta**. Har `messages.create()` call mein aapko **poori
  history** bhejni hoti hai — user turns + assistant turns (tool_use blocks sameet) + tool_result
  turns.
- Isliye agentic loop ka pehla kaam: **`messages` list ko har turn khud maintain karna**.
- Agar assistant ka turn append karna bhool gaye → BUG 1 (model half-blind re-answers).

## 2. Content is a list of typed blocks

Ek assistant response ka `.content` ek **list** hai, plain string nahi. Block types:

| Block | Matlab |
| --- | --- |
| `text` | Model ka prose output |
| `tool_use` | Model ek tool chalana chahta hai — `id`, `name`, `input` carry karta hai |
| `thinking` | Extended reasoning (jab enabled ho) |

Ek hi turn mein **text + ek ya zyada tool_use blocks** ho sakte hain. Isliye:
- Har tool_use block par loop karo, sirf `[0]` mat lो → warna BUG 5 (premature termination).

## 3. stop_reason — the loop's branch point

| `stop_reason` | Iska matlab | Loop kya kare |
| --- | --- | --- |
| `end_turn` | Model ne khud faisla kiya ke kaam ho gaya | Final text present karo, loop tod do |
| `tool_use` | Model tool call chahta hai | Har tool_use block execute karo, `tool_result` append karo, loop continue |
| `max_tokens` | Response truncate hua | Retry (zyada budget) ya error — parse mat karo |
| `stop_sequence` | Koi stop string mila | Context-dependent |
| `pause_turn` | Long-running server tool (jaise web search) | Response as-is wapas bhejo, continue |

**`stop_reason` par branch karo, content shape par nahi.** "text block maujood hai isliye done" =
BUG 3 — aisा turn jo prose bhi likhta hai aur tool bhi call karta hai (stop_reason abhi bhi
`tool_use`), usay final samajh liya jata hai aur tool call silently drop ho jati hai.

## 4. tool_use / tool_result / tool_use_id — the round-trip

```
assistant turn:  { role: assistant, content: [ {type: tool_use, id: "abc", name: "get_weather", input: {...}} ] }
                     ↓  (aap tool chalao)
user turn:       { role: user, content: [ {type: tool_result, tool_use_id: "abc", content: "Lahore: 32C" } ] }
```

- `tool_use_id` **exact match** hona chahiye — model isi se result ko apne call se jodta hai.
- Multi-tool turn: har `tool_use` ke liye ek `tool_result` block, sab ek hi user turn mein.
- Tool error → `tool_result` mein `is_error: true` (Claude API) / `isError: true` (MCP + CCAR-F
  guide ki terminology). **Successful empty result ≠ access failure** — dono alag hain.
- Tool result append karna bhool gaye → BUG 2 (model ko pata hi nahi chala tool chala).

## 5. Turn ceiling

Loop ko **hard `MAX_TURNS` bound** chahiye. Stuck model (jaise jo baar baar wahi call maangta hai
kyunki usay result nahi mila) infinitely chalega → BUG 4. Ceiling par clean, diagnosable error do.

## 6. Parallel tool calls

Ek turn mein model kai **independent** tools ek saath call kar sakta hai (jaise 3 sheher ka mausam).
Aap unhe parallel execute kar sakte ho, lekin **sab ke tool_result ek hi user turn mein** wapas jane
chahiye.

## 7. tool_choice — forcing the model's hand

| `tool_choice` | Behaviour | Kab |
| --- | --- | --- |
| `{"type": "auto"}` | Model khud decide kare tool use kare ya na kare (default jab tools diye ho) | Normal agentic use |
| `{"type": "any"}` | Model **koi ek tool** zaroor call kare (text-only allowed nahi) | Jab har turn ek action chahiye |
| `{"type": "tool", "name": "X"}` | Model **yeh specific tool** call kare | Structured extraction — Task 4.3: `tool_use` + JSON Schema se guaranteed-shape output nikalna |
| `{"type": "none"}` | Koi tool call na ho | Tools context mein rakhna hai par is turn use nahi karne |

**Note:** `any` / forced tool ke sath `stop_reason` `tool_use` aayega, `end_turn` nahi — loop design
karte waqt yaad rakho.

## 8. Homework question (Hour 1 ke baad)

> Claude Agent SDK ab aapke liye kya karega jo aapne abhi hmaath se implement kiya? → `homework.md`
