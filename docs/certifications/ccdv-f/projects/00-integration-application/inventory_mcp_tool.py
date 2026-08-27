"""Sample Question 3 (Domain 8 — Tools and MCPs): an MCP-server-shaped inventory tool, reusable
across multiple Claude application instances instead of hard-coded per-app logic.

Official guide's own scenario: a team wants an internal inventory REST API reachable from Claude,
reusable across multiple applications and independently maintained. The correct move is an MCP
server exposing the operations as tools — not hard-coding logic per app, not pasting live data into
every prompt, and not assuming a built-in tool reaches an arbitrary internal API.
"""
from __future__ import annotations

_INVENTORY = {
    "sku_100": {"name": "Widget A", "quantity": 42},
    "sku_200": {"name": "Widget B", "quantity": 0},
}

TOOL_DEF = {
    "name": "check_inventory",
    "description": "Look up current stock quantity for a SKU from the shared inventory service.",
    "input_schema": {
        "type": "object",
        "properties": {"sku": {"type": "string"}},
        "required": ["sku"],
    },
}


def check_inventory(sku: str) -> dict:
    item = _INVENTORY.get(sku)
    if item is None:
        return {"sku": sku, "found": False}
    return {"sku": sku, "found": True, **item}


class InventoryMCPServer:
    """One server instance, multiple "app" clients — the whole point of the sample question:
    reusable and independently maintained, instead of the same logic hard-coded into every
    application's system prompt."""

    def __init__(self):
        self.call_log: list[tuple[str, str]] = []

    def handle_tool_call(self, app_name: str, tool_name: str, tool_input: dict) -> dict:
        assert tool_name == "check_inventory"
        self.call_log.append((app_name, tool_input["sku"]))
        return check_inventory(tool_input["sku"])
