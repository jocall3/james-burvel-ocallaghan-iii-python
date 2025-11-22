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

    category: Literal["technology", "market", "finance", "team", "operations", "legal"]
    """The category the question relates to."""

    is_required: bool = FieldInfo(alias="isRequired")
    """Indicates if answering this question is mandatory to proceed."""

    question: str
    """The full question asked by Quantum Weaver AI."""


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
    """The current stage of the business pitch in the incubation process."""

    status_message: str = FieldInfo(alias="statusMessage")
    """A human-readable message detailing the current status."""

    estimated_funding_offer: Optional[float] = FieldInfo(alias="estimatedFundingOffer", default=None)
    """If approved, the estimated seed funding amount offered (in USD)."""

    feedback_summary: Optional[str] = FieldInfo(alias="feedbackSummary", default=None)
    """A high-level summary of AI feedback if available."""

    next_steps: Optional[str] = FieldInfo(alias="nextSteps", default=None)
    """Recommended next actions for the user."""

    questions: Optional[List[Question]] = None
    """Specific questions from the AI that require user input to proceed."""
