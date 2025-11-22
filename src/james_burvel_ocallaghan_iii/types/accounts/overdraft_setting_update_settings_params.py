# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OverdraftSettingUpdateSettingsParams"]


class OverdraftSettingUpdateSettingsParams(TypedDict, total=False):
    enabled: bool
    """Whether overdraft protection should be enabled or disabled."""

    fee_preference: Annotated[
        Literal["always_pay", "decline_if_over_limit", "ask_me_first"], PropertyInfo(alias="feePreference")
    ]
    """The new preference for how overdrafts should be handled."""

    linked_savings_account_id: Annotated[Optional[str], PropertyInfo(alias="linkedSavingsAccountId")]
    """The new savings account to link, or null to unlink."""

    link_to_savings: Annotated[bool, PropertyInfo(alias="linkToSavings")]
    """Whether to enable or disable linking to a savings account."""

    protection_limit: Annotated[Optional[float], PropertyInfo(alias="protectionLimit")]
    """The new maximum overdraft amount. Set to null to remove."""
