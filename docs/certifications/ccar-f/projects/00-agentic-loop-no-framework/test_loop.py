"""test_loop.py — offline diagnostic tests, no API key, no network.

Each test drives ONE broken_loop function against a scenario built to expose its specific bug's
symptom, then re-runs the identical scenario against fixed_loop.agent_loop to show the corrected
behavior. FakeClient records the exact `messages` payload sent on every call, so bugs that are
invisible in the final return value (like a silently-dropped tool call) are still provable.
"""
from types import SimpleNamespace

import pytest

import broken_loop
import fixed_loop


def text_block(s):
    return SimpleNamespace(type="text", text=s)


def tool_use_block(name, input_, id_):
    return SimpleNamespace(type="tool_use", name=name, input=input_, id=id_)


class FakeClient:
    def __init__(self, scripted_responses, tool_result=None, max_calls=8):
        self._queue = list(scripted_responses)
        self.calls = 0
        self.tool_calls = 0
        self.received_messages = []  # snapshot of the `messages` kwarg sent on each call
        self.tool_result = tool_result if tool_result is not None else {"ok": True}
        self.max_calls = max_calls
        self.messages = SimpleNamespace(create=self._create)

    def _create(self, **kwargs):
        self.calls += 1
        assert self.calls <= self.max_calls, (
            f"exceeded {self.max_calls} calls without stopping — this IS the symptom under test"
        )
        self.received_messages.append(list(kwargs["messages"]))
        assert self._queue, f"FakeClient exhausted after {self.calls} calls"
        return self._queue.pop(0)

    def execute_tool(self, name, input_):
        self.tool_calls += 1
        return self.tool_result


def _weather_then_answer_script():
    return [
        SimpleNamespace(stop_reason="tool_use", content=[tool_use_block("get_weather", {"city": "Lahore"}, "t1")]),
        SimpleNamespace(stop_reason="end_turn", content=[text_block("It's sunny in Lahore.")]),
    ]


def test_bug1_missing_history_drops_the_assistant_turn():
    script = _weather_then_answer_script()

    broken_client = FakeClient(list(script))
    broken_loop.loop_bug1_missing_history(broken_client, "What's the weather in Lahore?")
    # symptom: the 2nd call's messages never include an "assistant" role entry
    assert not any(m.get("role") == "assistant" for m in broken_client.received_messages[1])

    fixed_client = FakeClient(list(script))
    fixed_loop.agent_loop(fixed_client, "What's the weather in Lahore?")
    assert any(m.get("role") == "assistant" for m in fixed_client.received_messages[1])


def test_bug2_lost_tool_result_never_reaches_the_model():
    script = _weather_then_answer_script()

    broken_client = FakeClient(list(script))
    broken_loop.loop_bug2_lost_tool_result(broken_client, "What's the weather in Lahore?")
    # symptom: the tool ran (tool_calls == 1) but no follow-up message carries its result
    assert broken_client.tool_calls == 1
    assert len(broken_client.received_messages[1]) == 2  # just [user, assistant] — result vanished

    fixed_client = FakeClient(list(script))
    fixed_loop.agent_loop(fixed_client, "What's the weather in Lahore?")
    assert len(fixed_client.received_messages[1]) == 3  # [user, assistant, tool_result]


def test_bug3_incorrect_stop_handling_drops_a_pending_tool_call():
    script = [
        SimpleNamespace(
            stop_reason="tool_use",  # the API says: still working, a tool_use is pending
            content=[text_block("Let me check that for you."), tool_use_block("get_weather", {"city": "Lahore"}, "t1")],
        ),
        SimpleNamespace(stop_reason="end_turn", content=[text_block("It's sunny in Lahore.")]),
    ]

    broken_client = FakeClient(list(script))
    result = broken_loop.loop_bug3_incorrect_stop_handling(broken_client, "Weather in Lahore?")
    assert result["final_text"] == "Let me check that for you."  # stopped on stray reasoning text
    assert broken_client.tool_calls == 0  # the tool was never actually called

    fixed_client = FakeClient(list(script))
    result = fixed_loop.agent_loop(fixed_client, "Weather in Lahore?")
    assert fixed_client.tool_calls == 1
    assert result["final_text"] == "It's sunny in Lahore."


def test_bug4_repeated_tool_calls_never_terminates():
    endless_tool_use = SimpleNamespace(
        stop_reason="tool_use", content=[tool_use_block("get_weather", {"city": "Lahore"}, "t1")]
    )

    broken_client = FakeClient([endless_tool_use] * 8, max_calls=8)
    with pytest.raises(AssertionError, match="exceeded 8 calls"):
        broken_loop.loop_bug4_repeated_tool_calls(broken_client, "Weather in Lahore?")

    fixed_client = FakeClient([endless_tool_use] * 8, max_calls=8)
    result = fixed_loop.agent_loop(fixed_client, "Weather in Lahore?")
    assert result == {"final_text": None, "error": "max turns exceeded"}
    assert fixed_client.calls == fixed_loop.MAX_TURNS  # stopped itself, well under the hard ceiling


def test_bug5_premature_termination_drops_the_second_tool_call():
    script = [
        SimpleNamespace(
            stop_reason="tool_use",
            content=[
                tool_use_block("get_weather", {"city": "Lahore"}, "t1"),
                tool_use_block("get_traffic", {"city": "Lahore"}, "t2"),
            ],
        ),
        SimpleNamespace(stop_reason="end_turn", content=[text_block("Sunny, light traffic.")]),
    ]

    broken_client = FakeClient(list(script))
    broken_loop.loop_bug5_premature_termination(broken_client, "Weather and traffic in Lahore?")
    assert broken_client.tool_calls == 1  # get_traffic silently dropped

    fixed_client = FakeClient(list(script))
    fixed_loop.agent_loop(fixed_client, "Weather and traffic in Lahore?")
    assert fixed_client.tool_calls == 2
