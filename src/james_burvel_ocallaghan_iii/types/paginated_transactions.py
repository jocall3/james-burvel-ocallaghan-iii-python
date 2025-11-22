# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .transaction import Transaction

__all__ = ["PaginatedTransactions"]


class PaginatedTransactions(BaseModel):
    data: List[Transaction]
    """The list of transactions for the current page."""

    limit: int
    """The maximum number of items returned per page."""

    offset: int
    """The starting index of the list for pagination."""

    total: int
    """The total number of available items across all pages."""

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)
    """The offset to use for the next page of results, if available."""
