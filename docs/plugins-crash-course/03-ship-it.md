# 03 — Part 4: Ship It (Concepts 9-11)

## Concept 9 — Manifest Aur Structure

Claude Code plugin ek folder hai `.claude-plugin/plugin.json` manifest ke sath:

```json
{
  "name": "agent-factory",
  "description": "A portable skill, guard hooks, and a reviewer subagent.",
  "version": "1.0.0",
  "author": { "name": "Your Name" }
}
```

Baqi sab **plugin root** par rehta hai (`.claude-plugin/` ke andar nahi — yehi sabse common structural
galti hai):

```text
agent-factory/
├── .claude-plugin/
│   └── plugin.json          # sirf yeh yahan
├── skills/                  # <name>/SKILL.md
├── agents/                  # subagent definitions
├── hooks/
│   └── hooks.json
└── .mcp.json                # optional
```

`version` updates ke liye matter karta hai. `claude plugin validate` share karne se pehle chalao.

## Concept 10 — Marketplaces: Teammate Ko Kaise Milta Hai

**Marketplace** sirf ek git repository hai jisme ek catalog file (`marketplace.json`) plugins list karti
hai. Koi package registry nahi — bas repo point karte ho.

```json
{
  "name": "agent-factory",
  "owner": { "name": "Your Name" },
  "plugins": [{
    "name": "agent-factory",
    "source": "./plugins/agent-factory",
    "description": "A portable skill, guard hooks, and a reviewer."
  }]
}
```

Teammate:
```text
/plugin marketplace add your-org/agent-factory
/plugin install agent-factory@agent-factory
```

> **Develop karte waqt marketplace skip karo:** `claude --plugin-dir ./plugins/agent-factory` se disk se
> load karo, ya `claude plugin init <name>` se scaffold karo.

**2 manifests ko confuse mat karo:** *plugin* ka `.claude-plugin/plugin.json`; *marketplace* ka
`.claude-plugin/marketplace.json`.

**Pinning:** `ref` branch/tag pin karta hai, `sha` exact commit — dono set hon to `sha` jeetta hai.

**Charge kar sakte ho? Haan, files ke liye nahi.** Marketplace catalog hai, store nahi — koi payment
layer built-in nahi. Aur ek sharp edge: skill ek plaintext `SKILL.md` hai, koi DRM nahi. **Sirf model jo
real subscription support karta hai: hosted access** — valuable logic server par rakho, **server** tak
entry becho, files tak nahi. Installed plugin ek thin, free client hai jiska `.mcp.json` hosted MCP
server ki taraf point karta hai; key subscription gate hai.

## Concept 11 — Plugin User Ke Trust Mein Chalta Hai

Plugin machine par kya kar sakta hai socho: hooks shell commands chalate hain, MCP servers reach out
karte hain. **Plugin install karna kisi aur ka code chalana hai.**

**Author ki tarah:** least privilege. Sirf zaroori hooks, narrowly matched. Trust legible banao:

```text
README.md — the trust contract
  What this plugin installs   (skills, subagents, hooks, MCP servers)
  What hooks run, and when
  What files they inspect
  What commands they execute
  What network access they use (ideally: none)
```

**Installer ki tarah:** dependency ki tarah review karo. `claude plugin details <plugin>` component
inventory aur token cost print karta hai, kuch enable kiye bina.

✓ **Checkpoint:** Manifest, structure, marketplace jahan se teammate install kare, aur trust ka clear-eyed
view. Ab ek aur host, phir poora build.

---
[⬅ Deterministic Lever](02-deterministic-lever.md) · [⬆ Index](README.md) · [Agla: OpenCode + Worked Example ➡](04-opencode-worked-example-capstone.md)
