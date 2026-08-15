# 01 — Context Management: Is Course Ka Sab Se Zaroori Idea

Model sirf wahi kaam kar sakta hai jo abhi uske saamne hai — uski **context**. Ye ek bucket nahi, ek
**stack of layers** hai, aur **har layer har turn pe cost karti hai**:

1. **System prompt + tool definitions** — har turn load, fixed
2. **Rules file** — session start pe ek dafa load, fixed
3. **Conversation so far** — badhti rehti hai, `/compact` chhoti karta, `/clear` khatam
4. **Referenced files** — sirf demand pe
5. **Active skill** — sirf use hone pe

**Top 2 layers fixed hain. Baaki sab aapko manage karni hain.** Ye poora game hai — stack ko lean rakho.

> **Industry naam:** **Context engineering** — Karpathy ne Dec 2025 mein naam diya. Ye poori discipline
> hai: jaan-boojh kar decide karna window mein kya jaye.

## Concept 5: Context Rot Real Hai

1 ghante kaam kiya, jawab kamzor hone lagte hain — AI aapki di hui rule ignore karta hai, khatam hua kaam
dobara karta hai, aisi file mention karta hai jo exist hi nahi karti.

**3 problems:**
1. **Chat sochne se tezi se lambi hoti hai** — koi warning nahi milti
2. **AI conversation lambi hone se pehle hi kamzor hone lagta hai** — isay **context rot** kehte hain
3. **Lambi conversations mehngi hoti hain** — har message pe AI **poori** conversation dobara parhta hai

**Context check karo:**
- **Claude Code:** `/context` — full breakdown, konsi cheez trim karne layak hai batata hai
- **OpenCode:** live gauge, interface mein token/percentage dikhta hai

> **Rule:** Window ka aadha use hote hi `/compact` ya `/clear` karo — 100% hone ka wait mat karo.

## Concept 6: `/clear` Aur `/compact`

**`/clear`** (ya OpenCode mein `/new`) — poori chat delete, naya kaam shuru karne pe use karo.
**`/compact`** — AI poori conversation parhta hai, short summary likhta hai, baaki phenk deta hai. Same
task pe kaam jari rakhne ke liye.

```text
/compact keep the file names and the decisions we made
```

> **Mix mat karo:** `/clear` beech mein use karo to poora progress kho jata hai. `/compact` galat time
> pe use karo to purana clutter naye task mein carry ho jata hai.

**2 zaroori rules:**
- **Boundaries pe compact karo, mid-task nahi** — phase khatam hone pe (exploration khatam, plan
  approved)
- **Facts pehle file karo** — summary specifics kho deti hai. Compact se pehle AI se zaroori
  names/lists/decisions ko file mein likhwao

> **Ek line mein:** *summarize the journey, file the facts.*

## Concept 7: Sessions Resume Karo

- **Claude Code:** `claude --resume`
- **OpenCode:** `/sessions` ya `/resume`

**Galti hui? Undo karo:**
- **Claude Code:** `Esc` 2 dafa, ya `/rewind` — file edits undo karta hai, shell commands nahi
- **OpenCode:** `/undo` / `/redo` — git use karta hai, isliye **sab kuch** cover karta hai (file edits +
  terminal commands bhi)

> Undo **session-level convenience** hai, git ka substitute nahi. Jo rakhna hai, commit karo.

## Doom Loop Ki Nishaniyan

- AI sorry keh raha hai lekin fix nahi kar raha
- Wahi code baar baar badal raha hai, behtar nahi ho raha
- Aisi files/names mention kar raha jo exist nahi kartein
- Ek rule bhool gaya jo isi conversation mein di thi

**Jab ye dikhe: message bhejna band karo.** Explain karne ki koshish mat karo — `/compact` ya `/clear`
se reset karo.

## Cost Spikes — Kyun Aur Kaise Fix Karein

| Kya Dekhte Ho | Kyun | Fix |
| --- | --- | --- |
| Usage achanak barh gaya | Rules file badli, cache discount reset hua | Wapas badlo, ya one-time spike accept karo |
| Har message pehle se mehnga | Conversation badh rahi hai | `/compact` |
| Bohat lambi replies | Simple sawal, over-explaining | "code only, no explanation" |
| Monthly bill zyada | Har task pe expensive model | Simple tasks ke liye cheap model (Concept 4) |

> **Zaroori aadat:** Bara tool output (test run, logs) **file mein** bhejo, chat mein nahi — "full output
> `test-results.txt` mein, 3 failures" kaho.

---
[⬅ Foundations](00-foundations.md) · [Agla: Rules File ➡](02-rules-file.md)
