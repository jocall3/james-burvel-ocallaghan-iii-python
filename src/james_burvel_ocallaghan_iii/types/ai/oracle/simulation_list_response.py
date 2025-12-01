# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SimulationListResponse", "Data"]


class Data(BaseModel):
    creation_date: object = FieldInfo(alias="creationDate")
    """Timestamp when the simulation was initiated."""

    last_updated: object = FieldInfo(alias="lastUpdated")
    """Timestamp when the simulation status or results were last updated."""

    simulation_id: object = FieldInfo(alias="simulationId")
    """Unique identifier for the simulation."""

    status: Literal["processing", "completed", "failed"]
    """Current status of the simulation."""

    summary: object
    """A brief summary of what the simulation evaluated."""

    title: object
    """A user-friendly title for the simulation."""


class SimulationListResponse(BaseModel):
    limit: object
    """The maximum number of items returned in the current page."""

    offset: object
    """The number of items skipped before the current page."""

    total: object
    """The total number of items available across all pages."""

    data: Optional[List[Data]] = None

    next_offset: Optional[object] = FieldInfo(alias="nextOffset", default=None)
    """The offset for the next page of results, if available. Null if no more pages."""
