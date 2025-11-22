# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .transaction import Transaction

__all__ = ["PaginatedTransactions"]


class PaginatedTransactions(BaseModel):
    data: Optional[List[Transaction]] = None

    limit: Optional[int] = None
    """The maximum number of items returned per page."""

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)
    """The offset to use for the next page of results. Null if no more pages."""

    offset: Optional[int] = None
    """The starting index of the list for pagination."""

    total: Optional[int] = None
    """The total number of available items."""
