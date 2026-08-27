"""Exercises mcp_tool.handle_request with 4 scripted calls, verifying: search hits an authority
doc, search abstains on an out-of-corpus query, retrieve returns full text by stable_id, and
retrieve abstains on an unknown stable_id. No live server/network needed.

Run: python test_client.py   (exits non-zero and prints failures if anything is wrong)
"""
from __future__ import annotations

import sys

from mcp_tool import handle_request


def main() -> int:
    errors: list[str] = []

    r1 = handle_request({"tool": "search", "query": "refund"})
    if r1.get("status") != "ok" or not r1.get("hits"):
        errors.append(f"search('refund') expected ok+hits, got {r1}")
    elif not any(h["stable_id"] == "policy-refund-window-001" for h in r1["hits"]):
        errors.append(f"search('refund') did not hit policy-refund-window-001: {r1}")

    r2 = handle_request({"tool": "search", "query": "warranty extension for laptops"})
    if r2.get("status") != "abstain":
        errors.append(f"search on out-of-corpus query should abstain, got {r2}")

    r3 = handle_request({"tool": "retrieve", "stable_id": "procedure-refund-escalation-001"})
    if r3.get("status") != "ok" or "manager" not in r3.get("text", "").lower():
        errors.append(f"retrieve(procedure-refund-escalation-001) unexpected result: {r3}")

    r4 = handle_request({"tool": "retrieve", "stable_id": "does-not-exist-001"})
    if r4.get("status") != "abstain":
        errors.append(f"retrieve on unknown stable_id should abstain, got {r4}")

    # Statelessness check: two independent calls for the same query must return identical results,
    # proving no call mutates shared state that the next call could see.
    r5 = handle_request({"tool": "search", "query": "refund"})
    if r5 != r1:
        errors.append(f"two identical calls returned different results — handler is not stateless: {r1} vs {r5}")

    if errors:
        print("FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("All 5 checks passed: search hits + abstains correctly, retrieve hits + abstains "
          "correctly, repeated calls are identical (stateless).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
