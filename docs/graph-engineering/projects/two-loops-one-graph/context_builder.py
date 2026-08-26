#!/usr/bin/env python3
"""Bounded subgraph retrieval for a worker task (Concept 9).

Never hands out the whole graph. Given a task string:
  1. resolve  - find entities the task mentions
  2. expand   - walk claims 1-2 hops out from those entities
  3. include  - (skipped here — no "current artifact" versions in this toy graph)
  4. prioritize - recent and non-inference claims first
  5. conflicts  - if two active claims disagree (same subject+predicate,
                  different object, neither supersedes the other), surface BOTH
  6. budget   - cap the number of claims serialized (stand-in for a token budget)
  7. stable ids - every claim keeps its id, so a checker/worker can cite it

Usage: python context_builder.py "why does test_payments_flaky fail?" --max-claims 10
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent


def load_graph():
    with open(HERE / "graph" / "entities.json", encoding="utf-8") as f:
        entities = {e["id"]: e for e in json.load(f)["entities"]}
    with open(HERE / "graph" / "claims.json", encoding="utf-8") as f:
        claims = json.load(f)["claims"]
    return entities, claims


def resolve(task: str, entities: dict) -> set[str]:
    task_lower = task.lower()
    return {eid for eid in entities if eid.replace("_", " ") in task_lower or eid in task_lower}


def expand(seed_ids: set[str], claims: list[dict], hops: int = 2) -> list[dict]:
    frontier = set(seed_ids)
    collected = []
    collected_ids = set()
    for _ in range(hops):
        next_frontier = set()
        for c in claims:
            if c["id"] in collected_ids:
                continue
            if c["subject"] in frontier or c["object"] in frontier:
                collected.append(c)
                collected_ids.add(c["id"])
                next_frontier.add(c["subject"])
                next_frontier.add(c["object"])
        frontier |= next_frontier
    return collected


def find_conflicts(claims: list[dict]) -> list[tuple]:
    by_key = {}
    conflicts = []
    for c in claims:
        key = (c["subject"], c["predicate"])
        if key in by_key:
            other = by_key[key]
            if other["object"] != c["object"] and not c.get("supersedes") and not other.get("supersedes"):
                conflicts.append((other["id"], c["id"]))
        by_key.setdefault(key, c)
    return conflicts


def build_context(task: str, max_claims: int = 10) -> dict:
    entities, claims = load_graph()
    seed = resolve(task, entities)
    subgraph = expand(seed, claims)

    # prioritize: non-inference first, then most recent
    subgraph.sort(key=lambda c: (c["source"]["kind"] == "inference", c["created"]), reverse=False)
    subgraph.sort(key=lambda c: c["created"], reverse=True)
    subgraph.sort(key=lambda c: c["source"]["kind"] == "inference")

    conflicts = find_conflicts(subgraph)
    bounded = subgraph[:max_claims]

    return {
        "task": task,
        "resolved_entities": sorted(seed),
        "claims": [
            {"id": c["id"], "triple": [c["subject"], c["predicate"], c["object"]], "source": c["source"]["kind"]}
            for c in bounded
        ],
        "conflicts": [{"claim_ids": list(pair), "note": "same subject+predicate, different object, neither supersedes the other"} for pair in conflicts],
        "truncated": len(subgraph) > max_claims,
    }


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: python context_builder.py \"<task text>\" [--max-claims N]", file=sys.stderr)
        return 2
    task = argv[0]
    max_claims = 10
    if "--max-claims" in argv:
        max_claims = int(argv[argv.index("--max-claims") + 1])

    ctx = build_context(task, max_claims)
    print(json.dumps(ctx, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
