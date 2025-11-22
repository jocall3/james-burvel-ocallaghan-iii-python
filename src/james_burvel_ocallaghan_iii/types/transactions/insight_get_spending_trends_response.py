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
    ai_insights: List[AIInsight] = FieldInfo(alias="aiInsights")
    """AI-generated insights and actionable recommendations related to spending."""

    overall_trend: Literal["increasing", "decreasing", "stable"] = FieldInfo(alias="overallTrend")
    """Overall trend of spending."""

    percentage_change: float = FieldInfo(alias="percentageChange")
    """
    Percentage change in spending for the period (positive for increase, negative
    for decrease).
    """

    period: str
    """The period over which the spending trend is analyzed."""

    top_categories_by_change: List[TopCategoriesByChange] = FieldInfo(alias="topCategoriesByChange")
    """Categories with the most significant spending changes."""

    forecast_next_month: Optional[float] = FieldInfo(alias="forecastNextMonth", default=None)
    """AI's forecasted total spending for the next month."""
