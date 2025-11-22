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

    status: Literal["pending", "under_review", "escalated", "resolved", "rejected"]
    """Current status of the dispute."""

    next_steps: Optional[str] = FieldInfo(alias="nextSteps", default=None)
    """Actionable next steps for the user or expected timeline."""

    resolution_details: Optional[str] = FieldInfo(alias="resolutionDetails", default=None)
    """Details provided upon resolution or rejection of the dispute."""
