# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["KYCStatus"]


class KYCStatus(BaseModel):
    last_submission_date: Optional[datetime] = FieldInfo(alias="lastSubmissionDate", default=None)
    """The timestamp of the last KYC document submission."""

    overall_status: Literal["not_submitted", "in_review", "verified", "rejected"] = FieldInfo(alias="overallStatus")
    """The overall status of the user's KYC verification."""

    user_id: str = FieldInfo(alias="userId")
    """The ID of the user whose KYC status is being retrieved."""

    rejection_reason: Optional[str] = FieldInfo(alias="rejectionReason", default=None)
    """If status is 'rejected', provides the reason for rejection."""

    required_actions: Optional[List[str]] = FieldInfo(alias="requiredActions", default=None)
    """A list of actions required from the user to proceed with KYC."""

    verified_tier: Optional[Literal["bronze", "silver", "gold", "platinum"]] = FieldInfo(
        alias="verifiedTier", default=None
    )
    """The tier of verification achieved (e.g., for different spending limits)."""
