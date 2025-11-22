# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LinkedAccount"]


class LinkedAccount(BaseModel):
    id: str
    """Internal unique identifier for the linked account."""

    currency: str
    """ISO 4217 currency code of the account."""

    current_balance: float = FieldInfo(alias="currentBalance")
    """Current balance of the account."""

    institution_name: str = FieldInfo(alias="institutionName")
    """Name of the financial institution."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the account balance was last synced/updated."""

    name: str
    """User-friendly name of the account."""

    type: Literal["depository", "credit", "loan", "investment", "mortgage", "other"]
    """High-level type of the account."""

    available_balance: Optional[float] = FieldInfo(alias="availableBalance", default=None)
    """Available balance (may differ from current due to pending transactions)."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """Identifier from the external financial institution or aggregator."""

    is_primary: Optional[bool] = FieldInfo(alias="isPrimary", default=None)
    """Indicates if this is the user's primary account for general operations."""

    mask: Optional[str] = None
    """Masked account number (e.g., last 4 digits)."""

    subtype: Optional[str] = None
    """Specific subtype of the account (e.g., checking, savings, IRA, 401k)."""
