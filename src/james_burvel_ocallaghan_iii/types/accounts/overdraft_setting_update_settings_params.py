# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OverdraftSettingUpdateSettingsParams"]


class OverdraftSettingUpdateSettingsParams(TypedDict, total=False):
    enabled: bool
    """Set to `true` to enable, `false` to disable overdraft protection."""

    fee_preference: Annotated[
        Literal["always_pay", "decline_if_over_limit", "ask_me"], PropertyInfo(alias="feePreference")
    ]
    """New user preference for how overdrafts should be handled."""

    linked_savings_account_id: Annotated[Optional[str], PropertyInfo(alias="linkedSavingsAccountId")]
    """The ID of the savings account to link. Set to `null` if unlinking."""

    link_to_savings: Annotated[bool, PropertyInfo(alias="linkToSavings")]
    """Set to `true` to link to savings, `false` to unlink."""

    protection_limit: Annotated[Optional[float], PropertyInfo(alias="protectionLimit")]
    """The new maximum overdraft amount. Set to `null` if disabling protection."""
