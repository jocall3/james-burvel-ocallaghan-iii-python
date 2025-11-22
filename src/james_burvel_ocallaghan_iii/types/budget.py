# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .transactions.ai_insight import AIInsight

__all__ = ["Budget", "Category"]


class Category(BaseModel):
    allocated: float
    """Amount allocated to this category."""

    name: str
    """Name of the budget category."""

    progress_percentage: Optional[float] = FieldInfo(alias="progressPercentage", default=None)
    """Percentage of allocated amount spent."""

    remaining: Optional[float] = None
    """Remaining amount in this category."""

    spent: Optional[float] = None
    """Amount spent in this category."""


class Budget(BaseModel):
    id: str
    """Unique identifier for the budget."""

    end_date: date = FieldInfo(alias="endDate")
    """End date of the budget period."""

    name: str
    """Name of the budget."""

    period: Literal["weekly", "bi_weekly", "monthly", "quarterly", "annually", "custom"]
    """Recurrence period of the budget."""

    remaining_amount: float = FieldInfo(alias="remainingAmount")
    """Remaining amount in the budget."""

    spent_amount: float = FieldInfo(alias="spentAmount")
    """Amount spent so far in the current budget period."""

    start_date: date = FieldInfo(alias="startDate")
    """Start date of the budget period."""

    status: Literal["active", "completed", "upcoming", "archived"]
    """Current status of the budget."""

    total_amount: float = FieldInfo(alias="totalAmount")
    """Total allocated amount for the budget."""

    ai_recommendations: Optional[List[AIInsight]] = FieldInfo(alias="aiRecommendations", default=None)
    """AI-driven recommendations for budget optimization."""

    alert_threshold: Optional[int] = FieldInfo(alias="alertThreshold", default=None)
    """
    Percentage threshold at which an alert is triggered (e.g., 80% of budget spent).
    """

    categories: Optional[List[Category]] = None
    """Breakdown of the budget by categories."""
