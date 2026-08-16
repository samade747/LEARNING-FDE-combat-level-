# 01 — Part 2: Capability Levers (Concepts 4-6)

3 levers jo agent ki **capability** barhate hain (chautha, hooks, alag hai — apna Part hai).

## Concept 4 — Skills: Knowledge Jo Agent Choice Se Use Karta Hai

**Skill** ek folder hai jisme `SKILL.md` hai — description + instructions. Claude **description parhta
hai**, aur jab task match kare, khud usay pull karta hai — **model-invoked.**

```markdown
---
description: Review a diff for our team's standards. Use when reviewing code or a PR.
---

When reviewing, check in this order:
1. Does it match the existing patterns in the file?
2. Error handling and edge cases.
3. Tests for the new behavior.
4. Security: secrets, input validation, injection.
```

**Description sabse important line hai** — yeh decide karti hai skill relevant hai ya nahi, isliye
*"kab use karna hai"* ke baare mein likho, sirf "kya hai" nahi.

**Skill ek dafa likho, har tool parhta hai.** Portable rakhne ke liye: sirf `name`/`description`
frontmatter par rely karo, tool-specific cheezein (`$ARGUMENTS`, `allowed-tools`) mat use karo. Har host
apna khud description se skill invoke karta hai — baqi cheez jo ek tool support kare, doosra ignore ya
choke kar sakta hai.

## Concept 5 — Subagents: Fresh Context Ke Sath Delegate Karna

**Subagent** ek helper hai jisay main agent kaam de sakta hai, apni **khud ki clean context window** aur
apni instructions ke sath.

```markdown
---
name: reviewer
description: Reviews a diff against our standards. Use after a change is written.
---

You review code in your own context. Check, in order: matches existing
patterns, error handling, tests, security. Report findings as a short
ordered list. Do not edit files — only review and report.
```

Delegation 2 wajah se matter karta hai: subagent main conversation se distract nahi hota, aur uska kaam
main context ko clog nahi karta. **Use karo jab task self-contained aur verifiable ho** — "yeh diff
review karo," "yeh function kahan kahan call hota hai dhoondo."

**Galti se bacho:** har cheez ko subagent mat banao. Delegation ki cost hai (fresh context ko batana
parta hai usay kya chahiye).

## Concept 6 — MCP Servers: Bahar Ki Reach Jo Plugin Ship Kar Sakta Hai

Chautha lever agent ko aisi reach deta hai jo pehle nahi thi — aapki internal API, database, service —
ek **MCP server** ki taraf point kar ke. Aap [Connector-Native Apps](../connector-native-apps/README.md)
mein ek pehle hi bana chuke ho — **yahan doosra nahi banate. Plugin ka poora kaam usay wire karna hai.**

```json
{
  "mcpServers": {
    "my-api": {
      "type": "http",
      "url": "https://api.yourdomain.com/mcp",
      "headers": { "Authorization": "Bearer ${MY_API_KEY}" }
    }
  }
}
```

Server **remote** hai jaan-boojh kar — logic, data, secrets aapke control ki infrastructure par rehte
hain, plugin sirf pointer ship karta hai. **Server kahan se ata hai? Woh jo aap already bana chuke ho.**
Apna connector kholo, agent se chalwao, URL copy karo `.mcp.json` mein.

> **Local server kyun nahi?** Local server apna code plugin ke saath ship karta hai aur kisi aur ke
> computer par chalta hai — copyable, aisi runtime jo aap own nahi karte. Remote server almost hamesha
> sahi choice hai: ek dafa build/host karo, phir kitne bhi plugins usay URL se point kar sakte hain.

✓ **Checkpoint:** Skills knowledge add karte hain, subagents focused help add karte hain, MCP servers
reach add karte hain — teenon **advisory** hain (model decide karta hai kab use kare). Ab woh lever jo
optional nahi.

---
[⬅ The Shape](00-the-shape.md) · [⬆ Index](README.md) · [Agla: Deterministic Lever ➡](02-deterministic-lever.md)
