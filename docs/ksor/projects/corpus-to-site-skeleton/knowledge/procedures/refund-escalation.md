---
stable_id: procedure-refund-escalation-001
owner: fixture-team
version: 1.3
authority_class: authority
effective_period: 2026-01-01/open
---

# Refund Escalation Procedure

When a refund request arrives after the 30-day window (`policy-refund-window-001`), the Worker must
not approve it directly. It prepares a summary (order id, days over window, stated reason) and routes
it to a named store manager for approval. The Worker never approves an out-of-window refund itself.
