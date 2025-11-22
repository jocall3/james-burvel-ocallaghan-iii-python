# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OverdraftSettingUpdateSettingsParams"]


class OverdraftSettingUpdateSettingsParams(TypedDict, total=False):
    enabled: bool
    """Enable or disable overdraft protection."""

    fee_preference: Annotated[
        Literal["always_pay", "decline_if_over_limit", "ask_me_first"], PropertyInfo(alias="feePreference")
    ]
    """New preference for how overdraft fees are handled."""

    linked_savings_account_id: Annotated[Optional[str], PropertyInfo(alias="linkedSavingsAccountId")]
    """New ID of the linked savings account, if `linkToSavings` is true.

    Set to null to unlink.
    """

    link_to_savings: Annotated[Optional[bool], PropertyInfo(alias="linkToSavings")]
    """Enable or disable linking to a savings account for overdraft coverage."""

    protection_limit: Annotated[Optional[float], PropertyInfo(alias="protectionLimit")]
    """New maximum amount for overdraft protection. Set to null to remove limit."""
