# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CardUpdateControlsParams", "TimeBasedRestrictions"]


class CardUpdateControlsParams(TypedDict, total=False):
    atm_withdrawals: Required[Annotated[bool, PropertyInfo(alias="atmWithdrawals")]]
    """Allow or disallow ATM cash withdrawals."""

    contactless_payments: Required[Annotated[bool, PropertyInfo(alias="contactlessPayments")]]
    """Allow or disallow contactless payments."""

    daily_limit: Required[Annotated[float, PropertyInfo(alias="dailyLimit")]]
    """Maximum spending allowed per day."""

    international_transactions: Required[Annotated[bool, PropertyInfo(alias="internationalTransactions")]]
    """Allow or disallow international transactions."""

    monthly_limit: Required[Annotated[float, PropertyInfo(alias="monthlyLimit")]]
    """Maximum spending allowed per month."""

    online_transactions: Required[Annotated[bool, PropertyInfo(alias="onlineTransactions")]]
    """Allow or disallow online transactions."""

    single_transaction_limit: Required[Annotated[float, PropertyInfo(alias="singleTransactionLimit")]]
    """Maximum amount allowed for a single transaction."""

    merchant_category_restrictions: Annotated[
        Optional[SequenceNotStr[str]], PropertyInfo(alias="merchantCategoryRestrictions")
    ]
    """List of merchant categories (MCCs) allowed or blocked."""

    time_based_restrictions: Annotated[Optional[TimeBasedRestrictions], PropertyInfo(alias="timeBasedRestrictions")]

    vendor_restrictions: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="vendorRestrictions")]
    """Specific vendors allowed or blocked."""


class TimeBasedRestrictions(TypedDict, total=False):
    daily_end_time: Annotated[str, PropertyInfo(alias="dailyEndTime")]
    """End time for allowed transactions (HH:MM)."""

    daily_start_time: Annotated[str, PropertyInfo(alias="dailyStartTime")]
    """Start time for allowed transactions (HH:MM)."""

    weekdays_only: Annotated[bool, PropertyInfo(alias="weekdaysOnly")]
    """Only allow transactions on weekdays."""
