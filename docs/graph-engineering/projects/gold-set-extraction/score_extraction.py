#!/usr/bin/env python3
"""Score a predicted extraction against the hand-labeled gold set.

Usage: python score_extraction.py predicted_v1.json
Reports: relation precision/recall (exact subject/predicate/object match),
entity recall, and a schema-valid-rate check (every relation's subject/object
must be a declared entity in the SAME predicted file).
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent


def rel_key(r: dict) -> tuple[str, str, str]:
    return (r["subject"], r["predicate"], r["object"])


def main(path: str) -> int:
    with open(HERE / "gold_labels.json", encoding="utf-8") as f:
        gold = json.load(f)
    with open(path, encoding="utf-8") as f:
        pred = json.load(f)

    gold_entities = {e["name"] for e in gold["entities"]}
    pred_entities = {e["name"] for e in pred["entities"]}
    gold_rels = {rel_key(r) for r in gold["relations"]}
    pred_rels = {rel_key(r) for r in pred["relations"]}

    tp = gold_rels & pred_rels
    fp = pred_rels - gold_rels
    fn = gold_rels - pred_rels

    precision = len(tp) / len(pred_rels) if pred_rels else 0.0
    recall = len(tp) / len(gold_rels) if gold_rels else 0.0
    entity_recall = len(gold_entities & pred_entities) / len(gold_entities) if gold_entities else 0.0

    schema_valid = 0
    for r in pred["relations"]:
        if r["subject"] in pred_entities and r["object"] in pred_entities:
            schema_valid += 1
    schema_valid_rate = schema_valid / len(pred["relations"]) if pred["relations"] else 1.0

    print(f"=== {path} ===")
    print(f"Relation precision: {precision:.2f}  ({len(tp)} correct / {len(pred_rels)} predicted)")
    print(f"Relation recall:    {recall:.2f}  ({len(tp)} correct / {len(gold_rels)} in gold)")
    print(f"Entity recall:      {entity_recall:.2f}  ({len(gold_entities & pred_entities)} / {len(gold_entities)})")
    print(f"Schema-valid rate:  {schema_valid_rate:.2f}  ({schema_valid} / {len(pred['relations'])} relations reference declared entities)")

    if fp:
        print(f"\nFalse positives ({len(fp)}):")
        for r in sorted(fp):
            print(f"  - {r}")
    if fn:
        print(f"\nMissed (false negatives) ({len(fn)}):")
        for r in sorted(fn):
            print(f"  - {r}")

    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python score_extraction.py <predicted.json>", file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
