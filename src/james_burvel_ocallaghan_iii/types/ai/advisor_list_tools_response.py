# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AdvisorListToolsResponse", "Data", "DataParameters", "DataParametersProperties"]


class DataParametersProperties(BaseModel):
    description: Optional[str] = None

    enum: Optional[List[str]] = None

    type: Optional[str] = None


class DataParameters(BaseModel):
    properties: Optional[Dict[str, DataParametersProperties]] = None

    required: Optional[List[str]] = None

    type: Optional[Literal["object"]] = None


class Data(BaseModel):
    access_scope: str = FieldInfo(alias="accessScope")
    """The OAuth2 scope required to execute this tool."""

    description: str
    """A description of what the tool does."""

    name: str
    """The unique name of the AI tool (function name)."""

    parameters: DataParameters
    """OpenAPI schema object defining the input parameters for the tool function."""


class AdvisorListToolsResponse(BaseModel):
    limit: int
    """The maximum number of items returned in the current page."""

    offset: int
    """The number of items skipped before the current page."""

    total: int
    """The total number of items available across all pages."""

    data: Optional[List[Data]] = None

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)
    """The offset for the next page of results, if available. Null if no more pages."""
