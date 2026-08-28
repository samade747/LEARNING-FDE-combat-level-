"""Minimal logging setup for sdk_parser — one shared logger, no config file needed."""
from __future__ import annotations

import logging

logger = logging.getLogger("sdk_parser")
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)s %(name)s: %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
