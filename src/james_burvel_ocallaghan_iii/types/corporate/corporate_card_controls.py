# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CorporateCardControls"]


class CorporateCardControls(BaseModel):
    atm_withdrawals: Optional[bool] = FieldInfo(alias="atmWithdrawals", default=None)
    """If true, ATM cash withdrawals are allowed."""

    contactless_payments: Optional[bool] = FieldInfo(alias="contactlessPayments", default=None)
    """If true, contactless payments are allowed."""

    daily_limit: Optional[float] = FieldInfo(alias="dailyLimit", default=None)
    """Maximum spending limit per day (null for no limit)."""

    international_transactions: Optional[bool] = FieldInfo(alias="internationalTransactions", default=None)
    """If true, international transactions are allowed."""

    merchant_category_restrictions: Optional[List[str]] = FieldInfo(alias="merchantCategoryRestrictions", default=None)
    """List of allowed merchant categories.

    If empty, all are allowed unless explicitly denied.
    """

    monthly_limit: Optional[float] = FieldInfo(alias="monthlyLimit", default=None)
    """Maximum spending limit per month (null for no limit)."""

    online_transactions: Optional[bool] = FieldInfo(alias="onlineTransactions", default=None)
    """If true, online transactions are allowed."""

    single_transaction_limit: Optional[float] = FieldInfo(alias="singleTransactionLimit", default=None)
    """Maximum amount for a single transaction (null for no limit)."""

    vendor_restrictions: Optional[List[str]] = FieldInfo(alias="vendorRestrictions", default=None)
    """List of allowed vendors/merchants by name."""
