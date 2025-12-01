# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["KYCStatus"]


class KYCStatus(BaseModel):
    last_submission_date: Optional[datetime] = FieldInfo(alias="lastSubmissionDate", default=None)
    """Timestamp of the last KYC document submission."""

    overall_status: Literal["not_submitted", "in_review", "verified", "rejected", "requires_more_info"] = FieldInfo(
        alias="overallStatus"
    )
    """Overall status of the KYC verification process."""

    required_actions: List[str] = FieldInfo(alias="requiredActions")
    """List of actions required from the user if status is 'requires_more_info'."""

    user_id: str = FieldInfo(alias="userId")
    """The ID of the user whose KYC status is being retrieved."""

    rejection_reason: Optional[str] = FieldInfo(alias="rejectionReason", default=None)
    """Reason for rejection if status is 'rejected'."""

    verified_tier: Optional[Literal["bronze", "silver", "gold", "platinum"]] = FieldInfo(
        alias="verifiedTier", default=None
    )
    """The KYC verification tier achieved (e.g., for different service levels)."""
