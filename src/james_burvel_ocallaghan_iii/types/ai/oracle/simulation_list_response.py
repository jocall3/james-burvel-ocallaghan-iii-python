# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SimulationListResponse", "Data"]


class Data(BaseModel):
    creation_date: datetime = FieldInfo(alias="creationDate")
    """Timestamp when the simulation was requested."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the simulation status or results were last updated."""

    simulation_id: str = FieldInfo(alias="simulationId")
    """Unique identifier for the simulation."""

    status: Literal["queued", "processing", "completed", "failed"]
    """Current status of the simulation."""

    summary: str
    """A brief summary of what the simulation evaluated."""

    title: str
    """A short, descriptive title for the simulation."""


class SimulationListResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None
    """The maximum number of items returned per page."""

    offset: Optional[int] = None
    """The starting index of the list for pagination."""

    total: Optional[int] = None
    """The total number of available items."""
