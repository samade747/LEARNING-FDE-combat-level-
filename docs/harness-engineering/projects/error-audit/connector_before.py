"""A mock 'connector' with 3 realistic errors, written the way most APIs
actually write them — technically true, useless to an agent reading it."""


class ConnectorError(Exception):
    pass


def fetch_record(record_id, api_key=None):
    if not api_key:
        raise ConnectorError("401 Unauthorized")

    if not isinstance(record_id, str) or not record_id.startswith("rec_"):
        raise ConnectorError("400 Bad Request: invalid input")

    if record_id == "rec_ratelimited":
        raise ConnectorError("429 Too Many Requests")

    return {"id": record_id, "status": "ok"}
