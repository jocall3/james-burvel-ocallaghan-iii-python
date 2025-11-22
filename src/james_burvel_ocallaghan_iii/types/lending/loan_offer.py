# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LoanOffer"]


class LoanOffer(BaseModel):
    ai_personalization_score: Optional[float] = FieldInfo(alias="aiPersonalizationScore", default=None)
    """
    AI's score (0-1) indicating how well the offer is tailored to the user's
    needs/profile.
    """

    amount: float
    """The principal amount of the loan offered."""

    expiration_date: date = FieldInfo(alias="expirationDate")
    """Date the offer expires."""

    interest_rate: float = FieldInfo(alias="interestRate")
    """The annual interest rate (APR)."""

    is_pre_approved: bool = FieldInfo(alias="isPreApproved")
    """True if this is a pre-approved offer."""

    offer_id: str = FieldInfo(alias="offerId")
    """Unique identifier for the loan offer."""

    offer_type: Literal["personal_loan", "credit_line", "mortgage", "auto_loan", "student_loan"] = FieldInfo(
        alias="offerType"
    )
    """Type of loan being offered."""

    monthly_payment: Optional[float] = FieldInfo(alias="monthlyPayment", default=None)
    """Estimated monthly payment."""

    origination_fee: Optional[float] = FieldInfo(alias="originationFee", default=None)
    """Any origination fees associated with the loan."""

    repayment_term_months: Optional[int] = FieldInfo(alias="repaymentTermMonths", default=None)
    """Repayment term in months, if applicable."""

    total_repayable: Optional[float] = FieldInfo(alias="totalRepayable", default=None)
    """Total amount repayable over the life of the loan."""
