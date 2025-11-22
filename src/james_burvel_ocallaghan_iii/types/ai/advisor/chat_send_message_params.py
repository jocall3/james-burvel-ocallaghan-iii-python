# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ChatSendMessageParams", "FunctionResponse"]


class ChatSendMessageParams(TypedDict, total=False):
    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]
    """The ID of the ongoing conversation session."""

    function_response: Annotated[Optional[FunctionResponse], PropertyInfo(alias="functionResponse")]
    """
    Optional: The output from a tool/function call that the AI previously requested.
    """

    message: Optional[str]
    """The user's textual input to the AI Advisor."""


class FunctionResponse(TypedDict, total=False):
    name: Required[str]
    """The name of the tool/function that was called."""

    response: Required[object]
    """The JSON output returned by the execution of the tool/function."""

    call_id: Annotated[Optional[str], PropertyInfo(alias="callId")]
    """Optional: The `id` of the function call this response corresponds to."""
