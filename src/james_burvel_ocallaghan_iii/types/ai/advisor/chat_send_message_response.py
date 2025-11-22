# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .ai_function_call import AIFunctionCall
from ...transactions.ai_insight import AIInsight

__all__ = ["ChatSendMessageResponse"]


class ChatSendMessageResponse(BaseModel):
    session_id: str = FieldInfo(alias="sessionId")
    """The ID of the current conversation session."""

    text: str
    """The AI Advisor's natural language response."""

    function_calls: Optional[List[AIFunctionCall]] = FieldInfo(alias="functionCalls", default=None)
    """If the AI intends to use a tool, this provides the function call details."""

    proactive_insights: Optional[List[AIInsight]] = FieldInfo(alias="proactiveInsights", default=None)
    """AI-generated proactive insights or recommendations."""
