# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

    next_steps: str = FieldInfo(alias="nextSteps")
    """Guidance on what to expect next in the dispute process."""

    status: Literal["pending", "under_review", "requires_more_info", "resolved", "rejected"]
    """Current status of the dispute."""
