# 02 — Memory Aur Model-Swap (Scenarios 4-5)

## Scenario 4: Fresh Session Mein Bhi Yaad Rakhta Hai, Koi Commit Nahi (~15 min)

**Yehi OpenClaw se sab se sharp contrast hai.** OpenClaw mein aap ne ek **wall** prove ki thi — memory
per-channel thi, cross karne ke liye **deliberately commit** karna parta tha. **Hermes wall aur chore
dono hataata hai.** Khud memory curate karta hai, past sessions se **full-text search** ke zariye recall
karta hai.

**Step 1 — in-flight fact sikhao, chale jao:**
```text
Quick context for you to hold onto: I'm preparing a board update
for Thursday, and the number I'm worried about is churn.
```

**Step 2 — genuinely fresh session shuru karo:** TUI mein `/new` bhejo (ya alag surface se message karo).

**Step 3 — bina yaad dilaye poocho:**
```text
What was I worried about for this week, and what's the deadline?
```
Jawab deta hai — apni **past-session recall** se, aap ne dobara bataya nahi. **Koi `MEMORY.md` commit
nahi, koi `/reset` nahi. Khud wall cross ki.**

**Step 4 — apna model dekho:**
```text
Show me what Hermes has written about me so far: open
~/.hermes/memories/ and summarize USER.md and MEMORY.md.
```

**Done jab:** Step 3 mein fresh session ne in-flight fact yaad ki bina bataye, **aur** aap ne `memories/`
apni ankhon se parhi ho.

> **Contrast, saaf lafzon mein:** OpenClaw: **aap** commit karte ho, isliye memory auditable hai
> (aap ne likhi). Hermes: **wo** commit karta hai, isliye memory bina mehnat compound hoti hai — **isi
> liye periodically `memories/` parhna zaroori hai.** Convenience ne kaam *"yaad rakhna ke save karna
> hai"* se *"check karna kya save hua"* mein move kar diya.

## Scenario 5: Skill Reuse Karo, Model Swap Karo, Prove Karo Lock-In Nahi Hai (~15 min)

**2 proofs, ek idea:** Hermes mein **model replaceable part hai.** Durable asset skill-and-memory layer
hai, jo koi bhi brain use kar sakti hai.

### 5a: Skill Reuse Aur Improve Karo

Similar (identical nahi) task bhejo Scenario 3 se. Log dekho — agent **pehle likhi skill load karta hai**
from scratch ki bajaye, aur review karte waqt **usi skill ko update** karne ki taraf jhukta hai.

```text
Compare the skill now to what it was after Scenario 3. Did it get
updated or version-bumped?
```

> **Real self-improvement kaisi lagti hai:** Ek live run mein, skill v0.1.0 se v1.0.0 tak jump ki. Usne
> clumsy method (raw `curl` call haath se) chhora, clean method (apna built-in web search) apnaya, aur
> **"Common Pitfalls"** aur **"Verification Checklist"** sections add kiye jo usne seekhe zaroori hain.

### 5b: Brain Badlo, Baaki Sab Rakho

```text
Now prove there's no lock-in. Switch it to a different model,
ideally a cheaper one. Then re-run a task that uses the skill
from 5a.
```

**Done jab:** Task doosre model pe sahi complete hoti hai, wahi skill + memory use kar ke jo pehle model
ke neeche bani thi, aur switch **ek command** thi, migration nahi.

> **Ehtiyat: "No lock-in" ka matlab swap aasan hai, har model equal nahi.** Verbose skill sasta model
> pe daalo aur output kharab a sakta hai. **Fix skill ko chhota model chalne ke qabil banane mein hai**,
> mehenge model se chipke rehne mein nahi.

---
[⬅ Phone Aur Hard Task](01-phone-hard-task.md) · [Agla: Automate Aur Voice ➡](03-automate-voice.md)
