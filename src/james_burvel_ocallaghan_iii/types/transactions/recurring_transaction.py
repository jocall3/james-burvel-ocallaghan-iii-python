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
    """The amount of each recurring transaction."""

    category: str
    """Category of the recurring transaction."""

    currency: str
    """The currency of the recurring transaction."""

    description: str
    """Description of the recurring transaction."""

    frequency: Literal["daily", "weekly", "bi-weekly", "monthly", "quarterly", "annually"]
    """How often the transaction occurs."""

    next_due_date: Optional[date] = FieldInfo(alias="nextDueDate", default=None)
    """The next expected date for this transaction to occur."""

    status: Literal["active", "paused", "cancelled", "completed"]
    """Current status of the recurring transaction."""

    ai_confidence_score: Optional[float] = FieldInfo(alias="aiConfidenceScore", default=None)
    """AI's confidence score (0-1) that this is indeed a recurring transaction."""

    last_paid_date: Optional[date] = FieldInfo(alias="lastPaidDate", default=None)
    """The date the last recurring payment was made."""

    linked_account_id: Optional[str] = FieldInfo(alias="linkedAccountId", default=None)
    """The ID of the account from which this recurring transaction typically occurs."""
