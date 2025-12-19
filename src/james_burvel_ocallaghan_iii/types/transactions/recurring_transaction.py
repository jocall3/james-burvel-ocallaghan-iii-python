# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RecurringTransaction"]


class RecurringTransaction(BaseModel):
    """Details of a detected or user-defined recurring transaction."""

    id: object
    """Unique identifier for the recurring transaction."""

    amount: object
    """Amount of the recurring transaction."""

    category: object
    """Category of the recurring transaction."""

    currency: object
    """ISO 4217 currency code."""

    description: object
    """Description of the recurring transaction."""

    frequency: Literal["daily", "weekly", "bi_weekly", "monthly", "quarterly", "semi_annually", "annually"]
    """Frequency of the recurring transaction."""

    status: Literal["active", "inactive", "cancelled", "paused"]
    """Current status of the recurring transaction."""

    ai_confidence_score: Optional[object] = FieldInfo(alias="aiConfidenceScore", default=None)
    """AI confidence score that this is a recurring transaction (0-1)."""

    last_paid_date: Optional[object] = FieldInfo(alias="lastPaidDate", default=None)
    """Date of the last payment for this recurring transaction."""

    linked_account_id: Optional[object] = FieldInfo(alias="linkedAccountId", default=None)
    """ID of the account typically used for this recurring transaction."""

    next_due_date: Optional[object] = FieldInfo(alias="nextDueDate", default=None)
    """Next scheduled due date for the transaction."""
