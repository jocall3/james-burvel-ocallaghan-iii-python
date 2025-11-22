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
    """Name of the financial institution where the account is held."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp of when the account balance was last updated."""

    mask: str
    """Masked account number (e.g., last 4 digits) for display."""

    name: str
    """User-friendly name of the account."""

    type: Literal["depository", "credit", "loan", "investment", "other"]
    """High-level type of the financial account."""

    available_balance: Optional[float] = FieldInfo(alias="availableBalance", default=None)
    """The available balance, considering pending transactions or holds."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """Optional: Identifier from the external financial institution/aggregator."""

    subtype: Optional[str] = None
    """Specific subtype of the account (e.g., checking, savings, IRA, credit card)."""
