"""Apply a percentage discount to a list of prices.

BUG (planted on purpose for Project 4 — "A Fix Loop With a Real Checker"):
the discount is divided by 1000 instead of 100, so a "20% off" request only
takes 2% off. Real bug shape: a magic number a reviewer has to actually
compute, not a typo a linter would catch.
"""


def apply_discount(prices: list[float], discount_percent: float) -> list[float]:
    """Apply discount_percent off each price, rounded to 2 decimals."""
    return [round(p - p * discount_percent / 1000, 2) for p in prices]
