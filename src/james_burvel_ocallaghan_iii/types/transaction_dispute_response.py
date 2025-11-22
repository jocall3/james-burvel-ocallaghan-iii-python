# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TransactionDisputeResponse"]


class TransactionDisputeResponse(BaseModel):
    dispute_id: str = FieldInfo(alias="disputeId")
    """Unique identifier for the dispute."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the dispute status was last updated."""

    status: Literal[
        "pending",
        "under_review",
        "investigation",
        "escalated",
        "resolved_in_favor_user",
        "resolved_in_favor_merchant",
        "rejected",
    ]
    """Current status of the dispute."""

    next_steps: Optional[str] = FieldInfo(alias="nextSteps", default=None)
    """Guidance on what to expect next or actions required from the user."""

    resolution_details: Optional[str] = FieldInfo(alias="resolutionDetails", default=None)
    """Details provided if the dispute has been resolved or rejected."""
