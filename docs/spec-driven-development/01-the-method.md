# 01 — The Method

Workflow: **1 foundation (constitution) + 4 phases (Research → Specify → Clarify → Build).**

## Concept 4: Constitution — Har Spec Ke Upar Ke Rules

Ek chhoti document jo **sab** features ke liye persistent rules rakhti hai. Coding agents mein rules
file (`CLAUDE.md`/`AGENTS.md`), claude.ai mein **Project instructions**.

> **Ehtiyat:** Constitution **persistent context hai, enforced law nahi.** Jo rules **kabhi** break
> nahi honi chahiye (production data mat chhuo), sirf written rule pe trust mat karo — tests, hooks, CI
> checks se back karo.

```markdown
# Constitution — Smart Notes
## Principles
- Plain language over cleverness.
- Prefer well-established libraries over custom code.
- Every feature ships with its spec in specs/.
## Constraints
- Stack: keep it to what's already here.
- Never touch published/ or src/generated/.
## Definition of done
- Behaviour matches the spec, edge cases included.
- A human has reviewed the diff against the spec before merge.
```

> **Zyada sakht constitution har cheez ko zeher deti hai:** Weekend habit-tracker ko 90% test coverage,
> performance budget wali constitution do — button jo list mein ek row add karta hai, benchmark harness
> + 3 layers of abstraction ke sath ship hota hai. **Constitution ko stakes se match karo.**

**Test:** *"Ise hatane se AI galti karega?"* "Clean code likho" fail hota hai (AI already koshish karta
hai). "published/ mat chhuo" pass hota hai (AI ko khud pata nahi chal sakta tha).

## Concept 5: Phase 1 — Research Se Pehle

Spec likhne se pehle, AI se territory map karwao: problem, users, constraints, existing code kaise kaam
karta hai.

**Power move: parallel research.** Coding agents mein, **subagents** se ek ek area research karwao,
apni window mein, summary wapas do.

```text
Research what's involved in building [feature]. Investigate these
separately: (1) how this is usually done, (2) main approaches and
trade-offs, (3) existing project fit, (4) failure modes. Give me a
one-page findings doc. Don't propose a final design yet.
```

## Concept 6: Phase 2 — Spec Likho (What Aur Why, Kabhi How Nahi)

**6 sections:**
- **Goal** — why, 2-3 sentences
- **User scenarios** — "jab user X kare, Y milta hai"
- **Functional requirements** — testable musts
- **Edge cases & rules** — empty, huge, duplicate, unauthorized
- **Out of scope** — ye kabhi mat skip karo
- **Acceptance criteria** — "done" ki checklist

**"Tighten by hand" ka matlab:**
> **Pehle:** "Users apna password reset kar sakte hain."
> **Baad mein:** "Signed-out user email se password reset request kar sakta hai. Link ek dafa kaam
> karta hai, 30 minute mein expire hota hai... response kabhi reveal nahi karta email registered hai
> ya nahi."

Pehli line ek build ko pass kar degi jo plaintext password kisi ko bhi email kar de. **Doosri sirf wo
cheez pass kar sakti hai jo aap ne asal mein mani thi.**

## Concept 7: Phase 3 — Interview Se Clarify Karo (AI Se Poochwao)

**Sab se zyada value wala, sab se zyada skip hone wala step.** Sawal poochne ki bajaye, AI se **aapko**
interview karwao:

```text
Before we build anything, interview me about this spec. Ask one
question at a time, focusing on ambiguities, missing edge cases,
and unstated assumptions. Keep going until you could hand this
spec to a stranger and trust they'd build exactly what I mean.
```

> **Ye process ki sab se sasti jagah hai galti fix karne ki:** spec mein fix karna ek sentence, baad
> mein fix karna poora rebuild.

**Skip karne pe:** *"users profile photo upload kar sakte hain"* — sab nod karte hain, ship ho jata hai.
Ek din mein: koi 40MB TIFF upload karta hai (size limit nahi thi), 2 users ek dusre ki photo overwrite
karte hain (uniqueness rule nahi thi), broken file blank render hoti hai (fallback nahi tha). **3 bugs,
jo interview mein 3 sentences hote.**

## Concept 8: Phase 4 — Spec Se Build Karo

Process ka size change ke barabar hai:
- **1-sentence change** (typo, ek rule) — sirf poocho, plan skip karo
- **Approach uncertain, kuch files touch** — pehle plan karo
- **Multi-file/architectural** — poora loop: plan → build → verify

**2 cheezein hamesha constant:** Code se pehle approach review karo. Result ko spec ke against check
karo — **verify kabhi skip nahi karte.**

> **Kaun tasks mein todta hai? Agent khud.** Aap hand-written task list nahi likhte — Claude Code/
> OpenCode apna khud ka tracked checklist banate hain. **Aapka kaam breakdown review karna hai.**

```text
Plan: Based on the agreed spec, propose a technical plan... Don't
write code yet; I'll review the plan first.

Build: Implement the agreed plan in small, checkable steps. Do one
step at a time, check against the spec, stop for confirmation.
Commit after each.
```

> **Strong model se plan karo, cheap model se implement karo** — same Plan/Execute split jo coding
> course mein tha.

> **2nd check: kya shape abhi bhi sahi hai?** Acceptance criteria behavior prove karte hain, system
> healthy hai ya nahi wo nahi. Har chand build cycles, ek design pass chalao — agent isme khud ka bura
> judge hai (passing build ke liye optimize karta hai, cheap-to-change system ke liye nahi).

---
[⬅ The Shift](00-the-shift.md) · [Agla: Three Ways ➡](02-three-ways.md)
