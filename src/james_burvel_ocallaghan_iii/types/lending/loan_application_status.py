# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .loan_offer import LoanOffer

__all__ = ["LoanApplicationStatus", "AIUnderwritingResult"]


class AIUnderwritingResult(BaseModel):
    ai_confidence: float = FieldInfo(alias="aiConfidence")
    """AI's confidence score (0-1) in its underwriting decision."""

    decision: Literal["approved", "declined", "referred_to_human"]
    """The AI's underwriting decision."""

    reason: str
    """The AI's reasoning for the decision."""

    max_approved_amount: Optional[float] = FieldInfo(alias="maxApprovedAmount", default=None)
    """The maximum loan amount the AI would approve."""

    recommended_interest_rate: Optional[float] = FieldInfo(alias="recommendedInterestRate", default=None)
    """AI-recommended interest rate."""


class LoanApplicationStatus(BaseModel):
    application_date: datetime = FieldInfo(alias="applicationDate")
    """Timestamp when the application was submitted."""

    application_id: str = FieldInfo(alias="applicationId")
    """Unique identifier for the loan application."""

    loan_amount_requested: float = FieldInfo(alias="loanAmountRequested")
    """The original requested loan amount."""

    loan_purpose: Literal[
        "home_improvement", "debt_consolidation", "medical_expenses", "education", "business", "vehicle", "other"
    ] = FieldInfo(alias="loanPurpose")
    """The stated purpose of the loan."""

    status: Literal["underwriting", "approved", "declined", "pending_documents", "funded"]
    """Current status of the loan application."""

    ai_underwriting_result: Optional[AIUnderwritingResult] = FieldInfo(alias="aiUnderwritingResult", default=None)
    """Results of the AI-powered underwriting, available upon decision."""

    next_steps: Optional[str] = FieldInfo(alias="nextSteps", default=None)
    """Actionable next steps for the user."""

    offer_details: Optional[LoanOffer] = FieldInfo(alias="offerDetails", default=None)
    """Details of the approved loan offer, if applicable."""

    rejection_reason: Optional[str] = FieldInfo(alias="rejectionReason", default=None)
    """If declined, the reason for the rejection."""
