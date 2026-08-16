# 04 — Part 5: Judgment + Practice Projects + Glossary

## Kab AI Par Tekiya Na Lagao

Reading fluency ki ek ceiling hai, aur uske baare mein honest hona khud ek skill hai.

- **Security-sensitive code non-negotiable hai.** Passwords, API keys, payments, user data — carefully
  parho, ideally kisi domain-expert se review karwao. AI confidently insecure code likhta hai.
- **Jab genuinely parh nahi sakte, tests par zyada tekiya lagao, faith par nahi.** Agar generated
  function aapke level se upar hai, aapke `pytest` checks **zyada** important ban jate hain — yeh woh
  hissa hai jo aap verify kar sakte ho.
- **Chote, obvious changes kabhi haath se tez hote hain.** Ek variable rename karna khud karna describe
  karne se tez ho sakta hai.

## Apne Tests Ko Red-Team Karo

Aapke tests hi woh verification hain jo aap poori tarah control karte ho — kamzor test koi test na hone
se bura hai, kyunki yeh false confidence deta hai.

- **Agent ko kabhi apne code ke tests khud likhne mat do.** Yeh woh anti-pattern hai jo poore course ko
  chupke se defeat kar deta hai — agar AI code aur check dono likhe, koi independent signal nahi hai.
- **Agent ko test kamzor kar ke pass karwane mat do.** Jab test fail ho, agent kabhi kabhi **test** ko
  "fix" karta hai — assertion loosen kar ke, edge case delete kar ke. Yeh red ko green banata hai lekin
  bug wahin rehta hai.
- **Sirf happy path nahi, failures bhi test karo.** Har unit se poocho: *kaunsa input isay tod dega?*
  Empty list, zero, negative number, missing key.
- **Agar ek bhi test nahi soch sakte, aap abhi isay samajhte nahi.**

## Diff Review Karo Accept Karne Se Pehle

Claude Code/OpenCode sirf jawab nahi deta — **files badalta hai.** Har batch accept karne se pehle:

1. Kaunsi files badli? Ek function fix karne ki request se paanch files chhoona nahi chahiye
2. Kya tests badle? Agar haan, pehle wajah dhoondo
3. Kya dependencies add hui? Har naya package check karo zaroori aur real hai
4. Kya kuch sensitive touch hua? Secrets, keys, auth — carefully parho
5. `pytest`, Pyright, Ruff sab pass? Green sabka **floor** hai, ceiling nahi
6. Kya aap main function/class plain English mein explain kar sakte ho? Nahi to verify nahi kar sakte
7. **Kya code abhi bhi badalna aasan hai?** Same rule do jagah likha, ek function jo chupke se teen kaam
   karne laga, naam jo ab code se match nahi karta — tests yeh flag nahi karenge kyunki jawab abhi bhi
   sahi hai. Nuksan har us change mein hota hai jo aap aaj ke baad karte ho.

> **Poore course ka nichor:** Agent code lata hai; **aap judgment late ho** ke sahi hai ya nahi, aur kya
> yeh agle mahine bhi workable rahega. Yeh judgment fluent reading aur aapke likhe tests par khara hai.

## 6 Practice Projects (Overview)

Course mein 6 hands-on projects hain jo PRIMM-AI+ ko order mein chalate hain — parhna se lekar khud
banane tak:

1. **Read and predict** — function/comprehension parh kar output predict karna, phir verify
2. **First TDG cycle on a function** — `initials()` function tests-first banana
3. **TDG on a class** — `TaskList` class banana, ek silent bug khud pakarna (unknown task complete karna)
4. **Find the bug in agent code** — plausible-lagta code jisme ek real bug chhupa ho, test se pakarna
5. **Mini-capstone: Notes tool end-to-end** — poori TDG cycle, Pydantic model + class + generator +
   f-string sab ek sath
6. **On your own** — koi starter nahi, koi test nahi, sirf ek sentence: *"paragraph ke 3 most common
   words print karo."* Khud decompose karo, spec karo, generate/verify karo

**Solutions ka sabse kam important hissa reference code hai.** Jo matter karta hai: kya aapke tests ne
"correct" ka matlab pakra? Kya aap ne output sahi predict kiya?

## Self-Check — Kya Aap Pass Ho Gaye?

7 cheezein bina notes ke kar sako to course kaam kar gaya:

1. Function signature parh kar plain English mein explain karna
2. Kisi unit ke liye kam az kam 3 `pytest` tests likhna, code banne se **pehle**
3. AI agent ko un tests ke against implement karne ko kehna, typed signature ke sath
4. `pytest`, Pyright, Ruff chalana aur samajhna
5. Traceback bottom-up parh kar problem precisely describe karna
6. AI-generated code mein ek plausible-but-wrong bug pakarna
7. Ek vague, one-sentence goal ko testable units mein todna

## 60-Second Glossary

| Term | Aasan Matlab |
| --- | --- |
| **PRIMM-AI+** | Predict · Run · Investigate · Modify · Make — read-first method, agent partner ke sath |
| **TDD → TDG** | Test-Driven Development → Test-Driven Generation: failing test aap likho, code agent likhe |
| **`assert`** | Ek-line claim jaise `assert x == 5` — sach ho to kuch nahi, jhoot ho to crash |
| **Type/type hint** | Data ka label (`str`, `int`) — aur agent ke liye precise instruction |
| **list/dict/set/tuple** | 4 containers — dict (labeled pairs) sabse zyada milega |
| **Class/object** | Class blueprint hai; object (instance) uska bana hua cheez |
| **`self`/attribute/method** | `self` = "yeh object"; attribute = data; method = action |
| **Comprehension** | `for` loop ek line mein fold, nayi list banane ke liye |
| **f-string** | `f"..."` — `{...}` ki jagah value bharti hai |
| **Generator/`yield`** | Items ek waqt mein wapis deta hai — pile nahi, stream |
| **`with`** | Kholta hai, use karta hai, error ke bawajood safely band karta hai |
| **`async`/`await`** | Kai slow cheezein (jaise API calls) ek sath karne wala code |
| **Dunder (`__call__`, `__init__`)** | Double-underscore methods jo objects ko native cheez jaisa banate hain |
| **Decorator (`@name`)** | Function/class ke upar label jo behavior add karta hai |
| **Pydantic** | Structured data validate karta hai, LLM tool-calling ke JSON schemas banata hai |
| **pytest/Pyright/Ruff/uv** | Verification tools: test chalao / types check karo / style check karo / Python manage karo |
| **Traceback** | Python ka error report — bottom-up parho; last line problem naam leti hai |

## Yahan Se Aage

- **Build AI Agents** — jo Pydantic models, `async`/`await`, type hints ab pehchante ho, woh agent code
  ka rozana material ban jate hain
- **Postgres for AI** — data store/retrieve karne wala code parhna
- **Building a Digital FTE** — sab kuch assemble kar ke ek working AI worker banana

---
[⬅ TDG Loop](03-tdg-loop.md) · [⬆ Index](README.md)
