# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...transactions.ai_insight import AIInsight

__all__ = ["AuditRetrieveReportResponse", "Finding", "PeriodCovered"]


class Finding(BaseModel):
    description: Optional[str] = None

    related_entities: Optional[List[str]] = FieldInfo(alias="relatedEntities", default=None)

    severity: Optional[Literal["Low", "Medium", "High", "Critical"]] = None

    type: Optional[Literal["finding", "observation", "recommendation"]] = None


class PeriodCovered(BaseModel):
    end_date: Optional[date] = FieldInfo(alias="endDate", default=None)

    start_date: Optional[date] = FieldInfo(alias="startDate", default=None)


class AuditRetrieveReportResponse(BaseModel):
    audit_date: datetime = FieldInfo(alias="auditDate")
    """Date and time when the audit report was generated."""

    audit_id: str = FieldInfo(alias="auditId")
    """Unique identifier for the audit report."""

    findings: List[Finding]
    """Detailed findings, observations, and recommendations."""

    overall_compliance_score: int = FieldInfo(alias="overallComplianceScore")
    """An overall score (0-100) indicating the level of compliance."""

    period_covered: PeriodCovered = FieldInfo(alias="periodCovered")
    """The date range covered by the audit."""

    recommended_actions: List[AIInsight] = FieldInfo(alias="recommendedActions")
    """AI-generated actionable recommendations to improve compliance."""

    status: Literal["initiated", "processing", "completed", "failed"]
    """Current status of the audit generation."""

    summary: str
    """A high-level summary of the audit findings."""

    regulatory_adherence: Optional[Dict[str, str]] = FieldInfo(alias="regulatoryAdherence", default=None)
    """Specific adherence status for each regulatory framework audited."""
