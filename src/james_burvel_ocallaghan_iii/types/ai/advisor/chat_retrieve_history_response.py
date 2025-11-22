# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .ai_function_call import AIFunctionCall

__all__ = ["ChatRetrieveHistoryResponse", "Data"]


class Data(BaseModel):
    content: str
    """The content of the message."""

    role: Literal["user", "assistant", "tool"]
    """The role of the sender of the message."""

    timestamp: datetime
    """The timestamp when the message was sent/generated."""

    function_call: Optional[AIFunctionCall] = FieldInfo(alias="functionCall", default=None)
    """If the role is 'assistant' and this is a tool call."""

    function_response: Optional[object] = FieldInfo(alias="functionResponse", default=None)
    """If the role is 'tool', the output of the function call."""


class ChatRetrieveHistoryResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None
    """The maximum number of items returned per page."""

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)
    """The offset to use for the next page of results. Null if no more pages."""

    offset: Optional[int] = None
    """The starting index of the list for pagination."""

    total: Optional[int] = None
    """The total number of available items."""
