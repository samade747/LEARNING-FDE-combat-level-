"""Run: python test_agent_surface.py"""

from __future__ import annotations

import sys

from agent_surface import cited_answer, load_corpus, retrieve, search


def main() -> int:
    errors: list[str] = []
    docs = load_corpus()

    if len(docs) < 5:
        errors.append(f"expected 5+ governed corpus docs, found {len(docs)}")

    # search returns candidates with stable_id, not the answer itself.
    hits = search("refund", docs)
    if not hits or hits[0]["stable_id"] != "POLICY-REFUND-001":
        errors.append(f"search('refund') expected POLICY-REFUND-001 hit, got {hits}")

    # retrieve by stable_id returns the full doc.
    doc = retrieve("POLICY-SHIPPING-003", docs)
    if doc is None or "5 to 7 business days" not in doc["body"]:
        errors.append(f"retrieve(POLICY-SHIPPING-003) unexpected: {doc}")

    # cited_answer for an in-corpus question: answered + correct citation.
    r1 = cited_answer("What is the refund policy for large amounts?", docs)
    if r1["status"] != "answered" or r1["citation"]["stable_id"] != "POLICY-REFUND-001":
        errors.append(f"in-corpus question should be answered with a citation, got {r1}")

    # cited_answer for an out-of-corpus question: must abstain, not invent.
    r2 = cited_answer("What is the weather forecast for tomorrow?", docs)
    if r2["status"] != "abstain":
        errors.append(f"out-of-boundary question should abstain, got {r2}")
    if "answer" in r2:
        errors.append(f"abstain response leaked an 'answer' key: {r2}")

    if errors:
        print("FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("All checks passed: search/retrieve work by stable_id, in-corpus questions are cited, "
          "out-of-boundary questions abstain instead of inventing an answer.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
