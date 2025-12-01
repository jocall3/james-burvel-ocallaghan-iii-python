# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AnomalyListParams"]


class AnomalyListParams(TypedDict, total=False):
    end_date: Annotated[object, PropertyInfo(alias="endDate")]
    """End date for filtering results (inclusive, YYYY-MM-DD)."""

    entity_type: Annotated[
        Literal["PaymentOrder", "Transaction", "Counterparty", "CorporateCard", "Invoice"],
        PropertyInfo(alias="entityType"),
    ]
    """Filter anomalies by the type of financial entity they are related to."""

    limit: object
    """Maximum number of items to return in a single page."""

    offset: object
    """Number of items to skip before starting to collect the result set."""

    severity: Literal["Low", "Medium", "High", "Critical"]
    """Filter anomalies by their AI-assessed severity level."""

    start_date: Annotated[object, PropertyInfo(alias="startDate")]
    """Start date for filtering results (inclusive, YYYY-MM-DD)."""

    status: Literal["New", "Under Review", "Escalated", "Dismissed", "Resolved"]
    """Filter anomalies by their current review status."""
