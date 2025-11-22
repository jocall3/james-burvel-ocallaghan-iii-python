# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LinkedAccount"]


class LinkedAccount(BaseModel):
    id: str
    """Unique identifier for the linked account within ."""

    currency: str
    """The currency of the account (ISO 4217 code)."""

    current_balance: float = FieldInfo(alias="currentBalance")
    """The current balance of the account."""

    institution_name: str = FieldInfo(alias="institutionName")
    """Name of the financial institution holding the account."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the account balance and details were last synced."""

    name: str
    """User-friendly name of the account."""

    type: Literal["depository", "credit", "investment", "loan", "other"]
    """High-level type of the financial account."""

    account_link_status: Optional[Literal["active", "inactive", "reconnect_required", "error"]] = FieldInfo(
        alias="accountLinkStatus", default=None
    )
    """Current status of the connection to the external institution."""

    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """
    Full account number (sensitive, typically only accessible with explicit
    permissions).
    """

    available_balance: Optional[float] = FieldInfo(alias="availableBalance", default=None)
    """
    The available balance of the account (may differ from current due to pending
    transactions).
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    Optional: Identifier from the external financial institution (e.g., Plaid
    account ID).
    """

    mask: Optional[str] = None
    """Last 4 digits of the account number for display purposes (masked)."""

    routing_number: Optional[str] = FieldInfo(alias="routingNumber", default=None)
    """
    Bank routing number (sensitive, typically only accessible with explicit
    permissions).
    """

    subtype: Optional[str] = None
    """Specific subtype of the account (e.g., checking, savings, IRA, credit card)."""
