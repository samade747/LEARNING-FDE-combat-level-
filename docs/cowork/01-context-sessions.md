# 01 — Context, Sessions, Aur Projects

## Concept 4: Plan Hi Leverage Hai

Is poore tool ki asal discipline ye nahi ke aap achhe prompts likho — ye hai ke **aap kaam ko intent
aur execution ke darmiyan intercept karo.** Har zaroori action (file parhna, likhna, connector call
karna) ek pal se guzarta hai jahan aap dekh sakte ho **kya hone wala hai** aur redirect/deny/proceed kar
sakte ho. **Ye moments poore workflow mein sab se sasti course-correction jagah hain.**

**Cowork:** opening plan message + har inline approval card. **OpenWork:** numbered plan right panel
mein + todos timeline, permission cards gated actions pe.

**Har intercept point pe check karo:**
- **Scope** — sirf jo files describe hui wahi touch ho rahi hain?
- **Order** — sequence sahi hai, ya destructive step verification se pehle a gaya?
- **Tools** — koi unexpected connector/plugin?
- **Assumptions** — file formats, naming conventions ke baare mein kya assume ho raha hai?

Galat plan? Dobara shuru mat karo — ek-sentence redirect: *"Step 3 skip karo, step 4 mein existing
template ke column headers use karo."*

## Concept 5: Context Ab Bhi Paisa Kharch Karta Hai

Har message mein system prompt + global instructions + folder instructions + conversation so far + read
ki hui files + active skill — sab tokens cost karte hain. **Cowork:** bill Anthropic plan pe. **OpenWork:**
bill jo bhi provider configure kiya (Anthropic API, OpenRouter, self-hosted).

**2 practical implications:**
- **Poore folders unprompted context mein mat dumpo** — pehle list karwao, phir sirf zaroori files
  parhwao:
  ```text
  First, list this folder and tell me which files matter for
  [my question]. Read only those, then summarize.
  ```
- **Lambi sessions saaf khatam karo** — kal ki conversation aaj ke task mein carry mat karo

**Real example:** Litigation associate ki 340-document matter folder. *"Sab kuch parho"* poori context
load karta — millions tokens, weak recall. **Sahi tareeqa (2 prompts):** pehle list + triage karwao
(3-5 foundational files per group), phir **sirf unhi** ko parh kar synthesize karo. **Result: 12 files
actually read, ~5% cost ka.**

**Strategic cost:** Strong model **thinking** ke liye (multi-source synthesis, contract redline), economy
model **plumbing** ke liye (file listing, format conversion).

## Concept 6: Recurring Kaam Ke Liye Persistent Workspaces

**Ek idea:** Recurring kaam ek **folder + context file** mein rehna chahiye, har dafa fresh chat mein
nahi. Agar har Mangalwar wahi context re-explain kar rahe ho, ye signal hai.

**Pattern (dono tools mein same):**
1. **Folder banao** — ek matter/client/cycle ke liye
2. **Root mein markdown context file daalo** — `CLAUDE.md` (Cowork) ya `AGENTS.md` (OpenWork). Isme
   permanent context: role, conventions, terminology, file layout, tone
3. **Folder kholo, prompts chalao** — context file automatically load hoti hai

Cowork iske upar 2 extras deta hai: **Projects** (named bundle, cross-session memory) aur **scheduled
tasks**. OpenWork sirf folder + `AGENTS.md` hai — aap khud dobara fire karte ho.

**2 failure modes:**
- **Sab kuch ek folder mein daalna** — context bleed hoti hai. Alag workstreams, alag folders
- **Recurring kaam ke liye standalone sessions** — missing context file ka symptom hai

---
[⬅ Foundations](00-foundations.md) · [Agla: Rules Aur Instructions ➡](02-rules-instructions.md)
