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

    remaining: float
    """Remaining amount in this category."""

    spent: float
    """Amount spent in this category."""


class Budget(BaseModel):
    id: str
    """Unique identifier for the budget."""

    categories: List[Category]
    """Breakdown of the budget by category."""

    end_date: date = FieldInfo(alias="endDate")
    """The end date of the current budget period."""

    name: str
    """Name of the budget."""

    period: Literal["weekly", "monthly", "quarterly", "annually", "custom"]
    """The recurrence period of the budget."""

    remaining_amount: float = FieldInfo(alias="remainingAmount")
    """The remaining amount in this budget period."""

    spent_amount: float = FieldInfo(alias="spentAmount")
    """The amount spent so far in this budget period."""

    start_date: date = FieldInfo(alias="startDate")
    """The start date of the current budget period."""

    status: Literal["active", "completed", "archived", "overspent"]
    """Current status of the budget."""

    total_amount: float = FieldInfo(alias="totalAmount")
    """The total allocated budget amount."""

    ai_recommendations: Optional[List[AIInsight]] = FieldInfo(alias="aiRecommendations", default=None)
    """AI-generated recommendations related to budget performance."""

    alert_threshold: Optional[int] = FieldInfo(alias="alertThreshold", default=None)
    """
    Percentage of budget spent at which an alert should be triggered (e.g., 80 for
    80% spent).
    """
