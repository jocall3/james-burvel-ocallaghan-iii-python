# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ChatSendMessageParams", "FunctionResponse"]


class ChatSendMessageParams(TypedDict, total=False):
    function_response: Annotated[Optional[FunctionResponse], PropertyInfo(alias="functionResponse")]
    """
    Optional: The output from a tool function that the AI previously requested to be
    executed.
    """

    message: str
    """The user's textual input to the AI Advisor."""

    session_id: Annotated[Optional[str], PropertyInfo(alias="sessionId")]
    """Optional: Session ID to continue a conversation.

    If omitted, a new session is started.
    """


class FunctionResponse(TypedDict, total=False):
    name: str
    """The name of the tool function for which this is a response."""

    response: object
    """The JSON output from the execution of the tool function."""
