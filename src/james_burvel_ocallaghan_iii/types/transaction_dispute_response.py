# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TransactionDisputeResponse"]


class TransactionDisputeResponse(BaseModel):
    dispute_id: str = FieldInfo(alias="disputeId")
    """Unique identifier for the dispute case."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the dispute status was last updated."""

    status: Literal["pending", "under_review", "accepted", "rejected", "resolved"]
    """Current status of the dispute."""

    next_steps: Optional[str] = FieldInfo(alias="nextSteps", default=None)
    """Guidance on what will happen next or what action the user needs to take."""

    rejection_reason: Optional[str] = FieldInfo(alias="rejectionReason", default=None)
    """If the dispute was rejected, the reason for rejection."""
