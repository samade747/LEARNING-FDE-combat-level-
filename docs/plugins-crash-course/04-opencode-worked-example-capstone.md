# 04 — Part 5-7: OpenCode Plugins + Worked Example + Capstone

## Concept 12 — OpenCode Plugins: Hooks as Code

OpenCode wahi ideas alag form mein: plugin ek **JS/TS module** hai jo function export karta hai. Host
aapka function context object ke sath call karta hai, aap **hooks** return karte ho.

```ts
export const BlockSecrets: Plugin = async ({ project, client, $, directory }) => {
  return {
    "tool.execute.before": async (input, output) => {
      if (input.tool === "read" && output.args.filePath?.includes(".env")) {
        throw new Error("Blocked: .env files are off-limits.");
      }
    },
  };
};
```

Mental model seedha maps karta hai: `tool.execute.before` = `PreToolUse`, `tool.execute.after` =
`PostToolUse`, aur **error throw karna exit 2 jaisa hai.**

> **Key difference:** OpenCode mein plugin sirf hooks/tools ke liye hai — **skills ke liye nahi.**
> OpenCode `.opencode/skills/`, `.claude/skills/`, `.agents/skills/` se khud skills discover karta hai —
> koi plugin, koi shim nahi chahiye.

## Part 6 — Poora Worked Example: `agent-factory` Plugin Banana

Rhythm wahi hai: **plan → review → execute → verify.**

1. **Empty plugin scaffold karo** (Plugin Structure skill se, ya OpenCode docs parh kar)
2. **Guard hook pehle banao — must-always lever — aur prove karo blocks karta hai:**
   ```text
   Add two house rules my agent can't skip: auto-format... hard-block
   anything that reads my secrets or runs a destructive command. Prove
   both live.
   ```
   Phir reference se compare karo: *"Compare my guard against the proven one..."*
3. **Ek real job ke liye skill banao** (toy nahi — apna review checklist, commit-message format)
4. **Reviewer subagent add karo** jo apni context mein review kare, sirf report kare, edit nahi
5. **MCP server wire karo** — apna connector (pichle course se) ya starter ka sample server chalao
6. **Installable banao, prove karo travel karta hai:** ek doosre project mein install karo, dikhao guard
   wahan bhi kaam karta hai bina extra setup ke

**Done jab:** doosra project bhi same hook se protected ho. **Yehi plugin ka poora point hai: rule
travel karta hai.**

## Part 7 — Ceiling Aur Yeh Kahan Barhta Hai

## Concept 13 — Ceiling, Aur Bridges Bahar

**Loop aapka nahi hai.** Aapke hooks host ke loop ke around fire hote hain; apna loop nahi chalate.
Jab aapko woh worker chahiye jo apna loop own kare — Build AI Agents course.

**Identity aapki nahi hai.** Aapka plugin waisa act karta hai jaisa host chala raha banda hai — koi apna
credential nahi. Jab agent ko apni identity chahiye — [AI Identity](../ai-identity-crash-course/README.md)
course.

**Reach borrowed hai.** Plugin ek remote MCP server ko **wire** kar sakta hai, lekin durable, user-facing
server khud — woh connector-native app hai jo pichle course mein banaya.

**Lekin yeh dekho kahan yeh barhta hai:** Aapka banaya bundle coding agent se **aage** pahunchta hai —
Claude Cowork, claude.ai chat, OpenWork. Aur skill sabse zyada door tak jati hai — OpenClaw aur aage tak.

## Same Skeleton, Doosre Plugins

- **House-style plugin** — writing/code conventions ki skill, formatter, reviewer
- **Safety plugin** — production targets/secrets/destructive commands ke liye guards, kuch aur nahi
- **Service plugin** — hosted API ke liye remote MCP server + usage sikhane wali skill
- **Workflow plugin** — `Stop` hook jo test suite chalaye, release-steps skill

## Capstone

**Apna khud ka plugin ship karo.** Ek real friction chuno jo aapki team coding agent ke sath face karti
hai. Sahi levers se fix karo — kam az kam ek **hook** jo must-always rule enforce kare, aur kam az kam
ek capability lever (skill/subagent/MCP server). Marketplace par publish karo, kisi aur se install
karwao. Confirm karo hook unke liye, unke project mein, bina extra setup ke fire hota hai.

---
[⬅ Ship It](03-ship-it.md) · [⬆ Index](README.md)
