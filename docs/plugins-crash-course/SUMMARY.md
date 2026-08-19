# Plugins for AI Agents: One Bundle, Your Whole Team — Summary

Yeh chapter sikhata hai ke **plugin** kya hota hai — skills, subagents, MCP servers, instructions, aur
hooks ka ek bundle jo ek generic coding agent (Claude Code / OpenCode) ko **team ka apna** bana deta hai,
sirf ek install se. 13 concepts, 5 parts.

## 00 — The Shape (Concepts 1-3)

- **Concept 1 — Aap extend karte ho, own nahi:** Plugin koi program nahi jo aap chalate ho — pieces ka set
  hai jo **host** (Claude Code/OpenCode) load kar ke chalata hai. Host agent loop, model, machine own
  karta hai; plugin sirf capabilities/rules contribute karta hai.
- **Concept 2 — 2 Hosts, ek idea:** Claude Code = declarative bundle (folder + chota manifest). OpenCode =
  code module (JS/TS file jo events mein hook karti hai). Zyada tar pieces port hote hain (skill sirf
  `SKILL.md`, instructions markdown, MCP server sirf URL) — **hooks exception hain**, koi shared format
  nahi (Claude Code = JSON+shell, OpenCode = JS module jo throw karta hai). Claude Code plugin Claude
  Cowork/claude.ai mein bhi load hota hai; OpenCode plugin OpenWork mein.
- **Concept 3 — Bundle share karne ke liye, configure rakhne ke liye nahi:** `.claude/`/`.opencode/`
  folder personal customization ke liye (ek repo tak). **Plugin tab chahiye jab customization travel
  kare** (teammates, projects, community). Test: *kya karta hai* nahi — **kaun aur isay chahiye**. Plugin
  skills/commands plugin-naam se namespaced hote hain (`repo-tools:hello`) taake naam-clash na ho.

## 01 — Capability Levers (Concepts 4-6)

3 levers jo capability barhate hain (sab **advisory** — model decide karta hai kab use kare):
- **Concept 4 — Skills:** Folder jisme `SKILL.md` (description + instructions). **Model-invoked** — Claude
  description parhta hai, task match hone par khud pull karta hai. Description sabse important line hai
  ("kab use karna hai" likho, sirf "kya hai" nahi). Portable rakhne ke liye sirf `name`/`description`
  frontmatter par rely karo, tool-specific cheezein avoid karo.
- **Concept 5 — Subagents:** Helper jisay main agent kaam de sakta hai apni khud ki clean context window
  ke sath. Use karo jab task self-contained/verifiable ho (e.g. "yeh diff review karo"). Delegation ki
  cost hai — har cheez subagent mat banao.
- **Concept 6 — MCP Servers:** Bahar ki reach (internal API/DB/service) jo plugin ek MCP server point kar
  ke deta hai. Server **remote** hona chahiye jaan-boojh kar (logic/data/secrets aapke infra par); plugin
  sirf pointer ship karta hai. Local server almost kabhi sahi choice nahi.

## 02 — The Deterministic Lever: Hooks (Concepts 7-8)

- **Concept 7 — Hooks:** Command jo host agent lifecycle ke fixed point par khud-b-khud chalta hai — model
  suggestion nahi. 3 cadences: session mein ek dafa (`SessionStart`/`SessionEnd`), turn mein ek dafa
  (`UserPromptSubmit`/`Stop`), har tool call par (`PreToolUse` block kar sakta hai, `PostToolUse`). Exit
  codes: **0** = allow/done, **2 on PreToolUse** = tool call block (stderr model ko reason ki tarah
  milta hai), koi aur non-zero = non-blocking error/log. **Exit-2 rule hi guardrails ka poora khel hai**;
  exit 1 block **nahi** karta (sabse common galti).
- **Concept 8 — Must-always ek hook hai, instruction nahi:** Skill/`CLAUDE.md` mein likha kuch bhi
  advisory hai (model bhool sakta hai). Har-baar honi chahiye wali cheez ke liye hook chahiye. 2 patterns:
  format-on-write (`PostToolUse`, prettier), block-what-must-never-happen (`PreToolUse` exit 2, .env/
  secrets files, `rm -rf`/`git push --force` block). **Gotcha:** stdin ek stream hai — `jq` do dafa
  directly call karne se pehla call sab consume kar leta hai; `input=$(cat)` se ek dafa capture karo. 4
  misbehave rules: fast rakho, fail safe (formatter → exit 0, guard → block-if-unsure), har baar reason
  batao, host ki tarah debug karo (fake event pipe).

## 03 — Ship It (Concepts 9-11)

- **Concept 9 — Manifest aur structure:** Claude Code plugin = folder + `.claude-plugin/plugin.json`
  (name/description/version/author). Baaki sab **plugin root** par (skills/, agents/, hooks/, .mcp.json)
  — `.claude-plugin/` ke andar sirf manifest, isse bahar rakhna common galti hai. `claude plugin validate`
  share karne se pehle chalao.
- **Concept 10 — Marketplaces:** Marketplace sirf ek git repo hai jisme catalog file (`marketplace.json`)
  plugins list karti hai — koi package registry nahi. Teammate `/plugin marketplace add` +
  `/plugin install`. Develop karte waqt `claude --plugin-dir` se disk se load karo. Pinning: `ref` =
  branch/tag, `sha` = exact commit (dono set hon to sha jeetta hai). **Charge kar sakte ho, files ke liye
  nahi** — skill plaintext hai, DRM nahi. Sahi monetization model: **hosted access** (server tak entry
  becho, files tak nahi); installed plugin ek thin free client, `.mcp.json` hosted MCP server point karta
  hai, key subscription gate hai.
- **Concept 11 — Trust:** Plugin install karna kisi aur ka code chalana hai. Author: least privilege,
  narrowly matched hooks, README.md mein trust contract (kya install hota hai, kaunse hooks kab chalte
  hain, kya inspect/execute karte hain, network access). Installer: `claude plugin details <plugin>`
  se dependency ki tarah review karo, kuch enable kiye bina.

## 04 — OpenCode + Worked Example + Capstone (Concepts 12-13)

- **Concept 12 — OpenCode plugins (hooks as code):** Plugin = JS/TS module jo function export karta hai,
  host context object ke sath call karta hai, hooks return hote hain. Mapping: `tool.execute.before` =
  `PreToolUse`, `tool.execute.after` = `PostToolUse`, error throw karna = exit 2. **Key difference:**
  OpenCode plugin sirf hooks/tools ke liye hai, skills ke liye nahi — OpenCode khud `.opencode/skills/`,
  `.claude/skills/`, `.agents/skills/` se skills discover karta hai.
- **Part 6 — Worked example (`agent-factory` plugin banana):** Rhythm = plan → review → execute → verify.
  Steps: empty scaffold → guard hook pehle (must-always lever, prove karo blocks karta hai) → real-job
  skill (toy nahi) → reviewer subagent (edit nahi, sirf report) → MCP server wire karo → installable
  banao, doosre project mein install kar ke prove karo travel karta hai. **Done jab:** doosra project bhi
  same hook se protected ho.
- **Concept 13 — Ceiling aur bridges bahar:** Loop aapka nahi hai (hooks host ke loop ke around fire hote
  hain -> Build AI Agents course). Identity aapki nahi hai (plugin host-user ki tarah act karta hai -> AI
  Identity course). Reach borrowed hai (MCP server wire karta hai, khud nahi banata -> connector-native
  app). Lekin bundle coding agent se aage bhi pahunchta hai — Claude Cowork, claude.ai, OpenWork; skill
  sabse door tak (OpenClaw). Same-skeleton doosre plugin types: house-style, safety, service, workflow.
  **Capstone:** apna plugin ship karo — kam az kam ek must-always hook + ek capability lever, marketplace
  par publish, kisi se install karwao, confirm karo hook unke project mein bina extra setup fire hota hai.
