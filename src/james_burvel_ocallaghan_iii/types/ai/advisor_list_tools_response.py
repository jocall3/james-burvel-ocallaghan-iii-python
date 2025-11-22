# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AdvisorListToolsResponse", "AdvisorListToolsResponseItem"]


class AdvisorListToolsResponseItem(BaseModel):
    access_scope: str = FieldInfo(alias="accessScope")
    """The OAuth2 scope required to execute this tool."""

    description: str
    """A description of what the tool does."""

    name: str
    """The name of the tool function."""

    parameters: object
    """An OpenAPI-compatible schema object for the tool's input parameters."""


AdvisorListToolsResponse: TypeAlias = List[AdvisorListToolsResponseItem]
