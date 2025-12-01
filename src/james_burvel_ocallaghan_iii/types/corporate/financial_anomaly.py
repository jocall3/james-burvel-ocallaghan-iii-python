# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FinancialAnomaly"]


class FinancialAnomaly(BaseModel):
    id: object
    """Unique identifier for the detected anomaly."""

    ai_confidence_score: object = FieldInfo(alias="aiConfidenceScore")
    """AI's confidence in its detection of the anomaly (0-1)."""

    description: object
    """A brief summary of the anomaly."""

    entity_id: object = FieldInfo(alias="entityId")
    """
    The ID of the specific entity (e.g., transaction, user, card) the anomaly is
    linked to.
    """

    entity_type: Literal["PaymentOrder", "Transaction", "Counterparty", "CorporateCard", "User", "Invoice"] = FieldInfo(
        alias="entityType"
    )
    """The type of financial entity related to the anomaly."""

    recommended_action: object = FieldInfo(alias="recommendedAction")
    """AI-recommended immediate action to address the anomaly."""

    risk_score: object = FieldInfo(alias="riskScore")
    """AI-assigned risk score (0-100), higher is more risky."""

    severity: Literal["Low", "Medium", "High", "Critical"]
    """AI-assessed severity of the anomaly."""

    status: Literal["New", "Under Review", "Escalated", "Dismissed", "Resolved"]
    """Current review status of the anomaly."""

    timestamp: object
    """Timestamp when the anomaly was detected."""

    details: Optional[object] = None
    """Detailed context and reasoning behind the anomaly detection."""

    related_transactions: Optional[List[object]] = FieldInfo(alias="relatedTransactions", default=None)
    """List of IDs of other transactions or entities related to this anomaly."""

    resolution_notes: Optional[object] = FieldInfo(alias="resolutionNotes", default=None)
    """Notes recorded during the resolution or dismissal of the anomaly."""
