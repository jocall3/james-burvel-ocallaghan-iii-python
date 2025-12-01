# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LoanOffer"]


class LoanOffer(BaseModel):
    amount: float
    """The offered loan amount."""

    expiration_date: date = FieldInfo(alias="expirationDate")
    """Date the offer expires."""

    interest_rate: float = FieldInfo(alias="interestRate")
    """Annual interest rate offered (as a percentage)."""

    is_pre_approved: bool = FieldInfo(alias="isPreApproved")
    """Indicates if this is a pre-approved offer."""

    offer_id: str = FieldInfo(alias="offerId")
    """Unique identifier for the loan offer."""

    offer_type: Literal["personal_loan", "auto_loan", "mortgage", "credit_line", "microloan"] = FieldInfo(
        alias="offerType"
    )
    """Type of loan being offered."""

    ai_personalization_score: Optional[float] = FieldInfo(alias="aiPersonalizationScore", default=None)
    """AI's score for how well this offer is personalized to the user (0-1)."""

    monthly_payment: Optional[float] = FieldInfo(alias="monthlyPayment", default=None)
    """Estimated monthly payment (if applicable)."""

    origination_fee: Optional[float] = FieldInfo(alias="originationFee", default=None)
    """Any origination fees for the loan."""

    repayment_term_months: Optional[int] = FieldInfo(alias="repaymentTermMonths", default=None)
    """Repayment term in months (if applicable)."""

    terms_and_conditions_url: Optional[str] = FieldInfo(alias="termsAndConditionsUrl", default=None)
    """URL to the full terms and conditions of the loan offer."""

    total_repayable: Optional[float] = FieldInfo(alias="totalRepayable", default=None)
    """Total amount repayable over the loan term."""
