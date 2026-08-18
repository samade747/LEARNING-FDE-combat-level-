
# content.md — page copy for Abdul Samad's portfolio

Everything under a "### Copy" heading is text meant to land on the page, verbatim or
close to it. Anything after a "> Builder note:" is guidance for Phase 3 (markup/CSS), not
copy — do not render it as visible text.

Every checkable fact below traces to a specific line in `profile.md`. Where I elaborated
(motivation, framing, texture), I stayed inside what J1 calls "a sentence with a person in
it" — no employer, title, date, number, or technology appears that `profile.md` does not
already state.

---

## `#hero`

> Builder note: order of h1/p inside hero is yours (M11). Design.md calls for the name +
> tagline in open display type, with a monospace status line beneath reading like a system
> readout, not a headline.

### Copy

**H1:** Abdul Samad

**P (subhead, open display type):**
IT infrastructure and PSX trading-systems specialist, and full-stack / automation
developer — building AI agents, e-commerce stores and ad campaigns on the side.

**Status line (monospace, small, sits under the subhead):**
`KATS · NDM · Trade Rectification`

> Builder note: those three names are the PSX systems Abdul operates (profile.md,
> Experience → PSX entry, and Skills list) — not a slogan, a status readout, per design.md.

---

## `#about`

> Builder note: J3 requires this section to identify *this* person, not "a passionate
> developer." Every specific noun below is load-bearing — keep them, don't generalise them
> away in editing.

### Copy

Abdul Samad has spent more than four years inside the operations side of the Pakistan
Stock Exchange, keeping KATS, the Negotiated Deals Market and Trade Rectification running
inside a compliance chain that answers to SECP, NCCPL and CDC — work where precision isn't
a value statement, it's the job description. Outside that room he runs Windows Server and
Active Directory environments, LAN/WAN networks and system monitoring, and then, separately,
builds full-stack apps and AI-driven automation — AI agents, chatbots, Shopify and WordPress
stores — for freelance and client work. Few people carry both halves of that at once; this
page is split the same way his work is.

*(≈100 words, clears M11's 40-word floor.)*

---

## `#experience` (extra section — not required by M1/M11, but design.md builds a whole
register split around it; recommended placement is between `#about` and `#projects`, or
wherever the builder likes, as long as the required five ids keep their relative order)

> Builder note: per design.md, the PSX entry is the one monospace log line with the
> status-dot; Aiagentixz, Metafoic and the two freelance entries are open cards.

### Copy — PSX (monospace log entry)

```
● Trading Systems Operations — Pakistan Stock Exchange (PSX, Trading House)
  4+ years, per source — no absolute start date stated
  Systems: KATS · NDM · Trade Rectification
  Compliance: SECP · PSX · NCCPL · CDC
  Karachi, Sindh, Pakistan
```

Operating the KATS core trading system, the Negotiated Deals Market and Trade
Rectification workflows, with regulatory compliance work across the SECP, PSX, NCCPL and
CDC chain.

### Copy — Aiagentixz (open card)

**Aiagentixz — Full-Stack & AI Developer**
Remote and on-site, for a USA-based client. 1 year 5 months, per his own record — the
source gives a duration, not a start or end date. Full-stack and AI development: AI agent
projects, Shopify and WordPress work, and Meta and TikTok ad campaigns.

### Copy — Metafoic (open card)

**Metafoic — Shopify Developer**
Approx. 6 months, per source — again no start or end date given. Shopify development work
for Metafoic.

### Copy — Property Sale/Purchase (open card)

**Property Sale/Purchase — Accountant**
4+ years, per source — no absolute start date stated. Karachi, Sindh, Pakistan.

### Copy — Freelance: Facebook & TikTok Marketing (open card)

**Freelance — Facebook & TikTok Marketing**
Store optimization and sales campaigns for e-commerce clients, run out of Karachi.

### Copy — Freelance: Shopify & WordPress (open card)

**Freelance — Shopify & WordPress (Pakistan, USA, UAE)**
Shopify store creation and optimization across Pakistan, US and UAE markets, plus
WordPress site building — product research, inventory sourcing, Facebook marketing,
Google ads, and wholesaler research.

> Note on completeness: `profile.md`'s source explicitly says more roles will be added
> later — nothing on the page should imply this list is a full work history. None of the
> copy above claims that; leave it that way.

---

## `#projects`

> Builder note: three `###` entries under `## Projects` in `profile.md` → three
> `<article>`s, each ≥25 words, each naming what the thing does and what Abdul did (J2).
> Per design.md, this section is entirely in the open/build register — no monospace here.

### Copy — AI Agents & Automation Builds

Built for Aiagentixz, a USA-based client he works with both remotely and on-site, this is
a cluster of AI agents and automation tools rather than one single app: agents built for
HR processes, cybersecurity automation, and voice and WhatsApp chatbots built on
retrieval-augmented generation (RAG), so they answer from a real knowledge base instead of
guessing. His part covers the full stack and the AI layer — wiring the agents up, building
the interfaces around them, and getting each one from a working prototype to something a
client's team could actually use day to day.

*(~85 words)*

### Copy — Shopify & WordPress Store Builds

Freelance e-commerce build-outs for clients across Pakistan, the US and the UAE: setting
up and optimizing Shopify stores, building WordPress sites, and doing the less visible work
behind a storefront — product research, sourcing inventory, and vetting wholesalers before
anything goes live. Every store is a different market with different assumptions about
what will actually sell, so the research is as much the job as the build itself.

*(~65 words)*

### Copy — Meta & TikTok Ad Campaigns

Freelance management of Facebook and TikTok ad accounts for e-commerce clients — building
out campaigns, optimizing the store pages those ads land on, and adjusting both based on
what converts. This runs alongside the store-building work rather than apart from it: the
same clients often need a storefront that works and a campaign that sends people to it.

*(~62 words)*

---

## `#skills`

> Builder note: 23 skills in `profile.md`, so 23 `<li>`s, all of them. Per design.md, split
> into two lists that never share a column: ops/infrastructure (monospace terminal-style)
> and build (open chip grid). Group headings below are for that split; the skill text
> itself is copied as-is from `profile.md` so nothing drifts from the source.

### Copy — group intro lines (optional, for the seam between the two lists)

Ops / infrastructure — the systems he keeps running:

Build — the things he makes:

### Copy — Ops / infrastructure list (10 items, monospace)

- Windows Server administration
- Active Directory (users, groups, GPOs, domain controllers)
- LAN/WAN networking (TCP/IP, DNS, DHCP)
- Network monitoring & troubleshooting
- Cybersecurity fundamentals & endpoint security awareness
- System performance monitoring & root cause analysis
- IT governance & compliance (SECP, PSX, NCCPL, CDC)
- PSX trading systems operations (KATS, NDM, Trade Rectification)
- Project management
- IT strategy & planning

### Copy — Build list (13 items, open chip grid)

- Next.js
- React.js
- Node.js
- Express.js
- MongoDB
- FastAPI / REST, GraphQL & WebSocket API development
- Headless CMS (Sanity)
- Shopify development
- WordPress development
- Meta (Facebook/Instagram) & TikTok Ads
- AI agent development (Agentic AI, Python)
- Docker
- Kubernetes

10 + 13 = 23, matching `profile.md`'s Skills list exactly — none added, none dropped.

---

## `#contact`

### Copy

A short lead-in line:
Reach out by email, or find the work on GitHub, LinkedIn and X.

Links:
- Email: samad.e747@gmail.com → `mailto:samad.e747@gmail.com`
- Phone: +92 332 8222026
- Location: Karachi, Pakistan
- GitHub: https://github.com/samade747
- LinkedIn: https://www.linkedin.com/in/webdeveloper-mern-stackspecialist-samaddeveloperaiagentsdev/
- X: https://x.com/samaddeveloper

> Builder note: `mailto:samad.e747@gmail.com` alone already satisfies M11's "≥1 `<a>` with
> `mailto:` or `https://`" — the rest are bonus, real links, not placeholders.
> `profile.md`'s source also lists a "Portfolio" link with no resolvable URL — correctly
> omitted, not guessed at. Do not add one.

---

## `<nav>` label suggestions (for M17 — not a `content.md`-mandated section, but the nav
needs real words too)

Home · About · Experience · Projects · Skills · Contact

(Drop "Experience" from the nav if Phase 3 decides not to build that section — the
required five, hero/about/projects/skills/contact, must stay in that order regardless.)

---

## Report — where `profile.md` was thin

1. **Metafoic** entry has nothing beyond a role title and a duration ("Approx. 6 months,
   per source"). I did not elaborate beyond that — there's no "what it did / what he built"
   in the source for this role, unlike the Aiagentixz and freelance entries, so the copy
   for it is deliberately short rather than padded.
2. **Property Sale/Purchase — Accountant** is the same shape: title, duration, location,
   nothing else. No description of duties exists in `profile.md`, so none is on the page.
3. **Education/Certifications were not written into any of the five required sections**
   because M1/M11 don't require an education section and design.md doesn't design one.
   `profile.md` does support one if a later phase wants it, but two traps live there that
   whoever writes it would need to hold: (a) SMIT/BanoQabil/PIAIC/GIAIC are training-institute
   programs, not degrees — "program" or "completed," never "degree," and PIAIC/GIAIC's
   "AI Developer" labels are program names, not a professional title or certification; (b)
   the Karachi University B.Com. date range (2007–2008) must be reproduced exactly as
   the source states it, unusual as it looks, not "corrected."
4. **committers.top** is intentionally absent from this page's copy. `profile.md`'s own
   source notes exclude it from Certifications because it's a contributor-ranking listing,
   not an issued credential — I left it out entirely rather than rephrase it in, since
   nothing in the required sections needed it.
5. Everything else — Projects (3/3), Skills (23/23), Contact — was thick enough in
   `profile.md` to write from directly; no gaps to flag there.
