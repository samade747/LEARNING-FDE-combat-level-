# KSoR Project 3 — Governance/Provenance Record

**Concept:** Section 11 (Governance Model) · **Time:** 20-30 min · **Difficulty:** Easy-Medium

Ek sample source-register (4 entries: 3 "approved" + 1 jaan-boojh kar incomplete "draft") aur ek
validator jo `docs/ksor/03-governance-and-ai-native-role.md` ka **Source → Draft → Review → Approved
→ Authoritative** pipeline enforce karta hai: sirf "approved" entries citable hain, aur "approved"
entries ke paas poori governance metadata (`owner`, `effective_period`, `source_commit`) honi
chahiye.

## Files

- `source_register.json` — 4 entries, 4th (`draft-loyalty-policy-001`) jaan-boojh kar incomplete
  draft hai (empty owner/effective_period/source_commit)
- `validate_register.py` — duplicate-id check, approved-entries-must-be-complete check,
  draft-never-citable check

## Kaise Chalayein

```bash
python validate_register.py
```

## Trip Karo (jaan-boojh kar break karo)

`source_register.json` mein 4th entry ka `"review_state": "draft"` badal kar `"approved"` kar do
(fields empty hi rehne do). Dobara `python validate_register.py` chalao — expect karo failure
clearly bataye: `owner`, `effective_period`, `source_commit` teeno missing hain, aur entry citable
set mein leak ho gayi.

## Done Jab (Self-Check)

- [ ] `validate_register.py` clean pass karta hai as-is (3 citable, 1 draft correctly excluded)
- [ ] Draft ko approved mark kar ke dekha — validator ne teeno missing fields + citable-leak pakri
- [ ] Bata sako yeh kyun zaroori hai: "KSoR architecture deta hai, governance policy khud
      organization ki zimmedari rehti hai" — is validator ka scope kya hai, kya nahi (docs/ksor/03
      dekho)

---
[⬆ KSoR Practice Projects](../README.md) · [⬆ KSoR Index](../../README.md)
