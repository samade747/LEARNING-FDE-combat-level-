# 03 — Part 3: Khud Skill Banana (AI Isay Tumhare Liye Banata Hai) (Concepts 10-14)

Yeh part programming jaisa lagta hai, hai nahi. Plain English mein describe karo, AI SKILL.md
likhta, phir tum test+fix karte ho. Accountant ki client-summary skill running example hai.

## Concept 10 — Fastest Path: AI Ko Likhne Do

Anthropic **skill-creator** deta hai — bas pucho:

```text
Use the skill-creator skill to help me build a skill.

The skill prepares a monthly client financial summary for my
accounting firm. Whenever I ask for a "client summary" or
"monthly close," it should:
- Format all amounts in our reporting currency with thousands separators.
- Group line items by expense head.
- Flag any payment above the tax-withholding reporting threshold.
- Output using my standard four-section report layout.

Ask me anything you need, then build it.
```

AI kuch clarifying questions pucheta (threshold figure, template kaisa dikhta), phir complete,
correctly-formatted skill generate karta — prompting primer ka brainstorm-and-iterate loop, ek
tool par pointed.

> **Yeh tumhara pehla "code you never write" hai.** Outcome describe kiya, AI ne file + jo bhi code
> chahiye tha banaya — bina tumne ek line likhe ya parhe. Tum client ho, contractor nahi.

## Concept 11 — SKILL.md Ki Anatomy

```markdown
---
name: client-monthly-summary
description: Prepares a monthly client financial summary for an
  accounting firm. Use when the user asks for a "client summary",
  "monthly close", or "month-end report". Formats amounts in the
  firm's reporting currency, groups by expense head, and flags
  tax-withholding items.
---

# Client Monthly Summary

## Settings (edit these to make it yours)
- Reporting currency: your currency
- Withholding threshold: the amount above which to flag a payment

## Instructions
1. Format every amount in the reporting currency, thousands separators.
2. Group all line items by expense head, largest total first.
3. Flag any single payment above the threshold with "⚑ WITHHOLDING".
4. Produce exactly four sections: Overview, Income, Expenses by Head,
   Flags & Notes.

## Example
User: "Prepare the March summary for DEMO Trading."
Result: A four-section report, currency-formatted, withholding flagged.
```

2 parts: **frontmatter** (top block, 3-dash lines ke beech, naam+description — **sirf yehi
hamesha loaded rehta**, progressive disclosure level 1). Baqi sab **instructions** hain, description
match hone par load hoti — level 2.

Complex skills 3 optional folders add kar sakti: `references/` (detailed docs, level 3),
`assets/` (template fill-karne-wali), `scripts/` (exact steps ke programs).

**Upload rules:** file exactly `SKILL.md` naam ki ho; folder `kebab-case` mein (`client-monthly-
summary` ✅, "Client Monthly Summary" ❌, `client_monthly_summary` ❌); naam/description mein XML-
tags nahi; naam mein "claude"/"anthropic" nahi (reserved).

## Concept 12 — Description Field Hi Poora Khel Hai

Description decide karti skill kabhi fire hogi. **AI instructions nahi parhta relevance judge
karne ke liye** — sirf description. Formula: kya karta hai, kab use karna, exact phrases jo tum
bologe.

| Bad | Kyun fail hui | Better |
|---|---|---|
| "Helps with reports." | Bohot vague, sab ya kuch nahi fire karti | "Prepares a monthly client financial summary. Use when the user asks for 'client summary', 'monthly close', or 'month-end report'." |
| "Handles patient documentation." | Trigger words nahi | "Converts consultation notes into SOAP-format clinical notes. Use when the user asks for a 'SOAP note'..." |
| "Brand stuff for marketing." | Kya/kab pata nahi | "Writes social captions in our brand voice... Use when drafting Instagram/LinkedIn/X captions." |

**Debugging trick:** install hone ke baad pucho _"When would you use my client-summary skill?"_ —
answer narrow/wide ho to wahi fix karna.

**Negative trigger** = kab use NA karein ki line, jab skill zyada eager fire ho: _"Do NOT use for
one-off calculations or quick questions. Use only for full month-end reports."_

## Concept 13 — Test, Phir Iterate

1. **Plain English mein describe karo.** AI pehla version likhe.
2. **Draft parho test karne se pehle.** Har instruction line ko pucho: 2 colleagues isay parh kar
   same karenge? "Big payments flag karo" fail hoti; "withholding threshold se upar WITHHOLDING
   note" pass hoti.
3. **Kya fire karta test karo.** Jo phrases chalni chahiye try karo, confirm loads. Unrelated
   requests try karo, confirm takeover nahi karti.
4. **Output test karo.** Real/realistic input par chalao.
5. **Awkward cases bhi test karo.** No income wala mahina, threshold par exact payment, messy
   ledger.
6. **Failures skill-creator ko wapas do:** _"Yeh skill reversed entries ko double-count kar rahi.
   Reversals net-out karne ke liye update karo."_

**Timing list — kab galat hua pehchano:**

- **Pehli reply se galat** → file mein hi problem. Kabhi start nahi hoti → description vague/
  missing words. Galat cheezon par start hoti → description bohot broad, narrow karo/negative
  trigger add karo. Start hoti par output off → instruction loose hai.
- **Pehle theek, chat bare hone par worse** → chat lambi ho gayi, AI track khogaya. Skill fine hai
  — file edit mat karo, fresh chat start karo.
- **Same mistake har run, tight wording ke baad bhi** → step galat jagah hai. Exact step (sum,
  threshold check) chhoti program mein daalo — code exact hota, sentence har baar alag padha jata.
- **Pehle chalti thi, ab nahi** → skill change nahi hui, kuch uske around change hua (threshold,
  template, connector-wali file, team ka tareeqa). Skill dobara parho aaj ke hisab se.

## Concept 14 — Save Karna Aur Share Karna

skill-creator finish hote hi panel mein skill dikhti "Save skill" button ke sath. Click karo,
skill personal skills mein chali jati, switched on, account-private.

Team/Enterprise plans par colleagues ke sath share kar sakte, ya organization directory mein
publish. **Shared skills view-only hain, original change karne par khud update ho jati** — poori
firm ke documents standardize karta. Sharing default off hai, owner enable karta.
