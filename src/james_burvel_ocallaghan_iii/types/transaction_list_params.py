# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransactionListParams"]


class TransactionListParams(TypedDict, total=False):
    category: str
    """Filter transactions by their AI-assigned or user-defined category."""

    end_date: Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]
    """Retrieve transactions up to this date (inclusive)."""

    limit: int
    """Maximum number of items to return in a single page."""

    max_amount: Annotated[float, PropertyInfo(alias="maxAmount")]
    """Filter for transactions with an amount less than or equal to this value."""

    min_amount: Annotated[float, PropertyInfo(alias="minAmount")]
    """Filter for transactions with an amount greater than or equal to this value."""

    offset: int
    """Number of items to skip before starting to collect the result set."""

    search_query: Annotated[str, PropertyInfo(alias="searchQuery")]
    """Free-text search across transaction descriptions, merchants, and notes."""

    start_date: Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]
    """Retrieve transactions from this date (inclusive)."""

    type: Literal["income", "expense", "transfer", "investment", "refund", "bill_payment"]
    """Filter transactions by type (e.g., income, expense, transfer)."""
