# 01 — Part 1: The Shape (Concepts 1-4)

## Concept 1 — Aap Direct Karte Ho, Type Nahi Karte

Aap yeh server haath se nahi likhoge. Coding agent ko batao kya chahiye, woh code likhta hai, aapka kaam
parhna, chalana, check karna hai. Sabse zyada checking chahiye **sign-in code** ko (Concept 8) — agent
khushi khushi aisa sign-in code likh dega jo **dikhta** sahi hai lekin chupke se ghalat hai.

**Do vacuums yaad rakho:** Robot vacuum khud chalta hai — khud jagta hai, ghar mein ghoomta hai, khud
faislay karta hai. Hand vacuum sirf trigger dabane par chalta hai. **Coding agent** jo yeh banata hai
robot vacuum hai — khud chalta rehta hai. **Connector jo aap banate ho** hand vacuum hai — user ke haath
lagane tak dead rehta hai. Yeh self-running quality ka naam hai **"owning the loop"** — robot vacuum
apna loop own karta hai, aapka connector kabhi nahi. Aap ek loop-owning program se ek non-loop-owning
program bana rahe ho.

## Concept 2 — Naya App Shape

Ab aap khud server hain, aur caller AI hai. Teen facts jo har agla decision drive karte hain:

- **Chat app hi runtime hai, aur cloud mein rehta hai.** Jab user connector add karta hai, Claude
  Anthropic ke cloud se aapke server tak pahunchta hai — user ke laptop se nahi. To aapka server public
  internet par HTTPS ke sath hona chahiye.
- **User model laata hai.** Aap intelligence ke liye pay nahi karte — user ka free Claude tier deta hai.
  Aapka cost sirf chota server aur database hai. Yehi "free for anyone" ka economic trick hai.

## Concept 3 — Sirf Tools — Resources Nahi, Prompts Nahi

MCP server 3 cheezein offer kar sakta hai: **tools** (model call karta hai), **resources** (user point
karta hai), **prompts** (user pick karta hai). Is app ke shape ke liye, hum **sirf tools** use karte hain.

**Workshop socho:** **Tool** worker ki belt par cordless drill hai — kaam ke beech mein grab karo, kisi
se poochna nahi. **Resource** cabinet mein locked manual hai — koi walk kar ke le kar aaye tabhi useful.
**Prompt** ek form hai jo worker ko shelf se pick karna parta hai. Sirf drill hi kaam bina insan ke chalta
rehne deta hai.

## Concept 4 — Ek Gateway, Teen Groups (Plan Karo, Phir Scaffold)

Aapka server ek sath alag alag jobs karega. Sab tools ko ek dhaer mein daal do to do cheezein toot jati
hain: AI ko "article fetch karo" aur "yeh save karo" mein farq samajh nahi ata, aur **aap** khud ek hisse
par sochte waqt doosre se takrate ho. Fix: **har kism ke kaam ko apna labeled group do.**

Connector-native app mein hamesha yeh 3 kism ke jobs hote hain:

- **`domain_*`** — app asal mein kya karti hai (articles search, item fetch)
- **`user_*`** — kaun hai yahan, aur uske baare mein kya yaad hai (library card, saved shelf)
- **`config_*`** — app kaise behave kare (librarian ke rules, voice)

`domain` = **kaam**, `user` = **banda**, `config` = **behavior**. `_` prefix isay AI ke menu mein clean
sections mein dikhata hai.

**Ek server kyun, teen nahi?** Free plan par user sirf **ek** custom connector add kar sakta hai. Teenon
groups **ek** server mein, ek URL ke peeche.

```text
domain_search      domain_get_item      domain_do_action
user_get_profile   user_save_state
config_get_rules   config_get_persona
```

**Prompt 1 — poori cheez plan karwao, code likhne se pehle.** Plan mode (`Shift+Tab` Claude Code,
`Tab` OpenCode) mein, strong model par:

```text
I want to build the Reading Room connector on this base. Read AGENTS.md
and use the mcp-builder skill for tool naming and schemas, then propose
the architecture for me: the one gateway, the three tool groups (domain,
user, config), how it remembers a person, and how it proves who is
signed in. Show me the complete plan and the tool list before you write
any code, and for each piece tell me which of the four invariants it
serves and flag anything you are unsure about.
```

**Phir plan ko inspector ki tarah parho** — 4 invariants ke against check karo: ek gateway? sirf tools?
identity verified sign-in se, tool argument se nahi? fail-closed rule config mein?

**Prompt 2 — empty frame scaffold karo, prove karo khada hai.** Cheap model par (thinking plan mein ho
chuki):

```text
Looks right. With the mcp-builder skill's guidance, scaffold the
gateway: one FastMCP server on stateless streamable HTTP transport,
with a health tool and a domain_get_item stub. Run it and show me a
local client listing both tools, with no auth and no real data yet.
```

**Stateless streamable HTTP** wahi wire format hai jispar Claude jaisa remote host aapko reach karta hai
— *stateless* ka matlab server kisi ek connection ki memory nahi rakhta, isliye Anthropic ke koi bhi
servers koi bhi call handle kar sakte hain.

✓ **Checkpoint:** Ek gateway, tools naam se grouped, sahi transport par khada. Har agla concept isi
server mein ek real piece add karega.

---
[⬅ Overview](00-overview.md) · [⬆ Index](README.md) · [Agla: State Aur Domain ➡](02-state-and-domain.md)
