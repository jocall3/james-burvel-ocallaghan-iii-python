# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LoanOffer"]


class LoanOffer(BaseModel):
    amount: float
    """The principal amount of the loan offered."""

    expiration_date: date = FieldInfo(alias="expirationDate")
    """Date the offer expires."""

    interest_rate: float = FieldInfo(alias="interestRate")
    """Annual interest rate offered."""

    is_pre_approved: bool = FieldInfo(alias="isPreApproved")
    """True if this is a pre-approved offer, false if from an application."""

    offer_id: str = FieldInfo(alias="offerId")
    """Unique identifier for the loan offer."""

    offer_type: Literal["personal_loan", "credit_line", "mortgage", "auto_loan", "microloan"] = FieldInfo(
        alias="offerType"
    )
    """Type of loan offered."""

    ai_personalization_score: Optional[float] = FieldInfo(alias="aiPersonalizationScore", default=None)
    """
    AI's score for how well this offer matches the user's financial profile and
    needs.
    """

    monthly_payment: Optional[float] = FieldInfo(alias="monthlyPayment", default=None)
    """Estimated monthly payment (if applicable)."""

    origination_fee: Optional[float] = FieldInfo(alias="originationFee", default=None)
    """Any one-time origination fee."""

    repayment_term_months: Optional[int] = FieldInfo(alias="repaymentTermMonths", default=None)
    """Repayment term in months (if applicable)."""

    total_repayable: Optional[float] = FieldInfo(alias="totalRepayable", default=None)
    """Total amount repayable over the life of the loan."""
