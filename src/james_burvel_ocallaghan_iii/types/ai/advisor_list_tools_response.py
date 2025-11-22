# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AdvisorListToolsResponse", "AdvisorListToolsResponseItem"]


class AdvisorListToolsResponseItem(BaseModel):
    description: str
    """A description of what the AI tool does."""

    name: str
    """The programmatic name of the AI tool."""

    parameters: object
    """A JSON schema object defining the input parameters for the tool."""

    access_scope: Optional[str] = FieldInfo(alias="accessScope", default=None)
    """The OAuth2 scope required to execute this tool, if applicable."""


AdvisorListToolsResponse: TypeAlias = List[AdvisorListToolsResponseItem]
