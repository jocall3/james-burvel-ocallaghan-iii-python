# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LinkedAccount"]


class LinkedAccount(BaseModel):
    """Summary information for a linked financial account."""

    id: object
    """Unique identifier for the linked account within ."""

    currency: object
    """ISO 4217 currency code of the account."""

    current_balance: object = FieldInfo(alias="currentBalance")
    """Current balance of the account."""

    institution_name: object = FieldInfo(alias="institutionName")
    """Name of the financial institution where the account is held."""

    last_updated: object = FieldInfo(alias="lastUpdated")
    """Timestamp when the account balance was last synced."""

    name: object
    """Display name of the account."""

    type: Literal["depository", "credit", "loan", "investment", "other"]
    """General type of the account."""

    available_balance: Optional[object] = FieldInfo(alias="availableBalance", default=None)
    """Available balance (after pending transactions) of the account."""

    external_id: Optional[object] = FieldInfo(alias="externalId", default=None)
    """Optional: Identifier from the external data provider (e.g., Plaid)."""

    mask: Optional[object] = None
    """Masked account number (e.g., last 4 digits)."""

    subtype: Optional[object] = None
    """Specific subtype of the account (e.g., checking, savings, IRA, 401k)."""
