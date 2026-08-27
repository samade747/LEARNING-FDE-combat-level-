"""A small, self-contained 'agent' that the eval_runner exercises. Mirrors
P8's cited_answer, plus the class this scaffold is really here to test: a
question that needs BOTH a governed rule AND a live operational fact — the
kind of question that fails silently if you only ever test the two halves
separately.
"""

from __future__ import annotations

GOVERNED_RULES = {
    "refund-threshold": {
        "stable_id": "POLICY-REFUND-001",
        "text": "Refunds above $500 require supervisor approval.",
        "threshold": 500,
    },
}

# Stands in for a LIVE operational query (an order-status API, a database
# call) — not part of the governed corpus, and not cached alongside it,
# because operational state changes independently of policy.
OPERATIONAL_FACTS = {
    "order-101": {"amount": 750},
    "order-102": {"amount": 200},
}


def answer(case: dict) -> dict:
    kind = case["kind"]

    if kind == "citation":
        # Answerable purely from the governed corpus.
        if "refund" in case["question"].lower():
            rule = GOVERNED_RULES["refund-threshold"]
            return {"status": "answered", "citation": rule["stable_id"], "text": rule["text"]}
        return {"status": "abstain", "reason": "no matching governed source"}

    if kind == "rule_plus_fact":
        # Needs the governed threshold AND a live operational fact together.
        order_id = case.get("order_id")
        fact = OPERATIONAL_FACTS.get(order_id)
        if fact is None:
            return {"status": "abstain", "reason": f"no operational record for {order_id}"}
        rule = GOVERNED_RULES["refund-threshold"]
        needs_approval = fact["amount"] > rule["threshold"]
        return {
            "status": "answered",
            "citation": rule["stable_id"],
            "needs_approval": needs_approval,
            "amount": fact["amount"],
        }

    if kind == "outside_boundary":
        # Deliberately outside anything this agent's corpus or operational
        # facts cover — must abstain, never guess.
        return {"status": "abstain", "reason": "outside governed knowledge boundary"}

    raise ValueError(f"unknown case kind: {kind}")
