# 00 — Foundations

## 3 Baatein Tools Touch Karne Se Pehle

Andrej Karpathy se:

1. **Ye ghost hai, insaan nahi** — koi ego, koi motivation, kal ki koi memory nahi. Aap isay manage
   karte ho, ye khud ko nahi
2. **Iski intelligence jagged hai** — same model ek task mein superhuman ho sakta hai, agle mein kamzor
   — kabhi assume mat karo asaan cheez bhi theek karega
3. **Utna hi trust karo jitna output check ho sake** — jitna task **checkable** hai, utna zyada hand
   over kar sakte ho. Jahan check nahi ho sakta, judgment aapki rehti hai

## Concept 1: Ye Tools Asal Mein Kya Hain

Chatbot jawab deta hai. Claude Code/OpenCode **action lete hain** — files parhte, edit karte, commands
chalate, task khatam hone tak chalte hain.

**Biggest mindset shift:** *sawal poochna band karo, instruction do.*

| Sawal Poochna (kamzor) | Instruction Dena (strong) |
| --- | --- |
| "Notes kaise organize karoon?" | "Har file `notes/` mein parho. Ek summary file `weekly-summary.md` banao jo har action item list kare, person ke hisaab se grouped." |

```bash
curl -fsSL https://claude.ai/install.sh | bash      # Claude Code
curl -fsSL https://opencode.ai/install | bash        # OpenCode
```

**Konsa model chal raha hai check karo:** Claude Code mein `/status` ya `/model`. OpenCode mein
`/models`.

> **Ehtiyat:** Kuch "free" OpenCode models **stealth models** hain (anonymous, maker undisclosed) —
> temporary hain, aur free testing ke dauran aapka data training ke liye use ho sakta hai. Confidential
> kaam ke liye kabhi mat use karo.

## Concept 2: Plan Mode (Sab Se Kam Use Hone Wala Feature)

Normally, instruction dete hi kaam shuru ho jata hai. **Plan mode** "look but do not touch" state hai —
AI files parh sakta hai, soch sakta hai, lekin kuch badal nahi sakta. Pehle plan likhta hai.

- **Claude Code:** `Shift+Tab` dabao (2 dafa plan mode ke liye)
- **OpenCode:** `Tab` se Build ↔ Plan switch karo

**Kyun zaroori hai:**
1. **Galtiyan pehle pakarte ho** — 10 files edit hone se pehle, ek quick correction lambi cleanup se
   behtar hai
2. **AI plan bana kar behtar kaam karta hai** — plan likhna sochne pe majboor karta hai

**Rule of thumb:** Agar task 10 minute se zyada legi, pehle plan mode use karo.

## Concept 3: Permissions Discipline

Har action se pehle permission mangi jati hai. **Shuru mein sab kuch dekhna hai** — baad mein safe
actions ko auto-approve karo.

```json
// .claude/settings.json
{
  "permissions": {
    "allow": ["Read", "Edit", "Write", "Bash(npm test)", "Bash(git status)"],
    "deny": ["Bash(rm -rf *)", "Bash(npm publish *)", "Bash(git push *)"]
  }
}
```

**OpenCode** zyada control deta hai — har type ki action ke liye alag rule (`read`, `edit`, `bash`), aur
built-in safety: agar AI same action 3 dafa bina progress ke try kare, khud ruk jata hai.

## Concept 4: Model Ko Task Se Match Karo

| Kaam | Chuno |
| --- | --- |
| Planning, architecture, confusing debugging | Sab se capable model |
| Approved plan follow karna: routine edits, tests | Sasta/free model |
| Quick question, one-line fix | Jo pehle se loaded hai |

**Zaroori pairing:** *"strong model se plan karo, cheap model se execute karo"* — sab se zyada cost
savings yahin se ati hai, quality kam kiye bagair.

**2 ehtiyatein:** Sasti models ko clearer instructions chahiye (weaker model, zyada spell-out). Aur
zyada optimize mat karo — har chand minute mein model switch karna pennies bachata hai, attention kharch
karta hai.

---
[⬅ Index](README.md) · [Agla: Context Management ➡](01-context-management.md)
