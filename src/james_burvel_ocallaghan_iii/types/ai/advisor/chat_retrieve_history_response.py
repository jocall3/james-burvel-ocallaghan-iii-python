# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .ai_function_call import AIFunctionCall

__all__ = ["ChatRetrieveHistoryResponse", "Data", "DataToolOutput"]


class DataToolOutput(BaseModel):
    name: str
    """The name of the tool/function that was called."""

    response: object
    """The JSON output returned by the execution of the tool/function."""

    call_id: Optional[str] = FieldInfo(alias="callId", default=None)
    """Optional: The `id` of the function call this response corresponds to."""


class Data(BaseModel):
    content: str
    """The text content of the message."""

    role: Literal["user", "assistant"]
    """The sender of the message."""

    timestamp: datetime
    """The timestamp when the message was sent."""

    tool_calls: Optional[List[AIFunctionCall]] = FieldInfo(alias="toolCalls", default=None)
    """Optional: Tool calls made by the assistant within this message."""

    tool_outputs: Optional[List[DataToolOutput]] = FieldInfo(alias="toolOutputs", default=None)
    """Optional: Tool outputs provided by the user within this message."""


class ChatRetrieveHistoryResponse(BaseModel):
    data: List[Data]
    """The list of chat messages for the current page."""

    limit: int
    """The maximum number of items returned per page."""

    offset: int
    """The starting index of the list for pagination."""

    total: int
    """The total number of available items."""

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)
    """The offset to use for the next page of results. Null if no more pages."""
