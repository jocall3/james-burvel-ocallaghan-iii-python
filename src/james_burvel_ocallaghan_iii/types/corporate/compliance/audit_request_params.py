# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AuditRequestParams"]


class AuditRequestParams(TypedDict, total=False):
    audit_scope: Required[
        Annotated[
            Literal[
                "all_transactions", "corporate_cards", "specific_accounts", "international_payments", "user_onboarding"
            ],
            PropertyInfo(alias="auditScope"),
        ]
    ]
    """The scope of the compliance audit."""

    end_date: Required[Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]]
    """The end date for the audit period (inclusive)."""

    regulatory_frameworks: Required[
        Annotated[
            List[Literal["AML", "KYC", "PCI-DSS", "GDPR", "PSD2", "SOX", "CCPA"]],
            PropertyInfo(alias="regulatoryFrameworks"),
        ]
    ]
    """List of regulatory frameworks against which to audit."""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]]
    """The start date for the audit period (inclusive)."""

    additional_notes: Annotated[Optional[str], PropertyInfo(alias="additionalNotes")]
    """Any additional notes or specific areas of focus for the audit."""
