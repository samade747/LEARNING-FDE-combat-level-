"""Exercise 1 tools — a tiny in-memory fake CRM so the exercise runs with no external services.

Every tool either returns a plain dict (success) or raises ToolError (structured failure) —
the errorCategory/isRetryable shape the CCAR-F guide's Exercise 1 asks for.
"""
from __future__ import annotations

from dataclasses import dataclass


class ToolError(Exception):
    """A structured tool failure: errorCategory + isRetryable, not a bare exception message."""

    def __init__(self, error_category: str, is_retryable: bool, message: str):
        assert error_category in {"transient", "validation", "business", "permission"}
        self.error_category = error_category
        self.is_retryable = is_retryable
        self.message = message
        super().__init__(message)

    def to_dict(self) -> dict:
        return {
            "errorCategory": self.error_category,
            "isRetryable": self.is_retryable,
            "message": self.message,
        }


_CUSTOMERS = {
    "cust_1": {"customer_id": "cust_1", "name": "Amina Raza", "email": "amina@example.com"},
    "cust_2": {"customer_id": "cust_2", "name": "Bilal Khan", "email": "bilal@example.com"},
}

_ORDERS = {
    "ord_100": {"order_id": "ord_100", "customer_id": "cust_1", "total": 45.00, "shipped": True},
    "ord_200": {"order_id": "ord_200", "customer_id": "cust_2", "total": 899.00, "shipped": False},
}


def get_customer(name: str) -> dict:
    """Look a customer up by name. This is the exercise's mandatory verification step."""
    for customer in _CUSTOMERS.values():
        if customer["name"].lower() == name.lower():
            return dict(customer)
    raise ToolError("validation", False, f"No customer found matching name '{name}'.")


def lookup_order(customer_id: str, order_id: str) -> dict:
    order = _ORDERS.get(order_id)
    if order is None:
        raise ToolError("validation", False, f"No such order '{order_id}'.")
    if order["customer_id"] != customer_id:
        raise ToolError("permission", False, "Order does not belong to this customer.")
    return dict(order)


def process_refund(customer_id: str, order_id: str, amount: float) -> dict:
    order = lookup_order(customer_id, order_id)
    if amount > order["total"]:
        raise ToolError("validation", False, "Refund amount exceeds order total.")
    return {"refund_id": f"rf_{order_id}", "amount": amount, "status": "processed"}


def update_shipping_address(customer_id: str, order_id: str, address: str) -> dict:
    order = lookup_order(customer_id, order_id)
    if order["shipped"]:
        raise ToolError("business", False, "Order already shipped — address can no longer change.")
    return {"order_id": order_id, "new_address": address, "status": "updated"}


@dataclass(frozen=True)
class ToolSpec:
    name: str
    description: str
    input_schema: dict
    fn: callable


TOOLS: dict[str, ToolSpec] = {
    "get_customer": ToolSpec(
        name="get_customer",
        description=(
            "Look up a customer by their stated name and return their verified customer_id. "
            "Call this FIRST, before lookup_order/process_refund/update_shipping_address — those "
            "tools require a verified customer_id, not a customer name."
        ),
        input_schema={
            "type": "object",
            "properties": {"name": {"type": "string", "description": "Customer's full name as given by the user."}},
            "required": ["name"],
        },
        fn=get_customer,
    ),
    "lookup_order": ToolSpec(
        name="lookup_order",
        description="Retrieve order details by order_id, scoped to a verified customer_id.",
        input_schema={
            "type": "object",
            "properties": {
                "customer_id": {"type": "string", "description": "Verified customer_id from get_customer."},
                "order_id": {"type": "string"},
            },
            "required": ["customer_id", "order_id"],
        },
        fn=lookup_order,
    ),
    "process_refund": ToolSpec(
        name="process_refund",
        description=(
            "Issue a refund for an order, scoped to a verified customer_id. Refunds above the "
            "configured threshold always escalate to a human — this tool will not be called for those."
        ),
        input_schema={
            "type": "object",
            "properties": {
                "customer_id": {"type": "string"},
                "order_id": {"type": "string"},
                "amount": {"type": "number"},
            },
            "required": ["customer_id", "order_id", "amount"],
        },
        fn=process_refund,
    ),
    "update_shipping_address": ToolSpec(
        name="update_shipping_address",
        description="Update the shipping address on an unshipped order, scoped to a verified customer_id.",
        input_schema={
            "type": "object",
            "properties": {
                "customer_id": {"type": "string"},
                "order_id": {"type": "string"},
                "address": {"type": "string"},
            },
            "required": ["customer_id", "order_id", "address"],
        },
        fn=update_shipping_address,
    ),
}

ANTHROPIC_TOOL_DEFS = [
    {"name": t.name, "description": t.description, "input_schema": t.input_schema} for t in TOOLS.values()
]
