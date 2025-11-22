# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .financial_anomaly import FinancialAnomaly

__all__ = ["AnomalyListResponse"]


class AnomalyListResponse(BaseModel):
    limit: int
    """The maximum number of items returned in the current page."""

    offset: int
    """The number of items skipped before the current page."""

    total: int
    """The total number of items available across all pages."""

    data: Optional[List[FinancialAnomaly]] = None

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)
    """The offset for the next page of results, if available. Null if no more pages."""
