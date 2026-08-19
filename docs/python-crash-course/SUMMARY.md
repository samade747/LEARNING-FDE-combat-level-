# Python in the AI Era — Crash Course — Summary

Mode 2, Manufacturing Phase 1 (Chapter 1/6). 17 Concepts, "Read Before You Write" — ab Python **likhna**
nahi, **parhna** seekhna hai, kyunki agent code generate karta hai lekin sirf woh insan farq bata sakta
hai jo "working-looking" aur "correct" mein farq parh sake.

## 00 — Overview: Naya Mindset, PRIMM-AI+, Workbench

- **Concept 1 — Aap parhte ho, agent likhta hai:** 10-80-10 rule — aap pehle 10% (kya banana/correct ka
  matlab) aur aakhri 10% (verify) own karte ho, agent beech ke 80% (generate) karta hai. Recognition,
  recall nahi.
- **Concept 2 — PRIMM-AI+ method:** 5 steps — Predict (chalne se pehle guess), Run (chalao dekho), 
  Investigate (guess vs reality, line-by-line), Modify (ek cheez badlo dobara predict), Make (apna
  version specify karo, agent banaye, verify karo). Testing engine hai. Predict optional nahi — gap
  hi learning hai.
- **Concept 3 — Workbench 5 minute mein:** `uv` (package manager) se setup, tools: uv, pytest, Pyright
  (type-check), Ruff (formatting/style) — yeh "reading machines" hain jo agent-generated code ko aapke
  liye parhte hain. Setup fail ho to error copy-paste karo, "getting unstuck agent ka kaam hai."

## 01 — Part 2: Har Jagah Milne Wale Shapes (Concepts 4-9, ~70% Python coverage)

- **Concept 4 — Values/variables/4 types:** `=` = "value ko box mein rakho", str/int/float/bool, type
  hints (`: str`) optional lekin course mein hamesha use hote (agent ko exact batate hain).
- **Concept 5 — Functions/signature:** Signature = contract — body galat ho sakta, signature batati kya
  promise tha. `assert` se pin karo.
- **Concept 6 — Collections:** list (ordered, mutable), dict (key:value — JSON se direct maps, agent
  data-passing ka main tareeqa), set (unique), tuple (fixed).
- **Concept 7 — Control flow/comprehensions:** if/for, f-string, elif chain (top-to-bottom, first match),
  comprehension = for-loop ek line mein fold — AI code mein har jagah milta hai.
- **Concept 8 — Classes/objects:** Class = blueprint, object = instance. `__init__` setup method, `self`
  = "yeh particular object", attributes = data, methods = action. Pattern: `agent.run(task)`, `db.save()`.
- **Concept 9 — Baqi shapes:** `while` (infinite-loop risk), slicing (`[1:3]` exclusive end, `[-1]` last),
  `try`/`except` (crash na ho), `input()` (hamesha text return karta — math se pehle convert zaroori).
  Verify-worthy bug spots: non-terminating while, off-by-one slice, silently-swallowing except,
  unconverted input.

## 02 — Part 3: AI-Era Power Concepts (Concepts 10-15, Read-Only Zone)

- **Concept 10 — Type hints:** Agent ko steer karne wale labels. Achhi "generate karo" request ki
  anatomy: typed signature + 1-2 examples + constraints + verify-karne-ko-kaho.
- **Concept 11 — Dataclasses/Pydantic:** `@dataclass` shape deta hai (auto `__init__`); Pydantic runtime
  par **validate** karta hai (`Field(gt=..., lt=...)`), turant clear error deta hai — agent code mein
  har jagah kyunki JSON schemas bhi auto-generate karta hai (LLM tool calling ke liye). `pytest.raises`
  se error case pin karo.
- **Concept 12 — Generators/`yield`:** Ek waqt mein ek item — memory-safe stream vs poora list load.
  Return type `Iterator[str]` = generator ka signal.
- **Concept 13 — `with`:** Safely khol/band karo (files, DB connections) — error ke bawajood.
- **Concept 14 — `async`/`await`:** 20 API calls sequentially ~2s, async se ~sabse slow call jitna time.
- **Concept 15 — Dunder methods:** `__init__`, `__call__` — objects ko native cheezon jaisa behave
  karate. `__call__` hi wajah hai `model(x)` (PyTorch pattern) ki. Yeh sab **likhna** nahi, **pehchanna**
  hai — poori book ki verification skill.

## 03 — Part 4: TDG Loop End-to-End (Concepts 16-17)

- **Concept 16 — Test-Driven Generation:** Purana order ulta — failing test likho jo "correct" define
  kare (aap se aani chahiye, agent se nahi — warna independent signal nahi), agent implementation
  generate kare, test se verify karo. Agar agent **test** ko badal kar pass karwaye (code nahi), usay
  roko. TDG-step-ownership table (aap/agent/aap).
  - **Traceback reading:** bottom-up parho. 6 common errors table (ModuleNotFoundError, NameError,
    TypeError, AttributeError, KeyError, IndexError) — kya matlab, agent ko kya batana. Kabhi blindly
    "try again" mat dabao.
- **Concept 17 — Vague goal se specifiable pieces tak:** Decomposition = 5 steps — goal ek sentence,
  steps list karo (verbs = candidate units), har unit ko typed signature do, har unit TDG karo order
  mein, sab wire together karo. Heuristic: agar test likhna mushkil hai, unit bohat zyada kaam kar rahi
  hai. Reusable prompt template diya gaya (ONLY/NOT keywords load-bearing).

## 04 — Part 5: Judgment + Practice Projects + Glossary

- **Kab AI par tekiya na lagao:** security-sensitive code non-negotiable; genuinely-na-parh-sakne wale
  code par tests par zyada tekiya; chote-obvious changes khud tez.
- **Apne tests ko red-team karo:** agent ko apne tests khud likhne mat do; test kamzor kar ke pass
  karwane mat do; happy-path ke ilawa failures bhi test karo (empty, zero, negative, missing key).
- **Diff review checklist** (7 points) accept karne se pehle: kaunsi files badli, tests badle to kyun,
  new dependencies, sensitive touch, pytest/Pyright/Ruff pass, plain-English explain kar sakte ho, code
  abhi bhi badalna aasan hai.
- **6 Practice Projects:** (1) Read and predict, (2) First TDG cycle (`initials()`), (3) TDG on class
  (`TaskList`, silent bug pakarna), (4) Find the bug in agent code, (5) Mini-capstone: Notes tool
  end-to-end, (6) On your own (zero starter/tests — "3 most common words print karo").
- **Self-check (7 items)** — bina notes ke kar sako to course kaam kar gaya.
- **60-Second Glossary** — 16 terms (PRIMM-AI+, TDD→TDG, assert, type hint, collections, class/object,
  self/attribute/method, comprehension, f-string, generator/yield, with, async/await, dunder, decorator,
  Pydantic, pytest/Pyright/Ruff/uv, traceback).
- **Yahan se aage:** Build AI Agents, Postgres for AI, Building a Digital FTE.
