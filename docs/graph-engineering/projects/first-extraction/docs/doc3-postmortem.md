# Postmortem — INC-2091 Checkout Outage

Summary: the checkout outage on 2026-06-03 was caused by a defective Z9 rate-limiter unit sourced from
**Aria**, our long-standing Z-series supplier. This is the same defect family the supplier disclosed
on 2026-06-05.

Action items: (1) platform team lead Sana Iqbal to review the revised inspection protocol from the
supplier before the next shipment, (2) on-call runbook to reference contract AC-2024-11 directly
instead of the vendor's short name, to avoid ambiguity in future incident reports.
