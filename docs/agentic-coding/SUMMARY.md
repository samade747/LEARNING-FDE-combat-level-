# Claude Code and OpenCode — Summary

Chapter #3, "Claude Code and OpenCode: A Crash Course" — poora course ek idea ke ird gird hai:
**context engineering**, jaan-boojh kar decide karna model kya dekhe.

## Karpathy Se 3 Zaroori Baatein (poore course mein chalti hain)

1. Ye ghost hai, insaan nahi — koi ego, koi motivation.
2. Iski intelligence jagged hai — ek cheez mein superhuman, agli mein kamzor.
3. Utna hi trust karo jitna output check ho sake (**verification loop**).

## 00 — Foundations

- Chatbot jawab deta hai; Claude Code/OpenCode **action lete hain** — biggest shift: sawal poochna
  band karo, instruction do.
- Install: `curl -fsSL https://claude.ai/install.sh | bash` / `opencode.ai/install`. Ehtiyat: kuch
  free OpenCode "stealth models" temporary hain, data training ke liye use ho sakta hai.
- **Plan Mode** — "look but do not touch". Claude Code `Shift+Tab` x2, OpenCode `Tab`. Rule of thumb:
  task 10 min se zyada legi to plan mode use karo.
- **Permissions Discipline** — shuru mein sab dekho, phir safe actions auto-approve karo
  (`.claude/settings.json` allow/deny lists). OpenCode granular per-type rules + 3-repeat auto-stop.
- **Model Ko Task Se Match Karo**: planning/architecture → capable model; routine execution → cheap
  model. "Strong model se plan karo, cheap model se execute karo."

## 01 — Context Management

- Context = **stack of layers**, har layer cost karti hai: system prompt+tools (fixed), rules file
  (fixed), conversation (badhti), referenced files (on-demand), active skill (on-demand). Top 2 fixed,
  baaki manage karni hain.
- **Context engineering** — Karpathy ne Dec 2025 naam diya.
- **Context Rot** real hai — rules ignore, khatam kaam dobara, non-existent files mention. Rule:
  window ka aadha use hote hi `/compact` ya `/clear` karo.
- `/clear` (poori chat delete) vs `/compact` (summary rakhta hai) — mix mat karo; boundaries pe
  compact karo mid-task nahi; facts pehle file karo ("summarize the journey, file the facts").
- Sessions resume: `claude --resume` / `/sessions`. Undo: `Esc` x2 / `/rewind` (files only) vs
  OpenCode `/undo`/`/redo` (git-based, sab cover karta hai).
- **Doom loop signs**: sorry bolna par fix na karna, wahi code repeat, non-existent files, bhoola hua
  rule — message bhejna band karo, `/compact`/`/clear` se reset.
- Cost spikes table: usage spike (rules file badli/cache reset), expensive messages (conversation
  badh rahi — `/compact`), lambi replies (over-explaining), monthly bill zyada (expensive model har
  task pe). Bara tool output file mein bhejo, chat mein nahi.

## 02 — Rules File: CLAUDE.md / AGENTS.md

- File jo **har conversation ke shuru** mein parhta hai. Claude Code: `CLAUDE.md`; OpenCode:
  `AGENTS.md` (fallback CLAUDE.md).
- `/init` se auto-generate hoti hai (bohat lambi) — kaam: jo zaroorat nahi delete karo. **Har line ka
  test**: "agar hata doon kya AI galti karega?"
- Boris Cherny (Claude Code creator) ka file ~2,500 tokens hai saal bhar baad bhi.
- **Prune bhi karo** — contradictory rules jama hoti hain. July 2026 Claude Code team ne apna 80%+
  system prompt hataya bina performance loss. Forbid-rules ko standard-describe rules se replace
  karo (example table diya).
- Model capability ke hisaab se constrain karo — frontier model thin rules, cheap/local model zyada
  explicit. `/doctor` (Claude Code) review karta hai.

## 03 — Personalizing: Skills, Hooks, Subagents

- 3 alag problems: **Command/Skill** (saved reusable prompt), **Hook/Plugin** (hamesha khud chalti
  rule), **Subagent** (isolated-window helper).
- Skills: `.claude/skills/name/SKILL.md` → `/name` command. Description sabse zaroori line. Chhoti
  skills banao. `@` auto-import syntax skill ke andar mat use karo. Skill deterministic nahi banata —
  sirf range narrow karta hai; guaranteed result ke liye script/hook use karo.
- Hooks (Claude Code `.claude/settings.json`, JSON) / Plugins (OpenCode `.opencode/plugins/*.js`) —
  exit code 2 = block. Achi aadat: commit-time checks, per-edit nahi.
- **Verification Loop** — poori book ka sabse zaroori pattern: Attempt → Check → Fix → Repeat, beech
  mein koi insaan nahi. Boris Cherny: AI ko verify karne ka tareeqa do, result 2-3x behtar hoga.
  Robert C. Martin (July 2026): ab agents ka code parhta hi nahi, sirf extreme constraints
  (tests/coverage/mutation testing) rakhta hai — order zaroori: pehle checks, phir parhna chhora.
- Subagents: isolated context window, sirf summary wapis. Built-ins: Explore/Plan/general-purpose
  (Claude Code), Explore/General/Scout (OpenCode). Custom: `.claude/agents/name.md`.
- Skill vs Subagent table + Placement Question table (8 rows: rules file/skill/tool
  description/prompt/file-on-disk/executable-reference/subagent/delete) — "hamesha" surfaces sabse
  zyada editing maangte hain.

## 04 — Connecting to the World: MCP

- MCP AI ko services se connect karta hai (Slack, Docs, Notion, GitHub, DBs) — APIs ke upar standard
  wrapper. Asal sawal: "standing connection ke qabil hai ya agent seedha call kar sakta hai?"
- Setup: `claude mcp add --transport http` / OpenCode `opencode.json` mcp block. `/mcp` status.
- System of record connect karna zaroori use case — live authoritative data, stale paste nahi.
- Ehtiyat: sab connect mat karo — Claude Code defers (lazy load), OpenCode upfront load (zyada
  selective raho). 1-2 connections se shuru karo.
- **Prompt injection**: model jo parhta hai woh usay steer kar sakta hai. 3 habits: fetched content
  sirf inform kare, apni files hi instruct karein; untrusted content subagent se parhwao; behavior
  ajeeb ho to shak karo. Honest limit: exposure kam karta hai, immune nahi banata — deeper fences
  Harness Engineering course mein.

## 05 — Complete Worked Example (8 Steps)

Task: messy meeting notes → clean `weekly-actions.md`, owner-grouped, private excluded.
1. Rules file setup (`/init` + chhota karo).
2. Plan mode mein detailed instruction.
3. Plan review, galtiyan fix (sub-headings, unassigned section).
4. Execute — plan file mein save, phir approve.
5. `/compact` conversation saaf karo.
6. **Hook add karo khud paste kar ke** (model se nahi likhwate — warna apni hi rule follow kar ke
   safety check defeat kar sakta hai) — missing-file check `git commit` pe.
7. Side task subagent ko do (holiday lookup) — poori web page conversation mein nahi aati.
8. Skill ki tarah save karo agli baar ke liye (`~/.claude/skills/...`).
- Nateeja: koi code nahi likha — model ki attention manage ki. Claude Code/OpenCode farq minimal tha.

## 06 — Where to Run, Aur Kya Rakhein

- Interfaces: terminal, IDE plugin, desktop, web, mobile, cloud (Claude Code); terminal TUI, desktop
  beta, VS Code, web SDK, GitHub/Slack bot (OpenCode). Recommendation: terminal/IDE se shuru karo.
- **Personal context library**: shared style/commit conventions `~/.claude/CLAUDE.md` mein
  `@~/.claude/style/*.md` se, ya OpenCode `opencode.json` instructions array. Ek saath sab mat banao.
- **Memory beyond basics**: `notes/` folder, Memory MCP server, cross-conversation search. 2 craft
  rules: absolute dates hamesha, decisions over narration. Claude Code auto memory ab manual memory
  ki jagah leta hai.

## 07 — Composing Claude Code Aur OpenCode

- **Git worktrees** — parallel sessions bina conflict ke: `git worktree add -b branch ../copy`. File-
  edit rule: same file 2 sessions = bura; alag directories = acha. Claude Code creator ~5 terminal +
  5-10 browser sessions chalata hai, 10-20% abandon karta hai.
- **Pattern 1 — Plan/Execute Split**: Claude Code plan banaye → save → OpenCode cheap model se
  implement kare. Plan file = contract.
- **Pattern 2 — Cross-Model Review**: jisne code likha wahi review ke liye bura hai; alag family ka
  model review kare (Claude ↔ GPT).
- Kab single tool kaafi hai: chhote tasks. 2 tools kab: bari task, cost bachana, independent review.
