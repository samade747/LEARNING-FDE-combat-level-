"""test_research_pipeline.py — offline verification for Exercise 4, no API key, no network.

Each subagent is a plain Python function standing in for a Task-tool-dispatched subagent: it
takes one task dict and returns a list of findings, or raises SubagentTimeout.
"""
from research_pipeline import SubagentTimeout, build_report, dispatch_subagents, synthesize


def test_parallel_dispatch_collects_all_findings():
    def subagent_fn(task):
        return [{
            "subject": task["id"],
            "claim": f"finding for {task['id']}",
            "evidence_excerpt": "...",
            "source": f"https://example.com/{task['id']}",
            "published_date": "2026-01-01",
        }]

    tasks = [{"id": "web_search", "query": "market size"}, {"id": "doc_analysis", "query": "internal report"}]
    result = dispatch_subagents(subagent_fn, tasks)

    assert set(result["findings_by_task"]) == {"web_search", "doc_analysis"}
    assert result["errors_by_task"] == {}


def test_timeout_produces_structured_error_and_preserves_other_tasks():
    def subagent_fn(task):
        if task["id"] == "web_search":
            raise SubagentTimeout(query=task["query"], partial_results=[{"note": "got 1 of 5 pages"}])
        return [{
            "subject": "market_size", "claim": "$4B", "evidence_excerpt": "...",
            "source": "internal_report.pdf", "published_date": "2026-02-01",
        }]

    tasks = [{"id": "web_search", "query": "market size 2026"}, {"id": "doc_analysis", "query": "internal report"}]
    result = dispatch_subagents(subagent_fn, tasks)

    assert "web_search" not in result["findings_by_task"]  # it failed, no findings recorded for it
    assert "doc_analysis" in result["findings_by_task"]  # the OTHER task's results survive
    err = result["errors_by_task"]["web_search"]
    assert err["failure_type"] == "timeout"
    assert err["attempted_query"] == "market size 2026"
    assert err["partial_results"] == [{"note": "got 1 of 5 pages"}]


def test_synthesis_preserves_conflicting_sources_without_picking_a_winner():
    findings_by_task = {
        "web_search": [{
            "subject": "market_size", "claim": "$4B", "evidence_excerpt": "industry report says $4B",
            "source": "https://research-firm-a.com/report", "published_date": "2026-01-15",
        }],
        "doc_analysis": [{
            "subject": "market_size", "claim": "$2.5B", "evidence_excerpt": "internal estimate: $2.5B",
            "source": "internal_report.pdf", "published_date": "2026-02-01",
        }],
    }
    synthesis = synthesize(findings_by_task)

    assert synthesis["market_size"]["status"] == "contested"
    assert len(synthesis["market_size"]["findings"]) == 2  # both kept, neither dropped
    claims = {f["claim"] for f in synthesis["market_size"]["findings"]}
    assert claims == {"$4B", "$2.5B"}


def test_synthesis_marks_agreeing_sources_well_established():
    findings_by_task = {
        "web_search": [{
            "subject": "market_size", "claim": "$4B", "evidence_excerpt": "report A",
            "source": "https://a.com", "published_date": "2026-01-01",
        }],
        "doc_analysis": [{
            "subject": "market_size", "claim": "$4B", "evidence_excerpt": "report B agrees",
            "source": "https://b.com", "published_date": "2026-01-10",
        }],
    }
    synthesis = synthesize(findings_by_task)

    assert synthesis["market_size"]["status"] == "well_established"
    assert len(synthesis["market_size"]["findings"]) == 2  # both sources still cited


def test_report_includes_coverage_gaps_for_failed_tasks():
    def subagent_fn(task):
        if task["id"] == "web_search":
            raise SubagentTimeout(query=task["query"])
        return [{
            "subject": "market_size", "claim": "$2.5B", "evidence_excerpt": "...",
            "source": "internal_report.pdf", "published_date": "2026-02-01",
        }]

    tasks = [{"id": "web_search", "query": "market size 2026"}, {"id": "doc_analysis", "query": "internal"}]
    dispatched = dispatch_subagents(subagent_fn, tasks)
    report = build_report(dispatched["findings_by_task"], dispatched["errors_by_task"])

    assert report["coverage_gaps"] == [
        {"task_id": "web_search", "reason": "timeout", "query": "market size 2026"}
    ]
    assert "market_size" in report["synthesis"]  # the successful task's data is still reported
