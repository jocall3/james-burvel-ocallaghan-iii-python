# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CardListTransactionsParams"]


class CardListTransactionsParams(TypedDict, total=False):
    end_date: Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]
    """End date for filtering results (inclusive). Format: YYYY-MM-DD."""

    limit: int
    """Maximum number of items to return in the response."""

    offset: int
    """Number of items to skip before starting to collect the result set."""

    start_date: Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]
    """Start date for filtering results (inclusive). Format: YYYY-MM-DD."""
