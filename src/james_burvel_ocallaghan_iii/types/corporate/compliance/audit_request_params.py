# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AuditRequestParams"]


class AuditRequestParams(TypedDict, total=False):
    audit_scope: Required[
        Annotated[
            Literal["all_transactions", "specific_accounts", "specific_cards", "all_users"],
            PropertyInfo(alias="auditScope"),
        ]
    ]
    """The scope of the audit (e.g., all transactions, specific accounts)."""

    end_date: Required[Annotated[object, PropertyInfo(alias="endDate")]]
    """End date for the audit period (inclusive)."""

    regulatory_frameworks: Required[
        Annotated[
            List[Literal["AML", "KYC", "PCI-DSS", "GDPR", "CCPA", "SOX", "OFAC"]],
            PropertyInfo(alias="regulatoryFrameworks"),
        ]
    ]
    """List of regulatory frameworks against which to audit."""

    start_date: Required[Annotated[object, PropertyInfo(alias="startDate")]]
    """Start date for the audit period (inclusive)."""

    additional_context: Annotated[object, PropertyInfo(alias="additionalContext")]
    """Optional: Any additional context or specific areas of concern for the AI."""
