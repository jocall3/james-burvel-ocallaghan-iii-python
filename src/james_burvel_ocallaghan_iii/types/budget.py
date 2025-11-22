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
    """Amount spent in this category so far."""


class Budget(BaseModel):
    id: str
    """Unique identifier for the budget."""

    alert_threshold: int = FieldInfo(alias="alertThreshold")
    """Percentage threshold at which an alert is triggered (e.g., 80% spent)."""

    categories: List[Category]
    """Breakdown of the budget by categories."""

    end_date: date = FieldInfo(alias="endDate")
    """End date of the budget period."""

    name: str
    """Name of the budget."""

    period: Literal["weekly", "bi_weekly", "monthly", "quarterly", "annually", "custom"]
    """The frequency or period of the budget."""

    remaining_amount: float = FieldInfo(alias="remainingAmount")
    """Remaining amount in the budget."""

    spent_amount: float = FieldInfo(alias="spentAmount")
    """Total amount spent against this budget so far."""

    start_date: date = FieldInfo(alias="startDate")
    """Start date of the budget period."""

    status: Literal["active", "archived", "ended"]
    """Current status of the budget."""

    total_amount: float = FieldInfo(alias="totalAmount")
    """Total amount allocated for the entire budget."""

    ai_recommendations: Optional[List[AIInsight]] = FieldInfo(alias="aiRecommendations", default=None)
    """AI-driven recommendations related to this budget."""
