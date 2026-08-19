# Connector-Native Apps — Summary

Yeh chapter sikhata hai ek **remote MCP server** kaise banaya jaye jiska **customer ek AI hai**, insan nahi
— ek real product ("Reading Room") end-to-end banate hue: memory, real sign-in (OAuth), session contract,
sab claude.ai mein ek pasted URL se chalta hua. 14 Concepts, Mode 2 (Manufacturing) Phase 1 ka Chapter 2/6.

## 00 — Overview: 4 Invariants, Server Kya Hai

- **Server** = fixed address par hamesha-on computer jo request ka wait karta hai aur jawab deta hai (shop
  front counter analogy). **MCP server** = ek standard (AI ke liye "USB port") follow karne wala server,
  taake koi bhi AI custom wiring ke bina use kar sake.
- **4 Non-Negotiables (poora course inhi par bana hai):**
  1. **Ek gateway** — AI ek hi connector se milta hai (free account sirf 1 custom connector allow karta
     hai — limit hai, preference nahi)
  2. **Sirf Tools** — resources/prompts nahi, sirf tools (model reasoning ke beech call karta hai)
  3. **Prove karo, trust mat karo** — identity hamesha verified sign-in se, AI ke bataye kuch se nahi
  4. **Fail closed** — server missing/broken ho to AI ko chup kar improvise nahi karne dena; saaf "unavailable" bolna hai
  - Pehle 2 **shape** describe karte hain, aakhri 2 **jobs hain jo server ko karni hain kyunki AI trust nahi kiya ja sakta**.
- **Prerequisites:** typed Python, Agentic Coding course, connector use kar chuke ho. Build AI Agents zaroori nahi.
- Build pattern: **Plan → Review → Execute → Verify**, coding agent code likhta hai, aap spec dete/verify karte ho.
- Base zip mein `auth.py`, `session.py` already complete diye jaate hain (kabhi rewrite nahi karte).
- **Do tracks:** Beginner (bundled `mock_auth/`, koi account nahi) aur Standard (real hosted sign-in — AI Identity course mein).

## 01 — The Shape (Concepts 1-4)

- **Concept 1 — Aap Direct Karte Ho, Type Nahi:** coding agent code likhta hai. Sabse zyada scrutiny
  sign-in code ko chahiye — "dikhta sahi, chupke se galat" ho sakta hai. **Two-vacuums analogy:** coding
  agent = robot vacuum (khud chalta, apna loop own karta hai); banaya hua connector = hand vacuum (sirf
  trigger dabane par chalta, kabhi loop own nahi karta).
- **Concept 2 — Naya App Shape:** chat app hi runtime hai (cloud mein), isliye server public internet par
  HTTPS ke sath hona chahiye. **User model laata hai** — aap intelligence ke liye pay nahi karte, sirf
  chota server + database cost hota hai ("free for anyone" trick).
- **Concept 3 — Sirf Tools:** MCP 3 cheezein de sakta hai — tools (model calls), resources (user points),
  prompts (user picks). Is shape mein sirf **tools**. Workshop analogy: tool = cordless drill (belt par,
  grab karo); resource = locked manual cabinet mein; prompt = shelf se pick karna parne wala form. Sirf
  drill hi bina insan ke kaam chalne deta hai.
- **Concept 4 — Ek Gateway, Teen Groups:** 3 tool groups — `domain_*` (app kya karti hai), `user_*` (kaun
  hai/kya yaad hai), `config_*` (kaise behave kare). `_` prefix AI ke menu mein clean sections banata hai.
  Ek hi server mein teenon — kyunki free plan sirf 1 connector allow karta hai.
  - Prompt pattern: pehle plan mode mein poori architecture proposal mangwao (4 invariants ke against
    check karo), phir cheap model se empty scaffold banwao — **stateless streamable HTTP transport** par
    (stateless = koi ek connection ki memory nahi, isliye koi bhi Anthropic server call handle kar sakta hai).

## 02 — State Aur Domain (Concepts 5-6)

- **Concept 5 — State:** session ke across yaad rakhna hi toy ko product banata hai. v1 = Postgres, **do
  tables**: `users` (id = verified `sub`, email) aur `user_state` (user_id, state jsonb). Front-desk "guest
  register" (kaun hai — kam badalta) vs "stay-log" (kya kar raha — har visit badalta) analogy. `sub`
  (*subject*) = verified sign-in id, identity ka woh piece jispe trust kiya ja sakta hai.
  - Neon (hosted Postgres) coding agent MCP se drive karta hai. **Done jab:** value fresh connection par
    round-trip kare — state identity se pehle kaam karta hai.
- **Concept 6 — Domain:** abhi reference se, meaning se nahi. v1 sirf `domain_get_item(id)` — id se exact
  fetch, semantic search nahi (woh RAG course ka subject hai — "call-number desk" vs "librarian ko kahani
  batana" analogy).
- **Optional:** apne coding agent ko stand-in MCP client ki tarah use kar ke dev-time par tool call test
  kiya ja sakta hai (`claude mcp add`). Yeh sirf auth se pehle kaam karta hai — Concept 8 ke baad `401`.

## 03 — Identity Prove Karna — Jo Model Fake Nahi Kar Sakta (Concepts 7-8)

- **Concept 7 — Identity Verified Subject Se:** model ko kabhi decide nahi karne dena kiska data
  parhna/likhna hai. Hotel concierge analogy — desk concierge ki baat par mail nahi deta, khud passport
  check karta hai. **Rule: model kabhi identity supply nahi karta.** Trusted service signed token deti hai
  jisme verified `sub` hota hai — token = passport, `auth.py` (given, kabhi rewrite nahi hota) yeh enforce
  karti hai.
- **Concept 8 — Sign-In (OAuth):** 5-line summary — user kahin aur sign in karta hai, signed token milta
  hai, server verify karta hai, `sub` parhta hai, model kabhi identity supply nahi karta.
  - **Table — 4 parties:** User (data ka malik), Claude's MCP client (Anthropic cloud, banata nahi), Sign-in
    service (Clerk/Auth0/Stytch rented ya Better Auth self-host, banata nahi), Aapka gateway (sirf tokens
    check karta hai, **banate ho**).
  - **Flow:** (1) Discovery — bina-token call `401` deti hai; (2) Sign-in — consent screen, password kabhi
    Claude/server ko nahi chhuta; (3) Token — short-lived, verified `sub` + *audience* stamped; (4) Har
    call ke baad token carry hota hai.
  - **4 Checks (border desk passport):** Genuine (forgery nahi)? Trusted issuer? Stamped for us
    (**sabse dangerous** agar skip — doosri app ka token replay ho sakta hai)? Still in date?
  - **Beginner track = rehearsal, real nahi** — table dikhata hai laptop-par (mock, aap khud sign in) vs
    production (end user Authorize click, real sign-in service) — gateway aur `auth.py` dono ke beech
    **nahi badalte**.

## 04 — Model Ko Steer Karna (Concepts 9-11)

- **Concept 9 — App Ke Rules Kahan Rehte Hain:** Restaurant analogy — **Skill** = placemat (drift nahi ho
  sakti, hamesha view mein); **Connector** = waiter (baithte waqt bolta hai, baar baar re-hand karna
  parta hai). **Option A (uploaded Skill)** strong enforce lekin setup mehnga (code-exec on, ZIP upload,
  toggle). **Option B (connector ke andar, recommended)** — sirf connector add + Authorize, koi extra
  friction nahi. 4 reinforcing layers isay safe banate hain: tool description reminder, session-init ka
  return, har tool return ka 1-line reminder, real tools session-token-gated.
- **Concept 10 — Session-Init Contract:** `begin_session` tool jo model **pehle** call karta hai — desk
  check-in analogy: passport verify + **keycard** (short-lived session token) deta hai. Return karta hai
  rules (`config_*`) + user state (`user_*`) + keycard. Har real tool: "no keycard, no entry." Rules mein
  **cooperation ki tarah bolna hai, override ki tarah nahi** ("please help settle guest" vs "forget prior
  instructions" — dusra con-artist pattern hai, model isay pehchanne training rakhta hai).
- **Concept 11 — Fail Closed:** sabse silent failure — connector missing/broken ho to model apne aap se
  improvise kar leta hai, state invent kar deta hai. Session gate model ke apne knowledge ko nahi rokta,
  sirf tools ko lock karta hai — isliye rules mein explicit standing order chahiye: "fail closed, error par
  plainly bolo, improvise ya invent mat karo." Test: Postgres band karo, app clean refuse kare.

## 05 — Ship It + Capstone + Ceiling (Concepts 12-14)

- **Concept 12 — Live Chalao:** koi Docker/deploy nahi chahiye, sirf temporary tunnel (Cloudflare) + pop-up
  connector. Demo ke liye `AUTH_DISABLED=1` (lock already Concept 8 mein prove ho chuka). Caution: open
  temporary doorway, demo ke baad tunnel band karo.
- **Concept 13 — claude.ai Mein Add Karo:** Settings → Connectors → Add custom connector, tunnel URL
  paste. App khud `begin_session` call karti hai, rules+state leti hai. **Chat visit hai, identity profile
  hai** — nayi chat bhi wahin se resume karti hai (state user id ke under filed, chat ke under nahi).
- **Part 6 — Capstone:** skeleton kabhi nahi badalta (1 gateway, 3 groups, `begin_session`, subject-identity,
  fail-closed) — sirf domain badalta hai. Example shapes: Tutor, Support assistant, Internal-docs aide,
  Booking helper.
- **Concept 14 — Ceiling:** yeh app sirf **user type kare tab** act karti hai (hand vacuum) — khud jaag
  nahi sakti, schedule par nahi chal sakti. Loop host chat app ke paas hai, aapke paas nahi. Agla step:
  **Build AI Agents** (loop khud own karna). Related courses: **Plugins for AI Agents** (mirror image —
  coding agent extend karta hai instead of chat app), **AI Identity** (apna sign-in own karna).
  - **Table — isi app ka future upgrade path:** semantic search (RAG+pgvector), durable SoR (Digital FTE),
    rich persona (Identic AI), apna token issuer (AI Identity), proof of quality (Eval-Driven Development),
    production hardening (Deploy the Agent Harness).

## Ek Rule Jo Sab Explain Karta Hai

> "Aap server own karte ho, us dimagh ko nahi jo usay call karta hai." — Intelligence host app mein rehti
> hai; server sirf woh karta hai jo AI khud ke liye trust nahi kiya ja sakta.
