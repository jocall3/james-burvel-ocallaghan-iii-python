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
                "home_improvement",
                "debt_consolidation",
                "medical_expenses",
                "education",
                "business",
                "vehicle",
                "other",
            ],
            PropertyInfo(alias="loanPurpose"),
        ]
    ]
    """The purpose of the loan."""

    repayment_term_months: Required[Annotated[int, PropertyInfo(alias="repaymentTermMonths")]]
    """Desired repayment term in months."""

    additional_notes: Annotated[Optional[str], PropertyInfo(alias="additionalNotes")]
    """Any additional information for the loan application."""

    co_applicant: Annotated[Optional[CoApplicant], PropertyInfo(alias="coApplicant")]
    """Optional details if there is a co-applicant."""


class CoApplicant(TypedDict, total=False):
    email: Required[str]
    """Email of the co-applicant."""

    income: Required[float]
    """Annual income of the co-applicant."""

    name: Required[str]
    """Full name of the co-applicant."""

    credit_score: Annotated[Optional[int], PropertyInfo(alias="creditScore")]
    """Optional: Credit score of the co-applicant."""
