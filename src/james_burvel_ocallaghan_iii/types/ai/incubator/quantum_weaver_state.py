# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["QuantumWeaverState", "Question"]


class Question(BaseModel):
    id: str
    """Unique identifier for the question."""

    category: Literal["technology", "market", "finance", "team", "legal", "operations"]
    """The category of the question."""

    is_required: bool = FieldInfo(alias="isRequired")
    """Indicates if answering this question is mandatory to proceed."""

    question: str
    """The question posed by Quantum Weaver."""


class QuantumWeaverState(BaseModel):
    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the pitch status was last updated."""

    pitch_id: str = FieldInfo(alias="pitchId")
    """Unique identifier for the business pitch."""

    stage: Literal[
        "initial_review",
        "ai_analysis",
        "feedback_required",
        "test_phase",
        "final_review",
        "approved_for_funding",
        "rejected",
        "incubated_graduated",
    ]
    """Current stage of the business pitch within Quantum Weaver's incubation process."""

    status_message: str = FieldInfo(alias="statusMessage")
    """A human-readable message about the current status."""

    estimated_funding_offer: Optional[float] = FieldInfo(alias="estimatedFundingOffer", default=None)
    """Quantum Weaver's estimated funding offer, if in advanced stages."""

    feedback_summary: Optional[str] = FieldInfo(alias="feedbackSummary", default=None)
    """A summary of AI-generated feedback, if available and concise enough."""

    next_steps: Optional[str] = FieldInfo(alias="nextSteps", default=None)
    """Actionable next steps for the entrepreneur."""

    questions: Optional[List[Question]] = None
    """A list of questions from Quantum Weaver requiring entrepreneur's input."""
