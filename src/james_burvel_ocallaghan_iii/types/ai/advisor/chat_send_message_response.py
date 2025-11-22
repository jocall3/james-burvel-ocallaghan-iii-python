# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .ai_function_call import AIFunctionCall
from ...transactions.ai_insight import AIInsight

__all__ = ["ChatSendMessageResponse"]


class ChatSendMessageResponse(BaseModel):
    session_id: str = FieldInfo(alias="sessionId")
    """The ID of the conversation session."""

    function_calls: Optional[List[AIFunctionCall]] = FieldInfo(alias="functionCalls", default=None)
    """Optional: A list of tool/function calls the AI wants the client to execute."""

    proactive_insights: Optional[List[AIInsight]] = FieldInfo(alias="proactiveInsights", default=None)
    """
    Optional: A list of AI-generated insights or alerts related to the conversation.
    """

    text: Optional[str] = None
    """The AI Advisor's natural language response."""
