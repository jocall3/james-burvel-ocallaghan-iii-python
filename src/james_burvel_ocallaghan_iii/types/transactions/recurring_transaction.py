# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RecurringTransaction"]


class RecurringTransaction(BaseModel):
    id: str
    """Unique identifier for the recurring transaction."""

    amount: float
    """Amount of the recurring transaction."""

    category: str
    """Category of the recurring transaction."""

    currency: str
    """ISO 4217 currency code."""

    description: str
    """Description of the recurring transaction."""

    frequency: Literal["daily", "weekly", "bi_weekly", "monthly", "quarterly", "semi_annually", "annually"]
    """Frequency of the recurring transaction."""

    status: Literal["active", "inactive", "cancelled", "paused"]
    """Current status of the recurring transaction."""

    ai_confidence_score: Optional[float] = FieldInfo(alias="aiConfidenceScore", default=None)
    """AI confidence score that this is a recurring transaction (0-1)."""

    last_paid_date: Optional[date] = FieldInfo(alias="lastPaidDate", default=None)
    """Date of the last payment for this recurring transaction."""

    linked_account_id: Optional[str] = FieldInfo(alias="linkedAccountId", default=None)
    """ID of the account typically used for this recurring transaction."""

    next_due_date: Optional[date] = FieldInfo(alias="nextDueDate", default=None)
    """Next scheduled due date for the transaction."""
