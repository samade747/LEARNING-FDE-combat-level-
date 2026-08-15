# 01 — Constrain: Agent Ko Rokna

Pehla verb — sab se kam exciting, sab se zyada important. Ek loop mein agent **saikron actions**
leta hai, koi dekh nahi raha. Constraint isay survivable banata hai: aap **pehle se, likh kar** decide
karte ho konsi actions free hain, konsi ko insaan chahiye, aur konsi bilkul **namumkin** hain.

## Concept 4: Permission Rules — Allow, Ask, Deny

Raat 3 baje agent ek command chalana chahta hai. Koi awake nahi hai judge karne ke liye, to kuch to us
lamhe "haan" ya "nahi" bolega — aur wo hai **rule jo aap ne pehle likh rakhi hai**. Har mature harness
constraint ko isi tarah likhti hai — actions ki list, har ek ka jawab teen mein se ek:

> **Allow** = green light (chup chaap chala do)
> **Ask** = doorbell (ruko, insaan se "haan" lo)
> **Deny** = deewar (kabhi nahi, kisi ke bhi puchne pe)

**Design skill:** har action ko bucket mein dalna hai — aur ek reliable rule hai: **blast radius**
(agar galat ho jaye to kitna nuksan) se sort karo, **kitni baar hota hai** se nahi.

- Normal source file parhna → low risk → **allow**
- Secrets/credentials parhna → **deny** ya isolate karo (fooled agent kuch bhi leak kar sakta hai jo usne parha ho)
- Test suite chalana → **allow**
- Branch pe push karna → visible aur reversible hai, to **ask**, ya sirf `claude/` branches ke liye allow karo
- Worktree se bahar files delete karna, secrets touch karna, force-push, harness ka apna config badalna → **deny**

> **Jab shak ho, ek bucket sakht rakho jo convenient lage usse.** Ek hafte ki clean runs ke baad rule
> loosen karna sasta hai. Delete hui production database explain karna sasta nahi.

**Paisa bhi constrain bucket mein aata hai:** per-run spend cap, step cap, aur konsa model konsa job use
kare — ye bhi permission rules hain, sirf files ki bajaye budget guard karti hain.

### Claude Code — `settings.json`

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Bash(npm test *)",
      "Bash(git diff *)",
      "Bash(git push origin claude/*)"
    ],
    "ask": ["WebFetch"],
    "deny": [
      "Read(./.env)",
      "Read(./secrets/**)",
      "Bash(rm -rf *)",
      "Bash(git push --force *)"
    ]
  }
}
```

**Priority order:** Deny > Ask > Allow — matlab broad allow kabhi narrow deny ko leak nahi kar sakta.

**Honesty note:** Deny patterns **command text** match karte hain, **matlab nahi**. `Bash(rm -rf *)`
`rm -fr` ya Python one-liner ko nahi pakregi jo wahi folder delete kar de. In rules ko **tripwires**
(simple alarms) samjho — asli deewar **sandbox** hai (agla concept).

**2 naye surfaces:**
- **Parameter matching** — `Agent(model:opus)` jaisi rules, "kaunsa tool" se "kaunsa tool, kaise use hua" tak
- **Auto mode** — background classifier har action review karta hai: safe chalao, risky block/dikhao

### OpenCode — `opencode.json`

```json
{
  "permission": {
    "edit": "ask",
    "bash": {
      "*": "ask",
      "npm test*": "allow",
      "git diff*": "allow",
      "git push --force*": "deny",
      "rm -rf*": "deny"
    }
  }
}
```

- **Per-agent overrides** — reviewer agent apna alag `permission` block rakh sakta hai (read-only)
- **`permission.task` rules** — subagents khud subagents start na kar sakein, isay control karta hai

OpenCode mein jo product ke andar nahi milta, wo platform se lo: GitHub branch-protection rules "kabhi
main pe push nahi" ko repo ka **fact** bana dete hain.

## Concept 5: Sandboxes — Nuksan Ko Namumkin Banana

Permission rules limit karti hain agent **kya karta** hai. **Sandbox** limit karta hai wo **kahan**
kar sakta hai. Perfect rules wala agent bhi 100% safe nahi — ek bug, ya text mein chhupi hui ek hidden
instruction, agent se aisi cheez try karwa sakti hai jo aap ne list hi nahi ki thi. Isay **prompt
injection** kehte hain — attacker normal text (jaise bug report ka title) mein command chupata hai, aur
agent usay follow kar leta hai.

**Sandbox agent pe trust nahi karta.** Use jo karna hai karne do — andar jo bhi tootey, andar hi rehta
hai (jaise bachon ke sandpit).

**4 fences:**

1. **Worktree** (pichli course se) — har run ki apni copy
2. **Filesystem fences** — agent sirf apni workspace mein likh sakta hai, kahin aur nahi (unreachable)
3. **Network fences** — chhoti allowlist ya bilkul network nahi. Agar internet reach hi nahi, to koi
   injected instruction bhi code leak nahi kar sakti
4. **Branch fences** — unattended pushes sirf `claude/` branches pe, `main` hamesha human gate ke peeche

### Prompt Injection Ka Doosra, Zyada Khatarnak Form: Tool Poisoning

Yahan attack us text mein nahi ata jo agent parhta hai — ye ek **tool ki apni description/metadata**
mein chhupa hota hai (wahi text jo agent decision ke waqt trust karta hai). Ek poisoned MCP server
instructions carry kar sakta hai jo user ko kabhi dikhti hi nahi, sessions ke darmiyan persist kar sakti
hain, ya "rug-pull" kar sakti hain (install pe achha behave kare, baad mein malicious update push kare).

**Defense:** MCP servers ki **enforced allowlist**, version-pinned — koi naya/updated tool bina review
production loop tak na pohanche. Har connector ko utni ehtiyat se treat karo jitni har naye package ko.

### Self-Check
**Sawal:** Overnight loop mein agent ek malicious issue se prompt-injected ho jata hai aur `.env` file
bahar bhejne ki koshish karta hai. Do alag fences batao jo isay independently rok sakti hain.
**Jawab:** In mein se koi 2: **deny rule** `.env` pe (file kabhi milti hi nahi), **network fence**
(bahar reach hi nahi hoti), ya **filesystem fence** (real `.env` mount hi nahi hota). **Defense in
depth** poora point hai — har fence akela kaam karta hai, isliye kai fences chalao kyunke koi ek
misconfigure ho sakta hai.

---
[⬅ Overview](00-overview.md) · [Agla: Inform ➡](02-inform.md)
