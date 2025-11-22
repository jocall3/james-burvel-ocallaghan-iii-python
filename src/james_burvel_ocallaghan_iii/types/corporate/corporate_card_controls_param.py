# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CorporateCardControlsParam"]


class CorporateCardControlsParam(TypedDict, total=False):
    atm_withdrawals: Annotated[bool, PropertyInfo(alias="atmWithdrawals")]
    """Allow ATM withdrawals."""

    contactless_payments: Annotated[bool, PropertyInfo(alias="contactlessPayments")]
    """Allow contactless payments."""

    daily_limit: Annotated[Optional[float], PropertyInfo(alias="dailyLimit")]
    """Maximum spending limit per day."""

    international_transactions: Annotated[bool, PropertyInfo(alias="internationalTransactions")]
    """Allow international transactions."""

    merchant_category_restrictions: Annotated[
        Optional[SequenceNotStr[str]], PropertyInfo(alias="merchantCategoryRestrictions")
    ]
    """List of allowed or disallowed merchant categories."""

    monthly_limit: Annotated[Optional[float], PropertyInfo(alias="monthlyLimit")]
    """Maximum spending limit per month."""

    online_transactions: Annotated[bool, PropertyInfo(alias="onlineTransactions")]
    """Allow online transactions."""

    single_transaction_limit: Annotated[Optional[float], PropertyInfo(alias="singleTransactionLimit")]
    """Maximum amount for a single transaction."""

    vendor_restrictions: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="vendorRestrictions")]
    """List of specific allowed or disallowed vendors/merchants."""
