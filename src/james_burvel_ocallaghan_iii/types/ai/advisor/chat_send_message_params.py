# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ChatSendMessageParams", "FunctionResponse"]


class ChatSendMessageParams(TypedDict, total=False):
    message: Required[str]
    """The user's natural language input to the AI Advisor."""

    function_response: Annotated[Optional[FunctionResponse], PropertyInfo(alias="functionResponse")]
    """
    Optional: The output from a tool function that the AI previously requested to be
    executed by the client.
    """

    session_id: Annotated[Optional[str], PropertyInfo(alias="sessionId")]
    """Optional: The ID of an ongoing conversation session to maintain context."""


class FunctionResponse(TypedDict, total=False):
    name: str
    """The name of the function that was called."""

    response: object
    """The JSON object containing the result of the function call."""
