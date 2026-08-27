# Governance/Provenance Record

This fixture demonstrates docs/ksor/03-governance-and-ai-native-role.md's Governance Model
pipeline: Source -> Draft -> Review -> Approved -> Authoritative KSoR. `validate_register.py`
enforces that only "approved" entries are citable, and that "approved" entries carry full
governance metadata (owner, effective_period, source_commit).

Do not mark `draft-loyalty-policy-001` as "approved" in `source_register.json` to make it citable
— that entry is a deliberate bad example (empty owner/effective_period/source_commit) proving the
validator catches an incomplete approval.
