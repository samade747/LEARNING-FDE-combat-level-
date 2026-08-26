"""Offline verification for Exercise 1 — no ANTHROPIC_API_KEY, no network, no cost.

A FakeClient plays back scripted Messages-API-shaped responses so agent_loop()'s control flow
(stop_reason handling, the prerequisite hook, multi-tool-call turns, escalation) is exercised
exactly as it would be against the real API — anthropic's real Message objects expose the same
`.content` / `.stop_reason` shape agent.py reads.
"""
from types import SimpleNamespace

from agent import agent_loop


def text_block(s):
    return SimpleNamespace(type="text", text=s)


def tool_use_block(name, input_, id_):
    return SimpleNamespace(type="tool_use", name=name, input=input_, id=id_)


class FakeClient:
    """Pops one scripted response per call; fails loudly if the loop calls more than scripted
    (that would mean agent_loop kept looping past where the test expected it to stop)."""

    def __init__(self, scripted_responses):
        self._queue = list(scripted_responses)
        self.calls = 0
        self.messages = SimpleNamespace(create=self._create)

    def _create(self, **kwargs):
        self.calls += 1
        assert self._queue, f"FakeClient exhausted after {self.calls} calls — loop kept going unexpectedly"
        return self._queue.pop(0)


def test_hook_blocks_unverified_order_touch_and_escalates():
    client = FakeClient([
        SimpleNamespace(
            stop_reason="tool_use",
            content=[tool_use_block("process_refund", {"customer_id": "cust_1", "order_id": "ord_100", "amount": 10}, "t1")],
        ),
        SimpleNamespace(stop_reason="end_turn", content=[text_block("This needs a human to review.")]),
    ])
    result = agent_loop(client, "Refund my order please.")
    assert result["escalated"] is True
    assert result["final_text"] == "This needs a human to review."
    assert client.calls == 2


def test_verified_customer_can_touch_orders_and_multi_tool_turn_works():
    client = FakeClient([
        SimpleNamespace(
            stop_reason="tool_use",
            content=[tool_use_block("get_customer", {"name": "Amina Raza"}, "t1")],
        ),
        SimpleNamespace(
            stop_reason="tool_use",
            content=[
                tool_use_block("lookup_order", {"customer_id": "cust_1", "order_id": "ord_100"}, "t2"),
                tool_use_block("process_refund", {"customer_id": "cust_1", "order_id": "ord_100", "amount": 10}, "t3"),
            ],
        ),
        SimpleNamespace(stop_reason="end_turn", content=[text_block("Refunded $10.")]),
    ])
    state = {}
    result = agent_loop(client, "I'm Amina Raza, refund $10 on ord_100.", session_state=state)
    assert result["escalated"] is False
    assert result["final_text"] == "Refunded $10."
    assert state["verified_customer_id"] == "cust_1"
    assert client.calls == 3


def test_refund_over_threshold_escalates_even_when_verified():
    client = FakeClient([
        SimpleNamespace(stop_reason="tool_use", content=[tool_use_block("get_customer", {"name": "Bilal Khan"}, "t1")]),
        SimpleNamespace(
            stop_reason="tool_use",
            content=[tool_use_block("process_refund", {"customer_id": "cust_2", "order_id": "ord_200", "amount": 600}, "t2")],
        ),
        SimpleNamespace(stop_reason="end_turn", content=[text_block("Escalated to a human — amount above threshold.")]),
    ])
    result = agent_loop(client, "I'm Bilal Khan, refund $600 on ord_200.")
    assert result["escalated"] is True


def test_bad_tool_input_returns_structured_error_not_a_crash():
    client = FakeClient([
        SimpleNamespace(stop_reason="tool_use", content=[tool_use_block("get_customer", {"name": "Nobody"}, "t1")]),
        SimpleNamespace(stop_reason="end_turn", content=[text_block("I could not find that customer.")]),
    ])
    result = agent_loop(client, "I'm Nobody, look me up.")
    assert result["final_text"] == "I could not find that customer."
