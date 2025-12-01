# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CorporatePerformSanctionScreeningResponse", "MatchDetail"]


class MatchDetail(BaseModel):
    list_name: Optional[object] = FieldInfo(alias="listName", default=None)
    """Name of the sanction list where a match was found."""

    matched_name: Optional[object] = FieldInfo(alias="matchedName", default=None)
    """The name on the sanction list that matched."""

    public_url: Optional[object] = FieldInfo(alias="publicUrl", default=None)
    """Optional: URL to public record of the sanction list entry."""

    reason: Optional[object] = None
    """Reason for the match (e.g., exact name, alias, partial match)."""

    score: Optional[object] = None
    """Match confidence score (0-1)."""


class CorporatePerformSanctionScreeningResponse(BaseModel):
    match_details: List[MatchDetail] = FieldInfo(alias="matchDetails")
    """Details of any potential or exact matches found."""

    match_found: object = FieldInfo(alias="matchFound")
    """True if any potential matches were found on sanction lists."""

    screening_id: object = FieldInfo(alias="screeningId")
    """Unique identifier for this screening operation."""

    screening_timestamp: object = FieldInfo(alias="screeningTimestamp")
    """Timestamp when the screening was performed."""

    status: Literal["clear", "potential_match", "confirmed_match", "error"]
    """Overall status of the screening result."""

    message: Optional[object] = None
    """An optional message providing more context on the status."""
