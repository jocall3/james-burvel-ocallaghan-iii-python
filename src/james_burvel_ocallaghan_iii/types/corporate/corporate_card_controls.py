# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CorporateCardControls"]


class CorporateCardControls(BaseModel):
    atm_withdrawals: Optional[bool] = FieldInfo(alias="atmWithdrawals", default=None)
    """Allow ATM withdrawals."""

    contactless_payments: Optional[bool] = FieldInfo(alias="contactlessPayments", default=None)
    """Allow contactless payments."""

    daily_limit: Optional[float] = FieldInfo(alias="dailyLimit", default=None)
    """Maximum spending limit per day."""

    international_transactions: Optional[bool] = FieldInfo(alias="internationalTransactions", default=None)
    """Allow international transactions."""

    merchant_category_restrictions: Optional[List[str]] = FieldInfo(alias="merchantCategoryRestrictions", default=None)
    """List of allowed or disallowed merchant categories."""

    monthly_limit: Optional[float] = FieldInfo(alias="monthlyLimit", default=None)
    """Maximum spending limit per month."""

    online_transactions: Optional[bool] = FieldInfo(alias="onlineTransactions", default=None)
    """Allow online transactions."""

    single_transaction_limit: Optional[float] = FieldInfo(alias="singleTransactionLimit", default=None)
    """Maximum amount for a single transaction."""

    vendor_restrictions: Optional[List[str]] = FieldInfo(alias="vendorRestrictions", default=None)
    """List of specific allowed or disallowed vendors/merchants."""
