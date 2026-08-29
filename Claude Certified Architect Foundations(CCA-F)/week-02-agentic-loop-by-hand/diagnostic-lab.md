# Week 2, Hour 2 — 5-Bug Diagnostic Lab

Scaffold: [`../../docs/certifications/ccar-f/projects/00-agentic-loop-no-framework/`](../../docs/certifications/ccar-f/projects/00-agentic-loop-no-framework/README.md)
Run: `python -m pytest docs/certifications/ccar-f/projects/00-agentic-loop-no-framework/test_loop.py -q` → **5 passed** (2026-08-29).

**Exercise:** har broken loop ko chalao, sirf **symptom** dekho, phir bina fixed code dekhe bug
name karo. Neeche meri diagnosis — symptom se root cause tak.

| # | Symptom (jo dikha) | Meri diagnosis | Root cause | Fix (single line) |
| --- | --- | --- | --- | --- |
| 1 | Model har turn aadha-adhoora jawab deta hai, jaise usay yaad nahi kya kaha tha | **Missing history** | Assistant ka apna turn `messages` mein append nahi hua → agli stateless API call mein model ka pichla tool_use/reasoning gayab | `messages.append({"role": "assistant", "content": response.content})` har turn |
| 2 | Tool chala (side effect hua), lekin model ne kabhi acknowledge nahi kiya — wahi call dobara maangta hai | **Lost tool result** | `tool_result` block user turn ke roop mein append nahi hua → model ko pata hi nahi tool ka jawab kya tha | `messages.append({"role": "user", "content": tool_results})` |
| 3 | Model prose likhta hai + tool call karta hai ek hi turn mein, loop use "done" samajh leta hai, tool kabhi nahi chalta | **Incorrect stop handling** | Stop condition "koi text block hai?" hai, `stop_reason == "end_turn"` nahi. Mixed turn (text + tool_use, stop_reason abhi bhi `tool_use`) galat classify hota hai | `if response.stop_reason == "end_turn":` — content shape kabhi nahi |
| 4 | Loop kabhi khatam nahi hota, cost badhta rehta hai, koi error nahi | **Repeated tool calls / no ceiling** | `while True` — koi `MAX_TURNS` bound nahi. Stuck model (aksar Bug 2 ke saath) forever | `for _ in range(MAX_TURNS):` + exhaustion par clean error |
| 5 | Multi-tool turn: pehla tool chala, baaki silently ignore, model adhoore data par jawab deta hai | **Premature termination** | Sirf `tool_use_blocks[0]` execute hota hai, `blocks[1:]` drop | `for block in _tool_use_blocks(response):` — har block |

## Diagnostic drill (symptom → bug, bina code dekhe)

- "half ka jawab mila, tool call ho hi nahi paya" → **Bug 3**
- "loop kabhi khatam nahi hota" → **Bug 4**
- "tool chala par model ko pata nahi chala" → **Bug 2**
- "model bhool jata hai usne abhi kya kiya" → **Bug 1**
- "2 tools maange, sirf 1 chala" → **Bug 5**

## Reusable rule (exam)

> Loop-control bugs **symptom** aur **root cause** ke beech hamesha ek layer door hote hain. "Loop
> repeat karta hai" ka fix "retry logic add karo" nahi — root cause usually **missing tool_result**
> (Bug 2) ya **missing history** (Bug 1) hai. Symptom-patch (Bug 4 ka ceiling) crash rokta hai lekin
> asal masla nahi theek karता.
