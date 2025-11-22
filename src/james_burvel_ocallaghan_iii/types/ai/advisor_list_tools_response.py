# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AdvisorListToolsResponse", "AdvisorListToolsResponseItem"]


class AdvisorListToolsResponseItem(BaseModel):
    description: str
    """A description of what the tool does."""

    name: str
    """The unique name of the AI tool."""

    parameters: object
    """An OpenAPI schema object describing the input parameters for the tool."""

    access_scope: Optional[str] = FieldInfo(alias="accessScope", default=None)
    """The required OAuth2 scope to invoke this tool."""


AdvisorListToolsResponse: TypeAlias = List[AdvisorListToolsResponseItem]
