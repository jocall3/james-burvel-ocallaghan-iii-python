# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ChatSendMessageParams", "FunctionResponse"]


class ChatSendMessageParams(TypedDict, total=False):
    message: Required[str]
    """The user's natural language message or query for the AI Advisor."""

    function_response: Annotated[Optional[FunctionResponse], PropertyInfo(alias="functionResponse")]
    """
    Optional: If the user is responding to a tool call, this contains the output
    from the tool's execution.
    """

    session_id: Annotated[Optional[str], PropertyInfo(alias="sessionId")]
    """Optional: The ID of an ongoing conversation session to maintain context."""


class FunctionResponse(TypedDict, total=False):
    name: str
    """The name of the tool function that was executed."""

    response: object
    """The structured output/result from the tool function execution."""
