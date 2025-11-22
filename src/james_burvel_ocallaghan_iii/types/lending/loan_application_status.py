# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .loan_offer import LoanOffer

__all__ = ["LoanApplicationStatus", "AIUnderwritingResult"]


class AIUnderwritingResult(BaseModel):
    ai_confidence: Optional[float] = FieldInfo(alias="aiConfidence", default=None)

    decision: Optional[Literal["approved", "declined", "referred"]] = None

    max_approved_amount: Optional[float] = FieldInfo(alias="maxApprovedAmount", default=None)

    reason: Optional[str] = None

    recommended_interest_rate: Optional[float] = FieldInfo(alias="recommendedInterestRate", default=None)


class LoanApplicationStatus(BaseModel):
    application_date: datetime = FieldInfo(alias="applicationDate")
    """Date and time the application was submitted."""

    application_id: str = FieldInfo(alias="applicationId")
    """Unique identifier for the loan application."""

    loan_amount_requested: float = FieldInfo(alias="loanAmountRequested")
    """The amount originally requested in the application."""

    loan_purpose: str = FieldInfo(alias="loanPurpose")
    """The stated purpose of the loan."""

    next_steps: str = FieldInfo(alias="nextSteps")
    """Guidance on what the user should do next."""

    status: Literal["pending", "underwriting", "approved", "declined", "withdrawn", "funded"]
    """Current status of the loan application."""

    ai_underwriting_result: Optional[AIUnderwritingResult] = FieldInfo(alias="aiUnderwritingResult", default=None)
    """Outcome and details from the AI underwriting process."""

    decline_reason_details: Optional[List[str]] = FieldInfo(alias="declineReasonDetails", default=None)
    """Specific reasons for loan decline, adhering to regulatory requirements."""

    offer_details: Optional[LoanOffer] = FieldInfo(alias="offerDetails", default=None)
    """Details of the loan offer if the application is approved."""
