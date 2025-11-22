# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CardListTransactionsParams"]


class CardListTransactionsParams(TypedDict, total=False):
    end_date: Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]
    """Filter results up to this date (inclusive, YYYY-MM-DD)."""

    limit: int
    """Maximum number of items to return."""

    offset: int
    """Number of items to skip before starting to collect the result set."""

    start_date: Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]
    """Filter results from this date (inclusive, YYYY-MM-DD)."""
