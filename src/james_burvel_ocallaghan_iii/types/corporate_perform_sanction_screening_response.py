# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CorporatePerformSanctionScreeningResponse", "MatchDetail"]


class MatchDetail(BaseModel):
    additional_info: Optional[str] = FieldInfo(alias="additionalInfo", default=None)

    list_name: Optional[str] = FieldInfo(alias="listName", default=None)

    matched_name: Optional[str] = FieldInfo(alias="matchedName", default=None)

    reason: Optional[str] = None

    score: Optional[float] = None


class CorporatePerformSanctionScreeningResponse(BaseModel):
    match_found: bool = FieldInfo(alias="matchFound")
    """True if a potential match was found on any sanction list."""

    screening_id: str = FieldInfo(alias="screeningId")
    """Unique identifier for this screening request."""

    screening_timestamp: datetime = FieldInfo(alias="screeningTimestamp")
    """Timestamp when the screening was performed."""

    status: Literal["clear", "potential_match", "high_match", "error"]
    """Overall status of the screening result."""

    ai_recommendation: Optional[str] = FieldInfo(alias="aiRecommendation", default=None)
    """AI-generated recommendation based on the screening result."""

    ai_risk_score: Optional[int] = FieldInfo(alias="aiRiskScore", default=None)
    """AI-calculated risk score for the screened entity (0-100)."""

    match_details: Optional[List[MatchDetail]] = FieldInfo(alias="matchDetails", default=None)
    """Details of any potential matches found."""
