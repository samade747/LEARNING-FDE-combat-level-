# CCAR-F Exercise 2 — Configure Claude Code for a Team Development Workflow

*Official exam guide, Section 8, Exercise 2 (see [`../../03-how-to-prepare-and-sample-questions.md`](../../03-how-to-prepare-and-sample-questions.md)). Also Track B syllabus's **Week 7 lab**, aligned to Preparation Exercise 2. Domains reinforced: 3 (Claude Code Configuration & Workflows), 2 (Tool Design & MCP Integration).*

Ek fixture multi-developer project — real code nahi, sirf itna structure jitna exercise ke 5 steps ko *demonstrate + structurally verify* karne ke liye chahiye: project-level `CLAUDE.md`, path-scoped `.claude/rules/`, fork-isolated `.claude/skills/`, aur env-var-expanded `.mcp.json`. Step 5 (plan mode vs direct execution) is repo se verify nahi ho sakta — woh ek live Claude Code session ka observation hai, neeche "Kaise Chalayein" mein manually karne ka tareeqa hai.

## Files

- `CLAUDE.md` — project-level coding + testing standards (Exercise step 1). Version-controlled, poori team ke liye — `~/.claude/CLAUDE.md` (personal) se alag.
- `.claude/rules/api-conventions.md` — `paths: ["src/api/**/*"]` par scoped, sirf API handlers edit karte waqt load hoti hai (Exercise step 2).
- `.claude/rules/testing-conventions.md` — `paths: ["**/*.test.*"]` par scoped, sirf test files edit karte waqt load hoti hai (Exercise step 2).
- `.claude/skills/team-review/SKILL.md` — team ka shared review skill, `context: fork` (isolated exploration, caller context pollute nahi hoti) + `allowed-tools: ["Read", "Grep", "Glob"]` (read-only, edit nahi kar sakti) (Exercise step 3).
- `.mcp.json` — ek sample MCP server (`internal-ticketing`), credentials `${TICKETING_API_KEY}` env-var expansion se, hardcoded nahi (Exercise step 4).
- `src/api/handler.ts` + `.test.ts` — `api-conventions.md` aur `testing-conventions.md` dono ke glob ko match karne wali sample files.
- `src/web/App.tsx` — jaan-boojh kar `src/api/` se bahar, taake prove ho `api-conventions.md` isay load **nahi** karti.
- `validate_setup.py` — Exercise step 2 ki apni instruction ("test karo ke rules sirf matching files par load hote hain") ko structurally verify karta hai: har rule ka frontmatter `paths` glob parse kar ke confirm karta hai wo sahi files match karta hai, ghalat nahi.

## Kaise Chalayein

**Structural verification (no Claude Code session needed):**
```bash
python validate_setup.py
```
Confirm karta hai: `CLAUDE.md` maujood hai, dono rules apne intended files hi match karti hain (aur doosri files ko nahi), `team-review` skill fork-isolated + read-only hai, `.mcp.json` env-var expansion use karta hai.

**Live check (Step 2 aur 3 ka asal "verify" hissa, Claude Code session mein):**
```bash
cd docs/certifications/ccar-f/projects/02-claude-code-team-workflow
claude
```
1. `src/api/handler.ts` open/edit karo → confirm karo `api-conventions.md` load hoti hai (context mein dikhegi).
2. `src/web/App.tsx` open/edit karo → confirm karo `api-conventions.md` load **nahi** hoti (path glob match nahi karta).
3. `/team-review` chalao → confirm karo skill sirf Read/Grep/Glob use karti hai, koi edit nahi karti, aur uska exploration output main conversation context ko pollute nahi karta.

**Step 5 — Plan mode vs direct execution (manual observation, is fixture se bahar):**
Teen tasks try karo alag complexity ke sath — ek single-file bug fix, ek multi-file library migration, ek naya feature jiske multiple valid implementations hon — har ek pehle plan mode mein, phir direct execution mein. Note karo plan mode kab value deta hai (multi-file/ambiguous cases) aur kab overhead hai (single-file bug fix).

## Done Jab (Official Exercise's 5 Steps, Self-Check)

- [x] Project-level `CLAUDE.md` banaya, universal coding + testing conventions ke sath — `validate_setup.py` confirm karta hai maujood hai
- [x] Path-scoped rules banayi (`src/api/**/*`, `**/*.test.*`) — `validate_setup.py` confirm karta hai har rule sirf apni intended files match karti hai, doosri nahi
- [x] Fork-isolated, read-only skill banayi (`context: fork`, `allowed-tools` restricted) — `validate_setup.py` frontmatter check karta hai
- [x] `.mcp.json` env-var expansion (`${VAR}`) se configure hua, hardcoded credential nahi
- [ ] Plan mode vs direct execution — manually 3 tasks par observe karna hai (yeh checkbox is repo se auto-verify nahi hota, khud live session mein karo)

## Exam Connection

Exercise ka core lesson: team-wide consistency **config se** aati hai (version-controlled `CLAUDE.md` + path-scoped rules), har developer ki apni memory/discipline se nahi. `validate_setup.py::check_rule` yehi property test karta hai — glob pattern sahi files ko hi match kare, na kam na zyada.

---
[⬅ CCAR-F Projects Index](../README.md)
