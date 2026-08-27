# P4-P5 — Fumadocs I/II Scaffold

This project's one job: prove every governed document has full provenance (source, owner, version,
effective_period, authority_kind) before it reaches the human-readable surface.

Do not add a document to `knowledge/` without all six frontmatter fields — `build.js` refuses to build
otherwise, on purpose. Do not weaken that check to make a build "succeed."
