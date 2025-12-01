# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .loan_offer import LoanOffer

__all__ = ["LoanApplicationStatus", "AIUnderwritingResult"]


class AIUnderwritingResult(BaseModel):
    ai_confidence: object = FieldInfo(alias="aiConfidence")
    """AI's confidence in its underwriting decision (0-1)."""

    decision: Literal["approved", "declined", "referred_to_human"]
    """The AI's underwriting decision."""

    reason: object
    """Reasoning for the AI's decision."""

    max_approved_amount: Optional[object] = FieldInfo(alias="maxApprovedAmount", default=None)
    """The maximum amount the AI is willing to approve."""

    recommended_interest_rate: Optional[object] = FieldInfo(alias="recommendedInterestRate", default=None)
    """The interest rate recommended by the AI."""


class LoanApplicationStatus(BaseModel):
    application_date: object = FieldInfo(alias="applicationDate")
    """Timestamp when the application was submitted."""

    application_id: object = FieldInfo(alias="applicationId")
    """Unique identifier for the loan application."""

    loan_amount_requested: object = FieldInfo(alias="loanAmountRequested")
    """The amount originally requested in the application."""

    loan_purpose: Literal[
        "home_improvement", "debt_consolidation", "medical_expense", "education", "auto_purchase", "other"
    ] = FieldInfo(alias="loanPurpose")
    """The purpose of the loan."""

    next_steps: object = FieldInfo(alias="nextSteps")
    """Guidance on the next actions for the user."""

    status: Literal["submitted", "underwriting", "approved", "declined", "pending_acceptance", "funded", "cancelled"]
    """Current status of the loan application."""

    ai_underwriting_result: Optional[AIUnderwritingResult] = FieldInfo(alias="aiUnderwritingResult", default=None)

    offer_details: Optional[LoanOffer] = FieldInfo(alias="offerDetails", default=None)
