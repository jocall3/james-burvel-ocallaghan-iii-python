# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...transactions.ai_insight import AIInsight

__all__ = ["AuditRetrieveReportResponse", "Finding", "PeriodCovered"]


class Finding(BaseModel):
    description: Optional[object] = None

    related_entities: Optional[List[object]] = FieldInfo(alias="relatedEntities", default=None)
    """IDs of entities related to this finding (e.g., transaction IDs)."""

    severity: Optional[Literal["Low", "Medium", "High", "Critical"]] = None

    type: Optional[Literal["finding", "observation", "recommendation"]] = None


class PeriodCovered(BaseModel):
    end_date: Optional[object] = FieldInfo(alias="endDate", default=None)

    start_date: Optional[object] = FieldInfo(alias="startDate", default=None)


class AuditRetrieveReportResponse(BaseModel):
    audit_date: object = FieldInfo(alias="auditDate")
    """Timestamp when the audit report was generated."""

    audit_id: object = FieldInfo(alias="auditId")
    """Unique identifier for the compliance audit."""

    findings: List[Finding]
    """Detailed findings, observations, and recommendations."""

    overall_compliance_score: object = FieldInfo(alias="overallComplianceScore")
    """Overall compliance score (0-100), higher is better."""

    period_covered: PeriodCovered = FieldInfo(alias="periodCovered")
    """The period covered by this audit report."""

    recommended_actions: List[AIInsight] = FieldInfo(alias="recommendedActions")
    """AI-generated actionable recommendations to improve compliance."""

    status: Literal["processing", "completed", "failed"]
    """Current status of the audit."""

    summary: object
    """A high-level summary of the audit findings."""
