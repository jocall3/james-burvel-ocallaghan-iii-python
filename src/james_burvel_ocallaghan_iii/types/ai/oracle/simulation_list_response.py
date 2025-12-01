# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SimulationListResponse", "Data"]


class Data(BaseModel):
    creation_date: datetime = FieldInfo(alias="creationDate")
    """Timestamp when the simulation was initiated."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the simulation status or results were last updated."""

    simulation_id: str = FieldInfo(alias="simulationId")
    """Unique identifier for the simulation."""

    status: Literal["processing", "completed", "failed"]
    """Current status of the simulation."""

    summary: str
    """A brief summary of what the simulation evaluated."""

    title: str
    """A user-friendly title for the simulation."""


class SimulationListResponse(BaseModel):
    limit: int
    """The maximum number of items returned in the current page."""

    offset: int
    """The number of items skipped before the current page."""

    total: int
    """The total number of items available across all pages."""

    data: Optional[List[Data]] = None

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)
    """The offset for the next page of results, if available. Null if no more pages."""
