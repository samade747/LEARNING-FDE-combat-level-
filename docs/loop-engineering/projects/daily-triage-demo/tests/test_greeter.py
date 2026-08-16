import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from greeter import greet_all


def test_greet_all_includes_the_last_name():
    # The planted bug currently drops "Bilal" — this is the CI failure to triage.
    assert greet_all(["Ana", "Bilal"]) == ["Hello, Ana!", "Hello, Bilal!"]


def test_greet_all_empty_list():
    assert greet_all([]) == []


def test_greet_all_single_name():
    assert greet_all(["Zara"]) == ["Hello, Zara!"]
