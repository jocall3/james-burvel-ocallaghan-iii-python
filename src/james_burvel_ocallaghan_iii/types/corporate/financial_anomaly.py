# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FinancialAnomaly"]


class FinancialAnomaly(BaseModel):
    id: str
    """Unique identifier for the detected anomaly."""

    ai_confidence_score: float = FieldInfo(alias="aiConfidenceScore")
    """AI's confidence in the detection and classification of this anomaly."""

    description: str
    """A brief, human-readable description of the anomaly."""

    entity_id: str = FieldInfo(alias="entityId")
    """The ID of the primary entity related to this anomaly."""

    entity_type: Literal[
        "PaymentOrder", "Transaction", "Counterparty", "CorporateCard", "Invoice", "User", "System"
    ] = FieldInfo(alias="entityType")
    """The type of financial entity this anomaly is related to."""

    risk_score: int = FieldInfo(alias="riskScore")
    """AI-calculated risk score (0-100) for this anomaly."""

    severity: Literal["Low", "Medium", "High", "Critical"]
    """AI-assessed severity level of the anomaly."""

    status: Literal["New", "Under Review", "Escalated", "Dismissed", "Resolved"]
    """Current review status of the anomaly."""

    timestamp: datetime
    """Timestamp when the anomaly was detected."""

    details: Optional[str] = None
    """Detailed explanation of the anomaly, including relevant context."""

    recommended_action: Optional[str] = FieldInfo(alias="recommendedAction", default=None)
    """AI-suggested immediate action for the anomaly."""

    related_transactions: Optional[List[str]] = FieldInfo(alias="relatedTransactions", default=None)
    """List of IDs of other transactions or entities related to this anomaly."""

    resolution_notes: Optional[str] = FieldInfo(alias="resolutionNotes", default=None)
    """Notes added by a compliance officer upon resolving or dismissing the anomaly."""
