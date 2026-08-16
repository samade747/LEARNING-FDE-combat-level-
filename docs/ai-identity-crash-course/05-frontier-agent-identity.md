# 05 — Frontier: Agent Ke Liye Identity

Ab doosra half, aur course hone ki asal wajah. Ab tak har token ek insan ke liye khara tha. Lekin
Manufacturing path un agents ke baare mein hai jo apne aap kaam karte hain. To sawal ghumta hai: jab
agent kuch kare, **kiski** band pehne hue hai? Agar woh sirf aapka login reuse kare, logs kahengi **aap**
ne kiya, woh sab kuch kar sakta hai jo aap kar sakte ho, aur aap agent ko revoke nahi kar sakte bina khud
ko lock-out kiye. **Yeh galat jawab hai.**

## Aaj Vs Fix

**Aaj:** ek master band (shared token), har agent uski photocopy pehne hue. Server sirf ek shared band
dekhta hai — kaunsa agent? Pata nahi. Ek revoke karo? Nahi kar sakte, sab revoke ho jayenge.

**Agent Auth ke sath:** har agent ek trusted **host** ke under chalta hai aur apni khud ki band pehnta
hai, apni khud ki limits ke sath (agent 1: read only; agent 2: transfer $500 tak; agent 3: 50 reads/hour).
Server exactly kaunsa agent act kar raha hai dekhta hai, aur ek ko doosron ko chhue bina revoke kar sakta
hai.

## Band Milne Ka Flow (5 Steps)

1. **Discover** — agent booth aur uske house rules dhoondta hai (`GET /.well-known/agent-configuration`)
2. **Register** — host agent ko vouch karta hai, uski key + capabilities bhejta hai
3. **Approve** — insan "haan" bolta hai (delegated agent ke liye device code), ya house policy decide
   karti hai (autonomous ke liye)
4. **Sign** — agent apni khud ki short-lived Ed25519 band har call par khud sign karta hai
5. **Verify + run** — server band, grant, limits check karta hai, phir capability chalata hai

> Yeh 3 projects **beta** `@better-auth/agent-auth` plugin par chalte hain — Agent Auth Protocol ka
> implementation. Specific API ko ek swappable instantiation samjho; jo version istemal karo usay pin
> karo.

## Agent Ki Apni Band

Ab tak aap guest the. Yahan ek naya guest ata hai: AI agent. Pehla instinct usay **aapki** band pe clip
karna hai — yehi impersonation problem hai. Iski jagah agent **apni** band leta hai.

**3 cheezein jo isay farq karti hain:**
1. **Agent akela nahi ata** — ek **host** (runtime jo venue trust karta hai) ke andar chalta hai
2. **Band self-sealed aur short-lived hai** — agent apni band apni key se sign karta hai, ~1 minute
   ke liye chalti hai — churayi hui band leak hote hi almost stale ho jati hai. Seal **EdDSA** (Ed25519)
   hai (RS256 nahi — alag trust domain, alag signer)
3. **Capabilities** — named actions ki list, scope ka agent-version

```text
Read specs/projects/agent-credential/spec.md... Confirm the live
agent-auth surface against the Better Auth docs MCP first, it is beta.
Plan it, show me the plan, then build in small steps: enable autonomous
agent identity, register an agent under a host, have it self-sign its
own short-lived credential, and execute a granted capability.
```

> **Tension jo resolve hoti hai:** Bartender **kabhi booth ko phone nahi karta** (offline JWKS), phir bhi
> revoked band ki agli call fail honi chahiye. Short-lived band hi iska solution hai — jab band ~1 minute
> chalti hai, revoke karna simply *dobara issue na karna* hai. Band khud apni window mein mar jati hai.

## On-Behalf-Of: Ek Stamped Band

Yeh sabse important credential hai. Agent aksar **kisi ke liye** act karta hai. On-behalf-of honest
version hai: band **dono** parties naam leti hai — agent aur woh insan jiske liye act kar raha hai —
kaam hamesha agent-for-Alice pair ko attribute hota hai, sirf Alice ko nahi.

**Safe banane wali cheez: human approval loop mein.** Agent khud ke liye yeh band mint nahi kar sakta.
Woh poochta hai, Alice ko prompt milta hai (device-code flow — TV ko streaming account mein login karne
jaisa), aur woh "haan" bolti hai **authority exist hone se pehle.** No approval, no band.

```text
Read specs/projects/on-behalf-of/spec.md... Plan it, show me the plan,
then build it in small steps: enable delegated mode, have an agent
request a scoped capability, gate it behind human device-code approval,
and only then let it act.
```

## Band Tighten Karo: Scope, Value, Aur Dangerous Cheezon Ke Liye Fingerprint

- **Capability** — named action (agent note *share* kar sakta hai)
- **Value-constraint** — sirf allowed values tak narrow karta hai — "notes share kar sakta hai **sirf
  `@acme.com` ke sath**" — scope string yeh express nahi kar sakti
- **Step-up approval** — human gate ko action ke blast radius ke mutabiq scale karta hai: read auto-grant,
  share ko logged-in human chahiye, irreversible action (*delete everything*) ko **physical presence**
  (fingerprint/passkey) chahiye — taake AI agent khud apni destruction ko approve na kar sake

```text
Read specs/projects/step-up-approval/spec.md... three capabilities
across the approval ladder (auto, session, physical-presence), one with
a required value-constraint, and a single-use grant.
```

## Maturity Note: Yeh Honest Hai, Hype Nahi

Course aapko **durable primitives** par anchor karna sikhata hai — verified sign-in, agent ki apni
credential, on-behalf-of delegation, least-privilege scope, human approval. Phir har layer kitni settled
hai, saaf batata hai:

- **Stable spine aaj production-grade hai.** Sign-in, issuer, scopes/consent, real app, resource
  server — sab Better Auth par chalte hain, live verified.
- **CIMD edge hai.** Kaam karta hai, pinned aur proven hai, lekin pre-release/draft standard par chalta
  hai.
- **Agent identity frontier hai.** Industry isi taraf ja rahi hai, lekin standards abhi young hain.

## Yahan Se Aage

Poori identity layer ka through-line: koi bhi system uthao, ek sawal poocho — **yeh identity kiski hai,
authority insan se agent tak kaise pahunchi?** Door, booth, band, bartender dhoondo, phir poocho agent
insan ki band borrow kar raha hai ya apni.

- **Build AI Agents** — agent ko uska **loop** deta hai (reasoning + tools)
- **Human-Agent Teams** — is identity ko kaam mein lagate hain, agents ka roster insano ke sath

**Aap ne identity borrow karna band kar diya. Ab se, aap isay issue karte ho.**

---
[⬅ CIMD + Milestone](04-cimd-and-milestone.md) · [⬆ Index](README.md)
