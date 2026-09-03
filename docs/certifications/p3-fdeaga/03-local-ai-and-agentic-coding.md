# 03 — Local AI and Agentic Coding

*Sources: `using-open-source-llms` + `agentic-coding-crash-course` (Zia Tutor AI, corpus gen 62 —
gen 62 mein alag `local-ai-agentic-coding` slug nahi, syllabus URL inhi do ka combination hai). Deep
notes: [`docs/open-source-llms/`](../../open-source-llms/README.md) · [`docs/agentic-coding/`](../../agentic-coding/README.md).*

---

## PART A — Local AI (Open Source LLMs)

### A1. Ek Picture Poore Local AI Ki

> Har AI tool ke **2 parts**: **Harness** (tumhari machine par, hands-on kaam) aur **Brain** (model,
> sochne ka kaam). Harness brain ko ek **address** par reach karta hai. **Harness kabhi nahi
> badalta — sirf address badalta hai.**

> **Agent = harness + a swappable brain.** Yeh General Agents section ki core idea hai — brain khud
> own karke yeh day-1 se real ho jaati hai.

### A2. 3 Tiers (ek address, teen jagah)

| Tier | Serving layer | Address | Scale | Cost |
| --- | --- | --- | --- | --- |
| **Local** | **Ollama** | `http://localhost:11434` | 1 insaan, 1 laptop | kuch nahi |
| **Server/Cluster** | **vLLM** | `http://localhost:8000` | 50 concurrent, 1 machine/cluster | GPU rental (~$0.50–2/hr, 24GB card) |
| **Cloud** | **OpenRouter** (gateway) | `https://openrouter.ai/api` | frontier models jo koi self-host nahi kar sakta | per-token (~$0.44/M input DeepSeek → $15/M output Kimi K3) |

### A3. Local Tier — Ollama

- `ollama run gemma3:4b` — WiFi band karke bhi chalta hai, kuch bahar nahi jaata. `localhost` = "yehi
  computer."
- **Local brain ek alag brain hai** — cloud model ki chhoti copy nahi (phone-number analogy: address
  alag = alag banda).
- Harness wiring: Claude Code → `ANTHROPIC_BASE_URL` (bare address, **no `/v1`**); OpenCode →
  `opencode.json` provider config mein **`/v1` required**.
- **2 deewarein har local setup face karti hai:**
  | Wall | Kya | Fix |
  | --- | --- | --- |
  | **Capability** | model sahi structured tool-call kar sake | **strong / tool-use-trained model** (hardware se fix NAHI) |
  | **Throughput** | tez reading/generation | **GPU** (smarter/chhota model se fix NAHI) |
- Model guide: `llama3.2:3b` (tool calls mangle) < `qwen3:8b` (simple tasks OK) < `qwen3:30b-a3b`
  (best balance).
- **Healthy tool call = structured JSON.** Kamzor model plain text bhejta hai → harness reject karta
  hai.
- **Context window trap:** Ollama default sirf **4,096 tokens** (chup-chaap trim) — `num_ctx` ko
  64,000+ set karo.
- **Brain own karna kab:** privacy, offline, cost (din-bhar chalti loops sasti). **Limit:** ek
  customer serve karta hai.

### A4. Server Tier — vLLM

- Ollama concurrency ke sath **flat** rehta hai (design choice — ek insaan ka laptop, restaurant
  nahi). `OLLAMA_NUM_PARALLEL`.
- **vLLM = industrial kitchen**, kai users ek saath. 2 tricks: **continuous batching** +
  **PagedAttention**.
- `vllm serve` + **`--enable-auto-tool-choice`** + parser flags — inke baghair coding agents
  **chup-chaap fail** hoti hain. 16GB card → FP8 compressed build.
- **vLLM ek user ke liye tez nahi karta** — load ke neeche machine ko tez karta hai (chadhti curve
  GPU bharne tak).
- Sharing warning: kam se kam `--api-key` set karo jab machine kisi aur ko serve kare.
- **Honest limit:** sirf **throughput wall** move hoti hai — model utna hi smart. Capability wall ke
  liye cloud tier chahiye.

### A5. Cloud Tier — OpenRouter

- Open-weight models jo utha nahi sakte: **Kimi K3** (2.8T params, performance, 64+ chips) vs
  **DeepSeek V4 Pro** (1.6T / ~49B active, price-performance, MIT license, 8–16 GPUs).
- **"Open" 3 cheezein deta hai:** no lock-in · choice of landlord · floor under future.
- **OpenRouter = gateway** — 1 address, 1 key, 1 bill. Wiring: `ANTHROPIC_BASE_URL=openrouter.ai/api`.
- Ehtiyat: **Claude Code sirf Anthropic models par fully tested** — non-Anthropic ke liye
  **OpenCode / Claude Code Router (CCR)** full-supported path hai.
- Pricing: Kimi K3 ($3 in / $15 out) vs DeepSeek V4 Pro ($0.44 / $0.87) — output par ~17x sasta.
- **Working rule:** price-performance model **default**, escalate **sirf real-failure par**. Cached
  input zaroori (repeated prefix chhote fraction par).
- **3 sawal, is order mein:** (1) data bahar ja sakta? (2) mid-size model reach mein? (3) frontier
  genuinely chahiye?
- **Claude Code Router (CCR):** ek config file se request-by-request routing (default / background /
  think / longContext tiers). `ccr code`, `/model` mid-session switch. Community project — add tab
  karo jab zaroorat ho.

### A6. Apna Mini LLM Cloud (Appendix)

- **Inference engine (vLLM) ≠ Gateway.** vLLM akela = kitchen, restaurant nahi (koi identity /
  spending-limit / records / multi-model awareness nahi).
- **LiteLLM** (open-source proxy) — virtual keys, budgets + rate limits, ek address par menu,
  spending records. **Gateway = control tool, performance tool nahi.**
- 4-container stack: vLLM + LiteLLM + Postgres + Open WebUI (`docker compose up`).
- **Security:** March 2026 LiteLLM supply-chain attack — **exact version pin karo, `latest` track
  mat karo.**
- Keys: `user_id`, `models`, `max_budget`, `rpm_limit`.
- Teeno tiers ek darwaze ke peeche: fallback policy (GPU-down → chup-chaap cloud). OpenRouter key
  kabhi machine se bahar nahi jaati.
- Health metrics: **queue depth, time-to-first-token, GPU memory in use**.

---

## PART B — Agentic Coding (Claude Code & OpenCode)

### B1. Core Shift + Karpathy Ki 3 Baatein

- Chatbot **jawab deta hai**; Claude Code / OpenCode **action lete hain** — files parhte/edit karte,
  commands chalate, task khatam hone tak chalte. **Sawal poochna band, instruction do.**
- Poora course ek idea: **context engineering** — jaan-boojh kar decide karna model **kya dekhe**
  (Karpathy ne Dec 2025 naam diya). *Is book mein alag context-engineering course nahi — yehi hai.*
- **Karpathy ki 3 baatein:**
  1. Yeh **ghost hai, insaan nahi** — koi ego, koi motivation. Tum manage karte ho.
  2. Iski intelligence **jagged** hai — ek cheez mein superhuman, agli mein kamzor.
  3. **Utna hi trust karo jitna output check ho sake** → **verification loop** (poore course ka core).

### B2. Foundations

- Install: `curl -fsSL https://claude.ai/install.sh | bash` / `opencode.ai/install`. Ehtiyat: kuch
  free OpenCode "stealth models" temporary hain, data training ke liye use ho sakta.
- **Plan Mode** — "look but do not touch". Claude Code `Shift+Tab` ×2; OpenCode `Tab`. Rule: task
  **10 min se zyada** legi → plan mode.
- **Permissions discipline** — shuru mein sab dekho, phir safe actions auto-approve
  (`.claude/settings.json` allow/deny). OpenCode: granular per-type + 3-repeat auto-stop.
- **Model ko task se match karo:** planning/architecture → capable model; routine execution → cheap
  model. **"Strong model se plan karo, cheap model se execute karo."**

### B3. Context Management

- Context = **stack of layers**, har layer cost karti hai: system prompt + tools (fixed) · rules file
  (fixed) · conversation (badhti) · referenced files (on-demand) · active skill (on-demand). Top 2
  fixed, baaki manage karni hain.
- **Context rot** real — rules ignore, khatam kaam dobara, non-existent files. **Rule: window ka
  aadha use hote hi `/compact` ya `/clear`.**
- `/clear` (poori chat delete) vs `/compact` (summary rakhta) — mix mat karo; **boundaries par
  compact karo, mid-task nahi**; "summarize the journey, file the facts."
- **Doom/doom-loop signs:** sorry bolna par fix na karna · wahi code repeat · non-existent files ·
  bhoola hua rule → message bhejna band, reset.
- Undo: Claude Code `Esc`×2 / `/rewind` (files only); OpenCode `/undo` `/redo` (git-based, sab cover).
- Bara tool output **file mein bhejo, chat mein nahi**.

### B4. Rules File — CLAUDE.md / AGENTS.md

- File jo **har conversation ke shuru** mein parha jaata hai. Claude Code: `CLAUDE.md`; OpenCode:
  `AGENTS.md` (fallback `CLAUDE.md`).
- `/init` auto-generate (bohot lambi) — kaam: **jo zaroorat nahi delete karo**. Har line ka test:
  **"agar hata doon kya AI galti karega?"**
- Boris Cherny (Claude Code creator) ki file ~**2,500 tokens** saal bhar baad bhi.
- **Prune bhi karo** — contradictory rules jama hoti hain. July 2026 Claude Code team ne apna 80%+
  system prompt hataya bina performance loss. Forbid-rules → standard-describe rules.
- Model capability ke hisaab se constrain: frontier model → thin rules; cheap/local → zyada explicit.
  `/doctor` review karta hai.

### B5. Personalizing — 3 Alag Problems

| Tool | Problem yeh solve karta hai |
| --- | --- |
| **Command / Skill** (`.claude/skills/name/SKILL.md` → `/name`) | saved reusable prompt. **Description sabse zaroori line.** Chhoti skills. Skill **deterministic nahi** banata — sirf range narrow karta hai; guaranteed result → script/hook |
| **Hook / Plugin** (Claude Code `.claude/settings.json` JSON; OpenCode `.opencode/plugins/*.js`) | **hamesha khud chalti rule.** `exit code 2` = block. Achi aadat: **commit-time checks, per-edit nahi** |
| **Subagent** (`.claude/agents/name.md`) | isolated context window helper, **sirf summary wapis** |

- **Verification loop** — poori book ka sabse zaroori pattern: **Attempt → Check → Fix → Repeat**,
  beech mein koi insaan nahi. Boris Cherny: AI ko verify karne ka tareeqa do → result 2–3x behtar.
  Robert C. Martin (July 2026): ab agents ka code parhta hi nahi, sirf extreme constraints
  (tests/coverage/mutation testing) — **order zaroori: pehle checks, phir parhna chhora**.
- Hook **khud paste karo** (model se mat likhwao) — warna model apni hi rule follow karke safety
  check defeat kar sakta hai.

### B6. Connecting to the World — MCP

- MCP AI ko services se connect karta hai (Slack, Docs, Notion, GitHub, DBs) — APIs ke upar **standard
  wrapper**. Asal sawal: **"standing connection ke qabil hai, ya agent seedha call kar sakta hai?"**
- Setup: `claude mcp add --transport http` / OpenCode `opencode.json` mcp block. `/mcp` status.
- **System of record connect karna** = zaroori use case (live authoritative data, stale paste nahi).
- Ehtiyat: **sab connect mat karo** — Claude Code lazy-loads; OpenCode upfront load (zyada selective).
  1–2 se shuru.
- **Prompt injection:** model jo parhta hai woh usay steer kar sakta hai. 3 habits: **fetched content
  sirf inform kare, apni files hi instruct karein** · untrusted content **subagent se parhwao** ·
  behavior ajeeb ho to shak. Honest limit: exposure kam, immune nahi (deeper fences = Harness Eng).

### B7. Composing Claude Code + OpenCode

- **Git worktrees** — parallel sessions bina conflict: `git worktree add -b branch ../copy`. Rule:
  same file 2 sessions = bura; alag directories = acha.
- **Pattern 1 — Plan/Execute split:** Claude Code plan banaye → save → OpenCode cheap model implement
  kare. **Plan file = contract.**
- **Pattern 2 — Cross-model review:** jisne likha wahi review ke liye bura — alag family ka model
  review kare (Claude ↔ GPT).

---

## Ek-Line Revision (M3)

> Agent = harness + swappable brain; harness kabhi nahi badalta, sirf **address** (localhost:11434
> Ollama / localhost:8000 vLLM / openrouter.ai cloud) · 2 walls: **capability** (strong model) vs
> **throughput** (GPU) · agentic coding = **context engineering** (model kya dekhe) · Karpathy: ghost,
> jagged, trust = verifiable · **verification loop** Attempt→Check→Fix→Repeat · rules file: har line
> "agar hata doon kya AI galti karega?" · MCP: standing connection ke qabil? · plan mode 10min+ ·
> strong model plan, cheap model execute.

---

## MCQ Practice (jawab neeche)

1. "Harness" aur "brain" mein kaunsa badalta hai jab tum local se cloud jaate ho?
   a) Harness b) Sirf address c) Dono d) Kuch nahi

2. Ollama, vLLM, OpenRouter ke default addresses:
   a) Sab localhost b) localhost:11434 / localhost:8000 / openrouter.ai/api c) Sab cloud d) Random ports

3. Local setup ki "capability wall" kaise fix hoti hai?
   a) Behtar GPU b) Strong / tool-use-trained model (hardware se nahi) c) Zyada RAM d) Chhota model

4. Local setup ki "throughput wall" kaise fix hoti hai?
   a) Smarter model b) GPU (chhota model se nahi) c) Zyada prompts d) Cloud switch

5. Ollama ka context window default:
   a) 128,000 b) 32,000 c) 4,096 (chup-chaap trim — `num_ctx` barhao) d) unlimited

6. vLLM ek single user ke liye kya karta hai?
   a) Bahut tez b) Ek user ke liye tez nahi — load ke neeche machine ko tez karta hai
   c) Slow karta hai d) Kuch nahi

7. "Open" model 3 cheezein deta hai:
   a) Speed, cost, quality b) No lock-in, choice of landlord, floor under future c) 3 models
   d) Privacy, offline, free

8. Cloud tier par model chunne ke 3 sawal (order):
   a) Cost, speed, quality b) Data bahar ja sakta? → mid-size reach mein? → frontier chahiye?
   c) Model, tool, runtime d) Kimi, DeepSeek, Claude

9. Inference engine (vLLM) aur gateway (LiteLLM) ka farq:
   a) Same b) vLLM = performance/kitchen; gateway = control (identity, budgets, records) — restaurant
   c) vLLM control d) Gateway performance

10. Agentic coding course asal mein kis discipline ka full treatment hai?
    a) Prompt engineering b) Context engineering (model kya dekhe) c) Model training d) DevOps

11. Karpathy ki 3 baatein mein "trust" wali:
    a) AI par poora bharosa b) Kabhi bharosa mat karo c) Utna hi trust jitna output check ho sake →
    verification loop d) Sirf tests par bharosa

12. Rules file ki har line ka test:
    a) Chhoti ho b) "Agar main yeh hata doon, kya AI genuinely galti karega?" — nahi to delete
    c) Formal ho d) English mein ho

13. "Verification loop" kya hai?
    a) Human review har step b) Attempt → Check → Fix → Repeat, beech mein koi insaan nahi
    c) CI pipeline d) Code review

14. Skill/Command deterministic result deta hai?
    a) Haan b) Nahi — sirf range narrow karta hai; guaranteed result ke liye script/hook
    c) Sirf Claude Code mein d) Sirf hook ke sath

15. Hook kis se likhwana chahiye?
    a) Model se b) Khud paste karo — warna model apni hi rule follow karke safety check defeat kar
    sakta hai c) Koi farq nahi d) OpenCode se

16. MCP add karne se pehle asal sawal:
    a) Free hai? b) "Standing connection ke qabil hai, ya agent seedha call kar sakta hai?"
    c) Popular hai? d) Anthropic ka hai?

17. Plan/Execute split pattern mein "contract" kya hai?
    a) Legal doc b) Plan file (Claude Code banata, OpenCode cheap model implement karta) c) Rules file
    d) SKILL.md

18. Prompt injection ke against pehli habit:
    a) MCP band karo b) Fetched/untrusted content sirf inform kare — instruct sirf apni files karein
    c) Sab kuch subagent se d) Cloud model use karo

### Jawab Key

1‑b · 2‑b · 3‑b · 4‑b · 5‑c · 6‑b · 7‑b · 8‑b · 9‑b · 10‑b · 11‑c · 12‑b · 13‑b · 14‑b · 15‑b · 16‑b
· 17‑b · 18‑b

---
[⬅ 02 — Agent Factory Ecosystem](02-agent-factory-ecosystem.md) · [Agla: 04 — Loop Engineering ➡](04-loop-engineering.md)
