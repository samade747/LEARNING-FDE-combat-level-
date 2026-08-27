# KSoR Project 1 — Corpus-to-Site Skeleton

**Concept:** Section 8 (Project Structure), Section 11 (Governance Model) · **Time:** 20-30 min ·
**Difficulty:** Easy

Ek chhota fixture KSoR (`sample-refund-ksor`, ek online-store ki refund policy govern karti hai) —
`docs/ksor/02-architecture-and-tooling.md` ke project-structure convention (`knowledge/`,
`instance.md`) ko demonstrate karta hai, aur ek validator jo confirm karta hai har authority-class
knowledge file governance frontmatter (`stable_id`, `owner`, `version`, `authority_class`) carry
karti hai.

## Files

- `instance.md` — is fixture KSoR ki identity/maqsad
- `knowledge/about.md` — orientation content (koi rule cite nahi karta)
- `knowledge/policies/refund-window.md` — authority content, ek policy rule
- `knowledge/procedures/refund-escalation.md` — authority content, ek procedure jo policy ko cite karti hai
- `validate_corpus.py` — structure + frontmatter validator

## Kaise Chalayein

```bash
python validate_corpus.py
```

## Trip Karo (jaan-boojh kar break karo)

Kisi bhi `knowledge/**/*.md` file se `owner:` line hata do, phir dobara `python validate_corpus.py`
chalao — expect karo failure clearly bataye kaunsi file, kaunsa field missing hai.

## Done Jab (Self-Check)

- [ ] `validate_corpus.py` clean pass karta hai (koi missing field, koi duplicate `stable_id` nahi)
- [ ] Ek field jaan-boojh kar hata kar dekha — validator ne exact file + field name bataya
- [ ] Farq bata sako `about.md` (orientation) aur `refund-window.md` (authority) mein — kis test
      (citation/change/dispute) se authority content decide hota hai (docs/ecosystem-designing-the-vertical-sor
      ka "Two Kinds of Content" section dekho agar available ho)

---
[⬆ KSoR Practice Projects](../README.md) · [⬆ KSoR Index](../../README.md)
