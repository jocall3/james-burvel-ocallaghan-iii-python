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
    """Typical amount of the recurring transaction."""

    category: str
    """Category of the recurring transaction."""

    currency: str
    """Currency of the transaction."""

    description: str
    """Description of the recurring transaction."""

    frequency: Literal["daily", "weekly", "bi_weekly", "monthly", "quarterly", "semi_annually", "annually"]
    """How often the transaction occurs."""

    next_due_date: Optional[date] = FieldInfo(alias="nextDueDate", default=None)
    """The next expected date for this recurring transaction."""

    status: Literal["active", "inactive", "cancelled"]
    """Current status of the recurring transaction."""

    ai_confidence_score: Optional[float] = FieldInfo(alias="aiConfidenceScore", default=None)
    """AI's confidence in accurately identifying this as a recurring transaction."""

    last_paid_date: Optional[date] = FieldInfo(alias="lastPaidDate", default=None)
    """The date the last recurring transaction occurred."""

    linked_account_id: Optional[str] = FieldInfo(alias="linkedAccountId", default=None)
    """
    Optional: The account from which this recurring transaction is typically paid or
    received.
    """
