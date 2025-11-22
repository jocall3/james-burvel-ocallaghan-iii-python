# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LoanOffer"]


class LoanOffer(BaseModel):
    ai_personalization_score: float = FieldInfo(alias="aiPersonalizationScore")
    """
    AI's score indicating how well this offer is tailored to the user's financial
    profile.
    """

    amount: float
    """The principal amount of the loan offer."""

    interest_rate: float = FieldInfo(alias="interestRate")
    """Annual interest rate of the loan."""

    is_pre_approved: bool = FieldInfo(alias="isPreApproved")
    """
    True if this is a pre-approved offer, false if it's a response to an
    application.
    """

    offer_id: str = FieldInfo(alias="offerId")
    """Unique identifier for the loan offer."""

    offer_type: Literal["personal_loan", "business_loan", "credit_line", "mortgage", "auto_loan", "microloan"] = (
        FieldInfo(alias="offerType")
    )
    """Type of loan being offered."""

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)
    """Date when the offer expires."""

    monthly_payment: Optional[float] = FieldInfo(alias="monthlyPayment", default=None)
    """Estimated monthly payment."""

    origination_fee: Optional[float] = FieldInfo(alias="originationFee", default=None)
    """Any upfront origination fees."""

    repayment_term_months: Optional[int] = FieldInfo(alias="repaymentTermMonths", default=None)
    """Repayment term in months. Null for credit lines."""

    terms_and_conditions_url: Optional[str] = FieldInfo(alias="termsAndConditionsUrl", default=None)
    """URL to the full terms and conditions of the loan offer."""

    total_repayable: Optional[float] = FieldInfo(alias="totalRepayable", default=None)
    """Total amount repayable over the loan term (principal + interest + fees)."""
