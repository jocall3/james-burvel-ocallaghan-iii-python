# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .device import Device
from ...._models import BaseModel

__all__ = ["DeviceListResponse"]


class DeviceListResponse(BaseModel):
    limit: object
    """The maximum number of items returned in the current page."""

    offset: object
    """The number of items skipped before the current page."""

    total: object
    """The total number of items available across all pages."""

    data: Optional[List[Device]] = None

    next_offset: Optional[object] = FieldInfo(alias="nextOffset", default=None)
    """The offset for the next page of results, if available. Null if no more pages."""
