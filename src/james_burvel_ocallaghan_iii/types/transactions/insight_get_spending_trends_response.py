# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .ai_insight import AIInsight

__all__ = ["InsightGetSpendingTrendsResponse", "TopCategoriesByChange"]


class TopCategoriesByChange(BaseModel):
    absolute_change: Optional[object] = FieldInfo(alias="absoluteChange", default=None)

    category: Optional[object] = None

    percentage_change: Optional[object] = FieldInfo(alias="percentageChange", default=None)


class InsightGetSpendingTrendsResponse(BaseModel):
    ai_insights: List[AIInsight] = FieldInfo(alias="aiInsights")
    """AI-driven insights and recommendations related to spending."""

    forecast_next_month: object = FieldInfo(alias="forecastNextMonth")
    """AI-projected total spending for the next month."""

    overall_trend: Literal["increasing", "decreasing", "stable"] = FieldInfo(alias="overallTrend")
    """Overall trend of spending (increasing, decreasing, stable)."""

    percentage_change: object = FieldInfo(alias="percentageChange")
    """Percentage change in spending over the period."""

    period: object
    """The period over which the spending trend is analyzed."""

    top_categories_by_change: List[TopCategoriesByChange] = FieldInfo(alias="topCategoriesByChange")
    """Categories with the most significant changes in spending."""
