# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ChatRetrieveHistoryResponse", "Data", "DataFunctionCall", "DataFunctionResponse"]


class DataFunctionCall(BaseModel):
    args: Optional[object] = None

    name: Optional[object] = None


class DataFunctionResponse(BaseModel):
    name: Optional[object] = None

    response: Optional[object] = None


class Data(BaseModel):
    content: object
    """The textual content of the message."""

    role: Literal["user", "assistant", "tool_call", "tool_response"]
    """Role of the speaker (user, assistant, or tool interaction)."""

    timestamp: object
    """Timestamp of the message."""

    function_call: Optional[DataFunctionCall] = FieldInfo(alias="functionCall", default=None)
    """If role is 'tool_call', details of the tool function called by the AI."""

    function_response: Optional[DataFunctionResponse] = FieldInfo(alias="functionResponse", default=None)
    """If role is 'tool_response', the output from the tool function."""


class ChatRetrieveHistoryResponse(BaseModel):
    limit: object
    """The maximum number of items returned in the current page."""

    offset: object
    """The number of items skipped before the current page."""

    total: object
    """The total number of items available across all pages."""

    data: Optional[List[Data]] = None

    next_offset: Optional[object] = FieldInfo(alias="nextOffset", default=None)
    """The offset for the next page of results, if available. Null if no more pages."""
