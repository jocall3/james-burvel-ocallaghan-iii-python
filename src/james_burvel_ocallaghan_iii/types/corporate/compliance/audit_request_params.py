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
            Literal["all_transactions", "corporate_cards", "global_payments", "specific_accounts"],
            PropertyInfo(alias="auditScope"),
        ]
    ]
    """The scope of the audit (e.g., all transactions, specific accounts)."""

    end_date: Required[Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]]
    """The end date for the audit period (inclusive)."""

    regulatory_frameworks: Required[
        Annotated[
            List[Literal["AML", "PCI-DSS", "GDPR", "CCPA", "SOX", "internal_policy"]],
            PropertyInfo(alias="regulatoryFrameworks"),
        ]
    ]
    """List of regulatory frameworks or internal policies to audit against."""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]]
    """The start date for the audit period (inclusive)."""

    specific_accounts: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="specificAccounts")]
    """Optional: List of specific account IDs to include in the audit."""
