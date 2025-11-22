# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .incubator.quantum_weaver_state import QuantumWeaverState

__all__ = ["IncubatorListPitchesResponse"]


class IncubatorListPitchesResponse(BaseModel):
    data: Optional[List[QuantumWeaverState]] = None

    limit: Optional[int] = None
    """The maximum number of items returned per page."""

    offset: Optional[int] = None
    """The starting index of the list for pagination."""

    total: Optional[int] = None
    """The total number of available items."""
