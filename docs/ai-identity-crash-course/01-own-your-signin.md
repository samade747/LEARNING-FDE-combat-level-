# 01 — Apna Sign-In Own Karo (Setup + Quick Win)

## Setup

Poora build ek folder mein hota hai (course base). Yeh jaan-boojh kar lean hai — koi app abhi nahi.
Aapka pehla move agent ko ek banane ke liye direct karna hai.

**Step 1 — environment prove karo:**
```text
Read specs/00-set-up-the-base/spec.md (Phase 1)... Check my prerequisites
(Node, pnpm), install the skills it lists (Better Auth, shadcn, Neon),
and confirm the MCP servers are present and reachable. Don't scaffold
anything yet.
```

**Step 2 — app scaffold karo** (pehle Neon database provision karo):
```text
Now do Phase 2... scaffold the Next.js + Tailwind + shadcn app here,
pin the Better Auth 1.7 stack... Don't build any auth. Start the dev
server and show me the landing page is up.
```

**Done jab:** `pnpm dev` plain landing page serve kare, `pnpm build` aur `tsc` clean chalein.

## Quick Win: Apni Khud Ki App Mein Signed In Ho

4 pieces jo yeh banata hai: **Email/password sign-in** (door ID check karta hai jo aap ne khud set ki),
**session** (venue ko yaad hai aap aaye), **protected route** (back room jahan sirf signed-in members),
**password hash** (one-way fingerprint jo door rakhta hai, aapka asal password nahi).

```text
Read specs/01-own-your-sign-in/spec.md and the better-auth-best-practices
and email-and-password-best-practices skills. Plan the approach, show me
the plan, then build it in small steps. Run the spec's acceptance
checks, including the security ones.
```

**Done jab:** Account banao, dashboard par land ho jo naam/email dikhaye, password sirf one-way hash ki
tarah stored ho.

**Understand prompt** (no spec, sirf dekhne ke liye):
```text
I just signed up. Show me exactly what got stored in the database for
my account, and point out what is NOT there. Where is my password, and
why can't you show it to me?
```

Jawab (password sirf one-way hash hai, khud aapka server bhi wapis parh nahi sakta) — yeh course ki
pehli identity-literacy hai. Aap ne paragraph mein nahi parha — apne data par dekha.

## Poore Build Ki Spine (7 Steps)

```text
Stable Spine (production-grade):
0. Base set up karo
1. Apna sign-in own karo
2. Issuer bano (marquee)
3. Scopes & consent
4. Real app connect karo
5. Resource server connect karo

Edge:
6. Client identity (CIMD) — pre-release plugin, draft standard

Frontier:
Agent credential, on-behalf-of authority, scope/step-up — beta library
```

~50% milestone: sign-in ko harden karo (2FA + social login) — abhi bhi stable ground par.

---
[⬅ Venue Aur Wristband](00-the-picture.md) · [⬆ Index](README.md) · [Agla: Issuer Banna ➡](02-become-the-issuer.md)
