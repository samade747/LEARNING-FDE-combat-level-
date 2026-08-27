# P8 — Agent Surface, Hand-Built

*Practicum week P8, [`../../02-fde-practicum.md`](../../02-fde-practicum.md). **Milestone 2:** working
MCP agent surface — search, retrieve, and cited-answer over the governed corpus, knowledge boundary
enforced in application logic.*

## Files

- `corpus/*.md` — 5 tiny governed policy documents, each with `stable_id`, `authority_class`, `version`
  frontmatter (a minimal source-register shape).
- `agent_surface.py` — `search(query)` (candidates + `stable_id`, never the answer itself),
  `retrieve(stable_id)` (full document), `cited_answer(question)` (answers **only** when a governed
  source covers the question; otherwise returns `{"status": "abstain", "reason": ...}` — never invents).
- `test_agent_surface.py` — verifies search/retrieve work by `stable_id`, an in-corpus question gets a
  cited answer, and an out-of-corpus question abstains rather than being answered from the model's own
  general knowledge.

## Kaise Chalayein

```bash
cd docs/ccar-f-fde-track-b/projects/p8-agent-surface
python test_agent_surface.py
python agent_surface.py   # two example questions, one in-corpus, one not
```

## Done Jab (Self-Check)

- [x] 5 governed corpus documents with `stable_id` — `test_agent_surface.py` checks count
- [x] `search()` returns candidates by `stable_id`, not the raw answer
- [x] In-corpus question → answered with a citation
- [x] Out-of-corpus question → `abstain`, no fabricated `answer` key (this is the boundary the
      milestone actually tests — not "does the tool run", but "does it know what it doesn't know")

---
[⬅ Practicum Index](../../02-fde-practicum.md) · [⬆ Chapter Index](../../README.md)
