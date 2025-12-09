# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CorporateCardControlsParam"]


class CorporateCardControlsParam(TypedDict, total=False):
    """Granular spending controls for a corporate card."""

    atm_withdrawals: Annotated[object, PropertyInfo(alias="atmWithdrawals")]
    """If true, ATM cash withdrawals are allowed."""

    contactless_payments: Annotated[object, PropertyInfo(alias="contactlessPayments")]
    """If true, contactless payments are allowed."""

    daily_limit: Annotated[object, PropertyInfo(alias="dailyLimit")]
    """Maximum spending limit per day (null for no limit)."""

    international_transactions: Annotated[object, PropertyInfo(alias="internationalTransactions")]
    """If true, international transactions are allowed."""

    merchant_category_restrictions: Annotated[
        Optional[Iterable[object]], PropertyInfo(alias="merchantCategoryRestrictions")
    ]
    """List of allowed merchant categories.

    If empty, all are allowed unless explicitly denied.
    """

    monthly_limit: Annotated[object, PropertyInfo(alias="monthlyLimit")]
    """Maximum spending limit per month (null for no limit)."""

    online_transactions: Annotated[object, PropertyInfo(alias="onlineTransactions")]
    """If true, online transactions are allowed."""

    single_transaction_limit: Annotated[object, PropertyInfo(alias="singleTransactionLimit")]
    """Maximum amount for a single transaction (null for no limit)."""

    vendor_restrictions: Annotated[Optional[Iterable[object]], PropertyInfo(alias="vendorRestrictions")]
    """List of allowed vendors/merchants by name."""
