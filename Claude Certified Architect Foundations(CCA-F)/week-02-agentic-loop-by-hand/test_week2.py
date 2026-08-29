"""Week 2 offline tests — stop_reason classifier + the by-hand loop. No API key, no network.

Run:  pytest week-02-agentic-loop-by-hand/test_week2.py -v
"""
from __future__ import annotations

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)                       # for by_hand_loop
sys.path.insert(0, os.path.dirname(_HERE))      # CCA-F root, for lib.sdk_parser

from lib.sdk_parser import classify_stop_reason, is_tool_turn, next_step, text_is_final  # noqa: E402
from by_hand_loop import FakeClient, agent_loop  # noqa: E402


def test_end_turn_is_final():
    assert classify_stop_reason("end_turn") == "final"
    assert text_is_final("end_turn") is True
    assert is_tool_turn("end_turn") is False


def test_tool_use_calls_tools():
    assert classify_stop_reason("tool_use") == "call_tools"
    assert is_tool_turn("tool_use") is True
    assert text_is_final("tool_use") is False  # a turn can have prose AND a pending tool call


def test_max_tokens_is_retry_not_parse():
    assert classify_stop_reason("max_tokens") == "retry_truncated"


def test_unknown_and_none():
    assert classify_stop_reason("something_new") == "unknown"
    assert classify_stop_reason(None) == "unknown"


def test_next_step_from_dict_and_object():
    assert next_step({"stop_reason": "tool_use"}) == "call_tools"

    class R:
        stop_reason = "end_turn"

    assert next_step(R()) == "final"


def test_loop_handles_parallel_tools_and_end_turn():
    result = agent_loop(FakeClient(), "Compare the weather in Lahore and Karachi.")
    assert result["turns"] == 3
    assert "6 degree difference" in result["final_text"]
