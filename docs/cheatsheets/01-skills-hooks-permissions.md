# 01 — Skills, Hooks & Permissions (Panels 5-7)

Yeh teen panels Claude Code ki **L2/L3 layers** cover karte hain: Skills (knowledge packs), Hooks
(deterministic callbacks), aur Permissions (safety rules).

## Panel 5: ⚙️ Adding Skills (The Superpower)

Skills markdown guides hoti hain jo Claude **khud invoke** karta hai, jab natural language mein
request uske matching lagti hai — koi slash command type karne ki zaroorat nahi, Claude description
parh kar decide karta hai ke yeh skill relevant hai.

**Locations:**

- Project: `.claude/skills/name/SKILL.md`
- Personal: `~/.claude/skills/name/SKILL.md`

Har `SKILL.md` ek frontmatter block se shuru hoti hai:

```yaml
---
name: code-review
description: Review pull requests for style and correctness issues
allowed_tools: [Read, Grep, Bash]
---
```

Uske baad body mein actual instructions hoti hain jo Claude follow karega jab yeh skill trigger ho.

**Zaroori notes:**

- `description` field **critical** hai — yehi field decide karta hai ke auto-activation hogi ya nahi
  (jitna specific description, utna accurate trigger)
- Explicit invoke karna ho to seedha type karo: `/skill-name`

## Panel 6: 🪝 Setting Up Hooks

Hooks **deterministic callbacks** hain — yeh lifecycle ke specific events pe chalte hain, jaise:

- `PreToolUse` — tool chalne se **pehle**
- `PostToolUse` — tool chalne ke **baad**
- `Notification` — jab Claude koi notification deta hai

`settings.json` mein ek hook is tarah configure hota hai — Bash tool ko match karta hai aur ek
script chalata hai, timeout ke sath:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "./check.sh", "timeout": 10 }
        ]
      }
    ]
  }
}
```

**Exit codes ka contract:**

- `0` = allow (chalne do)
- `2` = block (rok do)

Input script ko **stdin** ke zariye milta hai (command ki detail) — ya agar hook HTTP-based hai, to
**POST body** ke zariye.

## Panel 7: 🔒 Permissions & Safety

Permissions `settings.json` mein ek **allow/deny** block ke tor pe likhi jaati hain:

```json
{
  "permissions": {
    "allow": ["Read:*", "Bash:git:*", "Write:*:*.md"],
    "deny": ["Read:env:*", "Bash:sudo:*"]
  }
}
```

**Kaise parhna hai:**

- Pattern shape: `Tool:arg:glob` — wildcard matching
- `allow` list mein jo match ho, wo **auto-approve** ho jata hai (koi prompt nahi)
- `deny` list mein jo match ho, wo **bilkul block** ho jata hai — koi override nahi
- `defaultMode` set karo `plan` / `auto` / `default` mein se — yeh baaki (unmatched) calls ka default
  behavior decide karta hai

---
[⬅ Prev](00-overview-and-memory.md) · [Next ➡](02-architecture-and-workflow.md)
