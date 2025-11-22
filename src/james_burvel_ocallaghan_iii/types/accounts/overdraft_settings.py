# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OverdraftSettings"]


class OverdraftSettings(BaseModel):
    account_id: str = FieldInfo(alias="accountId")
    """The ID of the account these settings apply to."""

    enabled: bool
    """Whether overdraft protection is currently enabled for this account."""

    fee_preference: Literal["always_pay", "decline_if_over_limit", "ask_me_first"] = FieldInfo(alias="feePreference")
    """
    User's preference for how overdrafts should be handled (e.g., always pay,
    decline if over limit).
    """

    linked_savings_account_id: Optional[str] = FieldInfo(alias="linkedSavingsAccountId", default=None)
    """The ID of the savings account linked for overdraft protection, if applicable."""

    link_to_savings: Optional[bool] = FieldInfo(alias="linkToSavings", default=None)
    """
    If true, attempts to draw funds from a linked savings account before incurring
    fees.
    """

    protection_limit: Optional[float] = FieldInfo(alias="protectionLimit", default=None)
    """The maximum amount the account can be overdrawn if protection is active."""
