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
    """AI's confidence score (0-1) in the anomaly detection."""

    description: str
    """A concise summary of the anomaly."""

    entity_id: str = FieldInfo(alias="entityId")
    """
    The ID of the specific entity (e.g., transaction ID, user ID) related to the
    anomaly.
    """

    entity_type: Literal[
        "PaymentOrder", "Transaction", "Counterparty", "CorporateCard", "Invoice", "User", "Account"
    ] = FieldInfo(alias="entityType")
    """The type of financial entity or activity the anomaly relates to."""

    risk_score: int = FieldInfo(alias="riskScore")
    """AI-calculated risk score (0-100) for the anomaly."""

    severity: Literal["Low", "Medium", "High", "Critical"]
    """AI-assessed severity level of the anomaly."""

    status: Literal["New", "Under Review", "Escalated", "Dismissed", "Resolved"]
    """Current review status of the anomaly."""

    timestamp: datetime
    """Timestamp when the anomaly was detected."""

    details: Optional[str] = None
    """Detailed description of the anomaly, including contributing factors."""

    recommended_action: Optional[str] = FieldInfo(alias="recommendedAction", default=None)
    """AI-recommended immediate action to address the anomaly."""

    related_transactions: Optional[List[str]] = FieldInfo(alias="relatedTransactions", default=None)
    """List of IDs of other transactions potentially related to this anomaly."""

    resolution_notes: Optional[str] = FieldInfo(alias="resolutionNotes", default=None)
    """
    Notes provided by an analyst or the AI upon resolving or dismissing the anomaly.
    """
