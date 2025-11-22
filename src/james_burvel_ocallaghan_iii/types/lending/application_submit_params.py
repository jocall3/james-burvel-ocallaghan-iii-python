# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ApplicationSubmitParams", "CoApplicant", "CollateralDetails"]


class ApplicationSubmitParams(TypedDict, total=False):
    loan_amount: Required[Annotated[float, PropertyInfo(alias="loanAmount")]]
    """The desired loan amount."""

    loan_purpose: Required[
        Annotated[
            Literal[
                "debt_consolidation", "home_improvement", "medical_expenses", "education", "business_startup", "other"
            ],
            PropertyInfo(alias="loanPurpose"),
        ]
    ]
    """The purpose of the loan."""

    repayment_term_months: Required[Annotated[int, PropertyInfo(alias="repaymentTermMonths")]]
    """Desired repayment term in months."""

    additional_notes: Annotated[Optional[str], PropertyInfo(alias="additionalNotes")]
    """Any additional information for the underwriting process."""

    co_applicant: Annotated[Optional[CoApplicant], PropertyInfo(alias="coApplicant")]
    """Optional details for a co-applicant."""

    collateral_details: Annotated[Optional[CollateralDetails], PropertyInfo(alias="collateralDetails")]
    """Optional details about collateral for secured loans."""


class CoApplicant(TypedDict, total=False):
    credit_score: Annotated[Optional[int], PropertyInfo(alias="creditScore")]

    email: str

    income: float

    name: str


class CollateralDetails(TypedDict, total=False):
    description: str

    type: str

    value: float
