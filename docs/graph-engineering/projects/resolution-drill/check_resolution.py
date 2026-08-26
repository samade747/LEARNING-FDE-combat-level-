#!/usr/bin/env python3
"""Score a proposed entity-resolution clustering against the answer key.

Usage: python check_resolution.py clusters.json
Exit 0 = all real duplicates merged AND the trap kept apart. Exit 1 = otherwise.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent


def form_to_cluster_map(clusters: list[dict]) -> dict[str, int]:
    mapping = {}
    for idx, c in enumerate(clusters):
        for fid in c["form_ids"]:
            mapping[fid] = idx
    return mapping


def main(path: str) -> int:
    with open(path, encoding="utf-8") as f:
        proposed = json.load(f)["clusters"]
    with open(HERE / "expected_clusters.json", encoding="utf-8") as f:
        expected = json.load(f)["clusters"]

    proposed_map = form_to_cluster_map(proposed)
    errors = []

    # 1. Every real multi-form entity must be fully merged into one proposed cluster.
    for exp in expected:
        if len(exp["form_ids"]) < 2:
            continue  # the trap singles — checked separately below
        proposed_clusters_used = {proposed_map.get(fid) for fid in exp["form_ids"]}
        if None in proposed_clusters_used:
            missing = [fid for fid in exp["form_ids"] if proposed_map.get(fid) is None]
            errors.append(f"MISSED MERGE: '{exp['canonical']}' - form(s) {missing} not assigned to any cluster")
        elif len(proposed_clusters_used) > 1:
            errors.append(f"MISSED MERGE: '{exp['canonical']}' - forms {exp['form_ids']} landed in {len(proposed_clusters_used)} different clusters instead of 1")

    # 2. The trap: sf19 and sf20 are different people. They must NOT share a cluster.
    trap_ids = [c["form_ids"][0] for c in expected if c["canonical"].startswith("J. Patel")]
    trap_clusters = {proposed_map.get(fid) for fid in trap_ids}
    if None in trap_clusters:
        errors.append(f"TRAP: one of {trap_ids} was not assigned to any cluster")
    elif len(trap_clusters) == 1:
        errors.append(f"FALSE MERGE (the trap): {trap_ids} were merged into the same cluster, but they are 2 different people who happen to share a printed name")

    print(f"Checked {len(proposed)} proposed clusters against {len(expected)} expected entities.")
    if errors:
        print(f"\n{len(errors)} ISSUE(S):")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("Real duplicates merged, the trap kept apart. Resolution is additive and correct.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python check_resolution.py <clusters.json>", file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
