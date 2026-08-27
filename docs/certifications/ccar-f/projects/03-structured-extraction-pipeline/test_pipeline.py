"""test_pipeline.py — offline verification for Exercise 3, no API key, no network.

FakeExtractionClient plays back scripted extraction/batch responses so pipeline.py's control flow
(validation-retry, batch resubmission, confidence routing) is exercised without a real model.
"""
from pipeline import extract_with_retry, route_by_confidence, run_batch


class FakeExtractionClient:
    def __init__(self, extract_responses=None):
        self._extract_responses = list(extract_responses or [])
        self.extract_calls = 0
        self._batch_responses = []
        self.batch_calls = 0

    def extract(self, document, prior_fields=None, prior_error=None):
        self.extract_calls += 1
        assert self._extract_responses, "extract() called more times than scripted"
        return self._extract_responses.pop(0)

    def queue_batch_response(self, response):
        self._batch_responses.append(response)

    def submit_batch(self, batch_request):
        self.batch_calls += 1
        assert self._batch_responses, "submit_batch() called more times than scripted"
        return self._batch_responses.pop(0)


VALID_FIELDS = {
    "invoice_number": "INV-001",
    "total_amount": 450.0,
    "currency": "USD",
    "due_date": None,  # genuinely absent from the source document
    "payment_method": "bank_transfer",
    "payment_method_detail": None,
}


def test_missing_info_returns_null_not_fabricated():
    """Step 1's own check: a field absent from the source document comes back null, not guessed."""
    client = FakeExtractionClient([{"fields": VALID_FIELDS}])
    result = extract_with_retry(client, {"id": "docA", "text": "..."})
    assert result["fields"]["due_date"] is None
    assert result["attempts"] == 1
    assert result["resolved_by_retry"] is False


def test_validation_retry_resolves_a_format_mismatch():
    """A wrong-case enum value fails validation; the retry, told the specific error, corrects it."""
    bad_fields = {**VALID_FIELDS, "payment_method": "Bank Transfer"}  # not in the enum
    client = FakeExtractionClient([
        {"fields": bad_fields},
        {"fields": VALID_FIELDS},  # corrected on the 2nd attempt
    ])
    result = extract_with_retry(client, {"id": "docA", "text": "..."})
    assert result["fields"]["payment_method"] == "bank_transfer"
    assert result["attempts"] == 2
    assert result["resolved_by_retry"] is True
    assert client.extract_calls == 2


def test_validation_retry_exhausts_on_a_persistent_error():
    """When the model keeps returning the same invalid value despite the error, retries exhaust
    cleanly instead of looping forever or silently accepting bad data."""
    bad_fields = {**VALID_FIELDS, "payment_method": "Bank Transfer"}
    client = FakeExtractionClient([{"fields": bad_fields}] * 3)  # 1 + MAX_RETRIES(2) = 3 attempts
    result = extract_with_retry(client, {"id": "docA", "text": "..."}, max_retries=2)
    assert result["fields"] is None
    assert result["attempts"] == 3
    assert "payment_method" in result["error"]
    assert client.extract_calls == 3


def test_batch_resubmits_oversized_documents():
    documents = [
        {"id": "docA", "text": "short doc"},
        {"id": "docB", "text": "x" * 10_000},
    ]
    client = FakeExtractionClient()
    client.queue_batch_response({
        "docA": {"status": "succeeded", "fields": VALID_FIELDS},
        "docB": {"status": "failed", "reason": "oversized"},
    })
    client.queue_batch_response({
        "docB": {"status": "succeeded", "fields": VALID_FIELDS, "chunked": True},
    })

    result = run_batch(client, documents)

    assert set(result["succeeded"]) == {"docA", "docB"}
    assert result["failed"] == {}
    assert result["resubmitted"] == ["docB"]
    assert client.batch_calls == 2


def test_confidence_routing_separates_low_confidence_fields():
    extractions = [
        {"doc_id": "docA", "confidence": {"invoice_number": 0.95, "total_amount": 0.9}},
        {"doc_id": "docB", "confidence": {"invoice_number": 0.4, "total_amount": 0.92}},
        {"doc_id": "docC", "confidence": {"invoice_number": 0.5, "total_amount": 0.3}},
    ]
    result = route_by_confidence(extractions, threshold=0.7)

    assert result["auto_accept"] == ["docA"]
    assert {r["doc_id"] for r in result["human_review"]} == {"docB", "docC"}
    assert result["low_confidence_by_field"] == {"invoice_number": 2, "total_amount": 1}
