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
    """Amount of each recurring payment."""

    category: str
    """Category of the recurring transaction."""

    currency: str
    """Currency of the recurring transaction."""

    description: str
    """Description of the recurring transaction."""

    frequency: Literal["daily", "weekly", "bi_weekly", "monthly", "quarterly", "semi_annually", "annually"]
    """Frequency of the recurring transaction."""

    next_due_date: date = FieldInfo(alias="nextDueDate")
    """Next scheduled payment date."""

    status: Literal["active", "paused", "cancelled", "completed"]
    """Current status of the recurring transaction."""

    ai_confidence_score: Optional[float] = FieldInfo(alias="aiConfidenceScore", default=None)
    """
    AI's confidence score (0-1) for its detection or categorization of this
    recurring pattern.
    """

    last_paid_date: Optional[date] = FieldInfo(alias="lastPaidDate", default=None)
    """Last date the transaction was paid."""

    linked_account_id: Optional[str] = FieldInfo(alias="linkedAccountId", default=None)
    """The account associated with this recurring transaction."""
