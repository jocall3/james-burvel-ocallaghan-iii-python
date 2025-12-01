# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["QuantumWeaverState", "Question"]


class Question(BaseModel):
    id: Optional[object] = None

    category: Optional[object] = None

    is_required: Optional[object] = FieldInfo(alias="isRequired", default=None)

    question: Optional[object] = None


class QuantumWeaverState(BaseModel):
    last_updated: object = FieldInfo(alias="lastUpdated")
    """Timestamp of the last status update."""

    next_steps: object = FieldInfo(alias="nextSteps")
    """Guidance on the next actions for the user."""

    pitch_id: object = FieldInfo(alias="pitchId")
    """Unique identifier for the business pitch."""

    stage: Literal[
        "submitted",
        "initial_review",
        "ai_analysis",
        "feedback_required",
        "test_phase",
        "final_review",
        "approved_for_funding",
        "rejected",
        "incubated_graduated",
    ]
    """Current stage of the business pitch in the incubation process."""

    status_message: object = FieldInfo(alias="statusMessage")
    """A human-readable status message."""

    estimated_funding_offer: Optional[object] = FieldInfo(alias="estimatedFundingOffer", default=None)
    """AI's estimated funding offer, if the pitch progresses."""

    feedback_summary: Optional[object] = FieldInfo(alias="feedbackSummary", default=None)
    """A summary of AI-generated feedback, if applicable."""

    questions: Optional[List[Question]] = None
    """List of questions from Quantum Weaver requiring the user's input."""
