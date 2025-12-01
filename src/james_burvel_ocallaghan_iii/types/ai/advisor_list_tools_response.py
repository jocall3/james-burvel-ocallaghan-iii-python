# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AdvisorListToolsResponse", "Data", "DataParameters"]


class DataParameters(BaseModel):
    properties: Optional[object] = None

    required: Optional[List[object]] = None

    type: Optional[Literal["object"]] = None


class Data(BaseModel):
    access_scope: object = FieldInfo(alias="accessScope")
    """The OAuth2 scope required to execute this tool."""

    description: object
    """A description of what the tool does."""

    name: object
    """The unique name of the AI tool (function name)."""

    parameters: DataParameters
    """OpenAPI schema object defining the input parameters for the tool function."""


class AdvisorListToolsResponse(BaseModel):
    limit: object
    """The maximum number of items returned in the current page."""

    offset: object
    """The number of items skipped before the current page."""

    total: object
    """The total number of items available across all pages."""

    data: Optional[List[Data]] = None

    next_offset: Optional[object] = FieldInfo(alias="nextOffset", default=None)
    """The offset for the next page of results, if available. Null if no more pages."""
