# AI Identity: Human Sign-In and Agent Access — Summary

Mode 2 Phase 1, aakhri chapter (6/6). Core sawal poore course ka: **yeh identity kiski hai, aur
authority insan se agent tak kaise pahunchti hai?** Do halves: pehle apna sign-in own karo, phir agent
ko apni (borrowed nahi) identity do — scoped, time-boxed, revocable, human-approved.

## 00 — Ek Tasveer: Venue Aur Wristband

- Metaphor table: Door=Sign-in, Booth=Issuer, Wristband=Token, Bartender=Validator. Booth ke paas
  private key (seal), public photo (published key) — verify kar sakte ho, forge nahi.
- Frontier: agent ki apni band, kabhi kabhi stamped ("acting for Alice...") = on-behalf-of authority.
- Session = server ko yaad hai (cookie). Token = signed claim (JWT: header.payload.signature). OAuth/
  OIDC = protocol jahan booth doosri app ke liye band print karti hai.

## 01 — Apna Sign-In Own Karo (Setup + Quick Win)

- Setup: Node/pnpm/Better Auth/shadcn/Neon, Next.js scaffold, phir email/password sign-in + session +
  protected route + password hash (one-way, server bhi wapis nahi parh sakta).
- Poore build ki 7-step spine: Base → Sign-in → Issuer → Scopes/Consent → Real app → Resource server
  (Stable, production-grade); CIMD (Edge, pre-release); Agent credential/on-behalf-of (Frontier, beta).
- ~50% milestone: sign-in harden karo (2FA + social login).

## 02 — Issuer Bano + Scopes Aur Consent

- **Step 2 — Become the Issuer**: bartender se booth ban jate ho — signed tokens issue karte ho jo
  doosri app khud verify kare (no DB call, public seal se). Authorization-code flow: code → app swap
  karti hai real token se. PKCE = proof same app ne shuru/khatam kiya. Consent screen approval se pehle.
- 3 Understand Prompts: JWKS endpoint dekho (private key nahi), `aud` 1 character se todo (reject),
  expired token push karo (reject).
- **Step 3 — Scopes & Consent**: token exactly bataye kya allowed hai. Consent screen exact list
  dikhaye. Least privilege real ban jata hai.

## 03 — Real App Connect Karo + Resource Server

- **Step 4**: client app (Notes) AuthCo se sign in — koi password/DB nahi chhuti. Verify: no secret
  copy, `aud` todo (reject), client revoke karo (agli call fail).
- **Step 5**: resource server = bearer token leta hai, `aud` parhta hai, RS256 check karta hai. 4 attack
  tests: galat algorithm, `alg:none`, HMAC-as-secret forgery (isliye algorithm pin karna zaroori),
  galat audience.

## 04 — CIMD (Edge) + 50% Milestone

- **CIMD** (Client ID Metadata Document) — pre-registration skip, app URL par public sign latka deti
  hai, booth pehli baar aate hi parh leti hai. Better Auth pre-release plugin + IETF draft standard.
- ~50% milestone project: **2FA** (second factor) + **Social login** ("Continue with Google") —
  sign-in ko harden karna, stable ground par pehla self-driven project.

## 05 — Frontier: Agent Ke Liye Identity

- Aaj (galat): master band shared, sab agents photocopy pehne — revoke sab ko revoke karta hai. Fix:
  har agent apni band, apni limits ke sath — server exact agent dekhta hai, individually revoke kar
  sakta hai.
- **5-step flow**: Discover (`.well-known/agent-configuration`) → Register (host vouch) → Approve
  (device-code/policy) → Sign (agent apni Ed25519 short-lived band khud sign karta hai) → Verify+run.
  Sab `@better-auth/agent-auth` beta plugin par.
- Agent ki apni band: host ke under chalta hai, self-sealed + short-lived (~1 min, EdDSA), capabilities
  (named actions). Revoke = simply dobara issue na karna.
- **On-Behalf-Of**: band dono naam leti hai (agent + human), human approval loop mein zaroori (device-
  code flow), authority exist hone se pehle approval chahiye.
- Tightening: capability, value-constraint (scope string se zyada precise), step-up approval (blast
  radius ke mutabiq: auto/session/physical-presence — irreversible actions ke liye fingerprint).
- Maturity note: stable spine production-grade, CIMD edge, agent identity frontier (young standards).
- "Aap ne identity borrow karna band kar diya. Ab se, aap isay issue karte ho."
