# 05 — Part 4: Power, Safely Held (Concepts 12-13)

## Concept 12 — Blast Radius: Files Touch Karne Wale Code Ke Rules

Claude.ai par mistakes free hain. Jis moment code **tumhare** machine par chalta, Concept 2 ki
warning theoretical nahi rehti: **code exactly wo karta jo bola gaya, perfectly, at scale, including
galat cheez.** 2 facts yaad rakho: agent se delete hui files aksar recycle bin **skip** karti hain;
script se edit hui files ka **koi undo history nahi** hota.

4 rules, cheap to follow, **blast radius** (run galat hone par sabse buri cheez) shrink karte hain.

**Rule 1 — Copies par kaam karo jab tak script ne trust na kamaya ho.** Koi bhi change-karne-wala
run se pehle: _"Pehle folder ko expenses-2025-backup mein copy karo, phir sirf original par kaam
karo."_ Ek sentence pehli bad run ko disaster se shrug mein badal deta.

**Rule 2 — Changes hone se pehle dekho.** **Dry run** = har operation ki list jo code karega,
kisi bhi change se pehle dikhayi. Rename/move/delete/overwrite se pehle: _"Kuch change mat karo
abhi, poori list dikhao — har rename, old naam next to new naam, aur meri approval ka wait karo."_
Cowork/OpenWork yeh by-design karte; terminal mein har baar khud maangna.

**Rule 3 — Agent ko sabse chhote folder par point karo.** Sabse chhota folder jisme problem hai —
kabhi home directory (sab personal files ka top folder) nahi, kabhi "Documents" nahi, kabhi
poora disk nahi. `expenses-2025/` ke andar confused script 12 CSVs ko damage kar sakta (jo Rule 1
ne backup kiye); drive ke top par confused script tumhari life damage kar sakta.

**Rule 4 — Output naye files mein likho, kabhi originals ke upar nahi.** _"Results naye file mein
likho, originals untouched chhodo."_ Original data clean rehta, har run naye file delete karke
undo ho sakta.

> 4 rules together: 3 sentences per brief, ~90 seconds per run.
>
> ```text
> Copy the folder to a backup first. Show me your plan of operations
> before changing anything, and wait for approval. Write all output
> to new files. Never modify the originals.
> ```

**Researcher example:** interview recordings "clean up karo duplicates hatao" bola. Dry-run list
mein 40 deletions dikhi — 6 galat grouped (name+length match kiya, content nahi). Rule correct ki
("content se match karo, naam-size se nahi"), dobara dry run, 34 true deletions approve ki. **2-
minute plan read ne 6 interviews bacha li jo recycle bin ke bahar chali jaati.**

## Concept 13 — Map Ka Edge, Aur Uske Paar Kya Hai

Brief mein fit hone wale, files mein rehne wale problems ke liye — AI-written code jo kabhi parhte
nahi, hamesha check karte, yehi aaj kaam ka tareeqa hai. Par is territory ki boundary jaanna
zaroori hai.

**Edge ke paar, one-prompt code se zyada chahiye:**

- **Software jisme doosre log in karte hain** — accounts, payments, many users, 3am uptime —
  **products hain, scripts nahi**, Part 4 ki discipline chahiye
- **Always-on automation, real consequences** — "clients ko automatically har hafte email karo"
  bina dekhe chalta, Concept 6 ke checks wahan nahi pahunch sakte — **Digital FTE** (poori role
  carry karne wala AI worker)
- **High-stakes acts, no undo** — code tax filing submit kare, mass email bheje, trade place kare
  — code _prepare_ kare, insaan _send_ kare
- **Judgment computation ka costume pehne hue** — "kaunse employees promote karein, compute karo" —
  arithmetic easy hai, **criteria** poora problem hain, aur wo tumhare hain. **Code computes, tum
  decide karte ho.**

**Territory ke andar, aaj se tumhara:** har reconciliation/rollup/rename/merge/clean/cross-check/
chart/report jo VPRF signal fire kare — zyadatar professionals ke liye saal mein sau-haaton ghante.

**Book aage kahan jati hai:** 2 bade levers mil gaye — exact documents (Markdown In, HTML Out) aur
computation unse order kiya hua (yeh course). Aage: **How to Think in the AI Era** (kab agent
bulana, kab nahi), phir **Problem Solving with General Agents** (dono ko Part 3 surfaces par le
jata). Tool walkthroughs (Agentic Coding, Cowork & OpenWork) uploading-annoy-karne-wale din ka
wait kar rahe.
