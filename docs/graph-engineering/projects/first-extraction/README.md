# Graph Project 3 — First Extraction

**Concept:** 6 (Extraction: schema is the training data) · **Time:** 45-60 min · **Difficulty:** Medium

Run a schema-constrained prompt over 3 related documents, validate every reply, and meet your own
duplicates: the same real vendor named 3 different ways across the 3 documents.

## Files

- `docs/doc1-incident-report.md`, `docs/doc2-vendor-contract-note.md`, `docs/doc3-postmortem.md` — 3
  short, related documents (fake data). The same supplier appears as "Aria Components Ltd" (doc1),
  "ACL" / "Aria Components Ltd." (doc2), and "Aria" (doc3) — deliberately, so resolution has something
  real to do later (Project 5).
- `entity_schema.json` — the shape every extraction must match (mirrors the Cookbook's Pydantic classes)
- `extract-prompt.md` — the exact prompt template to run headlessly
- `reference-extracted-doc{1,2,3}.json` — a worked reference extraction for all 3 docs (so you have
  something to compare your own run against, and so the validator has real fixtures to test)
- `validate_extraction.py` — schema validator (Python; `jq` mentioned in the book, not installed on
  this machine, so this is the portable equivalent) + a cheap cross-file surface-form-overlap hint

## Setup

Koi extra install nahi chahiye — Python 3 aur Claude Code ya OpenCode (headless mode).

## Test the Validator (No API Call Needed)

```bash
cd docs/graph-engineering/projects/first-extraction
python validate_extraction.py reference-extracted-doc1.json reference-extracted-doc2.json reference-extracted-doc3.json
```

Expect: all 3 files `schema-valid`, exit 0, and the overlap-hint section flags `Aria Components Ltd`
↔ `Aria` as a likely same-entity candidate (the token-overlap heuristic is cheap on purpose — it won't
catch `ACL`, that's why resolution in Project 5 needs a reasoning model, not string matching).

## Run Your Own Extraction

```bash
claude -p "$(cat extract-prompt.md | sed 's/{DOC_PATH}/docs\/doc1-incident-report.md/')" > my-extracted-doc1.json
# repeat for doc2 and doc3
python validate_extraction.py my-extracted-doc1.json my-extracted-doc2.json my-extracted-doc3.json
```

(OpenCode: `opencode run "..."` with the same prompt text.)

## Done Jab (Self-Check)

- [ ] Sab 3 apni extractions schema-valid JSON return karti hain (`validate_extraction.py` exit 0)
- [ ] Aap kam se kam 1 entity naam sakte ho jo 2+ surface forms ke under aayi (yahan: the vendor —
      "Aria Components Ltd" / "ACL" / "Aria")
- [ ] Apni extraction ko `reference-extracted-doc*.json` se compare kiya — kya missed ya extra tha?

---
[⬆ Practice Projects Index](../../08-practice-projects.md)
