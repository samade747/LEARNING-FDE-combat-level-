# 05 — Harness Engineering

*Source: `harness-engineering-crash-course` (Zia Tutor AI, corpus gen 62). Deep notes (+ 18-Q test +
8 projects): [`docs/harness-engineering/`](../../harness-engineering/README.md).*

> **Loop vs Harness (exam ka #1 trap):** Loop = **kab** chalta hai + **kya yaad** rakhta hai
> (heartbeat, spine). Harness = **ek beat ke andar** kya allowed / kya pata / kaam kaise proven / kuch
> ghalat ho to kya. **Missing heartbeat aur missing deny-rule do bilkul alag bugs hain.**

---

## A. Agent = Model + Harness

- Model **intelligence** deta hai. Harness usay **reliable** banata hai. Tum harness already use kar
  rahe ho (Claude Code, OpenCode) — bas default settings par. Course = usay **jaan-boojh kar
  engineer** karna.

### Harness ke 4 zaroori parts (2026 paper ki exact definition)

1. **Agent loop** — chhota engine jo model ko chalata rehta hai
2. **Tool interface** — jo actions model le sakta hai + har action ki shape
3. **Context management** — window mein kya, kya compact, kya file mein
4. **Control mechanisms** — permissions, limits, checks — **"nahi" kehne wale parts**

### Inner vs Outer harness

| | Inner harness | Outer harness |
| --- | --- | --- |
| Kisne banaya | model ka maker (native tool calling, context limits, safety training) | tum (ya Claude Code/OpenCode jo tum configure karte ho) |
| Tum kar sakte ho | sirf **choose** (model chun kar) | **configure / build** |

**Sawal jo yeh split solve karta hai:** *"behtar prompt se theek karoon ya behtar rule se?"* Agar
masla ye hai ke agent **kya kar sakta**, **kya jaanta**, ya kaam **kaise check hota** — fix **outer
harness** mein; prompt sirf chupa dega. **Prompts task ke liye; harness har task mein hamesha sach
rehne wali cheezon ke liye.**

## B. The 5 Verbs — Har Harness Surface Inhi Mein Se Ek Kaam Karti Hai

| # | Verb | Kya | Surfaces |
| --- | --- | --- | --- |
| 1 | **Constrain** | agent kya kar sakta hai limit karo | permission rules, deny lists, sandboxes |
| 2 | **Inform** | agent ko sab do jo kaam ke liye chahiye | rules file, skills, connectors |
| 3 | **Verify** | kaam ko count hone se pehle prove karo | hooks, tests, linters, typed output |
| 4 | **Correct** | ghalat ho to run recover karo, phir harness badlo | recovery + ratchet |
| 5 | **Escalate** | harness decide na kar sake → insaan ko bhejo **visibly** | typed-output fallback, "needs a human" |

> **Poore course ka jumla:** **Guardrail hamesha harness mein rehta hai, prompt mein kabhi nahi.**
> Road sign *puchta* hai; steel barrier *rokta* hai. `"please .env touch mat karna"` = request (model
> ignore/bhool sakta hai). `.env` par deny rule = tool layer par khud enforce.

| Surface | Behavior guide? | Mechanically enforce? |
| --- | --- | --- |
| Prompt / rules file / tool description | ✅ | ❌ |
| Permission deny rule | ✅ | ✅ tool layer |
| Sandbox / network fence | ✅ | ✅ OS layer |
| Hook (action ke baad) | ✅ | sirf forward — jo ho chuka undo nahi |
| Required CI check + branch protection | ✅ | ✅ merge par |

**Jitni lambi chain, utni kamzor:** har step 95% → 20 steps chain = ~**36%** clean runs. Behtar model
95 ko thoda barhata hai; **harness poori chain par attack karta hai**. Harness-only changes (bina model
badle) coding benchmarks par **10x tak** gains. 2026 mein top models qareeb — **box (harness) ab zyada
farq daalti hai**.

## C. Constrain

### Permission rules — Allow / Ask / Deny

- **Allow** = green light · **Ask** = doorbell (insaan se haan) · **Deny** = deewar (kabhi nahi)
- **Design skill:** har action ko **blast radius** (galat ho to kitna nuksan) se sort karo — **kitni
  baar hota hai se NAHI**.
- Secrets parhna → deny/isolate · test chalana → allow · branch push → ask (ya sirf `claude/`) ·
  worktree se bahar delete / force-push / harness config badalna → **deny**.
- **Jab shak ho, sakht bucket rakho** — hafte bhar clean runs ke baad loosen karna sasta; deleted prod
  DB explain karna nahi.
- Paisa bhi constrain hai: per-run spend cap, step cap, konsa model konsa job.
- **Priority: Deny > Ask > Allow** — broad allow kabhi narrow deny ko leak nahi karta.
- **Honesty:** deny patterns **command text** match karte hain, **matlab nahi** (`rm -rf` `rm -fr` ya
  Python one-liner ko nahi pakregi) → **tripwires**, asli deewar **sandbox** hai.

### Sandboxes — nuksan ko namumkin banana

- Permission = agent **kya** karta hai; sandbox = **kahan** kar sakta hai. Perfect rules wala agent
  bhi prompt injection se kuch aisa try kar sakta hai jo list hi nahi tha.
- **4 fences:** worktree · filesystem fence · network fence (internet reach nahi → injected instruction
  code leak nahi kar sakti) · branch fence (`claude/` only, `main` human gate ke peeche).
- **Prompt injection ka doosra form — tool poisoning:** attack **tool ki apni description/metadata**
  mein chupa (jo agent decision ke waqt trust karta hai). Poisoned MCP server hidden instructions,
  session-persistence, "rug-pull" (install par achha, baad mein malicious update). **Defense:** MCP
  servers ki **enforced, version-pinned allowlist**.
- **Defense in depth:** har fence akela kaam kare, kai chalao (koi ek misconfigure ho sakta hai).

## D. Inform

### Context surfaces — har beat ek sawal ka jawab

| Surface | Jawab | Cost |
| --- | --- | --- |
| **Rules file** | *yahan hamesha kya sach hai?* | har line har beat par — **chhota rakho** |
| **Skills** | *ye specific kaam kaise?* | sirf match par load — detail tab tak "free" |
| **Connectors** | *ye kya reach kar sakta, kaise?* | inform **aur** constrain decision, ek sath |

**Bug triage (10 sec):** agent ko kuch **pata nahi tha** → hamesha-sach = rules file · task-specific =
skill · reach = connector.

### AX — Agent Experience

- Har surface ka **reader = agent** (task ke beech, poori context window, tumse puchne ka koi tareeqa
  nahi). AX = us reader ke liye design karna (jaise UX human ke liye).
- **3 findings:** kam focused tools > bohot overlapping · **tool descriptions asal kaam karti hain**
  ("Searches customer DB by email or ID. Returns at most 20 rows" > "customer tool") · **error
  messages agla step batayein**.
- **Test har surface ke liye:** *kya ek competent ajnabi, sirf ye text dekh kar, sahi agla step le
  sakta hai?* Agent wahi ajnabi hai, **har beat par**.
- **Naming collision:** book ka "Designing Agent Experiences" = **insaan** ka agent-use tajurba;
  industry ka **AX** = **agent** ka tumhare system-use tajurba. Same letters, opposite reader.

## E. Verify

### Hooks — khud-chalne wali verification

- Maker-checker beat ke **end** par ek dafa; **hook musalsal** verify karta hai — harness khud, fixed
  moments par chalati hai, chahe model kuch bhi chahe.
- **Key word: "refuse".** Agent hook ko **skip/argue/bhool nahi sakta** — harness chalati hai, model
  nahi.
  - **Action se pehle** hook (`PreToolUse`, `Stop`) — action **poora rok** sakta hai (exit `2` = block)
  - **Action ke baad** hook (`PostToolUse`) — jo ho chuka **undo nahi** kar sakta; power = failure
    agent ke **agle turn** mein push kar de (khud heal)
- "Done" ab model ka claim nahi — **harness ka proven state**.
- OpenCode: **plugins** (`tool.execute.before/after`) + **git hooks/CI**. `pre-commit` = **pehli
  line** (bypass ho sakta `--no-verify`); **last line = required CI check + branch protection**.

### Typed output

- Verification chup-chaap tootti hai jab checked cheez **free text** ho. Reviewer *"This mostly
  passes, though I have doubts..."* → loop galat parhe ya ruk jaye. **Jiska verdict parse na ho, woh
  checker hai hi nahi.**
- **Fix:** fixed machine-checkable shape maango (JSON), phir **code se validate** karo — **har field
  allowed values ke against** (sirf `.verdict` exist check karna kaafi nahi — `{"verdict":"MAYBE"}`
  accept kar lega).
- Malformed verdict par: **hamesha retry NAHI, guess NAHI → escalate** (verb 5), visibly.

## F. Correct — 2 Clocks

| Clock | Kya | Beginners |
| --- | --- | --- |
| **Fast (Recovery)** | isi run ke andar kuch ghalat — agle second mein react | bhool jaate hain |
| **Slow (Ratchet)** | run khatam — yaqeeni banao yeh ghalti **kabhi wapas na aaye** | sirf yeh banate hain |

### Recovery — error classify karo

| Error type | Kya karo |
| --- | --- |
| **Transient** (network blip, rate limit, timeout) | retry, badhta wait, hard cap |
| **Hard failure** (missing permission, tool exist nahi) | retry mat karo (wahi fail degi) — skip/escalate |
| **Poisoned state** (run ne khud ko broken files mein phasa liya) | retry/reroute nahi — **wapas jane ka raasta** chahiye |

- **Checkpoint** = saved good state (video game save point). Sasta store = **git** — har verified step
  ke baad commit. Claude Code `/rewind`.
- **Production standard:** *crashed run **resume** karti hai, restart nahi* (restart = poori cost
  dobara).

### Ratchet — Hashimoto ka founding rule

> *"Jab agent ghalti kare, sirf kaam theek mat karo. Harness ko badal do taake woh ghalti **namumkin**
> ho jaye, phir aage barho aur kabhi is baare mein na socho."*

Ratchet ek taraf ghumta hai + lock. Har pakri failure **permanent part** ban jaati hai; harness sirf
**tight** hoti jaati hai.

### 4 Failure Classes — har ek ka apna ghar

| Failure class | Nishani | Verb | Fix kahan |
| --- | --- | --- | --- |
| **Context failure** | usay pata nahi tha (galat convention, missed constraint) | **Inform** | rules file / skill / tool description |
| **Constraint failure** | aisi cheez ki jo kabhi kar hi nahi sakna chahiye tha | **Constrain** | permission rule / sandbox / branch fence |
| **Verification failure** | bura kaam "done" keh diya, tests nahi chalayin | **Verify** | hook / required CI check / typed output |
| **Planning failure** | sahi pieces, galat order/size (bhatakna, bundled changes) | **Structure** (loop layer) | chhota task / subagent split / `steps` caps |

- **Practice:** har failure ke baad 5-min review — class naam do, us class ki surface par fix likho.
  **Same shape ki 2 failures namumkin honi chahiyen** — doosri dikhe = pehli galat classify hui.
- **Harness khud bhi test karo:** survey — ~90% ke paas observability, sirf ~50% offline evals. Fix:
  chhota fixed set of test tasks, har harness change ke baad dobara chalao.

## G. Staying the Engineer

### Observability

- **Chup-chaap fail hone wali loop koi loop na hone se bhi buri hai.** Blocked `.env` read raat ka
  **sabse valuable event** — sirf tab jab tum dekho (batata hai koi defenses test kar raha, deewar ne
  rok liya).
- **3 aadatein:** har beat ek jagah log (actions taken/blocked, verdict, cost — **spine = kaam ne kya
  kiya; harness log = system ne kya kiya**) · failure loud (chup = success, ya chup ka koi matlab
  nahi) · **cost as signal** (3x cost wali beat bhatak gayi — planning failure jo pehle cost mein
  announce hoti hai).

### Harness ki limits — 3 forces jo ratchet ko wapas kheenchti hain

1. **Capability vs Control trade-off** — har rule jo failure hataati hai, ek **move bhi** hataati hai.
   Max-tight harness = min-ambition kaam. **Tightness ko blast radius se match karo** (overnight loop
   tight, throwaway prototype loose — **tum** decide karte ho).
2. **Harness coupling** — ek model ki aadaton par over-fit harness khamoshi se **usi model ka hissa**
   ban jaati hai (token budgets ek tokenizer ke liye; nayi model gen ~30% zyada tokens). **Defense:**
   *behaviors* nahi, *contracts* (exit codes, schemas, tests) se couple; kabhi doosre model par chala
   kar dekho.
3. **Rule debt** — har rules line har beat par tokens, har hook har action par seconds, har ask-rule
   ek interruption. **Ek dafa ki oddity ke liye permanent rule = safety nahi, junk.** Monthly review:
   90 din se na-fire + koi linked incident nahi → removal candidate. **Secrets ki deewarein exempt.**

### Khud harness kab banao?

Jab tak Claude Code/OpenCode ki surfaces tumhari rules express kar sakti hain — unhi ke sath raho
(vendor harness khud har hafte behtar). **Khud tab** jab product ki deewarein aisi requirement rokein
jo tumhare paas asal mein ho: apna tool interface, apna verification stack, apna deployment shape.

> Loop tumhari **intent/accountability** nahi sambhal sakta. Harness bhi nahi. Harness sambhalti hai
> **judgment, permanent bana hua** — har rule ek decision jo tumne ek dafa liya, hamesha enforce hoti
> hai jab tum so rahe ho. **"Humans steer. Agents execute."**

---

## Ek-Line Revision (M5)

> Agent = Model + Harness · 4 parts: agent loop / tool interface / context mgmt / control · 5 verbs:
> **Constrain · Inform · Verify · Correct · Escalate** · guardrail hamesha harness mein, prompt mein
> kabhi nahi · allow/ask/deny — **blast radius se sort, frequency se nahi**; Deny>Ask>Allow · deny =
> text match not meaning (tripwire), sandbox = asli deewar · 4 fences (worktree/fs/network/branch) ·
> hook = "refuse", model skip nahi kar sakta · typed output — har field validate ya escalate · Correct
> = recovery (fast) + ratchet (slow) · **4 failure classes → 4 verbs** · resume not restart · 3 limits:
> capability-vs-control / coupling / rule debt.

---

## MCQ Practice (jawab neeche)

1. Loop aur Harness ka farq:
   a) Same b) Loop = kab chalta + kya yaad; Harness = ek beat ke andar allowed/known/proven/on-error
   c) Loop naya, Harness purana d) Harness = scheduler

2. "Agent =" kya?
   a) Model b) Model + Harness c) Model + Prompt d) Loop + Spine

3. 5 verbs mein "insaan ko visibly bhejna":
   a) Constrain b) Verify c) Escalate d) Inform

4. Guardrail kahan rehna chahiye?
   a) Prompt mein b) Rules file mein c) Harness mein — prompt mein kabhi nahi d) Tool description mein

5. Permission buckets kis se sort karne chahiye?
   a) Frequency (kitni baar) b) Blast radius (galat ho to kitna nuksan) c) Alphabetical d) Cost

6. Permission priority order:
   a) Allow > Ask > Deny b) Deny > Ask > Allow c) Ask > Deny > Allow d) Sab equal

7. `Bash(rm -rf *)` deny rule `rm -fr` ya Python one-liner ko rokegi?
   a) Haan b) Nahi — text match karti hai, matlab nahi; ye tripwire hai, asli deewar sandbox
   c) Sirf Claude Code mein d) Haan agar auto mode on ho

8. Network fence prompt injection ke against kaise madad karta hai?
   a) Injection detect karta b) Agar internet reach hi nahi, injected instruction code leak nahi kar
   sakti c) Model ko warn karta d) Logs rakhta

9. "Tool poisoning" kya hai?
   a) Bug report mein command b) Attack tool ki apni description/metadata mein chupa (jo agent trust
   karta hai) c) Slow tool d) Duplicate tool

10. Hook ko "harness part" kya banata hai (suggestion ke bajaye)?
    a) JSON format b) "Refuse" — agent skip/argue/bhool nahi sakta, harness chalati hai model nahi
    c) Exit code d) Speed

11. `PostToolUse` hook exit `2` kya karta hai?
    a) Edit undo b) Edit ho chuki — undo nahi; error text agent ke agle input mein wapas (khud heal)
    c) Session band d) Kuch nahi

12. Typed output validate karte waqt:
    a) Sirf `.verdict` exist check karo b) Har field allowed values ke against — warna `{"verdict":
    "MAYBE"}` accept ho jayega c) Length check d) JSON hai ya nahi

13. Malformed reviewer verdict par harness kya kare?
    a) Hamesha retry b) Guess kar le c) Escalate (verb 5) — visibly d) Ignore

14. Recovery mein "hard failure" (missing permission) ka jawab:
    a) Retry with backoff b) Retry mat karo — wahi call hamesha wahi fail degi; skip/escalate
    c) Checkpoint se resume d) Ratchet

15. Hashimoto ka ratchet rule:
    a) Kaam theek karo, aage barho b) Harness badal do taake woh ghalti namumkin ho jaye, phir kabhi
    na socho c) Model badlo d) Rule delete karo

16. 4 failure classes ki mapping:
    a) Context→Inform, Constraint→Constrain, Verification→Verify, Planning→Structure(loop)
    b) Sab Verify c) Sab prompt d) Context→Constrain, baaki→Inform

17. "Rule debt" ka fix:
    a) Zyada rules b) Monthly review — 90 din se na-fire + koi linked incident nahi → removal
    candidate (secrets ki deewarein exempt) c) Kabhi delete mat karo d) Sirf hooks rakho

18. "Capability vs control trade-off":
    a) Zyada rules = zyada capability b) Har rule jo failure hataati hai ek move bhi hataati hai;
    tightness ko blast radius se match karo c) Control hamesha behtar d) Model se control aata hai

### Jawab Key

1‑b · 2‑b · 3‑c · 4‑c · 5‑b · 6‑b · 7‑b · 8‑b · 9‑b · 10‑b · 11‑b · 12‑b · 13‑c · 14‑b · 15‑b · 16‑a
· 17‑b · 18‑b

---
[⬅ 04 — Loop Engineering](04-loop-engineering.md) · [Agla: 06 — Trusting the Checker ➡](06-trusting-the-checker.md)
