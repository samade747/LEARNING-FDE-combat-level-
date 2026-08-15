# 05 — Ek Complete Worked Example (8 Steps)

**Koi coding zaroori nahi.** Task: `notes/` folder mein 5 messy meeting notes hain — kuch mein "Action
Items" heading, kuch mein "Todos", kuch mein sub-headings ke andar chhupe hue action items, kuch
`[private]`/`[HR]` tagged. **Goal:** ek clean `weekly-actions.md` banao jo har item list kare, owner se
grouped, private items exclude, koi item miss na ho.

## Step 1: Rules File Setup

`/init` chalao, phir chhota karo:
```markdown
# weekly-rollup
## Layout
- `notes/`: meeting notes
- `weekly-actions.md`: rollup jo banayenge
## Critical rules
- Action items `## Action Items`, `## Todos`, `## Next Steps`, ya `## todo` (lowercase) ke neeche ho
  sakte hain. Sab heading levels dekho, sirf top nahi.
- Owners `@name` format mein. Bina owner wale "Unassigned" section mein jayein.
- `[private]` ya `[HR]` tagged bullet kabhi shamil na ho.
```

## Step 2: Plan Banao (Kaam Se Pehle)

Plan mode on karo (`Shift+Tab` ya `Tab`), phir:
```text
Read every file in notes/. Produce weekly-actions.md grouped by
owner. For each item include the action, the source filename, and
the meeting date. Skip anything tagged [private] or [HR]. Do not
lose any action items.
```

## Step 3: Plan Check Karo Aur Galtiyan Theek Karo

Plan mein 2 galtiyan hoti hain: (1) sirf top-level headings mention karta hai, sub-headings wale items
miss ho jate. (2) bina owner wale items ke liye kuch nahi kaha.

```text
Two changes. (1) Look at all heading levels. (2) Items without an
owner go to an "Unassigned" section; never drop them.
```

## Step 4: AI Ko Kaam Karne Do

Plan mode se nikal ke (`Shift+Tab`), pehle plan `plans/weekly-rollup-plan.md` mein save karwao, phir
approve karo. AI 5 files parhta, `weekly-actions.md` banata, owner se group karta, private items hataता
hai.

## Step 5: Conversation Saaf Karo

```text
/compact keep the heading rules, the owner list, and the
private/HR exclusion rule
```

## Step 6: Automatic Safety Check Add Karo

**Zaroori:** Ye ek step aap khud **paste karte ho, model se likhwate nahi** — 2 wajah: (1) "hook" ambiguous
hai (git hook vs Claude Code hook confuse ho sakta hai), (2) AI apni hi `[private]` rule follow kar ke
safety check ko **defeat** kar dega — vendor-review meeting (jismein sab kuch private hai) ko chup chaap
skip kar dega, koi warning nahi degi.

```json
// .claude/settings.json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{ "type": "command",
        "command": "jq -r '.tool_input.command' | grep -q '^git commit' || exit 0; for f in notes/*.md; do grep -q \"$(basename $f)\" weekly-actions.md || { echo \"Missing: $f\" >&2; exit 2; }; done" }]
    }]
  }
}
```

**Plain English:** Har `git commit` pe, check karo har `notes/` file `weekly-actions.md` mein mention
hui hai. Missing ho to commit block.

**Kya hota hai:** Commit try karte hi, check fire hoti hai: `Missing: notes/2026-12-11-vendor-review.md`
— kyunke uski har item `[private]` thi, isliye file mention hi nahi hui. Model error parhta hai aur ek
placeholder entry add karta hai file ka naam explicitly mention karte hue:
```markdown
## From 2026-12-11-vendor-review.md
- All items confidential — see meeting owner.
```
File naam ab present hai, hook pass, commit ho jata hai. **Aap ne kuch nahi kiya — safety net ne pakra,
model ne khud fix kiya.**

> **Ye Concept 10 ka verification loop hai, live**: Attempt → Check → Fix → Repeat.

## Step 7: Side Task Ek Helper Ko Do

```text
Use a research helper to look up the 2026 international public
holidays list and write the dates to tmp/holidays-2026.md.
```

Subagent web pe jata hai, holiday dates dhoondta hai, chhoti file mein save karta hai. **Poori web page
aapki conversation mein kabhi nahi ati.**

## Step 8: Skill Ki Tarah Save Karo Agli Dafa Ke Liye

```text
Create a skill at ~/.claude/skills/weekly-meeting-rollup/SKILL.md
based on what we just did. Include: heading variants, all-headings
rule, private/HR exclusion, Unassigned section, missing-file check,
and holiday cross-reference.
```

Agli Jumma, sirf "do the weekly rollup" type karo.

## Kya Hua?

8 steps mein **koi code nahi likha, koi API nahi jaani.** Jo kiya wo tha: model ki **attention manage**
karna — kya dekhe, kab plan kare, kab bhoole, kab delegate kare, kab khud pe trust na kare, kab yaad
rakhe. **Yehi poora chapter hai.**

Claude Code aur OpenCode ke darmiyan farq bohat kam thay: alag filename (`CLAUDE.md`/`AGENTS.md`), alag
keystroke (`Shift+Tab`/`Tab`), alag safety-net language (JSON/JavaScript), alag skill folder (same file).

> **Thinking hi tool hai. Configs sirf decoration hain.**

---
[⬅ Connecting to the World](04-connecting-world.md) · [Agla: Where to Run ➡](06-where-to-run.md)
