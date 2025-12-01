# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OverdraftSettings"]


class OverdraftSettings(BaseModel):
    account_id: object = FieldInfo(alias="accountId")
    """The account ID these overdraft settings apply to."""

    enabled: object
    """If true, overdraft protection is enabled."""

    fee_preference: Literal["always_pay", "decline_if_over_limit", "ask_me_first"] = FieldInfo(alias="feePreference")
    """
    User's preference for how overdraft fees are handled or if transactions should
    be declined.
    """

    linked_savings_account_id: Optional[object] = FieldInfo(alias="linkedSavingsAccountId", default=None)
    """The ID of the linked savings account, if `linkToSavings` is true."""

    link_to_savings: Optional[object] = FieldInfo(alias="linkToSavings", default=None)
    """If true, attempts to draw funds from a linked savings account."""

    protection_limit: Optional[object] = FieldInfo(alias="protectionLimit", default=None)
    """The maximum amount that can be covered by overdraft protection."""
