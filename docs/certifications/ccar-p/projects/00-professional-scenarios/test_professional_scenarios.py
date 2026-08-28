"""test_professional_scenarios.py — offline verification for all 3 CCAR-P sample questions."""
from least_privilege import enforce_least_privilege
from prompt_ordering import build_cached_prompt, is_cache_effective
from rag_diagnostics import diagnose_rag_regression


def test_sample1_support_staff_loses_refund_and_delete_tools():
    result = enforce_least_privilege(
        "support_staff", {"read_ticket", "draft_reply", "issue_refund", "delete_account"}
    )
    assert result["final_tools"] == {"read_ticket", "draft_reply"}
    assert result["removed_tools"] == {"issue_refund", "delete_account"}


def test_sample1_account_manager_keeps_refund_but_not_delete():
    result = enforce_least_privilege(
        "account_manager", {"read_ticket", "draft_reply", "issue_refund", "delete_account"}
    )
    assert result["final_tools"] == {"read_ticket", "draft_reply", "issue_refund"}
    assert "delete_account" in result["removed_tools"]


def test_sample2_static_content_ordered_before_dynamic_and_marked_cacheable():
    prompt = build_cached_prompt(
        static_system_prompt="You are a support agent...",
        static_policy="Refund policy: ...",
        dynamic_user_message="My order #123 hasn't arrived.",
    )
    blocks = prompt["blocks"]
    assert blocks[0]["cache_control"] is not None
    assert blocks[1]["cache_control"] is not None
    assert blocks[-1]["cache_control"] is None
    assert is_cache_effective(blocks) is True


def test_sample2_dynamic_content_before_static_breaks_cache_effectiveness():
    broken_order = [
        {"content": "user message", "cache_control": None},
        {"content": "static system prompt", "cache_control": {"type": "ephemeral"}},
    ]
    assert is_cache_effective(broken_order) is False


def test_sample3_document_refresh_with_stable_model_points_at_retrieval():
    result = diagnose_rag_regression(
        trigger_event="document_refresh", model_version_changed=False, latency_changed=False
    )
    assert result["most_likely_cause"] == "retrieval_or_indexing"


def test_sample3_unrelated_trigger_does_not_confidently_blame_retrieval():
    result = diagnose_rag_regression(
        trigger_event="unrelated_deploy", model_version_changed=True, latency_changed=True
    )
    assert result["most_likely_cause"] == "insufficient_evidence"
