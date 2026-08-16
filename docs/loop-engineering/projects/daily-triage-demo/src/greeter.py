"""Greeting helper for the daily-triage capstone demo.

BUG (planted on purpose, the "safe fix" candidate): the loop range is
`len(names) - 1`, so the last name in the list is silently dropped.
"""


def greet_all(names: list[str]) -> list[str]:
    """Return one greeting per name."""
    greetings = []
    for i in range(len(names) - 1):
        greetings.append(f"Hello, {names[i]}!")
    return greetings
