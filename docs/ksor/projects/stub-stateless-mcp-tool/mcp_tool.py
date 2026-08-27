"""Stub Stateless MCP Tool — demonstrates docs/ksor/02-architecture-and-tooling.md's Agent Surface
(MCP) section and Section 5's Abstention Is a Feature principle, without a real MCP SDK.

Each call to handle_request() is a pure function: it reloads the corpus from disk, takes no session
id, and keeps no state between calls (matches "stateless MCP core" language used across this repo's
certifications/CCAR-F Track B syllabus notes). Two tool shapes: 'search' (keyword match over
authority-class documents only) and 'retrieve' (exact stable_id lookup). Neither ever falls back to
a guess: no match -> {"status": "abstain"}, never a fabricated answer.
"""
from __future__ import annotations

import json
import os

CORPUS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "corpus.json")


def _load_corpus() -> list[dict]:
    with open(CORPUS_PATH, encoding="utf-8") as f:
        return json.load(f)["documents"]


def handle_request(request: dict) -> dict:
    """Stateless tool-call handler. `request` is a plain JSON-shaped dict — no session, no history."""
    tool = request.get("tool")
    documents = _load_corpus()  # reloaded every call — nothing persists between requests

    if tool == "search":
        query = (request.get("query") or "").lower()
        if not query:
            return {"status": "error", "message": "search requires a non-empty 'query'"}
        # Only authority-class documents are citable search hits (Section on Authority vs Orientation).
        hits = [
            {"stable_id": d["stable_id"], "title": d["title"], "version": d["version"]}
            for d in documents
            if d["authority_class"] == "authority" and query in d["text"].lower()
        ]
        if not hits:
            return {
                "status": "abstain",
                "reason": f"no authority document matches query {query!r} — this is not covered by the corpus",
            }
        return {"status": "ok", "hits": hits}

    if tool == "retrieve":
        stable_id = request.get("stable_id")
        for d in documents:
            if d["stable_id"] == stable_id:
                return {
                    "status": "ok",
                    "stable_id": d["stable_id"],
                    "owner": d["owner"],
                    "version": d["version"],
                    "authority_class": d["authority_class"],
                    "text": d["text"],
                }
        return {"status": "abstain", "reason": f"no document with stable_id {stable_id!r}"}

    return {"status": "error", "message": f"unknown tool {tool!r}, expected 'search' or 'retrieve'"}
