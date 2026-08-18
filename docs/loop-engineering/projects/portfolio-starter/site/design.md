# The design decision
Two typographic registers run through the page and never mix — monospace, exact, status-tagged for the regulated trading-systems work he operates (KATS, NDM, Trade Rectification, the SECP/PSX/NCCPL/CDC chain), and open display type for the products he builds and ships — so the one visible seam on the page is the same line that splits his career.

## Why this person
Abdul Samad has spent 4+ years keeping a stock exchange's trading systems (KATS, NDM, Trade Rectification) running inside a regulated compliance chain (SECP, PSX, NCCPL, CDC), where precision and exactness are the job — and, in parallel, builds AI agents, Next.js/MERN apps and automation for freelance clients, where the job is making something new. Almost nobody has both halves; a page that renders the ops half like a status log and the build half like an open canvas is true of him specifically and would misrepresent most other developers.

## How the page carries it out
- Hero: the name and tagline sit in open display type; directly beneath, one line reads like a system status readout in monospace — `KATS · NDM · Trade Rectification` — not a headline, a status line.
- Experience: the PSX role is set as a monospace log entry (role · duration · systems · compliance bodies) with a small status-dot in `--accent`; the Aiagentixz, Metafoic and freelance roles are set as open cards in display type — the visual break between the two happens exactly at the line between operating a system and building one.
- Skills: split into two lists that never share a column — infrastructure/ops skills (Windows Server, AD, LAN/WAN, PSX systems, IT governance/compliance) render as a monospace terminal-style list; build skills (Next.js, React, Node, MongoDB, AI agents) render as an open chip grid. The seam between the two lists is the one deliberate divider on the page.
- Projects: builder work only (AI agents, Shopify/WordPress, ad campaigns) as an open card grid in display type — this section is intentionally all in the "build" register, because these are things he made, not systems he keeps alive.
- `--accent` marks live/status signals only — the status-dot next to the PSX entry, link/focus states — and appears nowhere else, so it keeps meaning "this is live" instead of becoming decoration.
- At 390px: the ops list and build grid stop sitting side by side and stack, the ops list keeps its monospace/status styling in a single column so it still reads as a log rather than collapsing into a plain list, and the seam becomes a horizontal rule instead of a vertical divide between rail and canvas.

## Tokens
```css
:root {
  --bg: #10141a;
  --fg: #eef0ea;
  --accent: #34d399;      /* --fg on --bg = 16.1:1, --accent on --bg = 9.6:1 — both computed, both pass 4.5:1 */

  --text-xs: 0.75rem;
  --text-sm: 0.9rem;
  --text-base: 1.05rem;
  --text-lg: 1.35rem;
  --text-xl: clamp(2rem, 5vw, 3.4rem);
  --text-2xl: clamp(2.8rem, 9vw, 6.5rem);

  --space-1: 0.3rem;
  --space-2: 0.6rem;
  --space-3: 1.1rem;
  --space-4: 2rem;
  --space-5: 3.5rem;
  --space-6: 7rem;

  --measure: 47ch;
}
```
