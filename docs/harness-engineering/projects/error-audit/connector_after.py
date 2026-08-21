"""Same 3 errors, rewritten so the message itself tells the agent the next
step — no human needed to translate. This is what Project 3 asks you to
produce yourself, starting from connector_before.py."""


class ConnectorError(Exception):
    pass


def fetch_record(record_id, api_key=None):
    if not api_key:
        raise ConnectorError(
            "Missing api_key. Call fetch_record(record_id, api_key=<your key>) "
            "— get one from settings.md if you don't have it."
        )

    if not isinstance(record_id, str) or not record_id.startswith("rec_"):
        raise ConnectorError(
            f"record_id must be a string starting with 'rec_', got {record_id!r}. "
            "Example: fetch_record('rec_1234')."
        )

    if record_id == "rec_ratelimited":
        raise ConnectorError(
            "Rate limited. Wait 60 seconds before retrying this exact call — "
            "do not retry immediately, and do not switch record_id to work around it."
        )

    return {"id": record_id, "status": "ok"}
