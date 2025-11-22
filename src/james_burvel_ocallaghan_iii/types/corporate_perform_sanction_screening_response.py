# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CorporatePerformSanctionScreeningResponse", "MatchDetail"]


class MatchDetail(BaseModel):
    list_name: str = FieldInfo(alias="listName")
    """The name of the sanction list where a match was found."""

    matched_name: str = FieldInfo(alias="matchedName")
    """The name of the entry on the sanction list that matched."""

    reason: str
    """Reason for the potential match."""

    score: float
    """Match score (0-1), indicating confidence of the match."""


class CorporatePerformSanctionScreeningResponse(BaseModel):
    match_found: bool = FieldInfo(alias="matchFound")
    """True if any potential matches were found on sanction lists."""

    screening_id: str = FieldInfo(alias="screeningId")
    """Unique identifier for this screening request."""

    screening_timestamp: datetime = FieldInfo(alias="screeningTimestamp")
    """Timestamp when the screening was performed."""

    status: Literal["clear", "potential_match", "confirmed_match", "error"]
    """Overall status of the screening result."""

    ai_confidence_score: Optional[float] = FieldInfo(alias="aiConfidenceScore", default=None)
    """AI's confidence (0-1) in the accuracy of the screening result."""

    match_details: Optional[List[MatchDetail]] = FieldInfo(alias="matchDetails", default=None)
    """Details of any potential matches found."""
