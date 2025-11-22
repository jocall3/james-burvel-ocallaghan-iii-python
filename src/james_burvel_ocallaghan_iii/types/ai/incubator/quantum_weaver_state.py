# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["QuantumWeaverState", "Question"]


class Question(BaseModel):
    id: Optional[str] = None

    category: Optional[str] = None

    is_required: Optional[bool] = FieldInfo(alias="isRequired", default=None)

    question: Optional[str] = None


class QuantumWeaverState(BaseModel):
    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the pitch status was last updated."""

    pitch_id: str = FieldInfo(alias="pitchId")
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
    """
    Current stage of the business pitch within Quantum Weaver's incubation pipeline.
    """

    status_message: str = FieldInfo(alias="statusMessage")
    """A descriptive message about the current status of the pitch."""

    estimated_funding_offer: Optional[float] = FieldInfo(alias="estimatedFundingOffer", default=None)
    """Estimated seed funding amount offered by Quantum Weaver (if applicable)."""

    feedback_summary: Optional[str] = FieldInfo(alias="feedbackSummary", default=None)
    """A summary of AI-generated feedback or key findings from the current stage."""

    next_steps: Optional[str] = FieldInfo(alias="nextSteps", default=None)
    """Guidance on what the entrepreneur should do next."""

    questions: Optional[List[Question]] = None
    """
    A list of specific questions from Quantum Weaver requiring the entrepreneur's
    input.
    """
