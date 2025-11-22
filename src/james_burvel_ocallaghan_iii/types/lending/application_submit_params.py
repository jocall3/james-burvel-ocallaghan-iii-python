# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ApplicationSubmitParams", "CoApplicant"]


class ApplicationSubmitParams(TypedDict, total=False):
    loan_amount: Required[Annotated[float, PropertyInfo(alias="loanAmount")]]
    """The desired loan amount."""

    loan_purpose: Required[
        Annotated[
            Literal[
                "debt_consolidation", "home_improvement", "medical_expense", "education", "business_startup", "other"
            ],
            PropertyInfo(alias="loanPurpose"),
        ]
    ]
    """The purpose for which the loan is requested."""

    repayment_term_months: Required[Annotated[int, PropertyInfo(alias="repaymentTermMonths")]]
    """The desired repayment term in months."""

    additional_notes: Annotated[Optional[str], PropertyInfo(alias="additionalNotes")]
    """Any additional relevant information for the loan application."""

    co_applicant: Annotated[Optional[CoApplicant], PropertyInfo(alias="coApplicant")]
    """Optional details for a co-applicant."""

    desired_interest_rate: Annotated[Optional[float], PropertyInfo(alias="desiredInterestRate")]
    """
    Optional: User's desired interest rate (AI will try to match or offer best
    possible).
    """


class CoApplicant(TypedDict, total=False):
    credit_score: Annotated[Optional[int], PropertyInfo(alias="creditScore")]

    email: str

    income: float

    name: str
