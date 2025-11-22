# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OverdraftSettings"]


class OverdraftSettings(BaseModel):
    account_id: str = FieldInfo(alias="accountId")
    """The ID of the account these settings apply to."""

    enabled: bool
    """Indicates if overdraft protection is currently enabled for this account."""

    fee_preference: Optional[Literal["always_pay", "decline_if_over_limit", "ask_first"]] = FieldInfo(
        alias="feePreference", default=None
    )
    """User preference for how overdrafts should be handled regarding fees/denials."""

    last_updated: Optional[datetime] = FieldInfo(alias="lastUpdated", default=None)
    """Timestamp when these settings were last updated."""

    linked_savings_account_id: Optional[str] = FieldInfo(alias="linkedSavingsAccountId", default=None)
    """The ID of the savings account linked for overdraft protection, if applicable."""

    link_to_savings: Optional[bool] = FieldInfo(alias="linkToSavings", default=None)
    """If true, attempts to draw funds from a linked savings account."""

    protection_limit: Optional[float] = FieldInfo(alias="protectionLimit", default=None)
    """The maximum amount that can be covered by overdraft protection."""
