# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .ai_insight import AIInsight

__all__ = ["InsightGetSpendingTrendsResponse", "TopCategoriesByChange"]


class TopCategoriesByChange(BaseModel):
    absolute_change: Optional[float] = FieldInfo(alias="absoluteChange", default=None)

    category: Optional[str] = None

    percentage_change: Optional[float] = FieldInfo(alias="percentageChange", default=None)


class InsightGetSpendingTrendsResponse(BaseModel):
    overall_trend: Literal["increasing", "decreasing", "stable"] = FieldInfo(alias="overallTrend")
    """Overall trend in spending."""

    percentage_change: float = FieldInfo(alias="percentageChange")
    """Percentage change in spending over the period."""

    period: str
    """The period over which the spending trend is analyzed."""

    ai_insights: Optional[List[AIInsight]] = FieldInfo(alias="aiInsights", default=None)
    """AI-driven insights and recommendations related to spending."""

    forecast_next_month: Optional[float] = FieldInfo(alias="forecastNextMonth", default=None)
    """AI's forecast for total spending in the next month."""

    top_categories_by_change: Optional[List[TopCategoriesByChange]] = FieldInfo(
        alias="topCategoriesByChange", default=None
    )
    """Top categories with significant spending changes."""
