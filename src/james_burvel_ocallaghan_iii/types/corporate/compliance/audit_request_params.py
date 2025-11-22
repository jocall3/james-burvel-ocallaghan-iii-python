# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["AuditRequestParams"]


class AuditRequestParams(TypedDict, total=False):
    audit_scope: Required[
        Annotated[
            Literal[
                "all_transactions", "corporate_cards", "international_payments", "user_onboarding", "specific_accounts"
            ],
            PropertyInfo(alias="auditScope"),
        ]
    ]
    """The scope of the compliance audit."""

    end_date: Required[Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]]
    """End date for the audit period (inclusive)."""

    regulatory_frameworks: Required[
        Annotated[
            List[Literal["AML", "KYC", "PCI-DSS", "GDPR", "CCPA", "SOX"]], PropertyInfo(alias="regulatoryFrameworks")
        ]
    ]
    """List of regulatory frameworks to audit against."""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]]
    """Start date for the audit period (inclusive)."""

    specific_account_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="specificAccountIds")]
    """
    Optional: List of specific account IDs to include if `auditScope` is
    'specific_accounts'.
    """
