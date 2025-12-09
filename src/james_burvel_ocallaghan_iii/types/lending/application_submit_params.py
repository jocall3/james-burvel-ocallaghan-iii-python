# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ApplicationSubmitParams", "CoApplicant"]


class ApplicationSubmitParams(TypedDict, total=False):
    loan_amount: Required[Annotated[object, PropertyInfo(alias="loanAmount")]]
    """The desired loan amount."""

    loan_purpose: Required[
        Annotated[
            Literal["home_improvement", "debt_consolidation", "medical_expense", "education", "auto_purchase", "other"],
            PropertyInfo(alias="loanPurpose"),
        ]
    ]
    """The purpose of the loan."""

    repayment_term_months: Required[Annotated[object, PropertyInfo(alias="repaymentTermMonths")]]
    """The desired repayment term in months."""

    additional_notes: Annotated[object, PropertyInfo(alias="additionalNotes")]
    """Optional notes or details for the application."""

    co_applicant: Annotated[CoApplicant, PropertyInfo(alias="coApplicant")]
    """Optional: Details of a co-applicant for the loan."""


class CoApplicant(TypedDict, total=False):
    """Optional: Details of a co-applicant for the loan."""

    email: object

    income: object

    name: object
