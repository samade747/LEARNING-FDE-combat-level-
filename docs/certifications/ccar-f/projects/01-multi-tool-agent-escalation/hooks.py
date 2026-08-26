"""Exercise 1, step 4 — a programmatic hook that enforces a business rule Claude cannot be
trusted to always remember: verify the customer BEFORE touching orders, and never let the model
autonomously refund above a threshold.

This runs BEFORE the tool executes (a PreToolUse-style gate), not as a prompt instruction — the
CCAR-F guide's own Q1 sample question (see 03-how-to-prepare-and-sample-questions.md) is this
exact scenario: a prompt-only rule fails ~12% of the time in production; a programmatic gate
does not.
"""
from __future__ import annotations

REFUND_ESCALATION_THRESHOLD = 500.00

ORDER_TOOLS = {"lookup_order", "process_refund", "update_shipping_address"}


class Escalate(Exception):
    """Raised by a hook to redirect the turn to a human instead of executing the tool."""

    def __init__(self, reason: str):
        self.reason = reason
        super().__init__(reason)


def enforce_prerequisites(tool_name: str, tool_input: dict, session_state: dict) -> None:
    """Blocks order-touching tools until get_customer has verified a customer_id this session."""
    if tool_name in ORDER_TOOLS and not session_state.get("verified_customer_id"):
        raise Escalate(
            "Blocked: no verified customer_id yet. get_customer must succeed before "
            f"'{tool_name}' can run. Escalating to customer-verification workflow."
        )

    if tool_name == "process_refund":
        amount = tool_input.get("amount", 0)
        if amount > REFUND_ESCALATION_THRESHOLD:
            raise Escalate(
                f"Blocked: refund amount {amount} exceeds the {REFUND_ESCALATION_THRESHOLD} "
                "auto-approval threshold. Escalating to a human for manual approval."
            )


def record_verification(tool_name: str, tool_result: dict, session_state: dict) -> None:
    """A PostToolUse-style hook: once get_customer succeeds, remember the verified id."""
    if tool_name == "get_customer" and "customer_id" in tool_result:
        session_state["verified_customer_id"] = tool_result["customer_id"]
