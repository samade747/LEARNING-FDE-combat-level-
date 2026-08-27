# Stub Stateless MCP Tool

This fixture demonstrates docs/ksor/02-architecture-and-tooling.md's Agent Surface (MCP) section and
Section 5's Abstention Is a Feature principle: `handle_request()` is a pure function with no session
state, and returns `{"status": "abstain"}` instead of guessing when nothing in the corpus matches.

Do not add a fallback that returns a best-guess answer when search/retrieve finds nothing — the
whole point of this fixture is that abstention is correct behavior, not a bug to work around.
