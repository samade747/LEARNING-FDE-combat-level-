"""research_pipeline.py — Exercise 4: Design and Debug a Multi-Agent Research Pipeline.

A coordinator dispatches independent subagent research tasks (step 1), runs them without one
timeout crashing the whole batch (step 4's first half), collects structured findings that keep
content separate from metadata (step 3), and synthesizes results — preserving conflicting sources
instead of arbitrarily picking a winner (step 5) — annotated with what could not be covered
(step 4's second half).
"""
from __future__ import annotations

import time


class SubagentTimeout(Exception):
    """Raised by a subagent callable to simulate a timed-out research task."""

    def __init__(self, query: str, partial_results: list[dict] | None = None):
        self.query = query
        self.partial_results = partial_results or []
        super().__init__(f"subagent timed out on query: {query!r}")


def dispatch_subagents(subagent_fn, tasks: list[dict]) -> dict:
    """Step 1+2 — runs every task through `subagent_fn` (one task dict in, a list of findings
    out, or it raises SubagentTimeout). The exercise's "parallel" is about the *request shape*
    (multiple Task calls emitted in one coordinator turn, not one at a time waiting on each
    reply) — this is where a real harness fans the calls out concurrently; a timed-out task
    contributes a structured error entry instead of crashing the whole batch (step 4)."""
    started = time.perf_counter()
    findings_by_task: dict[str, list[dict]] = {}
    errors_by_task: dict[str, dict] = {}

    for task in tasks:
        try:
            findings_by_task[task["id"]] = subagent_fn(task)
        except SubagentTimeout as e:
            errors_by_task[task["id"]] = {
                "failure_type": "timeout",
                "attempted_query": e.query,
                "partial_results": e.partial_results,
            }

    elapsed = time.perf_counter() - started
    return {"findings_by_task": findings_by_task, "errors_by_task": errors_by_task, "elapsed_s": elapsed}


def synthesize(findings_by_task: dict[str, list[dict]]) -> dict:
    """Step 3+5 — groups findings by subject. Every finding keeps its own claim, evidence
    excerpt, source, and publication date (content never collapsed into prose that drops
    attribution). When findings about the same subject disagree, BOTH are kept with their
    sources — never arbitrarily resolved to one — and the subject is marked "contested" instead
    of "well_established"."""
    by_subject: dict[str, list[dict]] = {}
    for task_findings in findings_by_task.values():
        for finding in task_findings:
            by_subject.setdefault(finding["subject"], []).append(finding)

    report = {}
    for subject, findings in by_subject.items():
        claims = {f["claim"] for f in findings}
        report[subject] = {
            "findings": findings,
            "status": "well_established" if len(claims) == 1 else "contested",
        }
    return report


def build_report(findings_by_task: dict[str, list[dict]], errors_by_task: dict[str, dict]) -> dict:
    """Combines synthesize() with a coverage_gaps list — every task that failed is named, so a
    partial run is never presented to the reader as if it were complete (step 4's second half)."""
    return {
        "synthesis": synthesize(findings_by_task),
        "coverage_gaps": [
            {"task_id": task_id, "reason": err["failure_type"], "query": err["attempted_query"]}
            for task_id, err in errors_by_task.items()
        ],
    }
