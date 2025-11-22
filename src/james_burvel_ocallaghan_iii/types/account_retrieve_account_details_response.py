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
    """Balance on that date."""

    date: Optional[datetime.date] = None
    """Date of the balance snapshot."""


class AccountRetrieveAccountDetailsResponseProjectedCashFlow(BaseModel):
    confidence_score: Optional[float] = FieldInfo(alias="confidenceScore", default=None)
    """AI's confidence score (0-100) in the accuracy of the cash flow projection."""

    days30: Optional[float] = None
    """Projected net cash flow for the next 30 days."""

    days90: Optional[float] = None
    """Projected net cash flow for the next 90 days."""


class AccountRetrieveAccountDetailsResponse(LinkedAccount):
    account_holder: Optional[str] = FieldInfo(alias="accountHolder", default=None)
    """The name of the primary holder of the account."""

    balance_history: Optional[List[AccountRetrieveAccountDetailsResponseBalanceHistory]] = FieldInfo(
        alias="balanceHistory", default=None
    )
    """Historical daily balances for the account over a recent period."""

    interest_rate: Optional[float] = FieldInfo(alias="interestRate", default=None)
    """Annual interest rate for the account (e.g., APY for savings, APR for credit)."""

    opened_date: Optional[datetime.date] = FieldInfo(alias="openedDate", default=None)
    """The date the account was opened."""

    projected_cash_flow: Optional[AccountRetrieveAccountDetailsResponseProjectedCashFlow] = FieldInfo(
        alias="projectedCashFlow", default=None
    )

    transactions_count: Optional[int] = FieldInfo(alias="transactionsCount", default=None)
    """Total number of transactions recorded for this account."""
