"""Sample Question 1 (Domain 3 — Integration): least privilege, applied to a real agent config.

Official guide's own scenario: a customer-support agent can read tickets, draft replies, issue
refunds, and delete accounts. Support staff should only read and draft. The correct fix REMOVES the
unneeded tools entirely — logging or confirmation prompts are compensating controls, not privilege
removal, and a bigger model doesn't change the authorization scope at all.
"""
from __future__ import annotations

ALL_TOOLS = {"read_ticket", "draft_reply", "issue_refund", "delete_account"}

ROLE_REQUIRED_CAPABILITIES = {
    "support_staff": {"read_ticket", "draft_reply"},
    "account_manager": {"read_ticket", "draft_reply", "issue_refund"},
}


def enforce_least_privilege(role: str, configured_tools: set[str]) -> dict:
    """Removes any tool not required by the role — this IS the fix, not a detective control
    layered on top of an over-permissioned config."""
    required = ROLE_REQUIRED_CAPABILITIES.get(role, set())
    removed = configured_tools - required
    return {
        "role": role,
        "final_tools": configured_tools & required,
        "removed_tools": removed,
    }
