# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .ai_insight import AIInsight

__all__ = ["InsightGetSpendingTrendsResponse", "TopCategoriesByChange"]


class TopCategoriesByChange(BaseModel):
    absolute_change: Optional[float] = FieldInfo(alias="absoluteChange", default=None)
    """Absolute change in spending for this category."""

    category: Optional[str] = None
    """Category name."""

    percentage_change: Optional[float] = FieldInfo(alias="percentageChange", default=None)
    """Percentage change in spending for this category."""


class InsightGetSpendingTrendsResponse(BaseModel):
    ai_insights: List[AIInsight] = FieldInfo(alias="aiInsights")
    """AI-generated insights and alerts related to spending patterns."""

    overall_trend: Literal["increasing", "decreasing", "stable"] = FieldInfo(alias="overallTrend")
    """Overall spending trend for the period."""

    percentage_change: float = FieldInfo(alias="percentageChange")
    """
    Percentage change in overall spending compared to the previous equivalent
    period.
    """

    period: str
    """The period over which the spending trend is analyzed."""

    top_categories_by_change: List[TopCategoriesByChange] = FieldInfo(alias="topCategoriesByChange")
    """Categories with the most significant changes in spending."""

    forecast_next_month: Optional[float] = FieldInfo(alias="forecastNextMonth", default=None)
    """AI's projected total spending for the upcoming month."""
