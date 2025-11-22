# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .linked_account import LinkedAccount

__all__ = [
    "AccountRetrieveAccountDetailsResponse",
    "AccountRetrieveAccountDetailsResponseBalanceHistory",
    "AccountRetrieveAccountDetailsResponseProjectedCashFlow",
]


class AccountRetrieveAccountDetailsResponseBalanceHistory(BaseModel):
    balance: Optional[float] = None

    date: Optional[datetime.date] = None


class AccountRetrieveAccountDetailsResponseProjectedCashFlow(BaseModel):
    confidence_score: Optional[int] = FieldInfo(alias="confidenceScore", default=None)
    """AI's confidence score (0-100) in the accuracy of the projection."""

    days30: Optional[float] = None
    """AI-projected net cash flow for the next 30 days."""

    days90: Optional[float] = None
    """AI-projected net cash flow for the next 90 days."""


class AccountRetrieveAccountDetailsResponse(LinkedAccount):
    account_holder: Optional[str] = FieldInfo(alias="accountHolder", default=None)
    """Name of the primary account holder."""

    balance_history: Optional[List[AccountRetrieveAccountDetailsResponseBalanceHistory]] = FieldInfo(
        alias="balanceHistory", default=None
    )
    """Historical daily balances for the account."""

    interest_rate: Optional[float] = FieldInfo(alias="interestRate", default=None)
    """Annual interest rate for the account (e.g., for savings or loans)."""

    opened_date: Optional[datetime.date] = FieldInfo(alias="openedDate", default=None)
    """Date when the account was opened."""

    projected_cash_flow: Optional[AccountRetrieveAccountDetailsResponseProjectedCashFlow] = FieldInfo(
        alias="projectedCashFlow", default=None
    )
    """AI-driven projection of future cash flow for the account."""

    transactions_count: Optional[int] = FieldInfo(alias="transactionsCount", default=None)
    """
    Total number of transactions in the account's history (or within a default
    period).
    """
