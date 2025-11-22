# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CorporateCardControls"]


class CorporateCardControls(BaseModel):
    atm_withdrawals: Optional[bool] = FieldInfo(alias="atmWithdrawals", default=None)
    """Allow or disallow ATM cash withdrawals."""

    contactless_payments: Optional[bool] = FieldInfo(alias="contactlessPayments", default=None)
    """Allow or disallow contactless (NFC) payments."""

    daily_limit: Optional[float] = FieldInfo(alias="dailyLimit", default=None)
    """Maximum spending limit per day."""

    international_transactions: Optional[bool] = FieldInfo(alias="internationalTransactions", default=None)
    """Allow or disallow transactions outside the primary country."""

    merchant_category_restrictions: Optional[List[str]] = FieldInfo(alias="merchantCategoryRestrictions", default=None)
    """
    List of allowed or disallowed merchant categories (e.g., 'Restaurants',
    'Travel').
    """

    monthly_limit: Optional[float] = FieldInfo(alias="monthlyLimit", default=None)
    """Maximum spending limit per month."""

    online_transactions: Optional[bool] = FieldInfo(alias="onlineTransactions", default=None)
    """Allow or disallow online purchases."""

    single_transaction_limit: Optional[float] = FieldInfo(alias="singleTransactionLimit", default=None)
    """Maximum amount for a single transaction."""

    vendor_restrictions: Optional[List[str]] = FieldInfo(alias="vendorRestrictions", default=None)
    """
    List of allowed or disallowed specific vendors/merchants (e.g., 'Amazon',
    'Uber').
    """
