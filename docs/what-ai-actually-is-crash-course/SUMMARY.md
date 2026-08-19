# What AI Actually Is — Crash Course — Summary

Foundations-Everyone ka pehla chapter (koi math/code nahi) — **9 ideas** jo AI ke almost har ajeeb
behaviour explain karte hain, taake failures mysteries na rahein, **predictable** ban jayein. Ek
sentence: *"It is a prediction machine that learned by reading and has no organ for truth, so it is
fluent everywhere, reliable only where the text was thick, and you are the part that checks."*

## 00 — Overview
- Car-engine analogy: jo hood ke neeche jaante hain wo surprises se panic nahi karte.
- Is course ka rishta baaqi 5 Foundations courses se: yeh **mechanism** deta hai, wo **practice**
  (table diya gaya hai: knowledge/context-window/chat-history/confidence/reasoning/images topics dono
  jagah aate hain, jaan-boojh kar, alag angle se).
- **Strawberry test:** "R" letters count karo bina spell kiye vs spell kar ke — pehli baar galat, dusri
  baar sahi. Wajah: model letters nahi tokens dekhta (Idea 4). Typo bhi ignore hota hai (chunks meaning
  ke qareeb map ho jate hain) — dono facts ek hi mechanism se aate hain.
- Roadmap: Part 1 (Ideas 1-3, The Machine), Part 2 (Ideas 4-7, Why It Behaves), Part 3 (Ideas 8-9,
  Predictor→Agent).

## 01 — Part 1: The Machine (Ideas 1-3)
- **Idea 1:** Model next-piece-of-text predict karta hai, lookup nahi — "well-read autocomplete," na ke
  librarian. **Stochastic:** fixed answer nahi, likelihood-spread se sample. **Temperature** boldness
  control karta hai. Sparse topic → weak prediction → confident guess.
- **Idea 2:** Training (one-time, past) vs Inference (har use, weights frozen). Correction ke baad "aap
  sahi hain" bolna seekhna nahi — sirf context window se continue karna (Idea 5). **Frozen kyun:** cost,
  safety/testing, consistency. Knowledge cutoff aur "private world nahi jaanta" isi se follow karta hai.
  "Memory" features weights nahi badalte — product notes wapas feed karta hai.
- **Idea 3:** Koi doosri faculty nahi jo check kare sach hai ya nahi — **hallucination malfunction nahi,
  built-in behaviour hai** (thin text + majboori continuation + no auditor = confident invention).
  Example: tuition academy ki fabricated fee table.

## 02 — Part 2: Why It Behaves This Way (Ideas 4-7)
- **Idea 4 (Tokens):** Letters/words nahi, chunks mein padhta hai. Explains: letter-miscounting,
  wordplay-weakness, typo-tolerance, token-based cost/limits. Token = meaning + memory + money unit.
  Non-English scripts zyada tokens/word lete hain (mehnga + context jaldi bharta hai).
- **Idea 5 (Context window):** Sirf ek jagah jahan model specifics dekh sakta hai — "reading desk, brain
  nahi." Tenants: prompt, history, files, system prompt. 200K tokens ≈ 150K words; 1M ≈ 750K words —
  finite aur shared. Chat history = poora transcript replay har turn (model kuch store nahi karta, app
  karta hai). Skills = progressive disclosure (desk se bahar, demand pe load).
- **Idea 6 (Confidence):** Learned style (RLHF se), truth signal nahi. Explains sure-sounding-when-wrong
  aur sycophancy. Fixes: neutral framing, explicit criteria scoring.
- **Idea 7 (Jagged frontier):** Ability smooth nahi, jagged — hard task pe brilliant, easy-adjacent task
  pe fail, human-intuition se match nahi karta. 3 habits: hard-success ≠ easy-success guarantee, verify
  at boundary not middle, 2-3 models try karo. Frontier shift karta rehta hai — re-test schedule pe.

## 03 — Part 3: Predictor to Agent (Ideas 8-9)
- **Idea 8 (Tools):** Predict-act-observe loop — model action predict karta hai, product real mein
  chalata hai, result context mein wapas aata hai, dobara predict. Connectors = MCP standard plug + 
  per-service appliance; result bhi text ban kar desk pe aata hai. **Agent ki mechanical definition:**
  wahi predictor, tools ke saath, loop repeat karta hua.
- **Idea 9 (Thinking):** Answer se pehle lambi intermediate-working prediction — phir usi ko context mein
  rakh kar final answer predict karta hai. Genuinely helps (jaisa insaan ko paper pe sochna help karta
  hai), lekin second faculty nahi deta — reasoning chain ke andar bhi confidently hallucinate kar sakta
  hai. Extra tokens = extra cost/time.
- Jaan-boojh kar chhoda gaya: training compute/cost, safety/alignment, weights ki deeper mechanics.

## 04 — Recap + Practice Prompts
- 9 ideas ka ek-line recap (Idea 1 se 9 tak).
- **6 hands-on prompts (~25 min):** (1) invented "Karakush" game rules se prediction-not-lookup dekho,
  (2) correction ke baad nayi chat mein learning-loss dekho, (3) fake citations se missing truth-checker
  pakro, (4) "quote my first message" se transcript-replay confirm karo (nayi chat mein fail), (5) hard+
  easy task saath se jagged frontier feel karo, (6) thinking on/off compare karo.

## 05 — Appendix: Claude.ai Cockpit Tour (A.1-A.10) + Sources
- A.1 Onboarding (free plan, 5-hour token-based limit). A.2 Window controls (prompt box=Idea5,
  model selector=Idea2/7, thinking control=Idea9). A.3 Model ladder logic (default middle, escalate for
  depth, drop for bulk). A.4 Thinking/effort dial. A.5 **Desk tenants as product settings** (core
  section): account instructions, Projects (pre-loaded desk), Memory (self-updating note, not weight
  change), chat history/search (retrieval-then-context). A.6 Uploads (files→tokens, image fine-print
  weak). A.7 Artifacts/Files (Idea 8 visible — surgical iteration). A.8 Tools menu: web search, Research
  (full agent loop), Skills (progressive disclosure, draft-review-enable-test), Connectors (MCP). A.9
  30-min setup checklist (7 steps mapping back to ideas). A.10 What changes (products) vs what doesn't
  (the 9-idea mapping). Sources: Anthropic prompt-eng docs, Claude Help Center, OpenAI tokens article,
  Ouyang et al. 2022 (RLHF), Dell'Acqua et al. 2023 (jagged frontier), Karpathy "Intro to LLMs".
