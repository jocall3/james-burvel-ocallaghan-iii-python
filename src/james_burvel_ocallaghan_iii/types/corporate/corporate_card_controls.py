# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CorporateCardControls", "TimeBasedRestrictions"]


class TimeBasedRestrictions(BaseModel):
    daily_end_time: Optional[str] = FieldInfo(alias="dailyEndTime", default=None)
    """End time for allowed transactions (HH:MM)."""

    daily_start_time: Optional[str] = FieldInfo(alias="dailyStartTime", default=None)
    """Start time for allowed transactions (HH:MM)."""

    weekdays_only: Optional[bool] = FieldInfo(alias="weekdaysOnly", default=None)
    """Only allow transactions on weekdays."""


class CorporateCardControls(BaseModel):
    atm_withdrawals: bool = FieldInfo(alias="atmWithdrawals")
    """Allow or disallow ATM cash withdrawals."""

    contactless_payments: bool = FieldInfo(alias="contactlessPayments")
    """Allow or disallow contactless payments."""

    daily_limit: float = FieldInfo(alias="dailyLimit")
    """Maximum spending allowed per day."""

    international_transactions: bool = FieldInfo(alias="internationalTransactions")
    """Allow or disallow international transactions."""

    monthly_limit: float = FieldInfo(alias="monthlyLimit")
    """Maximum spending allowed per month."""

    online_transactions: bool = FieldInfo(alias="onlineTransactions")
    """Allow or disallow online transactions."""

    single_transaction_limit: float = FieldInfo(alias="singleTransactionLimit")
    """Maximum amount allowed for a single transaction."""

    merchant_category_restrictions: Optional[List[str]] = FieldInfo(alias="merchantCategoryRestrictions", default=None)
    """List of merchant categories (MCCs) allowed or blocked."""

    time_based_restrictions: Optional[TimeBasedRestrictions] = FieldInfo(alias="timeBasedRestrictions", default=None)

    vendor_restrictions: Optional[List[str]] = FieldInfo(alias="vendorRestrictions", default=None)
    """Specific vendors allowed or blocked."""
