# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ChatRetrieveHistoryResponse", "Data"]


class Data(BaseModel):
    content: str
    """The content of the message."""

    role: Literal["user", "assistant", "system"]
    """The role of the message sender."""

    timestamp: datetime
    """The timestamp when the message was sent/received."""

    metadata: Optional[Dict[str, object]] = None
    """
    Optional: Any additional metadata associated with the message, e.g., tool calls,
    insights.
    """


class ChatRetrieveHistoryResponse(BaseModel):
    data: List[Data]
    """The list of chat messages for the current page."""

    limit: int
    """The maximum number of items returned per page."""

    offset: int
    """The starting index of the list for pagination."""

    total: int
    """The total number of available items across all pages."""

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)
    """The offset to use for the next page of results, if available."""
