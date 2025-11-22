# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .ai_function_call import AIFunctionCall
from ...transactions.ai_insight import AIInsight

__all__ = ["ChatSendMessageResponse"]


class ChatSendMessageResponse(BaseModel):
    follow_up_questions: Optional[List[str]] = FieldInfo(alias="followUpQuestions", default=None)
    """Suggestions for next conversational turns or clarifications needed by the AI."""

    function_calls: Optional[List[AIFunctionCall]] = FieldInfo(alias="functionCalls", default=None)
    """
    Requests for the client application to execute specific tool functions on behalf
    of the AI.
    """

    proactive_insights: Optional[List[AIInsight]] = FieldInfo(alias="proactiveInsights", default=None)
    """AI-generated proactive insights or recommendations."""

    session_id: Optional[str] = FieldInfo(alias="sessionId", default=None)
    """The ID of the current conversation session."""

    text: Optional[str] = None
    """The AI Advisor's textual response."""
