# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CorporateCardControlsParam"]


class CorporateCardControlsParam(TypedDict, total=False):
    atm_withdrawals: Annotated[bool, PropertyInfo(alias="atmWithdrawals")]
    """If true, ATM cash withdrawals are allowed."""

    contactless_payments: Annotated[bool, PropertyInfo(alias="contactlessPayments")]
    """If true, contactless payments are allowed."""

    daily_limit: Annotated[Optional[float], PropertyInfo(alias="dailyLimit")]
    """Maximum spending limit per day (null for no limit)."""

    international_transactions: Annotated[bool, PropertyInfo(alias="internationalTransactions")]
    """If true, international transactions are allowed."""

    merchant_category_restrictions: Annotated[
        Optional[SequenceNotStr[str]], PropertyInfo(alias="merchantCategoryRestrictions")
    ]
    """List of allowed merchant categories.

    If empty, all are allowed unless explicitly denied.
    """

    monthly_limit: Annotated[Optional[float], PropertyInfo(alias="monthlyLimit")]
    """Maximum spending limit per month (null for no limit)."""

    online_transactions: Annotated[bool, PropertyInfo(alias="onlineTransactions")]
    """If true, online transactions are allowed."""

    single_transaction_limit: Annotated[Optional[float], PropertyInfo(alias="singleTransactionLimit")]
    """Maximum amount for a single transaction (null for no limit)."""

    vendor_restrictions: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="vendorRestrictions")]
    """List of allowed vendors/merchants by name."""
