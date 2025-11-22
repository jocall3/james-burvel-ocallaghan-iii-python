# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CorporatePerformSanctionScreeningResponse", "MatchDetail"]


class MatchDetail(BaseModel):
    additional_info: Optional[object] = FieldInfo(alias="additionalInfo", default=None)
    """Additional data from the sanctions list entry."""

    list_name: Optional[str] = FieldInfo(alias="listName", default=None)

    matched_name: Optional[str] = FieldInfo(alias="matchedName", default=None)

    reason: Optional[str] = None

    score: Optional[float] = None


class CorporatePerformSanctionScreeningResponse(BaseModel):
    match_found: bool = FieldInfo(alias="matchFound")
    """True if any potential matches were found, false otherwise."""

    screening_id: str = FieldInfo(alias="screeningId")
    """Unique identifier for this screening operation."""

    screening_timestamp: datetime = FieldInfo(alias="screeningTimestamp")
    """Timestamp when the screening was performed."""

    status: Literal["clear", "potential_match", "confirmed_match", "error"]
    """Overall status of the sanction screening."""

    ai_risk_score: Optional[int] = FieldInfo(alias="aiRiskScore", default=None)
    """AI-calculated risk score (0-100) based on screening results."""

    match_details: Optional[List[MatchDetail]] = FieldInfo(alias="matchDetails", default=None)
    """Details of any potential matches found during screening."""
