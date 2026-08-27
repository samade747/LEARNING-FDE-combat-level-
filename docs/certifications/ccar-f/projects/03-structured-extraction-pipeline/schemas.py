"""Exercise 3 schemas — the extraction tool's JSON schema, per the official exercise's step 1:
required + optional fields, an "other" + detail-string enum pattern, and nullable fields for
information that may not exist in a given source document.
"""
from __future__ import annotations

EXTRACTION_TOOL_DEF = {
    "name": "extract_invoice_fields",
    "description": (
        "Extract structured fields from an invoice document. Return null for any field whose "
        "value is not present in the document — never invent or estimate a value."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "invoice_number": {"type": ["string", "null"], "description": "Required on every real invoice."},
            "total_amount": {"type": ["number", "null"]},
            "currency": {"type": ["string", "null"]},
            "due_date": {"type": ["string", "null"], "description": "ISO 8601 date, or null if not stated."},
            "payment_method": {
                "type": ["string", "null"],
                "enum": ["bank_transfer", "credit_card", "check", "cash", "other", None],
                "description": "Use 'other' + payment_method_detail when a method is named but does not fit the enum.",
            },
            "payment_method_detail": {
                "type": ["string", "null"],
                "description": "Required when payment_method is 'other'; null otherwise.",
            },
        },
        "required": ["invoice_number", "total_amount", "currency", "due_date", "payment_method", "payment_method_detail"],
    },
}

REQUIRED_FIELDS = tuple(EXTRACTION_TOOL_DEF["input_schema"]["required"])
_ALLOWED_PAYMENT_METHODS = set(EXTRACTION_TOOL_DEF["input_schema"]["properties"]["payment_method"]["enum"])


def validate_extraction(fields: dict) -> list[str]:
    """Returns a list of validation errors (empty = valid). Mirrors what a Pydantic/JSON-schema
    validator would report — kept dependency-free for the offline exercise."""
    errors = []
    for name in REQUIRED_FIELDS:
        if name not in fields:
            errors.append(f"missing required field: {name}")

    if "payment_method" in fields:
        pm = fields["payment_method"]
        if pm not in _ALLOWED_PAYMENT_METHODS:
            errors.append(f"payment_method {pm!r} is not one of the allowed enum values")
        if pm == "other" and not fields.get("payment_method_detail"):
            errors.append("payment_method is 'other' but payment_method_detail is missing/null")
        if pm != "other" and fields.get("payment_method_detail") not in (None,):
            errors.append("payment_method_detail must be null unless payment_method is 'other'")

    if "total_amount" in fields and fields["total_amount"] is not None:
        if not isinstance(fields["total_amount"], (int, float)) or fields["total_amount"] < 0:
            errors.append("total_amount must be a non-negative number or null")

    return errors
