"""The checker for Project 4. A command decides "done" — never the agent."""

from discount import apply_discount


def test_twenty_percent_off():
    # $100 at 20% off should be $80.00 — the planted bug currently returns $98.00
    assert apply_discount([100.0], 20) == [80.0]


def test_no_discount_is_a_no_op():
    assert apply_discount([50.0, 10.0], 0) == [50.0, 10.0]


def test_multiple_prices():
    assert apply_discount([10.0, 20.0, 30.0], 50) == [5.0, 10.0, 15.0]
