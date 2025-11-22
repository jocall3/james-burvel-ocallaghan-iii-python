# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .loan_offer import LoanOffer

__all__ = ["LoanApplicationStatus", "AIUnderwritingResult"]


class AIUnderwritingResult(BaseModel):
    ai_confidence: Optional[float] = FieldInfo(alias="aiConfidence", default=None)

    decision: Optional[Literal["approved", "declined"]] = None

    max_approved_amount: Optional[float] = FieldInfo(alias="maxApprovedAmount", default=None)

    reason: Optional[str] = None

    recommended_interest_rate: Optional[float] = FieldInfo(alias="recommendedInterestRate", default=None)


class LoanApplicationStatus(BaseModel):
    application_date: datetime = FieldInfo(alias="applicationDate")
    """Date and time the application was submitted."""

    application_id: str = FieldInfo(alias="applicationId")
    """Unique identifier for the loan application."""

    loan_amount_requested: float = FieldInfo(alias="loanAmountRequested")
    """The original loan amount requested by the user."""

    loan_purpose: str = FieldInfo(alias="loanPurpose")
    """The purpose of the loan."""

    status: Literal["underwriting", "approved", "declined", "withdrawn"]
    """Current status of the loan application."""

    ai_underwriting_result: Optional[AIUnderwritingResult] = FieldInfo(alias="aiUnderwritingResult", default=None)
    """Result of the AI's underwriting process."""

    last_updated: Optional[datetime] = FieldInfo(alias="lastUpdated", default=None)
    """Timestamp when the application status was last updated."""

    next_steps: Optional[str] = FieldInfo(alias="nextSteps", default=None)
    """Next steps for the user based on the application status."""

    offer_details: Optional[LoanOffer] = FieldInfo(alias="offerDetails", default=None)
    """Details of the approved loan offer, if applicable."""
