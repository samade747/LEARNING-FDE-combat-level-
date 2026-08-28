# P4-P5 — Fumadocs I/II: Corpus to Site

*Practicum weeks P4 ("Fumadocs I: Corpus to Site") + P5 ("Fumadocs II: Structure and Deploy"),
[`../../02-fde-practicum.md`](../../02-fde-practicum.md). Milestone 1 target: live human surface,
5+ governed documents with provenance.*

**Scope:** this is a **local, zero-dependency** stand-in for the real Next.js+Fumadocs human
projection — no `npm install`, no live deployment. It exists to make the provenance discipline (the
part P4/P5 actually test) runnable and checkable in seconds. See "Real Fumadocs" below for the actual
production path.

## Files

- `knowledge/*.md` — 5 governed documents (outcome contracts, three-bin sort, source hierarchy,
  authority-vs-orientation, thin-vs-thick), each with a provenance frontmatter block: `title`,
  `source`, `owner`, `version`, `effective_period`, `authority_kind`.
- `build.js` — zero-dependency Node build. Parses every doc's frontmatter, **fails the build** if any
  required provenance field is missing or if fewer than 5 documents exist (Milestone 1's own bar),
  then renders `static/index.html` (nav) + one page per document.

## Kaise Chalayein

```bash
cd docs/ccar-f-fde-track-b/projects/p4-p5-fumadocs-corpus-to-site
node build.js
```
Opens/serves as plain static HTML — e.g. `python -m http.server --directory static 8000`, then visit
`http://localhost:8000`.

**Break it on purpose (P4's own lesson):** remove one frontmatter field from any `knowledge/*.md` file,
re-run `node build.js`, confirm it fails with a named missing field — then put the field back.

## Done Jab (Self-Check)

- [x] 5 governed documents, each with full 6-field provenance — `build.js` enforces this structurally
- [x] `node build.js` succeeds and produces one static page per document + a nav index
- [ ] You ran the "break it on purpose" step above and saw the named failure

## Real Fumadocs (For the Actual Practicum Deliverable)

This scaffold proves the provenance discipline; it is not a Fumadocs site. **2026-08-29 update:**
`@panaversity/ksor` has shipped `ksor init`/`ksor build` since v0.0.41 (checked against its own
`docs/status.md`, live on GitHub) — per this syllabus's own rule ("use shipped `ksor` commands where
they exist; otherwise build the relevant surface directly"), that is now the real P4-P5 path, not a
generic `create-fumadocs-app` scaffold:

```bash
# requires Node.js 24+
npx @panaversity/ksor@latest init my-knowledge-sor
cd my-knowledge-sor && npm install && npm run dev   # site live at localhost:3000, hot-reloads on edit

# then migrate knowledge/*.md into the generated knowledge/ directory,
# keeping the same 6-field provenance frontmatter this scaffold enforces
ksor build   # validates the whole record + generates indexes; exit 1 on any error, repo untouched
```

`ksor build` is exactly this scaffold's `build.js`, for real: it validates provenance/governance
structurally and refuses to produce output on a bad record. Milestone 1 ("live human surface, 5+
governed documents") is this `npm run dev` site, not the `static/` folder above.

---
[⬅ Practicum Index](../../02-fde-practicum.md) · [⬆ Chapter Index](../../README.md)
