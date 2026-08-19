# Problem Solving with General Agents — 90-Minute Crash Course — Summary

*Note: is folder mein ek extra `test.md` file bhi hai (content: "Sarah's example and don't worry") jo
README ke index mein shamil nahi hai — stray/leftover file lagti hai, isay chapter content ki tarah
treat nahi kiya gaya.*

Mode 1 (Chapter 2/3) — sikhata hai **kaise** general agent se problem solve karna hai, 4 tools (Claude
Code, OpenCode, Cowork, OpenWork) ke through 7 Principles se, jo 80% real-world use cover karte hain.

## 00 — Overview

- **4 tools grid:** Anthropic (Claude Code/Cowork) vs Open-source (OpenCode/OpenWork) × Coding vs
  Non-coding. 7 principles sab 4 mein same tarah kaam karte hain.
- **Mode 1 (problem solving, is course) vs Mode 2 (AI Workers banana, alag course).** Safety-first note:
  har action ki approval maango, sab kuch ek sath access mat do.
- **5 Bullets = 60% value:** Action over talk; Code/structure over prose; Verify don't trust; Small
  reversible steps; Files are memory. Baqi 2 (Constraints, Observability) pehle 5 ko operationalize
  karte hain.
- **Lindy Effect:** Purane tools (terminal, files, Git, SQL) AI ke sath aur zyada important ban jate
  hain, kyunki AI insaani zaban mein sochta hai lekin act inhi proven tools se karta hai.
- **7 Principles table** (building-dependency order, importance order nahi), P1 vs P2 ka farq clarify
  kiya gaya (Action vs Structure). Thesis: principles session govern karte hain, tools sirf interfaces.

## 01 — Principle 1: Bash is the Key

- Failure mode: "AI sirf baat karta hai, karta kyun nahi?" Bash = terminal ki language; AI wahi commands
  type karta hai jo aap khud karte. Cowork/OpenWork mein step cards ki tarah.
- Beginner mistake: advice mangna ("kaise organize karoon") vs instruction dena (specific input/output
  naam lena) — mental model: "Agent ke haath hain. Haathon ko brief karo, dimagh ko nahi."
- Examples: legal document search, downloads-folder organize, accounting reconciliation, marketing
  reporting.
- Hands-on: Pack 1 (53-file messy downloads folder), 5-word prompt se AI khud command cascade chalata
  hai.
- Apply: "method nahi, brief likho" — input naam do, output naam do, "how" verbs kaato ("find use karo"
  jaisa method-specify mat karo), sirf "what you want at the end" rakho.

## 02 — Principle 2: Code as Universal Interface

- Failure mode: prose request baar baar galat samjha jata hai. Sarah's 3000-photos example: paragraph
  se AI ne chota program likha (location parhna, rename, hash-based duplicates) — 15 minute.
- 2 hisse: complex kaam ke liye AI code likh kar karta hai; format content jitna matter karta hai.
- Bash (haath) vs Code (dimagh) table. Code ke 5 powers: precise thinking, workflow orchestration,
  organized memory, universal compatibility, instant tool creation.
- Aapke 2 kaam (nahi badalte): define the problem, verify the output.
- Hands-on: Pack 2 (15 receipts, mixed formats) — pehle plan mangwao, phir execute.
- Apply: 2+ apps wala kaam chuno, "script likh do" mat kaho — "apna approach batao" kaho pehle.

## 03 — Principle 3: Verification as a Core Step

- Failure mode: output theek dikhta hai lekin production mein toot jata hai. Key rule: jisne output
  banaya wahi uska sabse ghatiya verifier hai — independent path chahiye.
- Examples: legal citation mismatch, insurance policy limit mismatch, research side-effects mismatch.
- "Wrong Number" problem: AI se "is this correct?" poochna real verification nahi — usi galti ko "haan
  sahi hai" bolega. Fix: code khud parho (likhna nahi), trusted source se compare karo.
- Hands-on: Pack 5 — polished memo mein 5 hidden mistakes, `VERIFICATION.md` (Confirmed/Mismatch/No
  source found) — AI pehli koshish mein 3/5 pakar leta hai.
- Apply: sources **alag** se parho, sirf apna output dobara mat parho.

## 04 — Principle 4: Small, Reversible Decomposition

- Failure mode: ek bara change ne poori dopeher barbaad kar di. Rule of thumb: change wapis lene mein 2
  minute se zyada lage to change bara tha.
- Enforcement prompt: har step ke baad show/verify/commit/wait-for-OK.
- Example table: letter/report/spreadsheet — ek-bara vs step-by-step comparison.
- **Pixar lesson:** Toy Story 2 files 1998 mein galti se delete, backup weeks se fail tha, sirf ek
  employee ki personal copy ne bachaya — progress-saving process mein built-in hona chahiye.
- **Undo trap:** Sarah ka `git reset --hard` budget fix karta hai lekin volunteer list bhi mita deta hai
  (uncommitted thi) — last save ka size = max gawaya jane wala kaam.
- Hands-on: Pack 3 (Run A ek-shot vs Run B 4-step) — Run B cleaner.
- Apply: 4-7 steps list karo, har step check line ke sath, save after each.

## 05 — Principle 5: Persisting State in Files

- Failure mode: agent kal ka decision bhool jata hai. Fix: zaroori info file mein — sabse important:
  rules file (`CLAUDE.md`/`AGENTS.md`, `/init` se draft).
- Length rules: pehla draft <250 words, kuch hafton baad <60 lines, >500 words ho to documentation ban
  gayi hai — table of contents samjho, encyclopedia nahi.
- Shape template diya gaya (Project/Where things live/Critical rules/On-demand references).
- Plan files pattern: `docs/plans/feature-name.md`, multi-session resume.
- Hierarchy: Conversation volatile, project folder files durable, referenced files on-demand.
- Files kaafi na hon to database (Neon, free, 60-second setup) — har naya sawal ek query ban jata hai.
- Hands-on: Pack 6 — Run A (no rules file) Carlos ko credential-verify kiye bina ADVANCE karta hai; Run
  B (CLAUDE.md ke sath) khud rule follow kar ke Carlos ko HOLD karta hai.
- Apply: AI se khud pehla draft likhwao, generic lines hatao, test karo repeat na karna pade.

## 06 — Principle 6: Constraints and Safety

- Failure mode: agent unauthorized files chhuta hai. Limits AI ko slow nahi karte — itna trust dilate
  hain ke zyada azaadi de sako. Asli khatra: tez galat direction mein kaam karna.
- 3 Universal Trust Levers: Scope, Connections, Approvals.
- **Autonomy Ladder (5 levels):** Watching closely → Ambient supervision → Walk away → Act without
  asking → Scheduled/automated. Rule: walk-away trust nahi to schedule bhi mat karo.
- **Prompt-injection trap:** bahar ki files (email/resume/PDF) mein chhupi instructions AI ko trick kar
  sakti hain — full freedom mat do, unexpected plan approve mat karo, ajeeb ho to Stop dabao.
- Key idea: tool settings mein rules permanent hain, prompt mein likhe rules permanent nahi.
- Hook example diya gaya (`rm -rf` block karne wala PreToolUse JSON hook).
- Hands-on: Pack 1 reuse — `.claude/settings.json` mein deny rules (read-only downloads/), automatic
  block.
- Apply: check current access, repeat-hone-wale rules ko settings mein move karo, honest trust-level,
  monthly access clean-up reminder.

## 07 — Principle 7: Observability

- Failure mode: pata hi nahi agent ne kya kiya. Discipline: har novel task par kam az kam ek dafa
  execution view dekho.
- Examples: fleet-routing prompt-injection (47 driver ko galat pings), lawyer per-step review, controller
  ka stale-folder-reference discovery, silent agent (dashboard "running" par 3 din se no data — firewall
  block), cascading failure (LNPS triage: Logs→Network→Process→System).
- **5 symptoms — session off the rails:** purani baaton ka irrelevant reference, lambe vague responses,
  contradiction, baar-baar apology bina progress, unmentioned files/connectors ki baat.
- Response: type karna band karo, `/clear` ya nayi session, sirf zaroori facts paste karo — reset almost
  hamesha rescue se tez hai.
- Hands-on: Pack 1 teesri baar — AI har step narrate kare, ek surprise likh lo.
- Apply: walk-away task chuno, poori run baithe dekho (3-column notes), habit: naye task walk-away
  promote karne se pehle watch-once.

## 08 — Four-Phase Workflow + Five Failure Patterns

- **4 phases:** Explore (P1+P7, read-only) → Plan (P2+P5, sabse important phase) → Implement (P4+P3,
  atomic + verify) → Commit (P7, final verification + rules file update). P6 (Constraints) chaaron
  phases ko wrap karta hai — diagram ke around ka box, andar ka nahi.
- **5 Failure Patterns table:** The Drift (Persistence/P5), The Confident Wrong (Verification/P3), The
  Big Bang (Decomposition/P4), The Scope Creep (Constraints/P6), The Black Box (Observability/P7) —
  diagnostic shorthand ban jate hain team mein.

## 09 — Worked Example + Capstone

- Task family: complex artifact review + verified structured response (PR review / MSA redline) —
  identical workflow shape alag domains mein.
- 4 phases, 4 concrete prompts diye gaye (Explore/Plan/Implement/Commit) — result: har phase apni file
  deta hai, slower pehli baar, faster trust-time hamesha.
- **Capstone:** apna 60+ minute recurring task chuno, 4 phases se guzaro, consciously principle naam lo.
  5 journal questions (baseline time comparison, sabse mushkil principle, rules file addition, tightened
  constraint, dikha failure pattern).
- Compounding: doosri run 40-60% tez, teesri run se rules file growth ruk jata hai — "principles seekhna"
  se "principles use karna" ka threshold.
- 7 friction-to-principle mappings (agent sirf chat kyun kar raha → P1, etc.) — response friction par
  banao, pehle se nahi. Course-complete 5 signs listed.

## 10 — Quick Reference

- 7 principles ek-line mein (5 Doing + 2 Operating).
- Four-Phase Workflow diagram, 5 Failure Patterns table, Autonomy Ladder diagram.
- **Principles-per-tool matrix** (Claude Code/OpenCode/Cowork/OpenWork) — jaise Bash=Terminal/Local Linux
  VM, Persistence=CLAUDE.md/AGENTS.md.
- "Jab kuch ghalat mehsoos ho" quick response: context poisoned → type karna band, reset, file se
  continue.
