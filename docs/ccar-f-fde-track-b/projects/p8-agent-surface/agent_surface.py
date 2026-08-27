"""P8 scaffold: search, retrieve, and cited-answer over a tiny governed corpus,
with the knowledge boundary enforced in application logic (not left to the
model's discretion) — a question the corpus does not cover gets an explicit
abstain, never an invented answer.
"""

from __future__ import annotations

import os
import re

CORPUS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "corpus")


def _parse(path: str) -> dict:
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    fm_text, body = m.group(1), m.group(2).strip()
    fm = {}
    for line in fm_text.splitlines():
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    return {**fm, "body": body}


def load_corpus() -> list[dict]:
    docs = []
    for fname in sorted(os.listdir(CORPUS_DIR)):
        if fname.endswith(".md"):
            docs.append(_parse(os.path.join(CORPUS_DIR, fname)))
    return docs


def search(query: str, docs: list[dict] | None = None) -> list[dict]:
    """Search returns candidate docs with their stable_id — never the answer
    itself, only what a Worker would then retrieve and cite."""
    docs = docs if docs is not None else load_corpus()
    q = query.lower()
    hits = []
    for d in docs:
        if q in d["body"].lower() or q in d["id"]:
            hits.append({"id": d["id"], "stable_id": d["stable_id"], "snippet": d["body"][:80]})
    return hits


def retrieve(stable_id: str, docs: list[dict] | None = None) -> dict | None:
    docs = docs if docs is not None else load_corpus()
    for d in docs:
        if d["stable_id"] == stable_id:
            return d
    return None


# A tiny fixed keyword->stable_id map stands in for a real embedding search.
# This is deliberately narrow: it is what makes the "outside the boundary"
# case in cited_answer testable and honest, instead of a model quietly
# improvising an answer for anything that sounds plausible.
_KEYWORD_MAP = {
    "refund": "POLICY-REFUND-001",
    "escalat": "POLICY-ESCALATION-002",
    "ship": "POLICY-SHIPPING-003",
    "duplicate": "POLICY-DUPLICATE-004",
    "disclos": "POLICY-DISCLOSURE-005",
    "ai": "POLICY-DISCLOSURE-005",
}


def cited_answer(question: str, docs: list[dict] | None = None) -> dict:
    """Answer a question ONLY if a governed source covers it. Outside the
    boundary -> abstain, with a reason, never a guess."""
    docs = docs if docs is not None else load_corpus()
    q = question.lower()
    matched_stable_id = None
    for kw, stable_id in _KEYWORD_MAP.items():
        if kw in q:
            matched_stable_id = stable_id
            break

    if matched_stable_id is None:
        return {
            "status": "abstain",
            "reason": "no governed source in this corpus covers this question",
        }

    doc = retrieve(matched_stable_id, docs)
    return {
        "status": "answered",
        "answer": doc["body"],
        "citation": {"stable_id": doc["stable_id"], "id": doc["id"]},
    }


if __name__ == "__main__":
    print(cited_answer("What is the refund policy for large amounts?"))
    print(cited_answer("What is the weather forecast for tomorrow?"))
