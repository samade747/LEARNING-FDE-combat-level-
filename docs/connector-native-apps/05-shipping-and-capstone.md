# 05 — Part 5 & 6 & 7: Ship It + Capstone + Ceiling (Concepts 12-14)

## Concept 12 — Live Chalao (No Docker, No Deploy)

Kyunki Claude aapke server tak Anthropic ke cloud se pahunchta hai, "mere laptop par kaam karta hai"
kaafi nahi. Poora deploy ki zaroorat nahi bas **dekhne** ke liye ke kaam karta hai — ek temporary public
doorway kholo, ek **tunnel**, aur connector ka quick **pop-up** chalao. Free, koi host account nahi, ek
minute mein.

Ek honest move: claude.ai real OAuth se sign in karwata hai, aur abhi aapke paas real sign-in service
nahi hai. To is personal demo ke liye lock **off** kar do: `AUTH_DISABLED=1`. Aap ne Concept 8 mein pehle
hi lock prove kar liya tha mock ke against — yahan sirf temporarily set aside kar rahe ho.

```text
Put my connector live with the live-connector skill: turn auth off,
start the gateway, open the Cloudflare tunnel, and give me the public
connector URL.
```

**Done jab:** Skill ek `https://….trycloudflare.com/mcp` URL print kare aur unauthenticated `tools/list`
`200` return kare.

> **Caution:** Yeh ek open, temporary doorway hai. Auth off ke sath, jiske paas URL ho woh aapke tools
> aur Neon data tak pahunch sakta hai. Demo ke baad tunnel band kar do.

## Concept 13 — claude.ai Mein Add Karo Aur Poori App Dekho

1. **claude.ai** mein: **Settings → Connectors → Add custom connector.** Tunnel URL paste karo
   (`/mcp` par khatam), **Add** click karo
2. App ko plain language mein kaam karne ko kaho
3. Ek bilkul nayi chat kholo aur usay pooch ke jahan chhoda tha wahin se continue karo

**Kya dekhoge:** App khud ki tarah respond karti hai — model pehle `begin_session` call karta hai,
aapke rules aur stand-in user ka state leta hai, gated tools se kaam karta hai. Chunke state user id
ke under filed hai (chat ke under nahi), ek bilkul nayi chat bhi wahin se resume karti hai jahan chhoda
tha — **chat visit hai, identity profile hai.**

✓ **Checkpoint:** Aap ne poori app claude.ai ke andar chalte dekhi — identity-gated session ke through
tools call, memory chats ke across carry, app fake karne ki jagah fail-closed — sab ek free account par.
Baqi bacha ek real sign-in service — agla stop [AI Identity](https://agentfactory.panaversity.org/docs/ai-identity-crash-course).

## Part 6 — Capstone: Apna Khud Ka Domain

Skeleton kabhi nahi badalta — ek gateway, teen tool groups, `begin_session` contract, subject se
identity, fail closed — **sirf teen groups badalte hain.**

Kuch shapes:

- **Tutor** — domain: course content; user: learner ki progress; config: teacher persona + method
- **Support assistant** — domain: orders/policies; user: customer ki ticket history; config: tone +
  escalation rules
- **Internal-docs aide** — domain: team wiki search; user: kaunsi team; config: confidential kya hai
- **Booking helper** — domain: availability/reservations; user: saved preferences; config: cancellation
  rules

Wahi loop chalao: **plan → review → scaffold → accumulate → verify.**

```text
Before you build anything, map my domain onto the three groups for me:
what goes in domain, what goes in user, what goes in config, and what
begin_session should hand back for this app.
```

## Part 7 — Ceiling Aur Yeh Kahan Barhta Hai

### Concept 14 — Ceiling, Aur Loop Own Karne Ka Pull

Jo aap ne banaya woh sirf tab act kar sakta hai **jab user type kare.** Hand vacuum hai — hath squeeze
karne tak dead. **Yeh khud jaag nahi sakta, schedule par chal nahi sakta, kuch notice kar ke khud reach
out nahi kar sakta.** Yeh koi khami nahi hai — connector-native app ki nature hai. **Loop host chat app
ke paas hai, aapke paas nahi.**

Jaise hi aapko woh worker chahiye jo khud chale — jaage, steps le, tools loop mein call kare, aapke sote
waqt kaam khatam kare — aapko **loop khud own karna** parega. Yeh robot vacuum hai, aur yehi path aage
jata hai. *Build AI Agents* mein aap hand vacuum tend karna chhod kar robot banate ho.

**Do courses pehle ate hain:**

- **Plugins for AI Agents** — is course ka mirror image: connector-native app **chat app** (claude.ai)
  ko extend karta hai; plugin **coding agent** (Claude Code, OpenCode) ko extend karta hai
- **AI Identity** (Better Auth par bana) — pehle aap **sign-in own karte ho**, phir **agent ko apni
  identity** dete ho

### Same App, Poore Mode 2 Mein Deepen Hoti Hai

Aap v1 phenkte nahi. Baad ke courses **isi app** ko upgrade karte hain:

| Add Hoga | Kya Upgrade Hota Hai | Kahan |
| --- | --- | --- |
| Semantic search domain par | `domain_get_item` → `domain_search` | RAG on Postgres + pgvector |
| Durable system-of-record | Bare two-table memory | Building a Digital FTE |
| Rich persona/config | Simple `config_*` rules | Identic AI |
| Apna token issuer + agent identity | Rented sign-in service | AI Identity |
| Proof ke yeh acha kaam karti hai | "lagta hai kaam karta hai" | Eval-Driven Development |
| Production hardening | Live tunnel demo | Deploy the Agent Harness |

---
[⬅ Model Ko Steer Karna](04-steering-the-model.md) · [⬆ Index](README.md)
