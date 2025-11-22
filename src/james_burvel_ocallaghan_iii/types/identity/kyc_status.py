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

    overall_status: Literal["not_started", "in_review", "verified", "rejected", "requires_action"] = FieldInfo(
        alias="overallStatus"
    )
    """Overall status of the KYC verification process."""

    user_id: str = FieldInfo(alias="userId")
    """Unique identifier for the user."""

    rejection_reason: Optional[str] = FieldInfo(alias="rejectionReason", default=None)
    """Reason for rejection if the status is 'rejected'."""

    required_actions: Optional[List[str]] = FieldInfo(alias="requiredActions", default=None)
    """List of actions required from the user to proceed with verification."""

    verified_tier: Optional[Literal["bronze", "silver", "gold", "platinum"]] = FieldInfo(
        alias="verifiedTier", default=None
    )
    """The tier of verification achieved, granting access to different service levels."""
