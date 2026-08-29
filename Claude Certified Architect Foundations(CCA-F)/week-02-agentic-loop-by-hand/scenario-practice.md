# Week 2, Hour 3 — Scenario Practice (12 items)

*Format: har item — best answer, kyun best, distractors kyun kamzor, kaunsa principle. Domain 1,
Task 1.1 focus.*

---

**1.** Ek loop response ke `.content` mein `text` block dekh kar return kar deta hai. Kabhi kabhi tool
calls silently miss hote hain. Best fix?

- **A. `stop_reason == "end_turn"` par return karo, warna tool_use blocks process karo ✅**
- B. Har turn ke baad model se pucho "kya tum done ho?"
- C. Response mein "final answer" string dhoondo
- D. Ek router agent add karo jo decide kare turn final hai ya nahi

**Best: A.** Protocol ka signal (`stop_reason`) hi authoritative hai. B/C prose-parsing hain
(unreliable). D symptom-patch — complexity add karta hai bina root cause chhue. *Principle: completion
protocol se decide hota hai, content shape se nahi.*

---

**2.** Multi-tool turn mein model 3 tools call karta hai. Loop pehla execute karta hai, phir agli API
call karta hai. Symptom: model adhoore data par jawab deta hai. Root cause?

- **A. Loop sirf `tool_use_blocks[0]` execute karta hai ✅**
- B. Model ko parallel tools support nahi
- C. `max_tokens` bahut kam hai
- D. `tool_choice` `auto` par hai, `any` hona chahiye

**Best: A.** Har `tool_use` block execute hona chahiye, sab ke `tool_result` ek user turn mein. B
galat (model parallel calls emit kar raha hai). C/D unrelated. *Principle: har tool_use block, sirf
pehla nahi.*

---

**3.** Ek stateless Messages API loop dobара chalne par model "bhool jata hai" usne pichle turn kya
kaha. `messages` list mein user turns aur tool_result turns hain. Kya missing hai?

- **A. Assistant ke apne turns (`{"role": "assistant", "content": response.content}`) ✅**
- B. System prompt
- C. `tool_choice` parameter
- D. `metadata` field

**Best: A.** Stateless API — poori history har call mein bhejni hai, **assistant turns bhi** (tool_use
blocks sameet). *Principle: history maintenance loop ki zimmedari hai.*

---

**4.** Structured extraction: aap chahte ho model **hamesha** ek specific `extract_invoice` tool call
kare, kabhi plain text nahi. Kaunsa `tool_choice`?

- **A. `{"type": "tool", "name": "extract_invoice"}` ✅**
- B. `{"type": "auto"}`
- C. `{"type": "any"}`
- D. `{"type": "none"}`

**Best: A.** Forced specific tool. C (`any`) koi bhi tool force karta hai — agar sirf ek tool hai to
kaam karta hai lekin intent A se kam clear. B model ko choice deta hai. D tool use rokta hai.
*Principle: Task 4.3 — guaranteed-shape output = forced tool + JSON Schema.*

---

**5.** `stop_reason == "max_tokens"` mila. Loop kya kare?

- **A. Response truncated hai — retry with more budget ya error; content parse mat karo ✅**
- B. `end_turn` ki tarah treat karo, jo mila woh return karo
- C. Turn dobara bhejo bina kuch change kiye
- D. `tool_use` samajh kar tools chalao

**Best: A.** Truncated output incomplete/invalid ho sakta hai. B silently corrupt data deta hai.
*Principle: har stop_reason ka apna handling — sirf `end_turn` par parse.*

---

**6.** Loop `while True` hai. Model baar baar wahi tool call maangta hai. Kya hota hai, aur do fixes?

- **A. Infinite loop + cost. Fix: (1) `MAX_TURNS` ceiling, (2) check kyun result nahi pahonch raha (missing `tool_result`) ✅**
- B. Kuch nahi, model khud ruk jayega
- C. API rate-limit se ruk jayega, safe hai
- D. Sirf `MAX_TURNS` add karo, kaafi hai

**Best: A.** Ceiling crash rokta hai (symptom), lekin asal root cause aksar Bug 2 (lost tool_result)
hai. *Principle: symptom aur root cause dono address karo.*

---

**7.** Ek tool successfully chalta hai lekin khali list return karta hai (koi record nahi mila). Doosra
tool permission error deta hai. Loop dono ko same treat karta hai. Theek?

- **A. Nahi — successful-empty aur access-failure alag hain; tool_result mein `is_error` distinguish karta hai ✅**
- B. Haan, dono "no data" hain
- C. Dono par retry karo
- D. Dono par escalate karo

**Best: A.** Empty valid result = "koi record nahi" (aage badho). Access failure = "pata nahi" (retry
/ report). *Principle: successful empty ≠ failure — Domain 5 (reliability) se overlap.*

---

**8.** `tool_result` block mein `tool_use_id` galat/missing hai. Symptom?

- **A. Model result ko apni call se jod nahi pata — confused, dobara call kar sakta hai ✅**
- B. API 500 error
- C. Tool dobara execute hota hai
- D. Kuch nahi, id optional hai

**Best: A.** `tool_use_id` woh key hai jo result ko call se match karti hai. *Principle: round-trip
correlation exact id par depend karta hai.*

---

**9.** Team kehti hai "loop reliable nahi, ek dispatcher agent add karte hain jo har turn decide kare."
Aap architect ho. Response?

- **A. Pehle stop_reason handling + history + tool_result plumbing inspect karo — yeh classic loop bugs hain, dispatcher complexity nahi chahiye ✅**
- B. Haan, dispatcher agent add karo
- C. Multi-agent system mein convert karo
- D. Model badal do

**Best: A.** "Loop flaky hai" ke 5 classic root causes deterministic bugs hain. Dispatcher = routing
complexity jo root cause nahi chhuti. *Principle: root cause fix, symptom nahi; simplest pattern.*

---

**10.** `tool_choice: "any"` set hai. Loop `end_turn` ka intezaar karता hai. Kya hoga?

- **A. `end_turn` kabhi nahi aayega (model har turn tool call karne par majboor) — loop `MAX_TURNS` par galat error dega ✅**
- B. Normal chalega
- C. API error
- D. Model ek dafa tool call karke `end_turn` de dega

**Best: A.** `any` / forced tool ke sath model text-only turn nahi de sakta, isliye `stop_reason`
hamesha `tool_use`. Loop ko is mode ke liye alag exit condition chahiye. *Principle: tool_choice loop
ki control flow badal deta hai.*

---

**11.** Homework check: Agent SDK by-hand loop ki kaunsi cheez aapke liye handle karta hai?

- **A. History accumulation, tool_use→tool_result plumbing, stop_reason branching, turn ceiling, parallel tool execution ✅**
- B. Sirf authentication
- C. Sirf retries
- D. Kuch nahi, wrapper hai

**Best: A.** Yehi 5 cheezein Week 2 ne haath se banayi. SDK inhe internal karta hai — lekin
architect ko pata hona chahiye andar kya ho raha hai (exam Task 1.1). *Principle: abstraction samajh
kar use karo.*

---

**12.** Ek turn mein `content` = `[thinking, text, tool_use]`. `stop_reason` = `tool_use`. Loop kya kare?

- **A. `thinking`/`text` ko history mein rakho, `tool_use` execute karo, `tool_result` append, continue ✅**
- B. `text` return karke ruk jao
- C. `thinking` block error hai, discard karo
- D. Sirf `tool_use` history mein rakho

**Best: A.** Poora content block-for-block history mein; branch `stop_reason` par. B = Bug 3. D =
partial history, model confuse hoga. *Principle: full content preserve, stop_reason par branch.*

---

## Score / weak spots

*(Self-graded jab attempt karo — abhi yeh answer key + rationale hai. Week 12 six-scenario workshop
se pehle dobara blind attempt karna.)*
