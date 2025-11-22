# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...transactions.ai_insight import AIInsight

__all__ = ["AuditRetrieveReportResponse", "Finding", "PeriodCovered"]


class Finding(BaseModel):
    description: str
    """Detailed description of the finding."""

    severity: Literal["Low", "Medium", "High", "Critical"]
    """Severity of the finding."""

    type: Literal["observation", "recommendation", "potential_violation"]
    """Type of finding (e.g., observation, recommendation)."""

    ai_score: Optional[float] = FieldInfo(alias="aiScore", default=None)
    """AI's confidence score or relevance score for this finding."""

    regulatory_reference: Optional[str] = FieldInfo(alias="regulatoryReference", default=None)
    """Reference to specific regulatory requirement, if applicable."""

    related_entities: Optional[List[str]] = FieldInfo(alias="relatedEntities", default=None)
    """List of IDs of entities (transactions, cards, etc.) related to this finding."""


class PeriodCovered(BaseModel):
    end_date: date = FieldInfo(alias="endDate")
    """End date of the audit period."""

    start_date: date = FieldInfo(alias="startDate")
    """Start date of the audit period."""


class AuditRetrieveReportResponse(BaseModel):
    audit_date: datetime = FieldInfo(alias="auditDate")
    """Date when the audit report was generated."""

    audit_id: str = FieldInfo(alias="auditId")
    """Unique identifier for the compliance audit."""

    findings: List[Finding]
    """
    Detailed list of findings, including observations, recommendations, and
    potential violations.
    """

    overall_compliance_score: int = FieldInfo(alias="overallComplianceScore")
    """Overall compliance score (0-100), indicating adherence to rules."""

    period_covered: PeriodCovered = FieldInfo(alias="periodCovered")
    """The date range covered by the audit."""

    status: Literal["initiated", "processing", "completed", "failed"]
    """Current status of the audit."""

    summary: str
    """A summary of the audit findings."""

    recommended_actions: Optional[List[AIInsight]] = FieldInfo(alias="recommendedActions", default=None)
    """AI-generated actionable recommendations to improve compliance."""
